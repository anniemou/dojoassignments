class Bike(object):
    def __init__(self, price, speed):
        self.price = price
        self.speed = speed
        self.miles = 0
    def displayInfo(self):
        print "Total miles {}, Speed {}, Price {}".format(self.miles, self.speed, self.price)
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if(self.miles == 0):
            print "Cannot reverse"
            return self
        self.miles -= 5
        return self

bike1 = Bike(200, "25")
bike2 = Bike(500, "50")
bike3 = Bike(100, "10")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
