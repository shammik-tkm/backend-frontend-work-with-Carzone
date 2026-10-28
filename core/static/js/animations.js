document.addEventListener('DOMContentLoaded', () => {
    // Dinamicheskij god v footere
    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // Fade-in animacii pri skrolle
    document.querySelectorAll('section > div, article, .faq-item, aside > div, aside > a').forEach((t, i) => {
        t.classList.add('fade-in-element', `stagger-${(i % 4) + 1}`);
    });

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                obs.unobserve(entry.target);
            }
        });
    }, { root: null, threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-in-element').forEach(el => observer.observe(el));
});