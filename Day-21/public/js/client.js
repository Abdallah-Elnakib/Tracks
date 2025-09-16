const socket = io();
const username = localStorage.getItem("username");

document.getElementById("user").textContent = username;

socket.emit("register", username);

document.getElementById("sendBtn").addEventListener("click", () => {
  const toUser = document.getElementById("toUser").value;
  const message = document.getElementById("message").value;

  socket.emit("private-message", { to: toUser, message });

  addMessage(`You ➡️ ${toUser}: ${message}`);
  document.getElementById("message").value = "";
});

socket.on("private-message", (data) => {
  addMessage(`${data.from} ➡️ You: ${data.message}`);
});

function addMessage(msg) {
  const chatBox = document.getElementById("chatBox");
  const p = document.createElement("p");
  p.textContent = msg;
  chatBox.appendChild(p);
}

document.getElementById("logout").addEventListener("click", () => {
  fetch('http://127.0.0.1:3000/logout')
    .then(res => res.json())
    .then((data) => {
      if (data.message === "Logout successful") {
        localStorage.removeItem("username");
        window.location.href = "/login";
      }
      else {
        alert(data.message);
      }
    })
    .catch(err => alert(err));

});