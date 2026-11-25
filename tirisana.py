import pandas as pd

df = pd.read_csv("dati/ai4i2020.csv")

print("Rindu skaits sākumā:", len(df))

# Noņem dublikātus, lai viens ieraksts netiktu izmantots vairākas reizes.

df = df.drop_duplicates()

# Noņem rindas ar tukšām vērtībām, jo modelim nepieciešami pilni dati.

df = df.dropna()

print("Rindu skaits beigās:", len(df))

df.to_csv("tirs.csv", index=False)

