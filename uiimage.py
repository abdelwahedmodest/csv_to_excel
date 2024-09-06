import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage
import pandas as pd

def convert_csv_to_excel():
    # Ouvrir une boîte de dialogue pour sélectionner le fichier CSV
    csv_file_path = filedialog.askopenfilename(
        title="Sélectionnez un fichier CSV",
        filetypes=[("CSV files", "*.csv")]
    )
    
    if not csv_file_path:
        return  # L'utilisateur a annulé la sélection

    try:
        # Lire le fichier CSV
        df = pd.read_csv(csv_file_path)

        # Ouvrir une boîte de dialogue pour choisir où enregistrer le fichier Excel
        excel_file_path = filedialog.asksaveasfilename(
            title="Enregistrer le fichier Excel",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")]
        )
        
        if not excel_file_path:
            return  # L'utilisateur a annulé l'enregistrement
        
        # Convertir et sauvegarder en fichier Excel
        df.to_excel(excel_file_path, index=False, engine='openpyxl')

        # Informer l'utilisateur que la conversion est terminée
        messagebox.showinfo("Succès", "Le fichier a été converti avec succès !")
    except Exception as e:
        # En cas d'erreur, afficher un message d'erreur
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur CSV en Excel")

# Charger l'image
image_path = "st.png"  # Remplacez par le chemin vers votre image
img = PhotoImage(file=image_path)

# Ajouter une étiquette avec l'image
image_label = tk.Label(root, image=img)
image_label.pack(padx=20, pady=10)

# Ajouter un bouton pour lancer la conversion
convert_button = tk.Button(root, text="Convertir CSV en Excel", command=convert_csv_to_excel)
convert_button.pack(padx=20, pady=20)

# Lancer l'application Tkinter
root.mainloop()
