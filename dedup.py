import pandas as pd
import numpy as np
from rapidfuzz import fuzz

# Încarc fișierul Parquet
df = pd.read_parquet("veridion_product_deduplication_challenge.snappy.parquet")

# Afișez primele 5 rânduri
print("\n📦 Primele produse din dataset:")
print(df.head())

# Afișez toate coloanele disponibile
print("\n🧠 Coloane disponibile:")
print(df.columns)

# Normalizare titluri
df["title_clean"] = df["product_title"].fillna("").str.lower().str.strip()

# Threshold pentru fuzzy matching
threshold = 90

# Grupuri de duplicate
groups = []
seen = set()

print(f"\n🔍 Începem deduplicarea pe {len(df)} produse...\n")

for i, row in df.iterrows():
    if i in seen:
        continue

    title = row["title_clean"]

    # Progres pas cu pas
    print(f"🔎 Compar {i+1}/{len(df)}", end="\r")

    # Optimizare: nu mai comparăm cu toate, ci doar cu titluri care încep cu aceeași literă (am avut probleme cu codul si dura prea mult)
    matches = df[df.index != i].copy()
    matches = matches[matches["title_clean"].str[0:1] == title[0:1]]

    # Calculează scorul de similaritate
    matches["score"] = matches["title_clean"].apply(lambda x: fuzz.token_sort_ratio(title, x))
    dupes = matches[matches["score"] >= threshold]

    # Dacă sunt duplicate, grupăm
    group = [i] + list(dupes.index)
    groups.append(group)
    seen.update(group)

print(f"\n📚 Grupuri găsite: {len(groups)}")

# Consolidare grupuri într-un singur rând
consolidated = []

for group in groups:
    group_rows = df.loc[group]
    combined = {}
    for col in df.columns:
        if col == "title_clean":
            continue
        values = group_rows[col].dropna().astype(str)
        if not values.empty:
            combined[col] = max(values, key=len)
        else:
            combined[col] = np.nan
    consolidated.append(combined)

# DataFrame final
final_df = pd.DataFrame(consolidated)

# Afișează rezultat
print("\n📊 Nr. de rânduri în rezultat:", len(final_df))

# Salvează doar dacă există
if len(final_df) > 0:
    final_df.to_csv("deduplicated_products.csv", index=False, encoding="utf-8")
    print("✅ Fișier salvat: deduplicated_products.csv")
else:
    print("⚠️  Nu s-au găsit produse duplicate.")
