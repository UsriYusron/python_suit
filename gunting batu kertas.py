import random

print("Gunting-Batu-Kertas")
print("-------------------")

print("1.Gunting")
print("2.Batu")
print("3.kertas")
print("-------------------")

tipe = input("Silahkan pilih: ")

if tipe in ("gunting", "batu", "kertas"):
    choice = ("gunting", "batu", "kertas")
    komputer_random = random.choice(choice)
    print(tipe, "Lawan", komputer_random)
    print("-------------------")
    
    #logic
    if tipe == komputer_random:
        print("seri")
    else:
        if tipe == 'batu':
            if komputer_random == 'gunting':
                print ("menang")
            if komputer_random == 'kertas':
                print ("kalah")
                
        if tipe == 'kertas':
            if komputer_random == 'gunting':
                print ("kalah")
            if komputer_random == 'batu':
                print ("menang")
                
        if tipe == 'gunting':
            if komputer_random == 'batu':
                print ("kalah")
            if komputer_random == 'kertas':
                print ("menang")
    
    