from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    problem = models.TextField()

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name_plural = 'Contacts'
