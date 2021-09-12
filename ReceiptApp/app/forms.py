from django import forms

CATEGORY_CHOICES = (
    ('Medicine', 'Medicine'),
    ('Food', 'Food'),
    ('Cloths', 'Cloths'),
    ('CD/DVD', 'CD/DVD'),
    ('Books', 'Books'),
    ('Imported', 'Imported'),
    ('Pants', 'Pants')
)


class ItemForm(forms.Form):
    category = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES))
    item = forms.CharField(max_length=50)
    quantity = forms.IntegerField()
    price = forms.IntegerField()
