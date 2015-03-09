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
        self.gf = 'cloth'
        
    def money_for_gf(self, more):
        return self.coat * 10
        
a = Cloth()
b = Cloth()
c = Cloth_of_GF()

a.coat
b.leg
a.leg
c.gf

print a.buy_more()
print b.buy_more()

print a.buy_a_qiuku(20)
print b.buy_a_qiuku(30)

x = Cloth_of_GF(a.coat)
print x.money_for_gf(a.coat)
