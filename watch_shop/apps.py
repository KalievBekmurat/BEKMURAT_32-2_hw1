from django.apps import AppConfig


class CustomUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_users'


class WatchShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'watch_shop'
    verbose_name = 'Часы'
    verbose_name = 'Отзывы'