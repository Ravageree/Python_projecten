import random

def roulette():
    global chips
    inputs = []
    roulette_optellen = 0

    # Het aantal chips van de speler tonen
    print(f"Je hebt {chips} chips!")
    print("Op welke nummers wil je inzetten? (zeg 'stop' als je wilt stoppen)")

    # De speler laten inzetten totdat 5 inzetten zijn gedaan of als de speler 'stop' zegt
    while roulette_optellen < 5 and chips > 0:
        roulette_input = input(f"Inzet {roulette_optellen + 1}: ")
        
        # Stoppen als de speler 'stop' zegt
        if roulette_input.lower() == "stop":
            break
        
        try:
            # Veronderstel dat de speler een getal tussen 1 en 36 invoert
            invoer = int(roulette_input)
            if 1 <= invoer <= 36:
                inputs.append(invoer)
                chips -= 1 
                roulette_optellen += 1 
            else:
                print("Kies een nummer tussen 1 en 36.")
        except ValueError:
            print("Ongeldige invoer. Kies een nummer of zeg 'stop'.")
    
    # De uitkomst van de roulette bepalen
    winnende_getal = random.randint(1, 36)

    # Controleren of de speler heeft gewonnen
    if winnende_getal in inputs:
        winst = inputs.count(winnende_getal) * 35
        chips += winst
        print(f"Gefeliciteerd! Het winnende nummer is {winnende_getal}. Je hebt {winst} chips gewonnen.")
    else:
        print(f"Helaas! Het winnende nummer is {winnende_getal}. Geen winst deze ronde.")
    
    print(f"Je hebt nu {chips} chips.\n")

def start_spel():
    global chips
    chips = 10 

    while chips > 0:
        roulette()

        # Vragen of de speler door wil gaan na elke ronde
        doorgaan = input("Wil je een nieuwe ronde spelen? (Y/N): ").lower()
        if doorgaan == 'n':
            print("Dankjewel voor het spelen! Tot de volgende keer.")
            break

    # Als de chips op zijn, het einde van het spel afhandelen
    if chips == 0:
        print("GAME OVER")
    elif chips < 0:
        print(f"Je hebt een schuld van {chips} chips.")
        betalen = input("Hoe wil je betalen? (pin/cash): ").lower()

        if betalen == "pin":
            input("Vul hier je bankinformatie in: ")
        elif betalen == "cash":
            print("Ga naar de eerste beste kassa om je schuld in te lossen.")
        else:
            print("Ongeldige betalingsoptie.")

# Het spel starten
start_spel()
