from django.db import models

class UserProfile(models.Model):
	name  = models.CharField(max_length=100,blank=False)
	email = models.EmailField(max_length= 70,unique=True)
	college = models.CharField(max_length=100)
	phone_no = models.CharField(max_length=10,unique=True)


	def __str__(self):
		return self.name
