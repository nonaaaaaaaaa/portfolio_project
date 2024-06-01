from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

db = SQLAlchemy(app)

from models import Pet, User, Service, Veterinarian, Appointment

# Example route to test database
@app.route('/')
def index():
    return "Welcome to the Pet Clinic!"

if __name__ == '__main__':
    app.run()
