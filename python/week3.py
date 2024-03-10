def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price
def main():
    original_price = float(input("enter price: "))
    discount_percentage = float(input("enter discount: "))
    final_price = calculate_discount(original_price, discount_percentage)

    if final_price == original_price:
        print("no discount. fina, price:", final_price)
    else:
        print("final price soon:", final_price)
if __name__ == "__main__":
    main()
