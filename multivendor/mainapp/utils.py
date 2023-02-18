def productidgen(category,retailerid,productprice):
    try:
        if category == 'Mobiles':
            return 'm' + str(retailerid) + str(productprice)
        elif category == 'Electronics':
            return 'e' + str(retailerid) + str(productprice)
        elif category == 'Clothing':
            return 'c'+str(retailerid)+str(productprice)
        elif category == 'Footwear':
            return 'f'+str(retailerid)+str(productprice)
        elif category == 'Home Appliances':
            return 'ha'+str(retailerid)+str(productprice)
        elif category == 'Groceries':
            return 'g'+str(retailerid)+str(productprice)
    except:
        raise Exception('Invalid category')