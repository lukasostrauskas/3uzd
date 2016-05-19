class vagonas:
    
    self_m          #savita_mase
    load_m           #krovinio_mase
    max_load_m          #max_krovinio_mase
    uid             #unikalus kodas
    
    def __str__(self):
        return self.uid
    
    def __init__(self, no, smass, lmass, mlmass):
        self.uid = no
        self.self_m = smass
        self.load_m = lmass
        self.max_load_m = mlmass
        