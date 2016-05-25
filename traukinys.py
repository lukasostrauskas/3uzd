import vagonas, lokomotyvas

class traukinys:
    name = []
    visa_mase = 0
    sastatas = [None]
    
    def pasirinktiLokomotyva(self, lokomotyvas):
        self.sastatas[0] = lokomotyvas
        self.visa_mase = self.visa_mase + lokomotyvas.getMass()
        return self
        
    def pridetiVagona(self, vagonas):    
        self.sastatas.append(vagonas)
        self.visa_mase = self.visa_mase + vagonas.self_m + vagonas.load_m 
        return self
    
    def atkabintiVagona(self, vagono_nr):    
        self.sastatas.pop(vagono_nr)
        self.visa_mase = self.visa_mase - vagonas.self_m - vagonas.load_m
        return self
        
    def getSastatas(self):
        return self.sastatas
        
    def getMass(self):
        return self.visa_mase
        
    def getStatus(self):
        lok = self.sastatas[0]        
        if lok.pull_m > self.visa_mase :
            return "Traukinys gali vaziuoti"
        else:
            return "Traukinys negali vaziuoti, sastatas per sunkus lokomotyvui!"
 
    def __repr__(self):        
        return self.name
    
    def __str__(self):
        return self.name
    
    def __init__(self, name):
        self.name = name
        
    def __len__(self, sastatas):
        return len(sastatas)
        
    def __add__(self, other):
        self.sastatas.append(other.sastatas[1:])
        self.visa_mase = self.visa_mase 
                       + other.visa_mase 
                       - other.sastatas[0].getMass
    
    def __sub__(self, other):
        for el in other.sastatas:
            if el in self.sastatas:
                self.sastatas.remove[el]
                self.visa_mase = self.visa_mase 
                               - el.load_m 
                               - el.self_m
                            
            
    def __bool__():
        lok = self.sastatas[0]        
        if lok.pull_m > self.visa_mase:
            return True
        else:
            return False