from django.db import models

# Create your models here.

class personal_info(models.Model):
	CHOICES = [
	('ANE','Aeronautical Engineering'),
	('AGR','Agricultural Engineering'),
	('AUT','Automobile Engineering'),
	('BIO','Bio-Technology'),
	('CHE','Chemical Engineering'),
	('CIV','Civil Engineering'),
	('CSE','Computer Science & Engineering'),
	('EEE','Electrical & Electronics Engineering'),
	('INF','Information Technology'),
	('MEC','Mechanical Engineering'),
	]	

	name = models.CharField(max_length=40)	
	email = models.EmailField(max_length=40)	
	phone = models.DecimalField(decimal_places=0,max_digits=15)	
	photo = models.ImageField(upload_to='media/')	
	video = models.FileField(upload_to='media/')	
	stream=models.CharField(
		max_length=3,
		choices=CHOICES,
		)


	def __str__(self):
		return self.name
