CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(100),
    role VARCHAR(20)
);

INSERT INTO users VALUES
(1,'alice','alice123','patient'),
(2,'bob','bob123','doctor'),
(3,'admin','admin123','admin');

CREATE TABLE medical_records (
    id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    diagnosis TEXT
);

INSERT INTO medical_records VALUES
(1001,1,2,'Flu infection'),
(1002,1,2,'Annual checkup'),
(1003,99,2,'HIV Positive - Confidential');