# class Factory:
#     a = 12                                                       # attribute
    
#     def hello(self):                                             # method
#         print("How are you ?")
    
        
#     print("How r U. I'm getting initialized")    
# # print(Factory().a)
# # Factory().hello()

# obj = Factory()
# obj2 = Factory()


# print(obj.a)
# obj.hello()

# obj2.hello()
# print(obj.a)



# class Factory:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
        
#     def show(self):
#            print(f"Your objects details are {self.material}, {self.zips}, {self.pockets}") 
    
# obj = Factory('leather',5,6)    
# obj2 = Factory('mylon',1,2)    
# # print(obj.material)
# # print(obj2.pockets)

# obj.show()
# obj2.show()


# class User:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
        
#     def show(self):
#         print(f'The User details are {self.name}, {self.age},{self.grade}')    
    
    
# user1 = User("Bashudev",17,'XII')   
# user2 = User("Pradeep",16,12)   
# # print(user1.name)
# # print(user2.name)
# user1.show()
# user2.show()




#            Attributed and Methods
        
# class Person():
#     name = "Bashudev"                        #.................... Class Attribute >>>>>>>>>>>>>>>>>>>
#     print(name)
#     def __init__(self,name ,age):            #.................... Instance Attribute >>>>>>>>>>>>>>>>>>>
#         self.name = name
#         self.age = age
        
#     def show(self):                           #.................... Instance Method >>>>>>>>>>>>>>>>>>>
#         print(f'Name of person is {self.name} & age is {self.age}')    
        
#     @classmethod                               #.................... Class Method >>>>>>>>>>>>>>>>>>>
#     def classMethod(cls):
#         print('Please God protect me from all destraction')
        
#     @staticmethod                          #.................... Static Method >>>>>>>>>>>>>>>>>>>
#     def staticMethod():
#         print("It is Static method")
                
        
# person = Person("Jay Shree Ram",17)
# print(person.name)
# person.show()
# person.classMethod()
# person.staticMethod()


#                4 Pillars & they're given below:
#                   1. Inheritance
#                   2. Polymorphism
#                   3. Encapsulation
#                   4. Abstraction

#        INHERITANCE  
       
#                   Single Inheritance..........  
# class FactoryBtm:
#     name = "Pradeep Bhusal"
    
#     def __init__(self,material,cement,chad):
#         self.material = material
#         self.cement = cement
#         self.chad = chad
    
    
#     def show(self):
#         print(f"Material : {self.material} \n Cement : {self.cement} \n Chad : {self.chad}")



# class Factoryktm(FactoryBtm):
#     def __init__(self, material,cement,chad, petrol, deseal,oil):
#         super().__init__(material,cement,chad)
#         self.petrol = petrol
#         self.deseal = deseal
#         self.oil = oil
        
#     def show(self):
#         print(f"Material : {self.material} \n Cement : {self.cement} \n Chad : {self.chad} \n Petrol : {self.petrol} \n Diseal : {self.deseal} \n Oil : {self.oil}")    
        

# fact1 = FactoryBtm("Program is Worked Successfully","Just Wow","Very Happy")
# fact2 = Factoryktm("Stone & Sand", "2 Socks of Cement",'2 bundles of Chad','1 ltr petrol','2 ltr deseal','3ltr oil')
# fact1.show()
# fact2.show()
# print(fact1.material)



#                 ........ Multi Inheritance
# class Human:
#     name1 = "Ram"
    
# class God:
#     name2 = "Krishna"

# class Godess(Human,God):
#     name3 = 'Durga'
    
# obj = Godess()
# print(obj.name1)
# print(obj.name2)
# print(obj.name3)


# class Human:
#     def __init__(self,name1):
#         pass
# class God:
#         def __init__(self,name1,name2):
#             pass


# class Godess(God,Human):
#     name3 = 'Durga'
#     name1 = "krishna"
#     name2 = "Ram"
    
# obj = Godess("ram","krishna")
# print(obj.name1)
# print(obj.name2)
# print(obj.name3)

#                               # ........ Multi_Level Inheritance
# class bagFactory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips
        
#     # def show(self):
#     #     print(f"Material : {self.material}")
        
        
# class rebookFactory(bagFactory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
        
#         self.color = color
        
#     # def show(self):
#     #     print(f"Material : {self.material}")    
    
# class puneFactory(rebookFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
        
#         self.pockets = pockets
        
    
#     # def show(self):
#     #     print(f"Material : {self.material}")    
    
# obj = puneFactory("stone & cements","2packs anything","Red and Yellow","As customers wants")
# print(obj.pockets)



#              ............... __ 2. Polymorphism__..........

# class Human:
#         def show(self):
#                 print("It is of Human Class")
                
                
                
# class Animal(Human):
#         def show(self):
#                 print("It is of Animal Class")
                
# obj1 = Human()
# obj2 = Animal()
# obj1.show()
# obj2.show()

# class Animal:
#         def show(self):
#                 print("I am showing")
                
# class Human:
#         def show(self):
#                 print("I am also Showing")   
                
# obj = Animal()
# obj1 = Human()
# obj.show()
# obj1.show()


#                  ............ 3. Encapsulation  ...............
#         Project the class bcoz not to access ...# It must be Private
# class Factory:
#         __a = "Ram"
        
#         # def __show(self):
#         def show(self):
#                 print(Factory.__a)
#                 # print("Jay Shree Ram")
                
# class newFactory(Factory):
#         def show2(self):
#                 print(super().__a)            
# obj = newFactory()
# obj.show()
# # obj.show2()


# class Demo:
#         def __init__(self):
#                 self.name = "Bashudev"
#                 self._age = 17
#                 self.__salary = 15000
                
#         def show(self):
#                 print("Details of Employee : ")
#                 print(f"Name : {self.name} \n Age : {self._age} \n Salary : {self.__salary}")
        
# info = Demo()
# info.name = "Bhusal"
# info._age = 12
# info.__salary = 20000
# info.show()


#               4. Abstraction
# from abc import ABC, abstractmethod

# class abstract(ABC):
#         @abstractmethod
#         def area(self):
#                 pass
        
#         @abstractmethod
#         def perimeter(self):
#                 pass

# class Square(abstract):
#         def __init__(self,side):
#                 self.side = side
                
        
#         def area(self):
#                 print("`Area of Sq.` is created")
                
#         def perimeter(self):
#                 print("`Perimeter of Sq.` is created")          
                
                
                
# class Circle(abstract):
#         def __init__(self,raduis):
#                 self.radius = raduis                
                
        
#         def area(self):
#                 print("`Area of Circle` is created")
                
#         def perimeter(self):
#                 print("`Perimeter of Circle` is created")           
# sq = Square(4)
# cir = Circle(3.14)
# print(sq.side)               
# print(cir.radius)     

# sq.area()
# sq.perimeter()

# cir.area()
# cir.perimeter()          


# from abc import ABC, abstractmethod

# class abstract(ABC):
#         @abstractmethod
#         def perimeter(self):
#                 pass
        
#         @abstractmethod
#         def area(self):
#                 pass


# class circle:
#         def __init__(self,radius):
#                 self.radius = radius
               
#         def perimeter(self):
#                 print("Perimeter of Circle")
                
#         def area(self):
#                 print("Area of Circle")        
                
                
# class square:
#         def __init__(self,side):
#                 self.side = side
                
#         def perimeter(self):
#                 print("Perimeter of Square")
                
#         def area(self):
#                 print("Area of circle")                
                
# cir = circle(7//2)
# sq = square(12//3)

# print(cir.radius)
# print(sq.side)

# cir.perimeter()
# cir.area()

# sq.perimeter()
# sq.area()




# from abc import ABC, abstractmethod

# class abstract(ABC):
#         @abstractmethod
#         def area(self):
#                 pass
        
#         def perimeter(self):
#                 pass
        
        
        
# class Circle(abstract):
#         def __init__(self,radius):
#                 self.radius = radius
                
#         def perimeter(self):
#                 print(f" It isPerimeter of Circle")
        
#         def area(self):
#                  print(f' It is area of Circle')
                

# class Square(abstract):
#         def __init__(self,side):
#                 self.side = side
                
#         def perimeter(self):
#                 print(f" It's perimeter of Square")
#         def area(self):
#                 print(f" It's area os Square" )
        
                
# cir = Circle(3.14)
# sq = Square(4)    

# print(cir.radius)
# print(sq.side)      

# cir.area()
# cir.perimeter()

# sq.area()
# sq.perimeter()
# # print(cir)
# # print(sq)
                







    # ______________________............... Dunder Methods ................_______________________________

#   => It is special methods in Python that start and end with double underscores __init__ , __add__ , __str__ etc.

# class Animal:
#         def __init__(self,name):
#                 self.name = name
                
#         def __str__(self):
#                 return f'animal : {self.name}'
                

# obj = Animal("Tiger")
# print(obj)
# # obj.show()



# class Animal:
#         def __init__(self,name,age):
#                 self.name = name
#                 self.age = age
                
#         def __str__(self):
#                 return f"Name of Animal is {self.name} & age is {self.age}" 
        
#         def __add__(self,other):
#                 sum = 0
#                 for i in other:
#                         sum += i.age
#                 return f"Sum of age of Fish is {self.age + sum}"       
              
           
# obj = Animal('Dolphin',12)
# obj2 = Animal("Blue Whale",15)
# obj3 = Animal("Star Fish",3)
# print(obj)
# print(obj2)
# print(obj + (obj2 , obj3))

# class User:
#         def __init__(self,name,age):
#                 self.name = name
#                 self.age = age
                
#         def __str__(self):
#                 return f" Name is {self.name} \n Age is {self.age}"
        
#         def __add__(self,other):
#                 sum = 0
#                 for i in other:
#                         sum += i.age
#                 return f" The sum of all age of User is {self.age + sum}"
        

# user1 = User("Bashudev Bhusal",17)
# user2 = User("Jay Shree Ram",23)
# user3 = User("Jay Shree Krishna",37)
# user4 = User("Radhe Radhe",7)
# user5 = User("un_ishaaa",23)
# print(user1)
# print(user2)
# print(user3)
# print(user4)
# print(user5)
# print(user1 + (user2,user3,user4,user5))


# Linking the main.py for the output of Modules and Packages

# import main
# main.addition(1,2)
# main.multiply(2,3)

# from main import addition,multiply
# addition(9,1)
# multiply(2,3)

# from modules import mod1,mod2 
# add(1,2)
# # add(99,1)
# # multiply(50,2)