
def calculate_discount(price, discount_percent):
    """
    Takes in the original price and the discount percentage.
    Calculates the final price by apply the discount
    """
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
    else:
        final_price = price

    return final_price

def getNumber(description=""):
    num1 = ""
    terminator = 'a'
    while terminator != 'q':
        while num1 == "":
            num = input(f"{description}: ")
            for i in range(len(num)):
                if ord(num[i]) >= 48 and ord(num[i]) <= 57:
                    num1 += num[i]                
                else:
                    num1 = ""
                    print("Only integers are needed!!")
                    break
        terminator = 'q'
    return int(num1)


def display():
    Original_px = getNumber("Enter original price of the item")
    percent = getNumber("Enter discount percentage")

    final_px = calculate_discount(Original_px, percent)
    if final_px == Original_px:
        print(f"Percent is small, price remains {final_px}")
    else:
        print(f"Final price after discount is: {final_px}")
        
display()
