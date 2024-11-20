
CREATE DATABASE  flight_db;
USE flight_db;

-- Create the 'flights' table
CREATE TABLE flights (
    flight_id VARCHAR(10) PRIMARY KEY,
    airline_name VARCHAR(50) NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    capacity INT NOT NULL
);

-- Insert sample data into the 'flights' table
INSERT INTO flights (flight_id, airline_name, departure_time, arrival_time, capacity)
VALUES
    ('FL001', 'Air India', '10:00:00', '12:30:00', 180),
    ('FL002', 'Indigo', '09:15:00', '10:45:00', 150),
    ('FL003', 'SpiceJet', '08:30:00', '11:00:00', 200),
    ('FL004', 'Vistara', '14:00:00', '16:30:00', 220),
    ('FL005', 'GoAir', '17:45:00', '20:15:00', 160);

-- Check the data in the 'flights' table
SELECT * FROM flights;
