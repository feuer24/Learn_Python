#phones = ['IPhones','Galaxy','Xiaomi']

#product = {"name": "IPhone",
#"stock": 5,
#"price": 65000,
#'recomend': phones
#}

#print(product['recomend'])

#product["stock"] =  10
#print(product)


#print(product.get('stocks',0))

#del product["price"]
#print(product)

def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))

    if discount >= 100:
        price_witn_discount = price
    else:
        price_witn_discount = price - price*discount/100
    print(price_witn_discount)    

discounted(100,65)
discounted(200,-30)
discounted(-500,200)
