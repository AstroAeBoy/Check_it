from django.db import models


# Create your models here.
class Tour:
    """
    Instantiates the Travel places with user data
    """
    def __init__(self, id, place, desc, price):
        self.id = id
        self.place = place
        self.desc = desc
        self.price = price
