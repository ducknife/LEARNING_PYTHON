#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife   
    t = int(input())
    for _ in range(t):
        n = input()
        sum = 0
        check = True
        for i in range(0, len(n) - 1):
            sum += int(n[i])
            if abs(int(n[i]) - int(n[i + 1])) != 2:
                check = False
                break
        sum += int(n[len(n) - 1])
        print('YES' if check and sum % 10 == 0 else 'NO')
        
            