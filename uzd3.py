from vagonas import vagonas
from lokomotyvas import lokomotyvas
from traukinys import traukinys
import sys

"""
def check_input(int):
    pass
"""    

def naujas_traukinys():
    t = traukinys
    return t

def naujas_lokomotyvas():
    a = int(input("Iveskite lokomotyvo mase: "))
    b = int(input("Iveskite maksimalia lokomotyvo traukiama mase: "))
    c = input("Iveskite lokomotyvo identifikacini koda: ")
    l = lokomotyvas(a, b, c)
    l_list.append(l)
    return
    
def naujas_vagonas():
    v = vagonas
    v_list.append(v)
    return        
    
def perziureti_traukinius(current_train):
    print("#----Traukiniu sarasas-------#")
    for i in t_list:
        print(i)
    print("#----------------------------#")    
    return current_train
    
def pasirinkti_traukini(current_train):
    #pakeisti i fora su visais, kad graziau butu
    
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
        print("0 - neatimti ne vieno vagono, 1 - ", len(v_list), " pasirinkti is saraso")
        v_no = int(input())
        ct = current_train.atkabintiVagona(v_no)
        return ct
    return ct
        
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
            "Pasirinkti traukini", 
            "Keisti sastata", 
            "Naujas traukinys", 
            "Naujas lokomotyvas", 
            "Naujas vagonas",
            "Issaugoti ##neveikia", 
            "Ikelti issaugotus ##neveikia",
            "Iseiti"
            ]
            
main_menu = {
            1 : perziureti_traukinius,
            2 : pasirinkti_traukini,
            3 : keisti_sastata,
            4 : naujas_traukinys,
            5 : naujas_lokomotyvas, # veliau CRUDas?
            6 : naujas_vagonas, # veliau CRUDas?
            #7 : issaugoti,      
            #8 : ikelti issaugotus,              
            9 : sys.exit
        }
        
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
            print("Lokmotyvas, ", sarasas[0])
            
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

    current_train = main_menu[a](current_train) 