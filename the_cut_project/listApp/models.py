from django.db import models

# Create your models here.


class Categories(models.Model):
    cat_name=models.CharField(max_length=30,unique=True)
    cat_description=models.CharField(max_length=30,unique=False)
    cat_views=models.IntegerField(default=0)

class List(models.Model):
    cat_id=models.IntegerField()
    list_name=models.CharField(max_length=20,unique=False)
    list_desc=models.CharField(max_length=120,unique=False)
    list_views=models.IntegerField(default=0)

class PageVisits(models.Model):
    page_name=models.CharField(max_length=20,unique=True)
    view_count=models.IntegerField(default=0)
