# Generated by Django 4.2.5 on 2023-10-08 10:15

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('watch_shop', '0006_alter_reviews_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.IntegerField(choices=[(1, 'Администратор'), (2, 'VIP Клиент'), (3, 'Клиент')], verbose_name='Выберите тип пользователя')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Ваш сотовый:')),
                ('age', models.PositiveIntegerField(default=15, verbose_name='Укажите возраст')),
                ('gender', models.IntegerField(choices=[(1, 'M'), (2, 'Ж')], verbose_name='Ваш пол')),
                ('town', models.TextField(max_length=1000, null=True, verbose_name='Ваш город?')),
                ('adress', models.CharField(max_length=100, null=True, verbose_name='Фактическое место проживания')),
                ('card_number', models.PositiveIntegerField(choices=[('MBANK', 'MBANK'), ('OPTIMA', 'OPTIMA'), ('DEMIR', 'DEMIR'), ('RSK', 'RSK'), ('BAKAI', 'BAKAI')], null=True, verbose_name='выберите карту')),
                ('education', models.TextField(null=True, verbose_name='Какое у вас образование?')),
                ('messengers', models.CharField(choices=[('instagram', 'instagram'), ('facebook', 'facebook'), ('twitter', 'twitter'), ('whatsapp', 'whatsapp')], max_length=100, null=True, verbose_name='Выберите приложение через которое вы желаете с нами контактировать ')),
                ('data_of_birth', models.CharField(max_length=100, null=True, verbose_name='ваша дата рождения')),
                ('nationality', models.TextField(null=True, verbose_name='Ваша национальность')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
