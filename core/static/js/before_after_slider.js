document.addEventListener('DOMContentLoaded', () => {
    const sliderBox = document.getElementById('sliderBox');
    const beforeLayer = document.getElementById('beforeLayer');
    const beforeImg = document.getElementById('beforeImg');
    const dragDivider = document.getElementById('dragDivider');

    if (sliderBox && beforeLayer && beforeImg && dragDivider) {
        let isDragging = false;

        const syncWidth = () => {
            beforeImg.style.width = `${sliderBox.offsetWidth}px`;
        };
        syncWidth();
        window.addEventListener('resize', syncWidth);

        const updateSlider = (clientX) => {
            const rect = sliderBox.getBoundingClientRect();
            const x = Math.max(0, Math.min(clientX - rect.left, rect.width));
            const pct = (x / rect.width) * 100;
            beforeLayer.style.width = `${pct}%`;
            dragDivider.style.left = `${pct}%`;
        };

        const getClientX = (e) => (e.touches && e.touches.length > 0 ? e.touches[0].clientX : e.clientX);

        sliderBox.addEventListener('mousedown', (e) => {
            isDragging = true;
            updateSlider(getClientX(e));
        });
        window.addEventListener('mousemove', (e) => {
            if (isDragging) updateSlider(getClientX(e));
        });
        window.addEventListener('mouseup', () => { isDragging = false; });

        sliderBox.addEventListener('touchstart', (e) => {
            isDragging = true;
            updateSlider(getClientX(e));
        }, { passive: true });
        window.addEventListener('touchmove', (e) => {
            if (isDragging) updateSlider(getClientX(e));
        }, { passive: true });
        window.addEventListener('touchend', () => { isDragging = false; });
    }
});