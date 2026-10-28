// document.addEventListener('DOMContentLoaded', () => {
//     const contactForm = document.getElementById('contactForm');

//     if (contactForm) {
//         contactForm.addEventListener('submit', (e) => {
//             e.preventDefault();
//             const name = document.getElementById('name').value;
//             const phone = document.getElementById('phone').value;
//             const email = document.getElementById('email').value;
//             const service = document.getElementById('service').value;
//             const message = document.getElementById('message').value;

//             const subject = encodeURIComponent(`Anfrage von ${name} - ${service}`);
//             const body = encodeURIComponent(
//                 `Name: ${name}\nTelefon: ${phone}\nE-Mail: ${email}\nLeistung: ${service}\n\nNachricht:\n${message}`
//             );
//             window.location.href = `mailto:adbworkteam@gmail.com?subject=${subject}&body=${body}`;
//         });
//     }
// });

function updateFileName(input) {
    const label = document.getElementById('file-label');
    if (input.files && input.files.length > 0) {
        label.textContent = `Ausgewählt: ${input.files.length} Datei(en)`;
        label.classList.add('text-brand-orange');
    } else {
        label.textContent = 'Klicken Sie hier, um Fotos auszuwählen';
        label.classList.remove('text-brand-orange');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('name').value;
            const phone = document.getElementById('phone').value;
            const email = document.getElementById('email').value;
            const service = document.getElementById('service').value;
            const message = document.getElementById('message').value;
            const fileInput = document.getElementById('photos');

            let text = `Hallo CARZONA,\n\n`;
            text += `Ich habe eine Anfrage:\n`;
            text += `• Name: ${name}\n`;
            if (phone) text += `• Telefon: ${phone}\n`;
            text += `• E-Mail: ${email}\n`;
            text += `• Leistung: ${service}\n`;
            text += `• Nachricht: ${message}\n`;

            if (fileInput && fileInput.files.length > 0) {
                text += `\n(Ich sende die Fotos direkt in diesem Chat mit)`;
            }

            const encodedText = encodeURIComponent(text);
            const whatsappUrl = `https://wa.me/491729039100?text=${encodedText}`;

            window.open(whatsappUrl, '_blank');
        });
    }
});