from django.db import models
from django.utils.text import slugify
from courses.models import Category 
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50,null=True)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="", blank="", null=False, unique = True, db_index=True)
    category = models.ForeignKey(Category, default = 1, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)




class Categoriest(models.Model):

    id =models.IntegerField(primary_key=True)
    name =models.TextField()
    slug =models.TextField()


    def __str__(self):
        return f"{self.name}"
    





