class vagonas:
    self_m = None         #savita_mase
    load_m = None          #krovinio_mase
    max_load_m = None         #max_krovinio_mase
    uid = None            #unikalus kodas
    
    def __str__(self):
        return str(self.uid)
        
    def __repr__(self):
        
        return str(self.uid)
    
    def __init__(self, no, smass, lmass, mlmass):
        self.uid = no
        self.self_m = smass
        self.load_m = lmass
        self.max_load_m = mlmass
        