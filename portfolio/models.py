from django.db import models



class Contact(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    subject = models.CharField(max_length=200)
    messsage = models.TextField()


    def __str__(self):
        return self.your_name
