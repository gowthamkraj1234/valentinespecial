const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

// Dummy user (REAL LOGIN LOGIC)
const USER = {
  username: "gowtham",
  password: "12345"
};

// Routes
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (username === USER.username && password === USER.password) {
    res.redirect("/home.html");
  } else {
    res.send("<h2>Invalid credentials ❌</h2><a href='/login.html'>Try again</a>");
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
