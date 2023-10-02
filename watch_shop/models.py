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


class Reviews(models.Model):
    REVIEW_STARS = (
        ('1','1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    review_object = models.ForeignKey(Watches, on_delete=models.CASCADE, related_name='comment_object')
    review_text = models.TextField('напишите отзыв')
    review_stars = models.CharField(max_length=100, choices=REVIEW_STARS)
    reviews_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
    def __str__(self):
        return self.review_text







