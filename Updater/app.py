# Problem koji resava ova skripta je sldeci : Ucitava listu PDF fajlova koji koji se
# nalaze u tekstualnom fajlu listaFajlova.txt. Svaki od fajlova mora biti imenovan u 
# formatu [redni broj]_[naziv fajla].pdf
# Pri interpetiranju skripte, bice ucitani svi fajlovi, ekstrakovani njihovi nazivi
# i bice generisan tekstualni dokument sa ekstenzijom .js koji ce pretstavljati skriptu
# koja ce dinamicki da da popuni index.html dokument sa poslednjim fajlovima koji ce
# biti slobodni za download.


#######################################
#        Updater za DownlaodSection
#######################################

# Ucitavamo fajl listaFajlova.txt. I ukoliko dodje do neuspesnog ucitavanja  izbacujemo
# gresku
try:
    f = open("listaFajlova.txt", "r")
except (IOError):
    print "Error opening file. 'listaFajlova.txt'"
    exit()

# U niz fajlovi sam ucitao sve navedene fajlove (svaki se navodi jedan ispod drugog    
linijeDownload = f.readlines()

# Iterativno prolazim kroz sve fajlove i izvlacim naziv pdf fajla i ime koje ce mu biti prikazano
# u nizove fajlovi i imena

fajlovi = []
imena = []
for i in range(0, len(linijeDownload)):
    fajlovi.append(linijeDownload[i][linijeDownload[i].index('_') + 1 : linijeDownload[i].index('#')])
    imena.append(linijeDownload[i][linijeDownload[i].index('#') + 1: linijeDownload[i].index('.')])

# Otvaramo datoteku loadNewsAndDownloadSection.js za upisivanje i u nju upisujemo
# tagove i uputstva za popunjavanje News i Dowload sekcije na index strani sajta
try:
    g = open("loadNewsAndDownloadSection.js", "w")
except (IOError):
    print "Error opening file 'loadNewsAndDownloadSection.js'."

# Upisujem loadNewsAndDownloadSection.js kod koji ce dinamicki da popuni index.html stranu po njenom ucitavanju sa poslednje
# dodatim fajlovima za download. Ukoliko postoje fajlovi koji su dodati u poslednje 2 nedelje (1209600 sec) tada ce se uz 
# fajl dodati trepcuce "new" pored. Za to su potrebni paketi os i datetime. NAPOMENA: IE ne podrzava blink mogucnost
 
import os, datetime
from time import time

blinkFeature = "<font style = 'color: #FF8C00; padding-left: 100px'>NEW</font>"

g.write("function loadDownloadSection(){\n")

# Dodajem poslednji fajl na vrh sa dodatkom trepcuceg "new!!!" posto je to poslednji dodat fajl
g.write("document.getElementById(\"DownloadSection\").innerHTML = \"<li><a href ='../files/" + fajlovi[len(fajlovi)-1] +".pdf'><img src = 'images/pdf-icon2.png' height='17px' style='margin-left: 5px; margin-top: 3px; margin-right: 10px'></a>" + imena[len(imena)-1] + blinkFeature + "</li>")

# Proveravam vreme kreiranja fajla koji je pretposlednji dodat. Ukoliko je on dodat pre manje od 2 nedelje, uz njega ce da stoji
# dodato trepcuce "new!!!". Vreme kreiranja fajla proveravam preko fje os.path.getmtime('imefajla.pdf')
# link ka referenci -> http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
# trenutno vreme dobijam preko funkcije : time()
# Treba dodati try-except kalusule i napraviti program robusnim. Takodje treba obratiti paznju gde se nalaze
# fajlovi koji su trazeni, kao i na to gde ce program biti instaliran tj sa koje lokacije ce se pokretati

if (time() - os.path.getmtime("files/" + fajlovi[len(fajlovi) - 2] + ".pdf") < 1209600):
    g.write("<li><a href ='../files/" + fajlovi[len(fajlovi)-2] +".pdf'><img src = 'images/pdf-icon2.png' height='17px' style='margin-left: 5px; margin-top: 3px; margin-right: 10px'></a>" + imena[len(imena)-2] + blinkFeature +  "</li>")
else:
    g.write("<li><a href ='../files/" + fajlovi[len(fajlovi)-2] +".pdf'><img src = 'images/pdf-icon2.png' height='17px' style='margin-left: 5px; margin-top: 3px; margin-right: 10px'></a>" + imena[len(imena)-2] + "</li>")

if (time() - os.path.getmtime("files/" + fajlovi[len(fajlovi) - 3] + ".pdf") < 1209600):
    g.write("<li><a href ='../files/" + fajlovi[len(fajlovi)-3] +".pdf'><img src = 'images/pdf-icon2.png' height='17px' style='margin-left: 5px; margin-top: 3px; margin-right: 10px'></a>" + imena[len(imena)-3] + blinkFeature + "</li>\"")
else:
    g.write("<li><a href ='../files/" + fajlovi[len(fajlovi)-3] +".pdf'><img src = 'images/pdf-icon2.png' height='17px' style='margin-left: 5px; margin-top: 3px; margin-right: 10px'></a>" + imena[len(imena)-3] + "</li>\"")

g.write(";\n")
g.write("}\n\n")


# Zatvaram fajlove listaFajlova.txt posto sam uradio sa njim sve sto mi je trebalo
# datoteku g ostavljam otvorenu zato sto cu u nju dodati jos funkciju za ucitavanje News sekcije
f.close()

    
#######################################
#        Updater za NewsSection
#######################################

# Ucitavamo fajl news.txt. I ukoliko dodje do neuspesnog ucitavanja  izbacujemo
# gresku
try:
    h = open("news.txt", "r")
except (IOError):
    print "Error opening file. 'news.txt'"
    exit()
    
# U niz fajlovi sam ucitao sve navedene vesti, navode se jedna ispod druge sa vodecim rednim brojem
# format : [redni broj]_[vest]    
linijeNews = h.readlines()

# Iterativno prolazim kroz sve linije u fajlu i izvlacim vesti i smestam ih u niz vesti
# Izlvacenje se vrsi tako sto izostavljam vodece redne brojeve i donju crtu ispod
vesti = []
for i in range(0, len(linijeNews)):
    vesti.append(linijeNews[i][linijeNews[i].index('_') + 1 : -1])

# U datoteci kreiram funkciju loadNewsSection() koja ce imati komande za dimanicko punjenje stranice index.html
# Bice samo poslednjih 6 vesti ukljuceno!!!

g.write("function loadNewsSection(){\n")

# Ubacujemo poslednjih 6 vesti, prvo posledju pa preostalih 5

for i in range(0,6):
    g.write("document.getElementById(\"NewsSection" + str(i) + "\").innerHTML = \"" + vesti[len(vesti)-(i+1)] + "\";\n")

g.write("}")

h.close()
g.close()