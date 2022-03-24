
N = int(input("Enter an Integer Number: "))
original_number = N
X_list = []
divisor = 2


while N>=2:
    if N % divisor ==0:
        X_list.append(divisor)
        N = N/divisor
    else:
        divisor +=1


print('{} = '.format(original_number),end='')
for i in range(len(X_list)):
    if i == len(X_list)-1:
        print('{}'.format(X_list[i]), end='')
    else:
        print('{} x '.format(X_list[i]), end='')

