from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER, null=True)
    birth_date = models.DateField()
    image = models.ImageField(default='anonim.jpg', upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username} -- Profile'