from app import create_app, user_datastore
from app.extensions import db
import click

app = create_app()

# Create a user to test with


@app.cli.command('create-user')
@click.argument('email')
@click.argument('passsword')
def create_user(name, password):
    db.create_all()
    user_datastore.create_user(
        email=name, password=password)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
