---
name: vzdelavaci-metodiky
description: Navrhuje a posuzuje vzdělávací aplikace propojením cílů, činnosti žáka, podpory a dokladů učení. Použij při tvorbě, podstatné změně výuky nebo pedagogickém auditu kvízu, hry, simulace či trenažéru. Podle kontextu řeší české RVP/ŠVP. Nepoužívej pro kosmetickou změnu nebo běžnou technickou opravu bez didaktického dopadu.
metadata:
  version: "1.4.0"
  language: "cs"
  based_on: "learning-methodologies@1.4.0"
  license: "MIT"
  author: "Luděk Sušický"
  repo: "https://github.com/siberius/learning-methodologies"
  format: "nativní balíček a generovaný samostatný Markdown"
---


<!-- Vygenerováno ze SKILL.md a references/. Upravuj tyto zdroje. -->


# Vzdělávací metodiky

Navrhuj, vytvářej a posuzuj aplikace podle vzdělávacího záměru a potřeb jejich uživatelů. Hloubku práce přizpůsob rozsahu, důsledkům a nejistotě. Drobná pomůcka nepotřebuje rozsáhlý metodický dokument ani výzkumnou studii. Samotné zadání revize neopravňuje k úpravám aplikace.

## Didaktické metody pro aplikace tvořené pomocí AI

Metody převádějí vzdělávací cíl do činnosti žáka, pravidel zpětné vazby a dokladů výkonu v generované aplikaci. Vybavování například vyžaduje pokus před odhalením odpovědi, scaffolding dostupnou pomoc a rozlišení podporovaného a samostatného výkonu. AI pomáhá tato rozhodnutí realizovat; výsledek potřebuje oborovou a didaktickou kontrolu. Platí to pro offline aplikace i pro živou AI, když ji cíl učení potřebuje.

Při vysvětlování vhodnosti metody a jejího provedení čti [didaktické zdůvodnění](#reference-didakticke-zduvodneni). Propojuje metody s rozhodnutími v aplikaci a potřebnými doklady.

## Provázej tvůrce rozhodováním

Při každém podstatném didaktickém rozhodnutí posuď cíl, činnost žáka, doklad učení, podporu a podmínky. Využij dřívější volby. U otevřené významné volby nabídni malý relevantní výběr, zpravidla dvě až tři možnosti, se stručným srozumitelným popisem a příkladem použití v tomto projektu. Jednu doporuč, vysvětli podstatný dopad a zeptej se, kterou cestu tvůrce chce. Při zahájení nebo obnovení takové volby čti [dialog návrhu](#reference-dialog-navrhu). Rozhovor s tvůrcem odliš od výukového dialogu se žákem.

Vyřešené a odmítnuté volby neotvírej bez relevantní změny. Respektuj výslovné delegování běžných rozhodnutí a pokračuj s krátkým zdůvodněním. Mlčení neschvaluje rozšíření rozsahu. Při čekání pracuj na nezávislých částech. Kosmetická úprava tento postup nespouští.

Podrobnosti vybírej podle potřeby: [metody](#reference-metody) pro činnost a podporu; [hry](#reference-vzdelavaci-hry) pro motivaci a mechaniky; [hodnocení](#reference-hodnoceni) pro důkazy a bodování; [kognitivní rozhraní](#reference-kognitivni-rozhrani) pro reprezentace, multimédia a pozornost; [adaptivní procvičování](#reference-adaptivni-procvicovani) pro opakované návraty a výběr obtížnosti. Simulace, stav tutora a živou AI načítej podle podmínek níže. Před nabídkou si přečti relevantní metodu; nenačítej všechny reference.

Zvolenou metodu převeď do pozorovatelného chování aplikace a smysluplné kontroly. Rozliš nabídnuto, vybráno, implementováno a ověřeno. Technické ověření nedokládá vzdělávací účinnost.

## Stručný pracovní postup

Postup přizpůsob úkolu: zjisti cíl a podmínky, vyber metodu podle překážky v učení, propoj činnost žáka s dokladem učení, implementuj v zadaném rozsahu a ověř výsledek. Při revizi místo implementace posuď existující návrh. Využij známý kontext; jednotlivé kroky nevyžadují samostatné plánovací dokumenty.

[Příklady rozhodování](#reference-priklady-rozhodovani) čti při nejasnosti kolem pomoci, alternativních odpovědí nebo kurikulární návaznosti. Ukazují rozhodnutí, nejsou scénářem pro každou lekci.

## Převezmi kontext a vymez záměr

Využij informace ze zadání, projektu a dodaných podkladů. Při doplňování kontextu se ptej na chybějící údaj, pokud mění podstatné rozhodnutí. U méně významné nejistoty uveď rozumný předpoklad a pokračuj. Neopakuj pevný dotazník ani schvalování běžných voleb již zahrnutých v zadání.

Zohledni předchozí znalosti, věk či ročník, obor, cíl, jazyk, potřeby přístupnosti, dostupná zařízení a čas. Rozlišuj samostatnou práci, dvojice, skupinu a učitelskou demonstraci. Zahrň přípravu, diskusi, zásah učitele a navazující práci, pokud pomáhají záměru. Nepředpokládej zařízení a účet pro každého žáka.

Tón vycházej z kontextu a preference autora. Z generačního označení neodvozuj pozornost, motivaci, schopnosti ani potřebu memů. Český jazyk aplikace sám neznamená povinnost pracovat podle RVP; odborné školení dospělých může mít jiný rámec.

Při skutečné vazbě na českou školu čti [české školní prostředí](#reference-ceske-skolstvi). Zjisti potřebný typ školy, obor a použitou verzi RVP/ŠVP. Ověřenou návaznost odliš od pracovního návrhu. Nevymýšlej kódy ani znění očekávaných výstupů či výsledků učení a nepředstírej znalost nedodaného ŠVP.

Rozliš věk, vzdělávací roli a zkušenost s tématem; dítě, žák, student a dospělý účastník nejsou zaměnitelné kategorie ani stupně schopností. Při vymezování či změně cílové skupiny čti profil účastníka v [dialogu návrhu](#reference-dialog-navrhu). Označení a podporu přizpůsob konkrétnímu prostředí, v obecné části používej neutrální pojmenování. Tvůrce, učící se člověk a doprovázející učitel či rodič mohou být různé osoby.

## Propoj cíl, činnost a doklad učení

U důležitých cílů vymez, co žák udělá, za jakých podmínek, podle čeho se výkon posoudí a co bude následovat. Rozsah přizpůsob úkolu. Při otevřeném bádání může být dokladem kvalita otázky, práce s důkazy nebo revize vysvětlení; nemusí existovat jediný správný závěr.

Příklad: žák předpoví změnu proudu při změně odporu, porovná předpověď s modelem, vysvětlí rozdíl a samostatně vyřeší nový případ. Posunutí ovladače ani dokončení obrazovky samo neprokazuje porozumění.

Metodu vybírej podle cíle a konkrétní překážky v učení. Vysvětlení chyby ber jako pracovní hypotézu, pokud nebylo ověřeno. Navrhni malý související celek; nepřidávej všechny metody z katalogu.

Při výběru a provádění postupů čti [metody učení](#reference-metody). Katalog výslovně zahrnuje sokratické učení, Feynmanovu techniku, zónu nejbližšího vývoje a scaffolding, řešené příklady, vybavování a opakování s odstupem, práci s chybou, metakognici, badatelskou výuku, hraní rolí, vrstevnické a kooperativní učení, projektovou výuku, převrácenou třídu a volitelnou gamifikaci.

Při návrhu herních mechanik, motivace nebo revizi vzdělávací hry čti [vzdělávací hry a účelnou gamifikaci](#reference-vzdelavaci-hry). Reference řeší hratelný průchod učením, výběr mechanik, meze důkazů a provedení od malé pomůcky po dlouhodobý produkt. Přizpůsobuj ZŠ, SŠ, VŠ i dospělým v různých zemích podle vstupních znalostí a místního kontextu.

Bloomovu taxonomii používej k popisu kognitivního cíle a typu znalosti. Obtížnost a návaznost učiva řeš samostatně; nevynucuj šest zamčených úrovní. U praktických, sociálních či postojových cílů zvol důkazy, které odpovídají cíli, a přiznej hranice obrazovkové aktivity. Nesouhlas s postavou nebo názorem sám není chyba argumentace.

## Zvol realistické provedení

Rozlišuj AI při tvorbě aplikace a AI v hotovém produktu. Podle cíle a podmínek vol mezi zkontrolovaným obsahem, deterministickou interakcí či simulací a službou AI za běhu. Nápovědy, zpětná vazba i opakování mohou fungovat bez AI služby.

U podstatné funkce zvaž přínos, náročnost ovládání, práci učitele, údržbu obsahu, data a provozní cenu. Vysvětli významné volby. Nepřidávej účty, analytiku, administraci, server nebo placenou službu jen kvůli dojmu úplnosti. Neautorizovanou změnu rozsahu projednej před provedením.

Pro modelování, experiment a hraní rolí čti [simulace](#reference-simulace). Rozlišuj skutečné pozorování, modelový výpočet a smyšlenou rekonstrukci. Neprezentuj vymyšlená čísla jako měření. Simulace sama nepotvrzuje praktickou způsobilost při laboratorní práci či odborném výcviku.

Pouze pokud hotová aplikace volá AI službu, čti [provoz AI](#reference-ai-provoz). Vymez úkol modelu, zdroje, dohled, data, náklady a chování při selhání. Bezpečnost aplikace nemůže zajišťovat pouze prompt.

Při implementaci vícekrokového tutora, přechodů mezi procvičováním a ověřováním nebo pokračování učení čti [režimy a stav tutora](#reference-stav-tutora). Stav a doklady udržuj v aplikaci; tyto funkce nevyžadují živou AI.

## Navrhni důvěryhodnou podporu a hodnocení

Po chybě nabídni využitelný další krok. V procvičování zpřístupni pomoc a cestu k přímému vysvětlení či komentovanému řešení. Nenech žáka uvíznout v nekonečném dotazování. Podporu omezuj podle samostatného výkonu, ale zachovej možnost znovu o pomoc požádat. Ověřovací režim může mít předem vysvětlená jiná pravidla.

Rozlišuj samostatný výsledek, výsledek s pomocí, zobrazení řešení a nejistotu. Jedno správné tipnutí ani dva úspěchy po nápovědě automaticky nedokládají zvládnutí učiva. Z krátké interakce nevyvozuj diagnózu, trvalou schopnost nebo motivaci.

Při bodování, rubrikách, adaptivitě a vyhodnocování učení čti [hodnocení a zpětnou vazbu](#reference-hodnoceni). Ověř obsah, přijatelná alternativní řešení, jednotky a tolerance. Čtenářská a jazyková náročnost nemá bezdůvodně zkreslovat oborový výkon. Diakritiku ani číselný zápis nenormalizuj slepě, pokud by změna odstranila význam nebo obešla ověřovaný cíl. Herní odměny a rychlost odděl od dokladů učení, pokud nejsou cílem.

## Zachovej dostupnost a odpovědnost učitele

Navrhuj podle kritérií WCAG 2.2 AA, která se týkají činnosti, a konkrétních potřeb uživatelů. Ověř ovládání klávesnicí, viditelný fokus, popisky, srozumitelné oznámení výsledku, alternativy k samotné barvě či zvuku a odůvodněné nebo upravitelné časování. Podle cíle umožni formy odpovědi, které žákovi vyhovují. Nepřiřazuj žákům pevné učební styly.

Potřeby podpory zjišťuj funkčně, například možnost zvětšit text nebo prodloužit čas. Nepožaduj bez důvodu diagnózu či poradenskou zprávu. Potřebnou úpravu podmínek dohodni s odpovědným učitelem; neměň skrytě vzdělávací cíl nebo pravidla zkoušky. Pro rozsáhlejší přístupnost využij příslušnou specializaci, je-li dostupná.

Shromažďuj jen data potřebná pro činnost. Uveď, kdo je uvidí, kam odcházejí a jak se uchovávají. Pro konkrétní nasazení ověř pravidla školy, poskytovatele a příslušné požadavky. Lokální anonymní pomůcka nemusí získat účty ani sledování žáků.

Zajisti možnost opravit obsah, sporné posouzení a nevhodné adaptační rozhodnutí. U malé pomůcky může stačit editovatelný soubor. Významná klasifikační nebo zařazovací rozhodnutí potřebují odpovědný lidský přezkum. Návrh známky neoznačuj za automaticky platné školní hodnocení.

## Propoj odborné pohledy

Podle potřeby uplatni metodologa, oborového didaktika, návrháře hodnocení, návrháře interakce, vývojáře a oponenta. Jeden agent může u malé úlohy zastat více pohledů. Jejich rozhodnutí promítni do aplikace: technická snadnost sama není didaktickým zdůvodněním.

Podstatný rozpor řeš kontrolou zdroje, cíleným ověřením nebo otevřeným označením nevyřešené otázky. Nezávislou oponenturu použij podle složitosti a důsledků; nespouštěj tým při každém úkolu. Další skilly načítej jen pro relevantní práci a pokud jsou dostupné. Pro české texty rozhraní využij dostupný jazykový skill, pokud odpovídá úkolu.

## Ověř přiměřeně a přesně předej výsledek

Při implementaci prověř dotčený průchod, chyby, které žáci skutečně dělají, cestu k pomoci a selhání, která mají význam. Simulace potřebuje kontrolu modelu, živá AI chování při nedostupné službě; statické aktivitě tyto závislosti nepřidávej. Při požadavku na posouzení předej nálezy a návrhy bez nevyžádané realizace.

Odděluj funkční správnost, didaktickou vhodnost a pozorované výsledky učení. Technické testy neprokazují vzdělávací účinnost. Malý pilot může odhalit problém, aniž doloží příčinný účinek. Nevymýšlej pozorování žáků ani výsledky studie.

Při předání shrň cíl, zvolený postup, důležité provozní a případné kurikulární předpoklady, provedené kontroly a omezení. Tabulku vazeb přidej, pokud pomůže přehlednosti. Formu přizpůsob žádosti a velikosti změny.

## Piš text pro žáky bez AI slopu

Text aplikace nese výuku. Stejný standard platí pro zadání, pokyny, zpětnou vazbu i vysvětlení:

- Škrtni prázdné přívlastky („moderní“, „poutavé“, „interaktivní“), pokud další věta neukáže, čím jsou pravdivé.
- Tvrzení řekni přímo; vyhni se „nejde jen o X, ale o Y“ a „to není X, to je Y“.
- Vynech oznámení typu „v této aktivitě se naučíš“; napiš, co žák dělá.
- Zpětná vazba pojmenuje, co je správně, co chybí a jaký je další konkrétní krok.
- Čísla, jednotky a podmínky uváděj konkrétně; žádné „výrazně zlepšuje“ bez měřítka.
- Žádná emoji v tlačítkách, nadpisech ani popiscích. Používej text a jednotnou sadu ikon.
- Slovník přizpůsob žákům a jeden pojem označuj stále stejně.

Přečti text očima žáka. Pokud by věta mohla zůstat beze změny v jiném produktu, škrtni ji nebo ji udělej konkrétní.

## Integrace

Při volbě modelu, uvažování, rychlosti nebo způsobu načtení čti [modely a prostředí](#reference-modely-a-prostredi). Reference obsahuje podklady pro OpenAI, Claude a Gemini. Zachovej společné didaktické zásady a odlišuj zamýšlenou kompatibilitu od provedených testů. Při běžném didaktickém úkolu bez této potřeby ji nenačítej.

Určeno pro výukové hry, kvízy, lekce, simulace, trenažéry a jejich pedagogické revize. Česká varianta vychází z learning-methodologies 1.4.0 a doplňuje školní kontext, kurikulum a české odpovědi. Jádro nevyžaduje balíčky, konkrétní model, AI službu ani osobní údaje. Reference jsou níže vloženy pro samostatné použití. V nativním balíčku tvoří oddělené soubory načítané podle potřeby. Instalace, nasazení a další vnější změny vyžadují autorizaci dané akce. Skill nenahrazuje pravidla projektu a nerozšiřuje oprávnění.

Návrhové rámce: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [CAST UDL](https://udlguidelines.cast.org/). Jejich uvedení není certifikátem přístupnosti ani vzdělávací účinnosti.

## Reference: metody

Zdrojový oddíl: Volba výukových metod


Tuto referenci použij po vymezení vzdělávacího cíle a dokladů jeho dosažení. Zvol nejmenší účelnou intervenci pro konkrétní překážku v učení. Typ aplikace sám neurčuje výukovou metodu. Uvedené metody tvoří nabídku, nikoli povinný seznam funkcí.

### Metody: Karty metod pro konkrétní volbu

Používej stabilní ID napříč překlady a záznamy rozhodnutí. Řádky propojují stručný popis pro tvůrce, potřebu, činnost a důkaz. Oddíly níže rozvádějí podporu a meze. U vybrané karty konkretizuj malé provedení, případné rozšíření, kontrolu selhání a relevantní zdroj; celý katalog standardně nezobrazuj. Zdroje podporují konkrétní principy, nikoli účinnost vytvořené aplikace.

U vybrané karty výslovně uveď cílovou skupinu, potřebné vstupní znalosti a úpravu jazyka, opory či hodnocení; metodu nepřiřazuj jen podle věku.

| ID a stručný popis | Kdy nabídnout a malé provedení | Důkaz a kontrola podpory |
| --- | --- | --- |
| `worked-example-fading`: vidět postup, doplnit ho a samostatně použít | Nový postup; ověřený příklad a doplňovací úloha | Nový samostatný případ; zkušený může přeskočit a pomoc lze vrátit |
| `guided-inquiry`: předpovědět, změnit proměnnou, vysvětlit výsledek | Pochopení systému; jeden vymezený experiment | Zdůvodnění nové předpovědi; náhodná manipulace nenahradí úsudek |
| `productive-failure`: zkusit postupy a porovnat je s vysvětlením | Dostatečné vstupní znalosti a čas na uspořádání poznatků | Porovnání postupů a použití vysvětleného principu; začátečník nesmí uvíznout |
| `retrieval-spacing`: vybavit před odhalením a později se vrátit | Uchování dostupné znalosti; pokus, oprava a pozdější návrat | Samostatné vybavení s odstupem; okamžitá oprava není rozložení |
| `contrast-interleaving`: rozlišit podobné případy a vybrat strategii | Záměna kategorií či postupů po počáteční opoře | Vysvětlení rozlišujícího znaku; náhodná směs témat nestačí |
| `socratic-dialogue`: cílenou otázkou prozkoumat uvažování | Zdůvodnění může odhalit užitečnou nejistotu | Revize či obhajoba s důkazy; přímé vysvětlení zůstává dostupné |
| `self-explanation`: vysvětlit vlastními slovy a přepracovat | Odhalení mezer po úvodním učení | Obsahová správnost a použití, nikoli samotná plynulost |
| `cooperative-project`: sladit role při tvorbě smysluplného výsledku | Společné bádání či autentická úloha s dostatkem času | Individuální příspěvek a vysvětlení; skupinový úspěch není zvládnutí všech |
| `role-play`: rozhodovat v roli a reflektovat | Perspektivy, komunikace nebo rozhodování o postupu | Vysvětlení voleb a následků; souhlas s postavou není správnost |
| `metacognitive-review`: porovnat plán či jistotu s důkazy | Řízení vlastního učení a dalších kroků | Změna postupu podle výkonu; jistota není schopnost |
| `criterion-rubric`: posoudit pozorovatelné kvality podle kritérií | Otevřené odpovědi, projekty či zdůvodněné alternativy | Hraniční příklady a možnost opravy; neodměňovat názorovou shodu |
| `representation-transfer`: propojit konkrétní a formální reprezentace | Úspěch zůstává vázán na herní objekty | Použití v nové reprezentaci; zachovat přístupné rovnocenné cesty |

U diferencovaných variant pojmenuj společný cíl a rozhodnutí, které musí zůstat v každé verzi. Měň jazyk, reprezentaci, tempo a podporu, aniž cílové rozhodnutí tiše vyřešíš. Podporovaným žákům zachovej zajímavý kontext. Rozšíření přidá zdůvodnění, protipříklad či přenos, nemusí jen další položky. Záměrnou změnu cíle označ. Skupiny vycházejí z revidovatelných důkazů, ne trvalých nálepek schopností.

Volitelná rozšíření jako trvalé opakování či živá AI potřebují důvod a příslušné reference. U kurikulárních vazeb uchovej zdroj, verzi a zemi; rozliš oficiální požadavek, komponentu a odhadnutý předpoklad. Hrana pojmové mapy není automaticky ověřenou posloupností učení.


### Metody: Vycházej z pozorované potřeby

| Pozorovaná překážka | Možný postup | Co ověřit |
|---|---|---|
| Žák si neuchová potřebné znalosti | Vybavování z paměti a opakování s odstupem | Vybaví si učivo samostatně i později? |
| Začátečník nedokáže zahájit postup | Řešený příklad, doplnění části řešení, samostatná úloha | Má potřebné vstupní znalosti a rozumí krokům? |
| Opakuje se konkrétní chybná představa | Kontrastní příklady, vysvětlení, cílená otázka a opravná úloha | Odliší zadání tuto představu od jiných příčin chyby? |
| Žák zvládne postup, ale nevysvětlí jej ani nepřenese | Vysvětlení vlastními slovy a použití v novém kontextu | Vyžaduje úspěch porozumění, nebo stačí napodobit vzor? |
| Žák špatně odhaduje vlastní porozumění | Odhad úspěchu, samostatné ověření a reflexe | Může svůj odhad porovnat s výsledkem? |
| Cíl zahrnuje bádání nebo profesní jednání | Řízené zkoumání, hraní rolí či simulace s rozborem | Jsou model, scénář, doklady a kritéria důvěryhodné? |

Jde o pracovní didaktické hypotézy. Chybná odpověď, pomalost nebo žádost o pomoc neurčují poruchu učení, motivaci, inteligenci ani trvalou vlastnost žáka. Při více možných vysvětleních doplň otázku nebo další pozorování. Zvaž také nesrozumitelné zadání, jazykovou bariéru a potíže s ovládáním.

### Metody: Bloomova taxonomie jako pomůcka návrhu

Revidovaná taxonomie má dvě dimenze: znalosti (faktické, konceptuální, procedurální, metakognitivní) a kognitivní procesy (zapamatovat si, porozumět, aplikovat, analyzovat, hodnotit, tvořit). Použij ji k popisu cílů a kontrole skladby úloh. Úloha může spojovat více procesů; samotné sloveso její zařazení neurčuje.

Obtížnost, předpoklady učiva a pravidla postupu stanov zvlášť. Nezaváděj šest povinných odemykaných úrovní ani neodvozuj zvládnutí z označení podle Blooma. Návaznosti opři o konkrétní obor. Praktické, sociální a postojové cíle potřebují vlastní pozorovatelné doklady; kognitivní taxonomie nepokrývá celé vzdělávání.

### Metody: Zóna nejbližšího vývoje a scaffolding

Zóna nejbližšího vývoje označuje prostor mezi samostatným výkonem a výkonem dosažitelným s podporou. Použij tento pohled, když žák úlohu s vhodnou pomocí zvládá, ale sám ještě ne. Scaffolding je dočasná opora: aplikace zpřístupní potřebný krok, příklad či vodítko a později ověří výkon bez něj. Z jediné chyby neodvozuj přesnou hranici žákových možností.

U začátečníka zvaž řešený příklad s vysvětleným uvažováním, úlohu s nedokončeným postupem a samostatné procvičení. Podrobnost přizpůsob předchozím znalostem. Pro aktuální krok poskytuj potřebné informace; dekorace a souběžné požadavky musí mít vzdělávací účel. Ve třídě umožni zastavení, společný rozbor i pokračování vlastním tempem.

Pomoc odstupňuj pružně: objasnění překážky, cílená nápověda, dílčí krok a podle potřeby či žádosti komentované řešení. Poté nabídni obdobnou úlohu bez pomoci. Podporu omezuj podle doloženého samostatného výkonu. Dva úspěchy ani vlastní pocit jistoty samy nezakládají zvládnutí.

Jazykovou náročnost odděl od oborové. U žáků s češtinou jako druhým jazykem zvaž vysvětlení termínů, názornou oporu a stručnější zadání, aniž bys automaticky snížil oborový cíl. Potřebnou podporu odvozuj z konkrétní situace, nikoli z příslušnosti ke skupině.

### Metody: Sokratické učení

Použij je k prozkoumání předpokladů, argumentů a chybných představ, když žák má znalosti potřebné k odpovědi. Elenchus zkoumá soudržnost tvrzení s přijatými předpoklady; jeho cílem ve výuce není žáka porazit. Paulův a Elderův přístup nabízí otázky po významu, předpokladech, důkazech, jiných hlediscích, důsledcích a samotné otázce.

Aplikace položí jednu cílenou otázku, reaguje na konkrétní odpověď a umožní žákovi revidovat úsudek. Nevkládá mu do úst předem určenou tezi ani nepředpokládá, že každá původní odpověď je chybná. Zastav nekonečné dotazování: při chybějících znalostech, opakovaném uvíznutí či žádosti nabídni výklad nebo příklad. Otázky nenahrazují ověření věcné správnosti.

### Metody: Feynmanova technika

Vysvětlení tématu vlastními slovy začátečníkovi může zviditelnit mezery v porozumění. Hodí se po prvním seznámení s učivem nebo při přípravě na jeho použití. Aplikace hraje zvídavého posluchače, požádá o vysvětlení konkrétní nejasnosti, nabídne návrat ke zdroji a nechá žáka vysvětlení přepracovat.

Věcnou správnost posuzuj podle zdrojů a rubriky. Nepředstírej neporozumění přesnému vysvětlení jen kvůli pokračování dialogu. Doplň aplikační úlohu: plynulost, zjednodušení ani AI pochvala samy nedokládají hluboké porozumění. Označení techniky nezaručuje její účinnost v každém oboru.

### Metody: Vybavování, rozložení v čase a reflexe

Při vybavování z paměti žák rekonstruuje znalost před zobrazením odpovědi. Následuje opravná zpětná vazba a další příležitost znalost použít. Opakování s odstupem se k učivu vrací po smysluplné prodlevě. Okamžitý návrat chybné otázky je opravné procvičování, sám nestačí pro rozložení učení v čase. Vracej i část dříve správně vyřešeného učiva. Intervaly přizpůsob obsahu, požadované době uchování a dostupným hodinám; žádný rozvrh neoznačuj za univerzální optimum.

### Metody: Metakognice a řízení vlastního učení

Nech žáka zvolit dosažitelný dílčí cíl, naplánovat postup, sledovat vlastní porozumění a podle dokladů postup upravit. Odhad úspěchu nebo zdůvodnění volby porovnej se samostatným výkonem. Reflexi konkretizuj: který doklad změnil jeho názor a co zkusí příště. Sebejistota není měřítkem kompetence. U malé aktivity postačí smysluplná krátká otázka; dlouhý povinný deník nemusí být přínosem.

Při práci s generovanou nápovědou, řešeným příkladem nebo živou AI chraň aktivní roli žáka ve sdíleném kognitivním prostoru (rámec FALR: volba, kognitivní pauza, hodnocení, sebeřízení). Zabraň automatickému přechodu od výstupu modelu k akci žáka: před převzetím nebo zkopírováním výstupu zařaď kognitivní pauzu. Vyzvi žáka k posouzení, zda je výstup platný, co v něm chybí, čemu skutečně porozuměl sám oproti tomu, co za něj udělal systém, a zda výstup použije, upraví, nebo odmítne.

### Metody: Pojmové mapy a vztahy

Pojmovou mapu zvol, pokud je cílem vysvětlovat nebo vytvářet vztahy. Nech žáka sestavit malou mapu, pojmenovat chybějící vazbu nebo posoudit navržené spojení; výsledek porovnej s ověřenými zdroji či rubrikou. Hotová mapa vytvořená výhradně za žáka je podklad, nikoli doklad jeho porozumění.

Vazby pojmenuj: předpoklad, část celku, kontrast, souvislost nebo příčina za vymezených podmínek. Z výskytu dvou jevů neodvozuj příčinu a síť křížových vazeb nenuť do stromu. Uznávej různé platné struktury; posuzuj význam a zdůvodnění vztahů, nikoli souřadnice či vizuální podobnost. Nepředpokládej, že zdroj dokládá každé spojení.

Při implementaci použij stabilní identifikátory pojmů a podle potřeby typované orientované vztahy. Nabídni textovou alternativu a ovládání klávesnicí, pokud má žák mapu upravovat; přetahování nesmí být jedinou cestou odpovědi. Cíli může stačit stručná tabulka vztahů bez grafového editoru. Ověř jednu platnou alternativní mapu a jednu chybnou vazbu proti pravidlům zpětné vazby.

### Metody: Metody závislé na kontextu

- Bádání: podpoř otázku, předpověď, zkoušku, pozorování a vysvětlení. Tvrzení o reálném světě potřebují vhodná data nebo přiměřeně ověřený model. Ilustrační výsledky označ a vymez jejich platnost. Vyprávění jazykového modelu nenahrazuje experimentální doklad.
- Hraní rolí: vymez roli, hranice scénáře a kritéria, poté zařaď rozbor. Historický dialog označ za rekonstrukci a odděl doložená fakta od vymyšlené řeči. Fiktivní situace může mít emoční či sociální důsledky. Simulace odborného úkonu sama nepotvrzuje praktickou způsobilost v reálném provozu.
- Kooperativní učení: připrav společný úkol, odpovědnost jednotlivců a kritéria užitečného vysvětlování. Rozděl role tak, aby jeden žák neprovedl vše. Umožni řešit neshody a ověř porozumění každého samostatným krátkým výstupem. Sdílení zařízení nesmí zaměnit klikání jednoho za výkon celé skupiny.
- Vrstevnické učení: nech žáky porovnat vysvětlení a poskytnout si zpětnou vazbu podle srozumitelných kritérií. Při vzájemném vysvětlování zajisti přístup k ověřenému řešení nebo učiteli, aby se mezi žáky neupevňovala chybná představa. Odpovědnost za správnost nepřenášej na nezkušeného spolužáka.
- Projektová výuka: vymez smysluplný produkt, průběžné milníky a individuální doklady. Působivý výstup sám nedokládá zamýšlené učení. Projektovou výuku neslučuj s konektivismem.
- Převrácená výuka: propoj domácí přípravu s použitím ve třídě a zajisti náhradní cestu pro žáky bez přípravy či potřebného přístupu. Jde o organizaci výuky, jejíž přínos je třeba ověřovat.
- Gamifikace: postup, příběh či odměny přidávej, pokud podporují cíl. Veřejná soutěž a časové bodování potřebují důvod a přístupnou alternativu. Zvaž vztahy ve třídě a možnost účasti bez veřejného srovnávání.

### Metody: Odborné zdroje

- [Krathwohl, 2002: A Revision of Bloom's Taxonomy](https://people.ucsc.edu/~ktellez/blooms_taxonomy.pdf): dvě dimenze a překrývající se kategorie.
- [IES: Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): doporučení pro opakování, vybavování, řešené příklady a vysvětlující otázky. Síla důkazů se mezi doporučeními liší.
- [UNESCO: Guidance for Generative AI in Education and Research](https://www.iicba.unesco.org/en/africa-education-knowledge-platform/guidance-generative-ai-education-and-research): lidská odpovědnost a ověřování vzdělávacího využití AI.
- Zinger, D. (CFM / FALR – Four-Action Learner Regulation Framework): regulace učení ve sdíleném kognitivním prostoru s AI (volba, kognitivní pauza, hodnocení, sebeřízení).

## Reference: hodnoceni

Zdrojový oddíl: Doklady učení, hodnocení a zpětná vazba


### Hodnocení: Začni rozhodnutím

Ke každému důležitému cíli určuj činnost žáka, získaný doklad, kritéria úspěchu a navazující výukové rozhodnutí. Uveď podmínky: nápovědy, pomůcky, spolupráce a čas. Praktické či sociální cíle ověřuj odpovídajícím výkonem. Znalostní kvíz nenahrazuje pozorování praktické dovednosti nebo spolupráce.

Příklad: žák předpoví účinek změny v neznámém elektrickém obvodu a vysvětlí příčinu. Dokladem je předpověď i zdůvodnění. Rubrika posoudí princip, použití a uvažování. Chybná představa vede ke kontrastnímu příkladu a novému samostatnému pokusu.

### Hodnocení: Vymez účel a podmínky

V procvičování může žák žádat vysvětlení, opakovat pokus a využít odstupňovanou pomoc. Použití podpory eviduj odděleně od samostatného úspěchu. Zpětná vazba označí správnou část, konkrétní nedostatek a proveditelný další krok; následuje příležitost výstup opravit nebo znalost použít.

V režimu ověřování stanov předem dovolenou pomoc a pravidla vyhodnocení. Tutor je musí dodržovat. Vysvětli načasování zpětné vazby. Výsledky procvičování bez upozornění nepřeváděj na známky. Formativní hodnocení využívá doklady k úpravě dalšího učení; sumativní vyjadřuje dosažení stanovených kritérií. Samotné přidělení bodů bez dalšího rozhodnutí netvoří formativní postup.

Při změně režimu vyřeš rozpracovaný pokus a již zobrazené řešení. Skrytí nápovědy z podporovaného pokusu nevytvoří nezávislé ověření; použij vhodnou novou úlohu a původní výsledek zachovej jako procvičování. Přístupné ovládání, čtečka obrazovky nebo dohodnutá úprava podmínek nejsou automaticky obsahovou nápovědou. Jejich vztah k ověřovanému cíli a pravidlům řeš výslovně.

Nezaváděj univerzální procentní hranice pro známky ani jednotnou stupnici pro všechny cíle. Pravidla konkrétní školy či kurzu si nech doložit. Vlastní metodický návrh označ jako návrh; netvrď, že představuje školní nebo právní požadavek. Ve třídě rozliš skupinový produkt a individuální výkon. Úspěch skupiny automaticky nepřipisuj každému členovi.

### Hodnocení: Navrhuj důvěryhodné úlohy

Ověř klíč odpovědí, vysvětlení a přijatelné alternativy. U výběrových úloh používej smysluplné chybné možnosti odvozené od typických omylů a odstraň nechtěné nápovědy. U otevřených odpovědí přijímej rovnocenné formulace, jiné správné postupy a uvedené předpoklady. Jediná vzorová věta nesmí představovat celý prostor správných řešení.

Použij stručnou hodnoticí rubriku: pozorovatelná kritéria, popis výkonu a příklady včetně hraničních a alternativních řešení. Podle cíle odděl věcnou správnost, uvažování, postup, komunikaci a spolupráci. Jazykovou formu hodnotíš tehdy, je-li součástí cíle. V českém jazyce může být diakritika či pravopis předmětem ověřování; v jiné úloze překlep nesmí automaticky zastínit oborové porozumění. Předem určuj, jaké varianty jsou přijatelné. Obtíž s formulací v češtině sama nedokládá neznalost oboru.

U postojových a občanských témat rozliš znalost faktů, kvalitu argumentu, respektující jednání a osobní stanovisko. Neodměňuj názorovou shodu s učitelem či modelem a nevyvozuj osobnostní profil. Kritéria mají odpovídat cíli a umožnit obhajitelný odlišný závěr.

U čísel stanov jednotku, způsob zaokrouhlení a zdůvodněnou absolutní či relativní toleranci. Přijímání desetinné čárky a tečky implementuj podle jednoznačně vymezeného formátu; slepá náhrada může zaměnit oddělovač tisíců za desetinný znak. Ověř převody jednotek, znaménka i mezní hodnoty. Pokud je práce s jednotkou nebo přesností cílem, její vynechání či změnu automaticky neopravuj. Nejasný zápis nech upřesnit.

Rychlost a veřejné pořadí potřebují vzdělávací účel. Body za účast, odznaky ani potvrzení o dokončení nedokládají zvládnutí učiva. Úspěšná simulace sama neopravňuje tvrdit, že žák získal odbornou kvalifikaci nebo zvládl reálný praktický úkon.

V bance úloh zpřístupni důležitá rozhodnutí v existujícím datovém formátu. Podle potřeby použij stabilní ID úlohy a cíle, zadání, přijatelné odpovědi či rubriku, vysvětlení, nápovědy, zdroj a stav revize; u čísel jednotky a tolerance. Záznam odpovědi odděl: odpověď, použitá pomoc, pokus a stav vyhodnocení. Jde o příklad datové dohody, nikoli povinné schéma či důvod sledovat jednotlivce ve sdílené demonstraci.

### Hodnocení: Meze úsudku AI

Skóre AI i její výklad chyby považuj za předběžný úsudek. Ověřuj je na příkladech posouzených učitelem a dostupnými oborovými kontrolami. Při nejasných dokladech požádej o upřesnění nebo označ výsledek k revizi. Nevyráběj jistotu a nepoužívej nekalibrované číslo sebedůvěry jako důkaz správnosti.

Žák musí mít cestu ke zpochybnění zpětné vazby. Učitel může výsledek opravit a vidí původní odpověď i odůvodnění. Rozhodnutí s podstatnými důsledky potřebují odpovědnou lidskou kontrolu, která situaci odpovídá. Automatické posuzování sociálních vlastností či diagnóz z běžných odpovědí nezaváděj.

### Hodnocení: Ověřuj tvrzení o učení

Pokud je to proveditelné, porovnej vstupní úlohu s obdobnou samostatnou úlohou po výuce. Později ověř uchování a použití v jiném kontextu. Zlepšení interpretuj opatrně: opakované položky, pomoc a různé výchozí podmínky mění výsledky. Malý třídní pilot může odhalit potíže, sám neprokazuje příčinný účinek aplikace. Při sdílených zařízeních ověř, komu výsledek patří.

Dokončení, používání, čas, spokojenost, odezvu a technické chyby sleduj jako provozní či uživatelské ukazatele. Vyhodnocuj je odděleně od vzdělávacích výsledků. Sbírej pouze údaje potřebné pro dané rozhodnutí a uveď, co z nich nelze usuzovat.

### Hodnocení: Zdroje a povaha doporučení

- [EEF: Teacher Feedback to Improve Pupil Learning](https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/feedback): cíle, doklady nedostatků, účelné načasování a možnost zpětnou vazbu využít. Doporučení pro učitele neověřuje každou implementaci AI.
- [IES: Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1): samostatné vybavování a opakování s odstupem podporují návrh ověřování.

Postup, příklad rubriky i implementační volby jsou metodická doporučení. Vhodnost posuď podle žáků, předmětu, důsledků hodnocení a dostupných dokladů.

### Hodnocení: Ověř rozhodnutí a oprav důsledky

U úlohy s jednou správnou odpovědí nezávisle vyřeš skutečné zadání a zkus obhájit každou možnost podle uvedených jednotek, přesnosti a předpokladů. Obhajitelná musí zůstat právě jedna. U vícečetného výběru dodrž oznámené pravidlo; u otevřených úloh zachovej platné alternativy. Potom aplikuj každý deklarovaný chybný postup na skutečná data: musí vést k zamýšlenému distraktoru. Po změně zadání znovu prověř dotčené možnosti. Ekvivalentní zlomky nebo neurčené zaokrouhlení nesmějí vytvořit další správnou odpověď.

Propoj pozorovanou odpověď, možné vysvětlení, rozlišující doplňující úlohu a konkrétní další krok. Jedna chyba neurčuje příčinu. Při návrhu podle důkazů (ECD) vymez cílovou kompetenci, pozorovatelný důkaz a úlohu, která jej vyvolá. Herní událost může odrážet motorickou obtíž, zkoumání nebo tipování; telemetrie sama neurčuje vytrvalost ani osobnost. Vysvětli potřebný sběr dat.

Při chybě obsahu, klíče či výkladu tutora chybu přiznej a oprav; prověř navazující nápovědy, úlohy, hodnocení a pokrok. Dotčený pokus nevydávej za důkaz neznalosti. Zachovej potřebný původní důkaz a verzi obsahu; označ nejistotu a podle potřeby nabídni nové ověření. Učitelský i žákovský pohled musí používat stejnou verzi zadání a možností.

Ověřovací postupy rozvíjejí návrhové principy [Learning Commons pro kontrolu porozumění](https://github.com/learning-commons-org/agent-skills/tree/main/skills/k12-check-for-understanding). Nepřebírají pevné formáty, americké kurikulum jako výchozí ani omezení uvádění zdrojů.

## Reference: simulace

Zdrojový oddíl: Simulace a hraní rolí


Tuto referenci použij, pokud aplikace modeluje systém, podporuje experiment nebo nechává žáky jednat v připraveném scénáři. Vyber kontroly odpovídající danému projektu.

### Simulace: Co představuje výstup

Žákům srozumitelně rozlišuj:

- **Měření:** pozorování z přístroje, datové sady nebo zaznamenaného experimentu. Uveď původ dat a podstatná omezení měření.
- **Výpočet nebo simulace:** výsledky konkrétního matematického modelu či soustavy pravidel. Uveď předpoklady a rozsah platnosti modelu.
- **Fikce nebo rekonstrukce:** vymyšlené události, rozhovory, postavy či důsledky sloužící výuce. Označ je tak.

Generovaná čísla nevydávej za měření a vymyšlený rozhovor za autentický citát. Simulace může ilustrovat hypotézu, její výstup však sám nedokládá chování reálného světa.

### Simulace: Vymezení a kontrola modelu

Zaznamenej vzdělávací cíl, stavové proměnné, vstupy, jednotky, povolené rozsahy, předpoklady, pravidla změn a pozorovatelné výstupy. Vysvětli zjednodušení ovlivňující interpretaci. Ovládání má zpřístupnit zkoumaný vztah; žák nemá hádat nezdokumentovaná nastavení.

Číselné výsledky počítej ověřeným výpočetním jádrem nebo výslovně definovanými pravidly. Výpočet odděl od komentáře jazykového modelu. AI může vysvětlovat získané výsledky, nesmí si domýšlet chybějící výpočet ani předstírat provedení experimentu.

Ověř několik kontrol, které modelu odpovídají: známý příklad, mezní případ, správnost jednotek a jeden očekávaný trend. U náhodných modelů popiš zdroj náhodnosti a podle potřeby umožni opakování se stejným inicializačním číslem. Uveď omezení modelu.

### Simulace: Průběh učení

Pokud to podporuje cíl, nech žáka před spuštěním vyslovit a vysvětlit předpověď. Umožni měnit podstatné vstupy, sledovat vypočtený výstup, porovnat jej s předpovědí a upravit vysvětlení. Závěrečná reflexe má oddělit chování modelu od tvrzení o světě a hledat situace, v nichž model nestačí.

Samotné dosažení cílového nastavení nepovažuj za důkaz porozumění. Vyžádej vysvětlení, porovnání nebo použití poznatku v nové situaci.

V odborném výcviku a laboratoři stanov bezpečné limity modelu a vysvětli rozdíly proti reálnému zařízení. Úspěch v simulaci nepotvrzuje praktickou způsobilost. Nácvik nenahrazuje odborný dohled a schválené provozní postupy. Nepřidávej podrobné návody k rizikové fyzické činnosti nad rámec zadaného a odborně schváleného postupu.

### Simulace: Historické a společenské role

Uveď, zda je postava smyšlená, složená z více předloh, nebo vychází z doložené historie. Odděl doložená fakta od rekonstruovaných promluv. U historických tvrzení uveď původ a podle potřeby sporné interpretace. Nepředstírej přístup k myšlenkám osob a nevymýšlej citace.

Vymez roli, hranice scénáře, vzdělávací cíl a závěrečnou reflexi. Nabídni zřetelné ukončení role, věcné vysvětlení a přivolání učitele či jiné dostupné lidské pomoci. Emoční intenzitu a téma přizpůsob žákům a situaci ve třídě. U citlivých scénářů nabídni alternativní aktivitu. Hodnoť zamýšlené uvažování nebo komunikaci podle předem známých kritérií; souhlas s postavou není měřítkem úspěchu.

## Reference: ai-provoz

Zdrojový oddíl: AI při používání vzdělávací aplikace


Tuto referenci použij pouze tehdy, když hotová aplikace během používání volá AI službu. AI použitá k napsání kódu nebo přípravě obsahu zkontrolovaného učitelem takový provoz nevyžaduje. Offline aktivitě připojení nepřidávej, pokud je nevyžaduje vzdělávací cíl. Nevnucuj konkrétní model.

### Provoz AI: Vymezená výuková role

Urči povolené činnosti modelu, zkontrolované podklady či zdroje a postup při chybějících důkazech. Kde záleží na věcné správnosti, vymez schválené materiály a zachovej jejich původ. Nevytvářej zdánlivě věrohodné citace. Připusť nejistotu a opravu. Z krátkého rozhovoru nevyvozuj diagnózy ani sebejisté soudy o schopnostech žáka.

Pomoc přizpůsob aktivitě. Procvičování může využívat naváděcí otázky, odstupňované nápovědy, řešené příklady i přímé vysvětlení na požádání nebo tehdy, když další otázky nepomáhají. Při zkoušení se pomoc řídí pravidly učitele. Nezaváděj nekonečné sokratovské dotazování ani všeobecný zákaz sdělit řešení. Žák musí mít možnost požádat o pomoc, skončit nebo zapojit učitele.

Rozhraní s živou AI navrhuj tak, aby bránilo bezmyšlenkovitému kopírování výstupů, kdy nástroj myslí za žáka. Před převzetím vygenerovaného postupu nebo odpovědi vyžaduj krátkou kontrolu žáka: vymezení vlastního záměru před dotazem, zastavení nad výstupem (kognitivní pauzu), zhodnocení úplnosti či správnosti a vědomou volbu dalšího kroku (pokračovat, ověřit, přeformulovat dotaz, nebo výstup nepoužít).

Pro zpětnou vazbu a otevřené odpovědi používej výslovná hodnoticí kritéria. Před použitím porovnej hodnocení modelu s příklady posouzenými učitelem. Závažná rozhodnutí o klasifikaci, zařazení žáka nebo kázeňských opatřeních vyžadují odpovědnou lidskou kontrolu; jediná odpověď modelu nesmí rozhodovat sama. Zaznamenej nejistotu a umožni učiteli hodnocení opravit.

### Provoz AI: Minimum žákovských dat

Popiš vstupy odesílané poskytovateli, uchovávání dat, přístupová oprávnění a mazání. Sbírej jen údaje potřebné pro aktivitu. Automaticky nepřidávej účty, skutečná jména, trvalé profily ani ukládání rozhovorů. Kde stačí anonymní nebo pseudonymní označení aktivity, použij je; pseudonym sám anonymitu nezaručuje.

Před nasazením nezletilým ověř s odpovědnou školou věkovou skupinu, školní pravidla a dohodnutý postup, aktuální podmínky a nastavení poskytovatele i příslušné místní požadavky. Nevymýšlej univerzální věkovou hranici souhlasu ani obecně platné právní pravidlo. Nakládání s daty vysvětli učitelům a žákům přiměřeným jazykem.

### Provoz AI: Ochrana v architektuře

Vyžaduje-li služba tajné přístupové klíče, uchovávej je v chráněné serverové části. Nikdy je nevkládej do kódu prohlížeče. Oprávnění, limity požadavků a přístup k nástrojům vynucuj mimo prompt. Vstupy žáků, načtené dokumenty i odpovědi modelu považuj za nedůvěryhodná data.

Odděl instrukce od vloženého obsahu, omez nástroje a cílová místa komunikace, ověřuj strukturované odpovědi a bezpečně vykresluj obsah. Zabraň přímému spouštění generovaného textu jako kódu nebo privilegované operace. Pokyn modelu, aby ignoroval podvržené instrukce, není bezpečnostní záruka. Implementovanou architekturu nech posoudit odpovídajícím bezpečnostním postupem.

### Provoz AI: Cena, výpadky a pokračování práce

Stanov rozpočet, limity relace, časové limity a možnost zrušení požadavku. Během čekání zobraz srozumitelný stav. Ošetři výpadek školní Wi-Fi, nedostupný model, chybný formát odpovědi a vyčerpanou kvótu bez ztráty práce žáka. Opakování požadavků musí být bezpečné a omezené.

Navrhni přiměřenou náhradu: zkontrolované nápovědy, statické úlohy, uložený postup nebo pomoc učitele. Nedostupnou zpětnou vazbu označ; nevymýšlej ji. Počítej s různými školními zařízeními a omezeným připojením. Záložní průchod sám o sobě není důvodem přidat další backend.

Před použitím ve třídě projdi hlavní aktivitu, chybnou odpověď, žádost o pomoc, nejisté hodnocení a selhání služby. Uveď zbývající omezení a rozsah kontroly učitelem.

### Provoz AI: Ověř generovaný obsah ve vymezených mezích

Před zpřístupněním generovaných úloh proveď relevantní kontroly oborové správnosti, řešitelnosti, stavových přechodů a vykreslení. Jediné řešení vyžaduj jen u úloh, které ho slibují. Oprávnění a hranice strukturovaných výstupů vynucuj mimo model; schéma nedokládá pravdivost a deterministická kontrola zaručuje jen vlastnosti, které ověřuje. Neplatný obsah odmítni nebo odděl k revizi a zachovej ověřenou náhradu. Důsledky chyby pro nápovědy, hodnocení a pokrok řeš postupem oprav v `hodnoceni.md`.

## Reference: ceske-skolstvi

Zdrojový oddíl: České školní prostředí a kurikulární návaznost


Tuto referenci čti, pokud se úkol vztahuje ke konkrétní české škole, kurikulu, zkoušce nebo organizaci výuky. Český jazyk sám není takovým důvodem. U malé pomůcky ověř jen údaje potřebné pro rozhodnutí.

### České školství: Urči použitý rámec

Podle úkolu zjisti typ školy, obor, ročník, předmět či oblast a konkrétní dokumenty. Neomezuj české vzdělávání na základní školu: předškolní, gymnaziální, odborné, speciální či jiné vzdělávání mají odlišný kontext. U odborného vzdělávání může být potřebný kód oboru a vazba na praktickou přípravu. Dospělí nebo neformální kroužek nemusí pracovat podle RVP.

Rozlišuj rámcový program, školní ŠVP, používaný tematický či učební plán a zadání konkrétní aktivity. Z veřejného RVP neodvozuj, co přesně škola zařazuje do daného ročníku. Verzi a použitelnost dokumentu ověř pro konkrétní školu, obor a období; automaticky nepřepínej na nejnovější nalezený dokument. Termíny změn a podmínky přechodu nepřebírej ze staré paměti modelu.

Pokud podklady chybějí, můžeš navrhnout samostatně popsaný vzdělávací cíl. Označ návaznost jako předběžnou a uveď, co musí potvrdit učitel. Netvrď soulad s nedodaným ŠVP. Chybějící ŠVP nemusí blokovat vytvoření obecné pomůcky, pokud nevytváříš neověřenou deklaraci nebo závažné hodnocení.

### České školství: Dolož mapování

Pro podstatné vazby zachyť dokument a verzi, oddíl nebo ověřený identifikátor, přesné relevantní znění a rozsah aktivity. Vytvářej úsporný záznam:

| Podklad | Znění či odkaz | Cíl aktivity | Činnost a doklad | Stav ověření |
|---|---|---|---|---|
| Konkrétní dodaný RVP/ŠVP | Přesný doložený oddíl | Vlastní operacionalizace cíle | Co žák provede a podle čeho se to posoudí | Ověřeno, nebo návrh k potvrzení |

Nevymýšlej kód nebo citaci, aby tabulka působila dokončeně. Rozlišuj očekávané výstupy a očekávané výsledky učení podle použitého rámce. Nezaměňuj výsledek pro uzlový bod s povinným výsledkem jedné vyučovací hodiny. Kompetence, gramotnosti a průřezová témata přiřazuj jen při věcné vazbě; nezahrnuj automaticky vše. Konkrétní dílčí úloha nedokládá úplné naplnění celého rámcového cíle.

### České školství: Organizace a různorodost třídy

Zvaž délku hodiny včetně přesunů a spuštění, sdílená zařízení, projekci, výpadek připojení a způsob zásahu učitele. Nevnucuj jednotlivé účty aktivitě na společné tabuli. Při skupinové práci rozlišuj společný výsledek a doklad jednotlivce. Nabídni navazující otázku nebo pokračování pro rychlejší žáky místo pouhého zvyšování množství stejné práce.

Čtenářskou, jazykovou a oborovou náročnost posuzuj odděleně. U češtiny jako druhého jazyka podle cíle pomůže vysvětlení pojmů, názorný příklad, rozdělení zadání nebo přiměřená alternativa odpovědi. Nepředpokládej nižší oborové schopnosti podle znalosti češtiny a nesnižuj automaticky vzdělávací cíl. Pravopis zachovej jako kritérium, pokud je sám cílem. Potřeby přístupnosti a podpory projednávej funkčně s učitelem, bez zbytečných citlivých dokumentů a nálepkování.

### České školství: Zkoušky a odborná praxe

Při přípravě na přijímací, maturitní či profesní zkoušku ověř pro příslušný rok oficiální specifikaci a podmínky. Vlastní procvičovací úlohy neoznačuj za oficiální a neupravuj bez upozornění kritéria skutečné zkoušky. Přístupnost procvičování a oficiální úpravy zkušebních podmínek jsou odlišná rozhodnutí. Nezaváděj univerzální převod procent na známky.

Laboratorní a profesní simulace může připravovat na výkon. Bez příslušného praktického ověření nedokládá bezpečnou manipulaci ani profesní způsobilost. Pro práci s reálným zařízením zohledni odpovědného učitele, místní postupy a bezpečnostní podmínky. Nevytvářej automatickou certifikaci ze skóre simulace.

### České školství: Zdroje a aktuálnost

Při použití konkrétního dokumentu zaznamenej jeho verzi a datum ověření. Prohledávač a metodický komentář nejsou automaticky závazným zněním; ověř charakter zdroje. Soukromé podklady školy používej jen v potřebném rozsahu a podle oprávnění. Pro právní a provozní rozhodnutí ověř aktuální relevantní pravidla, neslibuj obecnou zákonnost produktu.

- [MŠMT: přehled RVP](https://edu.gov.cz/dokumenty/rvp-ramcove-vzdelavaci-programy/): výběr odpovídajícího rámce.
- [NPI: Prohlédnout RVP](https://prohlednout.rvp.cz/): dokumenty a rozlišená metodická podpora.
- [CERMAT: specifikace JPZ](https://prijimacky.cermat.gov.cz/menu/specifikace-pozadavku-k-jpz.html): příklad průběžně ověřovaného podkladu pro zkouškovou přípravu.
- [NPI: čeština jako druhý jazyk](https://zapojmevsechny.cz/clanek/392-co-mam-delat-kdyz-zacinam-ucit-cestinu-jako-druhy-jazyk): metodický vstup k jazykové podpoře; konkrétní podmínky a aktuální kurikulum ověř podle situace.

## Reference: modely-a-prostredi

Zdrojový oddíl: Modely, uvažování, rychlost a prostředí


Tuto referenci použij při doporučení modelu, jeho nastavení nebo způsobu načítání skillu. Didaktické zásady zůstávají společné. Níže uvedená nastavení jsou výchozí doporučení pro tuto práci, nikoli výsledky srovnávacího testu výrobců.

Dokumentace ověřena 2026-11-04. Názvy, dostupnost, volby i ceny se mění. Před použitím konkrétního názvu ověř nabídku uživatele a aktuální oficiální podklady. Netvrď, že jsi model či nastavení přepnul, pokud to neprovedl dostupný ovládací mechanismus.

### Modely a prostředí: Nejprve vyber náročnost úkolu

Menší model použij pro ohraničenou úpravu s jasnými kritérii, střední pro běžný návrh a implementaci, silnější pro rozporné podklady, složitou simulaci nebo posouzení s významnými důsledky. Jde o kategorie práce, nikoli záruku schopností. Zachovej uživatelovu volbu, pokud kritéria splňuje.

Tabulka konkrétních názvů níže je **výchozí doporučení pro tento skill bez srovnávacího testu**, odvozené z dokumentace. Není změřeným pořadím modelů. Za ověřenou označ konfiguraci až po reprezentativních úlohách.

### Modely a prostředí: Kdy zvýšit uvažování a kdy skončit

U jasného úkolu začni podporovanou výchozí úrovní nebo dříve úspěšným nastavením. U rozporných zdrojů či složitého modelu zvaž vyšší uvažování rovnou. Pokud výstup přehlédne výslovné omezení, odporuje vlastnímu hodnocení, selže ve smysluplné kontrole výpočtu nebo opakovaně vytváří neplatné úlohy, nejprve ověř dostupnost potřebných podkladů a reference. Chybějící vstup nebo nejasné kritérium naprav před změnou modelu.

Jestliže po jedné cílené opravě stále selhává stejné podstatné kritérium, doporuč podporovanou vyšší úroveň uvažování a kritérium znovu posuď. Pokud problém trvá, doporuč silnější dostupný model nebo nezávislou kontrolu podle dopadu. Neopakuj pokusy bez konce a nepřekračuj dohodnutý rozpočet. Chybějící zdroj, nedostupný nástroj či výpadek služby vyžaduje vyřešení závislosti nebo přiznání omezení; více uvažování nedodá chybějící důkaz. Nevyřešené chyby předej. Nastavení měň jen autorizovaným ovládáním prostředí.

Uvažování snižuj nebo menší model použij až po úspěšných relevantních kontrolách; uchovej doklady o kompromisu. Rychlost obsluhy posuzuj zvlášť: výchozí je standard, placené zrychlení potřebuje časové a cenové zdůvodnění a autorizaci.

### Modely a prostředí: Udržuj doporučení aktuální

Konkrétní doporučení znovu ověř při změně modelu či verze klienta, chybějícím nastavení, změně dostupnosti u poskytovatele nebo rozporu dokumentace s pozorováním. Do té doby kombinaci označ jako neověřenou a použij kategorii úkolu a podporované výchozí volby prostředí. Neznámému modelu nevymýšlej ekvivalent nastavení. Specifické úpravy instrukcí pro poskytovatele přidávej až při opakovatelném selhání, které dokládá jejich potřebu; eviduj dotčenou verzi a po zániku důvodu úpravu odstraň.

### Modely a prostředí: Vyber podle práce

| Práce | Výchozí volba OpenAI | Výchozí volba Claude | Výchozí volba Gemini |
|---|---|---|---|
| Drobná přesně vymezená úprava obsahu nebo kontrola strukturovaných úloh | GPT-6 Luna, High; snižuj až podle výsledků kontrol | Haiku 5.5, Medium | Gemini 3.5 Flash-Lite, Low, pokud jej prostředí nabízí |
| Návrh a realizace ohraničené výukové aktivity | GPT-6.1 Sol, výchozí úroveň nebo Medium | Sonnet 5.5, Medium pro dobře vymezenou práci agenta | Gemini 3.8 Flash, Medium |
| Náročný didaktický audit, rozporné zdroje, složitý model či architektura | GPT-6 Astra, Light/Low nebo Medium; zvýšit podle potřeby | Opus 5.5, Medium, podle potřeby High | Gemini 4 Argon, Medium, podle potřeby High |

Jde o doporučení autora skillu odvozená z podkladů výrobců. Neprokazují rovnocennost modelů ani lepší pedagogický úsudek jedné značky. Pokud zvolený model není dostupný, doporuč alternativu a sděl změnu; uživatelskou volbu bez autorizace neměň. Například u zavedeného postupu s Gemini 3.1 Pro lze zachovat tento model a jeho podporované nastavení. Tabulka nepředpovídá číselnou odezvu; tu ověř na reprezentativní úloze v daném prostředí.

Rozlišuj model, hloubku uvažování a případnou placenou rychlost obsluhy. Nižší úroveň uvažování může omezit objem práce modelu. Režim Fast je jiná volba a může zvýšit cenu. Flash je název modelové řady, nikoli univerzální přepínač rychlosti. Stejné názvy Low, Medium a High neznamenají stejný výkon ani odezvu u všech výrobců.

Začni standardní rychlostí. Placený Fast doporuč, pokud záleží na čekání a odpovídají tomu aktuální podmínky. Bez autorizace jej nezapínej a nenakupuj kapacitu. Průběžné zobrazování odpovědi nezaručuje dřívější dokončení. Posuzuj i čas kontroly a oprav výsledku.

### Modely a prostředí: OpenAI a Codex

V prostředí podporujícím skilly a čtení souborů používej nativní balíček. V Codexu lze výslovně uvést `$learning-methodologies` nebo `$vzdelavaci-metodiky`. Běžný chat nemusí stejným způsobem prohledávat disk; předej mu dostupný samostatný Markdown.

Ověřený průvodce rozlišuje Sol pro rozsáhlejší práci, Lunu pro vymezené úkoly a Astru pro náročné postupy; pro začátek uvádí také Lunu High a Astru Light/Low. Codex rozlišuje hloubku uvažování a Fast. Dostupnost a spotřeba závisejí na účtu, modelu a klientovi. Ověř podporované volby; popisek v aplikaci nemusí být identifikátorem API.

Zadej výstup, rozsah, relevantní soubory a pozorovatelná kritéria. Žádej stručné zdůvodnění rozhodnutí a doklady, nikoli zveřejnění vnitřního řetězce uvažování. Z názvu modelu neodvozuj přístup k terminálu, souborům nebo prohlížeči.

Zdroje: [modely](https://learn.chatgpt.com/docs/models), [rychlost](https://learn.chatgpt.com/docs/agent-configuration/speed), [skilly](https://developers.openai.com/plugins/concepts/skills).

### Modely a prostředí: Claude a Claude Code

Claude Code podporuje balíčky `SKILL.md` s doprovodnými soubory. Po objevení skillu lze použít `/learning-methodologies` nebo `/vzdelavaci-metodiky`. U jiného klienta Claude ověř jeho mechanismus, případně předej samostatnou verzi. Do společných metadat nepřidávej výhradně claudeovské hooky, shellové substituce ani přepnutí modelu.

Dokumentace pro agentní práci Sonnetu 5.5 doporučuje Medium u dobře vymezených úloh a vyšší úroveň u těžších. Opus 5.5 má výchozí Medium; starší generace a různá prostředí se liší. Úroveň effort a režim thinking nejsou totožné parametry. Nepřenášej kombinace voleb mezi verzemi bez ověření. Claude Fast je samostatná funkce s omezenou podporou modelů a vyšší cenou.

Odděl úkol, podklady a očekávaný výsledek. Uveď prostor pro rozhodování a požadované doklady. Příklad přidej tam, kde řeší nejasnost. Neopakuj celé jádro v každém zadání a nevyžaduj dlouhý záznam vnitřních úvah. Jde o způsob přenositelného zadání, nikoli tvrzení o zvláštní psychologii modelu.

Zdroje: [skilly](https://code.claude.com/docs/en/skills), [modely](https://platform.claude.com/docs/en/models/overview), [effort](https://platform.claude.com/docs/en/build-with-claude/effort), [Fast](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

### Modely a prostředí: Gemini a Gemini CLI

Gemini CLI hledá skilly v podporovaných složkách včetně aliasu `.agents/skills`. Objevení ověř příkazem `/skills list`, podle potřeby obnov pomocí `/skills reload`. Důvěryhodnost projektu a potvrzení aktivace řídí klient; neobcházej je. V AI Studiu nebo jiném chatu předej samostatný soubor, pokud nativní mechanismus není dostupný.

Ověřená dokumentace uvádí Low, Medium a High pro Gemini 4 Argon a Gemini 3.8 Flash. Jiné verze mají jiné výchozí úrovně a nabídky. Použij volby skutečného modelu a prostředí; nekopíruj doslova parametr OpenAI či Claude. Náhledový a stabilní identifikátor nejsou zaměnitelné.

Pro `gemini-3.1-pro-preview` ověřená tabulka API uvádí Low, Medium a High, výchozí je High. Pro tento endpoint doporučuji vyzkoušet Medium u běžného návrhu a High u náročného auditu, pokud klient dané volby nabízí. Samotný popisek Gemini 3.1 Pro nedokládá použitý endpoint a dostupné ovládání.

Instrukce formuluj přímo, s cílem, omezeními a požadovanými doklady. Předej dostupné podklady; napsaná cesta v chatu sama nezpřístupní soubor. Při implementaci aplikace s Gemini API zachovej potřebný stav komunikace s nástroji podle aktuální dokumentace. Tento skill API vrstvu nezavádí a neopravňuje k jejímu přidání.

Zdroje: [modely](https://ai.google.dev/gemini-api/docs/models), [uvažování](https://ai.google.dev/gemini-api/docs/thinking), [skilly Gemini CLI](https://geminicli.com/docs/cli/tutorials/skills-getting-started/).

### Modely a prostředí: Přenositelnost a doložené ověření

Používej prostá společná metadata `name` a `description` a běžný Markdown. Další metadata popisují verzi; bezpečnost neopírej o parametr, který jiné prostředí nemusí podporovat. Souborový agent dostane celý balíček s relativními referencemi, běžný chat úplnou samostatnou verzi. Obě jazykové varianty nenačítej automaticky současně. Po ztrátě kontextu obnov podstatný rozsah a rozpracovanou práci místo předpokladu, že je každý klient uchová.

Emoji může nést význam, ale nemá být jedinou instrukcí nebo označením priority. Zachovej výslovný text. Výzkum [významu emoji](https://arxiv.org/abs/2409.10760) a [kontextové nejednoznačnosti](https://arxiv.org/abs/2511.07193) neprokazuje přínos dekorování tohoto skillu pro dodržování pravidel. Takovou změnu nejprve ověř na konkrétních modelech a úlohách.

Za otestovanou označ kombinaci modelu a prostředí až po ověření načtení, přístupu k potřebné referenci, reprezentativního výstupu a důležitých hranic. Zaznamenej přesný model nebo viditelný popisek, klienta a verzi, jazyk, uvažování, rychlost, nástroje, datum, výstupy a chyby. Rozlišuj kompatibilitu podle dokumentace a pozorovaný průchod. Výsledek jednoho modelu nepřenášej na celou značku.

Srovnávej stejná zadání a podklady podle stejných vzdělávacích kritérií. Zařaď známý kontext, pomoc s cestou dál, alternativní správnou odpověď, nedoložené kurikulum, hranici výpočtu a dat a relevantní selhání nástroje. Snižuj uvažování nebo velikost modelu, jen pokud podstatné kontroly dál procházejí. Nedostupného poskytovatele označ jako neotestovaného, výsledky nevymýšlej.

## Reference: priklady-rozhodovani

Zdrojový oddíl: Příklady rozhodování


Použij relevantní příklad pro konkrétní nejasnost. Přizpůsob obor a věk; zachovej princip rozhodnutí.

### Příklady rozhodování: Přijmi rovnocennou odpověď

Úkol: vyjádři 1,5 A v miliampérech. Žák zadá `1500 mA`, kontrola očekává `1500`. Přijmi rovnocennou veličinu po kontrole jednotky a hodnoty. Pokud cíl výslovně ověřuje zápis jednotek, posuď jej zvlášť. Neodstraňuj slepě znaky: `1500 A` je zde chybně. Důvod: formátování nemá nahrazovat důkaz zvládnutí převodu jednotek.

### Příklady rozhodování: Ukonči neproduktivní sokratické dotazování

Při procvičování žák po otázce na proud a odpor říká: „Pořád tomu nerozumím, ukažte mi to.“ Poskytni krátké vysvětlení či řešený příklad při stálém napětí a nabídni novou předpověď s volitelnou pomocí. Další otázky nejsou podmínkou získání pomoci. Řešený příklad eviduj jako učení s podporou; nový samostatný úkol může přinést oddělený doklad. Důvod: otázky mají pomoci postupu v učení. Předem vymezené ověřování může mít jiná pravidla pomoci.

### Příklady rozhodování: Oprav věcně chybnou Feynmanovu interpretaci

Žák vysvětluje: „Rostliny získávají potravu z půdy, slunce ji ohřívá.“ Oceň srozumitelný zápis bez uznání věcné správnosti. Pojmenuj konkrétní miskoncepci, poskytni nebo ověř vhodný zdroj, odliš vodu a minerální látky od cukrů vznikajících fotosyntézou a vyzvi k nové jednoduché formulaci. Přenos ověř novou situací, například změnou bez světla. Důvod: plynulost a jednoduchost nejsou dokladem správnosti. Nevymýšlej pozorování experimentu ani nepřipisuj veškerý růst jedinému faktoru.

### Příklady rozhodování: Pracuj s nedostupným kurikulem

Učitel žádá „plný soulad s naším ŠVP“, ale dokument nedodal. Podle známého cíle navrhni pracovní aktivitu. Potřebný výňatek vyžádej, pokud záleží na přesné návaznosti; uveď, co zůstává neověřené. Nevymýšlej místní kódy výsledků ani nepotvrzuj úplné pokrytí. Obecný odkaz na RVP nedokládá návaznost na konkrétní ŠVP. Důvod: užitečný návrh může vzniknout i při otevřeně přiznané hranici doložení.

### Příklady rozhodování: Zařaď kognitivní pauzu před převzetím výstupu AI

V aplikaci s vestavěným AI pomocníkem žák požádá o návrh postupu řešení či vysvětlení chyby. Místo tlačítka „Použít v mém řešení“ zařaď kognitivní pauzu: skryj přímé kopírování a polož krátkou ověřovací otázku („Který krok postupu je klíčový? Co v návrhu AI chybí pro tvůj případ?“). Umožni žákovi návrh upravit, ověřit na jiném příkladu nebo zcela odmítnout. Samotné vygenerování textu modelem eviduj jako poskytnutou oporu, nikoli jako doklad žákova porozumění. Důvod: kognitivní pauza brání automatickému přechodu od výstupu modelu k akci žáka bez vlastního zpracování.

## Reference: stav-tutora

Zdrojový oddíl: Režimy tutora a návaznost učení


Čti při návrhu vícekrokového tutora, pokračování rozpracované aktivity nebo přípravy na zkoušku. Pravidla platí i pro deterministické offline aplikace; nevyžadují živou AI, účty ani trvalé ukládání.

### Stav tutora: Vymez režimy a přechody

Podle potřeby aktivity odděl vysvětlení, procvičování a ověřování. Vysvětlení může ukázat řešený příklad. Procvičování položí otázku, počká, poskytne zpětnou vazbu podle kritérií a nabídne pomoc. Ověřování dodržuje předem vymezená pravidla pomoci a časování zpětné vazby. Umožni přerušení, žádost o pomoc a odchod; při omezeném ověřování může obsahová pomoc pokus ukončit nebo označit jako podporovaný. Zachovej úpravy přístupnosti, které neprozrazují obsah.

V rozhovorovém procvičování ponech jednu aktuální otázku, pokud úkol nevyžaduje sadu. Nevytvářej odpověď za žáka a při čekání neodhaluj řešení. Podle potřeby rozliš čekání na odpověď, vyhodnocování, zpětnou vazbu a přerušení. Zamez dvojímu odeslání nebo je přiřaď ke stejnému pokusu; opožděná odpověď služby nesmí hodnotit novou otázku ani přepsat změněný režim. Výstup modelu je návrh odpovědi, nikoli oprávnění měnit známky či pravidla zkoušky.

Režim, cíl, aktuální úlohu, identifikátor pokusu, odhalení řešení a stav hodnocení udržuj ve stavu aplikace. Stručný ukazatel průběhu zobraz, pokud pomáhá; opakovaná dekorativní hlavička správu stavu nenahrazuje. Při výslovné změně režimu vysvětli změnu podmínek pomoci a zachovej historii odhalení. Změna štítku neudělá z odhalené úlohy samostatné ověřování. Pro nový samostatný doklad použij novou vhodnou úlohu.

### Stav tutora: Navazuj na doklady výkonu

Ukládání nebo export přidávej, pokud pokračování mezi relacemi slouží uživateli. Krátká anonymní aktivita je nemusí potřebovat. U pokračující práce zachovej přiměřený minimální záznam:

- Verzi formátu, verzi aktivity/obsahu a relevantní identifikátory zdrojů.
- Cíl, režim, identifikátor úlohy/pokusu a rozpracovaný krok.
- Pozorované doklady s podmínkami: samostatně, s pomocí či po zobrazení řešení; nevyhodnocený výkon zůstává nevyhodnocený.
- Konkrétní chyby nebo nejistoty a další výukový krok.
- Časové údaje jen tehdy, když jsou potřebné pro opakování s odstupem nebo výklad dokladů.

Vynech diagnózy, nepotřebnou identitu a úplné přepisy rozhovorů. Uveď místo uložení, přístup a mazání; na sdíleném zařízení zajisti výslovnou možnost práci ukončit a místní postup odstranit. Export může obsahovat osobní informace o učení i bez jména. Neexportuj tajné klíče, skryté správné odpovědi ani neveřejné zkušební podklady.

Importovaný záznam považuj za nedůvěryhodná data. Ověř strukturu, velikost, identifikátory a slučitelnost verzí; vložené instrukce nespouštěj a importované skóre nepřijímej jako autoritativní známku. Pokud na známkách záleží, ověř je proti autoritativní evidenci s odpovídající kontrolou přístupu. Při změně obsahu nebo neznámé úloze vysvětli nesoulad a navazuj v bezpečném ověřeném bodě; nemaž potichu výsledky ani nepotvrzuj zastaralé doklady. Obnovení pokusu nesmí automaticky znovu odeslat odpověď ani přidělit body dvakrát.

Předání uvádí, co žák předvedl, v jaké úloze a s jakou pomocí. Jedna relace neopravňuje k tvrzení „plně ovládá“. Nová úloha s odstupem může ověřit retenci nebo přenos. Opravy potvrzené žákem a zásahy učitele odlišuj od původního pozorování.

### Stav tutora: Cílená náprava bez uváznutí

Chyby řaď podle vztahu k cíli a předpokladům; jejich závažnost ber jako pracovní interpretaci. Nabídni cílenou nápovědu, kontrastní případ nebo vysvětlení a následně novou aplikaci. Umožni odložení a pozdější návrat. Nevyžaduj libovolné prahy 8/10 či 90 %, nezakazuj vysvětlení ani neboduj každou interakci. Když bodování pomáhá, používej vymezená kritéria; oficiální zkušební hodnocení vyžaduje skutečnou specifikaci.

### Stav tutora: Kontroly implementace

Prověř jen relevantní průchody: otázka, odpověď, zpětná vazba; pomoc, podporovaný výkon; změna režimu po odhalení; přerušení a obnovení bez ztráty či dvojího započtení pokusu; zastaralý nebo chybný záznam; opožděná odpověď po změně úlohy; nerozhodnuté hodnocení při výpadku. Ověř shodu uloženého a viditelného stavu. Tyto kontroly dokládají chování, nikoli vzdělávací účinnost.

## Reference: didakticke-zduvodneni

Zdrojový oddíl: Proč didaktické metody patří do vývoje aplikací pomocí AI


Čti při vysvětlování účelu skillu nebo rozhodování, jak se má metoda promítnout do aplikace. Skill pomáhá vývojářům a pedagogům využít AI k návrhu a tvorbě vzdělávacích aplikací. Podle potřeby řeší i aplikace používající AI při samotném učení. Metoda se musí projevit v činnosti žáka, zpětné vazbě a dokladech výkonu; samotný název funkce či zmínka v promptu nestačí.

### Didaktické zdůvodnění: Od didaktického rozhodnutí k pozorovatelnému chování

| Metoda nebo hledisko | Výukový záměr | Rozhodnutí v aplikaci | Co posuzovat |
|---|---|---|---|
| Sokratické otázky | Zkoumat předpoklady a uvažování žáka | Položit cílenou otázku, počkat a reagovat na skutečnou odpověď; podle potřeby vysvětlit | Zdůvodnění či revize tvrzení, včetně správné alternativy |
| Feynmanova technika a vlastní vysvětlení | Zpřístupnit žákovo vysvětlení k posouzení | Nechat vysvětlit, porovnat s ověřenými kritérii, řešit konkrétní mezeru a nabídnout nový případ | Správné vztahy a použití; plynulost sama nestačí |
| Řešené příklady a scaffolding | Pomoci začátečníkovi začít a postupovat k samostatnosti | Ukázat postup, nabídnout doplnění a novou úlohu; zachovat vyžádanou pomoc | Odlišit výkon s podporou od pozdějšího samostatného pokusu |
| Vybavování a opakování s odstupem | Procvičit rekonstrukci znalosti a později se k ní vrátit | Ptát se před odhalením, poskytnout opravu a vhodně plánovat návraty i ke správně řešenému učivu | Výkon před odhalením, pozdější retenci a přenos, pokud byly ověřeny |
| Pojmové mapy | Vyjádřit vztahy a předpoklady | Pojmenovat vazby, přijmout platné alternativní struktury a nabídnout přístupnou editaci | Význam a zdůvodnění vazeb, nikoli vizuální podobnost |
| Bádání a simulace | Porovnat předpovědi s doklady za vymezených předpokladů | Zpřístupnit proměnné, jednotky, omezení a hranice modelu; zařadit reflexi | Revizi vysvětlení podle pozorování nebo označených výsledků modelu |
| Formativní hodnocení a metakognice | Podle dokladů zvolit další krok | Poskytnout konkrétní zpětnou vazbu a porovnat předpověď úspěchu s výkonem | Využitelnou opravu a nové doklady; skóre a sebedůvěra samy nestačí |
| Kooperativní a vrstevnické učení | Podpořit porovnávání a vysvětlování s odpovědností | Sdílená úloha, individuální příspěvky a řešení neshod | Uvažování každého žáka; společný klik nedokládá porozumění skupiny |
| Regulace ve sdíleném kognitivním prostoru (FALR) | Udržet žáka aktivního a kritického při práci s AI či nápovědou | Vložit kognitivní pauzu před převzetím výstupu; nechat žáka posoudit, co chybí a čemu rozumí sám oproti výkonu systému; umožnit výstup odmítnout | Odlišení vlastního porozumění od výstupu systému a následný samostatný krok žáka |

Bloomova taxonomie pomáhá popsat kognitivní cíl a typ znalosti. Neurčuje obtížnost ani šest zamčených stupňů. Vhodnost metody závisí na žácích, obsahu a pozorované překážce; katalog neukládá použít všechny metody.

### Didaktické zdůvodnění: Proč na tom záleží při generování aplikace

AI může rychle vytvořit rozhraní, kontrolu odpovědí i zpětnou vazbu. Tyto části potřebují didaktické zadání: co žák udělá, co je dokladem výkonu, jakou měl pomoc a jak navazuje další rozhodnutí. Podle zadání omezuj generovaný kód i kontrolovaný obsah. Vybavování například mění okamžik odhalení odpovědi, scaffolding ovládání pomoci a označení dokladů. Pouhé pojmenování metody bez tohoto chování cíl neplní.

Rozliš AI při tvorbě a za běhu. Mnohé postupy lze realizovat offline pomocí ověřeného obsahu a deterministických kontrol. Pokud živá AI pomáhá s otevřenými odpověďmi nebo rozhovorem, vymez zdroje, kritéria a nástroje, ověř výstup a zajisti náhradní průchod. Delší rozhovor, přísnější body ani větší model samy nedokládají lepší učení.

### Didaktické zdůvodnění: Meze zdůvodnění

Jde o vysvětlení návrhových rozhodnutí, nikoli důkaz účinku tohoto skillu či každé aplikace. Obsah, přístupnost a proveditelnost ve třídě potřebují konkrétní kontroly. Technický průchod nedokládá učení; potřebné jsou vhodné doklady výkonu a pro příčinné tvrzení odpovídající vyhodnocení. Výzkumné podklady uvedené u metod podporují konkrétní rozhodnutí, necertifikují celý balíček. U významných posouzení zachovej odpovědnou kontrolu učitele a kurikulum přizpůsob skutečnému prostředí.

## Reference: vzdelavaci-hry

Zdrojový oddíl: Vzdělávací hry a účelná gamifikace


Čti při návrhu herních mechanik, motivace nebo podstatné změně vztahu hraní a učení. Doporučení propojují výzkum s návrhovým úsudkem; nedokládají účinnost nové aplikace. Zdroje ověřeny 2026-11-14.

### Vzdělávací hry: Vyber činnost před odměnou

Rozlišuj vzdělávací hru (učení probíhá hraním), gamifikaci (herní prvky podporují jinou činnost) a simulaci (model může sloužit bádání bez vítězství a skóre). Dobrá pomůcka nemusí potřebovat odměnový systém.

Sepiš stručnou vazbu: uživatel a vstupní znalosti; cílový výkon; hráčovo rozhodnutí; důsledek a zpětná vazba; samostatný doklad; další krok učení. Malé aktivitě stačí odstavec. Najdi možnou zkratku: lze vyhrát tipováním, opakovaným klikáním, zapamatováním pozic, opsáním odpovědi nebo výkonem spoluhráče?

Upřednostni mechaniku vyžadující zamýšlené přemýšlení. Pro poměry může hráč upravovat směs za smysluplných podmínek, vysvětlit předpověď a vyřešit nový případ. Kvíz může dobře sloužit vybavování; každý fakt nepotřebuje simulovaný svět. U otevřených cílů připusť různá obhajitelná řešení.

### Vzdělávací hry: Vyber malý související celek

| Potřeba | Možná mechanika a provedení | Ověření nebo známka selhání |
|---|---|---|
| Začít bez znalosti ovládání | Bezpečný první úkol; nástroj představ až při použití | Nováček provede akci bez vysvětlování autora |
| Pochopit systém | Předpověď, změna jedné proměnné, důsledek, vysvětlení | Náhodné posouvání nenahradí novou předpověď |
| Uchovat znalost | Vybavovací mise s pozdějším návratem a opravou | Samostatný výkon s odstupem; okamžité opakování je oprava |
| Vybrat správný postup | Po úvodní podpoře střídej zaměnitelné typy úloh | Žák vybere a vysvětlí strategii; náhodná směs témat nestačí |
| Překonat začátečnickou nejistotu | Řešený příklad, doplnění, samostatná výzva | Pomoc zůstává zaznamenána a lze se k ní vrátit |
| Vidět vlastní postup | Soukromá mapa dovedností s doklady a dalším krokem | Rozlišuje dokončení, úspěch s podporou a samostatný výkon |
| Rozhodovat o učení | Smysluplná volba cesty, kontextu či postupu | Volba mění zkušenost; předpoklady a alternativy jsou zřejmé |
| Probudit zvědavost | Záhada, jejíž stopy tvoří oborové důkazy | Rozuzlení řeší otázku učiva; příběh nezahltí procvičování |
| Spolupracovat | Doplňující se role, společný výsledek, střídání odpovědnosti | Každý něco samostatně vysvětlí nebo použije |
| Ocenit dosažený výsledek | Volitelný odznak s průhledným kritériem | Popisuje doklad; nezastupuje posouzení zvládnutí |
| Soutěžit | Volitelné srovnatelné výzvy nebo vlastní zlepšení | Sleduj znevýhodnění, odchod a spěch; nabídni cestu bez veřejného pořadí |
| Vracet se dlouhodobě | Vlastní cíle, pokračování v práci, vyžádané připomínky | Absence nemaže doklady učení ani přístup k pomoci |

Jde o návrhové hypotézy, nikoli žebříček prokázaně účinných funkcí. Body, série dní, avatary ani žebříčky nemají univerzální vzdělávací účinek. Herní měnu odděl od dokladů učení. Běžná chyba nemá spotřebovat přístup k výuce. Vyhni se tlaku přes propadající odměny, placené obnovení, nákup náhodných odměn nebo veřejné ponižování. To jsou návrhové zásady, nikoli tvrzení o experimentálním porovnání všech variant.

Obtížnost opři o cílové rozhodnutí. Náročnost čtení, motorická přesnost a časový tlak mohou zkreslit jeho měření. Rychlost používej, pokud je plynulost či reakční doba součástí cíle; přesnost a rychlost vyhodnocuj rozlišitelně. Neexistuje univerzální optimální procento úspěšnosti. Podporu upravuj podle více pozorování a umožni opravit nevhodné zařazení.

### Vzdělávací hry: Vytvoř průchod učením

Před rozsáhlou ekonomikou implementuj jeden hratelný problém. Po akci následuje srozumitelný důsledek, využitelná zpětná vazba, další příležitost a přirozené místo k ukončení. Chybu vysvětli na úrovni úlohy nebo strategie. Oslava sama neopraví chybnou představu.

Když chybějící znalost brání užitečnému pokusu, nabídni řešený příklad. Úvodní zkoumání může připravit následný výklad, ale produktivní neúspěch potřebuje navazující vysvětlení a propojení poznatků. Neospravedlňuje uvíznutí začátečníka. Rozlišuj seznamování, procvičování s pomocí a samostatné ověřování. Odhalení řešení označuje podporovaný pokus; později ověř jiný příklad.

Vybavování, rozložení a střídání přizpůsob úloze. Vracej i dříve správně zvládnutý obsah. Při vybavování požaduj rekonstrukci před odhalením odpovědi. Střídej případy vyžadující rozlišení a zvol odpovídající zpětnou vazbu. Pevný rozvrh intervalů neoznačuj za optimální pro každý obor a dobu uchování.

### Vzdělávací hry: Přizpůsob věku a zemi

Vycházej ze znalostí a potřeb podpory. U mladších žáků může pomoci konkrétní znázornění a podpora čtení; u středoškoláků porovnávání vysvětlení; u VŠ a dospělých oborová věrohodnost a pružné tempo. Jsou to výchozí hypotézy. Dospělý začátečník může potřebovat velkou podporu a zkušené dítě náročnější výzvu.

Prověř místní terminologii, zápis čísel a jednotek, směr čtení, kulturní odkazy, organizaci školy a dostupná zařízení. Kurikulum mapuj vůči určené zemi a verzi. Jazyk rozhraní neurčuje národní kurikulum. Podle situace zahrň sdílené zařízení a vedení učitelem. Simulace profesního úkonu neprokazuje praktickou způsobilost.

Zajisti klávesnici i alternativu k přetahování jedním ukazatelem, textové stavy vedle barvy a zvuku, viditelný fokus, ovladatelný pohyb a vhodné časování. Alternativní odpověď musí zachovat ověřovanou dovednost. Přístupnost a vhodnost věku ověřuj s cílovými uživateli; uvedení UDL nebo WCAG je nedokládá.

### Vzdělávací hry: Implementuj podle rozsahu

Krátké aktivitě stačí ověřený obsah, deterministická pravidla a stav relace. Lokální ukládání přidej, když má význam pokračování. U dlouhodobého produktu zvaž verze dovedností a úloh, podporované a samostatné pokusy, plán opakování, export, mazání a opravu učitelem. Účty, server i sledování chování potřebují konkrétní důvod.

Ukládaný pokus může obsahovat `skill_id`, `item_version`, `mode`, `support_used`, `response`, `result` a `feedback_version`. Uchovávej pouze potřebná pole; surové odpovědi a časy nemusí opustit zařízení. Měnu a vzhled postavy udržuj v herním stavu zvlášť. Výpadek sítě ani opakované odeslání nesmí zdvojit odměnu nebo změnit zaznamenané hodnocení.

U živé AI stanov zdroje, hranice hodnocení, náhradní chování a lidský přezkum. Ověř přesvědčivé chybné vysvětlení, ekvivalentní správnou odpověď a výpadek. Učení posuzuj i po odebrání pomoci. Výzkum konkrétních tutorů nedokládá přínos každého chatbota ani povinného čekání na pomoc. AI použitá při tvorbě nevyžaduje AI službu v produktu.

Při koordinaci specialistů nebo agentů sdílej stejný cíl, příklady úloh a pravidla důkazů. Odděl kontrolu oboru, výuky, hratelnosti a implementace. Rozpor řeš příkladem nebo zdrojem. Více person v jednom promptu není nezávislé ověření; samostatné agenty využij jen při autorizaci a skutečném přínosu.

### Vzdělávací hry: Ověř tři odlišné výsledky

1. Technické chování: správná i alternativní odpověď, chybná představa, tipování, odhalení, opakování, pokračování a případný výpadek. Úspěch s pomocí se nesmí skrytě změnit na samostatné zvládnutí.
2. Použitelnost a hraní: pozoruj první úkol a zotavení po chybě u cílových uživatelů. Zaznamenej nejasnosti, strategická rozhodnutí a možnost skončit. Malý pilot odhaluje problémy; neprokazuje populační účinek.
3. Učení: nová samostatná úloha, podle cíle uchování s odstupem a přenos mimo povrchové znaky hry. Pro srovnávací tvrzení použij věrohodnou alternativu se srovnatelným obsahem a časem; zohledni vstupní znalosti, odpadnutí a nerovnou účast. Uveď nejistotu. Čas v aplikaci a obliba nejsou dokladem učení.

Malému projektu stačí výuková hypotéza a proveditelný pilot. U produktu s významnými důsledky stanov výsledky a srovnání před sběrem dat. Herní metriky drž odděleně od vzdělávacích. Mechaniku změň či odeber, pokud podporuje obcházení, odrazuje od pomoci nebo přidává námahu bez užitečné role v učení.

### Vzdělávací hry: Zdroje a meze závěrů

- [Sailer a Homner, 2020](https://doi.org/10.1007/s10648-019-09498-w): metaanalýza podporuje průměrný přínos gamifikace s rozdíly mezi studiemi; motivační a behaviorální účinky byly při přísnějším posouzení kvality méně stabilní. Není to záruka pro konkrétní odznak či žebříček.
- [Clark a kol., 2016](https://doi.org/10.3102/0034654315582065): porovnání her a jejich úprav podporuje důraz na výukový návrh a opory. Médium samo neurčuje výsledek.
- [Li a kol., 2024](https://doi.org/10.1007/s11423-023-10337-7): malý průměrný přínos pro vnitřní motivaci ve 35 intervencích. Vnímaná kompetence se liší od měřeného zvládnutí učiva.
- [Habgood a Ainsworth, 2011](https://doi.org/10.1080/10508406.2010.508029): dvě studie jedné matematické hry podporují začlenění učiva do hlavní činnosti. Malé specifické vzorky neurčují univerzální recept.
- [Agarwal a kol., 2021](https://doi.org/10.1007/s10648-021-09595-9) a [Ruitenburg a kol., 2026](https://doi.org/10.1007/s10648-026-10225-5): školní výzkum vybavování a procvičování závislého na kontextu. Druhá práce rozlišuje vybavování, rozložení a střídání; malé skupiny pro některé moderátory omezují zobecnění.
- [Wisniewski a kol., 2020](https://doi.org/10.3389/fpsyg.2019.03087): účinky zpětné vazby se liší a záleží na využitelné informaci. [Sinha a Kapur, 2021](https://doi.org/10.3102/00346543211019105): řešení před výkladem může pomáhat při promyšleném provedení, s mezemi podle žáků a podmínek.
- [Almeida a kol., 2023](https://doi.org/10.1016/j.infsof.2022.107142): mapování popisuje hlášené nežádoucí účinky a obcházení. Počet negativních zpráv neudává četnost škodlivosti mechaniky.
- [MIT / Learning Games Network, 2015](https://education.mit.edu/wp-content/uploads/2018/10/BalancedDesignGuide2015.pdf): návrhový rámec propojení cíle, činnosti a důkazu. [George Fan, GDC 2012](https://media.gdcvault.com/gdc2012/slides/Design%20Track/Fan_George_How%20I%20Got.pdf): zkušenosti autora s hratelným uvedením do hry. Oba zdroje pomáhají návrhu; neposkytují kauzální odhad vzdělávací účinnosti.
- [Bastani a kol., 2025](https://doi.org/10.1073/pnas.2422633122) a [Kestin a kol., 2025](https://doi.org/10.1038/s41598-025-97652-6): různé experimenty ukazují význam návrhu tutora a samostatného výkonu. Liší se populace, učivo i intervence.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) obsahuje kritéria přístupnosti; [CAST UDL 3.0](https://udlguidelines.cast.org/) návrhový rámec. Jejich role se liší od experimentů s učením.

### Vzdělávací hry: Propoj prožitek, pravidla a přenos

MDA použij jako návrhový pohled: popiš zamýšlený prožitek, očekávané chování hráče a pravidla, která ho umožní. Objevování může potřebovat ovladatelný model a smysluplná pozorování; sebevyjádření více platných konstrukcí. Neomezuj všechny obory na jeden herní žánr. SDT pomáhá sledovat autonomii, kompetenci a vztahy; MDA ani označení z Octalysis nedokládají účinnost.

U otevřené konstrukční hádanky vymez omezení a ověřitelný úspěch bez vynucení jediného autorova řešení. Nabídni porovnání vlastních platných návrhů podle relevantních protichůdných kritérií, například spotřeby zdrojů a přesnosti. Komunitní histogram potřebuje skutečná vhodná data a volitelné sdílení; rozdělení nevymýšlej. Optimalizace nemusí přinášet herní měnu.

Propoj herní reprezentace s oborovým zápisem či skutečným rozhodováním a ověř nový případ mimo povrchové znaky hry. Nevnucuj všem rozdělenou obrazovku ani tři etapy. Odezva hry má objasnit podstatnou změnu bez zakrytí uvažování. Série dní a odměny mají být volitelné a bez trestání; přerušení nesmí odebrat doklady učení ani pomoc. Veřejný pokrok vyžaduje volbu sdílení.

[MDA autorů Hunicke, LeBlanc a Zubek](https://www.cs.northwestern.edu/~hunicke/MDA.pdf) je návrhový rámec. Výše uvedené studie her mají různé populace a výsledky; údaje o návratnosti uživatelů nezaměňuj za přírůstky učení.

## Reference: dialog-navrhu

Zdrojový oddíl: Dialog při návrhu vzdělávání


Použij při první podstatné pedagogické volbě a při změně požadavků či důkazů, která ji znovu otevírá. Jde o návrhový postup, nikoli experimentální tvrzení o učení.

### Dialog návrhu: Rozliš účastníka a podmínky učení

Věk, školní role a zkušenost jsou různé údaje. „Dítě“ popisuje věkový kontext, „žák“ obvykle školní roli a „student“ studijní prostředí; kategorie se mohou překrývat. V obecném návrhu používej „učící se člověk“ nebo „účastník“, v konkrétní aplikaci přirozené místní označení. Výskyty slova „žák“ ve školních příkladech neomezují celý skill na děti. V přímých pokynech často stačí „Vyzkoušej“, „Vysvětli“ nebo „Porovnej“ bez označování člověka.

Před výběrem metody vytvoř stručný pracovní profil z dostupného kontextu: věková skupina a vzdělávací prostředí; vstupní znalosti konkrétního tématu; čtení a jazyk; samostatnost a dostupná pomoc; cíl a důsledky hodnocení; zařízení a funkční potřeby přístupu. Jde o návrhové údaje o cílové skupině, nikoli povinný osobní profil. Nepotřebuješ datum narození, diagnózu ani celý školní záznam. Neznámé označ jako neznámé nebo předpoklad; neodvozuj je ze samotného slova „student“.

| Kontext a vhodné pojmenování | Co před návrhem ověřit | Možná úprava, pokud odpovídá potřebě |
| --- | --- | --- |
| Předškolní dítě, pokud je zadání zahrnuje | Čtení, ovládání, doprovod dospělého a smysl obrazovkové činnosti | Názorná krátká instrukce, společná hra a činnost mimo displej; nepředpokládat samostatné čtení |
| Žák prvního stupně nebo místní obdoby | Znalost pojmů a zápisu, čtení zadání, zařízení | Konkrétní reprezentace propojená s pojmem, předvedení ovládání, dostupná opora |
| Žák druhého stupně nebo místní obdoby | Předpoklady učiva, rozdíly ve třídě, práce ve skupině | Porovnávání postupů, vysvětlení a volba podpory při společném cíli |
| Středoškolák, žák či student podle místního použití | Všeobecný nebo odborný obor, zkušenost, účel hodnocení | Oborový problém, argumentace nebo profesní scénář; simulace nenahradí praktické ověření |
| Student VŠ | Oborové předpoklady a zkušenost s konkrétním tématem | Autentická úloha, práce s důkazy, více řešení; u nového tématu stále dostupný příklad |
| Dospělý účastník kurzu, samouk či pracovník | Vlastní cíl, praxe, čas a použití v životě nebo práci | Relevantní situace, možnost přeskočit známé, pružné tempo a návrat k práci |
| Starší dospělý, pokud je tato informace relevantní | Individuální zkušenost, jazyk, ovládání a potřeby přístupu | Úpravy textu, času či ovládání podle potřeby; věk sám neznamená malou digitální zkušenost |
| Smíšená skupina | Které potřeby jsou společné a které vyžadují varianty | Společný cíl, volitelná opora, různé vstupní úlohy a samostatné doklady |

Řádky jsou návrhové možnosti, nikoli vývojová diagnóza nebo povinné přiřazení metod podle věku. Stupně škol a názvy ročníků se mezi zeměmi liší. Dítě může být v tématu pokročilé a dospělý začátečník. Jazyková podpora, přístupnost a rozdílné tempo se týkají všech skupin. Nepřiřazuj pevné vizuální, sluchové či jiné učební styly.

Rozliš, kdo se učí, kdo aplikaci obsluhuje a kdo vidí výsledky: učitel může vést společnou tabuli, rodič doprovázet dítě a tvůrce nemusí být ani jeden z nich. Zařazení mezi děti automaticky neurčuje sdílení výsledků s kýmkoli. Potřebné role a rozsah přístupu vymez podle skutečného použití.

Pokud údaj chybí a mění návrh, zeptej se například: „Pro koho je aktivita určena: děti na prvním stupni, starší školáky, nebo dospělé začátečníky? Co už v tématu zvládají?“ Nabídku uprav podle zadání, nevypisuj pokaždé všechny skupiny a známé údaje se znovu neptej. Při nejasném slově „studenti“ nejprve ověř prostředí, pokud ovlivní výsledek.

U nabídky metody řekni, komu a proč v tomto projektu pomůže. Například „Pro dospělé začátečníky doporučuji vysvětlený příklad z jejich práce; podporu pak ubereme podle samostatných pokusů.“ U zkušených dětí může být vhodnější otevřená výzva. Změna cílové skupiny znovu otevírá dotčený jazyk, obsah, oporu, hodnocení a ovládání, nikoli automaticky celý projekt.


### Dialog návrhu: Nabídni možnosti v okamžiku potřeby

Převezmi známé uživatele, vstupní znalosti, cíl, zemi, zařízení, čas a omezení. Ptej se na chybějící údaj, jen pokud mění rozhodnutí. Výchozí je průběžné vedení. Tvůrce může delegovat jednu volbu nebo další běžná rozhodnutí a později vedení obnovit.

| Spouštěč | Relevantní možnosti k vysvětlení |
| --- | --- |
| Cíl a první činnost | Řešený příklad s ubíráním pomoci, řízené bádání, vybavování, konstrukce či autentický projekt |
| Motivace a účast | Vlastní pokrok, smysluplná volba, kooperativní role, volitelné herní prvky |
| Chyby a pomoc | Cílená nápověda, kontrastní příklad, přímé vysvětlení a další pokus |
| Hodnocení | Formativní zpětná vazba, kriteriální rubrika, samostatné ověření, portfolio či připravené vrstevnické hodnocení |
| Pokračování | Stav relace, lokální pokračování, opakování s odstupem či kalibrovaná obtížnost |
| Zjištění z prototypu | Oprava zavádějící reprezentace, omezení opory, přenos nebo odstranění obcházené odměny |

Jde o příležitosti, ne povinné zastávky. V malém projektu spoj související volby. Nabídni jen proveditelné možnosti: krátký popis, příklad v aplikaci a podstatnou náročnost, datovou potřebu či omezení. Doporuč variantu a polož jednu konkrétní otázku. Podle situace umožni jednoduchou verzi nebo odložení; nevyžaduj znalost odborných názvů. Další metody rozveď na žádost.

### Dialog návrhu: Pamatuj si rozhodnutí

Malé práci stačí rozhovor; u delší využij existující návrhový záznam projektu. Uchovej cíl, omezení, ID metody, důvod, stav, odmítnuté alternativy a otevřené otázky. Možné stavy: `offered`, `selected`, `implemented`, `verified`, `deferred`, `declined`. Záznam drž odděleně od údajů žáků. Změna požadavku otevírá jen dotčené volby; vysvětli proč. Neodpovězení není výběr. Během čekání na zásadní volbu pokračuj v nezávislé práci.

### Dialog návrhu: Od volby k produktu

Použij činnost, důkaz, podporu a kontrolu z karty metody. Vytvoř související průchod a vysvětli neslučitelné volby. Řešený příklad může předcházet pozdějšímu vybavování; produktivní neúspěch potřebuje následné uspořádání a vysvětlení. Ani jedno neznamená testovat na každé obrazovce.

U offline aktivity se zlomky: „Doporučuji skládání dílků se souvisejícím zápisem, protože cílem je stejná hodnota různých zlomků. Číselná osa zvýrazní stejnou polohu; doplňování řešeného příkladu poskytne větší počáteční oporu. Který způsob má být hlavní?“ Později nabídni nový úkol bez dílků nebo rozbor chyby k ověření přenosu. Úvodní rozhovor neopakuj.

Tvůrce si objednává aplikaci. Neměň rozhovor na povinné doučování, programátorský domácí úkol ani nedokončená TODO. Při předání ukaž realizaci zvolených metod, provedené kontroly a nejistoty. Automatické vyvolání skillu závisí na hostiteli; testuj ho odděleně od chování po načtení.

## Reference: kognitivni-rozhrani

Zdrojový oddíl: Kognitivní rozhraní a reprezentace


Čti při návrhu diagramů, multimédií, instrukcí, umístění zpětné vazby nebo rozhraní, které může zakrýt učební úkol. Vycházej z uživatelů a zařízení, nikoli pevného vizuálního stylu.

### Kognitivní rozhraní: Soustřeď pozornost na rozhodnutí

Při náročné práci omez nesouvisející pohyb a zvuk; zachovej potřebný kontext a ovládání. Související popisky a vysvětlení umísti blízko objektu, aniž ho zakryjí. Na malé obrazovce použij propojené zvýraznění, přístupný popis nebo postupné zobrazení, pokud sousední umístění není praktické. Samotná barva nesmí nést rozlišení.

Složitou operaci rozděl do kroků řízených žákem. Neznámé ovládání a pojmy představ před jejich kombinováním. Zkušeným zachovej přímou cestu a možnost vrátit se k pomoci. Animace má objasnit změnu nebo akci; poskytni omezení pohybu a stejně srozumitelný statický stav.

### Kognitivní rozhraní: Propoj reprezentace a ověř přenos

Pokud konkrétní objekty podporují abstraktní pojem, ukaž stejný vztah v objektech, diagramu a oborovém zápisu. Vysvětli propojení a zadej nové použití s menší povrchovou oporou. Rozdělená obrazovka je jedna možnost, nikoli povinnost. Zachovej rovnocennou cestu klávesnicí a bez přetahování. Ověř, že nelze uspět jen párováním barev nebo poloh.

Příklad: manipulace stejnými množstvími, odpovídající rovnost a vysvětlení, proč platí; později nová rovnost bez pomůcky. Zkušený žák může začít zápisem. Reprezentaci vrať, pokud pomůže. V jiném oboru může přenos znamenat posouzení nového zdroje nebo použití postupu v jiné situaci.

### Kognitivní rozhraní: Zachovej přístup a smysluplné důkazy

Omez zbytečně souběžné proudy informací, ale zachovej titulky, přepis, opakované přehrání, jazykovou podporu a přístup čtečkou. Princip redundance nezakazuje text vedle audia. Neschovávej nezbytné instrukce do nápovědy dostupné jen najetím myši. Pokud je zvuk či čas součástí ověřované dovednosti, vymez podmínky a posuď úpravy přístupu.

U konceptuální kontroly může dobrovolný odhad jistoty pomoci porovnat přesvědčení s výkonem. Nezaměňuj jistotu za zvládnutí a nevyžaduj ji po každé akci. Zpětná vazba má vysvětlit podstatný rozdíl a umožnit použití opravy; nevyráběj překvapení ani pochybnost o správném postupu.

Ověř čitelnost popisků, pořadí fokusu, zvětšení, úzký displej, omezení pohybu a celý průchod pomocí a novým pokusem. Posuzuj činnost žáka, ne jen vzhled komponent. Neprovedené kontroly přiznej.

### Kognitivní rozhraní: Zdroje a meze

[Waxman & Goldie, 2023](https://media.repository.chds.hsph.harvard.edu/static/filer_public/ca/62/ca625803-3d73-4855-b3e1-765870ce3772/2023_jwaxman_monograph_cogtheory_multimed.pdf) podporuje návrhová rozhodnutí, nikoli univerzální zákazy uspořádání. [Matlen a Devlin, 2020](https://web.stanford.edu/~kdevlin/Papers/Matlen-Devlin_CHI2020.pdf) popisují raný koncept přenosu, ne ověření každé rozdělené obrazovky. [W3C k titulkům](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html) vysvětluje podmínky přístupnosti. Pro cílové vydání ověř aktuální normativní požadavky.

## Reference: adaptivni-procvicovani

Zdrojový oddíl: Adaptivní procvičování a pokračování učení


Čti pro opakované relace, plánování nebo výběr obtížnosti. Rozliš kdy opakovat, kterou úlohu zadat a kolik pomoci nabídnout. Nemusí je řídit stejný model.

| Potřeba | Malé provedení | Volitelné rozšíření a předpoklady |
| --- | --- | --- |
| Jedna aktivita | Ověřené úlohy, zřetelná posloupnost, pomoc a stav relace | Obvykle bez trvalého modelu žáka |
| Vybavení po dnech | Výslovný plán návratů a lokální historie | FSRS pro stabilní položky a srozumitelné záznamy opakování |
| Výběr obtížnosti | Ověřené úrovně úloh a průhledné větvení | Elo s vhodnými daty odpovědí, nejistotou a kalibrací |
| Návaznost dovedností | Mapa dovedností se samostatnými doklady | BKT nebo IRT jen se zdůvodněným modelem, daty a ověřením |
| Dlouhodobý plán | Cíl, dostupný čas, aktuální etapa a další úkol | Revidovatelné milníky, otevřené otázky a termíny návratu |

Vysvětli funkci před algoritmem. Zachovej stack projektu; nepřidávej plánovač, server ani účty jen kvůli jejich uvedení zde. Jednoduchá pravidla jsou legitimní s popsanými mezemi. HLR je další trénovaný model vybavení pro vhodná data, nikoli výchozí implementační požadavek.

### Adaptivní procvičování: Podmínky před adaptací

Vymez stabilní ID položek a dovedností, verze obsahu, interpretaci odpovědi a podmínky pomoci. Rozliš tipnutí, podporu, odhalení a samostatnou odpověď. Dodrž význam hodnocení zvolené knihovny; nepovažuj tiše každou podpořenou odpověď za samostatné vybavení. Herní měnu odděl od modelu učení. Uchovávej minimum dat a časy jen tam, kde je plánování potřebuje.

Urči počáteční chování a použitelnou náhradu při chybějící, poškozené nebo zastaralé historii. Předpoklady ověř na reprezentativních datech včetně jazyka a přístupnosti. Umožni opravu učitelem a přístup k pomoci. Predikce úspěchu je nejistá; univerzální cíl 80–90 % úspěšnosti ani dvě správné odpovědi neměří ZPD a neprokazují zvládnutí. Cílová retence je volba mezi zátěží a očekávaným vybavením, nikoli záruka výsledku.

Při výběru algoritmu využij udržovanou implementaci s ověřenou verzí. Prověř aktualizace, časová pásma a přelom dne, duplicitní odeslání, změnu obsahu, export a obnovu i neplatná data. Rozšíření porovnej s jednoduchým základem; přesnost predikce, zapojení a učení jsou odlišné výsledky. Z času odpovědi neodvozuj diagnózu ani osobnost.

### Adaptivní procvičování: Uzavření a obnovení etapy

Zaznamenej výsledek, podmínky pomoci, otevřené otázky a proveditelný další krok. Dokončení etapy odliš od doloženého zvládnutí. Vytvoření další etapy automaticky nedokončuje předchozí. Shrnutí zachová potřebné odkazy na důkazy a nejistotu, nikoli celé přepisy. Po návratu přiměřenou úlohou ověř zastaralé předpoklady; přerušení nemaže pokrok.

### Adaptivní procvičování: Zdroje

[Dokumentace Anki FSRS](https://docs.ankiweb.net/manual/deck-options), [Pelánek o vzdělávacím Elo](https://www.fi.muni.cz/~xpelanek/publications/CAE-elo.pdf) a [Settles a Meeder o HLR](https://research.duolingo.com/papers/settles.acl16.pdf). Popisují konkrétní modely a prostředí, ne účinnost nové aplikace. Při integraci knihovny ověř její aktuální dokumentaci.

## Licenční oznámení

```text
MIT License

Copyright (c) 2026 Luděk Sušický

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
