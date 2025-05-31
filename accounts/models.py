from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, DateField, \
    TextField, CharField


class UserProfile(Model):
    user = OneToOneField(User, on_delete=CASCADE, unique=True)
    date_of_birth = DateField(null=True, blank=True)
    phone = CharField(null=True, blank=True)
    biography = TextField(null=True, blank=True)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f"UserProfile(user={self.user})"

    def __str__(self):
        return self.user.username
