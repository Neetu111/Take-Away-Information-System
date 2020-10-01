from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
from django.db import models

# Create your models here.

Preferred_Food_Choice = (('Indian', ('Indian')),
                         ('Chinese', ('Chinese')),
                         ('Italian',('Italian')),
                         ('Greek', ('Greek')),
                         ('Other', ('Other')))
Payment_Method = (('Online', ('Online')),
                  ('In Store', ('In Srote')))

Food_Status = (('Preparing', ('Preparing')),
               ('Ready', ('Ready')))

Food_Types = (('Burgers', ('Burgers')),
               ('Wraps', ('Wraps')),
              ('Meal Options', ('Meal Options')),
              ('Snacks', ('Snacks')))

class Person(models.Model):
    PID = models.CharField(max_length=6, primary_key=True)
    First_Name = models.CharField(max_length=400)
    Last_Name = models.CharField(max_length=400)
    Password = models.CharField(max_length=32)
    Country = models.CharField(max_length=400)
    City = models.CharField(max_length=400)
    Email = models.CharField(max_length=400)
    Contact_Number = models.CharField(max_length=400)

    def __str__(self):
        return str(self.PID) + ' ' + str(self.First_Name)

class Customer(models.Model):
    PID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Join_Date = models.DateField(("Date"), default=date.today)
    Feedback = models.CharField(max_length=400, null=True)
    Preferred_Food_Taste = models.TextField(choices = Preferred_Food_Choice, default="Indian")
    Card_Number = models.CharField(max_length=400, null=True)
    Card_Exp_Date = models.DateField(("Date"), default=date.today)
    Card_CVV = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    Card_Valid = models.BooleanField()

    def __str__(self):
        return str(self.PID) + ' ' + str(self.Join_Date)

class Business_Owner(models.Model):
    PID = models.ForeignKey(Person, on_delete=models.CASCADE)
    ABN = models.DecimalField(max_digits=11, decimal_places=0, null=False)

    def __str__(self):
        return str(self.PID) + ' ' + str(self.ABN)

class Menu(models.Model):
    MID = models.CharField(max_length=6, primary_key=True)
    Price = models.DecimalField(max_digits=4, decimal_places=2, null=False)

    def __str__(self):
        return str(self.MID) + ' ' + str(self.Price)

class Menu_Prepare(models.Model):
    MID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    PID = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('MID','PID'),)

    def __str__(self):
        return str(self.MID) + ' ' + str(self.PID)

class Food(models.Model):
    MID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    Name = models.CharField(max_length=60)
    Ingredient = models.CharField(max_length=1000)
    Food_Type = models.TextField(choices = Food_Types, default= 'Burgers', null=False)

    def __str__(self):
        return str(self.MID) + ' ' + str(self.Name) + '' + str(self.Ingredient) + '' + str(self.Food_Type )

class Drink(models.Model):
    MID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.MID) + ' ' + str(self.Name)

class Order(models.Model):
    OID = models.CharField(max_length=6, primary_key=True)
    Payment_Method = models.TextField(choices = Payment_Method)
    Status = models.TextField(choices = Food_Status)
    Waiting_Time = models.TimeField()

    def __str__(self):
        return str(self.OID) + ' ' + str(self.Status)

class Order_Feedback(models.Model):
    OID = models.ForeignKey(Order, on_delete=models.CASCADE)
    PID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Feedback = models.CharField(max_length=1000)

    class Meta:
        unique_together = (('OID','PID'),)

    def __str__(self):
        return str(self.OID) + ' ' + str(self.PID)

class Create_Your_Own_Food(models.Model):
    OID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Preferred_Food_Taste = models.TextField(choices = Preferred_Food_Choice)

    def __str__(self):
        return str(self.OID) + ' ' + str(self.Preferred_Food_Taste)

class Customize(models.Model):
    OID = models.ForeignKey(Order, on_delete=models.CASCADE)
    MID = models.ForeignKey(Menu, on_delete=models.CASCADE)
    Changes = models.CharField(max_length=1000)

    class Meta:
        unique_together = (('MID','OID'),)

    def __str__(self):
        return str(self.OID) + ' ' + str(self.MID)

class Pick(models.Model):
    OID = models.ForeignKey(Order, on_delete=models.CASCADE)
    MID = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('MID','OID'),)

    def __str__(self):
        return str(self.MID) + ' ' + str(self.OID)


