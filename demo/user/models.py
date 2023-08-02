from django.db import models

class User(models.Model):
    username = models.CharField("name", max_length=100)
    password = models.CharField("password", max_length=20)
    email = models.CharField("email", max_length=30, null=True)

    class Meta:
        db_table = 'user'

class VerificationCode_info(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()

    def __str__(self):
        return self.email
    class Meta:
        db_table='VerificationCode_info'
# Create your models here.
