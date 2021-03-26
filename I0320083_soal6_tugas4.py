# Operator Bitwise 4 dan 11
x = 4
print("nilai x =", x, " ,binary", format(x,'08b'))
y = 11
print("nilai y =", y, ",binary", format(y,'08b'))

# bitwise OR
a = x|y
print("nilai a =",a, ",binary", format(a,'08b'))

# bitwise right shift
b = x>>y
print("nilai b =",b, " ,binary", format(b,'08b'))

# bitwise XOR
c = x^y
print("nilai c =",c, ",binary", format(c,'08b'))

# bitwise NOT
d = ~x
print("nilai d =",d, ",binary", format(d,'08b'))

# bitwise AND
e = y&x
print("nilai e =",e, " ,binary", format(e,'08b'))
