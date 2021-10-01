from .serializers import BillingSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Here I have defined %tax based on categories.
category_tax = {'Medicine': 5, 'Cloths': 5, 'CD/DVD': 3, 'Food': 5, 'Imported': 18, 'Books': 0, 'Pants': 5}


''' This function is responsible for getting data from the client and sending back the required data in a JSON format as a response. 
Rather than choosing Mixins or Concrete classes, purposely I have coded each step how Api gets data from client , do calculations and send it back to client'''
@csrf_exempt
def billing_api(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = BillingSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            print('done')
            category = python_data.get('category')
            item = python_data.get('item')
            price = python_data.get('price')
            quantity = python_data.get('quantity')
            today_date = python_data.get('date')
            today_time = python_data.get('time')
            total_price = price * quantity
            tax = calculate_tax(total_price, category)
            total_tax = (total_price * tax) / 100
            bill = total_price + total_tax
            amount_to_pay = final_bill(bill)
            final_receipt = {'total': amount_to_pay, 'item': item, 'quantity': quantity, 'price': price,
                             'date': today_date, 'time': today_time}

            return JsonResponse(final_receipt, safe=False)

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


# This function is responsible for calculating the total tax based on category and quantity.
def calculate_tax(total_price, category):
    if category.lower() == 'cloths':
        if total_price < 1000:
            tax = category_tax.get(category)
        elif total_price >= 1000:
            tax = 12
        return tax
    else:
        tax = category_tax.get(category)
        return tax


# This function is responsible for calculating the finall bill amount of the client.
def final_bill(bill):
    if bill > 2000:
        total_bill = (bill * 5) / 100
        amount = bill - total_bill
    else:
        amount = bill
    return amount
