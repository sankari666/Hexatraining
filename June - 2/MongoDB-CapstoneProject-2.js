use edtech_capstone_db



db.learners.find()


db.courses.find()


db.learners.find(
    {},
    { _id: 0, name: 1, city: 1, goal: 1 }
)


db.learners.find({ city: "Hyderabad" })


db.learners.find({ goal: "AI Engineer" })


db.courses.find({ category: "Data Engineering" })


db.courses.find({ price: { $gt: 10000 } })


db.courses.find({ level: "Beginner" })


db.enrollments.find({ "payment.status": "Success" })


db.learners.find({ phone: null })



db.learners.find({ experience_years: { $gt: 2 } })


db.courses.find({
    price: {
        $gte: 8000,
        $lte: 18000
    }
})


db.courses.find({
    level: {
        $in: ["Beginner", "Intermediate"]
    }
})


db.enrollments.find({
    "progress.completion_percent": { $gte: 80 }
})


db.enrollments.find({
    "payment.status": { $ne: "Success" }
})


db.learners.find({
    city: {
        $in: ["Hyderabad", "Bangalore", "Pune"]
    }
})

db.courses.find({
    category: { $ne: "Cloud" }
})


db.instructors.find({
    expertise: "AI"
})


db.instructors.find({
    expertise: "SQL"
})


db.courses.find({
    tools: "Python"
})


db.courses.find({
    tools: "Databricks"
})

db.enrollments.find({
    quiz_scores: 95
})


db.enrollments.find({
    quiz_scores: { $gt: 85 }
})


db.courses.find().sort({ price: -1 })


db.courses.find()
    .sort({ price: -1 })
    .limit(3)


db.learners.find()
    .sort({ experience_years: -1 })


db.learners.find()
    .sort({ experience_years: -1 })
    .limit(2)


db.instructors.find()
    .sort({ rating: -1 })


db.learners.updateOne(
    { learner_id: 1 },
    { $set: { city: "Secunderabad" } }
)


db.courses.updateOne(
    { course_id: 203 },
    { $set: { price: 9000 } }
)


db.enrollments.updateOne(
    { enrollment_id: 1006 },
    { $set: { "progress.completion_percent": 30 } }
)


db.enrollments.updateOne(
    { enrollment_id: 1005 },
    { $set: { status: "Inactive" } }
)


db.learners.updateMany(
    {},
    { $set: { active: true } }
)


db.learners.updateMany(
    {},
    { $unset: { active: "" } }
)


db.courses.updateOne(
    { course_id: 201 },
    { $push: { tools: "MongoDB" } }
)


db.enrollments.deleteMany({
    "payment.status": "Failed"
})

db.learners.deleteMany({
    experience_years: 0
})


db.learners.countDocuments()


db.courses.countDocuments()


db.enrollments.countDocuments({
    "payment.status": "Success"
})


db.learners.distinct("city")


db.courses.distinct("category")


db.enrollments.distinct("payment.mode")


db.enrollments.aggregate([
    {
        $match: {
            "payment.status": "Success"
        }
    },
    {
        $group: {
            _id: "$payment.mode",
            total_revenue: {
                $sum: "$payment.amount"
            }
        }
    }
])

db.enrollments.aggregate([
    {
        $match: {
            "payment.status": "Success"
        }
    },
    {
        $group: {
            _id: "$course_id",
            total_revenue: {
                $sum: "$payment.amount"
            }
        }
    }
])


db.learners.aggregate([
    {
        $group: {
            _id: "$goal",
            total_learners: { $sum: 1 }
        }
    }
])


db.courses.aggregate([
    {
        $group: {
            _id: "$category",
            average_price: {
                $avg: "$price"
            }
        }
    }
])


db.enrollments.aggregate([
    {
        $group: {
            _id: "$course_id",
            average_completion: {
                $avg: "$progress.completion_percent"
            }
        }
    }
])


db.enrollments.aggregate([
    {
        $group: {
            _id: "$status",
            total_enrollments: { $sum: 1 }
        }
    }
])


db.enrollments.aggregate([
    {
        $match: {
            "payment.status": "Success"
        }
    },
    {
        $group: {
            _id: "$course_id",
            total_revenue: {
                $sum: "$payment.amount"
            }
        }
    },
    {
        $match: {
            total_revenue: { $gt: 15000 }
        }
    }
])



db.enrollments.aggregate([
    {
        $lookup: {
            from: "learners",
            localField: "learner_id",
            foreignField: "learner_id",
            as: "learner_details"
        }
    },
    {
        $unwind: "$learner_details"
    },
    {
        $project: {
            _id: 0,
            enrollment_id: 1,
            learner_name: "$learner_details.name",
            city: "$learner_details.city",
            course_id: 1,
            status: 1
        }
    }
])


db.enrollments.aggregate([
    {
        $lookup: {
            from: "courses",
            localField: "course_id",
            foreignField: "course_id",
            as: "course_details"
        }
    },
    {
        $unwind: "$course_details"
    },
    {
        $project: {
            _id: 0,
            enrollment_id: 1,
            course_name: "$course_details.course_name",
            category: "$course_details.category",
            amount: "$payment.amount",
            payment_status: "$payment.status"
        }
    }
])

db.courses.aggregate([
    {
        $lookup: {
            from: "instructors",
            localField: "instructor_id",
            foreignField: "instructor_id",
            as: "instructor_details"
        }
    },
    {
        $unwind: "$instructor_details"
    },
    {
        $project: {
            _id: 0,
            course_name: 1,
            category: 1,
            instructor_name: "$instructor_details.instructor_name",
            instructor_rating: "$instructor_details.rating"
        }
    }
])


db.enrollments.aggregate([
    {
        $lookup: {
            from: "learners",
            localField: "learner_id",
            foreignField: "learner_id",
            as: "learner_details"
        }
    },
    {
        $unwind: "$learner_details"
    },
    {
        $lookup: {
            from: "courses",
            localField: "course_id",
            foreignField: "course_id",
            as: "course_details"
        }
    },
    {
        $unwind: "$course_details"
    },
    {
        $lookup: {
            from: "instructors",
            localField: "course_details.instructor_id",
            foreignField: "instructor_id",
            as: "instructor_details"
        }
    },
    {
        $unwind: "$instructor_details"
    },
    {
        $project: {
            _id: 0,
            enrollment_id: 1,
            learner_name: "$learner_details.name",
            city: "$learner_details.city",
            goal: "$learner_details.goal",
            course_name: "$course_details.course_name",
            category: "$course_details.category",
            instructor_name: "$instructor_details.instructor_name",
            payment_amount: "$payment.amount",
            payment_status: "$payment.status",
            completion_percent: "$progress.completion_percent",
            enrollment_status: "$status"
        }
    }
])
