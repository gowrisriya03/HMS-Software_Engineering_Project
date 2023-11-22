-- Create Schema

CREATE SCHEMA `hms`;
use hms;

-- Create Tables

CREATE TABLE `hms`.`patients` (
  `patient_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `age` INT NOT NULL,
  `phone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `patient_id_UNIQUE` (`patient_id` ASC) VISIBLE);
  
CREATE TABLE `hms`.`doctors` (
  `doctor_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`doctor_id`),
  UNIQUE INDEX `doctor_id_UNIQUE` (`doctor_id` ASC) VISIBLE);

CREATE TABLE `hms`.`pharmacists` (
  `pharma_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`pharma_id`),
  UNIQUE INDEX `pharma_id_UNIQUE` (`pharma_id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE);
  
CREATE TABLE `hms`.`visits` (
  `visit_id` INT NOT NULL,
  `datetime` DATETIME NOT NULL,
  `patient_id` INT NOT NULL,
  `doctor_id` INT NULL DEFAULT NULL,
  `visit_done` BIT(1) NOT NULL DEFAULT 0,
  `diagnose` VARCHAR(45) NULL DEFAULT NULL,
  `review` VARCHAR(45) NULL DEFAULT NULL,
  `prescription` VARCHAR(45) NULL DEFAULT NULL,
  `pharmacy_done` BIT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`visit_id`),
  UNIQUE INDEX `visit_id_UNIQUE` (`visit_id` ASC) VISIBLE);

-- Add Foreign Keys

ALTER TABLE `hms`.`visits`
  ADD CONSTRAINT `fk_visits_patient`
  FOREIGN KEY (`patient_id`)
  REFERENCES `hms`.`patients` (`patient_id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
ALTER TABLE `hms`.`visits`
  ADD CONSTRAINT `fk_visits_doctor`
  FOREIGN KEY (`doctor_id`)
  REFERENCES `hms`.`doctors` (`doctor_id`)
  ON DELETE SET NULL
  ON UPDATE CASCADE;

-- Insert data into 'patients' table
INSERT INTO `hms`.`patients` (`patient_id`, `name`, `age`, `phone`, `email`) 
VALUES 
(1, 'John Doe', 25, '1234567890', 'johndoe@example.com'),
(2, 'Jane', 30, '9876543210', 'jane@example.com'),
(3, 'Bob', 40, '5551234567', 'bob@example.com'),
(4, 'Alice', 28, '3334445555', 'alice@example.com'),
(5, 'Charlie', 35, '6667778888', 'charlie@example.com');
-- Insert data into 'doctors' table
INSERT INTO `hms`.`doctors` (`doctor_id`, `name`, `email`) 
VALUES 
(101, 'Dr. Smith', 'smith@example.com'),
(102, 'Dr. Johnson', 'johnson@example.com'),
(103, 'Dr. Davis', 'davis@example.com');
-- Insert data into 'pharmacists' table
INSERT INTO `hms`.`pharmacists` (`pharma_id`, `name`, `email`) 
VALUES 
(201, 'PharmaCare', 'pharmacare@example.com'),
(202, 'QuickMeds', 'quickmeds@example.com');
-- Insert data into 'visits' table
INSERT INTO `hms`.`visits` (`visit_id`, `datetime`, `patient_id`, `doctor_id`, `visit_done`, `diagnose`, `review`, `prescription`, `pharmacy_done`) 
VALUES 
(1, '2023-11-21 10:00:00', 1, 101, 1, 'Fever', 'Good recovery', 'Paracetamol', 1),
(2, '2023-11-22 14:30:00', 2, 102, 1, 'Headache', 'Stable condition', 'Ibuprofen', 1),
(3, '2023-11-23 11:45:00', 3, NULL, 0, NULL, NULL, NULL, 0),
(4, '2023-11-24 09:15:00', 4, 103, 1, 'Cough', 'Improving', 'Cough syrup', 0),
(6, '2023-11-24 11:45:00', 2, NULL, 0, NULL, NULL, NULL, 0),
(5, '2023-11-25 16:00:00', 5, 101, 1, 'Allergy', 'No issues', 'Antihistamine', 0);
  