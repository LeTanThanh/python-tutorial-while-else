if __name__ == "__main__":
  # Introduction to Python while else statement

  """
  while condition:
    # code block to run
  else:
    # else clause code block
  """

  # Python while else statement example

  basket = [
    {"fruit": "apple", "qty": 20},
    {"fruit": "banana", "qty": 30},
    {"fruit": "orange", "qty": 10}
  ]

  fruit = input("Enter a fruit: ")

  index = 0
  found = False

  # while index < len(basket):
  #   item = basket[index]

  #   if item["fruit"] == fruit:
  #     found = True
  #     print(f"The basket has {item['qty']} {item['fruit']}(s)")
  #     break

  #   index += 1

  # if not found:
  #   qty = int(input(f"Enter the qty for {fruit}: "))
  #   basket.append({"fruit": fruit, "qty": qty})
  #   print(basket)

  while index < len(basket):
    item = basket[index]

    if item["fruit"] == fruit:
      print(f"The basket has {item['qty']} {item['fruit']}(s)")
      break

    index += 1
  else:
    qty = int(input(f"Enter the qty for {fruit}: "))
    basket.append({"fruit": fruit, "qty": qty})
    print(basket)
