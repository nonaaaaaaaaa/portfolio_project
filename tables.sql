CREATE TABLE Pet (
    petId VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255),
    breed VARCHAR(255),
    age INT,
    medicalHistory TEXT
);

CREATE TABLE User (
    userId VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    phoneNumber VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE Service (
    serviceId VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2)
);

CREATE TABLE Veterinarian (
    veterinarianId VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    specialization VARCHAR(255),
    phoneNumber VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE Appointment (
    appointmentId VARCHAR(255) PRIMARY KEY,
    petId VARCHAR(255),
    userId VARCHAR(255),
    serviceId VARCHAR(255),
    veterinarianId VARCHAR(255),
    date DATE,
    time TIME,
    status ENUM('scheduled', 'completed', 'canceled'),
    FOREIGN KEY (petId) REFERENCES Pet(petId),
    FOREIGN KEY (userId) REFERENCES User(userId),
    FOREIGN KEY (serviceId) REFERENCES Service(serviceId),
    FOREIGN KEY (veterinarianId) REFERENCES Veterinarian(veterinarianId)
);