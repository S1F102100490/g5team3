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


// サーバーに質問を送信
function askQuestion() {
    const userInput = document.getElementById("userInput").value;
    const chatOutput = document.getElementById("chatOutput");

    // DjangoのCSRFトークンを取得
    const csrftoken = getCookie("csrftoken");

    // サーバーに質問を送信
    fetch("/ask/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json", // JSON形式でデータを送信
            "X-CSRFToken": csrftoken, // CSRFトークンを含める
        },
        body: JSON.stringify({ question: userInput }), // 質問データをJSONに変換
    })
        .then((response) => response.json())
        .then((data) => {
            // ChatGPTからの応答を表示
            const chatMessage = document.createElement("p");
            chatMessage.textContent = data.answer;
            chatOutput.appendChild(chatMessage);
        });
}

// DjangoのCSRFトークンを取得
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


