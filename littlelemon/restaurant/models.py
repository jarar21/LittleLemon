from django.db import models

# Create your models here.

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.bookingdate}"

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # Changed from title to name
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.name} : ${self.price}"
