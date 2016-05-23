class lokomotyvas:
    mass = None #mase
    pull_m = None #traukos mase
    
    def __str__(self):
        return self
    
    def __init__(self, mass, pull_m):
        self.mass = mass
        self.pull_m = pull_m