
#Primero se exporta la libería random para usarlo posteriormente
import random

#Se declaran 3 arreglos, estos representaran ambos lados del río y la balsa, en el primero estan todos los objetos necesarios y los otros vacíos pues aun no se completa nada
Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
Lado_B = []
Path = []

#Se creo la función selección, recibe de parámetro L
def seleccion(L):
    op = random.randint(0,len(L)-1)
    return (L[op])

#Se creo la función viaje, recibe de parámetros F y D
def Viaje(F, D):
    p1 = seleccion(F) #Para obtener la p1 se usa la función selección con el parametro F
    #print ('Selección -> ', p1)
    if p1 != 'Granjero':  #Se hace uso de una condición si p1 no es igual a Granjero
        #p1 será quitado del arreglo F y agregado al arreglo D
        F.remove(p1)
        D.append(p1)

    #Cuando se es granjero granjero es removido del arreglo F y se agregará al arreglo D
    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    return ('Granjero',p1) #Se regresa Granjero y p1

#Se creo la función valida_estado, recibe el parámetro L
def valida_estado(L):
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2: #Si Maíz, ganzo estan en L y L mide 2 se regresa falso
        return False
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2: #Si Zorro, ganzo estan en L y L mide 2 se regresa falso
        return False
    return True #en caso contrario se regresa verdadero

#Se creo la función reiniciar_sistema
def reiniciar_sistema():
    global Lado_A, Lado_B, Path #Se hace uso de los arreglos globales Lado_A, Lado_B y path
    #Se declaran dichos arreglos
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
    Lado_B = []
    Path = []
    
#Se creo la función HCR
def HCR():
    #F y D valdrán los arreglos Lado_A y Lado_B
    F = Lado_A
    D = Lado_B
    #Mientras el arreglo Lado_B no tenga 4 objetos, se corre el programa
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)#p1 y p2 serán iguales a el retorno de la función Viaje dando los parametros F y D
        if valida_estado (F) and valida_estado (D): #Se hace uso de una condición para validar que los arreglos no incumplan con "las reglas"
            #print ('Estado valido, continuamos')
            if F == Lado_A: #Si F vale lo mismo que Lado_A en el arreglo Path se agrega "A->B : " para hacer la indicación del cambio
                Path.append('A->B :')
            else: #En caso que no en el arreglo path se agrega "B->A : " para hacer la indicación del cambio
                Path.append('B->A :')
            #Al arreglo path se agregan los valores p1 y p2
            Path.append(p1)
            Path.append(p2)
            
            #Se hace cambios de variables para que Temp valga F, F valga D y D valga Temp
            Temp = F
            F = D
            D = Temp      
        else: #En caso que no se validen los arreglos
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema() #Se reinicia el programa
            #Los arreglos F y D valdrán Lado_A y Lado_B respectivamente
            F = Lado_A 
            D = Lado_B
    return (Path) #Por último se regresa el arreglo Path

#Se creo la función main
def main():
    P = HCR() #P valdrá la función HCR
    while len(P) > 22: #mientras que P valga más que 22, se corre el programa
        reiniciar_sistema() #Se reinicia el programa
        print ('\nBuscando una mejor solución, Longitud del Path', len(P)) #Se le indica al usuario que la solución no fue la encontrada y su progreso
        P = HCR()
    #Se imprime P y y el tamaño de P
    print (P)
    print (len(P))
            
main() #Se inicializa el programa

  
