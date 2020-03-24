def cost_of_hotel(nights):
  return 100 * nights

def cost_of_flight(city):
  if city == "Paris":
    return 85
  elif city == "Nice":
    return 211
  elif city == "Lyon":
    return 76
  elif city == "Marseille":
    return 182
  elif city == "Bordeaux":
    return 183


def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost


def total_trip_cost(city, days, extras):
  sum = rental_car_cost(days) + cost_of_hotel(days -1) + cost_of_flight(city) + extras
  return sum

print(total_trip_cost("Nice", 10, 800))