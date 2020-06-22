import pygame
import time
import math
import numpy
from random import *
 
 
class GameConfig :
    #TOUTES LES VARIABLES FIXES
 
    windowW=960
    windowH=540
  
    shurikenC = 20
 
    progressW = 180
    progressH = 25
 
    flecheW = 300
    flecheH = 300
 
    pointeurW = round(progressW / 9)
    pointeurH = round(progressH / 2)
 
    persoW = 61
    persoH = 113
 
    ennemyW1 = 40
    ennemyH1 = 36
 
    ennemyW2 = 64
    ennemyH2 = 51
 
    ennemyW3 = 95
    ennemyH3 = 80
 
    ennemyW4 = 80
    ennemyH4 = 41
 
    white = (255,255,255)
    red = (255,0,0)
    bleu=(113,177,227)
 
    imgBackground = pygame.image.load('image/background.jpg')
    imgBackground = pygame.transform.scale(imgBackground,(windowW,windowH))
    imgShuriken = pygame.image.load('image/shuriken.png')
    imgShuriken = pygame.transform.scale(imgShuriken,(shurikenC,shurikenC))
    imgProgress = pygame.image.load('image/power_barre.png')
    imgProgress = pygame.transform.scale(imgProgress,(progressW,progressH))
    imgFleche = pygame.image.load('image/fleche1.png')
    imgFleche = pygame.transform.scale(imgFleche,(flecheW,flecheH))
    imgPointeur = pygame.image.load('image/pointeur.png')
    imgPointeur = pygame.transform.scale(imgPointeur,(pointeurW,pointeurH))
    imgPerso = pygame.image.load('image/perso.png')
    imgPerso = pygame.transform.scale(imgPerso,(persoW, persoH))
 
    imgNuage_gris = pygame.image.load('image/nuage_1.png')
    imgNuage_gris = pygame.transform.scale(imgNuage_gris,(windowW,windowH))
    imgNuage_blanc = pygame.image.load('image/nuage_2.png')
    imgNuage_blanc = pygame.transform.scale(imgNuage_blanc,(windowW,windowH))
 
    imgEnnemy1 = pygame.image.load('image/boon_jaune.png') #boon jaune
    imgEnnemy1 = pygame.transform.scale(imgEnnemy1,(ennemyW1,ennemyH1))
 
    imgEnnemy2 = pygame.image.load('image/boon_orange.png') #boon orange
    imgEnnemy2 = pygame.transform.scale(imgEnnemy2,(ennemyW2,ennemyH2))
 
    imgEnnemy3 = pygame.image.load('image/boon_rose_1.png') #boon violet/rose
    imgEnnemy3 = pygame.transform.scale(imgEnnemy3,(ennemyW3,ennemyH3))
 
    imgEnnemy4 = pygame.image.load('image/boon_vert.png') #boon vert
    imgEnnemy4 = pygame.transform.scale(imgEnnemy4,(ennemyW4,ennemyH4))
 
 
    pygame.mixer.init(frequency=8000, size=16, channels=1)
 
    sonShuriken = pygame.mixer.Sound("sound/shuriken.wav")
    sonGameOver = pygame.mixer.Sound("sound/game_over.wav")
    sonHit = pygame.mixer.Sound("sound/hit_damage.wav")
    sonThemePoke = pygame.mixer.Sound("sound/poke_theme.wav")
    sonThemeEpic1 = pygame.mixer.Sound("sound/epic_orchestral.wav")
    sonThemeEpic2 = pygame.mixer.Sound("sound/epic_tambour_theme.wav")
    sonWSR = pygame.mixer.Sound("sound/wiiSportResort.wav")
 
 
 
 
class Ennemy :
 
    def __init__(self, type) :
 
        
 
        if type == 1 : #boon orange
            self.largeur = GameConfig.ennemyW2
            self.longueur = GameConfig.ennemyH2
            self.imageEnnemy = GameConfig.imgEnnemy2
            self.ennemyX = 960
            self.ennemyY = randint(0,240-GameConfig.ennemyH2)
            self.ennemySpeed = 0.4

        if type == 2 : #boon jaune
            self.largeur = GameConfig.ennemyW1
            self.longueur = GameConfig.ennemyH1
            self.imageEnnemy = GameConfig.imgEnnemy1
            self.ennemyX = 960
            self.ennemyY = randint(0,240-GameConfig.ennemyH1)
            self.ennemySpeed = 0.3
 
        if type == 3 : #boon rose
            self.largeur = GameConfig.ennemyW3
            self.longueur = GameConfig.ennemyH3
            self.imageEnnemy = GameConfig.imgEnnemy3
            self.ennemyX = 960
            self.ennemyY = randint(0,240-GameConfig.ennemyH3)
            self.ennemySpeed = 0.5
 
        if type == 4 : #boon vert
            self.largeur = GameConfig.ennemyW4
            self.longueur = GameConfig.ennemyH4
            self.imageEnnemy = GameConfig.imgEnnemy4
            self.ennemyX = 960
            self.ennemyY = randint(0,240-GameConfig.ennemyH4)
            self.ennemySpeed = 0.7
  
    def getImg(self):
        return self.imageEnnemy
    def getX(self) :
        return self.ennemyX
    def getY(self) :
        return self.ennemyY
    def getSpeed(self) :
        return self.ennemySpeed
    def getW(self):
        return self.largeur
    def getH(self):
        return self.longueur
 
    def setX(self,X) :
        self.ennemyX=X
    def setY(self,Y) :
        self.ennemyY=Y
    def setSpeed(self, X) :
        self.ennemySpeed = self.ennemySpeed * X
 
 
class Shuriken :
    def __init__(self,angle,puissance) :
        self.imgShuriken=GameConfig.imgShuriken
        self.shurikenX=100
        self.shurikenY=360
        self.puissance=puissance
        self.angle=angle
        self.horl=0
        self.vitesse=0.1
    def getImg(self) :
        return self.imgShuriken
    def getX(self) :
        return self.shurikenX
    def getY(self) :
        return self.shurikenY
    def getL(self) :
        return self.shurikenL
    def getAngle(self) :
        return self.angle
    def getPuissance(self) :
        return self.puissance
    def getHorl(self) :
        return self.horl
    def setX(self,X) :
        self.shurikenX=X
    def setY(self,Y) :
        self.shurikenY=Y
    def setL(self) :
        self.shurikenL=False
    def avancer(self) :
        self.horl=self.horl+self.vitesse
 
class EnsembleShuriken :
    def __init__(self) :
        self.ensemble=[]
    def add(self,shuriken) :
        self.ensemble.append(shuriken)
    def rem(self,shuriken) :
        self.ensemble.remove(shuriken)
    def getEnsembleShuriken(self) :
        return self.ensemble
    def getSize(self) :
        return self.ensemble.length()
 
class GameState :
 
    angleIncrement = 2
 
    def __init__(self) :
        #position shuriken
        self.shurikenXI = 100
        self.shurikenYI = 360
 
        self.EnsembleShuriken=EnsembleShuriken()
 
        #force et position progress barre avec la fleche qui l'indique
        self.forceI=4
        self.force=self.forceI
 
 
        self.progressX=50
        self.progressY=510
 
        self.pointeurX=50
        self.pointeurY=523
 
        #position de la fleche qui gere l'angle
        self.angle=0
 
        self.flecheX=self.shurikenXI + GameConfig.shurikenC/2 - GameConfig.flecheW/2
        self.flecheY=self.shurikenYI + GameConfig.shurikenC/2 - GameConfig.flecheH/2
 
        self.persoX = 40
        self.persoY = 340
 
        self.nuage_blancX = 0
        self.nuage_blancY = -200
 
        self.nuage_grisX = 0
        self.nuage_grisY = -200
 
        self.score = 0
 
 
        #variables liées aux ennemies
        self.ensembleEnnemy = []
        self.vague = 1 #correspond aux différents niveaux de difficulté
        self.t=0
        self.NonFocus=[]
 

        #variable avancement de la difficulté
        self.multiSpeed = 1
        self.multiSpawn = 1
        self.intervalSpawn = 20 #spawn tout les x de score
        self.multiSpeedMax = 8
        self.multiSpawnMax = 5
        self.newSpawn = 5 #premier spawn puis spawn suivant
 
    def draw(self,window) :
        window.fill(GameConfig.bleu)
        window.blit(GameConfig.imgBackground,(0,0))
 
        #dessiner nuage ebn fonction de position
 
        window.blit(GameConfig.imgNuage_gris,(self.nuage_grisX, self.nuage_grisY))
        window.blit(GameConfig.imgNuage_blanc,(self.nuage_blancX, self.nuage_blancY))
  
        displayMessage(window, "Score : " + str(round(self.score)), 24, 50, 10)
 
        for x in self.EnsembleShuriken.getEnsembleShuriken() :
            window.blit(x.getImg(),(x.getX(),x.getY()))
 
 
        window.blit(GameConfig.imgProgress,(self.progressX,self.progressY))
        window.blit(GameConfig.imgPerso,(self.persoX,self.persoY))
 
        imgFleche=pygame.transform.rotate(GameConfig.imgFleche,self.angle)
        window.blit(imgFleche,(self.flecheX,self.flecheY))
 
        window.blit(GameConfig.imgPointeur,(self.pointeurX+self.force*GameConfig.pointeurW-self.forceI*GameConfig.pointeurW,self.pointeurY))
 
        #Affichage des ennemy
        for x in self.ensembleEnnemy:
            window.blit(x.getImg(), (x.getX(),x.getY()))
 
 
    def advanceState(self,nextM) :
 
        if 0 <= self.score%10 < 0.05 : #pour afficher de temps en temps
            print("multiplicateurs vitesse des ennemies : " + str(self.multiSpeed))
            print("multiplicateurs nombres d'ennemies : " + str(self.multiSpawn))


        self.score = self.score + 0.05
            

        if self.multiSpeed < self.multiSpeedMax :
            self.multiSpeed = self.multiSpeed + 0.0001

        if self.multiSpawn < self.multiSpawnMax :
            self.multiSpawn = self.multiSpawn + 0.0001

 
        for x in self.ensembleEnnemy :
            x.setX(x.getX() - x.getSpeed())
 

        newSpawn = self.newSpawn
        #création ennemy
        if self.score > self.newSpawn :
            self.newSpawn = self.newSpawn + (self.intervalSpawn/self.multiSpawn)
            

            if self.score < 200 : #spawn orange et jaune
                type = randint(1,2) 
            elif self.score < 600 : #spawn orange et jaune et rose
                type = randint(1,3) 
            else : #spawn all
                type = randint(1,4)

            newEnnemy = Ennemy(type)
            newEnnemy.setSpeed(self.multiSpeed)

            self.NonFocus=[]
            self.ensembleEnnemy.append(newEnnemy)
            for x in self.ensembleEnnemy :
                    self.NonFocus.append(x)


        #éxécution du prochain mouv
        if nextM == 1 and self.angle < 90 : #monter
            self.angle = self.angle + self.angleIncrement
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
 

        if nextM == 2 and self.angle > 0 : #descendre
            self.angle = self.angle - self.angleIncrement
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
 

        if nextM == 3 and self.force < 12 : #chargement de la force
            self.force+=1


        if nextM == 4 : #lancer
            self.EnsembleShuriken.add(Shuriken(self.angle,self.force*9))
            self.force=self.forceI


        if nextM == 5 and self.angle < 90 : #monter et charger force
            self.angle = self.angle + self.angleIncrement
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            if self.force < 12 :
                self.force+=1
 

        if nextM == 6 and self.angle > 0 : #descendre et charger force
            self.angle = self.angle - self.angleIncrement
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            if self.force < 12 :
                self.force+=1


        if nextM == 7 and self.angle < 90 : #monter vite
            if self.angle + self.angleIncrement*5 > 90 :
                self.angle = 90
            else :
                self.angle = self.angle + self.angleIncrement*5
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
 

        if nextM == 8 and self.angle > 0 : #descendre vite
            if self.angle - self.angleIncrement*5 < 0 :
                self.angle = 0
            else :
                self.angle = self.angle - self.angleIncrement*5
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))


        if nextM == 9 and self.angle < 90 : #monter vite et charger
            if self.angle + self.angleIncrement*5 > 90 :
                self.angle = 90
            else :
                self.angle = self.angle + self.angleIncrement*5
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            if self.force < 12 :
                self.force+=1


        if nextM == 10 and self.angle > 0 : #descendre vite et charger
            if self.angle - self.angleIncrement*5 < 0 :
                self.angle = 0
            else :
                self.angle = self.angle - self.angleIncrement*5
            self.flecheX = self.shurikenXI + GameConfig.shurikenC/2 - (GameConfig.flecheW*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            self.flecheY = self.shurikenYI + GameConfig.shurikenC/2 - (GameConfig.flecheH*math.sqrt(2)/2*math.sin((abs(self.angle)+45)*math.pi/180))
            if self.force < 12 :
                self.force+=1

 
    def lancer(self) :
        for x in self.EnsembleShuriken.getEnsembleShuriken() :
            x.avancer()
            x.setX((x.getPuissance())*math.cos(-x.getAngle()*math.pi/180)*x.getHorl()+self.shurikenXI)
            x.setY(1/2*9.81*x.getHorl()*x.getHorl()+x.getPuissance()*math.sin(-x.getAngle()*math.pi/180)*x.getHorl()+self.shurikenYI)
            if x.getX()>960 or x.getY()>540 :
                self.EnsembleShuriken.rem(x)
  
 
    def tuer(self):
        #2 boucles qui vérifie si un des shuriken se trouve a la position d'un ennemy
        for ennemy in self.ensembleEnnemy:
            for shuriken in self.EnsembleShuriken.getEnsembleShuriken():
                if ((shuriken.getX() > ennemy.getX()) and (shuriken.getX() < ennemy.getX() + ennemy.getW())) and ((shuriken.getY() > ennemy.getY()) and (shuriken.getY() < ennemy.getY() + ennemy.getH())):
                    self.ensembleEnnemy.remove(ennemy)
                    self.EnsembleShuriken.rem(shuriken)
                    sonhit = GameConfig.sonHit
                    sonhit.play()
 

    def dichotomie(self,a,b,puissance,position1seulplanX,position1seulplanY) :
        fa=(1/4)*9.81*9.81*a*a*a*a-position1seulplanY*9.81*a*a-puissance*puissance*a*a-2*position1seulplanX*puissance*a+(position1seulplanX*position1seulplanX+position1seulplanY*position1seulplanY)
      
        m=(b+a)/2
        fm=(1/4)*9.81*9.81*m*m*m*m-position1seulplanY*9.81*m*m-puissance*puissance*m*m-2*position1seulplanX*puissance*m+(position1seulplanX*position1seulplanX+position1seulplanY*position1seulplanY)
 
        if b-a>0.0000001 :
            if fa*fm<0 :
                self.dichotomie(a,m,puissance,position1seulplanX,position1seulplanY)
            else :
                self.dichotomie(m,b,puissance,position1seulplanX,position1seulplanY)
        else :
            self.t=m
 
 
    def getIACommand(self) :
               
        ennemyXfocus = 1000
        ennemyYfocus = 1
        focus = Ennemy(1)
 
        #Trouver l'ennemi le plus proche
        if self.NonFocus :
            for x in self.NonFocus :
                if x.getX() < ennemyXfocus :
                    ennemyXfocus = x.getX()
                    focus = x
 
        ennemyXfocus = focus.getX()
        ennemyYfocus = focus.getY()
 
        puissance = 108
 
        position1seulplanX = ennemyXfocus - self.shurikenXI
        position1seulplanY = -(ennemyYfocus -  self.shurikenYI)
 
        t=0.0
        tm=True
        while tm==True :
            if (1/4)*9.81*9.81*t*t*t*t-position1seulplanY*9.81*t*t-puissance*puissance*t*t-2*position1seulplanX*puissance*t+(position1seulplanX*position1seulplanX+position1seulplanY*position1seulplanY) > 0 :
                t+=0.5
            else :
                tm=False
        self.dichotomie(0,t,puissance,position1seulplanX,position1seulplanY)
        angleTheorique=math.degrees(math.acos((position1seulplanX/self.t+focus.ennemySpeed)/(puissance*self.t)))
 
 
        angleTheoriqueinf = angleTheorique - self.angleIncrement/2
        angleTheoriquesupp = angleTheorique + self.angleIncrement/2
 
        if self.NonFocus!=[] :
            if angleTheoriqueinf<self.angle<angleTheoriquesupp and self.force==12 and focus.getX()-(focus.ennemySpeed*t)<800 :
                self.NonFocus.remove(focus)
                return 4 #tirer
            else :
                if self.angle < angleTheoriqueinf :
                    return 5 #monter et charger
                elif self.angle > angleTheoriquesupp :
                    return 6 #descendre et charger
                else :
                    return 3
        else :
            return 0
 
      
 
 
    def isOver(self) :
        for x in self.ensembleEnnemy:
            #revoir la largeur
            if(x.getX() + GameConfig.ennemyW1 < 0) :
                son = GameConfig.sonGameOver
                son.play()
                return True
            else :
               return False
 
 
def gameLoop(window,horloge) :
    gameState = GameState()
    game_over = False
    nextMove=0
    pygame.key.set_repeat(10,100)
    IA=False #Activer ou désactiver l'IA
 
    sontheme = GameConfig.sonWSR #MUSIC DE JEU
    sontheme.play()
 
 
    while not game_over :
        nextMove=0
      
        if IA==False:
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    sontheme.stop()
                    game_over = True
                    #SANS IA
                if pygame.key.get_pressed()[pygame.K_UP] : #monter
                    if pygame.key.get_pressed()[pygame.K_SPACE] :
                        nextMove = 5 #monter et charger
                    else :
                        nextMove = 1
                elif pygame.key.get_pressed()[pygame.K_DOWN] : #descendre
                    if pygame.key.get_pressed()[pygame.K_SPACE] :
                        nextMove = 6 #descendre et charger
                    else :
                        nextMove = 2
                elif pygame.key.get_pressed()[pygame.K_LEFT] : #monter2
                    if pygame.key.get_pressed()[pygame.K_SPACE] :
                        nextMove = 9 #descendre2 et charger
                    else :
                        nextMove = 7
                elif pygame.key.get_pressed()[pygame.K_RIGHT] : #descendre2
                    if pygame.key.get_pressed()[pygame.K_SPACE] :
                        nextMove = 10 #monter2 et charger
                    else :
                        nextMove = 8



                elif pygame.key.get_pressed()[pygame.K_SPACE] : #charger tire
                    nextMove = 3
 
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_SPACE : #tirer
                        nextMove = 4
                        sonshuriken = GameConfig.sonShuriken
                        sonshuriken.play()
                    #FIN SANS IA
              
 
        if IA==True :
            #AVEC IA
            nextMove = gameState.getIACommand()
            #FIN AVEC IA
        gameState.advanceState(nextMove)
        gameState.draw(window)
        if nextMove == 4 or gameState.EnsembleShuriken.getEnsembleShuriken() != []:
            gameState.lancer()
        if(gameState.isOver()) :
            sontheme.stop()
            GameConfig.sonGameOver.play()
            displayMessage(window,"GAME OVER!",150,GameConfig.windowW/2,GameConfig.windowH/2-50)
            displayMessage(window,"Appuyer sur une touche pour continuer",20,GameConfig.windowW/2,GameConfig.windowH/2+50)
            game_over = True
        pygame.display.update()
        gameState.tuer()
 
        horloge.tick(100)
    if(playAgain()) :
        gameLoop(window,horloge)
 
 
 
def playAgain() :
    time.sleep(2)
    while True :
        for event in pygame.event.get([pygame.KEYDOWN,pygame.QUIT]) :
            if event.type == pygame.QUIT :
                return False
            elif event.type == pygame.KEYDOWN :
                return True
        time.sleep(0.5)
 
 
def displayMessage(window, text, fontSize, x, y) :
    font = pygame.font.Font('BradBunR.ttf',fontSize)
    img = font.render(text, True, GameConfig.red)
    displayRect = img.get_rect()
    displayRect.center=(x,y)
    window.blit(img, displayRect)
 
 
 
 
 
 
def main() :
    pygame.init()
    horloge=pygame.time.Clock()
    window=pygame.display.set_mode((GameConfig.windowW,GameConfig.windowH))
    pygame.display.set_caption("Slice Defence")
    gameLoop(window,horloge)
    pygame.quit()
    quit()
 
 
 
main()
 
 
 
 
 

