from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class extendeduser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	Contact_no=models.IntegerField()
	Service_No=models.IntegerField(null=True)
	Address=models.TextField(max_length=1000,null=True)
	Rank=models.CharField(max_length=20,null=True)
	Trade=models.CharField(max_length=20,null=True)
	Section=models.CharField(max_length=20,null=True)
	Unit=models.CharField(max_length=20,null=True)
	Ip_NO=models.IntegerField()
	def __str__(self):
		return self.Ip_NO



