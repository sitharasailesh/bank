from django.db import models

class District(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Branch(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Account(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    ACCOUNT_TYPE_CHOICES = [('S', 'Savings'), ('C', 'Current')]


    name = models.CharField(max_length=200,blank=True)
    dob = models.DateField(blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True)
    phone_number = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    district = models.ForeignKey(to=District, on_delete=models.CASCADE,blank=True)
    branch = models.ForeignKey(to=Branch, on_delete=models.CASCADE,blank=True)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES,blank=True)


