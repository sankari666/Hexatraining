use EnergyMonitoringDB
db.sensor_logs.insertMany([
{
    device_id: 1,
    timestamp: ISODate("2026-06-01T09:00:00Z"),
    room: "Conference Room",
    power_usage: 6.2,
    voltage: 220,
    current: 2.8,
    status: "ON"
},
{
    device_id: 1,
    timestamp: ISODate("2026-06-01T15:00:00Z"),
    room: "Conference Room",
    power_usage: 6.3,
    voltage: 221,
    current: 2.9,
    status: "ON"
},
{
    device_id: 2,
    timestamp: ISODate("2026-06-01T10:00:00Z"),
    room: "Server Room",
    power_usage: 25.8,
    voltage: 230,
    current: 5.4,
    status: "ON"
},
{
    device_id: 3,
    timestamp: ISODate("2026-06-01T12:00:00Z"),
    room: "Lab",
    power_usage: 4.5,
    voltage: 220,
    current: 1.1,
    status: "OFF"
}
]);
