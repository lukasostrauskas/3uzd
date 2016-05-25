class vagonas:
    """
    Vagonas turi savo mase, krovinio mase, maksimalia krovinio mase
    ir unikalu identifikacini numeri
    """
    self_m = None         
    load_m = None          
    max_load_m = None         
    uid = None            
    
    
    def getMass(self):
        return self.self_m
        
    def getLoadMass(self):
        return self.load_m
        
    def getMaxLoadMass(self):
        return self.max_load_m
    
    def getId(self):
        return uid
    
    def __str__(self):
        return str(self.uid)
        
    def __repr__(self):
        
        return str(self.uid)
    
    def __init__(self, no, smass, lmass, mlmass):
        self.uid = no
        self.self_m = smass
        self.load_m = lmass
        self.max_load_m = mlmass
        