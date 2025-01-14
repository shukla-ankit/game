import pygame as pg

BG = (60, 60, 60)
GREY = (50, 50, 50)

class grid:
    def __init__(self):
        pg.init()
        self.size = (400, 300) 

    def draw(self, tsize):
        self.grid = pg.display.set_mode(self.size)
        pg.display.set_caption('===== S N A K E =====')
        self.grid.fill(BG)
        for x in range(tsize, self.size[0], tsize):
            pg.draw.line(self.grid, GREY, (x, 0), (x, self.size[1]))

    def run(self):
        fps = 10
        run = True
        clock = pg.time.Clock()
        while run:
            clock.tick(fps)
            self.draw(100)    
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            pg.display.update()
        pg.quit()

            
