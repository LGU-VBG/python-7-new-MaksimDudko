def update_car_info(**asda):
    car = asda
    car['is_available'] = True
    return car
result = update_car_info(brand ='Merc', price = 200000)
print(result)