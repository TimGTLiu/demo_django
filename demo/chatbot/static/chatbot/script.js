function sendMessage() {
    var message = document.getElementById('message').value;
    if (message.trim() !== "") {
        var userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'user-message';
        userMessageDiv.textContent = message;

        document.getElementById('chat-box').appendChild(userMessageDiv);
        document.getElementById('message').value = '';

        fetch('get_response/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            var botMessageDiv = document.createElement('div');
            botMessageDiv.className = 'bot-message';
            botMessageDiv.textContent = data.response;
            document.getElementById('chat-box').appendChild(botMessageDiv);
            document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;
        })
        .catch(error => console.error('Error:', error));
    }
}

document.getElementById('message').addEventListener('keypress', function(e) {
    if (e.which === 13) {
        sendMessage();
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
