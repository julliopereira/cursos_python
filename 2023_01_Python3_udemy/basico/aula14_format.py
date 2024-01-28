a = 'A'
b = 'B'
c = 1.1

string = 'a={}; b={}; c={:.5f}'
formato = string.format(a, b, c)

print(formato)

#indices
string = 'a={0}; b={1}; c={2:.5f}'
formato = string.format(a, b, c)

print(formato)

