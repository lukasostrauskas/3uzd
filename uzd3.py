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
    l = lokomotyvas
    return l
    
def naujas_vagonas():
    v = vagonas
    return v        
    
def perziureti_traukinius():
    print(t_list)

def pasirinkti_traukini():
    print(t_list) #pakeisti i fora su visais, kad graziau butu
    print("0 - palikti esama traukini, 1 - ", len(t_list), " pasirinkti is saraso")
    t_no = int(input())
    if t_no == 0:
        return 
    else:
        return t_list[t_no-1]
    
def keisti_sastata():
    print("1: Pakeisti lokomotyva")
    print("2: Prideti vagona")
    print("3: Istrinti vagona")
    a = int(input())
    
    if a == 1:
        print(l_list)
        print("0 - palikti esama lokomotyva, 1 - ", len(l_list), " pasirinkti is saraso")
        l_no = int(input())
    
    if a == 2:
        print(v_list)
        print("0 - neprideti ne vieno vagono")
        l_no = int(input())
    
    if a == 3:
        print(v_list)
        print("0 - neatimti ne vieno vagono")
        l_no = int(input())
################# MAIN ##################        
t_list = [None]
l_list = [None]
v_list = [None]

t_list.append(naujas_traukinys())

for i in range(0, 5):
    l_list.append(naujas_lokomotyvas())
    v_list.append(naujas_vagonas())
    print("dedam")
main_menu_text = ["Perziureti traukinius", "Pasirinkti traukini", "Keisti sastata", "Naujas traukinys", "Naujas lokomotyvas", "Naujas vagonas"]
main_menu = {
            1 : perziureti_traukinius,
            2 : pasirinkti_traukini,
            3 : keisti_sastata,
            4 : naujas_traukinys,
            5 : naujas_lokomotyvas,
            6 : naujas_vagonas,
            #7 : issaugoti,      
            #8 : ikelti issaugotus,              
            9 : sys.exit
        }
while True:
    for i in range(0, len(main_menu_text)):        
        print(i+1,"---", main_menu_text[i])

    a = int(input("Pasirinkite: "))

    main_menu[a]()
