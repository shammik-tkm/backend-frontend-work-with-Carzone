document.addEventListener('DOMContentLoaded', () => {
    // Scrollspy (podsvetka menyu)
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('#desktopNav .nav-link');

    const highlightNav = () => {
        const y = window.pageYOffset;
        sections.forEach(cur => {
            const top = cur.offsetTop - 120;
            if (y > top && y <= top + cur.offsetHeight) {
                navLinks.forEach(l => {
                    l.classList.toggle('active', l.getAttribute('href') === `#${cur.id}`);
                });
            }
        });
    };

    // Progressbar, ToTop button, compact header
    const bar = document.getElementById('scrollBar');
    const toTop = document.getElementById('toTop');
    const header = document.querySelector('header.fixed');

    const onScroll = () => {
        const y = window.scrollY;
        const max = document.documentElement.scrollHeight - window.innerHeight;
        if (bar) bar.style.width = (max > 0 ? (y / max) * 100 : 0) + '%';
        if (toTop) toTop.classList.toggle('show', y > 600);
        if (header) header.classList.toggle('is-scrolled', y > 40);
    };

    window.addEventListener('scroll', highlightNav);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
});