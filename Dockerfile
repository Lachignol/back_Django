# Utilise l'image officielle Python
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Supprimer les migrations existantes
RUN find . -path "*/migrations/*.py" -not -name "__init__.py" -delete \
    && find . -path "*/migrations/*.pyc" -delete

# Créer de nouvelles migrations et migrer la base
RUN python manage.py makemigrations \
    && python manage.py migrate

# Exposer le port (ex. 8000)
EXPOSE 8000

# Commande pour démarrer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

