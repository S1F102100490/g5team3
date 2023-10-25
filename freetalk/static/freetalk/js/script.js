document.addEventListener("DOMContentLoaded", function() {
    const chatMessages = document.getElementById("chat-messages");
    const messageInput = document.getElementById("message-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", function() {
        const userMessage = messageInput.value;
        displayUserMessage(userMessage);

        // ChatGPT APIにユーザーの入力を送信し、応答を表示
        fetch('/chat_with_gpt/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // CSRFトークンを含める
            },
            body: JSON.stringify({ user_input: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.bot_response;
            displayBotMessage(botResponse);
        })
        .catch(error => console.error(error));

        messageInput.value = "";
    });

    function displayUserMessage(message) {
        const userMessageElement = document.createElement("div");
        userMessageElement.textContent = message;
        userMessageElement.classList.add("user-message");
        chatMessages.appendChild(userMessageElement);
    }



    
    function displayBotMessage(message) {
        const botMessageElement = document.createElement("div");
        botMessageElement.textContent = message;
        botMessageElement.classList.add("bot-message");
        chatMessages.appendChild(botMessageElement);
    }



    // CSRFトークンを取得する関数
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // CSRFトークンのクッキー名は "csrftoken"
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
