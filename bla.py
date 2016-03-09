global films

def main():
    welcome()
#Testar att lägga till
    
def welcome():
    print "*"*70
    print "Välkommen tiil den bästa filmsamlingen någonsin skådad!"
    print "*"*70
    film_list()
    
def film_list():
    global films
    films = ["The Green Mile", "Star Wars", "Sagan om Ringen", "Snatch", "Lock, Stock and Two Smoking Barrels"]
    print "*"*70
    print "Dessa filmer finns än så länge i samlingen:"
    print "*"*70
    for film in films:
        print film
    print "*"*70
    menu()
    
def updated_films():
    global films
    films = ["The Green Mile", "Star Wars", "Sagan om Ringen", "Snatch", "Lock, Stock and Two Smoking Barrels"]
    for film in films:
        print film
        
def menu():
    print "*"*70
    print "Meny"
    print "*"*70
    print "Du har 4 alternativ att välja på, var god välj en siffra mellan 1-4"
    print "1. Visa filmerna"
    print "2. Lägg till en film"
    print "3. Ta bort en film"
    print "4. Avsluta"
    menu_choice()
    
def menu_choice():
    global films
    choice = raw_input("Ditt menyval: ")
    while choice == "1" or choice == "2" or choice == "3" or choice == "4":
        if choice == "1":
            order_menu()
            for film in films:
                print film
            print "*"*70
            menu_choice()
        elif choice == "2":
            add_film()
            menu_choice()
        elif choice == "3":
            remove_film()
            menu_choice()
        elif choice == "4":
            end()
        break
            
def add_film():
    global films
    films = ["The Green Mile", "Star Wars", "Sagan om Ringen", "Snatch", "Lock, Stock and Two Smoking Barrels"]
    print "*"*70
    print "Lägg till en film i samlingen"
    print "*"*70
    films.append(raw_input("Vilken film vill du lägga till? "))
    for film in films:
        print film
    print "*"*70
    menu()
    
    

def remove_film():
    global films
    films = ["The Green Mile", "Star Wars", "Sagan om Ringen", "Snatch", "Lock, Stock and Two Smoking Barrels"]    
    print "*"*70
    print "Ta bort en film från samlingen"
    print "*"*70
    films.remove(raw_input("Vilken film vill du ta bort? "))
     
    for film in films:
        print film
    print "*"*70
    menu()
    
def end():
    '''
    avslutar programmet och säger hejdå
    '''
    print "*"*70
    print "Tack för din medverkan, nu avslutas programmet!" 

def order_menu():
    print "*"*70
    print "Hur vill du sortera listan?"
    print "1. Kronologisk ordning"
    print "2. Alfabetisk ordning - stigande"
    print "3. Alfabtisk ordning - fallande"
    order_choice()

def order_choice():
    global films
    choice = raw_input("Ditt val: ")
    while choice == "1" or choice == "2" or choice == "3":
        if choice == "1":
            for film in films:
                print film
            print "*"*70
            menu()
        elif choice == "2":
            
            order_choice()
        elif choice == "3":
            order_choice()
        
        break


#kör programmet
main()
