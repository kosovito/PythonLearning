# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    altura = 1.81
    #un atributo puede ser opcional si le damos un valor en su constructor, pero ha de ser el/los ultimos
    #por lo tanto no admite multiples constructores por imperativo, pero se simulan con atributos predefinidos con valor
    #en este ejemplo hay en realidad 4 constructores (name, surname), (name, surname, edad), (name surname alias), y (name,surname,edad,alias)
    def __init__(self, name, surname, edad=18, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.edad = edad;
        self.alias = alias;
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} que mide {self.altura} está caminando con {self.edad} años")
    
    def set_altura(self, altura: float):
        self.altura = altura


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.edad = 25
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)


my_complete_person = Person("Álvaro", "García")
my_complete_person.walk()
my_complete_person = Person("Álvaro", "García", 30)
my_complete_person.walk()
my_complete_person = Person("Álvaro", "García", alias="kosovito")
my_complete_person.walk()
my_complete_person = Person("Álvaro", "García", 30, "kosovito")
my_complete_person.walk()
my_complete_person = Person("Álvaro", "García", 30, "kosovito")
my_complete_person.set_altura(1.83)
my_complete_person.walk()

#HERENCIA
#se hereda, creando la clase pasando otra como atributo
class Student(Person):
    def __init__(self, name, surname, lenguaje, edad=18, alias="Sin alias"):
        self.lenguaje = lenguaje
        #llamamos constructor del padre
        super().__init__(name, surname, edad, alias)
    def walk(self):
        super().walk()
        print(f"hacia clase de {self.lenguaje}")

my_complete_student = Student("Álvaro", "García", "Python", 30, "kosovito")
my_complete_student.walk()
    