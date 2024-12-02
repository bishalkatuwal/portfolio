from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_no = models.CharField(max_length=15) 
    message = models.TextField()

    def __str__(self):
        return f"{self.name} "
    

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Projects(models.Model):
    title = models.CharField(max_length=100)
    project_img = models.ImageField(upload_to='images/')
    technologies = models.ManyToManyField(Technology)
    descriptions = FroalaField()



    def __str__(self):
        return f"{self.title}"
