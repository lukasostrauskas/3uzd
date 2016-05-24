import vagonas, lokomotyvas

class traukinys:
    name = []
    sastatas = [None]
    
    def pasirinkti_lokomotyva(self, lokomotyvas):
        self.sastatas[0] = lokomotyvas
        return self
        
    def pridetiVagona(self, vagonas):    
        self.sastatas.append(vagonas)
        return self
    
    def atkabintiVagona(self, vagono_nr):    
        self.sastatas.pop(vagono_nr)
        return self
        
    def getSastatas(self):
        return self.sastatas

    def __repr__(self):
        #representation = "<text>"
        """
        representation = self.sastatas[0]
        for i in range (1, len(sastatas)):
            representation.append(" Vagonas nr. ", i, "---", repr(sastatas[i])) 
        """
        return self.name
    
    def __str__(self):
        return self.name
    
    def __init__(self, name):
        self.name = name