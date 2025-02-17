from django.db import models
from django.contrib.auth.models import User

class booking(models.Model):
 
    
  
    specialization = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name()} ({self.specialization})"


     