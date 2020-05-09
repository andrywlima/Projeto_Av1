from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Objeto(models.Model):
	 nome = models.CharField(max_length= 100)
	 descricao = models.CharField(max_length= 1000)
	 data = models.DateField(auto_now_add=False, auto_now=False, blank=True)
	 cell = models.CharField(max_length=11)
	 email = models.EmailField()
	 img = models.ImageField(upload_to='pertences')
	 active = models.BooleanField(default=True)
	 user = models.ForeignKey(User, on_delete=models.CASCADE)


	 def __str__(self):
	 	return str(self.id)


	 class meta:
	 	db_table = 'pertence' 