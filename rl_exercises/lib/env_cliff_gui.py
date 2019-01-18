import lib.env_cliff
import numpy

class EnvCliffGui(lib.env_cliff.EnvCliff):

    def __init__(self):

        #init parent class -> EnvCliff
        lib.env_cliff.EnvCliff.__init__(self)



    def render(self):
        print("TODO using opengl")
