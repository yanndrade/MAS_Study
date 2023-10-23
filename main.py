from agents import *
from model import *



if __name__ == "__main__":

    # positions = []

    cologne = ant_cologne(10,5,5)

    # print_grid(cologne)

    # for cell in cologne.grid.coord_iter():
    #     cell_content, x, y = cell
    #     if (cologne.grid.is_cell_empty((x,y))):
    #        pass
    #     else: 
    #         for ant in cell_content:
    #             ant.move()


    

    # print_grid(cologne)

    #cologne.step()

    grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
    server = mesa.visualization.ModularServer(
    ant_cologne, [grid], "Ant Cologne", {"num": 10, "L": 5, "H": 5}
    )
    # server = ModularServer(ant_cologne,
    #     [grid],
    #     "Ant cologne",
    #     {"num": 10, "L": 5, "H": 5  })
    server.port = 8521 # The default
    server.launch()
    
