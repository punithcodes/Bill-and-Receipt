# Bill-and-Receipt

This is small project which contains client side web application called "Receipt App" and REST api called "Billing App".
User can select category, enter item, quantity, price and press submit button to generate bill. 
The request goes to REST api that is "Billing App", it calculates based on quantity, amount per item and tax then sends final bill to the user in a JSON format. The "Receipt App" parse the JSON format into native data types and display the result/bill.

Tools and Technologies used :
- Python, Django, DRF
- Html, SQLite, Pycharm IDE
