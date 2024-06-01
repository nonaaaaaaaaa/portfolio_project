from app import db

class Pet(db.Model):
    petId = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    species = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255))
    age = db.Column(db.Integer)
    medicalHistory = db.Column(db.Text)

class User(db.Model):
    userId = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phoneNumber = db.Column(db.String(255))
    address = db.Column(db.String(255))

class Service(db.Model):
    serviceId = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2))

class Veterinarian(db.Model):
    veterinarianId = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255))
    phoneNumber = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)

class Appointment(db.Model):
    appointmentId = db.Column(db.String(255), primary_key=True)
    petId = db.Column(db.String(255), db.ForeignKey('pet.petId'), nullable=False)
    userId = db.Column(db.String(255), db.ForeignKey('user.userId'), nullable=False)
    serviceId = db.Column(db.String(255), db.ForeignKey('service.serviceId'), nullable=False)
    veterinarianId = db.Column(db.String(255), db.ForeignKey('veterinarian.veterinarianId'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    status = db.Column(db.Enum('scheduled', 'completed', 'canceled', name='status_enum'), nullable=False)
