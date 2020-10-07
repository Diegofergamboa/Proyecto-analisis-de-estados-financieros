
#La empresa se llama Premier_COl, es una empresa de asesorias academicas.
#Se agrega la palabra 'est' mas lo demas con el fin de consultar los estados

class empresa():
    
    def __init__(self, empleados, colaboradores, clientes, ingresos, costos, gastos):
        self.empleados = empleados
        self.colaboradores = colaboradores
        self.clientes = clientes
        self.ingresos = ingresos
        self.costos = costos
        self.gastos = gastos
        
    def estempleados(self, empleados): 
        print ('La cantidad de empleados de la empresa tiene es {}'.format(empleados))
        return
    
    
if __name__ == "__main__":

    premier = empresa(7, 1, 20, 5500000, 1000000, 500000)
    premier.estempleados(7)