from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.group}: {self.content[:50]}..."
    
