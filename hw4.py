

def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')




def bisection1(f,start_point,end_point,e):

    condition = True
    while condition:
        m = (start_point + end_point) / 2
        if f(start_point) * f(m) < 0:
            end_point = m
        else:
            start_point = m
        condition = abs(f(m)) > e
    return m



f1 = lambda x: x**3 - 5*x - 9
atr1 = bisection1(f1,2,3,0.0001)
print(atr1)

def bisection2(f,a,b,N):


    start_point = a
    end_point = b
    for n in range(1,N+1):
        m = (start_point + end_point)/2
        res = f(m)
        if f(start_point)*res < 0:
            start_point = start_point
            end_point = m
        elif f(end_point)*res < 0:
            start_point = m
            end_point = end_point
        elif res == 0:
            print("ERROR")
            return m
        else:
            print("ERROR")
            return None
    return (start_point + end_point)/2

f2 = lambda x: x**2 - x - 1
atr2 = bisection2(f2,1,2,25)
print(atr2)


def bisection3(f,start_point,end_point):
    condition = True
    while condition:
        m = (start_point + end_point) / 2
        if f(start_point) * f(m) < 0:
            end_point = m
        else:
            start_point = m
        condition = abs(f(m)) > 0.0001
    return m



