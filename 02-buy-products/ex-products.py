products = {
  'sonho': 5,
  'croissant': 4,
  'coxinha': 3, 'pastel': 4.5,
  'refrigerante': 6
}

order = input('Vai levar o que? ').lower()

order_list = []

for item in order.split(","):
    order_list.append(item.strip())

total_value = products[order_list[0]] + products[order_list[1]]
total_formated = "R${:,.2f}".format(total_value)

print('------------------------------------')
print(f'Total: {total_formated}')
