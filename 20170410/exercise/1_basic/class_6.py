# -*- coding:utf-8 -*-

class Service:
    def setname(self, name):
        self.name = name
        self.secret = "영구는 배꼽이 두 개다"
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
        

pey = Service()
pey.setname("john haan")
pey.sum(1,1)