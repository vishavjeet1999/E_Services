from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class user_services(models.Model):
    image = models.ImageField(null=True, upload_to='media/')
    service_name = models.CharField(max_length=40)
    service_charges = models.IntegerField()
    service_description = models.CharField(max_length=500)
    service_rating = models.IntegerField()
    service_category = models.CharField(max_length=40)
    uploaded_by = models.CharField(max_length=40)
    service_long = models.DecimalField(
        max_digits=9, decimal_places=6)

    service_lat = models.DecimalField(
        max_digits=9, decimal_places=6)


class category(models.Model):
    image = models.ImageField(null=True, upload_to='media/')
    category_name = models.CharField(max_length=40)


class Comments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(user_services, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + "..." + " by " + self.user.username
