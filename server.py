from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import *
from agents import *
import math



def diffusion_portrayal(agent):
    if agent is None:
        return

    # derived from sugarscape and schelling
    portrayal = {}
    portrayal["Shape"] = "rect"
    portrayal["Filled"] = "true"
    portrayal["Layer"] = 0
    portrayal["w"] = 1
    portrayal["h"] = 1

        # Calculate the amount of red we want

        # Scale this between red and white
        # cite https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code-in-python
    portrayal["Color"] = '#FF0000'

    return portrayal

# dervied from ConwaysGameOfLife
# Make a world that is 50x50, on a 500x500 display.
canvas_element = CanvasGrid(diffusion_portrayal, 50, 50, 500, 500)

# derived from schelling
model_params = {
    "H": 50,
    "L": 50,
    "num": 10    
}

server = ModularServer(
    World, [canvas_element], "Phero", model_params
)