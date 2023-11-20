#!/usr/bin/env python3

from mesa import Agent
from mesa.model import Model

class Ant(Agent):
    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)

    def random_move(self):
        step = self.model.grid.get_neighborhood(
            self.coords,
            moore = False,
            include_center=False
        )
        new_step = self.random.choice(step)
    
        print(f"Ant:{self.unique_id} moving from {self.coords} to {new_step}")
        
        self.model.grid.move_agent(self, new_step)
    
    def step(self):
        pass


class Environment(Agent):
    def __init__(self, unique_id: int, model: Model, pos: tuple) -> None:
        super().__init__(unique_id, model)

        self.pos = pos
        self.amount_phero = 0

    def add_phero(self):
        self.amount_phero += 1

    def get_pos(self):
        return self.pos
    
    def advance(self):
        pass
    
    def step(self):
        self.add_phero()



class ant_agent(Agent):
    """Ant agent"""

    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)

        #self.phero = 1

        self.coords = (0,0)
    
    def drop_phero(self):
        cell_cologne = self.get_item(self.model)
        cell_cologne.add()


    def random_move(self):
        step = self.model.grid.get_neighborhood(
            self.coords,
            moore = False,
            include_center=False
        )
        new_step = self.random.choice(step)

        print(f"Ant:{self.unique_id} moving from {self.coords} to {new_step}")
        
        self.model.grid.move_agent(self, new_step)

    def phero_move(self):
        pass


    def step(self):
        print(self.model.phero)
        self.move
        

        #print(f"Hi i am a ant number {self.unique_id} and i have {self.phero} pheromones")



