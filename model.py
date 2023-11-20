from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from agents import *

import numpy as np
import matplotlib.pyplot as plt


class World(Model):

    def __init__(self, num, L, H):
        super().__init__()

        self.num_agents = num
        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(L,H,torus=True)   
        #self.phero = 0

        for (content, (x, y)) in self.grid.coord_iter():
            cell = Environment(self.next_id(),pos=(x,y), model=self)
            self.grid.place_agent(cell,(x,y))
            self.schedule.add(cell)
            

    def step(self):
        self.schedule.step()

# class phero_grid(mesa.Model):

#     def __init__(self, model_cologne:Model):

#         self.grid = mesa.space.MultiGrid(model_cologne.grid.width,model_cologne.grid.height)

#     def step(self):

#         for
        

def print_grid(model):

    agent_counts = np.zeros((model.grid.width, model.grid.height))

    for cell in model.grid.coord_iter():
        cell_content, (x, y) = cell
        for agent in cell_content:
            print(agent.amount_phero)
        agent_count = len(cell_content)
        agent_counts[x][y] = agent_count

    plt.imshow(agent_counts, interpolation='nearest')
    plt.colorbar()
    plt.show()


        
def agent_portrayal(agent):
    portrayal = {
    "Shape": "circle",
    "Color": "red",
    "Filled": "true",
    "Layer": 0,
    "r": 0.5,}
    return portrayal