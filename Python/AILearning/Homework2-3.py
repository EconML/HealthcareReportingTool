def question1():
    print("Please enter a DNA string", end='')
    lst = str(input()).replace('T','U')
    print(lst)



def question2():
    print('Enter a DNA string', end='')
    lst = list(input())
    
    print('Enter the substring to compare', end='')
    s = input()
    
    n = 0
    final = []
    while True:
        st = lst[n:n+len(s)]
        if st == list(s):
            final.append(n+1)
        if n+len(s)==len(lst):
            break;
        n+=1
    
    print(final)
    
    
question2()

