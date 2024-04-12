from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# class Todo(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
    
class TaskList(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(default=timezone.now) 
	deadline = models.DateField(default=timezone.now) 
	completionStatus = models.BooleanField(default=False)
	userKey = models.ForeignKey(User, on_delete= models.CASCADE,  null=True, blank=True)#storing user_id
	def __str__(self):
		return f"{self.name}" 
	class Meta:
		order_with_respect_to = 'userKey'