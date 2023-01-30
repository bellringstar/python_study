# fee(600, 50) #=> 91000
# fee(600, 110) #=> 10
import math

def fee(minute, km):
    price_a = minute * 120 
    price_b = math.ceil(minute/30) * 525     
    if km < 100:
        price_c = 170 * km
    else:
        price_c = 170 * 100 + (km-100) * 85
    
    return price_a + price_b + price_c

print(fee(600, 110))

