from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    prod_desc = models.TextField()
    prod_category = models.CharField(max_length=50)
    prod_img = models.ImageField(upload_to='products/')
    prod_qty = models.IntegerField()


class NewEntry(models.Model):
    stud_reg=models.IntegerField(max_length=10)
    stud_name=models.CharField(max_length=100)
    stud_course=models.CharField(max_length=100)


    #anytime you make changes to models you MUST run migrations
    # python manage.py makemigrations
    # python manage.py migrate