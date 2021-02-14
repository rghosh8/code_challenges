class ExpSum(object):
    def __init__(self, coeff, exponent):
        self.coeff = coeff
        self.exponent = exponent

    def sum_(self, x):
        s=0
        for c, e in zip(self.coeff, self.exponent):
            s+=c*x**e

        return s

if __name__ == '__main__':
    coeff_=[4,1]
    exponent_=[1,0]

    print(ExpSum(coeff_,exponent_).sum_(1))

