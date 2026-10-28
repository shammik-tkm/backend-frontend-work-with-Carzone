function moveSlider(input) {
        const container = input.closest('.before-after-container');
        const beforeImg = container.querySelector('.before-image');
        const sliderLine = container.querySelector('.slider-line');
        const val = input.value + '%';
        
        beforeImg.style.width = val;
        sliderLine.style.left = val;
    }

    // Автоматическая подгонка ширины внутреннего изображения До
    function adjustBeforeImgWidth() {
        document.querySelectorAll('.before-after-container').forEach(container => {
            const width = container.offsetWidth;
            const fullImg = container.querySelector('.w-full-container');
            if (fullImg) {
                fullImg.style.width = width + 'px';
            }
        });
    }

    window.addEventListener('resize', adjustBeforeImgWidth);
    window.addEventListener('DOMContentLoaded', adjustBeforeImgWidth);