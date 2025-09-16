 document.getElementById("registerForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch('http://127.0.0.1:3000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ firstName, lastName, username, email, password , role : "user" })
    })
    .then(res => res.json())
    .then((data) => {
        if (data.message === "User registered successfully") {
            localStorage.setItem("username", username);
            window.location.href = "/chat"
        }
        else {
            alert(data.message);
        }
    })
    .catch(err => alert(err));
 });