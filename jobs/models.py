from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class jobSeeker(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50)
    mobileNum = models.IntegerField()
    bio = models.TextField(blank=True)
    resume = models.FileField(null=True,blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.fullName}"
    

class jobProvider(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    mobileNum = models.IntegerField()
    jobDesc = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.fullName}"
    

class jobDesc(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    companyName = models.CharField(max_length=50)
    aboutCompany = models.TextField(max_length=1000)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    experience = models.IntegerField()
    qualifications = models.TextField(max_length=300)
    responsibilities = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.id} | {self.role} | {self.companyName}"
    
    

