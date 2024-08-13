menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_cost = 0
while True:
    try:
        order = input("Item: ")
        titled_order = order.title()
        if titled_order in menu:
            total_cost += menu[titled_order]
            print(f"Total: ${format(total_cost, '.2f')}")

    except EOFError:
        print()
        break

