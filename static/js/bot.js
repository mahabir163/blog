const botButton = document.getElementById("botButton");
const chatWindow = document.getElementById("chatWindow");
const closeChat = document.getElementById("closeChat");

botButton.addEventListener("click", () => {
    chatWindow.classList.toggle("hidden");
});

closeChat.addEventListener("click", () => {
    chatWindow.classList.add("hidden");
});