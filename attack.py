# import random
#
#
# playerhp = 260
# enemyatkl = 60
# enemyatkh = 80
#
# while playerhp > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp = playerhp - dmg
#
#     if playerhp <= 30:
#         playerhp = 30
#     else:
#         print("Enemy strikes for", dmg, "points of damage! Current HP is", playerhp)
#
#     if playerhp < 0:
#         print("OVERKILL!")

indítás = str(input("Az I rész indításhoz írja be:.........START I\n"
                    "A II rész indításához írja be:........START II\n"))
if indítás == "START I":
    print("A játék elindult!\n \nI rész: LEGENDA\n")
    print("Szörnyű fejfájással az erdőben ébredsz. Nem tudod hogyan kerültél oda. Ahogy körülnézel minden irányban\n"
          "megtépázott fákat, letört ágakat, vizes füvet, alatta sáros talajt látsz. Lassan sötétedik, valószínüleg\n"
          "átaluttad az egész napot. Az eget felhők borítják és erős szél fúj. Előrelépsz egyet, és csak akkor veszed\n"
          "észre, hogy nincs rajtad cipő, mikor a sáros vízbe lépsz. A távolban egy kunyhó fényeire leszel figyelmes.\n"
          "Elmész a kunyhóhoz, vagy inkább keresel egy rejtekhelyet a fák között éjszakára?\n (Ha a kunyhó felé veszed"
          "az irányt,írd be az 1-es számot. Ha inkább az erdőben probálsz meghúzódni, írd be a 2-es számot.)")
    valasztas1 = str(input("Válasszon: 1 vagy 2\n"))
    if valasztas1 == "1":
        print("Úgy döntöttél hogy a kunyhóban akarsz menedéket keresni magadnak. Ahogyan a sáros csúszós ösvényen\n"
              "sétálsz, rájössz, hogy a kunyhó messzebb van mint hitted. Az idő előrehaladtával egyre sötétebb és\n"
              "hidegebb lesz az erdőben. Séta közben egy patak keresztezi az utadat. Megpróbálod átugrani, és nagy\n"
              "nehezen sikerül is. A talpad a patak túloldalán a sárba csapódik, és valami megzörren a hátadon. Ekkor\n"
              "veszed észre hogy van rajtad egy hátizsák. Folytatod utadat a kunyhó felé, és közben átnézed mi van a\n"
              "táskában. Sajnos csak öt darab pogácsa, és 3 darab aranypénz. Lassan odaérsz a kis épülethez.\n"
              "Megvizsgálod, és többek között észreveszed, hogy az ajtó zárva van, de a mellette lévő ablak résnyire\n"
              "nyitva. Kicsit magasan van, de ha nyújtózkodsz, akkor elérheted. Ahogy körbejársz a ház körül, a\n"
              "a kunyhóból halk szuszogást hallasz. Egyre sötétebb lesz, és mivel már most is nagyon hideg van, és a \n"
              "távolból farkasok hangjára leszel figyelmes, úgy döntesz, muszály bejutod.\n FELOLDVA - hátizsák\n"
              "(Ha dörömbölni kezdesz az ajtón, írd be az 1-es számot. Ha inkább az ablakon próbálsz bejutni, írd be"
              "a 2-es számot.")
        valasztas2 = str(input("Válasszon: 1 vagy 2\n"))
        if valasztas2 == "1":
            print("Úgy döntöttél, dörömbölni kezdesz az ajtón. Egy kis idő elteltével a szuszogás abbamarad, és egy\n"
                  "vénember hangját hallod meg, ahogy ordítani kezd a házban:\n"
                  "  - NA! FRANCKY MIT CSINÁLSZ MÁR MEGINT?! HÁNYSZOR MONDTAM MÁR NEKED?! KI FOGLAK RAKNI!!\n"
                  "Bár eléggé erőszakosan ütlegelted az ajtót, legalább három percen keresztül, felötlik benned, hogy\n"
                  "talán nem hallotta, így ráversz még hármat, négyet az öreg ajtóra.\n"
                  "  - Jólvan már megyek csak ne verje már szét az ajtómat legyen szives!\n"
                  "Az ajtó lassan kinyílik, és egy középmagas, félig kopasz, görnyedt testalkatú bácsikával találod\n"
                  "szemben magad. Mögötte egy nyálgombócra hasomlító kutyafej nézett fel rád érdeklődően. Csak az\n"
                  "volt a furcsa benne, hogy a fej nem az öregember lábánál, nem is a derekánál, Valahol az oldalánál\n"
                  "és ez neked csak akkor tűnt fel, amikor arrébblökte az öregúrt, és nekedrontott. Le is terített,\n"
                  "és ezután a nagy nyálas fejéval elkezdett anyalni. mire a gazdája lesegítete rólad, alig láttál a\n"
                  "nyáltól."
                  "  - Köszönöm! - mondtad, majd bementetek a házba.\n"
                  "Odabennt kellemes meleg fogadott, volt étel és ital, és szétrágott szőnyegdarabok. Összességében\n"
                  "takaros kis kunyhó volt. Az öreg megkínál néhány étellel, majd leül veled szemben, az ágyára.\n"
                  "  - Naés te mit keresel errefelé ilyenkor? - kérdezi az öreg.\n"
                  "  - Hát nem ist tudom... - mondod neki zavartan - Fogalmam sincs, csak az erdőben tértem magamhoz,\n"
                  "    gondolom elaludhattam...\n"
                  "  - Nem épp eszű ember az aki errefelé csak úgy az erddőben elalszik. Főleg nem ebben az\n"
                  "    időszakban... Szerencsés vagy, hogy életben maradtál.\n"
                  "  - Hogy életben maradtam? - kérdezel vissza értetlenül.\n"
                  "  - Nem ide valósi vagy igaz-e?"
                  "  - Nem tudom..."
                  "  - Vezsélyes ez az erdő. A legenda szerint régen sok ember élt itt, egy városkában, az erdő\n"
                  "    kellős közepén. Ám egy nap egy lakos, kinek nevét nem jegyeztem meg, elindult, hogy élelmet\n"
                  "    szerezzen. Csak járta az erdőt, és a fák közül hirtelen egy töpörödött kis sötét alak ugrott\n"
                  "    elő és így szólt: 'Nem mehetsz tovább! Te és a fajtád egy romlott nép vagytok! Eltűrtünk\n"
                  "    titeket éveken át, aztán egyre csak többen jöttetek, elvittétek az élelmünket, leöltétek az\n"
                  "    állatainkat, és mérgező füsttel pusztítotok mindent, ami él! De ennek ma vége lesz! ÉS mi\n"
                  "    fogunk véget vetni nekik, a YANKok, az erdő népe, akik évszázadokon át megbújtunk a sötétben!\n"
                  "    Szólj hát társaidnak ember, mire a nap lemegy, bevonulunk otthonaitokba!' Azzal amilyen\n"
                  "    gyorsan előurott, úgy el is tűnt. Edmund (közben eszembe jutott a neve) hazasietett, de esze\n"
                  "    ágában sem volt figyelmeztetni bárkit is, egyáltalán nem vette komolyan, amit a titokzatos\n"
                  "    lény, a yank mondott. Ám kár volt kételkednie, mert ahogyan az meg lett jósolva, törpék,\n"
                  "    furcsa humanoid növények, entek, manók, egyesek szerint farkasemberek és egyéb mítikus lények\n"
                  "    kezdték ostromolni a várost, nem törődve a lakókkal. De az emberek nem adták könnyen magukat,\n"
                  "    harcba szálltak a yankokkal, és Edmund vezetésével éveken át háborúztak. Mígnem egyszer az\n"
                  "    emberekben felötlött egy új fegyver gondolata. Edmund és néhány harcosa elindultak az erdőbe\n"
                  "    és felkeresték azt a helyet, Ahol a yankok születtek. Ahogy odaértek, varázslatos látvány\n"
                  "    fogadta őket. Egy óriási fa állt egy apró tisztás közepén, egy akkora fa, hogy húsz ember nem\n"
                  "    tudta volna telljesen körbefogni! A közepén egy hatalmas repedés volt látható, amin furcsa\n"
                  "    fény szűrődött át. Itt születtek a yankok, egy ősi varázslatnak hála, melyet az erdő mágusa,\n"
                  "    családjának, és rendjének első tagja, Gilbert rúnák segítségével hozott létre. Edmund ellopta\n"
                  "    a rúnákat, és fekete mágia segítségével a maga uralma alá hajtotta a yankokat. Edmund elméjét\n"
                  "    megfertőzte a varázslat, gonosz tetteket vitt végbe. Többek között örök életre keltette magát\n"
                  "    és három legjobb harcosát. A yankokat lezáratta egy föld alatti üregbe, hogy örök életükre\n"
                  "    ott raboskodjanak. A négy rúnából hármat nekik adott, és elküldte őket, hogy rejtsék\n"
                  "    el és akár az életük árán is védelmezzék a őket. A háború elült, a vér a földbe száradt.\n"
                  "    A négy gonosz honlétéről senki sem tud. De a legenda szerint, ha valaki mind a négy rúnát\n"
                  "    visszajuttatná a fára, a varázslat kiszabadítaná a yankokat, és újra nyugalom, és harmónia\n"
                  "    uralkodhatna az erdőben.\n"
                  "  - Érdekes... Senki sem próbálta még meg eddig?\n"
                  "  - Nem tudok olyanról aki megpróbálta, és túlélte volna... De már jó lenne ha valaki elintézné\n"
                  "    ezt a négy őrültet, mert a gonosz egyre csak terjed, egyre gyorsabban terjed az erdőben...\n"
                  "    De most aludjunk, fáradtnak tűnsz.\n"
                  "  - Rendben aludjunk, tényleg az vagyok...\n"
                  "Lassan nehezen bírsz elaludni, az öreg meséje jár a fejedben. Nem tudhatod, hogy a legendából\n"
                  "mennyi iga, de mi tagadás, te is sétáltál az erdőben, és tudod jól, hogy nyomasztó, még délben\n"
                  "is sötét van. Végre elalszol.\n"
                  "Reggel a FRANCKY nyelvével az arcodon ébredsz. Egész nap az öreggel beszélgetsz, és megismeritek\n"
                  "egymást, összebrátkoztok. Sokáig laksz az öregnél, ezalatt sok mindent eltanulsz tőle. Még mindíg\n"
                  "nem tudod ki voltál, de már egy új ember vagy, edzett, ravasz, okos, és jó ember. Ezt mind az\n"
                  "öregnek köszönheted, de mégis az évek során csak a yankokról kérdezel, már szinte mindent tudsz\n"
                  "róluk. Hogy-hogynem, eldöntöd, hogy újonnan szerzett tudásoddal te leszel a következő, aki\n"
                  "megpróbálja megvalósítani a legenda végét, legyőzni a négy őrzőt, és kiszabadítani a yankokat.\n"
                  "Kicsit izgat téged a gondolat, hogy ez a küldetésed, és megegyezel az öreggel, hogy holnap már\n"
                  "indulsz is.\n"
                  "\n"
                  "VÉGE AZ ELSŐ RÉSZNEK! REMÉLEM ÉLVEZTED A JÁTÉKOT! A MÁSODIK RÉSZ KÖVETKEZIK? KÉREM AZ INDTÁSÁHOZ"
                  "INDÍTSA ÚJRA A PROGRAMOT!")
        if valasztas2 == "2":
            print("Úgy döntöttél, megpróbálsz bemászni az ablakon. NYútózkodsz, és el is éred. Egyik lábaddal\n"
                  "felállsz a szegélyre, és a kezeddel az ablakpárkány felé nyúlsz. Nem számítasz rá, hogy forró\n"
                  "leves van az ablakban. Ahogy megégei a kezedet, elkapod onnan felordítasz, majd hátraesel.\n"
                  "Bevered a fejed, és elájulsz. Halálra fagysz az ajtó előtt.\n MEGHALTÁL, KÖSZÖNÖM HOGY JÁTSZOTTÁL."
                  "ÚJRAKEZDENI A PROGRAM ÚJRAINDÍTÁSÁVAL LEHET.\n")
    if valasztas1 == "2":
        print("Úgy döntesz az erdőben keresel menedéket. Ahogy bojongsz a fák között lassan rájössz, hogy ez nem\n"
              "tartozik a legjobb döntéseid közé. Eltévedtél. Egyre hidegebb lesz, és nem tudod mit kellene tenned.\n"
              "Egy kis idő után arra jutsz, hogy megpróbálsz felmászni egy fára. Már másznál is, amikor a hátad mögül\n"
              " egy falkányi farkas nekedront. A támadás hirtelen ér, nem tudsz mit tenni ellenük. Farkasok vacsorája\n"
              "ként végzed\n MEGHALTÁL, KÖSZÖNÖM HOGY JÁTSZOTTÁL. ÚJRAKEZDENI A PROGRAM ÚJRAINDÍTÁSÁVAL LEHET.\n"
              "ÚJ MÉRFÖLDKŐ - állatkedvelő (Halj meg profi módon az első döntésnél!)\n")
if indítás == "START II":
    print("A játék elindult!\n \nII. rész\n")
if indítás != "START I" or indítás != "START II":
    print("\nEz nincs a lehetőségek között! Kérem indítsa újra a programot.")
