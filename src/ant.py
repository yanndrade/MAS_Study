#!/usr/bin/env python3

import mesa
from mesa.model import Model

import numpy as np
import matplotlib.pyplot as plt


class ant_agent(mesa.Agent):
    """Ant agent"""

    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)

        #self.phero = 1

        self.coords = (0,0)


    def move(self):
        step = self.model.grid.get_neighborhood(
            self.coords,
            moore = False,
            include_center=False
        )
        new_step = self.random.choice(step)

        print(f"Ant:{self.unique_id} moving from {self.coords} to {new_step}")
        
        self.model.grid.move_agent(self, new_step)

    def step(self):
        print(self.model.phero)
        

        #print(f"Hi i am a ant number {self.unique_id} and i have {self.phero} pheromones")



class ant_cologne(mesa.Model):

    def __init__(self, num, L, H):

        self.num_agents = num
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(L,H,torus=True)
        self.phero = 0

        for i in range(self.num_agents):
            ant = ant_agent(i,self)
            self.schedule.add(ant)
            coords= (self.random.randrange(0,L),self.random.randrange(0,H))
            ant.coords = coords

            self.grid.place_agent(ant,coords)
        

    

    def step(self):
        ## Add phero into a cell if the cell has an ant
        for cell in self.grid.coord_iter():
            cell_content,x,y = cell
            if len(cell_content)!=0:
                print(f"cell content: {cell_content}\n")
                self.phero = 1*len(cell_content) ## Adding more phero if the cell has more than one ant

        
        self.schedule.step()

# class phero_grid(mesa.Model):

#     def __init__(self, model_cologne:Model):

#         self.grid = mesa.space.MultiGrid(model_cologne.grid.width,model_cologne.grid.height)

#     def step(self):

#         for
        




def print_grid(model):

    agent_counts = np.zeros((model.grid.width, model.grid.height))

    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
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