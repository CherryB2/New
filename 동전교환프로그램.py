money = int(input("돈 얼마 ? :"))
mon500,mon100,mon50,mon10 = 0,0,0,0

mon500=money//500
money %= 500
print("\n 남은돈  %d" %money)
mon100=money//100
money%=100
print("\n 남은돈  %d" %money)
mon50 = money//50
money%=50
print("\n 남은돈  %d" %money)
mon10=money//10
money%=10
print("\n 남은돈  %d" %money)
#print("\n 500원 : %d \n100원 : %d \n50원 : %d \n10원 : %d \n",%mon500,mon100,mon50,mon10)            


print("\n 500원짜리 %d" %mon500)

print("\n 100원짜리 %d" %mon100)

print("\n 50원짜리 %d" %mon50)

print("\n 10원짜리 %d" %mon10)

