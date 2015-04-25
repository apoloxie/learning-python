class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    defl altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
