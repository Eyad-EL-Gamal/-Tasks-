temp = 25
if temp >= 30 :
    print("it,s a hot day. stay hydrated")
elif temp >=20 and temp <= 29 :
     print("it,s a warm day. enjoy the weather")
elif temp >=10 and temp <=19 :
     print("it,s a cool day. wear a jacket")
elif temp <10 :
     print("it,s a cool day. stay warm")
number = list(range(1,21))
for x in range(1,21):
     print(x)
for x in number:
     if x % 3 == 0:
          print(x)