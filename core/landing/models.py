from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField('Slug (например: smart-repair)', unique=True, max_length=100)

    class Meta:
        verbose_name = 'Категория галереи'
        verbose_name_plural = 'Категории галереи'

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    title = models.CharField('Заголовок (например: Mazda 3 — Seitenwand)', max_length=255)
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='items', verbose_name='Категория')
    badge_text = models.CharField('Тэг (например: Smart Repair)', max_length=100, default='Smart Repair')
    description = models.TextField('Описание', blank=True, null=True)
    
    image_before = models.ImageField('Изображение (ДО)', upload_to='gallery/before/')
    image_after = models.ImageField('Изображение (ПОСЛЕ)', upload_to='gallery/after/')
    
    is_active = models.BooleanField('Отображать на сайте', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Работа (До/После)'
        verbose_name_plural = 'Работы (До/После)'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ContactInquiry(models.Model):
    name = models.CharField('Имя', max_length=150)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    email = models.EmailField('E-Mail')
    service = models.CharField('Услуга', max_length=100)
    message = models.TextField('Сообщение')
    photo = models.ImageField('Фото повреждения', upload_to='inquiries/', blank=True, null=True)
    created_at = models.DateTimeField('Дата заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.name} - {self.service} ({self.created_at.strftime("%Y-%m-%d")})'