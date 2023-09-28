from django.db import models

class Watches(models.Model):
    OPERATING_PRINCIPLE = (
        ('механические', 'механические'),
        ('электронные', 'электронные'),
        ('кварцевые', 'кварцевые')
    )
    CHARACTERISTICS = (
        ('обычный', 'обычный'),
        ('водонепроницаемый', 'водонепроницаемый'),
    )
    title = models.CharField('Укажите название часов', max_length=100,null=True)
    description = models.TextField('Укажите описание часов', blank=True,null=True)
    image = models.ImageField('Добавьте фото', upload_to='images/',null=True)
    made_in = models.TextField('Производитель',null=True)
    cost = models.PositiveIntegerField('Укажите цену',null=True)
    watches_author = models.TextField('Укажите создателя часов',null=True)
    operating_principle = models.CharField('Укажите принцип работы часов',max_length=100,choices=OPERATING_PRINCIPLE,null=True)
    characteristics = models.CharField('Укажите характеристику часов',max_length=100,choices=CHARACTERISTICS,null=True)
    data_of_made = models.PositiveIntegerField('Укажите год производства',null=True)
    video_of_watches = models.URLField('Укажите ссылку на видео часов',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новинку'
        verbose_name_plural = 'Новинки'
