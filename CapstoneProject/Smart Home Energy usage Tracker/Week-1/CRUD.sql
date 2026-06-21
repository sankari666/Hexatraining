#create
INSERT INTO devices
(device_name,device_type,status,room_id)
VALUES
('Projector','Electronics','ON',1);
#read
SELECT * FROM devices;
SELECT
d.device_name,
e.usage_kwh,
e.log_date
FROM devices d
JOIN energy_logs e
ON d.device_id=e.device_id;
#update
UPDATE devices
SET status='OFF'
WHERE device_id=1;
UPDATE energy_logs
SET usage_kwh=15.5
WHERE log_id=1;
#delete
DELETE FROM energy_logs
WHERE log_id=5;
DELETE FROM devices
WHERE device_id=4;
