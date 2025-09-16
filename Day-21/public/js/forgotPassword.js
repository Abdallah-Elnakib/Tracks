document.getElementById("forgotPasswordForm").addEventListener("submit", (e) => {
    console.log(5555)
    e.preventDefault();
    const email = document.getElementById("email").value;
    fetch('http://127.0.0.1:3000/send-otp', {
        method: 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({ email })
    })
    .then(res => res.json())
    .then((data) => {
        if (data.message === "OTP sent successfully") {
            localStorage.setItem("email", email);
            window.location.href = "/new-password"
        }
        else {
            alert(data.message);
        }
    })
    .catch(err => alert(err));
})