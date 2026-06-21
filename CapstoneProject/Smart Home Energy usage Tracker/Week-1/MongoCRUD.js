db.sensor_logs.find()
db.sensor_logs.find({
    device_id: 1
})
db.sensor_logs.updateOne(
    { device_id: 3 },
    {
        $set: {
            status: "ON"
        }
    }
)
db.sensor_logs.deleteOne({
    device_id: 3
})
