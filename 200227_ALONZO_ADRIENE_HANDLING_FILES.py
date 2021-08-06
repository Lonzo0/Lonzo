#!/usr/bin/env python
# coding: utf-8

# In[4]:


# CODE CELL
# PROBLEM 1

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    coffee = products[code]
    return coffee

print(get_product("espresso"))


# In[5]:


# CODE CELL
# PROBLEM 2

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_property(code1, property):
    coffee1 = products[code1][property]
    return coffee1

print(get_property("dalgona", "price"))


# In[22]:


# CODE CELL
# PROBLEM 3

def main():
    orders = {}
    quantity = []
    total = 0
    subtotal = 0
    
    while 1>0:
        menu = input("Enter the customer's order 'product_code,quantity'. Or, type '/' to end session. ")
        if menu == "/":
            break

        code, qty = menu.split(",")
        name_price = get_product(code)
        qty = int(qty)
        price = get_property(code, 'price')
        total = price * qty

        if code in orders.keys():
            orders[code]["qty"] += qty
            orders[code]["total"] += total
        else:
            orders[code] = {"qty":qty,"total":total}

        subtotal += total

    orders = dict(sorted(orders.items()))
    receipt = []
    receipt.append("==\nCODE\t\t\tNAME\t\t\tQUANTITY\t\tSUBTOTAL")

    for code,order in orders.items():
        name = get_property(code,"name")
        qty = order["qty"]
        price = order["total"]
        receipt.append(f"{code}\t\t{name}\t\t{qty}\t\t\t\t{price}")

    receipt.append(f"\nTotal:\t\t\t\t\t\t\t\t\t\t\t{subtotal}\n==")
    receipt = "\n".join(receipt)
    
    with open("receipt.txt","w") as f:
        f.write(receipt)

main()

#CODE END


# In[ ]:




