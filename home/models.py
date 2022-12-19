from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=400)
    post = models.CharField(max_length=500)
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=400, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=150)
    logo = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name

class Address(models.Model):
    logo = models.CharField(max_length=300)
    add = models.CharField(max_length=200)
    street = models.CharField(max_length=200)

    def __str__(self):
        return self.add

class Phone(models.Model):
    logo = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    working = models.CharField(max_length=200)

class Email(models.Model):
    logo = models.CharField(max_length=300)
    email_address = models.EmailField(max_length=150)
    query = models.CharField(max_length=200)




