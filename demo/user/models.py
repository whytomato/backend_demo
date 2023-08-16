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

class UserLoginInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    device_info = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    login_status = models.CharField(max_length=10)  # 登录状态，例如 'success' 或 'failure'
    login_type = models.CharField(max_length=20)  # 登录类型，例如 'username_password' 或 'third_party'

    class Meta:
        ordering = ['-login_time']  # 按登录时间倒序排序
        db_table='UserLoginInfo'

class Login_info(models.Model):
    user_id=models.CharField("user_id",max_length=1000)
    num=models.IntegerField("num")
    class Meta:
        db_table='Login_info'
# Create your models here.
