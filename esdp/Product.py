from abc import ABC, abstractmethod
class Product:

    def __init__(self,name,price):
      self.name=name
      self.price=price
      
      @abstractmethod
      def get_price(self):
        pass
      
      def display_details(self):
        pass

class Electronics(Product):
   
   def __init__(self,size,color,material):
    super().__init__(name,price)
    self.brand=brand
    self.warranty=warranty

    def display_details(self):
       print("Name:",self.name)
       print("Price:",self.price)
       print("Brand:",brand)
       print("Warranty:",warranty)
     

class Clothing(Product):
   def __init__(self,size,color,material):
    super.get_price(self,size,color,material)
    self.size=size
    self.color=color
    self.material=material

    super.display_details(self)
    print("Color:",self.color)
    print("Material:",self.material)

class Books(Product):
  def __init__(self,auther,genere):
    super.get_price(self,auther,genere)
    self.auther=auther
    self.genere=genere

    super.display_details(self)
    print("Auther:",self.auther)
    print("Genere:",self.genere)


name=input("Enter your name:")
price=eval(input("Enter price:"))
brand=input("Enter Brand:")
warranty=input("Enter warranty:")
size=int(input("Enter size:"))
color=input("Enter Color:")
material=input("Enter material:")
auther=input("Enter auther name:")
genere=input("Enter Genere:")



e=Electronics(size,color,material)
e.get_price(brand,warranty)
e.display_details()

c=Clothing(size,color,material)
c.get_price(size,color,material)
c.display_details()

b=Books(auther,genere)
b.get_price(auther,genere)
b.display_details()

  

    
        

 






