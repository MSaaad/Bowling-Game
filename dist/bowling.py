
import pygame
pygame.init()
clock = pygame.time.Clock()

class window():
    def __init__(self):
        self.win=pygame.display.set_mode((1200,600))
        pygame.display.set_caption("BOWLING")
        self.x=900
        self.y=560
        self.yy=0
        self.xx=700
        self.position1=350
        self.position2=600
        self.vel=6
        clock=pygame.time.Clock()
        self.color=(55,55,50)
        self.color2=(250,200,200)
        self.color3 = (0,0,0)
        self.radius=(30)
        self.boundary1=740
        self.boundary2=1000
        self.boundary3=30
        self.boundary4=33
        
        self.a = 950
        self.b = 910
        self.c = 870
        self.d = 830
        self.e = 790
        self.f = 810
        self.g = 850
        self.h = 890
        self.i = 930
        self.j = 830
        self.k = 870
        self.l = 910
        self.m = 850
        self.n = 890
        self.o = 870
    
    def main_menu(self):
        self.intro= True
        while self.intro:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.intro=False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.win.fill((255,255,255))
            self.font = pygame.font.SysFont('freesansbold.ttf',50)
            self.win.blit(self.font.render('BOWLING PINS PRESS Q TO QUIT AND C TO CONTINUE',True,(self.color3)), (100, 205))
                          
            pygame.display.update()
            clock.tick(15)

class movement(window):
    def display(self):
        score = 0    
        self.run=True
        self.speedy = 0
        while self.run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_SPACE:
                       self.speedy = -3
                    
            keys=pygame.key.get_pressed()
            self.y += self.speedy
            if self.y == 560:
                if keys[pygame.K_LEFT]and self.x > self.boundary1:
                    self.x-=5
                if keys[pygame.K_RIGHT] and self.x < self.boundary2:
                    self.x+=5
                if keys[pygame.K_SPACE] and self.y > self.boundary3:
                    self.y -= 10  
            if self.y < -20:
                self.speedy = 0
                self.x=900
                self.y = 560
            if  not (self.x + self.radius < self.a or self.x - self.radius > self.a + 20 or self.y + self.radius > 50):
                self.a  = -self.a
                score = score + 1
            if  not (self.x + self.radius < self.b or self.x - self.radius > self.b + 20 or self.y + self.radius > 50):
                self.b  = -self.b
                score = score + 1 
            if  not (self.x + self.radius < self.c or self.x - self.radius > self.c + 20 or self.y + self.radius > 50):
                self.c  = -self.c
                score = score + 1
            if  not (self.x + self.radius < self.d or self.x - self.radius > self.d + 20 or self.y + self.radius > 50):
                self.d  = -self.d
                score = score + 1 
            if  not (self.x + self.radius < self.e or self.x - self.radius > self.e + 20 or self.y + self.radius > 50):
                self.e  = -self.e
                score = score + 1 
            if  not (self.x + self.radius < self.f or self.x - self.radius > self.f + 20 or self.y + self.radius > 50):
                self.f  = -self.f
                score = score + 1 
            if  not (self.x + self.radius < self.g or self.x - self.radius > self.g + 20 or self.y + self.radius > 50):
                self.g  = -self.g
                score = score + 1
            if  not (self.x + self.radius < self.h or self.x - self.radius > self.h + 20 or self.y + self.radius > 50):
                self.h  = -self.h
                score = score + 1
            if  not (self.x + self.radius < self.i or self.x - self.radius > self.i + 20 or self.y + self.radius > 50):
                self.i  = -self.i
                score = score + 1
            if  not (self.x + self.radius < self.j or self.x - self.radius > self.j + 20 or self.y + self.radius > 50):
                self.j  = -self.j
                score = score + 1
            if  not (self.x + self.radius < self.k or self.x - self.radius > self.k + 20 or self.y + self.radius > 50):
                self.k  = -self.k
                score = score + 1
            if  not (self.x + self.radius < self.l or self.x - self.radius > self.l + 20 or self.y + self.radius > 50):
                self.l  = -self.l
                score = score + 1
            if  not (self.x + self.radius < self.m or self.x - self.radius > self.m + 20 or self.y + self.radius > 50):
                self.m  = -self.m
                score = score + 1
            if  not (self.x + self.radius < self.n or self.x - self.radius > self.n + 20 or self.y + self.radius > 50):
                self.n  = -self.n
                score = score + 1
            if  not (self.x + self.radius < self.o or self.x - self.radius > self.o + 20 or self.y + self.radius > 50):
                self.o  = -self.o
                score = score + 1
            def Score(count):
                font = pygame.font.SysFont('georgia', 50)
                text = font.render("Score Board: "+str(count), True, (0,0,0))
                self.win.blit(text,(100,265))
            self.win.fill((250,100,150))     
            pygame.draw.rect(self.win,self.color2,(self.xx,self.yy,self.position1,self.position2))
            pygame.draw.circle(self.win,self.color,(self.x,self.y),self.radius)
            
            pygame.draw.rect(self.win,(255,102,178),(self.a,10,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.b,10,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.c,10,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.d,10,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.e,10,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.f,52,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.g,52,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.h,52,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.i,52,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.j,95,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.k,95,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.l,95,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.m,138,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.n,138,20,40))
            pygame.draw.rect(self.win,(255,102,178),(self.o,182,20,40))
            Score(score)
            pygame.display.update()
        clock.tick(60)		
if __name__=='__main__':
    z=window()
    z.main_menu()
    y=movement()
    y.display()    
pygame.quit()
