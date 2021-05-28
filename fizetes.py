
#### A program célja, hogy kiszámítsuk mennyi lesz a havi keresetünk, attól függően, hogy táppénzen voltunk-e vagy sem.

havi_jovedelem = input("Adja meg egy havi teljes jövedelmét (amit kézhet kap) minden juttatással: ")
havi_jovedelem = int(havi_jovedelem)

cafeteria = input("Adja meg ebből mennyi a cafetéria: ")
cafeteria = int(cafeteria)

munkanapok = input("Adja meg hány munkanap volt a hónapban: ")
munkanapok = int(munkanapok)

ledolgozott = input("Ebből hány napon dolgozott: ")
ledolgozott = int(ledolgozott)

szabadnap = input("Kivett szabadnapok: ")
szabadnap = int(szabadnap)




print()
# Egy napi fizetés:

napi_fizetes = (havi_jovedelem - cafeteria) / munkanapok

print("Az adott hónapban egy napi fizetés értéke:", int(napi_fizetes), "forint, cafetéria nélkül.")




# fizetés a hónapban:
print()

havi_fizetes = 0
tappenz = False

if munkanapok == ledolgozott:
    tappenz = False
elif munkanapok > ledolgozott and szabadnap > 0:
    tappenz = False
elif munkanapok > ledolgozott and szabadnap == 0:
    tappenz = True

if tappenz == True:
    cafeteria = 0


havi_fizu = 0
hetven_szazalek = 0


if tappenz == False:
    havi_fizu = (napi_fizetes*munkanapok)+cafeteria
    print("A hónapban nem volt táppénzen, így a havi fizetése:", int(havi_fizu), "forint.")

else:
    hetven_szazalek = munkanapok - ledolgozott

    havi_fizu = napi_fizetes*ledolgozott
    havi_fizu += hetven_szazalek*(napi_fizetes*0.7)

    print("A hónapban", hetven_szazalek, "munkanapot töltött táppénzen.")
    print("A havi fizetése így:", int(havi_fizu), "forint.")






