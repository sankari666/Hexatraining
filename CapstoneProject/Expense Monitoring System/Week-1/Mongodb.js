use ExpenseTrackerDB
db.receipts.insertMany([
{
    user_id: 1,
    receipt_id: "R1001",
    receipt_date: ISODate("2026-06-01"),
    category: "Food",
    amount: 500,
    notes: "Lunch at restaurant",
    scanned_receipt: {
        file_name: "receipt1.jpg",
        store: "ABC Restaurant",
        payment_mode: "UPI"
    }
},
{
    user_id: 1,
    receipt_id: "R1002",
    receipt_date: ISODate("2026-06-05"),
    category: "Transport",
    amount: 200,
    notes: "Bus travel",
    scanned_receipt: {
        file_name: "receipt2.jpg",
        route: "Chennai-Bangalore",
        payment_mode: "Cash"
    }
},
{
    user_id: 2,
    receipt_id: "R1003",
    receipt_date: ISODate("2026-06-07"),
    category: "Shopping",
    amount: 1500,
    notes: "Clothing purchase",
    scanned_receipt: {
        file_name: "receipt3.jpg",
        store: "Fashion Store",
        payment_mode: "Card"
    }
}
]);
