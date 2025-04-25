product_price = int ( input ( " Enter please the product price :"))
if product_price < 100:
    discount_2 = product_price * 0.02
    total_price = product_price - discount_2
    print(f" Your discount is:  {discount_2}  and the total price is : {total_price}")
else:
    discount_10 = product_price * 0.10
    final_price = product_price - discount_10
    print (f" Your discount: {discount_10} and the total price is : {final_price} ")