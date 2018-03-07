class Car(object):
  def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage 
        if price > 10000:
          self.tax = 0.15
        else:
          self.tax = 0.12
        self.display_all()
            
  def display_all(self):
    print 'Price: '+ str(self.price)
    print 'Speed '+ str(self.speed)
    print 'Fuel: '+ str(self.fuel) 
    print 'Mileage: '+ str(self.mileage)

    
car1 = Car(2000, 35, 'Full', 15, 0.12)
car2 = Car(2000, 15, 'not full', 105, 0.12)
car3 = Car(2000, 15, 'kind of full', 95, 0.12)
car4 = Car(2000, 25, 'full', 25, 0.12)
car5 = Car(2000, 45, 'empty', 25, 0.12)
car6 = Car(2000000, 35, 'empty', 15, 0.15)

    


