#load as dict and print product+price separated by space
import json
input_data = '{"product": "Book", "price": 9.99}'
value = json.loads(input_data)
print(f"{value['product']} {value['price']}")

import json
input_data = '{"product": "Book", "price": 9.99}'
value = json.loads(input_data)
print(f"{value['product'],value['price']}")
