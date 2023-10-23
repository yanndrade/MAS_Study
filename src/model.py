from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from agents import *


class World(Model):

    def __init__(self, num, L, H):

        self.num_agents = num
        self.schedule = SimultaneousActivation(self)

        self.grid = MultiGrid(L,H,torus=True)
        #self.phero = 0

        for i in range(self.num_agents):
            ant = Ant(self.next_id(), self)
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