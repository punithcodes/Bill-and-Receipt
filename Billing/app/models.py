from django.db import models

# These are the categories which can be choose by user.
CATEGORY_CHOICES = (
    ('Medicine', 'Medicine'),
    ('Food', 'Food'),
    ('Cloths', 'Cloths'),
    ('CD/DVD', 'CD/DVD'),
    ('Books', 'Books'),
    ('Imported', 'Imported'),
    ('Pants', 'Pants')
)


# This class is responsible for creating user bill.
class BillingModel(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

