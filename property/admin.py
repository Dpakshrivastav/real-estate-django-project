from django.contrib import admin
from .models import House, HouseAddress, HouseOwnerDetails
# Register your models here.

admin.site.register(House)
admin.site.register(HouseOwnerDetails)
admin.site.register(HouseAddress)

