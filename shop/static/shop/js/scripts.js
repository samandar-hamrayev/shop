document.addEventListener("DOMContentLoaded", function () {
    console.log("Website loaded successfully!");
});


// Hide messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messageContainer = document.getElementById('message-container');
    if (messageContainer) {
        setTimeout(function() {
            messageContainer.style.transition = 'opacity 0.5s';
            messageContainer.style.opacity = '0';
            setTimeout(function() {
                messageContainer.remove();
            }, 500);
        }, 5000);
    }
});