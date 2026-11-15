from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField('Kategoriename', max_length=100)
    slug = models.SlugField(
        'URL-Kennung (z. B. smart-repair)',
        unique=True,
        max_length=100
    )

    class Meta:
        verbose_name = 'Galeriekategorie'
        verbose_name_plural = 'Galeriekategorien'

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    title = models.CharField(
        'Titel (z. B. Mazda 3 – Seitenwand)',
        max_length=255
    )
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Kategorie'
    )
    badge_text = models.CharField(
        'Leistungsbezeichnung',
        max_length=100,
        default='Smart Repair'
    )
    description = models.TextField('Beschreibung', blank=True, null=True)

    image_before = models.ImageField(
        'Vorher-Bild',
        upload_to='gallery/before/'
    )
    image_after = models.ImageField(
        'Nachher-Bild',
        upload_to='gallery/after/'
    )

    is_active = models.BooleanField('Auf der Website anzeigen', default=True)
    created_at = models.DateTimeField('Erstellt am', auto_now_add=True)

    class Meta:
        verbose_name = 'Referenzarbeit (Vorher/Nachher)'
        verbose_name_plural = 'Referenzarbeiten (Vorher/Nachher)'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ContactInquiry(models.Model):
    name = models.CharField('Name', max_length=150)
    phone = models.CharField('Telefonnummer', max_length=50, blank=True)
    email = models.EmailField('E-Mail-Adresse')
    service = models.CharField('Gewünschte Dienstleistung', max_length=100)
    message = models.TextField('Nachricht')
    photo = models.ImageField(
        'Foto des Fahrzeugschadens',
        upload_to='inquiries/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField('Eingegangen am', auto_now_add=True)

    class Meta:
        verbose_name = 'Kundenanfrage'
        verbose_name_plural = 'Kundenanfragen'

    def __str__(self):
        return f'{self.name} – {self.service} ({self.created_at.strftime("%d.%m.%Y")})'