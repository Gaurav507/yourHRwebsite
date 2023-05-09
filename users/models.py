from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

    def get_jobSeeker(self):
        if(hasattr(self, 'jobSeeker')):
            return self.get_jobSeeker
        return None
        
    def get_jobProvider(self):
        if(hasattr(self, 'jobProvider')):
            return self.get_jobProvider
        return None
    

