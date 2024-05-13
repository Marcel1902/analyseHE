import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from PIL import Image, ImageTk
    
fenetre_accueil = tk.Tk()
fenetre_accueil.title("Page d'accueil")
fenetre_accueil.iconbitmap("graduate.ico")
fenetre_accueil.geometry("580x520")

# Création d'un cadre pour contenir les images
cadre_images = tk.Frame(fenetre_accueil)
cadre_images.pack(side="top", padx=10, pady=10)

# Redimensionner et convertir les images en format Tkinter PhotoImage
logo1 = ImageTk.PhotoImage(Image.open("logo_imra.png").resize((100, 100)))
logo2 = ImageTk.PhotoImage(Image.open("logo_ispm.png").resize((100, 100)))
logo3 = ImageTk.PhotoImage(Image.open("logo-cnre.png").resize((100, 100)))

# Afficher les images dans des labels
image1 = tk.Label(cadre_images, image=logo1)
image1.pack(side="left", padx=(20, 60), pady=(0, 0))

image2 = tk.Label(cadre_images, image=logo2)
image2.pack(side="left", padx=(20, 60), pady=(0, 0))

image3 = tk.Label(cadre_images, image=logo3)
image3.pack(side="left", padx=(20, 60), pady=(0, 0))

# Labels et boutons de la fenêtre d'accueil
label_message = tk.Label(fenetre_accueil, text="ANALYSES QUALITATIVES ET ACTIVITES BIOLOGIQUE DU HE", font=("Arial", 13, "bold"), fg="#025c02")
label_message.pack(pady=20)   

def ouvrir_fenetre_principale():
    fenetre_accueil.destroy()
    
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Institut Superieure Polytechnique de Madagascar")
    root.iconbitmap("logo_ispm.ico")
    root.geometry("580x520")

    #création du titre
    label_densite = tk.Label(root, text="ANALYSE QUALITATIVES DU HE", font=("Arial", 16, "bold"), fg="#025c02")
    label_densite.grid(row=0, column=0, columnspan=7, padx=30, pady=(5, 10), sticky="n")

    # Création des libellés et des champs de saisie
    label_densite = tk.Label(root, text="Densité relative :")
    label_densite.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    entre_densite = tk.Entry(root, width=25)
    entre_densite.grid(row=2, column=1, padx=10, pady=5)

    label_indice_refraction = tk.Label(root, text="Indice de réfraction :")
    label_indice_refraction.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    entre_indice_refraction = tk.Entry(root, width=25)
    entre_indice_refraction.grid(row=3, column=1, padx=10, pady=5)

    label_indice_acide = tk.Label(root, text="Indice d'acide :")
    label_indice_acide.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    entre_indice_acide = tk.Entry(root, width=25)
    entre_indice_acide.grid(row=4, column=1, padx=10, pady=5)

    label_indice_ester = tk.Label(root, text="Indice d'ester :")
    label_indice_ester.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    entre_indice_ester = tk.Entry(root, width=25)
    entre_indice_ester.grid(row=5, column=1, padx=10, pady=5)

    # Titre pour les interprétations
    label_titre_interpretation = tk.Label(root, text="Interprétations", font=("Arial", 12, "bold"))
    label_titre_interpretation.grid(row=1, column=3, columnspan=2, padx=10, pady=5, sticky="n")

    # Labels pour les interprétations
    label_interpretation_densite = tk.Label(root, text="", fg="blue")
    label_interpretation_densite.grid(row=2, column=2, columnspan=2, padx=10, pady=5, sticky="w")

    label_interpretation_refraction = tk.Label(root, text="", fg="blue")
    label_interpretation_refraction.grid(row=3, column=2, columnspan=2, padx=10, pady=5, sticky="w")

    label_interpretation_acide = tk.Label(root, text="", fg="blue")
    label_interpretation_acide.grid(row=4, column=2, columnspan=2, padx=10, pady=5, sticky="w")

    label_interpretation_ester = tk.Label(root, text="", fg="blue")
    label_interpretation_ester.grid(row=5, column=2, columnspan=2, padx=10, pady=5, sticky="w")
    
    # Fonction pour calculer et afficher les résultats
    def calculer_resultats():
        # Récupérer les valeurs saisies par l'utilisateur en tant que chaînes de caractères
        densite_relative_str = entre_densite.get()
        indice_refraction_str = entre_indice_refraction.get()
        indice_acide_str = entre_indice_acide.get()
        indice_ester_str = entre_indice_ester.get()

        # Vérification si les champs sont vides
        if densite_relative_str == "":
            messagebox.showwarning("Champ vide", "Veuillez saisir la densité relative.")
            return  # Arrêter la fonction si le champ est vide

        if indice_refraction_str == "":
            messagebox.showwarning("Champ vide", "Veuillez saisir l'indice de réfraction.")
            return

        if indice_acide_str == "":
            messagebox.showwarning("Champ vide", "Veuillez saisir l'indice d'acide.")
            return

        if indice_ester_str == "":
            messagebox.showwarning("Champ vide", "Veuillez saisir l'indice d'ester.")
            return

        # Convertir les valeurs en nombres flottants
        try:
            densite_relative = float(densite_relative_str)
            indice_refraction = float(indice_refraction_str)
            indice_acide = float(indice_acide_str)
            indice_ester = float(indice_ester_str)
        except ValueError:  # Si une exception se produit lors de la conversion
            messagebox.showwarning("Valeur incorrecte", "Veuillez saisir des nombres valides.")
            return  # Arrêter la fonction en cas d'erreur

        # Interprétation des indices
        interpretation_densite = "L'huile essentielle est dense."
        if densite_relative < 0.999:
            interpretation_densite = "L'huile essentielle est legère."
        label_interpretation_densite.config(text=interpretation_densite)

        interpretation_refraction = "L'huile essentielle est impure."
        if indice_refraction > 1.3333:
            interpretation_refraction = "L'huile essentielle est pure."
        label_interpretation_refraction.config(text=interpretation_refraction)

        interpretation_acide = "L'huile essentielle est moins conservatrice."
        if indice_acide < 2:
            interpretation_acide = "L'huile essentielle est conservatrice."
        label_interpretation_acide.config(text=interpretation_acide)

        interpretation_ester = "L'huile essentielle est qualité inférieure."
        if indice_ester > 22:
            interpretation_ester = "L'huile essentielle est de bonne qualité."
        label_interpretation_ester.config(text=interpretation_ester)
        
    def reinitialiser():
        entre_densite.delete(0, tk.END)
        entre_indice_refraction.delete(0, tk.END)
        entre_indice_acide.delete(0, tk.END)
        entre_indice_ester.delete(0, tk.END)
        label_interpretation_densite.config(text="")
        label_interpretation_refraction.config(text="")
        label_interpretation_acide.config(text="")
        label_interpretation_ester.config(text="")

    # Création du bouton pour afficher les interprétations
    bouton_interpretation = tk.Button(root, text="Executer", command=calculer_resultats, width=10, font=("Helvetica", 12, "bold"))
    bouton_interpretation.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

    bouton_nouveau = tk.Button(root, text="Nouveau", command=reinitialiser, width=10, font=("Helvetica", 12, "bold"))
    bouton_nouveau.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

    separator = ttk.Separator(root, orient='horizontal' )
    separator.grid(row=7, columnspan=3, sticky="ew", pady=10)

    #création du titre
    label_densite = tk.Label(root, text="ACTIVITES BIOLOGIQUE DU HE", font=("Arial", 16, "bold"), fg="#025c02")
    label_densite.grid(row=8, column=0, columnspan=7, padx=30, pady=(5, 10), sticky="n")

    # Titre pour l'interprétation
    label_titre_interpretation = tk.Label(root, text="Interprétation", font=("Arial", 12, "bold"))
    label_titre_interpretation.grid(row=9, column=3, padx=10, pady=5, sticky="n")

    # Création du libellé et du champ de saisie
    label_cmb_cmi = tk.Label(root, text="CMB/CMI :")
    label_cmb_cmi.grid(row=10, column=0, padx=10, pady=5, sticky="w")

    entre_cmb_cmi = tk.Entry(root, width=25)
    entre_cmb_cmi.grid(row=10, column=1, padx=10, pady=5)


    # Label pour l'interprétation
    label_interpretation_cmb_cmi = tk.Label(root, text="", fg="blue")
    label_interpretation_cmb_cmi.grid(row=10, column=2, padx=10, pady=5, sticky="w")
    
    # Fonction pour calculer et afficher les résultats
    def calculer_resultats_cmb():
        # Récupérer la valeur saisie par l'utilisateur
        cmb_cmi_str = entre_cmb_cmi.get()

        # Interprétation du CMB/CMI
        if cmb_cmi_str == "":
            messagebox.showwarning("champ vide", "Veuillez remplir le champ")
        try:
            cmb_cmi = float(cmb_cmi_str)
        except ValueError:  # Si une exception se produit lors de la conversion
            messagebox.showwarning("Valeur incorrecte", "Veuillez saisir des nombres valides.")
            return 
        
        interpretation_cmb_cmi = "L\'huile essentielle a un pouvoir Bacteriostatique"
        if cmb_cmi <= 4:
            interpretation_cmb_cmi = "L\'huile essentielle a un pouvoir Bactericide"
        label_interpretation_cmb_cmi.config(text=interpretation_cmb_cmi)

    # Fonction pour réinitialiser le champ de saisie
    def reinitialiser():
        entre_cmb_cmi.delete(0, tk.END)
        label_interpretation_cmb_cmi.config(text="")


    # Création des boutons pour afficher l'interprétation et réinitialiser le champ de saisie
    bouton_interpretation = tk.Button(root, text="Executer", command=calculer_resultats_cmb, width=10, font=("Helvetica", 12, "bold"))
    bouton_interpretation.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    bouton_nouveau = tk.Button(root, text="Nouveau", command=reinitialiser, width=10, font=("Helvetica", 12, "bold"))
    bouton_nouveau.grid(row=11, column=2,columnspan=2, padx=10, pady=10)
    
    def quitter():
        if messagebox.askyesnocancel("quitter", "voulez-vous vraiment quitter?"):
            root.quit()
    
    bouton_quitter = tk.Button(root, text="Quiter", command=quitter)
    bouton_quitter.grid(row=12, column=2, columnspan=1, padx=15, pady=15)


    
bouton_entrer = tk.Button(fenetre_accueil, text="Entrer", command=ouvrir_fenetre_principale, bd=2, height=2, width=20, font=("Helvetica", 12, "bold"))
bouton_entrer.pack(pady=10)

bouton_quitter = tk.Button(fenetre_accueil, text="Quitter", command=fenetre_accueil.quit, bd=2, height=2, width=20, font=("Helvetica", 12, "bold"))
bouton_quitter.pack(pady=10)

# Lancement de la boucle principale
fenetre_accueil.mainloop()
