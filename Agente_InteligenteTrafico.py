import os
def bienvenida():
    '''
    Parametro
    --------------
    No ingresa ningun parametro

    Retorna 
    --------------
    No retorna nada
    
    Funcion
    ----------------
    Nos da un membrete de bienvenida
    
    '''
    #Imprime el la cantidad de 56 '*'
    print("="*44)
    #imprime una bienvenida
    print("Bienvenido al Agente inteligente Trafico ")
    #imprime una linea divisora 
    print("="*44)
    
def agente_inteligente():
    '''
    Parametro
    --------------
    Recibe ningun parametro

    Retorna 
    --------------
    No retorna nada
    
    Funcion
    ----------------
    En esta funcion desarolla el estado_aspiradora de la aspiradora y los estados que tiene esta
    
    '''
    diccionario_trafico = {"Quito - Sto. Domingo" : '0', "Quito - Cayambe": '0', 'Quito - Papallacta': '0', 'Quito - Aloag': '0'}

    print("Si tiene trafico ingrese 1 caso contrario 0")
    carretera1 = input("Existe trafico en la via Quito - Sto. Domingo : ")
    carretera2 = input("Existe trafico en la via Quito - Cayambe : ")
    carretera3 = input("Existe trafico en la via Quito - Papallacta : ")
    carretera4 = input("Existe trafico en la via Quito - Aloag : ")
    accion = 0 

    print("="*44)
    if carretera1 == '1':
        print("En la ruta Quito - Sto. Domingo existe trafico ")
        print("Recomendamos tomas las medidas pertinentes")
        accion = accion +1
         
    if carretera2 == '1':
        print("En la ruta Quito - Cayambe existe trafico ")
        print("Recomendamos tomas las medidas pertinentes")
        accion = accion +1
       
    if carretera3 == '1':
        print("En la ruta Quito - Papallacta existe trafico ")
        print("Recomendamos tomas las medidas pertinentes")
        accion = accion +1
          
    if carretera4 == '1':
        print("En la ruta Quito - Aloag existe trafico ")
        print("Recomendamos tomas las medidas pertinentes")
        accion = accion +1
        
    if carretera1 == '0':
        print("En la ruta Quito - Sto. Domingo no existe trafico ")
        print("Maneje con cuidado y un excelente viaje")
         
    if carretera2 == '0':
        print("En la ruta Quito - Cayambe no existe trafico ")
        print("Maneje con cuidado y un excelente viaje") 
    if carretera3 == '0':
        print("En la ruta Quito - Papallacta no existe trafico ")
        print("Maneje con cuidado y un excelente viaje")
    if carretera4 == '0':
        print("En la ruta Quito - Aloag no existe trafico ")
        print("Maneje con cuidado y un excelente viaje")

    print("El costo de la accion es de: ",accion)   



if  __name__ == "__main__":
    diccionario_trafico = {"Quito - Sto. Domingo" : '0', "Quito - Cayambe": '0', 'Quito - Papallacta': '0', 'Quito - Aloag': '0'}
    #llama a la fncion bienvenida
    bienvenida()
    
    while True:
        #llama a la funcion accion y como parametro la funcion menu 
        agente_inteligente()
        print("="*44)
        input("presione enter para continuar")
        
        os.system('cls')
