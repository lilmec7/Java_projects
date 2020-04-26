def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

# Write code here
def calculate_simple_return(start_price, end_price, dividend = 0):
  return  (end_price - start_price + dividend) / start_price
print(calculate_simple_return(200, 250, 20))
simple_return = calculate_simple_return(200, 250, 20)

print("The simple rate of return is " + display_as_percentage(simple_return))


print("hELLO")
for i in range(3):
  print(5)