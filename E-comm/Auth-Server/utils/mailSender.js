const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL,
        pass: process.env.PASSWORD
    }
});


const SendEmailToUser = (to, subject, text) => {
    const mailOptions = {
        from: process.env.EMAIL,
        to: to,
        subject: subject,
        text: text
    };
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });
}


module.exports = { SendEmailToUser }


// http://127.0.0.1:3000/login  => body => { usernameOrEmail, password } headers => { username: 'admin', password: 'admin' }

// req = {
//     body : {},
//     params : {},
//     query : {},
//     headers : {},
//     cookie : {}
// }


// login done

// fetch('http://1270.0.0.1:3000/login', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ usernameOrEmail: 'admin', password: 'admin' })
// })

// .then(data => data.json())
// .then(final => console.log(final))
// .catch(error => console.log(error))