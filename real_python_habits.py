class Habitos:

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.semana: dict[int, dict[str, bool]] = {}
  
    def iniciar_dias_semana(self) -> dict[str, bool]:
        """ 
        Input: NA
        Return: Regresa un diccionario con {Dia de la semana: Boolean}
        """
        temp_dic: dict[str, bool] = {"Lunes": False, 
                                     "Martes": False,
                                     "Miercoles": False,
                                     "Jueves": False,
                                     "Viernes": False,
                                     "Sabado": False,
                                     "Domingo": False}
        return temp_dic

    def crear_semana(self, num_semana: int):
        try:
            semana = int(num_semana)

            if semana not in self.semana:
                self.semana.update({semana: self.iniciar_dias_semana()})
                print(f"[Ok] Semana {semana} creada para {self.nombre}.")
            else:
                raise ValueError(f"La semana {semana} ya existe!")
        except Exception as e:
            print(f"[Error] No se pudo agregar la semana, error: {e}")


ejercicio = Habitos("Ejercicio")

# crear semanas
ejercicio.crear_semana(34)
ejercicio.crear_semana(34)

# checar que no se pueda repetir la semana
ejercicio.crear_semana("qwe")

# imprimir semana
print(ejercicio.semana)

lectura = Habitos("Lectura")
lectura.crear_semana(34)
