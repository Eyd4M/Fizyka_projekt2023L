# Ziemia i Mars jak w układzie słonecznym
star1 = Planet(
    pos=Vector(500, 500),
    vel=Vector(0.2, 0),
    mass=1_000_000,
    radius=50,
    color=colors['yellow'],
    hole_pos=Vector(500, 500),
    hole_radius=0 #warto pokazać dla 50 -> brak masy (planety)
    )

p1 = Planet(
    pos=Vector(400, 400),
    vel=Vector(2, -2),
    radius=20,
    mass=3,
    color=colors['blue'],
    hole_pos=Vector(400, 400),
    hole_radius=0
)

p2 = Planet(
    pos=Vector(350, 350),
    vel=Vector(1.6, -1.6),
    radius=10,
    mass=0.3,
    color=colors['red'],
    hole_pos=Vector(350, 350),
    hole_radius=0
)

#Układ planet - zwykła, wycięty środek, przesunięty wycięty środek - kolizja
p1 = Planet(
    pos=Vector(400, 400),
    vel=Vector(2, -2),
    radius=20,
    mass=3,
    color=colors['blue'],
    hole_pos=Vector(410, 400),
    hole_radius=10
)

p2 = Planet(
    pos=Vector(600, 400),
    vel=Vector(2, 2),
    radius=20,
    mass=3,
    color=colors['green'],
    hole_pos=Vector(600, 400),
    hole_radius=0
)

p3 = Planet(
    pos=Vector(400, 600),
    vel=Vector(-2, -2),
    radius=20,
    mass=3,
    color=colors['red'],
    hole_pos=Vector(400, 600),
    hole_radius=10
)


#Planety fajne z kometą

star1 = Planet(
    pos=Vector(500, 700),
    vel=Vector(0.2, 0),
    mass=1_000_000,
    radius=50,
    color=colors['yellow'],
    hole_pos=Vector(500, 700),
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