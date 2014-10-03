customer_data=open("customer_orders.csv")
    
melon_cost = 1.00

for line in customer_data:
    data = line.split(",")
    customer_name = data[1]
    melons_purchased = int(data[2])
    funds_paid = float(data[3])
    customer_expected = melons_purchased * melon_cost
    
    if customer_expected != funds_paid:
        print customer_name, "paid %.2f, expected %.2f"%(funds_paid, customer_expected)


customer_data.close()

