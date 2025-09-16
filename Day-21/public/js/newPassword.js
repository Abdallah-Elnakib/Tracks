document.getElementById('newPasswordForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const otp = document.getElementById('otp').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    fetch('http://127.0.0.1:3000/new-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email : localStorage.getItem('email'), otp, newPassword, confirmPassword })
    })
    .then(res => res.json())
    .then((data) => {
        if (data.message === "Password updated successfully") {
            window.location.href = "/login"
            localStorage.removeItem('email');
        }
        else {
            alert(data.message);
        }
    })
    .catch(err => alert(err));
});