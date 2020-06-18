from django.db import models


# Create your models here.
# class Tour:
#     """
#     Instantiates the Travel places with user data
#     """
#     def __init__(self, id, place, desc, price,image):
#         self.id = id
#         self.place = place
#         self.desc = desc
#         self.price = price
#         self.image=image

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
