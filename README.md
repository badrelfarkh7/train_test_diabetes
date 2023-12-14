# train_test_diabetes

#### Les etapes pour Dockeriser : 
vi Dockerfile 
FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python main.py 

docker build -t classification-model .

docker run -p 4000:5000 classification-model

docker volume create my-volume

docker run -p 4000:5000 -v nom_du_volume:/app/c1 classification-model

docker stop <containe_id>
docker run -d -p 8080:5000 classification-model

-	Créer un repositery dans dockerhub 
-	Login in the terminal 
docker tag classification-model:latest fadiamalak/my-repo-classification:latest
docker push fadiamalak/my-repo-classification:latest


NB : les conteneurs peuvent consommer et stocker des données dans le volume.