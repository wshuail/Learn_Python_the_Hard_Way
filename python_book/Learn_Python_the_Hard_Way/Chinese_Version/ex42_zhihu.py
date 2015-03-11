class Cloth(object):

    def __init__(self):
        self.coat = 200
        self.leg = 'qiuku'

    def buy_more(self):
        print "I have no money."

    def buy_a_qiuku(self, more):
        self.leg = self.coat + more
        return self.leg

class Cloth_of_GF(object):

    def __init__(self):
        self.gf = 500
        
    def money_for_gf(self, n):
        return self.gf * n
        
a = Cloth()
b = Cloth()
c = Cloth_of_GF()

a.coat
b.leg
a.leg
c.gf

print a.buy_more()
print b.buy_more()

print 'What is the price of the qiuku ?'
print a.buy_a_qiuku(20)
print '\n'
print 'What is the price of the other qiuku ?'
print b.buy_a_qiuku(30)

x = Cloth_of_GF()
print 'What is the price of the gf\'s cloth ?'
print x.money_for_gf(5)
