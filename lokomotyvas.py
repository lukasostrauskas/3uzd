class lokomotyvas:
    mass = None #mase
    pull_m = None #traukos mase
    id = None #id
    
    def get_pull_m(self):
        return self.pull_m
    
    def __init__(self, mass, pull_m, id):
        self.mass = mass
        self.pull_m = pull_m
        self.id = id
        
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.id
        
        
        