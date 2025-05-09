from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    # All custom fields for users can be added here.

    def __str__(self):
        return self.username
