const mongoose = require("mongoose");
const configs = require("../configs");

async function connectDB() {
  try {
    await mongoose.connect(configs.mongoUrl);
    console.log("Connected to MongoDB");
  } catch (error) {
    console.error("Error connecting to MongoDB:", error.message);
    process.exit(1);
  }
}

module.exports = connectDB;
