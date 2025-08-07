import json
json_data='{"name":"June","contact":{"email":"june@example.com","city":"Paris"}}'
value=json.loads(json_data)
print(f"{value["contact"]["email"],value["contact"]["city"]}")