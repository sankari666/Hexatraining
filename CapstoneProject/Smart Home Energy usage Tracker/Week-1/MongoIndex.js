db.sensor_logs.createIndex(
    { device_id: 1 }
)
db.sensor_logs.createIndex(
    { timestamp: -1 }
)
db.sensor_logs.createIndex(
    {
        device_id: 1,
        timestamp: -1
    }
)
