temperature, wind, humidity = int(input()), int(input()), int(input())
if temperature>=30 and wind ==0:
    print('開冷氣')
elif humidity >=85:
    print('開除溼')
else:
    print('關冷氣')