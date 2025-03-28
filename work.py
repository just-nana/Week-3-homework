def calculate_discount(price,discount_percent):
   

    if discount_percent>=20:
        discount_amount = (discount_percent/100)*price
        final_price = price - discount_amount
        return final_price
    else:
        return price

price = float(input("Enter product price"))
discount = float(input("Enter discount amount"))  

print(calculate_discount(price,discount))



       
      