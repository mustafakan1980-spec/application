// Application - Vanilla JS interactions
document.addEventListener('DOMContentLoaded', () => {
    // Parola göster / gizle fonksiyonu
    const toggleBtns = document.querySelectorAll('.password-toggle-btn');
    toggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const input = document.getElementById(targetId);
            if (input) {
                if (input.type === 'password') {
                    input.type = 'text';
                    btn.textContent = '🙈';
                    btn.setAttribute('aria-label', 'Parolayı gizle');
                } else {
                    input.type = 'password';
                    btn.textContent = '👁️';
                    btn.setAttribute('aria-label', 'Parolayı göster');
                }
            }
        });
    });
});
