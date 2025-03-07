from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add price field

    def __str__(self):
        return self.Item_name



    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
     Description = models.TextField(blank=False)

class Feedback(models.Model):
   User_name = models.CharField(max_length=15)
   Descriptions = models.TextField(blank=False)
   rating = models.IntegerField()
   Image = models.ImageField(upload_to='items/',blank=True)

def __str__(self):
        return self.User_name 

class BookTable(models.Model):
   Name = models.CharField(max_length=15)
   Phone_number = models.IntegerField()
   Email = models.EmailField()
   Total_person = models.IntegerField()
   Booking_date = models.DateField()
def __str__(self):
        return self.Name
