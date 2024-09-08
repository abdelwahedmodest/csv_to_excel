# Utiliser l'image de base Ubuntu
FROM ubuntu:latest

# Installer Python 3.11 et pip
RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3-pip \
    python3-tk git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Définir Python 3.11 comme version par défaut
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# Créer un répertoire de travail
WORKDIR /
#/C:/Users/lenovo/Desktop/Waiting/Septembre/06092024/1      ==>ask  chatgpt about   path

# Copier le fichier requirements.txt et installer les dépendances
COPY /requirements.txt  .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu de votre projet dans le conteneur
COPY . .

# Exposer les ports (si nécessaire, par exemple pour une interface web)
EXPOSE 8080

# Définir la commande de démarrage
CMD ["python", "main.py"]
