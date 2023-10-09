from django.db import models
from django.contrib.auth.models import User
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





ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'Администратор'),
    (VIPClient, 'VIP Клиент'),
    (CLIENT, 'Клиент')
)


MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE , 'M'),
    (FEMALE, 'Ж')


)

CARD_NUMBER = (
    ('MBANK','MBANK'),
    ('OPTIMA','OPTIMA'),
    ('DEMIR','DEMIR'),
    ('RSK','RSK'),
    ('BAKAI','BAKAI'),
)
MESSENGERS = (
    ('instagram','instagram'),
    ('facebook','facebook'),
    ('twitter','twitter'),
    ('whatsapp','whatsapp'),
)

class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    user_type = models.IntegerField(choices=USER_TYPE,
                                    verbose_name='Выберите тип пользователя')
    phone_number = models.CharField('Ваш сотовый:',max_length=13)
    age = models.PositiveIntegerField('Укажите возраст', default=15)
    gender = models.IntegerField(choices=GENDER_TYPE,verbose_name='Ваш пол')
    town = models.TextField(max_length=1000, verbose_name='Ваш город?',null=True)
    adress = models.CharField('Фактическое место проживания',max_length=100, null=True)
    card_number = models.PositiveIntegerField(choices=CARD_NUMBER,verbose_name='выберите карту', null=True)
    education = models.TextField('Какое у вас образование?',null=True)
    messengers = models.CharField(max_length=100,choices=MESSENGERS,verbose_name='Выберите приложение через которое вы желаете с нами контактировать ',null=True)
    data_of_birth = models.CharField(max_length=100,verbose_name='ваша дата рождения' ,null=True)
    nationality = models.TextField('Ваша национальность', null=True)



