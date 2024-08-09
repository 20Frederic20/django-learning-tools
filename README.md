docker pull python:3.10-slim
sudo docker compose run web django-admin startproject composeexample .
# sudo chown -R $USER:$USER composeexample manage.py
docker compose up