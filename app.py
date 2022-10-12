from src import app, utils
from src.models import Models
from os import environ

models = Models()
models.createModels()
utils.readDbFile("src/data.sql", models)

#app.run(host='locahost', debug=False, port=environ.get("PORT", 8080))
