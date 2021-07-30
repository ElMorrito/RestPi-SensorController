import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy.model import Model


from app import create_app
from app.extensions import db


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
