def absolute_value(num) :

    if num >= 0:
        return num

    else:
        return -num

def super_av (prompt, num) :

    if num >= 0:
        x=prompt + " " + num
        return x

    else:
        return -x

print(super_av(2))
print(absolute_value(-4666))