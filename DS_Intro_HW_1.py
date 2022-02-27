#eden duktzayev - 316365733
#Q1
def my_func(x1, x2, x3):
    n = float((x1+x2+x3)*(x2+x3)*x3)
    d = float(x1+x2+x3)
    if d == 0:
        return 'Not a number – denominator equals zero'
    elif not isinstance(x1,float) or not isinstance(x2,float) or not isinstance(x3,float):
        return 'Error: parameters should be double'
    else:
        return n/d

#Q2
def convert(hours,minutes=0):
    if hours < 0 or minutes < 0:
        return 'Input error!'
    hor=hours*3600
    min=minutes*60
    return hor+min









