"""
Random League Team Generator Patch 10.6
idfk why i made this i regret it already
i dont comment code because i cant read

some notes
All Players will have boots :)
All junglers will have smite and jungle item, other players may have smite but no jungle item (for simplicity)
There is probably a 100% better way to do this but ultimate bravery was down and i had 30mins kicking around

probably will do a check for jg in the normal loop instead of the copy pasta, and just pop an item for jg item
"""

import random

champPool = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie",
                "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard", "Blitzcrank",
                "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath",
                "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise",
                "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio",
                "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim",
                "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV",
                "Jax", "Jayce", "Jhin", "Jinx", "KaiSa", "Kalista", "Karma", "Karthus",
                "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred",
                "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian",
                "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune",
                "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee",
                "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy",
                "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Renekton", "Rengar",
                "Riven", "Rumble", "Ryze", "Sejuani", "Senna", "Sett", "Shaco", "Shen", "Shyvana",
                "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra",
                "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle",
                "Tryndamere", "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar",
                "VelKoz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah",
                "Xerath", "Xin Zhao", "Yasuo", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]
itemPool = ["Abyssal Mask", "Adaptive Helm", "Archangel's Staff", "Ardent Censer", "Athene's Unholy Grail",
            "Banshee's Veil", "Black Cleaver ", "Black Mist Scythe", "Blade of the Ruined King",
            "Bloodthirster", "Bulwark of the Mountain", "Dead Man's Plate", "Death's Dance",
            "Duskblade of Draktharr", "Edge of Night", "Essence Reaver", "Frozen Heart",
            "Frozen Mallet", "Gargoyle Stoneplate", "Guardian Angel", "Guinsoo's Rageblade",
            "Hextech GLP-800", "Hextech Gunblade", "Hextech Protobelt-01", "Iceborn Gauntlet",
            "Infinity Edge", "Knight's Vow", "Liandry's Torment", "Lich Bane", "Locket of the Iron Solari",
            "Lord Dominik's Regards", "Luden's Echo", "Manamune", "Maw of Malmortius", "Mejai's Soulstealer",
            "Mercurial Scimitar", "Mikael's Crucible", "Morellonomicon", "Mortal Reminder", "Muramana",
            "Nashor's Tooth", "Pauldrons of Whiterock", "Phantom Dancer", "Rabadon's Deathcap",
            "Randuin's Omen", "Rapid Firecannon", "Ravenous Hydra", "Redemption", "Righteous Glory",
            "Rod of Ages", "Runaan's Hurricane", "Rylai's Crystal Scepter", "Sanguine Blade", "Seraph's Embrace",
            "Shard of True Ice", "Shurelya's Reverie", "Spellbinder", "Spirit Visage", "Statikk Shiv", "Sterak's Gage",
            "Stormrazor", "Sunfire Cape", "Thornmail", "Titanic Hydra", "Trinity Force", "Twin Shadows",
            "Umbral Glaive", "Void Staff", "Warmog's Armor", "Wit's End", "Youmuu's Ghostblade", "Zeke's Convergence",
            "Zhonya's Hourglass"]
smites = ["Skirmisher's Sabre", "Stalker's Blade"]
jgItems = ["Cinderhulk", "Warrior", "Blood Razor", "Runic Echoes"]
bootPool = ["Beserker's Greaves", "Boots of Mobility", "Boots of Swiftness", "Ionion Boots of Lucidity",
            "Mercury's Treads", "Ninja Tabi", "Sorcerer's Shoes"]
team = ["Top", "Jungle", "Mid", "ADC", "Support"]
summonerSpells = ["Heal", "Ghost", "Barrier", "Exhaust", "Clarity", "Flash", "Teleport", "Smite", "Cleanse", "Ignite"]

for lane in team:
    itemList = []
    summList = []
    itemCount = 0
    champNum = random.randint(1, 148)
    champion = champPool[champNum-1]
    bootNumb = random.randint(1, 7)
    boots = bootPool[bootNumb-1]

    if lane == "Jungle":
        summList.append("Smite")
        summNum = random.randint(1, 10)
        summ = summonerSpells[summNum-1]
        summList.append(summ)
        s = random.randint(1, 2)
        smite = smites[s-1]
        jg = random.randint(1, 4)
        jgItem = jgItems[jg-1]
        while itemCount < 4:
            itemNum = random.randint(1, 73)
            itemList.append(itemPool[itemNum-1])
            itemCount += 1
        print(lane + ": " + champion + "\n    Boots:\n        " + boots +
                "\n    Build:\n        " + smite + " " + jgItem)
        for item in itemList:
                print("        "+item)
        print("    Summoner Spells:\n        "+summList[0]+"\n        "+summList[1])
    else:
        while itemCount < 5:
            itemNum = random.randint(1, 73)
            itemList.append(itemPool[itemNum-1])
            itemCount += 1
        while len(summList) < 2:
            x = random.randint(1, 10)
            summ = summonerSpells[x-1]
            if summ not in summList:
                summList.append(summ)
        print(lane + ": " + champion + "\n    Boots:\n        " + boots + "\n    Build:")
        for item in itemList:
            print("        " + item)
        print("    Summoner Spells:\n        " + summList[0] + "\n        " + summList[1])
    print("-"*30)
