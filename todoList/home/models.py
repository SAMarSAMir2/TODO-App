from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField(null=True , blank=True)
    time = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle
