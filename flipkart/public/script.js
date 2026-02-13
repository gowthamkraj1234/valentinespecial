function login() {
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;
  const error = document.getElementById("error");

  // demo credentials
  if (user === "gowtham" && pass === "12345") {
    window.location.href = "home.html";
  } else {
    error.textContent = "Invalid username or password";
  }
}
