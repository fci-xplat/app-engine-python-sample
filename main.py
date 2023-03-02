# from flask import Flask

# import logging

# app = Flask(__name__)


# @app.get("/")
# def index():
#     return "This is your first Python app run on App Engine!"


# if __name__ == "__main__":
#     # Dev only: run "python main.py" and open http://localhost:8080
#     app.run(host="0.0.0.0", port=8080, debug=True)

########Fast APi
from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.

@app.get("/")
async def root():
    return {"message": "App Engine is Running"}