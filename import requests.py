import requests

api_key = "oZQaqGhwliMAhP0XODZUiMESd4IukP_Kam8j7lpQfD_spak9Emho7egz"

url = "https://api.sellercenter.daraz.pk?Action=GetOrder&Format=json&OrderId=3538&Timestamp=2023-05-06T19%3A09%3A23%2B00%3A00&UserID=jamilqpr%40gmail.com&Version=1.0&Signature=c48c06b5b7717a9a5ff01018495e1350bf9b12721ed4d16eb38dda392a2a5633&apiKey=" + api_key

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the data as needed
else:
    # Handle the error
    print("Error: Request failed with status code", response.status_code)
