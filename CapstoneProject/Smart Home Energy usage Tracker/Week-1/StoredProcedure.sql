DELIMITER $$
CREATE PROCEDURE DailyRoomEnergyUsage(
    IN p_date DATE
)
BEGIN
    SELECT
        r.room_name,
        e.log_date,
        SUM(e.usage_kwh) AS total_energy_usage
    FROM rooms r
    JOIN devices d
        ON r.room_id = d.room_id
    JOIN energy_logs e
        ON d.device_id = e.device_id
    WHERE e.log_date = p_date
    GROUP BY r.room_name, e.log_date;

END$$
DELIMITER ;
CALL DailyRoomEnergyUsage('2026-06-01');
