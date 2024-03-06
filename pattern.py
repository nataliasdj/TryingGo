"""
Example 1:
Input: N = 3
Output: 
* * *
* * *
* * *
"""
def pattern1():
    # print('Enter a number, 1st pattern: ')
    # x = int(input()) #if wanna use input but lazy so - then replace 5 wtih x
    #or if you dont want to use like per row do this
    """
    print(“Toppr”, end=’ ‘)
    print(“is awesome”) it will print toppr is awesome  - trus at end is new line
    """
    #row = ""
    for i in range(5):
        for j in range(5):
            print("*", end=' ')
        print() #since that end does not give automatic endl
def pattern2():
    for i in range(5):
        for j in range(i+1):
            print("*", end=' ')
        print()
def pattern3():
    for i in range(5):
        num = 1
        for j in range(i+1):
            print(num, end=' ')
            num += 1
        print()
def pattern4():
    for i in range(5):
        for j in range(i+1):
            print(i+1, end=' ')
        print()
def pattern5():
    for i in range(5):
        #for i in range(start, stop, step):
        for j in range(5-i, 0, -1):
            print("*", end=' ')
        print()
def pattern6():
    for i in range(5):
        num = 1
        #for i in range(start, stop, step):
        for j in range(5-i, 0, -1):
            print(num, end=' ')
            num+=1
        print()
def pattern7():
    prev_row_star = 1
    mid = (5*2-1)//2
    for i in range(5):
        for x in range(5-i-1):
            print(" ", end=' ')
        for y in range(2*i+1):
            print("*", end=' ')
        for z in range(5-i-1):
            print(" ", end=' ')
            # if prev_row_star == 1 and j == mid:
            #     print("*", end = ' ')
            #     continue
            # if j >= mid-prev_row_star+2 and j <= mid+prev_row_star-2:
            #     print("*", end = ' ')
            # else:
            #     print(" ", end= ' ')
        prev_row_star += 2
        print()
def pattern8():
    for i in range(5):
        for x in range(i):
            print(" ", end=' ')
        for y in range((5-i)*2-1):
            print("*", end=' ')
        for z in range(i):
            print(" ", end=' ')
        print()
def pattern9():
    for i in range(5):
        for x in range(i):
            print(" ", end=' ')
        for y in range((5-i)*2-1):
            print("*", end=' ')
        for z in range(i):
            print(" ", end=' ')
        print()
# pattern1()
# pattern2()
# pattern3()
# pattern4()
#pattern5()
#pattern6()
# pattern7()
pattern8()