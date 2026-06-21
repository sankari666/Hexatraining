db.receipts.createIndex(
    { user_id: 1 }
);
db.receipts.createIndex(
    { receipt_id: 1 },
    { unique: true }
);
db.receipts.createIndex(
    {
        user_id: 1,
        receipt_date: -1
    }
);
