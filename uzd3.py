import sys 
import json
from vagonas import vagonas
from lokomotyvas import lokomotyvas
from traukinys import traukinys
from customExcp import ZeroOrLess, ExistantId

def checkIdInput(text):
    """
    Patikrina ar ID unikalus tarp visu vagonu ir lokomotyvu
    """
    while True:
        try:        
            n = input(text)
            
            if type(n) is not str:
                raise ValueError
            
            for l in l_list:
                if str(l) == n:
                    raise ExistantId  
            
            for v in v_list:
                if str(v) == n:
                    raise ExistantId              
                
            break
        except ValueError:
            print("ID turetu buti sudarytas is raidziu ir skaiciu,",
                  "bei buti validi simboliu eilute")
            
        except ExistantId:    
            print("Sis ID jau naudojamas vagono ar lokomotyvo",
                  ", iveskite kita!")
    return n

def checkInput(text):
    """
    Tikrina ivesti, kad visi vartotojo ivesti duomenys 
    butu sviekieji didesni uz nuli
    """
    while True:
        try:        
            n = input(text)
            n = int(n)
            if n <= 0:
                raise ZeroOrLess
            break
        except ValueError:
            print("Ivestas skaicius nera sveikasis, bandykite dar karta.")
        except ZeroOrLess:    
            print("Ivestas sveikasis skaicius negali buti mazesnis ", 
                  "ar lygus nuliui!")
    return n   

def naujas_traukinys():
    
    t = traukinys(checkIdInput("Iveskite naujo traukinio pavadinima: "))
    return t

def naujas_lokomotyvas():
    a = checkIdInput("Iveskite lokomotyvo identifikacini koda: ")    
    b = checkInput("Iveskite lokomotyvo mase: ")
    c = checkInput("Iveskite maksimalia lokomotyvo traukiama mase: ")
                
    l = lokomotyvas(a, b, c)    
    return l
    
def naujas_vagonas():
    a = checkIdInput("Iveskite vagono identifikacini koda: ")
    b = checkInput("Iveskite vagono savitaja mase: ")
    c = checkInput("Iveskite krovinio mase: ")
    d = checkInput("Iveskite maksimalia krovinio mase: ")
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
        
    print("0 - palikti esama traukini, 1 - ", len(t_list), 
          " pasirinkti is saraso")
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
            print("0 - palikti esama lokomotyva, 1 - ", len(l_list), 
                  " pasirinkti is saraso")
            l_no = int(input()) - 1
            ct = current_train.pasirinktiLokomotyva(l_list[l_no])
            return ct
            
        if a == 2:
            print(v_list)
            print("0 - neprideti ne vieno vagono, 1 - ", len(v_list), 
                  " pasirinkti is saraso")
            v_no = int(input()) - 1
            ct = current_train.pridetiVagona(v_list[v_no])
            return ct
            
        if a == 3:
            sarasas = current_train.getSastatas()
            for i in sarasas[1:]:
                    print("Vagono id: ", i)  
            print("0 - neatimti ne vieno vagono, 1 - ", len(sarasas[1:]), 
                  " pasirinkti is saraso")
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
            
def write_to_file(t_list, v_list, l_list):
    """
    Irasymas i traukiniai.json
    """
    with open('traukiniai.json', 'w') as outfile:
        
        for l in l_list:
            string_list = [str(l) , l.getMass(), l.getPullMass()]
            temp = {"lokomotyvas": string_list}          
            json.dump(temp,  outfile)
            outfile.write("\n")

        for v in v_list:
            string_list = [
                    str(v), 
                    v.getMass(), 
                    v.getLoadMass(), 
                    v.getMaxLoadMass()
                    ]  
            temp = {"vagonas": string_list}     
            json.dump(temp, outfile)
            outfile.write("\n")
                
        for t in t_list:
            train = [str(t)]            
            for el in t.sastatas:            
                train.append(str(el))            
            temp = {"traukinys": train}
            json.dump(temp, outfile)
            outfile.write("\n")
       
def read_from_file():
    """
    Traukiniai.json nuskaitymas
    """
    v_list = []
    l_list = []
    t_list = []
    data = []    
    try:
        with open('traukiniai.json', 'r') as infile:
            for line in infile:
                data.append(json.loads(line))
        
        for item in data:
            for value in item:
                if value == "vagonas":
                    v = vagonas(
                        item[value][0],
                        item[value][1], 
                        item[value][2], 
                        item[value][3]
                        )
                    v_list.append(v)
                if value == "lokomotyvas":
                    l = lokomotyvas(
                        item[value][0], 
                        item[value][1], 
                        item[value][2]
                        )
                    l_list.append(l)
                if value == "traukinys":
                    t = traukinys(item[value][0])
                    
                    for l in l_list:
                        if str(item[value][1]) == str(l):
                            t.pasirinktiLokomotyva(l)
                        
                    for i in range (2, len(item[value])):
                        for v in v_list:
                            if str(v) == str(item[value][i]):
                                t.pridetiVagona(v)
                        
                    t_list.append(t)
    except: print("Failas traukiniai.json nerastas programos aplanke!")
    return t_list, l_list, v_list
            
t_list = []
l_list = []
v_list = []
current_train = None

main_menu_text = [
            "Perziureti traukinius", 
            "Rusiuoti traukinius",
            "Pasirinkti traukini", 
            "Keisti sastata", 
            "Naujas traukinys", 
            "Naujas lokomotyvas", 
            "Naujas vagonas",
            "Ikelti issaugotus",
            "Issaugoti",             
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
            print("Lokomotyvas: ", sarasas[0])
            print("Mase: ", sarasas[0].getPullMass(), " / ", 
                  current_train.getMass())
            
        if len(sarasas) == 1:
            print("Sio traukinio sastatas dar nenustatytas")
        else:
            for i in sarasas[1:]:
                print("Vagono id: ", i)            
        
    print("#----------------------------------------------#")
    for i in range(0, len(main_menu_text)):        
        print(i+1,"---", main_menu_text[i])
    print("#----------------------------------------------#")
    a = int(input("Pasirinkite: "))

    if a == 1:
        perziureti_traukinius()
    
    if a == 2:
        t_list = rusiuoti_traukinius(t_list)
        
    if a == 3:
        current_train = pasirinkti_traukini(current_train)
    
    if a == 4:
        if current_train != None:
            current_train = keisti_sastata(current_train)
        else:
            print("Nepasirinktas traukinys!")
            
    if a == 5:
        t_list.append(naujas_traukinys())
        
    if a == 6:
        l_list.append(naujas_lokomotyvas())
        
    if a == 7:
        v_list.append(naujas_vagonas())
    
    if a == 8:
        t_list, l_list, v_list = read_from_file()
        
    if a == 9:
        write_to_file(t_list, v_list, l_list)
        
    if a == 10:
        sys.exit()
    
    
        