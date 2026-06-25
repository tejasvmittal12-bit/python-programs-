snack_name = "Chips"
price = 1.50
quantity = 10
is_avalible = True

print("Snack", snack_name)
print("Price: $", price )
print("In Stock:", quantity)
print("Avalible?", is_avalible)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_avalible))

total = price * quantity
print("Total Value: $", total)
print("Sale Price: $", price- 0.25)
print("Double Stock:", quantity * 2)

print("Is Price Under $2?", price < 2)
print("More Than 5 In stock?", quantity > 5)
print("Is Price Exactly $1.50", price == 1.50)

shop_name = "Quick" + " " + "Bites"
print("Shop name", shop_name)
print("Letters in snack name", len(snack_name))
print("First Letter:", snack_name[0])

price_a = 1.50
price_b = 3.00  
print("Before:", price_a, "and", price_b)

temp    = price_a
price_a = price_b
price_b = temp
print("After:", price_a, "and", price_b)