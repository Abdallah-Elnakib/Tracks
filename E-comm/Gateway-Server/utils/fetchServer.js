
const fetchPOSTREQUEST = async (url, body) => {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'username': process.env.USERNAME_SERVER,
                'password': process.env.PASSWORD_SERVER
            },
            body: JSON.stringify(body)
        });
        const data = await response.json();
        return data

    } catch (error) {
        console.log(error);
    }
}


module.exports = { fetchPOSTREQUEST }