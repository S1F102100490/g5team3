// サーバーに質問を送信
function askQuestion() {
    const userInput = document.getElementById("userInput").value;
    const chatOutput = document.getElementById("chatOutput");

    // DjangoのCSRFトークンを取得
    const csrftoken = getCookie("csrftoken");

    // サーバーに質問を送信
    fetch("/ask_sample/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json", // JSON形式でデータを送信
            "X-CSRFToken": csrftoken, // CSRFトークンを含める
        },
        body: JSON.stringify({ question: userInput }), // 質問データをJSONに変換
    })
    fetch("/ask_sample/", {
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

