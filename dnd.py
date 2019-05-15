#DnD generator
#I wrote this just after I first learned python


import random
import math
import tkinter as tk


def dungeonmap(name):
    #name(str): name of dungeon
    #everything else random
    2+2
  



def dungeon():
    list1=["Fell ", "Dire ", "Black ", "Red ", "Snow ", "Sand ", "Death ", "Bone ", "Orb ", "Dark ",
           "Whispering ", "Evil ", "Genie ", "Demon ", "Celestial ", "Lich ", "Magpie ", "Ghastly ",
           "Lower ", "Necro", "Wooden ", "Ice ", "Blood ", "Mage ", "Gehenna ", "Acheron ", "Carceri ",
           "Bleak ", "Empty ", "Spear ", "Lost ", "Big ", "Little ", "Frozen ", "Great ", "Adjective ", "", "Skull ",
           "King's ", "Orc's ", "Elven ", "Stark ", "Flooded ", "Burned ", "Huge ", "Eight-Inch ", "First ",
           "Last ", "Fire ", "Water ", "Air ", "Earth ", "Lawful ", "Chaotic ", "Mechanus ", "Pandemonium ",
           "Crag ", "Mt. ", "Saint's ", "Wizards' ", "Laughing ", "Fighting ", "Gold ", "Dwarven ", "Outsider ",
           "Crow ", "Ibis ", "Wolf ", "Monkey ", "Dog ", "Tiger ", "Palm ", "Bronze ", "Ticklish ", "Well-engineered ",
           "Ethereal ","Hungering ", "Hungry ", "Angry ", "Careless ", "Angsty ", "Crippled ", "Furious ", "Uttering ",
           "Yelling ", "Rebel ", "Murmuring ", "Mistaken ", "Forgotten ", "Desecrated ", "Hallowed ", "Holy ",
           "Unholy ", "Blasphemous ", "Overgrown ", "Reclaimed ", "Draconic ", "Uneasy ", "Cursed ", "Mad ",
           "Scalding ", "Brimstone ", "Skirling ", "Upper ", "Wispy ", "Lazy ", "Nauseous ", "Foul ", "Perilous ",
           "Vile ", "Awful ", "Squalid ", "Hideous ", "Beautiful ", "Gigantic ", "Spooky ", "Crashing ","Shrieking ","Fallen "]
    list2=["Falls ", "Gate ", "Hill ", "Hills ", "Storm ", "Portal ", "Rest ", "Singer ", "Sword ", "Spell ",
           "Doom ", "Mountain ", "River ", "Woods ", "Shrub ", "Beach ", "Bones ", "Tyrant ", "Devil's ",
           "Thunder ", "Noun ", "Glacier ", "Dune ", "Hedge ", "Grace ", "Whisper ", "Skull ", "Inn ", "Watch ",
           "Widow ",  "Boulder ","","","",
           "Tibula ", "Tribute ", "Hound ", "Lightning ", "Comet ", "Meteor ", "Star ", "Circle ", "Gash ", "Fist ",
           "Bow ", "Master ", "Sorcerer ", "Soldier ", "Ranger ", "", "Warlock ", "Angel ", "Elemental ", "Stalagmite "
           ,"Stalactite ", "Fissure ", "Elephant ", "Saddle ", "Rapids ", "Thinker ", "Love ", "Dream ", "Joy ",
           "Ash ", "Collapse ", "Tooth ", "Knuckle ", "Hyena ", "Retaining ", "Hag ","Illusion ", "Raid ", "Bee ", "Dragon ",
           "Sun ", "Saviour ", "Disciple ", "Night ", "Knight ", "Vampire ", "Warg ", "Lady ", "Prince ", "Merchant ",
           "Lord ","Horse ", "Siege ", "Battle ", "Skirmish ", "Hurricane ", "War ", "Curse ", "Bear ", "Lava ", "Blizzard "
           ,"Debate ", "Fight ", "Eyeball ", "Ghost ", "Rock ", "Sand ", "Gravel ", "Lamp ", "Owlbear "]
    list3=["Barrow", "Tomb", "Rest", "Catacombs", "Tunnels", "Cave", "Caverns", "Wall", "Tower","Base"
           ,"Outpost","Lair","Crevice","Crevasse","House","Monastery","Lookout","Hole","Sinkhole",
           "Ruins","Relic","Bridge","Gateway","Sea Cave","Underground River","Castle","Fortress","Motte",
           "Village","Hideout","Warehouse","Sewer","Dungeon","Stronghold", "Hive","Deep Road","Underdark Cave",
           "Pass","Outlook","Graveyard","Crypt","Prison","Ward","Barracks","Standing Stones","Ritual Circle",
           "Summoner's Circle","Rift","Planar Rift","Water Cave","Grave","Pyramid","Ziggurat","Temple","Cathedral"
           ,"Laboratory","Mage Tower","Library","Repository","Maze","Archive","Labyrinth","Tombs","Crypts","Burial Ground",
           "Caves","Cavern","Passage"]

    int1=random.randint(0,len(list1))-1
    int2=random.randint(0,len(list2))-1
    int3=random.randint(0,len(list3))-1
    
    output=str(list1[int1]+list2[int2]+list3[int3])
    #print(output)

    return(output)



     
def character(verbose=0):
     man1=["Bob","Fred","Jon","Ben","Luc","Tar","Von","Ran","Ray","Res","Len","Dar","Sam",
           "San","Der","Ol","Torr","Hen","Her","Gen","Skal","Yan","Yi","Les","Jo","Joh","Mat",
           "Ma","Mo","Ta","Adra","Mel","Shas","Warr","Wagna","Si","Lar","Lan","Dy","Ar","Joff",
           "Ty","An","Ed","Edd","Eddy","Tan","Lau","Ron","Rio","Ley","Man","This","Theo","Bri","Bree",
           "Bred","Bren","En","Lew","Jes","Ami","Tav","Tarr","Ulf","Olf","Ilte","Jak","Lak","Kyr","Lach",
           "Dach","Ham","Abr","Meli","Re","Ra","Ran","Yol","Eir","Eo","Hay","Hae","Thae","Ty","Ky","Val","Ea",
           "Rad","Nar","Nal","Lal","Lay","Nik","The","Che","Chas","Chan","Shan","Sat","An","Mad","Dan","Dane",
           "Kor","Sten","Sven","Stan","El","En","Em","Kev","Ead","Ung","Kler","Serg","Seto","Samm","Sal","Een",
           "Oph","Top","Tou","Teth","Ket","Ze","Zay",'Zan',"Jey","Jai","Jye",'Kye',"Greg",'Gren','Gres','Gre',
           'Get','Aul','Mard','Marv','Mark','Cark','Carn','Darn','Darl','E',"A",'O','I','U',"Pa",'Pal',"Paul"]
     
     male=["fred","nian","bert","ter","gen","ren","len","lan","ler","saz","bald","leo","ten",
           "wen","der","wel","del","sel","tel","ham","teth","then","tre","dre","dred","drew",
           "tres","trew","wert","bes","ello","lo","ror","mond","mun","mon","nick","k","man","rhen","dold","rold","yan","yeo"
           ,"zil","tyso","las","sac", "ss","rovan","m","n","an","er","ew","hern","ican","sy","c","in","el","es","ken","ler","ty",
           "ee","lo","ko","pin","op","s","","","",""]
     
     female=["fred","lie","tie","die","tre","trie","tra","sdra","ai","asha","oa","iah","lah","mia","my","sie","sica","ya",
             "sa","sasy","ly","see","anna","i","ie","ia","my","mie","ye","au","aia","alla","ana","li","cha","che","ren","wen",
             "ulie","brin","erl","gred","a","tai","ae","ii","e","kea","lia","ea","lea","nie","cie","cy","y","mee"]
             
     commoner=["Smith","Waterman","Goodman","Mace","Foote","Cooper","Reeve","Headman","Stone",
               "Snow","Mason","Crofter","Tree","Hounder","Ween","Speekes","Longleg","Speere","Deerman",
               "Handy","Stable","Tender","Well","Digger","Tumble","Lame","Rice","Oakes","Olds","Starman",
               "Wiseman","Wisher","Lorn","Crawley","Hoofter","Poole","Drifter","Grass","Ley","Helman",
               "Stag","Fisher","Outman","Creepe","Letterman","Rivers","the Red","Antkeeper","Whitefoot",
               "Bighead","Beeren","Brewer","Linger","Speller","Bridger","Rocke","Toole","Barton","Innes",
               "Dayne","Forth","Abramelin","Priestly","Dolf","Sailor","the Blue","the Giant","Onehand","Storm",
               "Six-Fingers","the Big","the Third","Scarface","Melon","Langer","Clanger","Walker","Carter","Porter",
               "Page","Squire","Deep","Tuna","Cropp","Crane","Reamer","Long","Short","Waves","Baker","Bredd","Axman",
               "the Shifty","Cutter","Logger","Spellweaver","Shorthand","Tiny-Hands","the Orange","the Green",'the Wall'
               ,"the Brick","Meathead","Sheepthief","Doglover","Kennelman","Sewer-Sweeper","Ashe","Ashford",'Talltree',
               'Bigman','Pigg','Toastbaker','Left-Foot','Fast-Brain','Quickeye','Hawk','the Sad','the Jolly','Addisen',
               'Upwell','Durce','Reaper','Greybeard','the Walrus','the Mule','the Fast','the Furious','Pennypincher',
               'Jester','Drumm','Swig','Twiggy','Orefinder','Ogreslayer','Dreamseer','Mageson','Magehand','Wheate']
     
     nobleman=["Balmoral","Thorne","Windrun","Preston","Carnegie","Durlamie","Torrens","Diamac","Redford",
               "Ford","Woomba","Ries","Laynor","Tierbal","Andron","Brien","Cassior","Drewen","Erath","Fostor",
               "Grandchester","Higgins","Jertis","Kostello","Lerrden","Mistine","Newpart","Overell","Prattis","Questor",
               "Richards","Sandforth","Trent","Unnaver","Wester","Xaxob","Yirned","Zerag","Akbart","Biste",
               "Clancy","Danji","Eobard","Fassted","Ghetsis","Hilmenor","Inshore","Jolian","Karloh","Lewyn",
               "Melina","Northropp","Obrams","Passtree","Quint","Redwater","Sandoval","Tassell","Underhill",
               "Ventra","Willow","Yertle","Zratto"]

     personality=["Selfish","Obsequious","Drowsy","Bookish","Observant","Not observant","Critical","Lazy","Art lover",
                  "Hobbyist","Book collector","Big spender","Cheapskate","Pessimist","Optimist","Alcoholic","Puritanical",
                  "Polite","Rude","Jumpy","Aloof","Arrogant","Individualist","Conformist","Hot tempered","Calm","Jealous",
                  "Brave","Cowardly","Careless","Curious","Truthful","Liar","Energetic","Pious","Atheist","Strong political views",
                  "Racist against elves","Hates racism","Paranoid","Moody","Angsty","Happy","Uses big words","Quiet",
                  "Interested in magic","Comedian", "Interested in the planes", "Interested in history","Dutiful"]

     appearance=["Scar on face","Missing tooth","Missing finger","Bad breath","Bad smelling","Perfumed","Sweaty","Fat",
                 "Thin","Shaky hands","Coughs","Sneezes","Hiccups","Loud voice","Quiet voice","Pale eyes","Pale skin","Dark eyes",
                 "Distinctive brithmark","Unusual hair colour","Tattoo","Shaven head","Long hair","Lazy eye","Whistles a lot","Sings a lot",
                 "Stands tall","Tall","Short","Bad skin","Attractive","Ugly","Dirty","Clean","Big nose","Big hands","Small hands", "Silky hair",
                 "Strong jawline", "Prominent chin", "High cheek bones"]

     talent=["Plays the lute","Plays the drums","Plays the flute","Plays the triangle","Speaks in tongues sometimes",
             "Speaks elven languages","Speaks dwarven languages","Speaks Abyssal", "Speaks Celestial","Speaks Aquan",
             "Speaks Draconic", "Has great luck", "Irresistible to men", "Irresistible to women", "Irresistible to mozzies",
             "Photographic memory","Very intelligent", "Very charismatic", "Very attractive", "Very fit", "Huge appetite",
             "Animal lover","Has a pet shocker lizard", "Good with children", "Great at chess","Good at impressions",
             "Fast runner", "Draws beautifully", "Skilled painter", "Drinks everyone under the table", "High-pitched voice",
             "Expert carpenter","Expert artisan","Knows 5 or so cantrips","Expert cook", "Can skip stones like 10 times",
             "Excellent actor","Skilled dancer", "Skilled trickster","Can throw cards", "Strong puncher","Strong immune system",
             "Unnatural eye colour","Has a tiny bit of dragon blood", "Has a tiny bit of fiend blood", "Has a tiny bit of celestial blood"
             ,"Well read","Sees the future in their dreams", "Can sense supernatural creatures", "Can lick own elbow"]



     age=random.randint(12,70)

     gender=random.randint(1,2)
     classs=random.randint(1,2)

     int1=random.randint(0,len(man1))-1
     int2=random.randint(0,len(male))-1
     int3=random.randint(0,len(female))-1
     int4=random.randint(0,len(nobleman))-1
     int5=random.randint(0,len(commoner))-1
     int6=random.randint(0,len(personality))-1
     int7=random.randint(0,len(appearance))-1
     int8=random.randint(0,len(talent))-1

     if gender==1:
          name1=man1[int1]+male[int2]
     else:
          name1=man1[int1]+female[int3]

     if classs==1:
          name=name1+", of House "+nobleman[int4]
     else:
          name=name1+" "+commoner[int5]


     
     
     if verbose==1:
         print(name)
         
         print("    Age "+str(age))
         print("   ",personality[int6])
         print("   ",appearance[int7])
         print("   ",talent[int8])
  

     return name


def town():
    pop=(int)(6000/math.log(random.randint(1,50)))
    name="treesworth"
    ruler=character(0)


    print("the town of ",name,"controlled by ", ruler,"population of ", pop)
        
     

def artifact():
    list1=["Thunder","Rage","Joy",'Light','Agony','Wonder','Laughter','Fear','Wave','Storm','Flame','Fire','Power',
           'Hate','Love','Terror','Red','Blood','Comet','Storm','Meteor','Lightning','Acid','Bile','Mystery','Death','Doom',
           'Will','Bone','Energy','Life','Skull','Hand','Lich','Dragon','Bane','Whisper','Lost','Wail','Red','Orange','Yellow','Green',
           'Blue','Indigo','Violet','Sun','Moon','Star','Tree','Plant','Dog','Monster','Night','Knight','Dawn','Dusk','Day','Evening',
           'Prince','Leaf','Heart','Hammer','Knuckle','Song']
    list2=['fury','doom','bane','killer','hustler','crusher','slayer','vanquish','bringer','hand','seer','destroyer','wing','king',
           'death','light','razor','saver','blade','striker','slasher','maul','great','joy','tool','toy','stabber','sickle','reaper','flayer',
           'mauler','screamer','lifter','breaker','mover','brute','thinker','dream','sleeper','mind','crystal','stone','smasher']
    list3=['Spear','Short Sword','Longsword','Bastard Sword','Greatsword','Lance','Javelin','Pike','Quarterstaff','Thirdstaff',
           '10-foot Pole','Light Pick','Heavy Pick','Pick Hammer','Two-headed Pick','Warhammer','Sledgehammer',
           'One-handed Axe','Longaxe','Greataxe','Light Mace','Heavy Mace','Morningstar','Flail','Club','Shiv','Dagger',
           'Dual Swords','Rapier','1-metre Sword','Swordstaff','Staff','Wand','Orb','Cube','Crown','Whip','Sphere',
           'Idol','Focus','Rod','Shortbow','Longbow','Light Crossbow','Full-auto Crossbow']
    list4=['Goblins','Humans','Men','Elves','Ancient Humans','Dwarves','Ancient Dwarves','Ancient Elves','Hobgoblins',
           'Mind Flayers','Knights','Holy Order of Thuss','Order of the Crying Monkey','Kobolds','Lephantians','Kuo-toa',
           'Astral Fliers','Birdmen','Lizardmen','Reptilians','Dragons','Dragonborn','Paladins','Sorcerers','Wizards','Rangers',
           'Halflings','Gnomes','Bards','Order of the Last Sunset','Order of Saint Danetyso','Order of Lady Eoua','Order of Pelor',
           'Reptilian Priests','Goblin Kings','Elven Lords','Reptilian Sun-Kings','Dwarven Kings','Human Kings','Human Lords',
           'Cupbearers','Wordbearers','Hierophants','Bloodtyrants','Lich-Lord','Sun-Priest','Dark Ones','Outsiders',
           'Demon Cultists','Celestial Guardians','Guardians','Survivors','Farmers','Peasants','Communists','Sorcerer-Kings',
           'Order of Sir Narty Preston','Scientists','Engineers','Sages',"Abylonians","Miraanis","Mak Citizens"]


    int1=random.randint(0,len(list1))-1
    int2=random.randint(0,len(list2))-1
    int3=random.randint(0,len(list3))-1
    int4=random.randint(0,len(list4))-1

    name=list1[int1]+list2[int2]+', '+list3[int3]+' of the '+list4[int4]
    #print(name)
    return(name)

def madlibs():
    characte=character(0)
    characte2=character(0)
    artifac=artifact()
    dungeo=dungeon()
    dungeo2=dungeon()

    form=random.randint(1,9)

    if form==1:
        print()
        print("You are approached by",characte,"to recover the legendary",artifac,"from",dungeo)
        print()
        dungeonmap(dungeo)
    elif form==2:
        print()
        print("A local leader,",characte,"offers a reward if you can clear out",dungeo)
        print()
        dungeonmap(dungeo)

    elif form==3:
        print()
        print("Local adventurer and hero,",characte,"has gone missing and their friend,",characte2,
              "wants to get them back. They were last seen near",dungeo)
        print()
        dungeonmap(dungeo)

    elif form==4:
        print()
        print("The inhabitants of two local ruins,",dungeo,"and",dungeo2,"are engaged in a turf war. Local leader",
              characte,"is offering a reward if anyone can stop them fighting or clear both out.")
        print()
    elif form==5:
        print()
        print("A bandit chief known as",characte,"wielding the powerful artifact",artifac,"is terrorising the area. "
              "Local leader,",characte2,"offers a bounty if the bandit chief is killed. The bandits' lair is known to be in",dungeo+".")
        print()
    elif form==6:
        print()
        print("A local merchant,",characte,"wants you to hide their treasured artifact",artifac,"in the monster-infested ruins of",
              dungeo,"for safekeeping. However their competitor,",characte2,"offers a reward if you bring the artifact straight to them.")
        print()
    elif form==7:
        print()
        print("The people of a town have hired you to investigate someone,",characte,"who is acting suspiciously. They have been"
              " making frequent night-time visits to the nearby ruins of",dungeo)
        print()
    elif form==8:
        print()
        print("The monstrous inhabitants of",dungeo,"want to start trading with a local village. However the leader of the village",
              characte,"wants you to sneak into",dungeo,"and find out what the monsters really want.")
        print()
    elif form==9:
        print()
        print("Local leader", characte,"wants you to sneak into the home of their enemy",characte2,"and steal their heirloom",
              artifac+".","When",characte2,"finds out they will blame the monsters in",dungeo,"and hire you to get the heirloom back from there.")
        print()

    
def main():
    while True:
        print()
        madlibs()
        a = str(input("Which one: dungeon d, character c, character (verbose) v, artifact a, town t "))
        b = input("num. of iterations")
        if b == "":
            b = 0
        else:
            b = int(b)
        
        count=0
        if a=="d":
            while count < b:
                print(dungeon())
                count += 1

        elif a=="c":
            while count < b:
                print(character(0))
                count += 1
                
        elif a=="v":
              
              while count<b:
                character(1)
                count+=1

        elif a=="t":
            while count<b:
                town()
                count+=1
            
        else:
            while count<b:
                print(artifact())
                count+=1
        dungeonmap('fff')


        



main()

          



    
