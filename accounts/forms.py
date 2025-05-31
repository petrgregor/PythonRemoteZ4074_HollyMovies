from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, PasswordInput, DateField, NumberInput, \
    Textarea

from accounts.models import UserProfile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']

        labels = {
            'username': 'Uživatelské jméno',
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'email': 'E-mail'
        }

    password1 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo'}),
        label='Heslo'
    )

    password2 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo znovu'}),
        label='Heslo znovu'
    )

    date_of_birth = DateField(
        widget=NumberInput(attrs={'type': 'date'}),
        label='Datum narození',
        required=False
    )

    phone = CharField(
        label='Telefon',
        required=False
    )

    biography = CharField(
        widget=Textarea(),
        label='Biografie',
        required=False
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)  # vytvoříme uživatele

        # ještě potřebujeme vytvořit UserProfile
        date_of_birth = self.cleaned_data.get('date_of_birth')
        phone = self.cleaned_data.get('phone')
        biography = self.cleaned_data.get('biography')
        user_profile = UserProfile(
            user=user,
            date_of_birth=date_of_birth,
            phone=phone,
            biography=biography
        )
        if commit:
            user_profile.save()
        return user

