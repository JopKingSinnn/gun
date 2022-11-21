import math
from random import choice, randint
import pygame
FPS = 60
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x + self.r > 740:
            self.vx = -self.vx
        if  self.y + self.r > 510:
            self.vy = -self.vy
        self.vy -= 0.2
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        '''
        рисует ядра и дробь
        '''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((b.x - target.x)**2 + (b.y - target.y)**2) < (target.r + b.r) ** 2:
            return True
class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.bullet = False
    def fire2_start(self, event):
        self.f2_on = 1
    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (40, 480),
            50
        )
        self.l = 110
        self.w = 40
        self.x = 40
        self.y = 470

        pygame.draw.polygon(screen, self.color,
                        [[self.x, self.y],
                         [self.x + (self.f2_power+100)/170*self.l*math.cos(self.an), self.y + (self.f2_power+100)/170*self.l*math.sin(self.an)],
                         [self.x + (self.f2_power+100)/170*self.l*math.cos(self.an)+self.w*math.sin(self.an), self.y + (self.f2_power+100)/170*self.l*math.sin(self.an)-self.w*math.cos(self.an)],
                         [self.x + self.w*math.sin(self.an), self.y-self.w*math.cos(self.an)]])
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = BLACK
class Target:
    def __init__(self):
        """ Конструктор класса Target
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.vy=0
        self.points = 0
        self.live = 1
        self.new_target()
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 700)
        y = self.y = randint(300, 500)
        r = self.r = randint(2, 50)
        color = self.color = RED
        self.vy=randint(-3, 3)
    def draw(self):
        # create a surface object, image is drawn on it.
        imp = pygame.draw.circle(screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if  self.y + self.r > 510 or self.y - self.r < 0:
            self.vy = -self.vy
        self.y -= self.vy
font_name = pygame.font.match_font('arial')
def scores(scr, text, size, x, y):
    '''
    вывод счета, берет на вход текст, который надо вывести, его размер и положение на экране
    '''
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    scr.blit(text_surface, text_rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
points = 100
targets = []
clock =pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREY, (0, 530, 800, 70)) # created earth for balls to bounce
    pygame.draw.rect(screen, GREY, (750, 0, 50, 600)) # created earth for balls to bounce
    gun.draw()
    for t in range(2):
        target.draw()
        target.move()
    for b in balls:
        b.draw()
        gun.bullet = False
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:  # Выход из игры по нажатию пробела (сделал чтобы за мышкой не тянуться каждый раз)
            if event.key == pygame.K_SPACE:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    target.live = 1
    for b in balls:
        b.move()
        scores(screen, str(points), 26, 15, 10)
        if hittest(b, target) and target.live:
            target.live = 0
            points += 1
            for t in range(2):
                target.new_target()
            print(bullet)
            balls=[]
            bullet = 0
    gun.power_up()
pygame.quit()
print(points)