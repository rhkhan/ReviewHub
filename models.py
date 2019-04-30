from django.db import models
from django.utils import timezone
import datetime


USER_TYPES=(
	('CLIENT','client'),
	('FRELANCERS','freelancers')
)

class Country(models.Model):
    country_name = models.CharField(max_length=200)
	
    def __str__(self):
        return self.country_name


class Project(models.Model):
	client=models.ForeignKey('User',on_delete=models.CASCADE,related_name='+',limit_choices_to={'user_type': 'CLIENT'}) #related_name is used to avoid cascading problem
	project_name=models.CharField(max_length=500)
	completion_date=models.DateField()
	freelance=models.ForeignKey('User',on_delete=models.CASCADE,related_name='+',limit_choices_to={'user_type': 'FRELANCERS'})
	comments=models.TextField()
	project_description=models.CharField(max_length=10000,blank=True)
	project_techs=models.CharField(max_length=200,blank=True)

#class ProjectDetails(models.Model):
	#project=models.ForeignKey(Project,on_delete=models.CASCADE)
	#project_description=models.CharField(max_length=1000)
	#project_techs=models.CharField(max_length=200)
			

class Freelancer(models.Model):
	country=models.ForeignKey(Country,on_delete=models.CASCADE)
	freelancer_name=models.CharField(max_length=200)

	def __str__(self):
		return self.freelancer_name

class User(models.Model):
	full_name=models.CharField(max_length=200)
	country=models.ForeignKey(Country, on_delete=models.CASCADE)
	user_name=models.CharField(max_length=100)
	user_password=models.CharField(max_length=50)
	user_type=models.CharField(max_length=20,choices=USER_TYPES)
	creation_date=models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.full_name
	