import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField, NumberInput

from viewer.models import Genre, Country, Creator


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        labels = {
            'name': 'Název žánru'
        }

    def clean_name(self):
        initial = self.cleaned_data['name']
        return initial.capitalize()


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        labels = {
            'name': 'Název země'
        }

    def clean_name(self):
        initial = self.cleaned_data['name']
        if len(initial) < 4:
            return initial.upper()
        return initial.capitalize()


class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
        #fields = ['name', 'surname']
        #exclude = ['date_of_birth', 'date_of_death']

        labels = {
            'name': 'Jméno',
            'surname': 'Příjmení',
            'country': 'Země',
            'date_of_birth': 'Datum narození',
            'date_of_death': 'Datum úmrtí',
            'biography': 'Biografie'
        }

    date_of_birth = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label='Datum narození')
    date_of_death = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label='Datum úmrtí')

    def clean_name(self):
        initial = self.cleaned_data['name']
        if initial:
            return initial.capitalize()
        return initial

    def clean_surname(self):
        initial = self.cleaned_data['surname']
        if initial:
            return initial.capitalize()
        return initial

    def clean_date_of_birth(self):
        initial = self.cleaned_data['date_of_birth']
        if initial and initial > date.today():
            raise ValidationError("Datum narození nesmí být v budoucnosti.")
        return initial

    def clean_date_of_death(self):
        initial = self.cleaned_data['date_of_death']
        if initial and initial > date.today():
            raise ValidationError("Datum úmrtí nesmí být v budoucnosti.")
        return initial

    def clean_biography(self):
        initial = self.cleaned_data['biography']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        cleaned_data = super().clean()
        initial_name = cleaned_data['name']
        initial_surname = cleaned_data['surname']
        error_message = ''
        if not initial_name and not initial_surname:
            #raise ValidationError("Je nutné zadat jméno nebo příjmení (nebo oboje).")
            error_message += "Je nutné zadat jméno nebo příjmení (nebo oboje). "

        initial_date_of_birth = cleaned_data['date_of_birth']
        initial_date_of_death = cleaned_data['date_of_death']
        if initial_date_of_birth and initial_date_of_death and initial_date_of_death < initial_date_of_birth:
            #raise ValidationError("Datum úmrtí nesmí být dřív, než datum narození.")
            error_message += "Datum úmrtí nesmí být dřív, než datum narození."

        if error_message:
            raise ValidationError(error_message)

        return cleaned_data
