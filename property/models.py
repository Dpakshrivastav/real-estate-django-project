from django.db import models


class House(models.Model):
    house_no = models.CharField(max_length=50)
    registry_no = models.CharField(max_length=100)
    property_pic = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
    property_type = models.CharField(max_length=50)
    property_style = models.CharField(max_length=50)
    property_region = models.CharField(max_length=50)
    size = models.CharField(max_length=5)
    no_of_kitchen = models.CharField(max_length=5)
    no_of_bedroom = models.CharField(max_length=5)
    no_of_bathroom = models.CharField(max_length=5)
    year_built = models.CharField(max_length=5)
    price = models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.house_no


class HouseOwnerDetails(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, )
    lastname = models.CharField(max_length=100, null=True)
    contact_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=2000)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    pin = models.IntegerField(max_length=6)


    def __str__(self):
        return self.contact_no


class HouseAddress(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    block = models.CharField(max_length=50)
    sec = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pin = models.IntegerField(max_length=6)

    def __str__(self):
        return self.block + '  ' + self.sec + '  ' + self.state
