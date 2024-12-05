class vehi:
    def vehi(self):
        print ('this is parent vehicle class method')
class car(vehi):
    def car(self):
        print ('this is child car class method')
kar = car()
kar.vehi()
kar.car()
class person:
    name= ''
    age = 0
    def __init__(self,person_name,person_age):
        self.name= person_name
        self.age= person_age
    def showname(self):
        print (self.name)
    def showage(self):
        print (self.age)
class student (person):
    studentid= ''
    def __init__(self,studentname,studentage,studentid):
        person.__init__(self,studentname,studentid)
        self.studentid= studentid
    def getid(self):
        return self.studentid
person1 =person('udi',20)
person1.showname()
person1.showage()
student1 = student('iki', 30,111)
print (student1.getid())
class robot(object):
    def __init__(self):
        self.a= 123
        self._b= 123
obj = robot()
print (obj.a)
print (obj._b)

