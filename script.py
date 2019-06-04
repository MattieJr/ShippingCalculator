premium_ground_shipping = 125

def ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3
  elif weight <= 10:
    price_per_pound = 4
  else:
    price_per_pound = 4.75
  return (weight * price_per_pound) + 20

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9
  elif weight <= 10:
    price_per_pound = 12
  else:
    price_per_pound = 14.25
  return (weight * price_per_pound)

def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
    print("Ground Shipping is cheapest at $" + str(ground_shipping(weight)) + " for an item that weighs " + str(weight) + "lbs.")
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
    print("Drone Shipping is cheapest at $" + str(drone_shipping(weight)) + " for an item that weighs " + str(weight) + "lbs.")
  elif premium_ground_shipping < ground_shipping(weight) and premium_ground_shipping < drone_shipping(weight):
    print("Premium Ground Shipping is cheapest at $" + str(premium_ground_shipping) + " for an item that weighs " + str(weight) + "lbs.")
  else:
    print("Sorry. We could not determine the cheapest shipping option.")
    
cheapest_shipping(5.8)   