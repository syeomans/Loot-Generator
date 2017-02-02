from random import *
from Tkinter import *

#Make a roll and return its value
def dice(ddice):
    '''ex: 2d8+2'''
    num, val = ddice.split('d')
    add = 0
    if '+' in val:
        val, add = val.split('+')
    elif '-' in val:
        val, add = val.split('-')
        add = -int(add)
    roll = 0
    for i in range(0,int(num)):
        roll += randrange(1,int(val)+1)
    return roll+int(add)

#Gem loot
def gem10():
    val=dice('1d12')
    lootList = ['Azurite','Banded Agate','Blue quartz','Eye agate','Hematite','Lapis lazuli','Malachite','Moss agate','Obsidian','Rhodochrosite','Tiger eye','Turquoise']
    loot = lootList[val-1]+ ' (10GP)'
    return(loot)

def gem50():
    val=dice('1d12')
    lootList = ['Bloodstone','Carnelian','Chalcedony','Chrysoprase','Citrine','Jasper','Moonstone','Onyx','Quartz','Sardonyx','Star rose quartz','Zircon']
    loot = lootList[val-1]+ ' (50GP)'
    return(loot)

def gem100():
    val=dice('1d10')
    lootList = ['Amber','Amethyst','Chrysoberyl','Coral','Garnet','Jade','Jet','Pearl','Spinel','Tourmaline']
    loot = lootList[val-1]+ ' (100GP)'
    return(loot)

def gem500():
    val=dice('1d6')
    lootList = ['Alexandrite','Aquamarine','Blue pearl','Blue spinel','Peridot','Topaz']
    loot = lootList[val-1]+ ' (500GP)'
    return(loot)

def gem1000():
    val=dice('1d8')
    lootList = ['Black opal','Blue sapphire','Emerald','Fire opal','Opal','Star ruby','Star sapphire','Yellow sapphire']
    loot = lootList[val-1]+ ' (1000GP)'
    return(loot)

def gem5000():
    val=dice('1d4')
    lootList = ['Black sapphire','Diamond','Jacinth','Ruby']
    loot = lootList[val-1]+ ' (5000GP)'
    return(loot)

#Art objects
def art25():
    val=dice('1d10')
    lootList = ['Silver ewer','Carved bone statuette','Small gold bracelet','Cloth-of-gold vestments','Black velvet mask stitched with silver thread','Copper chalice with silver filigree','Pair of engraved bone dice','Small mirror set in a painted wooden frame','Embroidered silk handkerchief','Gold locket with a painted portrait inside']
    loot = lootList[val-1]+ ' (25GP)'
    return(loot)

def art250():
    val=dice('1d10')
    lootList = ['Gold ring set with bloodstones','Carved ivory statuette','Large gold bracelet','Silver necklace with a gemstone pendant','Bronze crown','Silk robe with gold embroidery','Large well-made tapestry','Brass mug with jade inlay','Box of turquoise animal figurines','Gold bird cage with electrum filigree']
    loot = lootList[val-1]+ ' (250GP)'
    return(loot)

def art750():
    val=dice('1d10')
    lootList = ['Silver chalice set with moonstones', 'Silver-plated steel longsword with jet set in hilt', 'Carved harp of exotic wood with ivory inlay and zircon gems', 'Small gold idol', 'Gold dragon comb set with red garnets as eyes','Bottle stopper cork embossed with gold leaf and set with amethysts', 'Ceremonial electrum dagger with a black pearl in the pommel', 'Silver and gold brooch', 'Obsidian statuette with gold fittings and inlay', 'Painted gold war mask']
    loot = lootList[val-1]+ ' (750GP)'
    return(loot)

def art2500():
    val=dice('1d10')
    lootList = ['Fine gold chain set with a fire opal','Old masterpiece painting','Embroidered silk and velvet mantle set with numerous moonstones','Platinum bracelet set with a sapphire','Embroidered glove set with jewel chips','Jeweled anklet','Gold music box','Gold circlet set with four aquamarines','Eye patch with a mock eye set in blue sapphire and moonstone','A necklace string of small pink pearls']
    loot = lootList[val-1]+ ' (2500GP)'
    return(loot)

def art7500():
    val=dice('1d8')
    lootList = ['Jeweled gold crown','Jeweled platinum ring','Small gold statuette set with rubies','Gold cup set with emeralds','Gold jewelry box with platinum filigree',"Painted gold child's sarcophagus",'Jade game board with solid gold playing pieces','Bejeweled ivory drinking horn with gold filigree']
    loot = lootList[val-1]+ ' (7500GP)'
    return(loot)

#Magic items tables
def itemA():
    val=dice('1d100')
    if val <= 50:
        loot = 'Potion of healing'
    elif val <= 60:
        loot = 'Spell scroll (cantrip)'
    elif val <= 70:
        loot = 'Potion of climbing'
    elif val <= 90:
        loot = 'Spell scroll (1st level)'
    elif val <= 94:
        loot = 'Spell scroll (2nd level)'
    elif val <= 98:
        loot = 'Potion of greater healing'
    elif val <= 99:
        loot = 'Bag of holding'
    else:
        loot = 'Driftglobe'
    return(loot)
        
def itemB():
    val=dice('1d100')
    if val <= 15:
            loot = "Potion of greater healing"
    elif val <= 22:
            loot = "Potion of fire breath"
    elif val <= 29:
            loot = "Potion of resistance"
    elif val <= 34:
            loot = "Ammunition, +1"
    elif val <= 39:
            loot = "Potion of animal friendship"
    elif val <= 44:
            loot = "Potion of hill giant strength"
    elif val <= 49:
            loot = "Potion of growth"
    elif val <= 54:
            loot = "Potion of water breathing"
    elif val <= 59:
            loot = "Spell scroll (2nd level)"
    elif val <= 64:
            loot = "Spell scroll (3rd leve l)"
    elif val <= 67:
            loot = "Bag of holding"
    elif val <= 70:
            loot = "Keoghtom's ointment"
    elif val <= 73:
            loot = "Oil of slipperiness"
    elif val <= 75:
            loot = "Dust of disappearance"
    elif val <= 77:
            loot = "Dust of dryness"
    elif val <= 79:
            loot = "Dust of sneezing and choking"
    elif val <= 81:
            loot = "Elemental gem"
    elif val <= 83:
            loot = "Philter of love"
    elif val <= 84:
            loot = "Alchemy jug"
    elif val <= 85:
            loot = "Cap of water breathing"
    elif val <= 86:
            loot = "Cloak of the manta ray"
    elif val <= 87:
            loot = "Driftglobe"
    elif val <= 88:
            loot = "Goggles of night"
    elif val <= 89:
            loot = "Helm of comprehending languages"
    elif val <= 90:
            loot = "Immovable rod"
    elif val <= 91:
            loot = "Lantern of revealing"
    elif val <= 92:
            loot = "Mariner's armor"
    elif val <= 93:
            loot = "Mithral armor"
    elif val <= 94:
            loot = "Potion of poison"
    elif val <= 95:
            loot = "Ring of swimming"
    elif val <= 96:
            loot = "Robe of useful items"
    elif val <= 97:
            loot = "Rope of climbing"
    elif val <= 98:
            loot = "Saddle of the cavalier"
    elif val <= 99:
            loot = "Wand of magic detection"
    elif val <= 100:
            loot = "Wand of secrets"
    return(loot)

def itemC():
    val = dice('1d100')
    if val <= 15:
            loot = "Potion of superior healing"
    elif val <= 22:
            loot = "Spell scroll (4th level)"
    elif val <= 27:
            loot = "Ammunition, +2"
    elif val <= 32:
            loot = "Potion of clairvoyance"
    elif val <= 37:
            loot = "Potion of diminution"
    elif val <= 42:
            loot = "Potion of gaseous form"
    elif val <= 47:
            loot = "Potion of frost giant strength"
    elif val <= 52:
            loot = "Potion of stone giant strength"
    elif val <= 57:
            loot = "Potion of heroism"
    elif val <= 62:
            loot = "Potion of invulnerability"
    elif val <= 67:
            loot = "Potion of mind reading"
    elif val <= 72:
            loot = "Spell scroll (5th le vel)"
    elif val <= 75:
            loot = "Elixir of health"
    elif val <= 78:
            loot = "Oil of etherealness"
    elif val <= 81:
            loot = "Potion of fire giant strength"
    elif val <= 84:
            loot = "Quaal's feather token"
    elif val <= 87:
            loot = "Scroll of protection"
    elif val <= 89:
            loot = "Bag of beans"
    elif val <= 91:
            loot = "Bead of force"
    elif val <= 92:
            loot = "Chime of opening"
    elif val <= 93:
            loot = "Decanter of endless water"
    elif val <= 94:
            loot = "Eyes of minute seeing"
    elif val <= 95:
            loot = "Folding boat"
    elif val <= 96:
            loot = "Heward's handy haversack"
    elif val <= 97:
            loot = "Horseshoes of speed"
    elif val <= 98:
            loot = "Necklace of fireballs"
    elif val <= 99:
            loot = "Periapt of health"
    elif val <= 100:
            loot = "Sending stones"
    return(loot)

def itemD():
    val=dice('1d100')
    if val <= 20:
            loot = "Potion of supreme healing"
    elif val <= 30:
            loot = "Potion of invisibility"
    elif val <= 40:
            loot = "Potion of speed"
    elif val <= 50:
            loot = "Spell scroll (6th level)"
    elif val <= 57:
            loot = "Spell scroll (7th level)"
    elif val <= 62:
            loot = "Ammunition, +3"
    elif val <= 67:
            loot = "Oil of sharpness"
    elif val <= 72:
            loot = "Potion of flying"
    elif val <= 77:
            loot = "Potion of cloud giant strength"
    elif val <= 82:
            loot = "Potion of longevity"
    elif val <= 87:
            loot = "Potion of vitality"
    elif val <= 92:
            loot = "Spell scroll (8th level)"
    elif val <= 95:
            loot = "Horseshoes of a zephyr"
    elif val <= 98:
            loot = "Nolzur's marvelous pigments"
    elif val <= 99:
            loot = "Bag of devouring"
    elif val <= 100:
            loot = "Portable hole"
    return(loot)

def itemE():
    val=dice('1d100')
    if val <= 30:
            loot = "Spell scroll (8th level)"
    elif val <= 55:
            loot = "Potion of storm giant strength"
    elif val <= 70:
            loot = "Potion of supreme healing"
    elif val <= 85:
            loot = "Spell scroll (9th level)"
    elif val <= 93:
            loot = "Universal solvent"
    elif val <= 98:
            loot = "Arrow of slaying"
    elif val <= 100:
            loot = "Sovereign glue"
    return(loot)

def itemF():
    val=dice('1d100')
    if val <= 15:
            loot = "Weapon, +1"
    elif val <= 18:
            loot = "Shield,+ 1"
    elif val <= 21:
            loot = "Sentinel shield"
    elif val <= 23:
            loot = "Amulet of proof against detection and location"
    elif val <= 25:
            loot = "Boots of elvenkind"
    elif val <= 27:
            loot = "Boots of striding and springing"
    elif val <= 29:
            loot = "Bracers of archery"
    elif val <= 31:
            loot = "Brooch of shielding"
    elif val <= 33:
            loot = "Broom of flying"
    elif val <= 35:
            loot = "Cloak of elvenkind"
    elif val <= 37:
            loot = "Cloak of protection"
    elif val <= 39:
            loot = "Gauntlets of ogre power"
    elif val <= 41:
            loot = "Hat of disguise"
    elif val <= 43:
            loot = "Javelin of lightning"
    elif val <= 45:
            loot = "Pearl of power"
    elif val <= 47:
            loot = "Rod of the pact keeper, + 1"
    elif val <= 49:
            loot = "Slippers of spider climbing"
    elif val <= 51:
            loot = "Staff of the adder"
    elif val <= 53:
            loot = "Staff of the python"
    elif val <= 55:
            loot = "Sword of vengeance"
    elif val <= 57:
            loot = "Trident of fish command"
    elif val <= 59:
            loot = "Wand of magic missiles"
    elif val <= 61:
            loot = "Wand of the war mage, + 1"
    elif val <= 63:
            loot = "Wand of web"
    elif val <= 65:
            loot = "Weapon of warning"
    elif val <= 66:
            loot = "Adamantine armor (chain mail)"
    elif val <= 67:
            loot = "Adamantine armor (chain shirt)"
    elif val <= 68:
            loot = "Adamantine armor (scale mail)"
    elif val <= 69:
            loot = "Bag of tricks (gray)"
    elif val <= 70:
            loot = "Bag of tricks (rust)"
    elif val <= 71:
            loot = "Bag of tricks (tan)"
    elif val <= 72:
            loot = "Boots of the winterlands"
    elif val <= 73:
            loot = "Circlet of blasting"
    elif val <= 74:
            loot = "Deck of illusions"
    elif val <= 75:
            loot = "Eversmoking bottle"
    elif val <= 76:
            loot = "Eyes of charming"
    elif val <= 77:
            loot = "Eyes of the eagle"
    elif val <= 78:
            loot = "Figurine of wondrous power (silver raven)"
    elif val <= 79:
            loot = "Gem of brightness"
    elif val <= 80:
            loot = "Gloves of missile snaring"
    elif val <= 81:
            loot = "Gloves of swimming and climbing"
    elif val <= 82:
            loot = "Gloves of thievery"
    elif val <= 83:
            loot = "Headband of intellect"
    elif val <= 84:
            loot = "Helm of telepathy"
    elif val <= 85:
            loot = "Instrument of the bards (Doss lute)"
    elif val <= 86:
            loot = "Instrument of the bards (Fochlucan bandore)"
    elif val <= 87:
            loot = "Instrument of the bards (Mac-Fuimidh cittern)"
    elif val <= 88:
            loot = "Medallion of thoughts"
    elif val <= 89:
            loot = "Necklace of adaptation"
    elif val <= 90:
            loot = "Periapt of wound closure"
    elif val <= 91:
            loot = "Pipes of haunting"
    elif val <= 92:
            loot = "Pipes of the sewers"
    elif val <= 93:
            loot = "Ring of jumping"
    elif val <= 94:
            loot = "Ring of mind shielding"
    elif val <= 95:
            loot = "Ring of warmth"
    elif val <= 96:
            loot = "Ring of water walking"
    elif val <= 97:
            loot = "Quiver of Ehlonna"
    elif val <= 98:
            loot = "Stone of good luck"
    elif val <= 99:
            loot = "Wind fan"
    elif val <= 100:
            loot = "Winged boots"
    return(loot)

def itemG():
    val=dice('1d100')
    if val <= 11:
            loot = "Weapon, +2"
    elif val <= 14:
            loot = "Figurine of wondrous power"
            val2=dice('1d8')
            dollList=['Bronze griffon','Ebony fly','Golden lions','Ivory goats','Marble elephant','Onyx dog','Onyx dog','Serpentine owl']
            loot += ' (' + dollList[val2-1] + ')'
    elif val <= 15:
            loot = "Adamantine armor (breastplate)"
    elif val <= 16:
            loot = "Adamantine armor (splint)"
    elif val <= 17:
            loot = "Amulet of health"
    elif val <= 18:
            loot = "Armor of vulnerability"
    elif val <= 19:
            loot = "Arrow-catching shield"
    elif val <= 20:
            loot = "Belt of dwarvenkind"
    elif val <= 21:
            loot = "Belt of hill giant strength"
    elif val <= 22:
            loot = "Berserker axe"
    elif val <= 23:
            loot = "Boots of levitation"
    elif val <= 24:
            loot = "Boots of speed"
    elif val <= 25:
            loot = "Bowl of commanding water elementals"
    elif val <= 26:
            loot = "Bracers of defense"
    elif val <= 27:
            loot = "Brazier of commanding fire elementals"
    elif val <= 28:
            loot = "Cape of the mountebank"
    elif val <= 29:
            loot = "Censer of controlling air elementals"
    elif val <= 30:
            loot = "Armor, +1 chain mail"
    elif val <= 31:
            loot = "Armor of resistance (chain mail)"
    elif val <= 32:
            loot = "Armor,+ 1 chain shirt"
    elif val <= 33:
            loot = "Armor of resistance (chain shirt)"
    elif val <= 34:
            loot = "Cloak of displacement"
    elif val <= 35:
            loot = "Cloak of the bat"
    elif val <= 36:
            loot = "Cube of force"
    elif val <= 37:
            loot = "Daern's instant fortress"
    elif val <= 38:
            loot = "Dagger of venom"
    elif val <= 39:
            loot = "Dimensional shackles"
    elif val <= 40:
            loot = "Dragon slayer"
    elif val <= 41:
            loot = "Elven chain"
    elif val <= 42:
            loot = "Flame tongue"
    elif val <= 43:
            loot = "Gem of seeing"
    elif val <= 44:
            loot = "Giant slayer"
    elif val <= 45:
            loot = "Clamoured studded leather"
    elif val <= 46:
            loot = "Helm of teleportation"
    elif val <= 47:
            loot = "Horn of blasting"
    elif val <= 48:
            loot = "Horn of Valhalla (silver or brass)"
    elif val <= 49:
            loot = "Instrument of the bards (Canaith mandolin)"
    elif val <= 50:
            loot = "Instrument of the bards (Cli lyre)"
    elif val <= 51:
            loot = "Ioun stone (awareness)"
    elif val <= 52:
            loot = "Ioun stone (protection)"
    elif val <= 53:
            loot = "Ioun stone (reserve)"
    elif val <= 54:
            loot = "Ioun stone (sustenance)"
    elif val <= 55:
            loot = "Iron bands of Bilarro"
    elif val <= 56:
            loot = "Armor, + 1 leather"
    elif val <= 57:
            loot = "Armor of resistance (leather)"
    elif val <= 58:
            loot = "Mace of disruption"
    elif val <= 59:
            loot = "Mace of smiting"
    elif val <= 60:
            loot = "Mace of terror"
    elif val <= 61:
            loot = "Mantle of spell resistance"
    elif val <= 62:
            loot = "Necklace of prayer beads"
    elif val <= 63:
            loot = "Periapt of proof against poison"
    elif val <= 64:
            loot = "Ring of animal influence"
    elif val <= 65:
            loot = "Ring of evasion"
    elif val <= 66:
            loot = "Ring of feather falling"
    elif val <= 67:
            loot = "Ring of free action"
    elif val <= 68:
            loot = "Ring of protection"
    elif val <= 69:
            loot = "Ring of resistance"
    elif val <= 70:
            loot = "Ring of spell storing"
    elif val <= 71:
            loot = "Ring of the ram"
    elif val <= 72:
            loot = "Ring of X-ray vision"
    elif val <= 73:
            loot = "Robe of eyes"
    elif val <= 74:
            loot = "Rod of rulership"
    elif val <= 75:
            loot = "Rod of the pact keeper, +2"
    elif val <= 76:
            loot = "Rope of entanglement"
    elif val <= 77:
            loot = "Armor, +1 scale mail"
    elif val <= 78:
            loot = "Armor of resistance (scale mail)"
    elif val <= 79:
            loot = "Shield, +2"
    elif val <= 80:
            loot = "Shield of missile attraction"
    elif val <= 81:
            loot = "Staff of charming"
    elif val <= 82:
            loot = "Staff of healing"
    elif val <= 83:
            loot = "Staff of swarming insects"
    elif val <= 84:
            loot = "Staff of the woodlands"
    elif val <= 85:
            loot = "Staff of withering"
    elif val <= 86:
            loot = "Stone of controlling earth elementals"
    elif val <= 87:
            loot = "Sun blade"
    elif val <= 88:
            loot = "Sword of life stealing"
    elif val <= 89:
            loot = "Sword of wounding"
    elif val <= 90:
            loot = "Tentacle rod"
    elif val <= 91:
            loot = "Vicious weapon"
    elif val <= 92:
            loot = "Wand of binding"
    elif val <= 93:
            loot = "Wand of enemy detection"
    elif val <= 94:
            loot = "Wand of fear"
    elif val <= 95:
            loot = "Wand of fireballs"
    elif val <= 96:
            loot = "Wand of lightning bolts"
    elif val <= 97:
            loot = "Wand of paralysis"
    elif val <= 98:
            loot = "Wand of the war mage, +2"
    elif val <= 99:
            loot = "Wand of wonder"
    elif val <= 100:
            loot = "Wings of flying"
    return(loot)

def itemH():
    val=dice('1d100')
    if val <= 10:
            loot = "Weapon, +3"
    elif val <= 12:
            loot = "Amulet of the planes"
    elif val <= 14:
            loot = "Carpet of flying"
    elif val <= 16:
            loot = "Crystal ball (very rare version)"
    elif val <= 18:
            loot = "Ring of regeneration"
    elif val <= 20:
            loot = "Ring of shooting stars"
    elif val <= 22:
            loot = "Ring of telekinesis"
    elif val <= 24:
            loot = "Robe of scintillating colors"
    elif val <= 26:
            loot = "Robe of stars"
    elif val <= 28:
            loot = "Rod of absorption"
    elif val <= 30:
            loot = "Rod of alertness"
    elif val <= 32:
            loot = "Rod of security"
    elif val <= 34:
            loot = "Rod of the pact keeper, +3"
    elif val <= 36:
            loot = "Scimitar of speed"
    elif val <= 38:
            loot = "Shield, +3"
    elif val <= 40:
            loot = "Staff of fire"
    elif val <= 42:
            loot = "Staff of frost"
    elif val <= 44:
            loot = "Staff of power"
    elif val <= 46:
            loot = "Staff of striking"
    elif val <= 48:
            loot = "Staff of thunder and lightning"
    elif val <= 50:
            loot = "Sword of sharpness"
    elif val <= 52:
            loot = "Wand of polymorph"
    elif val <= 54:
            loot = "Wand of the war mage, +3"
    elif val <= 55:
            loot = "Adamantine armor (half plate)"
    elif val <= 56:
            loot = "Adamantine armor (plate)"
    elif val <= 57:
            loot = "Animated shield"
    elif val <= 58:
            loot = "Belt of fire giant strength"
    elif val <= 59:
            loot = "Belt of frost (or stone) giant strength"
    elif val <= 60:
            loot = "Armor, + 1 breastplate"
    elif val <= 61:
            loot = "Armor of resistance (breastplate)"
    elif val <= 62:
            loot = "Candle of invocation"
    elif val <= 63:
            loot = "Armor, +2 chain mail"
    elif val <= 64:
            loot = "Armor, +2 chain shirt"
    elif val <= 65:
            loot = "Cloak of arachnida"
    elif val <= 66:
            loot = "Dancing sword"
    elif val <= 67:
            loot = "Demon armor"
    elif val <= 68:
            loot = "Dragon scale mail"
    elif val <= 69:
            loot = "Dwarven plate"
    elif val <= 70:
            loot = "Dwarven thrower"
    elif val <= 71:
            loot = "Efreeti bottle"
    elif val <= 72:
            loot = "Figurine of wondrous power (obsidian steed)"
    elif val <= 73:
            loot = "Frost brand"
    elif val <= 74:
            loot = "Helm of brilliance"
    elif val <= 75:
            loot = "Horn of Valhalla (bronze)"
    elif val <= 76:
            loot = "Instrument of the bards (Anstruth harp)"
    elif val <= 77:
            loot = "Ioun stone (absorption)"
    elif val <= 78:
            loot = "Ioun stone (agility)"
    elif val <= 79:
            loot = "Ioun stone (fortitude)"
    elif val <= 80:
            loot = "Ioun stone (insight)"
    elif val <= 81:
            loot = "Ioun stone (intellect)"
    elif val <= 82:
            loot = "Ioun stone (leadership)"
    elif val <= 83:
            loot = "Ioun stone (strength)"
    elif val <= 84:
            loot = "Armor, +2 leather"
    elif val <= 85:
            loot = "Manual of bodily health"
    elif val <= 86:
            loot = "Manual of gainful exercise"
    elif val <= 87:
            loot = "Manual of golems"
    elif val <= 88:
            loot = "Manual of quickness of action"
    elif val <= 89:
            loot = "Mirror of life trapping"
    elif val <= 90:
            loot = "Nine lives stealer"
    elif val <= 91:
            loot = "Oath bow"
    elif val <= 92:
            loot = "Armor, +2 scale mail"
    elif val <= 93:
            loot = "Spellguard shield"
    elif val <= 94:
            loot = "Armor, + 1 splint"
    elif val <= 95:
            loot = "Armor of resistance (splint)"
    elif val <= 96:
            loot = "Armor, + 1 studded leather"
    elif val <= 97:
            loot = "Armor of resistance (studded leather)"
    elif val <= 98:
            loot = "Tome of clear thought"
    elif val <= 99:
            loot = "Tome of leadership and influence"
    elif val <= 100:
            loot = "Tome of understanding"
    return(loot)

def itemI():
    val=dice('1d100')
    if val <= 5:
            loot = "Defender"
    elif val <= 10:
            loot = "Hammer of thunderbolts"
    elif val <= 15:
            loot = "Luck blade"
    elif val <= 20:
            loot = "Sword of answering"
    elif val <= 23:
            loot = "Holy avenger"
    elif val <= 26:
            loot = "Ring of djinni summoning"
    elif val <= 29:
            loot = "Ring of invisibility"
    elif val <= 32:
            loot = "Ring of spell turning"
    elif val <= 35:
            loot = "Rod of lordly might"
    elif val <= 38:
            loot = "Staff of the magi"
    elif val <= 41:
            loot = "Vorpal sword"
    elif val <= 43:
            loot = "Belt of cloud giant strength"
    elif val <= 45:
            loot = "Armor, +2 breastplate"
    elif val <= 47:
            loot = "Armor, +3 chain mail"
    elif val <= 49:
            loot = "Armor, +3 chain shirt"
    elif val <= 51:
            loot = "Cloak of invisibility"
    elif val <= 53:
            loot = "Crystal ball (legendary version)"
    elif val <= 55:
            loot = "Armor, + 1 half plate"
    elif val <= 57:
            loot = "Iron flask"
    elif val <= 59:
            loot = "Armor, +3 leather"
    elif val <= 61:
            loot = "Armor, +1 plate"
    elif val <= 63:
            loot = "Robe of the archmagi"
    elif val <= 65:
            loot = "Rod of resurrection"
    elif val <= 67:
            loot = "Armor, +1 scale mail"
    elif val <= 69:
            loot = "Scarab of protection"
    elif val <= 71:
            loot = "Armor, +2 splint"
    elif val <= 73:
            loot = "Armor, +2 studded leather"
    elif val <= 75:
            loot = "Well of many worlds"
    elif val <= 76:
            loot = "Magic armor ("
            val2=dice('1d12')
            if val2 <= 2 :
                loot += "+2 half plate)"
            elif val2 <= 4 :
                loot += "+2 plate)"
            elif val2 <= 6 :
                loot += "+3 studded leather)"
            elif val2 <= 8 :
                loot += "+3 breastplate)"
            elif val2 <= 10:
                loot += "+3 splint)"
            elif val2 <= 11:
                loot += "+3 half plate)"
            elif val2 <= 12:
                loot += "+3 plate)"
    elif val <= 77:
            loot = "Apparatus of Kwalish"
    elif val <= 78:
            loot = "Armor of invulnerability"
    elif val <= 79:
            loot = "Belt of storm giant strength"
    elif val <= 80:
            loot = "Cubic gate"
    elif val <= 81:
            loot = "Deck of many things"
    elif val <= 82:
            loot = "Efreeti chain"
    elif val <= 83:
            loot = "Armor of resistance (half plate)"
    elif val <= 84:
            loot = "Horn of Valhalla (iron)"
    elif val <= 85:
            loot = "Instrument of the bards (Ollamh harp)"
    elif val <= 86:
            loot = "Ioun stone (greater absorption)"
    elif val <= 87:
            loot = "Ioun stone (mastery)"
    elif val <= 88:
            loot = "Ioun stone (regeneration)"
    elif val <= 89:
            loot = "Plate armor of etherealness"
    elif val <= 90:
            loot = "Plate armor of resistance"
    elif val <= 91:
            loot = "Ring of air elemental command"
    elif val <= 92:
            loot = "Ring of earth elemental command"
    elif val <= 93:
            loot = "Ring of fire elemental command"
    elif val <= 94:
            loot = "Ring of three wishes"
    elif val <= 95:
            loot = "Ring of water elemental command"
    elif val <= 96:
            loot = "Sphere of annihilation"
    elif val <= 97:
            loot = "Talisman of pure good"
    elif val <= 98:
            loot = "Talisman of the sphere"
    elif val <= 99:
            loot = "Talisman of ultimate evil"
    elif val <= 100:
            loot = "Tome of the stilled tongue"
    return(loot)

#Individual loot
def individual1():
    val=dice('1d100')
    if val <= 30:
        loot = str(dice('5d6')) + 'CP'
    elif val <= 60:
        loot = str(dice('4d6')) + 'SP'
    elif val <= 70:
        loot = str(dice('3d6')) + 'EP'
    elif val <= 95:
        loot = str(dice('3d6')) + 'GP'
    else:
        loot = str(dice('1d6')) + 'PP'
    return(loot)

def individual2():
    val=dice('1d100')
    loot = []
    if val <= 30:
        loot.append(str(dice('4d6')*100) + 'CP')
        loot.append(str(dice('1d6')*10) + 'EP')
    elif val <= 60:
        loot.append(str(dice('6d6')*10) + 'SP')
        loot.append(str(dice('2d6')*10) + 'GP')
    elif val <= 70:
        loot.append(str(dice('1d6')*10) + 'EP')
        loot.append(str(dice('2d6')*10) + 'GP')
    elif val <= 95:
        loot.append(str(dice('4d6')*10) + 'GP')
    else:
        loot.append(str(dice('2d6')*10) + 'GP')
        loot.append(str(dice('3d6')) + 'PP')
    return(loot)

def individual3():
    val=dice('1d100')
    loot = []
    if val <= 20:
        loot.append(str(dice('4d6')*100) + 'SP')
        loot.append(str(dice('1d6')*100) + 'GP')
    elif val <= 35:
        loot.append(str(dice('1d6')*100) + 'EP')
        loot.append(str(dice('1d6')*100) + 'GP')
    elif val <= 75:
        loot.append(str(dice('2d6')*100) + 'GP')
        loot.append(str(dice('1d6')*10) + 'PP')
    else:
        loot.append(str(dice('2d6')*100) + 'GP')
        loot.append(str(dice('2d6')*10) + 'PP')
    return(loot)

def individual4():
    val=dice('1d100')
    loot = []
    if val <= 15:
        loot.append(str(dice('2d6')*1000) + 'EP')
        loot.append(str(dice('8d6')*100) + 'GP')
    elif val <= 55:
        loot.append(str(dice('1d6')*1000) + 'GP')
        loot.append(str(dice('1d6')*100) + 'PP')
    else:
        loot.append(str(dice('1d6')*1000) + 'GP')
        loot.append(str(dice('2d6')*100) + 'PP')
    return(loot)

#Hoard loot
def hoard1():
    val=dice('1d100')
    loot=[]
    loot.append(str(dice("6d6")*100)+' CP')
    loot.append(str(dice("3d6")*100)+' SP')
    loot.append(str(dice("2d6")*10)+' GP')
    if val<=6:
        loot.append("No gems or items")
    elif val<=16:
        for i in range(0,dice('2d6')):
            loot.append(gem10())
        loot.append("No magic items")
    elif val<=26:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        loot.append("No magic items")
    elif val<=36:
        for i in range(0,dice('2d6')):
            loot.append(gem50())
        loot.append("No magic items")
    elif val<=44:
        for i in range(0,dice('2d6')):
            loot.append(gem10())
        for i in range(0,dice('1d6')):
            loot.append(itemA())
    elif val<=52:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d6')):
            loot.append(itemA())
    elif val<=60:
        for i in range(0,dice('2d6')):
            loot.append(gem50())
        for i in range(0,dice('1d6')):
            loot.append(itemA())
    elif val<=65:
        for i in range(0,dice('2d6')):
            loot.append(gem10())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=70:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=75:
        for i in range(0,dice('2d6')):
            loot.append(gem50())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=78:
        for i in range(0,dice('2d6')):
            loot.append(gem10())
        for i in range(0,dice('1d4')):
            loot.append(itemC())
    elif val<=80:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d4')):
            loot.append(itemC())
    elif val<=85:
        for i in range(0,dice('2d6')):
            loot.append(gem50())
        for i in range(0,dice('1d4')):
            loot.append(itemC())
    elif val<=92:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d4')):
            loot.append(itemF())
    elif val<=97:
        for i in range(0,dice('2d6')):
            loot.append(gem50())
        for i in range(0,dice('1d4')):
            loot.append(itemF())
    elif val<=99:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d1')):
            loot.append(itemG())
    elif val<=100:
        for i in range(0,dice('2d6')):
            loot.append(gem50())
        for i in range(0,dice('1d1')):
            loot.append(itemG())
    return(loot)

def hoard2():
    val=dice('1d100')
    loot=[]
    loot.append(str(dice("2d6")*100)+' CP')
    loot.append(str(dice("2d6")*1000)+' SP')
    loot.append(str(dice("6d6")*100)+' GP')
    loot.append(str(dice("3d6")*10)+' PP')
    if val<=4:
        loot.append("No gems or items")
    elif val<=10:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        loot.append("No magic items")
    elif val<=16:
        for i in range(0,dice('3d6')):
            loot.append(gem50())
        loot.append("No magic items")
    elif val<=22:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        loot.append("No magic items")
    elif val<=28:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        loot.append("No magic items")
    elif val<=32:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d6')):
            loot.append(itemA())
    elif val<=36:
        for i in range(0,dice('3d6')):
            loot.append(gem50())
        for i in range(0,dice('1d6')):
            loot.append(itemA())
    elif val<=40:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        for i in range(0,dice('1d6')):
            loot.append(itemA())
    elif val<=44:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d6')):
            loot.append(itemA())
    elif val<=49:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=54:
        for i in range(0,dice('3d6')):
            loot.append(gem50())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=59:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=63:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=66:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d4')):
            loot.append(itemC())
    elif val<=69:
        for i in range(0,dice('3d6')):
            loot.append(gem50())
        for i in range(0,dice('1d4')):
            loot.append(itemC())
    elif val<=72:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        for i in range(0,dice('1d4')):
            loot.append(itemC())
    elif val<=74:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d4')):
            loot.append(itemC())
    elif val<=76:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d1')):
            loot.append(itemD())
    elif val<=78:
        for i in range(0,dice('3d6')):
            loot.append(gem50())
        for i in range(0,dice('1d1')):
            loot.append(itemD())
    elif val<=79:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        for i in range(0,dice('1d1')):
            loot.append(itemD())
    elif val<=80:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d1')):
            loot.append(itemD())
    elif val<=84:
        for i in range(0,dice('2d4')):
            loot.append(art25())
        for i in range(0,dice('1d4')):
            loot.append(itemF())
    elif val<=88:
        for i in range(0,dice('3d6')):
            loot.append(gem50())
        for i in range(0,dice('1d4')):
            loot.append(itemF())
    elif val<=91:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        for i in range(0,dice('1d4')):
            loot.append(itemF())
    elif val<=94:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d4')):
            loot.append(itemF())
    elif val<=96:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        for i in range(0,dice('1d4')):
            loot.append(itemG())
    elif val<=98:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d4')):
            loot.append(itemG())
    elif val<=99:
        for i in range(0,dice('3d6')):
            loot.append(gem100())
        for i in range(0,dice('1d1')):
            loot.append(itemH())
    elif val<=100:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d1')):
            loot.append(itemH())
    return(loot)

def hoard3():
    val=dice('1d100')
    loot=[]
    loot.append(str(dice("4d6")*1000)+' GP')
    loot.append(str(dice("5d6")*100)+' PP')
    if val<=3:
        loot.append("No gems or items")
    elif val<=6:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        loot.append("No items")
    elif val<=9:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        loot.append("No items")
    elif val<=12:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        loot.append("No items")
    elif val<=15:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        loot.append("No items")
    elif val<=19:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=23:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=26:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=29:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d4')):
            loot.append(itemB())
    elif val<=35:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d6')):
            loot.append(itemC())
    elif val<=40:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        for i in range(0,dice('1d6')):
            loot.append(itemC())
    elif val<=45:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        for i in range(0,dice('1d6')):
            loot.append(itemC())
    elif val<=50:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d6')):
            loot.append(itemC())
    elif val<=54:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d4')):
            loot.append(itemD())
    elif val<=58:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        for i in range(0,dice('1d4')):
            loot.append(itemD())
    elif val<=62:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        for i in range(0,dice('1d4')):
            loot.append(itemD())
    elif val<=66:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d4')):
            loot.append(itemD())
    elif val<=68:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d1')):
            loot.append(itemE())
    elif val<=70:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        for i in range(0,dice('1d1')):
            loot.append(itemE())
    elif val<=72:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        for i in range(0,dice('1d1')):
            loot.append(itemE())
    elif val<=74:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d1')):
            loot.append(itemE())
    elif val<=76:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d1')):
            loot.append(itemG())
    elif val<=78:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        for i in range(0,dice('1d1')):
            loot.append(itemG())
    elif val<=80:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        for i in range(0,dice('1d1')):
            loot.append(itemG())
    elif val<=82:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d1')):
            loot.append(itemG())
    elif val<=85:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=88:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=90:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=92:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=94:
        for i in range(0,dice('2d4')):
            loot.append(art250())
        for i in range(0,dice('1d1')):
            loot.append(itemI())
    elif val<=96:
        for i in range(0,dice('2d4')):
            loot.append(art750())
        for i in range(0,dice('1d1')):
            loot.append(itemI())
    elif val<=98:
        for i in range(0,dice('3d6')):
            loot.append(gem500())
        for i in range(0,dice('1d1')):
            loot.append(itemI())
    elif val<=100:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d1')):
            loot.append(itemI())
    return(loot)

def hoard4():
    val=dice('1d100')
    loot=[]
    loot.append(str(dice("12d6")*1000)+' GP')
    loot.append(str(dice("8d6")*1000)+' PP')
    if val<=5:
        loot.append("No gems or items")
    elif val<=8:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d8')):
            loot.append(itemC())
    elif val<=11:
        for i in range(0,dice('1d1')):
            loot.append(art2500())
        for i in range(0,dice('1d8')):
            loot.append(itemC())
    elif val<=14:
        for i in range(0,dice('1d4')):
            loot.append(art7500())
        for i in range(0,dice('1d8')):
            loot.append(itemC())
    elif val<=22:
        for i in range(0,dice('1d8')):
            loot.append(gem5000())
        for i in range(0,dice('1d8')):
            loot.append(itemC())
    elif val<=30:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d6')):
            loot.append(itemD())
    elif val<=38:
        for i in range(0,dice('1d1')):
            loot.append(art2500())
        for i in range(0,dice('1d6')):
            loot.append(itemD())
    elif val<=46:
        for i in range(0,dice('1d4')):
            loot.append(art7500())
        for i in range(0,dice('1d6')):
            loot.append(itemD())
    elif val<=52:
        for i in range(0,dice('1d8')):
            loot.append(gem5000())
        for i in range(0,dice('1d6')):
            loot.append(itemD())
    elif val<=58:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d6')):
            loot.append(itemE())
    elif val<=63:
        for i in range(0,dice('1d1')):
            loot.append(art2500())
        for i in range(0,dice('1d6')):
            loot.append(itemE())
    elif val<=68:
        for i in range(0,dice('1d4')):
            loot.append(art7500())
        for i in range(0,dice('1d6')):
            loot.append(itemE())
    elif val<=69:
        for i in range(0,dice('1d8')):
            loot.append(gem5000())
        for i in range(0,dice('1d6')):
            loot.append(itemE())
    elif val<=70:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d4')):
            loot.append(itemG())
    elif val<=71:
        for i in range(0,dice('1d1')):
            loot.append(art2500())
        for i in range(0,dice('1d4')):
            loot.append(itemG())
    elif val<=72:
        for i in range(0,dice('1d4')):
            loot.append(art7500())
        for i in range(0,dice('1d4')):
            loot.append(itemG())
    elif val<=74:
        for i in range(0,dice('1d8')):
            loot.append(gem5000())
        for i in range(0,dice('1d4')):
            loot.append(itemG())
    elif val<=76:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=78:
        for i in range(0,dice('1d1')):
            loot.append(art2500())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=80:
        for i in range(0,dice('1d4')):
            loot.append(art7500())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=85:
        for i in range(0,dice('1d8')):
            loot.append(gem5000())
        for i in range(0,dice('1d4')):
            loot.append(itemH())
    elif val<=90:
        for i in range(0,dice('3d6')):
            loot.append(gem1000())
        for i in range(0,dice('1d4')):
            loot.append(itemI())
    elif val<=95:
        for i in range(0,dice('1d1')):
            loot.append(art2500())
        for i in range(0,dice('1d4')):
            loot.append(itemI())
    elif val<=100:
        for i in range(0,dice('1d4')):
            loot.append(art7500())
        for i in range(0,dice('1d4')):
            loot.append(itemI())
    return(loot)
    
#GUI
root = Tk()
root.geometry('300x500')
root.wm_title('Loot Generator')

lootType=StringVar(root)
text=StringVar()
def run():
    tp=lootType.get()
    item = ''
    loot=[]
    if tp=='Treasure Hoard: Challenge 0-4':
        item=hoard1()
    elif tp=='Treasure Hoard: Challenge 5-10':
        item=hoard2()
    elif tp=='Treasure Hoard: Challenge 11-16':
        item=hoard3()
    elif tp=='Treasure Hoard: Challenge 17+':
        item=hoard4()
    elif tp=='Individual Treasure: Challenge 0-4':
        item=individual1()
    elif tp=='Individual Treasure: Challenge 5-10':
        item=individual2()
    elif tp=='Individual Treasure: Challenge 11-16':
        item=individual3()
    elif tp=='Individual Treasure: Challenge 17+':
        item=individual4()
    elif tp=='10 GP Gemstones':
        item=gem10()
    elif tp=='50 GP Gemstones':
        item=gem50()
    elif tp=='100 GP Gemstones':
        item=gem100()
    elif tp=='500 GP Gemstones':
        item=gem500()
    elif tp=='1000 GP Gemstones':
        item=gem1000()
    elif tp=='5000 GP Gemstones':
        item=gem5000()
    elif tp=='25 GP Art Objects':
        item=art25()
    elif tp=='250 GP Art Objects':
        item=art250()
    elif tp=='750 GP Art Objects':
        item=art750()
    elif tp=='2500 GP Art Objects':
        item=art2500()
    elif tp=='7500 GP Art Objects':
        item=art7500()
    elif tp=='Magic Item Table A':
        item=itemA()
    elif tp=='Magic Item Table B':
        item=itemB()
    elif tp=='Magic Item Table C':
        item=itemC()
    elif tp=='Magic Item Table D':
        item=itemD()
    elif tp=='Magic Item Table E':
        item=itemE()
    elif tp=='Magic Item Table F':
        item=itemF()
    elif tp=='Magic Item Table G':
        item=itemG()
    elif tp=='Magic Item Table H':
        item=itemH()
    elif tp=='Magic Item Table I':
        item=itemI()

    if type(item) == str:
        loot.append(item)
    elif type(item)==list:
        loot += item
    loot="\n".join(loot)
    global text
    text.set(loot)
    print(loot)

typeMenu = OptionMenu(root,lootType,'Treasure Hoard: Challenge 0-4',
                      'Treasure Hoard: Challenge 5-10',
                      'Treasure Hoard: Challenge 11-16',
                      'Treasure Hoard: Challenge 17+',
                      'Individual Treasure: Challenge 0-4',
                      'Individual Treasure: Challenge 5-10',
                      'Individual Treasure: Challenge 11-16',
                      'Individual Treasure: Challenge 17+',
                      '10 GP Gemstones',
                      '50 GP Gemstones',
                      '100 GP Gemstones',
                      '500 GP Gemstones',
                      '1000 GP Gemstones',
                      '5000 GP Gemstones',
                      '25 GP Art Objects',
                      '250 GP Art Objects',
                      '750 GP Art Objects',
                      '2500 GP Art Objects',
                      '7500 GP Art Objects',
                      'Magic Item Table A',
                      'Magic Item Table B',
                      'Magic Item Table C',
                      'Magic Item Table D',
                      'Magic Item Table E',
                      'Magic Item Table F',
                      'Magic Item Table G',
                      'Magic Item Table H',
                      'Magic Item Table I')
textblock=Label(root,textvariable=text,justify=LEFT)
ok=Button(root,text="ok",command=run)

typeMenu.pack()
ok.pack()
textblock.pack(side=LEFT)

root.mainloop()
