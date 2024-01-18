# Welcome Message.
LINE = "-" * 79
welcome = "Welcome to the Jewellery Shop!"
print(f"{LINE}\n{welcome}\n{LINE}\n\nStock:\n")


products = "A. Fresh Water Pearl Earrings - £30\n"
products += "B. Chunky Gold Chain Necklace- £45\n"
products += "C. Dangling Gemstone Pendant Earrings - £35\n"
products += "D. Multi-Coloured Gemstone Ring - £45\n"
products += "E. Chunky Open Silver Ring - £20\n"
products += "F. Velvet Jewellery Box - £35\n"

print(products)

enum = enumerate(products)


price = [30, 45, 35, 45, 20, 35]

stock = [4, 5, 3, 7, 4, 5]

price_count = 0



menu = input("Please enter number 1-4:\n\
    1. Add Item\n\
    2. Remove Item\n\
    3. Update Item\n\
    4. Exit Cart\ ")

# for i, product in enumerate(products):
#     if 

while menu == "1":
    print(products)
    add_item = input("What item would you like to add to your cart?")
    if add_item.upper() == "A":
        print("You have added Fresh Water Pearl Earrings to your cart!")
        price_count += 30
    elif add_item.upper() == "B":
        print("You have added Chunky Gold Chain Necklace to your cart!")
        price_count += 45
    elif add_item.upper() == "C":
        print("You have added Dangling Gemstone Pendant Earrings to your cart!")
        price_count += 35
    elif add_item.upper() == "D":
        print("You have added Multi-Coloured Gemstone Ring to your cart!")
        price_count += 45
    elif add_item.upper() == "E":
        print("You have added Chunky Open Silver Ring to your cart!")
        price_count += 20
    elif add_item.upper() == "F":
        print("You have added Velvet Jewellery Box to your cart!")
        price_count += 35
    else:
        print("snarfle")


# elif menu == "2":
#     print("Item Removed")
# elif menu == "3":
#     print("Item Updated")
# elif menu == "4":
#     print("Have A Good Day!")
    
else:
    print("Invalid Option")