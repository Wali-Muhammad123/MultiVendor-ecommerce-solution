import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','multivendor.settings')
import django
django.setup()
from random import choice,randint
from mainapp.models import ProductDetails,Retailer_Product

def populate():
    categories=['e','c','g','m','ha','fw']
    prices=[100,200,300,400,500,600,700,800,900,1000]
    product_ids=[]
    for i in range(50):
        product_ids.append(choice(categories)+str(randint(1,10))+str(choice(prices)))
    product_names=[
        'Samsung Galaxy S10',
        'Samsung Galaxy S10+',
        'Samsung Galaxy S10e',
        'Samsung Galaxy S10 5G',
        'Samsung Galaxy Note 10',
        'Samsung Galaxy Note 10+',
        'Samsung Galaxy Note 10 5G',
        'Samsung Galaxy A50',
        'Samsung Galaxy A70',
        'Samsung Galaxy A80',
        'Samsung Galaxy A90',
        'Samsung Galaxy A10',
        'Samsung Galaxy A20',
        'Samsung Galaxy A30',
        'Samsung Galaxy A40',
        'Samsung Galaxy A60',
        'Samsung Galaxy A6+',
        'Samsung Galaxy A8+',
        'Samsung Galaxy A9',
        'Samsung Galaxy A9 Pro',
        'Samsung Galaxy A9 Star',
        'Samsung Galaxy A9 Star Lite',
        'Samsung Galaxy A9s',
        'Samsung Galaxy A9s 2018',
        'Samsung Galaxy A9s 2019',
        'Samsung Galaxy A9s 2020',
        'Samsung Galaxy A9s 2021',
        'Samsung Galaxy A9s 2022',
        'Samsung Galaxy A9s 2023',
        'Samsung Galaxy A9s 2024',
        'Samsung Galaxy A9s 2025',
        'Samsung Galaxy A9s 2026',
        'Samsung Galaxy A9s 2027',
        'Samsung Galaxy A9s 2028',
        'Samsung Galaxy A9s 2029',
        'Samsung Galaxy A9s 2030',
        'Samsung Galaxy A9s 2031',
        'Samsung Galaxy A9s 2032',
        'Samsung Galaxy A9s 2033',
        'Samsung Galaxy A9s 2034',
        'Samsung Galaxy A9s 2035',
        'Samsung Galaxy A9s 2036',
        'Samsung Galaxy A9s 2037',
        'Samsung Galaxy A9s 2038',
        'Samsung Galaxy A9s 2039',
        'Samsung Galaxy A9s 2040',
        'Samsung Galaxy A9s 2041',
        'Samsung Galaxy A9s 2042',
        'Samsung Galaxy A9s 2043',
        'Samsung Galaxy A9s 2044',
    ]
    product_description="This is dummy data"
    for i in range(50):
        quantity=randint(1,10)
        price=randint(100,1000)
        category=choice(['Electronics','Clothing','Groceries','Mobiles','Home Appliances','Footwear'])
        product=ProductDetails.objects.get_or_create(product_id=product_ids[i],name=product_names[i],description=product_description,price=price, category=category)
    print("Populating script")
    populate()
    print("Populating complete")