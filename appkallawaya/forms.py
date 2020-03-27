from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from appkallawaya.models import Post

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]


class UserForm(forms.Form):

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.favorite_fruit = self.self.widget = forms.RadioSelect(choices=FRUIT_CHOICES)
        if commit:
            user.save()

        return user


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email_name = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )


class HomeFormInit(forms.Form):
    example = forms.CharField(widget=forms.Textarea(), required=True)
