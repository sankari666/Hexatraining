#read
db.receipts.find();
db.receipts.find({ user_id: 1 });
#update
db.receipts.updateOne(
    { receipt_id: "R1001" },
    {
        $set: {
            notes: "Updated lunch expense"
        }
    }
);
#delete
db.receipts.deleteOne({
    receipt_id: "R1003"
});
