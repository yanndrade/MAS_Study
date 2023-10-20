#!/usr/bin/env python3

import mesa
from mesa.model import Model


class ant_agent(mesa.Agent):
    """Ant agent"""

    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)

        self.phero = 1

    def step(self):
        print(f"Hi i am a ant number {self.unique_id} and i have {self.phero} pheromones")



class ant_cologne(mesa.Model):

    def __init__(self, num):

        self.num_agents = num
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(self.num_agents):
            ant = ant_agent(i,self)
            self.schedule.add(ant)

    def step(self):
        self.schedule.step()


        