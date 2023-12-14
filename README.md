# train_test_diabetes

#### Les etapes pour Dockeriser : 
vi Dockerfile : Pour modifier le fichier docker
FROM python:3.8-alpine #l'image  de base qu'on utilise 
COPY . /app   #Copier les fichier de notre application dans le contenaire
WORKDIR /app 
RUN pip install -r requirements.txt # commande a execute dand l image
CMD python main.py # commande a execute dand le contenqire
docker build -t classification-model .  # la creation de l image docker

Création d'un volume:

docker volume create my-volume

Lors de l'exécution du conteneur, on  utilise l'option -v pour monter le volume créé sur la  machine hôte.

Pour le lancer localement : 
docker run -p 4000:5000 -v nom_du_volume:/app/c1 classification-model

-	Créer un repositery dans dockerhub 
-	Login in the terminal 
docker tag classification-model:latest fadiamalak/my-repo-classification:latest
docker push fadiamalak/my-repo-classification:latest


NB : les conteneurs peuvent consommer et stocker des données dans le volume.