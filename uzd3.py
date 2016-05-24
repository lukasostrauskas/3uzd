from vagonas import vagonas
from lokomotyvas import lokomotyvas
from traukinys import traukinys
import sys

"""
def check_input(int):
    pass
"""    

def naujas_traukinys():
    t = traukinys()
    t = keisti_sastata(t)
    return t

def naujas_lokomotyvas():
    a = int(input("Iveskite lokomotyvo mase: "))
    b = int(input("Iveskite maksimalia lokomotyvo traukiama mase: "))
    c = input("Iveskite lokomotyvo identifikacini koda: ")
    l = lokomotyvas(a, b, c)    
    return l
    
def naujas_vagonas():
    a = input("Iveskite vagono identifikacini koda: ")
    b = int(input("Iveskite vagono savitaja mase: "))
    c = int(input("Iveskite krovinio mase: "))
    d = int(input("Iveskite maksimalia krovinio mase: "))
    v = vagonas(a, b, c, d)
    return v
         
    
def perziureti_traukinius():
    print("#----Traukiniu sarasas-------#")
    for i in t_list:
        print(i)
    print("#----------------------------#")    
    return
    
def pasirinkti_traukini(current_train):  
    for i in range(0, len(t_list)):
        print(i+1, " --- ", t_list[i])
        
    print("0 - palikti esama traukini, 1 - ", len(t_list), " pasirinkti is saraso")
    t_no = int(input())
    if t_no == 0:
        return current_train 
    else:
        current_train = t_list[t_no-1]
        return current_train
    
def keisti_sastata(current_train):
    while True:
        print("0: Grizti")
        print("1: Pakeisti lokomotyva")
        print("2: Prideti vagona")
        print("3: Istrinti vagona")
        a = int(input())
        
        if a == 1:
            print(l_list)
            print("0 - palikti esama lokomotyva, 1 - ", len(l_list), " pasirinkti is saraso")
            l_no = int(input()) - 1
            ct = current_train.pasirinkti_lokomotyva(l_list[l_no])
            return ct
            
        if a == 2:
            print(v_list)
            print("0 - neprideti ne vieno vagono, 1 - ", len(v_list), " pasirinkti is saraso")
            v_no = int(input()) - 1
            ct = current_train.pridetiVagona(v_list[v_no])
            return ct
            
        if a == 3:
            sarasas = current_train.getSastatas()
            for i in sarasas[1:]:
                    print("Vagono id: ", i)  
            print("0 - neatimti ne vieno vagono, 1 - ", len(sarasas[1:]), " pasirinkti is saraso")
            v_no = int(input())
            ct = current_train.atkabintiVagona(v_no)
            return ct
            
        if a > 3:
            print("Ivedete neteisinga pasirinkima")
        
        if a == 0:
            return

def rusiuoti_traukinius(t_list):
    t_list.sort(key=lambda traukinys: traukinys.visa_mase)
    return t_list
            
def write_to_file():
    pass
    
def read_from_file():
    pass
            
################# MAIN ##################        
t_list = []
l_list = []
v_list = []
current_train = None
t_list.append(traukinys("Butaforija"))
######pakeisim i json nuskaityma#########
v_list.append(vagonas(1, 20, 50, 50))
l_list.append(lokomotyvas(20, 100, "1Z"))

main_menu_text = [
            "Perziureti traukinius", 
            "Rusiuoti traukinius",
            "Pasirinkti traukini", 
            "Keisti sastata", 
            "Naujas traukinys", 
            "Naujas lokomotyvas", 
            "Naujas vagonas",
            "Issaugoti ##neveikia", 
            "Ikelti issaugotus ##neveikia",
            "Iseiti"
            ]
                   
while True:
    print("#----------------------------------------------#")
    if current_train == None:
        print("Siuo metu nepasirinktas joks traukinys")     
    else:
        print("Dabartinis traukinys: ", current_train)
        
        sarasas = current_train.getSastatas()
        
        if sarasas[0] == None:
            print("Sis sastatas dar neturi parinkto lokomotyvo")
        else:
            print(current_train.getStatus())
            print("Lokmotyvas: ", sarasas[0])
            
        if len(sarasas) == 1:
            print("Sio traukinio sastatas dar nenustatytas")
        else:
            for i in sarasas[1:]:
                print("Vagono id: ", i)            
        
        ###printinsim viska apie traukini###
    print("#----------------------------------------------#")
    for i in range(0, len(main_menu_text)):        
        print(i+1,"---", main_menu_text[i])
    print("#----------------------------------------------#")
    a = int(input("Pasirinkite: "))
    ####paklausti gal yra geresnis control flow? Ideja: objektai, manageriai. Funkcijos pasiima ka reikia is objektu kurie saugoja duomenis. 
    #<- naudojam dict pasiekt funkcijom, jas kvieciam be parametru.
    if a == 1:
        perziureti_traukinius()
    
    if a == 2:
        t_list = rusiuoti_traukinius(t_list)
        
    if a == 3:
        current_train = pasirinkti_traukini(current_train)
    
    if a == 4:
        current_train = keisti_sastata(current_train)
    
    if a == 5:
        t_list.append(naujas_traukinys())
        
    if a == 6:
        l_list.append(naujas_lokomotyvas())
        
    if a == 7:
        v_list.append(naujas_vagonas())
        
    if a == 9:
        sys.exit()        