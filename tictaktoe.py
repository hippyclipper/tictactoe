import pygame

#hippyclipper

screenScale = 8
width = int(100 * screenScale)
height = width
UP = -1
DOWN = 1
RED = (255,0,0)
BLUE = (0,0,255)
LEFT_MOUSE = 1
RIGHT_MOUSE = 3
done = False

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

class Board:
    def __init__(self,w,h):
        
        self.x = w//3
        self.y = h//3
        self.w = w
        self.h = h
        self.smallSide = 10
        
        self.rec1 = pygame.Rect(0,self.y, self.w, self.smallSide)
        self.rec2 = pygame.Rect(0,self.y*2, self.w, self.smallSide)
        
        self.rec3 = pygame.Rect(self.x, 0, self.smallSide, self.h)
        self.rec4 = pygame.Rect(self.x*2, 0, self.smallSide, self.h)
        
    def draw(self):
        
        pygame.draw.rect(screen, RED, self.rec1)
        pygame.draw.rect(screen, RED, self.rec2)
        pygame.draw.rect(screen, RED, self.rec3)
        pygame.draw.rect(screen, RED, self.rec4)


class Piece:
    
    def __init__(self, x, y):
        
        self.x = x * width//3 + (width//3//2)
        self.y = y * height//3 + (height//3//2)
        self.r = 20
        
    def draw(self):
        
        pygame.draw.circle(screen, RED, (self.x, self.y), self.r)
        
        
class Cross(Piece):
    def __init__(self,x,y):
        
        super().__init__(x, y)
        
        offsetX = 50
        offsetY = 50
        
        self.xTop = (x*width//3) + offsetX
        self.yTop = (y*height//3) + offsetY
        self.xBot = x*width//3 + width//3 - offsetX
        self.yBot = y*height//3 + height//3 - offsetY
        
        self.xTop1 = (x*width//3) + width//3 - offsetX
        self.yTop1 = (y*height//3) + offsetY
        self.xBot1 = x*width//3 + offsetX
        self.yBot1 = y*height//3 + height//3 - offsetY
        
        self.thickness = 20
        
    def draw(self):
        
        pygame.draw.line(screen, BLUE, (self.xTop, self.yTop), (self.xBot, self.yBot), self.thickness)
        pygame.draw.line(screen, BLUE, (self.xTop1, self.yTop1), (self.xBot1, self.yBot1), self.thickness)
        
class Pieces:
    
    def __init__(self):
        
        self.pieces = []
        self.board = {}
        
    def addNew(self,x,y, cirlceTurn):
        
        x = x//(width//3)
        y = y//(height//3)
        
        if (x,y) in self.board:
            return False
        
        self.board[(x,y)] = circleTurn
        
        if circleTurn:
            self.pieces.append(Piece(x,y))
        else:
            self.pieces.append(Cross(x,y))
            
        return True
            
    def draw(self):
        
        for x in self.pieces:
            x.draw()
        
board = Board(width, height)
pieces = Pieces()
circleTurn = True
while not done:
    
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  RIGHT_MOUSE:           
            x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_MOUSE:
            x, y = pygame.mouse.get_pos()
            added = pieces.addNew(x,y, circleTurn)
            if added:
                circleTurn = not circleTurn
            
    pieces.draw()
    board.draw()
    pygame.display.flip()
    clock.tick(60)
    screen.fill((0, 0, 0))


pygame.display.quit()
pygame.quit()