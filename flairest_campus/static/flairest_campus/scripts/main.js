function sendMessage() {
    var messageInput = document.getElementById("messageInput");
    var message = messageInput.value.trim();

    if (message !== "") {
        appendMessage(message, true); // отправляем сообщение пользователя
        simulateBotResponse(message); // имитируем ответ от ии
        messageInput.value = "";
    }
}

function appendMessage(message, isUser) {
    var messagesContainer = document.getElementById("messages");
    var messageElement = document.createElement("div");
    messageElement.classList.add("message");
    messageElement.textContent = message;

    if (isUser) {
        messageElement.classList.add("sent-message");
    } else {
        messageElement.classList.add("received-message");
    }

    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function simulateBotResponse(message) {
    var botResponse = "Принято ваше сообщение: '" + message + "'. Ваш запрос обрабатывается.";
    setTimeout(function() {
        appendMessage(botResponse, false); // добавляем ответ от бота в чат
    }, 1000); // имитация задержки в обработке запроса
}

