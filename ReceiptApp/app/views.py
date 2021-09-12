import json
import requests
from django.shortcuts import render
from .forms import ItemForm
from datetime import *

today_date = date.today()
today_time = datetime.now().strftime("%H:%M:%S")


def home(request):
    form = ItemForm()
    return render(request, 'homepage.html', {'form': form})


URL = "https://antstackbillingapi.herokuapp.com/billing/"


def receipt(request):
    if request.method == 'POST':
        category = request.POST['category']
        item = request.POST['item']
        price = request.POST['price']
        quantity = request.POST['quantity']
        data = {
            'category': category,
            'item': item,
            'quantity': int(quantity),
            'price': int(price),
            'date': str(today_date),
            'time': str(today_time)
        }
        json_data = json.dumps(data)
        r = requests.post(url=URL, data=json_data)
        data = r.json()
        item = data.get('item')
        price = data.get('price')
        quantity = data.get('quantity')
        total = data.get('total')
        date_now = data.get('date')
        time_now = data.get('time')

        return render(request, 'receipt.html', {'item': item, 'price': price, 'quantity': quantity,
                                                'total': total, 'date': date_now, 'time': time_now})
