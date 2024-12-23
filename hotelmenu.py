
#***********this code is Restaurent Menu &  Order  System******************
"""
    ------Create By Bosudeb Naiya------
  --email-bosudeb.cse@gmail.com--
    Github (1st)bosudebexe.
    ------(2nd)bosudebcse.
"""
menu={
    'pizza':99,
    'chilli chicken':149,
    'butter naan':49,
    'chicken masala':199,
    'chicken kosha':99,
    'momo':99,
}
#greet
print('wellcome to PYTHON restaurent')
print(' pizza=99\n chilli chiken=149 \n butter naan=49\n chicken masala=199\n chicken kosha=99 \n momo=99')

order_total=0
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1} has been added to your order")
else:
    print(f"ordered item {item_1} has been not avaialable yet!")


another_order = input("Do you want to add another item? (YES/NO) ")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"item{item_2}has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")
print(f"the total amount of items is to pay {order_total}")