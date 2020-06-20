from celery import Celery
import json

# Celery hosted on local redis server
app = Celery(
    'flask-celery',
    backend='redis://localhost:6379/0',
    broker='redis://localhost:6379/0'
)

@app.task()
def update(key, value):
    # Updates the links.json object, adding a new shortened_link - link (key-value) pair
    with open("links.json", "r") as jsonFile:
        links = json.load(jsonFile)

    links[key] = value;

    with open("links.json", "w") as jsonFile:
        json.dump(links, jsonFile)

