  
# Tapşırıq 1: Bir "Person" sinifi yaradin, ad ve soyad atributlari olan obyekt yaradin.
class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname 
# Tapşırıq 2: "Person" sinifindən iki obyekt yaradin ve onlarin ad və soyadlarını cap edin.
class Boy (Person):
        def __init__(self, name='Tofig', surname='Saftarli'):
             super().__init__(name=name, surname=surname)
             self.name=name
             self.surname=surname
boy = Boy(name='Tofig', surname='Saftarli')
print(f'{boy.name} {boy.surname}')
    

# Tapşırıq 3: "Calculator" adlı bir sinif yaradin, toplama və çıxma əməliyyatlarını həyata keçirin.
class Calculator:
     def toplama(self,x,y):
          return x+y
     def cixma (self,x,y):
          return x-y
# Tapşırıq 4: "Calculator" sinifindən bir obyekt yaradin və toplama əməliyyatını həyata keçirin.
calc=Calculator()
result = calc.toplama(5,9)
print(f'toplama: {result}')
# Tapşırıq 5: Bir "Shape" sinifi yaradin, bu sinifdan türemiş "Circle" və "Rectangle" sinifləri yaradin.
class Shape():
     pass
class Circle(Shape):
     def __init__(self,radius):
         self.radius = radius 
class Rectangle(Shape):
     def __init__(self,height,width):
          self.height = height
          self.width = width

# Tapşırıq 6: Bir "Student" sinifi yaradin, ad, soyad və imtahan notları atributları olan obyekt yaradin.
          
class Student:
     def __init__(self,name, surname,ballar):
          self.name = name
          self.surname = surname
          self.ballar = ballar


# Tapşırıq 7: "Student" sinifindən bir obyekt yaradin və ortalama notunu hesablayin.
student= Student('Qismet', 'Abdurahmanov' ,[67,58,76,87])
orta_bal = sum(student.ballar) / len(student.ballar)
print (f'{student.name}{student.surname}{orta_bal}')

# Tapşırıq 8: Bir "Animal" sinifi yaradin, səs çıxaran bir metodu olsun.

class Animal: 
     def make_sound (self):
      pass


# Tapşırıq 9: "Dog" və "Cat" adlı sinifləri yaradin və onları "Animal" sinifindən türetin.
class Dog(Animal):
     def make_sound(self):
          return 'hav''hav!'
class Cat(Animal):
     def make_sound(self):
          return 'Myau''Myau!'

# Tapşırıq 10: Bir "BankAccount" sinifi yaradin, balans artırma və azaltma metotları əlavə edin.
class BankAccount:
     def __init__(self,balans):
          self.balans = balans
     def balans_artir(self, mebleg):
          self.balans += mebleg
     def balans_azalt (self,mebleg):
          self.balans -= mebleg 
     

# Nümunə obyekt yaratmaq və əməliyyatları həyata keçirmək:
xezine = BankAccount(3000)
xezine.balans_artir(1300)
xezine.balans_azalt(800)
print(f'Yekun mebleg: {xezine.balans}')