N = int(input("Enter an integer: "))
def power_of_two(value):
    while value>0:
        if value == 1:
            return True
        elif value % 2 == 1:
            return False
        else:
            value = value /2


round=[]
i=0
while N>i:
    x =int(input("Enter round number: "))
    j=1
    sum=0
    while x>=j:
        if power_of_two(j):

            sum=sum-j
        else:

            sum = sum + j
        j+=1
    round.append(sum)
    i=i+1

for sum in round:
    print(sum)
