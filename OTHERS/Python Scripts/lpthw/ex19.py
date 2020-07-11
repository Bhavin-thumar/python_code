def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses.")
    print(f"you have {boxes_of_crackers} boxes_of_crackers")
    print("Man thats enough for party.")
    print("Get a blanket.\n")

print("we can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print("Or use variable from our script.")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine variable and math in arguments.")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10000)
