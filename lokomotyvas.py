class lokomotyvas:
    """
    Lokomotyvas - turi savo mase, max tempiama mase, ir unikalu id
    """
    mass = None 
    pull_m = None 
    id = None 
    
    def getMass(self):
        return self.mass
    
    def getPullMass(self):
        return self.pull_m
    
    def __init__(self, id, mass, pull_m):
        self.mass = mass
        self.pull_m = pull_m
        self.id = id
        
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.id