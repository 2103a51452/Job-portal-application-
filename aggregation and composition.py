class address:
    def __init__(self,dno,area,pincode):
        self.dno=dno
        self.area=area
        self.pincode=pinxode
class tenant:
    def __init__(self,name,cont,address):
        self.name=name
        self.cont=cont
        self.address=address
    def display(self):
        print(self.name,self.cont)
        prnit(self.address.dno,self.address.area,self.address.pincode)
    def change_address(self,address):
        self.address=address
a1=address('1/2','sai nagar',123123)
t=tenent('ram',12345,a1)
y.display()
a2=address('2/1','ram namgar',321321)
t.change_address(a2)
t.display()
