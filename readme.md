# Veridion - Product Deduplication Challenge

> Consolidarea intrarilor duplicate intr-un singur rand de produs, maximizand informatia si pastrand unicitatea.

---

## Scopul taskului

Datasetul contine descrieri partiale ale produselor, extrase automat de pe diferite pagini web. Fiecare produs poate aparea de mai multe ori, cu campuri incomplete sau variabile.

 Obiectivul:  
- Identifica duplicatele (acelasi produs, descris diferit)
- Combina-le intr-o **singura inregistrare completa**
- Exporteaza rezultatul intr-un fisier `.csv` curat, cu un rand per produs

---


### Ce am vrut sa obtin:

- O solutie **corecta** care identifica duplicatele chiar daca sunt scrise diferit
- Un mod de a **combina eficient** informatia intre randuri
- Performanta rezonabila chiar si pe ~20.000 de produse
- Un cod **curat, documentat si usor de extins**

#### Intrebari pe care mi le-am pus:

- Ce defineste un produs "identic"? E suficient titlul?
- Cum decid ce date pastrez dintre duplicate?
- Cum evit sa compar fiecare rand cu toate celelalte (comparatie O(n²))?
- Cum dau feedback vizual ca scriptul functioneaza (fiind foarte multe produse nu stiam daca codul functioneaza si dura destul de mult sa astept sa vad daca mi se genereaza fisierul)?

---

##### Cum se ruleaza:
-Instalare dependinte("pip install pandas pyarrow rapidfuzz numpy")
-Rulare script("python3 dedup.py")


###### Ce contine folderul:
veridion_dedup/
─ dedup.py                        # Codul principal
─ veridion_product_...parquet     # Fisierul sursa
─ deduplicated_products.csv       # Fisierul rezultat
─ README.md                       # Documentatia

Multumesc pentru oportunitate si pentru un task interesant!
