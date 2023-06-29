import math
import pygame
import sys

colors = {
    'blue': (135, 206, 235),
    'green': (0, 255, 0),
    'red': (255, 0, 0),
    'black': (0, 0, 0),
    'yellow': (249, 215, 28),
    'white': (255, 255, 255),
    'purple': (255,0,255)
}

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    @property
    def grid_coords(self):
        return round(self.x), round(self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Planet:

    def __init__(self, pos: Vector, vel, mass, hole_pos: Vector, color=colors['blue'], radius=15, hole_radius=0):
        #self.pos = pos
        self.vel = vel
        self.acc = Vector(0, 0)
        self.color = color
        self.radius = radius
        self.hole_radius = hole_radius
        self.circle_center = pos

        self.hole_pos = hole_pos

        d = mass/((4/3)*math.pi*(radius**3))
        hole_mass = (4/3)*math.pi*(hole_radius**3)*d
        self.mass = mass - (4/3)*math.pi*(hole_radius**3)*d

        '''
        pos -> wektor srodka masy
        hole_pos -> wektor środka wydronżonej dziury
        new_pos -> wektor środka masy po wydrązeniu dziury
        '''
        x, y = pos.grid_coords
        x_h, y_h = hole_pos.grid_coords
        x_new = x + ((x - x_h)*hole_mass/mass)
        print(hole_mass/mass)
        y_new = y + ((y - y_h)*hole_mass/mass)
        self.pos = Vector(x_new, y_new)
        print(self.pos)

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.circle_center.grid_coords, self.radius)
        pygame.draw.circle(win, colors['black'], self.hole_pos.grid_coords, self.hole_radius)
        pygame.draw.circle(win, colors['white'], self.pos.grid_coords, 5)



    def calculate_acceleration(self, planet_list, g):
        acc_components = []
        for planet in planet_list:
            if planet != self:
                r_vec = planet.pos - self.pos
                r = abs(r_vec)
                acc = g * planet.mass / r ** 3 * r_vec
                acc_components.append(acc)
        self.acc = sum(acc_components, start=Vector(0, 0))

    def update(self, dt):
        self.pos = self.pos + self.vel * dt + 0.5 * self.acc * dt ** 2
        self.circle_center = self.circle_center + self.vel * dt + 0.5 * self.acc * dt ** 2
        self.hole_pos = self.hole_pos + self.vel * dt + 0.5 * self.acc * dt ** 2
        self.vel = self.vel + self.acc * dt


class Simulation:
    dt = 0.05
    g = 0.001

    def __init__(self, planet_list, win_size):
        pygame.init()
        self.win = pygame.display.set_mode(win_size)
        self.planet_list = planet_list

    def calculate_acceleration(self):
        for planet in self.planet_list:
            planet.calculate_acceleration(self.planet_list, self.g)

    def update(self):
        for planet in self.planet_list:
            planet.update(self.dt)

    def draw(self):
        for planet in self.planet_list:
            planet.draw(self.win)

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.win.fill(colors['black'])
            self.calculate_acceleration()
            self.update()
            self.draw()
            pygame.display.flip()


star1 = Planet(
    pos=Vector(500, 700),
    vel=Vector(0, 0),
    mass=1_000_000,
    radius=50,
    color=colors['yellow'],
    hole_pos=Vector(515, 700),
    hole_radius=25 #warto pokazać dla 50 -> brak masy (planety)
    )

p1 = Planet(
    pos=Vector(400, 600),
    vel=Vector(2, -2),
    radius=20,
    mass=3,
    color=colors['blue'],
    hole_pos=Vector(400, 600),
    hole_radius=0
)

p2 = Planet(
    pos=Vector(600, 600),
    vel=Vector(2, 2),
    radius=20,
    mass=3,
    color=colors['green'],
    hole_pos=Vector(600, 600),
    hole_radius=0
)

p3 = Planet(
    pos=Vector(400, 800),
    vel=Vector(-2, -2),
    radius=20,
    mass=3,
    color=colors['red'],
    hole_pos=Vector(400, 800),
    hole_radius=0
)

p4 = Planet(
    pos=Vector(600, 800),
    vel=Vector(-2, 2),
    radius=20,
    mass=3,
    color=colors['purple'],
    hole_pos=Vector(600, 800),
    hole_radius=0
)

#gwiazda game-changer
# star2 = Planet(
#     pos=Vector(0, 2000),
#     vel=Vector(1, -1),
#     mass=1_000_000,
#     radius=50,
#     color=colors['yellow'],
#     hole_pos=Vector(1000, 2000),
#     hole_radius=0 #warto pokazać dla 50 -> brak masy (planety)
#     )

comet = Planet(
    pos=Vector(0, 200),
    vel=Vector(0.2, 0.6),
    radius=10,
    mass=0.5,
    color=colors['white'],
    hole_pos=Vector(0, 200),
    hole_radius=0
)


# star1 = Planet(
#     pos=Vector(500, 500),
#     vel=Vector(0, 0),
#     mass=1_000_000,
#     radius=50,
#     color=colors['yellow'],
#     hole_pos=Vector(525, 500),
#     hole_radius=25 #warto pokazać dla 50 -> brak masy (planety)
#     )
# p1 = Planet(
#     pos=Vector(400, 400),
#     vel=Vector(2, -2),
#     radius=20,
#     mass=3,
#     color=colors['blue'],
#     hole_pos=Vector(400, 400),
#     hole_radius=0
# )
#
# p2 = Planet(
#     pos=Vector(350, 350),
#     vel=Vector(1.6, -1.6),
#     radius=10,
#     mass=0.3,
#     color=colors['red'],
#     hole_pos=Vector(350, 350),
#     hole_radius=0
# )

sim = Simulation([star1, p1, p2, p3, p4, comet], (1500, 1000))
sim.run()
