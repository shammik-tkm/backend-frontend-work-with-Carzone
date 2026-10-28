document.getElementById('whatsapp-submit-btn').addEventListener('click', function () {
    const phoneNumber = "491729039100"; // Ваш номер WhatsApp без '+'

    // Получаем значения полей формы
    const name = document.getElementById('name').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const email = document.getElementById('email').value.trim();
    const service = document.getElementById('service').value;
    const message = document.getElementById('message').value.trim();

    // Простая проверка обязательных полей
    if (!name || !email || !message) {
    alert('Bitte füllen Sie alle Pflichtfelder aus.');
    return;
    }

    // Собираем текст сообщения с эмодзи и переносами строк (\n)
    let text = `Hallo CARZONA! 👋\n\n`;
    text += `Ich möchte eine Anfrage stellen:\n`;
    text += `👤 Name: ${name}\n`;
    if (phone) text += `📞 Telefon: ${phone}\n`;
    text += `✉️ E-Mail: ${email}\n`;
    text += `🛠️ Leistung: ${service}\n`;
    text += `📝 Nachricht: ${message}`;

    // Кодируем текст для безопасности передачи в URL
    const encodedText = encodeURIComponent(text);

    // Формируем и открываем ссылку WhatsApp
    const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodedText}`;
    window.open(whatsappUrl, '_blank');
});
