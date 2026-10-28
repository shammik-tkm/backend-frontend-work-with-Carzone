document.addEventListener('DOMContentLoaded', () => {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(btn => {
        btn.addEventListener('click', () => {
            const answer = btn.nextElementSibling;
            const icon = btn.querySelector('i');
            const isExpanded = btn.getAttribute('aria-expanded') === 'true';

            faqQuestions.forEach(other => {
                if (other !== btn) {
                    other.setAttribute('aria-expanded', 'false');
                    if (other.nextElementSibling) other.nextElementSibling.hidden = true;
                    const oi = other.querySelector('i');
                    if (oi) oi.className = 'fas fa-plus text-brand-orange';
                }
            });

            btn.setAttribute('aria-expanded', !isExpanded);
            if (answer) answer.hidden = isExpanded;
            if (icon) {
                icon.className = isExpanded
                    ? 'fas fa-plus text-brand-orange'
                    : 'fas fa-minus text-brand-orange';
            }
        });
    });
});