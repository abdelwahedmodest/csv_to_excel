import pandas as pd

# Chemin vers le fichier CSV
csv_file_path = 'animals.csv'

# Chemin vers le fichier Excel de sortie
excel_file_path = 'animals.xlsx'

# Lire le fichier CSV
df = pd.read_csv(csv_file_path)

# Convertir et sauvegarder en fichier Excel
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Conversion terminée ! Le fichier Excel est enregistré à : {excel_file_path}")
