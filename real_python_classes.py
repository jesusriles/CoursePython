from dataclasses import dataclass

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}."


class Empleado(Person):
    def __init__(self, name: str, age: int, 
                 empleado: bool = True, empresa: str = "Empresa no especificada") -> None:
        super().__init__(name, age)
        self.empleado = empleado
        self.empresa = empresa

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Empleado: {self.empleado}, Empresa: {self.empresa}."


# Ejemplos
jesus = Person("Jesus", 34)
aranza = Person("Aranza", 35)
homero = Empleado("Homero", 34, empresa="Geely")

print(jesus)
print(aranza)
print(homero)


# Ejemplo de dataclass
@dataclass
class Animal:
    tipo: str = "Tipo no especificado"
    edad: int = 0

perro = Animal("Perro", 12)
print(perro)
print(perro.edad)
