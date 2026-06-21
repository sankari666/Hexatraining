CREATE DATABASE EnergyMonitoring;
USE EnergyMonitoring;
CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(100) NOT NULL,
    floor_no INT
);
CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    device_type VARCHAR(50),
    status VARCHAR(20),
    room_id INT,
    FOREIGN KEY (room_id)
    REFERENCES rooms(room_id)
);
CREATE TABLE energy_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    device_id INT,
    usage_kwh DECIMAL(10,2),
    log_date DATE,
    FOREIGN KEY (device_id)
    REFERENCES devices(device_id)
);
INSERT INTO rooms(room_name, floor_no)
VALUES
('Conference Room',1),
('Server Room',2),
('Lab',1);
INSERT INTO devices(device_name,device_type,status,room_id)
VALUES
('AC Unit','Air Conditioner','ON',1),
('Server Rack','Computer','ON',2),
('LED Lights','Lighting','OFF',3);
INSERT INTO energy_logs(device_id,usage_kwh,log_date)
VALUES
(1,12.5,'2026-06-01'),
(1,10.2,'2026-06-01'),
(2,25.8,'2026-06-01'),
(3,4.5,'2026-06-01'),
(2,27.4,'2026-06-02');
