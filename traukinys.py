import vagonas, lokomotyvas

class traukinys:
    name = []
    visa_mase = 0
    sastatas = [None]
    
    def pasirinkti_lokomotyva(self, lokomotyvas):
        self.sastatas[0] = lokomotyvas
        self.visa_mase = self.visa_mase + lokomotyvas.mass
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
        return self.mass
        
    def getStatus(self):
        lok = self.sastatas[0]        
        if lok.pull_m > self.visa_mase :
            return "Traukinys gali vaziuoti"
        else:
            return "Traukinys negali vaziuoti, lokomotyvo maksimali tempiama mase per maza kroviniui % < %" % (lok.pull_m, self.visa_mase)
    ####perkelti i maina ^^^^^########
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
        
    def __add__():
        pass
    
    def __sub__():
        pass
        
    def __bool__():
        lok = self.sastatas[0]        
        if lok.pull_m > self.visa_mase :
            return True
        else:
            return False
    
        