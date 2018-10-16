from django.db import models


# Create your models here.


class House(models.Model):
    house_no = models.CharField(max_length=50)
    registry_no = models.CharField(max_length=100)
    property_pic = models.CharField(max_length=1000)
    property_type = models.CharField(max_length=50)
    property_style = models.CharField(max_length=50)
    property_region = models.CharField(max_length=50)
    Age = models.CharField(max_length=50)
    size = models.CharField(max_length=5)
    no_of_kitchen = models.CharField(max_length=5)
    no_of_bedroom = models.CharField(max_length=5)
    year_built = models.CharField(max_length=5, default=1990)
    price = models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.house_no


class HouseOwnerDetails(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=2000)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.contact_no


class HouseAddress(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    block = models.CharField(max_length=50)
    sec = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.block + '  ' + self.sec + '  ' + self.state
