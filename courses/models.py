from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50,null=True)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()


    def __str__(self):
        return f"{self.title} {self.date}"

class Categoriest(models.Model):

    id =models.IntegerField(primary_key=True)
    name =models.TextField()
    slug =models.TextField()


    def __str__(self):
        return f"{self.name}"
    
    





