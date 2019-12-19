from django.db import models

# Create your models here.
class Project(models.Model):
	choices=[('PRP','PROPOSED'),('CMP','COMPLETED'),('CNC','CANCELLED'),('HLT','HALTED')]
	name=models.TextField()
	start_date=models.DateTimeField(null=True,blank=True)
	status=models.CharField(max_length=3,choices=choices,default='PRP')
	link=models.TextField(blank=True)
	def __str__(self):
		return self.name
		
