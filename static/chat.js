document.addEventListener('DOMContentLoaded', function() {
    const chatToggleBtn = document.getElementById('chatToggleBtn');
    const closeChatBtn = document.getElementById('closeChatBtn');
    const chatPanel = document.getElementById('chatPanel');
    const chatInput = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendBtn');
    const chatMessages = document.getElementById('chatMessages');

    function toggleChat() {
        if (!chatPanel) return;
        const isNowOpen = !chatPanel.classList.contains('open');
        chatPanel.classList.toggle('open');

        if (isNowOpen && !sessionStorage.getItem('plantAssistantWelcomeShown')) {
            addMessage("Hi! I'm your AI Plant Assistant 🌿. Upload an image or describe your plant issue.", 'bot');
            sessionStorage.setItem('plantAssistantWelcomeShown', 'true');
        }

        // Show context if disease exists
        const chatbotContext = document.getElementById('chatbotContext');
        const contextDisease = document.getElementById('contextDisease');
        const chatbotFloating = document.getElementById('chatbotFloating');
        const lastDisease = chatbotFloating ? chatbotFloating.dataset.lastDisease || '' : '';
        if (chatbotContext && contextDisease && lastDisease) {
            contextDisease.textContent = lastDisease;
            chatbotContext.style.display = 'block';
        } else if (chatbotContext) {
            chatbotContext.style.display = 'none';
        }
    }

    function sendMessage() {
        if (!chatInput || !chatMessages) return;
        const message = chatInput.value.trim();
        if (!message) return;

        addMessage(message, 'user');
        chatInput.value = '';

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data && data.reply) {
                addMessage(data.reply, 'bot');
            } else {
                addMessage('Error occurred', 'bot');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('Error occurred', 'bot');
        });
    }

    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = type + '-message';
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    if (chatToggleBtn) {
        chatToggleBtn.addEventListener('click', toggleChat);
    }

    function closeAndResetChat() {
        if (!chatPanel) return;
        chatPanel.classList.remove('open');
        
        // Clear history visually
        if (chatMessages) {
            chatMessages.innerHTML = '';
        }
        sessionStorage.removeItem('plantAssistantWelcomeShown'); 
        
        // Call backend /reset to clear session context
        fetch('/reset').catch(err => console.error("Reset failed", err));
    }

    if (closeChatBtn) {
        closeChatBtn.addEventListener('click', closeAndResetChat);
    }

    const suggestionButtons = document.querySelectorAll('.suggestion-btn');
    const chatbotFloating = document.getElementById('chatbotFloating');
    const useLastResultBtn = document.getElementById('useLastResultBtn');
    const lastDisease = chatbotFloating ? chatbotFloating.dataset.lastDisease || '' : '';
    const lastTreatment = chatbotFloating ? chatbotFloating.dataset.lastTreatment || '' : '';

    function handleSuggestionClick(event) {
        const value = event.currentTarget.getAttribute('data-msg');
        if (!value || !chatInput) return;
        chatInput.value = value;
        sendMessage();
    }

    function handleUseLastResult() {
        if (!chatInput || !lastDisease) return;
        const value = `Last diagnosis: ${lastDisease}. Treatment: ${lastTreatment || 'N/A'}. Please explain what to do next.`;
        chatInput.value = value;
        sendMessage();
    }

    function autoSendMessage(message) {
        addMessage(message, 'user');
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data && data.reply) {
                addMessage(data.reply, 'bot');
            } else {
                addMessage('Error occurred', 'bot');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('Error occurred', 'bot');
        });
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    if (useLastResultBtn) {
        useLastResultBtn.addEventListener('click', handleUseLastResult);
    }

    if (suggestionButtons) {
        suggestionButtons.forEach(btn => {
            btn.addEventListener('click', handleSuggestionClick);
        });
    }

    if (sendBtn && chatInput) {
        sendBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendMessage();
            }
        });
    }

    // --- Mobile Navbar Auto-Close Logic ---
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    // Close when clicking outside of the navbar
    document.addEventListener('click', function(e) {
        if (navbarCollapse && navbarCollapse.classList.contains('show')) {
            if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target)) {
                if (typeof bootstrap !== 'undefined') {
                    const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse) || new bootstrap.Collapse(navbarCollapse, {toggle: false});
                    bsCollapse.hide();
                } else {
                    navbarCollapse.classList.remove('show');
                }
            }
        }
    });

    // Close when any nav link is clicked
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                if (typeof bootstrap !== 'undefined') {
                    const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse) || new bootstrap.Collapse(navbarCollapse, {toggle: false});
                    bsCollapse.hide();
                } else {
                    navbarCollapse.classList.remove('show');
                }
            }
        });
    });
});
