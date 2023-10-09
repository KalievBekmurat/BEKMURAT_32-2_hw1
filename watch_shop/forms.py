from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
class WatchShopForm(forms.ModelForm):
    class Meta:
        model = models.Watches
        fields = '__all__'


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
    (MALE, 'M'),
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


class RegistrationNewForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE,required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE,required=True)
    town = forms.CharField(max_length=1000, required=True)
    adress = forms.CharField( max_length=100, required=True)
    card_number = forms.ChoiceField(choices=CARD_NUMBER,required=True)
    education = forms.CharField( max_length=100 ,  required=False)
    messengers = forms.ChoiceField(choices=MESSENGERS ,
                                  required=False)
    data_of_birth = forms.CharField( required=False)
    nationality = forms.CharField( max_length=100 , required=False)


    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'town',
            'adress',
            'card_number',
            'education',
            'messengers',
            'data_of_birth',
            'nationality',
        )

    def save(self, commit=True):
        user = super(RegistrationNewForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


