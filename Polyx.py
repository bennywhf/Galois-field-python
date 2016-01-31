from copy import deepcopy
class polynomial:
    def __init__(self,lst,rev = True):
        self.lst = deepcopy(lst)
        if rev == True:
            self.lst.reverse()
        for i in range(len(self.lst)):
            self.lst[i] = int(self.lst[i])
        self.rev = rev

    def evaluate(self,x):
        r = 0
        for i in range(len(self.lst)):
            r += self.lst[i] * x**i
        return r

    def __call__(self,x):
        return self.evaluate(x)

    def coeff(self):
        l = deepcopy(self.lst)
        if self.rev:
            l.reverse()
        return l

    def __add__(self,other,mod = 2):
        if len(self.lst) != len(other.lst):
            raise Exception('both polynomials must be of field of same ordder')

        size = len(self.lst)
        l = [0] * size
        for i in range(size):
            l[i] = (self.lst[i] + other.lst[i]) % mod
        l.reverse()
        return polynomial(l)

    def __str__(self):
        co = self.coeff()
        s = ''
        size = len(co)
        for i in range(size):
            if co[i] == 1:
                if i != 0 and s != '':
                    s+= ' + '
                if size-i-1 == 0:
                    s+= '1'
                else:
                    if size - i - 1 == 1:
                        s += 'X'
                    else:
                        s+='X^'+str(size-i-1)
                    
        return s


def find_irredu(deg,mod = 2):
    l = []
    for i in range(mod**(deg)):
        a = ['1']
        a.extend(list(fill_rest(bin(i)[2:],deg)))
        l.append(polynomial(a))
    for i in l:
        if (i(1) % mod != 0 and i(0) % mod != 0):
            yield(i)


def fill_rest(bits,size):
    while len(bits)<size:
        bits = '0' + bits
    return bits

def main():
    l = [0,0,0,0,0,1]
    for i in range(35):
        l.pop(0)
        l.append(0)
        if l[0] == 1:
            l[2] = (l[2] + 1) % 2
            l[-1] = (l[-1] + 1) %2
        l[0] = 0
        print(str(i+1) + " " +str(polynomial(l)))
main()
    

#class extenfield:
 #   def __init__(self,
