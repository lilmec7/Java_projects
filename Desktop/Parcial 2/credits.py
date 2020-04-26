def ground_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
    return 20 + (weight * price_per_pound)
    print(ground_shipping_cost(8.4))
    
    premium_ground_shipping = 125.00
  
def drone_shipping_price(weight):
  
  if weight <= 2:
    drone_shipping_cost = 4.50
  elif weight <= 6:
    drone_shipping_cost = 9.00
  elif weight <= 10:
    drone_shipping_cost = 12.00
  else:
    drone_shipping_cost = 14.25
    return 0.0 + (weight * drone_shipping_cost)
    print(drone_shipping_price(14.25))
    
def cheapest_method(weight):
  ground = ground_shipping_cost(weight)
  premium = premium_ground_shipping
  drone = drone_shipping_price(weight)
  
  if ground < premium and ground < drone:
    best_method = "Ground Shipping"
    cost = ground
  elif premium < ground and premium < drone:
    best_method = "Premium Shipping"
    cost = premium
  else:
    best_method = "Drone Shipping"
    cost = drone
    
    print("You should ship using" + best_method + " it will cost" + cost + ".")