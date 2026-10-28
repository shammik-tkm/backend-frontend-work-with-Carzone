// Движение слайдера До/После
function moveSlider(input) {
    const container = input.closest('.before-after-container');
    const beforeImg = container.querySelector('.before-image');
    const sliderLine = container.querySelector('.slider-line');
    const val = input.value + '%';
    
    beforeImg.style.width = val;
    sliderLine.style.left = val;
}

// Выравнивание ширины оригинальной картинки До
function adjustBeforeImgWidth() {
    document.querySelectorAll('.before-after-container').forEach(container => {
        const width = container.offsetWidth;
        const fullImg = container.querySelector('.w-full-container');
        if (fullImg) {
            fullImg.style.width = width + 'px';
        }
    });
}

// Фильтрация по категориям
function filterGallery(category) {
    const items = document.querySelectorAll('.gallery-item');
    const buttons = document.querySelectorAll('.filter-btn');

    buttons.forEach(btn => {
        btn.classList.remove('bg-brand-orange', 'text-black', 'active');
        btn.classList.add('bg-brand-card', 'text-brand-muted');
    });

    event.currentTarget.classList.remove('bg-brand-card', 'text-brand-muted');
    event.currentTarget.classList.add('bg-brand-orange', 'text-black', 'active');

    items.forEach(item => {
        if (category === 'all' || item.classList.contains(category)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
    
    adjustBeforeImgWidth();
}

// Модальное окно
function openModal(src, caption) {
    document.getElementById('modal-img').src = src;
    document.getElementById('modal-caption').innerText = caption;
    document.getElementById('image-modal').classList.remove('hidden');
    document.getElementById('image-modal').classList.add('flex');
}

function closeModal() {
    document.getElementById('image-modal').classList.add('hidden');
    document.getElementById('image-modal').classList.remove('flex');
}

window.addEventListener('resize', adjustBeforeImgWidth);
window.addEventListener('DOMContentLoaded', adjustBeforeImgWidth);