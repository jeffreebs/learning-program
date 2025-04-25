

sales = [
    {
        "date": "01/03/2025",
        "customer_email" : "jeff@gmail.com",
        "items": [
            {
                "name": "Red Bull", "upc": "Dnks-181", "unit_price": 1.5,
            }
        ],
    },
    {
        "date": "15/03/2025",
        "customer_email" : "manolo@gmail.com",
        "items": [
            {
                "name": "Lays", "upc": "snks-171", "unit_price": 1,
            }
        ],  
    },

    {"date": "25/03/2025",
        "customer_email" : "tiapaola@gmail.com",
        "items": [
            {
                "name": "apple", "upc": "fruit-101", "unit_price": 1,
            }
        ],

    },
]

total_sales = {}

for sale in sales:
    for item in sale["items"]:
        upc = item ["upc"]
        price = item["unit_price"]


        if upc in total_sales:
            total_sales[upc] += price 
        else:
            total_sales[upc] = price


print (total_sales)


