from django.db import models

# Create your models here.


#this class is for my assignment management
class Myassignment(models.Model):
    task_name                   = models.CharField(max_length=50)
    task_description            = models.TextField(max_length=500)
    task_purpose                = models.TextField(max_length=500)
    task_key_goal_indicators    = models.IntegerField(null=True, blank=True, default=0)
    
    def __str__(self):
        return self.task_name

