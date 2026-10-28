document.addEventListener('DOMContentLoaded', () => {
    const swatches = document.querySelectorAll('.swatch');
    const colorNameElem = document.getElementById('active-color-name');
    const stackBaseColor = document.getElementById('stackBaseColor');
    const carImages = document.querySelectorAll('.car-image');

    swatches.forEach(swatch => {
        swatch.addEventListener('click', function() {
            const selectedColor = this.getAttribute('data-color');
            const selectedName = this.getAttribute('data-name');

            swatches.forEach(s => {
                s.classList.remove('active');
                s.setAttribute('aria-pressed', 'false');
            });

            this.classList.add('active');
            this.setAttribute('aria-pressed', 'true');

            if (colorNameElem) colorNameElem.textContent = selectedName;

            if (stackBaseColor && this.dataset.hex) {
                stackBaseColor.style.background = `linear-gradient(90deg, ${this.dataset.hex}, #000)`;
            }

            carImages.forEach(img => {
                if (img.id === `car-${selectedColor}`) {
                    img.classList.add('active');
                } else {
                    img.classList.remove('active');
                }
            });
        });
    });
});