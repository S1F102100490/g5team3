document.addEventListener("DOMContentLoaded", function() {
    const chatMessages = document.getElementById("chat-messages");
    const messageInput = document.getElementById("message-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", function() {
        const userMessage = messageInput.value;
        displayUserMessage(userMessage);
        // ここでユーザーの入力を処理し、応答を生成するコードを追加
        messageInput.value = "";
    });

    function displayUserMessage(message) {
        const userMessageElement = document.createElement("div");
        userMessageElement.textContent = message;
        userMessageElement.classList.add("user-message");
        chatMessages.appendChild(userMessageElement);
    }

    // ここで応答メッセージを表示する関数を追加
});
