import pgzrun

TITLE = "Maze runner"
WIDTH = 600
HEIGHT = 800
RUCH = 5

CZERWONY = (255, 0, 0)

alien = Actor('alien', anchor=('center', 'center'))
gorna_sciana = Rect((0,0), (WIDTH, 30))
dolna_sciana = Rect((0,HEIGHT-30), (WIDTH, HEIGHT))

def draw():
    screen.fill('black')
    alien.draw()
    screen.draw.filled_rect(gorna_sciana, CZERWONY)
    screen.draw.filled_rect(dolna_sciana, CZERWONY)

def update():
    if keyboard.left:
        alien.x -= RUCH
    elif keyboard.right:
        alien.x += RUCH
    elif keyboard.up:
        alien.y -= RUCH
    elif keyboard.down:
        alien.y += RUCH

pgzrun.go()
