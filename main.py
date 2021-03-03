from myMath import myArithmetic
num_1 = int(input('請輸入第一個數: '))
num_2 = int(input('請輸入第二個數: '))
num_3 = int(input('請輸入第三個數: '))
num_4 = int(input('請輸入第四個數: '))
num_5 = int(input('請輸入第五個數: '))
s = (num_1,num_2,num_3,num_4,num_5)
Sum = 0
for i in range (5):
    Sum = myArithmetic.myAdd(Sum,s[i])
Avg = myArithmetic.myDiv(Sum,5)
print('數值和為:',Sum,'平均為:',Avg)
