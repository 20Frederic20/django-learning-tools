docker pull python:3.10-slim
sudo docker compose run web django-admin startproject composeexample .

# sudo chown -R $USER:$USER composeexample manage.py

docker compose up

Mise en place d'un consumer de rabbitmq

Actuellement celui-ci recoit des données d'une apllication laravel

Accéder au dépot microservice-test pour voir la configuration docker utilisé

Actullement j'ai essayé de dockkerisé les applications part à part mais je n'ai pas réussi donc j'ai mis les deux dans le meme dossiers pour les faire communiquer
