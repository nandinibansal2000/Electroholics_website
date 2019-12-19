from django.db import models

# Create your models here.
class Session(models.Model):
	choices=[('PRP','PROPOSED'),('CMP','COMPLETED'),('CNC','CANCELLED'),('CNF','CONFIRMED')]
	name=models.TextField()
	date=models.DateTimeField(null=True,blank=True)
	status=models.CharField(max_length=3,choices=choices,default='PRP')
	link=models.TextField(blank=True)
	def __str__(self):
		return self.name
		

