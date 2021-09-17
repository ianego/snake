#Se importa el programa HCRfinal (donde se hace la resolución del problema)
import HCRfinal
#Se importa la librería pygame
import pygame

#Se creo la función redrawGameWindow con los parámetros Dir, p1 y p2
def redrawGameWindow(Dir, p1, p2):
    global x, y, Side_A, Side_B #Se declaran variables globales x, y, Side_A y Side_B
    #        
    win.blit(bg,(0,0))
    ypos = 300
    for item in Side_A:
        win.blit(item,(5,ypos))
        ypos = ypos - 60

    ypos = 300
    for item in Side_B:
        win.blit(item,(450,ypos))
        ypos = ypos - 60

    if p1 != 'Unknown':
        if right:
            win.blit(BoatRight,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))           
        elif left:
            win.blit(BoatLeft,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))            
    else:
        win.blit(char,(x, y))
    pygame.display.update()

#Se creo la función get_characters, con los parámetros d, p1 y p2
def get_characters(d, p1, p2):
    #Se hace uso de una condicional
    if p2 == 'Zorro': #Si p2 es igual a zorro, character valdrá fox
        character = fox
    elif p2 == 'Maiz': #Si p2 es igual a maiz, character valdrá corn
        character = corn
    elif p2 == 'Ganzo': #Si p2 es igual a ganzo, character valdrá duck
        character = duck
    else: #Si no, character valdrá falmer
        character = farmer
    return (d, farmer, character) #La función regresa d, famer y character

#Se creo la función Embark_characters, con los parámetros B, p1, p2
def Embark_characters(B, p1, p2):
    #Se hace uso de condicionales
    if p1 in B: #Si p1 esta en B
        B.remove(p1) #Será removido p1 del arreglo B     
    if p2 in B: #si p2 esta en B
        B.remove(p2) #Será removido p2 del arreglo B

#Se creo la función Disembark_characters, con los parámetros A, p1, p2 
def Disembark_characters(A, p1, p2):
    #Se hace uso de condicionales
    if p1 not in A: #si p1 no está en A
        A.append(p1) #p1 será agregado al arreglo A
    if p2 not in A: #si p2 no está en B
        A.append(p2) #p2 será agregado al arreglo B

#Se creo la función HCR_anmacion, con el parámetro P    
def HCR_animacion(P):
    #Se declaran las variables globales x, y, left, right, vel, Side_A, Side_B
    global x, y, left, right, vel
    global Side_A, Side_B

    clock = pygame.time.Clock()
    run = True
    move = 0
    while run:
        clock.tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
            right = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_B, p1, p2)
                for step in range(65):
                    x -= vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_A, p1, p2)

        elif keys[pygame.K_RIGHT]:
            right = True
            left = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_A, p1, p2)
                for step in range(65):
                    x += vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_B, p1, p2)
        else:
            redrawGameWindow ('Standby','Unknown', 'Unknown')
        

    pygame.quit()

#Se creo la función Busca_solucion
def Busca_solucion():
    P = HCRfinal.HCR() #P valdrá el retorno de la función HCRfinal.HCR()
    while len(P) > 22: #mientras p mida más de 22, se corre el programa
    #while len(P) > 42:
        HCRfinal.reiniciar_sistema() #HCRfinal hará uso de reiniciar_sistema
        print ('\nBuscando una mejor solución, Longitud del Path', len(P)) #se imprimirá un mensaje indicando que se buscará una mejor solución y cuanto mide p
        P = HCRfinal.HCR() #P valdrá el retorno de la función HCRfinal.HCR()
    print (P) #Se imprime P
    print (len(P)) #se imprime cuanto mide P
    print ('\n =====> Solución encontrada:') #Se imprime el mensaje que se econtrlo la solucion
    return (P) #Se regresa P

 
            
P = Busca_solucion() #P valdrá el retorno de la función Busca_solucion
print ('Aquí su animación') #Se imprime el mensaje "Aquí su animación"

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("How to Cross the River")

BoatRight   = pygame.image.load('BoteRight.png')
BoatLeft    = pygame.image.load('BoteLeft.png')
bg          = pygame.image.load('seaL.png')
char        = pygame.image.load('BoteRight.png')
fox         = pygame.image.load('fox.png')
corn        = pygame.image.load('corn.png')
duck        = pygame.image.load('duck.png')
farmer      = pygame.image.load('farmer.png')
x       = 10
y       = 425
vel     = 5
left    = False
right   = False

Side_A = [farmer, fox, duck, corn]
Side_B = []

HCR_animacion(P)




