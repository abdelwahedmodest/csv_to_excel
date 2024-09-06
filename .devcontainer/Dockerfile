# Utiliser l'image de base Ubuntu
FROM ubuntu:latest

# Installer Python 3.11 et pip
RUN apt-get update && apt-get install -y python3.11 python3.11-venv python3-pip

# Installer Tkinter pour Ubuntu
RUN apt-get install -y python3-tk

# Installer git pour le contrôle de version
RUN apt-get install -y git

# Définir Python 3.11 comme version par défaut
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Créer un répertoire de travail
WORKDIR /app

# Copier tout le contenu de ton projet dans le conteneur
COPY . /app

# Exposer les ports (si nécessaire, par exemple pour une interface web)
# EXPOSE 8080

# Définir la commande de démarrage
CMD ["python", "main.py"]
