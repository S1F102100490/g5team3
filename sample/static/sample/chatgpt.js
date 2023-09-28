// chatgpt.js

function askQuestion() {
    const userInput = document.getElementById("userInput").value;
    const chatOutput = document.getElementById("chatOutput");

    // サーバーに質問を送信
    fetch("/ask/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken"), // CSRFトークンを含める（Djangoの場合）
        },
        body: new URLSearchParams({ question: userInput }),
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
