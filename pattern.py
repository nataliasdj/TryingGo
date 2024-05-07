"""
Example 1:
Input: N = 3
Output: 
* * *
* * *
* * *
Pattern from https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/
"""
def pattern1(n):
    """
    print(“Toppr”, end=’ ‘)
    print(“is awesome”) it will print toppr is awesome  - trus at end is new line
    """
    #row = ""
    for i in range(n):
        for j in range(n):
            print("*", end=' ')
        print() #since that end does not give automatic endl
def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=' ')
        print()
def pattern3(n):
    for i in range(n):
        num = 1
        for j in range(i+1):
            print(num, end=' ')
            num += 1
        print()
def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=' ')
        print()
def pattern5(n): #btw they are exactly the same lol just one is +1 for loop, the other is -1
    for i in range(n):
        #for i in range(start, stop, step):
        for j in range(n-i, 0, -1):
            print("*", end=' ')
        print()

    # for i in range(n):
    #     for j in range(n-i):
    #         print("*", end = ' ')
    #     print()
def pattern6(n):
    for i in range(n):
        num = 1
        #for i in range(start, stop, step):
        for j in range(n-i, 0, -1):
            print(num, end=' ')
            num+=1
        print()
def pattern7(n):
    prev_row_star = 1
    mid = (n*2-1)//2
    for i in range(n):
        for x in range(n-i-1):
            print(" ", end=' ')
        for y in range(2*i+1):
            print("*", end=' ')
        for z in range(n-i-1):
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
def pattern8(n):
    for i in range(n):
        for x in range(i):
            print(" ", end=' ')
        for y in range((n-i)*2-1):
            print("*", end=' ')
        for z in range(i):
            print(" ", end=' ')
        print()
def pattern9(n):
    pattern7(n)
    pattern8(n)
def pattern10(n):
    for i in range(n):
        for k in range(i+1):
            print("*", end = ' ')
        print()
    for i in range(n):
        for j in range(n-i):
            print("*", end = ' ')
        print()
def pattern11(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end = ' ')
            if num == 1: 
                num = 0 
            elif num == 0: 
                num = 1
        if i % 2 == 0: num = 1
        else : num = 0  
        print()
# pattern1(5)
# pattern2(5)
# pattern3(5)
# pattern4(5)
# pattern5(5)
#pattern6(5)
# pattern7(5)
# pattern8(5)
# pattern9(5)
# pattern10(5)
pattern11(5)