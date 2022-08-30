usd_price_example = 5.00
euro_price_example = 5.70

def final_result_message(total_price, amount, discount, result_from_conversion, result_with_discount, coin):
    print(f"""
Current price: {coin}{total_price}
Products amount: {amount}x
Discount: {discount}%

{coin}{total_price} to R${result_from_conversion}
You must pay: R${result_with_discount}
    """)

def calc(price, amount, coin = "brl", discount = 5):

    total_price = amount * price

    if coin == "usd":

        usd_to_brl = total_price * usd_price_example
        result_with_discount = usd_to_brl - (usd_to_brl * (discount / 100))

        final_result_message(total_price, amount, discount, usd_to_brl, result_with_discount, '$')
        

    elif coin == "euro":
        
        euro_to_brl = total_price * euro_price_example
        result_with_discount = euro_to_brl - (euro_to_brl * (discount / 100))
        
        final_result_message(total_price, amount, discount, euro_to_brl, result_with_discount, '£')

    elif coin == "brl":

        result_with_discount = total_price - (total_price * (discount / 100))

        final_result_message(total_price, amount, discount, total_price, result_with_discount, 'R$')

    else:
        print("This coin doesn't exist.")

calc(10, 3, "brl", 5)