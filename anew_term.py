#!/usr/bin/python

#- ANEW_TERM.PY ------------------------------------------------------------#
#  Raw term data with average valence and arousal for a set of terms from	#
#  the ANEW and Happiness sentiment dictionaries, used by ANEW.PY for		#
#  sentiment calculations													#
#																			#
#- Modification History: ---------------------------------------------------#
#  When:		Who:					Comments:							#
#																			#
#  28-Sep-14	Christopher G. Healey	Converted from Javascript			#
#---------------------------------------------------------------------------#

#  ANEW terms w/word, stem, avg valence and arousal, stdev of valience
#  and arousal, and number of evaluations

anew_word = {
  "abduction": {
    "dict": "anew", "word": "abduction", "stem": "abduct",
    "avg": [ 2.76, 5.53 ], "std": [ 2.06, 2.43 ], "fq": 1
  },
  "abortion": {
    "dict": "anew", "word": "abortion", "stem": "abort",
    "avg": [ 3.50, 5.39 ], "std": [ 2.30, 2.80 ], "fq": 6
  },
  "absurd": {
    "dict": "anew", "word": "absurd", "stem": "absurd",
    "avg": [ 4.26, 4.36 ], "std": [ 1.82, 2.20 ], "fq": 17
  },
  "abundance": {
    "dict": "anew", "word": "abundance", "stem": "abund",
    "avg": [ 6.59, 5.51 ], "std": [ 2.01, 2.63 ], "fq": 13
  },
  "abuse": {
    "dict": "anew", "word": "abuse", "stem": "abus",
    "avg": [ 1.80, 6.83 ], "std": [ 1.23, 2.70 ], "fq": 18
  },
  "acceptance": {
    "dict": "anew", "word": "acceptance", "stem": "accept",
    "avg": [ 7.98, 5.40 ], "std": [ 1.42, 2.70 ], "fq": 49
  },
  "accident": {
    "dict": "anew", "word": "accident", "stem": "accid",
    "avg": [ 2.05, 6.26 ], "std": [ 1.19, 2.87 ], "fq": 33
  },
  "ace": {
    "dict": "anew", "word": "ace", "stem": "ace",
    "avg": [ 6.88, 5.50 ], "std": [ 1.93, 2.66 ], "fq": 15
  },
  "ache": {
    "dict": "anew", "word": "ache", "stem": "ach",
    "avg": [ 2.46, 5.00 ], "std": [ 1.52, 2.45 ], "fq": 4
  },
  "achievement": {
    "dict": "anew", "word": "achievement", "stem": "achiev",
    "avg": [ 7.89, 5.53 ], "std": [ 1.38, 2.81 ], "fq": 65
  },
  "activate": {
    "dict": "anew", "word": "activate", "stem": "activ",
    "avg": [ 5.46, 4.86 ], "std": [ 0.98, 2.56 ], "fq": 2
  },
  "addict": {
    "dict": "anew", "word": "addict", "stem": "addict",
    "avg": [ 2.48, 5.66 ], "std": [ 2.08, 2.26 ], "fq": 1
  },
  "addicted": {
    "dict": "anew", "word": "addicted", "stem": "addict",
    "avg": [ 2.51, 4.81 ], "std": [ 1.42, 2.46 ], "fq": 3
  },
  "admired": {
    "dict": "anew", "word": "admired", "stem": "admir",
    "avg": [ 7.74, 6.11 ], "std": [ 1.84, 2.36 ], "fq": 17
  },
  "adorable": {
    "dict": "anew", "word": "adorable", "stem": "ador",
    "avg": [ 7.81, 5.12 ], "std": [ 1.24, 2.71 ], "fq": 3
  },
  "adult": {
    "dict": "anew", "word": "adult", "stem": "adult",
    "avg": [ 6.49, 4.76 ], "std": [ 1.50, 1.95 ], "fq": 25
  },
  "advantage": {
    "dict": "anew", "word": "advantage", "stem": "advantag",
    "avg": [ 6.95, 4.76 ], "std": [ 1.85, 2.18 ], "fq": 73
  },
  "adventure": {
    "dict": "anew", "word": "adventure", "stem": "adventur",
    "avg": [ 7.60, 6.98 ], "std": [ 1.50, 2.15 ], "fq": 14
  },
  "affection": {
    "dict": "anew", "word": "affection", "stem": "affect",
    "avg": [ 8.39, 6.21 ], "std": [ 0.86, 2.75 ], "fq": 18
  },
  "afraid": {
    "dict": "anew", "word": "afraid", "stem": "afraid",
    "avg": [ 2.00, 6.67 ], "std": [ 1.28, 2.54 ], "fq": 57
  },
  "aggressive": {
    "dict": "anew", "word": "aggressive", "stem": "aggress",
    "avg": [ 5.10, 5.83 ], "std": [ 1.68, 2.33 ], "fq": 17
  },
  "agility": {
    "dict": "anew", "word": "agility", "stem": "agil",
    "avg": [ 6.46, 4.85 ], "std": [ 1.57, 1.80 ], "fq": 3
  },
  "agony": {
    "dict": "anew", "word": "agony", "stem": "agoni",
    "avg": [ 2.43, 6.06 ], "std": [ 2.17, 2.67 ], "fq": 9
  },
  "agreement": {
    "dict": "anew", "word": "agreement", "stem": "agreement",
    "avg": [ 7.08, 5.02 ], "std": [ 1.59, 2.24 ], "fq": 106
  },
  "air": {
    "dict": "anew", "word": "air", "stem": "air",
    "avg": [ 6.34, 4.12 ], "std": [ 1.56, 2.30 ], "fq": 257
  },
  "alcoholic": {
    "dict": "anew", "word": "alcoholic", "stem": "alcohol",
    "avg": [ 2.84, 5.69 ], "std": [ 2.34, 2.36 ], "fq": 3
  },
  "alert": {
    "dict": "anew", "word": "alert", "stem": "alert",
    "avg": [ 6.20, 6.85 ], "std": [ 1.76, 2.53 ], "fq": 33
  },
  "alien": {
    "dict": "anew", "word": "alien", "stem": "alien",
    "avg": [ 5.60, 5.45 ], "std": [ 1.82, 2.15 ], "fq": 16
  },
  "alimony": {
    "dict": "anew", "word": "alimony", "stem": "alimoni",
    "avg": [ 3.95, 4.30 ], "std": [ 2.00, 2.29 ], "fq": 2
  },
  "alive": {
    "dict": "anew", "word": "alive", "stem": "aliv",
    "avg": [ 7.25, 5.50 ], "std": [ 2.22, 2.74 ], "fq": 57
  },
  "allergy": {
    "dict": "anew", "word": "allergy", "stem": "allergi",
    "avg": [ 3.07, 4.64 ], "std": [ 1.64, 2.34 ], "fq": 1
  },
  "alley": {
    "dict": "anew", "word": "alley", "stem": "alley",
    "avg": [ 4.48, 4.91 ], "std": [ 1.97, 2.42 ], "fq": 8
  },
  "alone": {
    "dict": "anew", "word": "alone", "stem": "alon",
    "avg": [ 2.41, 4.83 ], "std": [ 1.77, 2.66 ], "fq": 195
  },
  "aloof": {
    "dict": "anew", "word": "aloof", "stem": "aloof",
    "avg": [ 4.90, 4.28 ], "std": [ 1.92, 2.10 ], "fq": 5
  },
  "ambition": {
    "dict": "anew", "word": "ambition", "stem": "ambit",
    "avg": [ 7.04, 5.61 ], "std": [ 1.98, 2.92 ], "fq": 19
  },
  "ambulance": {
    "dict": "anew", "word": "ambulance", "stem": "ambul",
    "avg": [ 2.47, 7.33 ], "std": [ 1.50, 1.96 ], "fq": 6
  },
  "angel": {
    "dict": "anew", "word": "angel", "stem": "angel",
    "avg": [ 7.53, 4.83 ], "std": [ 1.58, 2.63 ], "fq": 18
  },
  "anger": {
    "dict": "anew", "word": "anger", "stem": "anger",
    "avg": [ 2.34, 7.63 ], "std": [ 1.32, 1.91 ], "fq": 48
  },
  "angry": {
    "dict": "anew", "word": "angry", "stem": "angri",
    "avg": [ 2.85, 7.17 ], "std": [ 1.70, 2.07 ], "fq": 45
  },
  "anguished": {
    "dict": "anew", "word": "anguished", "stem": "anguish",
    "avg": [ 2.12, 5.33 ], "std": [ 1.56, 2.69 ], "fq": 2
  },
  "ankle": {
    "dict": "anew", "word": "ankle", "stem": "ankl",
    "avg": [ 5.27, 4.16 ], "std": [ 1.54, 2.03 ], "fq": 8
  },
  "annoy": {
    "dict": "anew", "word": "annoy", "stem": "annoy",
    "avg": [ 2.74, 6.49 ], "std": [ 1.81, 2.17 ], "fq": 2
  },
  "answer": {
    "dict": "anew", "word": "answer", "stem": "answer",
    "avg": [ 6.63, 5.41 ], "std": [ 1.68, 2.43 ], "fq": 152
  },
  "anxious": {
    "dict": "anew", "word": "anxious", "stem": "anxious",
    "avg": [ 4.81, 6.92 ], "std": [ 1.98, 1.81 ], "fq": 29
  },
  "applause": {
    "dict": "anew", "word": "applause", "stem": "applaus",
    "avg": [ 7.50, 5.80 ], "std": [ 1.50, 2.79 ], "fq": 14
  },
  "appliance": {
    "dict": "anew", "word": "appliance", "stem": "applianc",
    "avg": [ 5.10, 4.05 ], "std": [ 1.21, 2.06 ], "fq": 5
  },
  "arm": {
    "dict": "anew", "word": "arm", "stem": "arm",
    "avg": [ 5.34, 3.59 ], "std": [ 1.82, 2.40 ], "fq": 94
  },
  "army": {
    "dict": "anew", "word": "army", "stem": "armi",
    "avg": [ 4.72, 5.03 ], "std": [ 1.75, 2.03 ], "fq": 132
  },
  "aroused": {
    "dict": "anew", "word": "aroused", "stem": "arous",
    "avg": [ 7.97, 6.63 ], "std": [ 1.00, 2.70 ], "fq": 20
  },
  "arrogant": {
    "dict": "anew", "word": "arrogant", "stem": "arrog",
    "avg": [ 3.69, 5.65 ], "std": [ 2.40, 2.23 ], "fq": 2
  },
  "art": {
    "dict": "anew", "word": "art", "stem": "art",
    "avg": [ 6.68, 4.86 ], "std": [ 2.10, 2.88 ], "fq": 208
  },
  "assassin": {
    "dict": "anew", "word": "assassin", "stem": "assassin",
    "avg": [ 3.09, 6.28 ], "std": [ 2.09, 2.53 ], "fq": 6
  },
  "assault": {
    "dict": "anew", "word": "assault", "stem": "assault",
    "avg": [ 2.03, 7.51 ], "std": [ 1.55, 2.28 ], "fq": 15
  },
  "astonished": {
    "dict": "anew", "word": "astonished", "stem": "astonish",
    "avg": [ 6.56, 6.58 ], "std": [ 1.61, 2.22 ], "fq": 6
  },
  "astronaut": {
    "dict": "anew", "word": "astronaut", "stem": "astronaut",
    "avg": [ 6.66, 5.28 ], "std": [ 1.60, 2.11 ], "fq": 2
  },
  "athletics": {
    "dict": "anew", "word": "athletics", "stem": "athlet",
    "avg": [ 6.61, 6.10 ], "std": [ 2.08, 2.29 ], "fq": 9
  },
  "autumn": {
    "dict": "anew", "word": "autumn", "stem": "autumn",
    "avg": [ 6.30, 4.51 ], "std": [ 2.14, 2.50 ], "fq": 22
  },
  "avalanche": {
    "dict": "anew", "word": "avalanche", "stem": "avalanch",
    "avg": [ 3.29, 5.54 ], "std": [ 1.95, 2.37 ], "fq": 1
  },
  "avenue": {
    "dict": "anew", "word": "avenue", "stem": "avenu",
    "avg": [ 5.50, 4.12 ], "std": [ 1.37, 2.01 ], "fq": 46
  },
  "awed": {
    "dict": "anew", "word": "awed", "stem": "awe",
    "avg": [ 6.70, 5.74 ], "std": [ 1.38, 2.31 ], "fq": 5
  },
  "baby": {
    "dict": "anew", "word": "baby", "stem": "babi",
    "avg": [ 8.22, 5.53 ], "std": [ 1.20, 2.80 ], "fq": 62
  },
  "bake": {
    "dict": "anew", "word": "bake", "stem": "bake",
    "avg": [ 6.17, 5.10 ], "std": [ 1.71, 2.30 ], "fq": 12
  },
  "bandage": {
    "dict": "anew", "word": "bandage", "stem": "bandag",
    "avg": [ 4.54, 3.90 ], "std": [ 1.75, 2.07 ], "fq": 4
  },
  "bankrupt": {
    "dict": "anew", "word": "bankrupt", "stem": "bankrupt",
    "avg": [ 2.00, 6.21 ], "std": [ 1.31, 2.79 ], "fq": 5
  },
  "banner": {
    "dict": "anew", "word": "banner", "stem": "banner",
    "avg": [ 5.40, 3.83 ], "std": [ 0.83, 1.95 ], "fq": 8
  },
  "bar": {
    "dict": "anew", "word": "bar", "stem": "bar",
    "avg": [ 6.42, 5.00 ], "std": [ 2.05, 2.83 ], "fq": 82
  },
  "barrel": {
    "dict": "anew", "word": "barrel", "stem": "barrel",
    "avg": [ 5.05, 3.36 ], "std": [ 1.46, 2.28 ], "fq": 24
  },
  "basket": {
    "dict": "anew", "word": "basket", "stem": "basket",
    "avg": [ 5.45, 3.63 ], "std": [ 1.15, 2.02 ], "fq": 17
  },
  "bastard": {
    "dict": "anew", "word": "bastard", "stem": "bastard",
    "avg": [ 3.36, 6.07 ], "std": [ 2.16, 2.15 ], "fq": 12
  },
  "bath": {
    "dict": "anew", "word": "bath", "stem": "bath",
    "avg": [ 7.33, 4.16 ], "std": [ 1.45, 2.31 ], "fq": 26
  },
  "bathroom": {
    "dict": "anew", "word": "bathroom", "stem": "bathroom",
    "avg": [ 5.55, 3.88 ], "std": [ 1.36, 1.72 ], "fq": 18
  },
  "bathtub": {
    "dict": "anew", "word": "bathtub", "stem": "bathtub",
    "avg": [ 6.69, 4.36 ], "std": [ 1.57, 2.59 ], "fq": 4
  },
  "beach": {
    "dict": "anew", "word": "beach", "stem": "beach",
    "avg": [ 8.03, 5.53 ], "std": [ 1.59, 3.07 ], "fq": 61
  },
  "beast": {
    "dict": "anew", "word": "beast", "stem": "beast",
    "avg": [ 4.23, 5.57 ], "std": [ 2.41, 2.61 ], "fq": 7
  },
  "beautiful": {
    "dict": "anew", "word": "beautiful", "stem": "beauti",
    "avg": [ 7.60, 6.17 ], "std": [ 1.64, 2.34 ], "fq": 127
  },
  "beauty": {
    "dict": "anew", "word": "beauty", "stem": "beauti",
    "avg": [ 7.82, 4.95 ], "std": [ 1.16, 2.57 ], "fq": 71
  },
  "bed": {
    "dict": "anew", "word": "bed", "stem": "bed",
    "avg": [ 7.51, 3.61 ], "std": [ 1.38, 2.56 ], "fq": 127
  },
  "bees": {
    "dict": "anew", "word": "bees", "stem": "bee",
    "avg": [ 3.20, 6.51 ], "std": [ 2.07, 2.14 ], "fq": 15
  },
  "beggar": {
    "dict": "anew", "word": "beggar", "stem": "beggar",
    "avg": [ 3.22, 4.91 ], "std": [ 2.02, 2.45 ], "fq": 2
  },
  "bench": {
    "dict": "anew", "word": "bench", "stem": "bench",
    "avg": [ 4.61, 3.59 ], "std": [ 1.40, 2.07 ], "fq": 35
  },
  "bereavement": {
    "dict": "anew", "word": "bereavement", "stem": "bereav",
    "avg": [ 4.57, 4.20 ], "std": [ 1.70, 2.15 ], "fq": 4
  },
  "betray": {
    "dict": "anew", "word": "betray", "stem": "betray",
    "avg": [ 1.68, 7.24 ], "std": [ 1.02, 2.06 ], "fq": 4
  },
  "beverage": {
    "dict": "anew", "word": "beverage", "stem": "beverag",
    "avg": [ 6.83, 5.21 ], "std": [ 1.48, 2.46 ], "fq": 5
  },
  "bird": {
    "dict": "anew", "word": "bird", "stem": "bird",
    "avg": [ 7.27, 3.17 ], "std": [ 1.36, 2.23 ], "fq": 31
  },
  "birthday": {
    "dict": "anew", "word": "birthday", "stem": "birthday",
    "avg": [ 7.84, 6.68 ], "std": [ 1.92, 2.11 ], "fq": 18
  },
  "black": {
    "dict": "anew", "word": "black", "stem": "black",
    "avg": [ 5.39, 4.61 ], "std": [ 1.80, 2.24 ], "fq": 203
  },
  "blackmail": {
    "dict": "anew", "word": "blackmail", "stem": "blackmail",
    "avg": [ 2.95, 6.03 ], "std": [ 1.95, 2.70 ], "fq": 2
  },
  "bland": {
    "dict": "anew", "word": "bland", "stem": "bland",
    "avg": [ 4.10, 3.29 ], "std": [ 1.08, 1.89 ], "fq": 3
  },
  "blase": {
    "dict": "anew", "word": "blase", "stem": "blase",
    "avg": [ 4.89, 3.94 ], "std": [ 1.16, 1.76 ], "fq": 7
  },
  "blasphemy": {
    "dict": "anew", "word": "blasphemy", "stem": "blasphemi",
    "avg": [ 3.75, 4.93 ], "std": [ 2.26, 2.34 ], "fq": 4
  },
  "bless": {
    "dict": "anew", "word": "bless", "stem": "bless",
    "avg": [ 7.19, 4.05 ], "std": [ 1.69, 2.59 ], "fq": 9
  },
  "blind": {
    "dict": "anew", "word": "blind", "stem": "blind",
    "avg": [ 3.05, 4.39 ], "std": [ 1.99, 2.36 ], "fq": 47
  },
  "bliss": {
    "dict": "anew", "word": "bliss", "stem": "bliss",
    "avg": [ 6.95, 4.41 ], "std": [ 2.24, 2.95 ], "fq": 4
  },
  "blister": {
    "dict": "anew", "word": "blister", "stem": "blister",
    "avg": [ 2.88, 4.10 ], "std": [ 1.75, 2.34 ], "fq": 3
  },
  "blond": {
    "dict": "anew", "word": "blond", "stem": "blond",
    "avg": [ 6.43, 5.07 ], "std": [ 2.04, 2.70 ], "fq": 11
  },
  "bloody": {
    "dict": "anew", "word": "bloody", "stem": "bloodi",
    "avg": [ 2.90, 6.41 ], "std": [ 1.98, 2.00 ], "fq": 8
  },
  "blossom": {
    "dict": "anew", "word": "blossom", "stem": "blossom",
    "avg": [ 7.26, 5.03 ], "std": [ 1.18, 2.65 ], "fq": 7
  },
  "blubber": {
    "dict": "anew", "word": "blubber", "stem": "blubber",
    "avg": [ 3.52, 4.57 ], "std": [ 1.99, 2.38 ], "fq": 1
  },
  "blue": {
    "dict": "anew", "word": "blue", "stem": "blue",
    "avg": [ 6.76, 4.31 ], "std": [ 1.78, 2.20 ], "fq": 143
  },
  "board": {
    "dict": "anew", "word": "board", "stem": "board",
    "avg": [ 4.82, 3.36 ], "std": [ 1.23, 2.12 ], "fq": 239
  },
  "body": {
    "dict": "anew", "word": "body", "stem": "bodi",
    "avg": [ 5.55, 5.52 ], "std": [ 2.37, 2.63 ], "fq": 276
  },
  "bold": {
    "dict": "anew", "word": "bold", "stem": "bold",
    "avg": [ 6.80, 5.60 ], "std": [ 1.61, 2.21 ], "fq": 21
  },
  "bomb": {
    "dict": "anew", "word": "bomb", "stem": "bomb",
    "avg": [ 2.10, 7.15 ], "std": [ 1.19, 2.40 ], "fq": 36
  },
  "book": {
    "dict": "anew", "word": "book", "stem": "book",
    "avg": [ 5.72, 4.17 ], "std": [ 1.54, 2.49 ], "fq": 193
  },
  "bored": {
    "dict": "anew", "word": "bored", "stem": "bore",
    "avg": [ 2.95, 2.83 ], "std": [ 1.35, 2.31 ], "fq": 14
  },
  "bottle": {
    "dict": "anew", "word": "bottle", "stem": "bottl",
    "avg": [ 6.15, 4.79 ], "std": [ 1.49, 2.44 ], "fq": 76
  },
  "bouquet": {
    "dict": "anew", "word": "bouquet", "stem": "bouquet",
    "avg": [ 7.02, 5.46 ], "std": [ 1.84, 2.47 ], "fq": 4
  },
  "bowl": {
    "dict": "anew", "word": "bowl", "stem": "bowl",
    "avg": [ 5.33, 3.47 ], "std": [ 1.33, 2.12 ], "fq": 23
  },
  "boxer": {
    "dict": "anew", "word": "boxer", "stem": "boxer",
    "avg": [ 5.51, 5.12 ], "std": [ 1.80, 2.26 ], "fq": 1
  },
  "boy": {
    "dict": "anew", "word": "boy", "stem": "boy",
    "avg": [ 6.32, 4.58 ], "std": [ 1.60, 2.37 ], "fq": 242
  },
  "brave": {
    "dict": "anew", "word": "brave", "stem": "brave",
    "avg": [ 7.15, 6.15 ], "std": [ 1.64, 2.45 ], "fq": 24
  },
  "breast": {
    "dict": "anew", "word": "breast", "stem": "breast",
    "avg": [ 6.50, 5.37 ], "std": [ 1.78, 2.39 ], "fq": 11
  },
  "breeze": {
    "dict": "anew", "word": "breeze", "stem": "breez",
    "avg": [ 6.85, 4.37 ], "std": [ 1.71, 2.32 ], "fq": 14
  },
  "bride": {
    "dict": "anew", "word": "bride", "stem": "bride",
    "avg": [ 7.34, 5.55 ], "std": [ 1.71, 2.74 ], "fq": 33
  },
  "bright": {
    "dict": "anew", "word": "bright", "stem": "bright",
    "avg": [ 7.50, 5.40 ], "std": [ 1.55, 2.33 ], "fq": 87
  },
  "broken": {
    "dict": "anew", "word": "broken", "stem": "broken",
    "avg": [ 3.05, 5.43 ], "std": [ 1.92, 2.42 ], "fq": 63
  },
  "brother": {
    "dict": "anew", "word": "brother", "stem": "brother",
    "avg": [ 7.11, 4.71 ], "std": [ 2.17, 2.68 ], "fq": 73
  },
  "brutal": {
    "dict": "anew", "word": "brutal", "stem": "brutal",
    "avg": [ 2.80, 6.60 ], "std": [ 1.90, 2.36 ], "fq": 7
  },
  "building": {
    "dict": "anew", "word": "building", "stem": "build",
    "avg": [ 5.29, 3.92 ], "std": [ 1.15, 1.94 ], "fq": 160
  },
  "bullet": {
    "dict": "anew", "word": "bullet", "stem": "bullet",
    "avg": [ 3.29, 5.33 ], "std": [ 2.06, 2.48 ], "fq": 28
  },
  "bunny": {
    "dict": "anew", "word": "bunny", "stem": "bunni",
    "avg": [ 7.24, 4.06 ], "std": [ 1.32, 2.61 ], "fq": 1
  },
  "burdened": {
    "dict": "anew", "word": "burdened", "stem": "burden",
    "avg": [ 2.50, 5.63 ], "std": [ 1.32, 2.07 ], "fq": 4
  },
  "burial": {
    "dict": "anew", "word": "burial", "stem": "burial",
    "avg": [ 2.05, 5.08 ], "std": [ 1.41, 2.40 ], "fq": 11
  },
  "burn": {
    "dict": "anew", "word": "burn", "stem": "burn",
    "avg": [ 2.73, 6.22 ], "std": [ 1.72, 1.91 ], "fq": 15
  },
  "bus": {
    "dict": "anew", "word": "bus", "stem": "bus",
    "avg": [ 4.51, 3.55 ], "std": [ 1.57, 1.80 ], "fq": 34
  },
  "busybody": {
    "dict": "anew", "word": "busybody", "stem": "busybodi",
    "avg": [ 5.17, 4.84 ], "std": [ 2.02, 2.41 ], "fq": 0
  },
  "butter": {
    "dict": "anew", "word": "butter", "stem": "butter",
    "avg": [ 5.33, 3.17 ], "std": [ 1.20, 1.84 ], "fq": 27
  },
  "butterfly": {
    "dict": "anew", "word": "butterfly", "stem": "butterfli",
    "avg": [ 7.17, 3.47 ], "std": [ 1.20, 2.39 ], "fq": 2
  },
  "cabinet": {
    "dict": "anew", "word": "cabinet", "stem": "cabinet",
    "avg": [ 5.05, 3.43 ], "std": [ 0.31, 1.85 ], "fq": 17
  },
  "cake": {
    "dict": "anew", "word": "cake", "stem": "cake",
    "avg": [ 7.26, 5.00 ], "std": [ 1.27, 2.37 ], "fq": 9
  },
  "cancer": {
    "dict": "anew", "word": "cancer", "stem": "cancer",
    "avg": [ 1.50, 6.42 ], "std": [ 0.85, 2.83 ], "fq": 25
  },
  "candy": {
    "dict": "anew", "word": "candy", "stem": "candi",
    "avg": [ 6.54, 4.58 ], "std": [ 2.09, 2.40 ], "fq": 16
  },
  "cane": {
    "dict": "anew", "word": "cane", "stem": "cane",
    "avg": [ 4.00, 4.20 ], "std": [ 1.80, 1.93 ], "fq": 12
  },
  "cannon": {
    "dict": "anew", "word": "cannon", "stem": "cannon",
    "avg": [ 4.90, 4.71 ], "std": [ 2.20, 2.84 ], "fq": 7
  },
  "capable": {
    "dict": "anew", "word": "capable", "stem": "capabl",
    "avg": [ 7.16, 5.08 ], "std": [ 1.39, 2.07 ], "fq": 66
  },
  "car": {
    "dict": "anew", "word": "car", "stem": "car",
    "avg": [ 7.73, 6.24 ], "std": [ 1.63, 2.04 ], "fq": 274
  },
  "carcass": {
    "dict": "anew", "word": "carcass", "stem": "carcass",
    "avg": [ 3.34, 4.83 ], "std": [ 1.92, 2.07 ], "fq": 7
  },
  "carefree": {
    "dict": "anew", "word": "carefree", "stem": "carefre",
    "avg": [ 7.54, 4.17 ], "std": [ 1.38, 2.84 ], "fq": 9
  },
  "caress": {
    "dict": "anew", "word": "caress", "stem": "caress",
    "avg": [ 7.84, 5.14 ], "std": [ 1.16, 3.00 ], "fq": 1
  },
  "cash": {
    "dict": "anew", "word": "cash", "stem": "cash",
    "avg": [ 8.37, 7.37 ], "std": [ 1.00, 2.21 ], "fq": 36
  },
  "casino": {
    "dict": "anew", "word": "casino", "stem": "casino",
    "avg": [ 6.81, 6.51 ], "std": [ 1.66, 2.12 ], "fq": 2
  },
  "cat": {
    "dict": "anew", "word": "cat", "stem": "cat",
    "avg": [ 5.72, 4.38 ], "std": [ 2.43, 2.24 ], "fq": 0
  },
  "cell": {
    "dict": "anew", "word": "cell", "stem": "cell",
    "avg": [ 3.82, 4.08 ], "std": [ 1.70, 2.19 ], "fq": 65
  },
  "cellar": {
    "dict": "anew", "word": "cellar", "stem": "cellar",
    "avg": [ 4.32, 4.39 ], "std": [ 1.68, 2.33 ], "fq": 26
  },
  "cemetery": {
    "dict": "anew", "word": "cemetery", "stem": "cemeteri",
    "avg": [ 2.63, 4.82 ], "std": [ 1.40, 2.66 ], "fq": 15
  },
  "chair": {
    "dict": "anew", "word": "chair", "stem": "chair",
    "avg": [ 5.08, 3.15 ], "std": [ 0.98, 1.77 ], "fq": 66
  },
  "champ": {
    "dict": "anew", "word": "champ", "stem": "champ",
    "avg": [ 7.18, 6.00 ], "std": [ 1.97, 2.43 ], "fq": 1
  },
  "champion": {
    "dict": "anew", "word": "champion", "stem": "champion",
    "avg": [ 8.44, 5.85 ], "std": [ 0.90, 3.15 ], "fq": 23
  },
  "chance": {
    "dict": "anew", "word": "chance", "stem": "chanc",
    "avg": [ 6.02, 5.38 ], "std": [ 1.77, 2.58 ], "fq": 131
  },
  "chaos": {
    "dict": "anew", "word": "chaos", "stem": "chao",
    "avg": [ 4.17, 6.67 ], "std": [ 2.36, 2.06 ], "fq": 17
  },
  "charm": {
    "dict": "anew", "word": "charm", "stem": "charm",
    "avg": [ 6.77, 5.16 ], "std": [ 1.58, 2.25 ], "fq": 26
  },
  "cheer": {
    "dict": "anew", "word": "cheer", "stem": "cheer",
    "avg": [ 8.10, 6.12 ], "std": [ 1.17, 2.45 ], "fq": 8
  },
  "child": {
    "dict": "anew", "word": "child", "stem": "child",
    "avg": [ 7.08, 5.55 ], "std": [ 1.98, 2.29 ], "fq": 213
  },
  "chin": {
    "dict": "anew", "word": "chin", "stem": "chin",
    "avg": [ 5.29, 3.31 ], "std": [ 1.27, 1.98 ], "fq": 27
  },
  "chocolate": {
    "dict": "anew", "word": "chocolate", "stem": "chocol",
    "avg": [ 6.88, 5.29 ], "std": [ 1.89, 2.55 ], "fq": 9
  },
  "christmas": {
    "dict": "anew", "word": "christmas", "stem": "christma",
    "avg": [ 7.80, 6.27 ], "std": [ 1.55, 2.56 ], "fq": 27
  },
  "church": {
    "dict": "anew", "word": "church", "stem": "church",
    "avg": [ 6.28, 4.34 ], "std": [ 2.31, 2.45 ], "fq": 348
  },
  "circle": {
    "dict": "anew", "word": "circle", "stem": "circl",
    "avg": [ 5.67, 3.86 ], "std": [ 1.26, 2.13 ], "fq": 60
  },
  "circus": {
    "dict": "anew", "word": "circus", "stem": "circus",
    "avg": [ 7.30, 5.97 ], "std": [ 1.84, 2.59 ], "fq": 7
  },
  "city": {
    "dict": "anew", "word": "city", "stem": "citi",
    "avg": [ 6.03, 5.24 ], "std": [ 1.37, 2.53 ], "fq": 393
  },
  "cliff": {
    "dict": "anew", "word": "cliff", "stem": "cliff",
    "avg": [ 4.67, 6.25 ], "std": [ 2.08, 2.15 ], "fq": 11
  },
  "clock": {
    "dict": "anew", "word": "clock", "stem": "clock",
    "avg": [ 5.14, 4.02 ], "std": [ 1.54, 2.54 ], "fq": 20
  },
  "clothing": {
    "dict": "anew", "word": "clothing", "stem": "cloth",
    "avg": [ 6.54, 4.78 ], "std": [ 1.85, 2.88 ], "fq": 20
  },
  "clouds": {
    "dict": "anew", "word": "clouds", "stem": "cloud",
    "avg": [ 6.18, 3.30 ], "std": [ 2.18, 2.08 ], "fq": 38
  },
  "clumsy": {
    "dict": "anew", "word": "clumsy", "stem": "clumsi",
    "avg": [ 4.00, 5.18 ], "std": [ 2.22, 2.40 ], "fq": 6
  },
  "coarse": {
    "dict": "anew", "word": "coarse", "stem": "coars",
    "avg": [ 4.55, 4.21 ], "std": [ 1.42, 1.84 ], "fq": 10
  },
  "coast": {
    "dict": "anew", "word": "coast", "stem": "coast",
    "avg": [ 5.98, 4.59 ], "std": [ 1.86, 2.31 ], "fq": 61
  },
  "cockroach": {
    "dict": "anew", "word": "cockroach", "stem": "cockroach",
    "avg": [ 2.81, 6.11 ], "std": [ 2.11, 2.78 ], "fq": 2
  },
  "coffin": {
    "dict": "anew", "word": "coffin", "stem": "coffin",
    "avg": [ 2.56, 5.03 ], "std": [ 1.96, 2.79 ], "fq": 7
  },
  "coin": {
    "dict": "anew", "word": "coin", "stem": "coin",
    "avg": [ 6.02, 4.29 ], "std": [ 1.96, 2.48 ], "fq": 10
  },
  "cold": {
    "dict": "anew", "word": "cold", "stem": "cold",
    "avg": [ 4.02, 5.19 ], "std": [ 1.99, 2.23 ], "fq": 171
  },
  "color": {
    "dict": "anew", "word": "color", "stem": "color",
    "avg": [ 7.02, 4.73 ], "std": [ 1.57, 2.64 ], "fq": 141
  },
  "column": {
    "dict": "anew", "word": "column", "stem": "column",
    "avg": [ 5.17, 3.62 ], "std": [ 0.85, 1.91 ], "fq": 71
  },
  "comedy": {
    "dict": "anew", "word": "comedy", "stem": "comedi",
    "avg": [ 8.37, 5.85 ], "std": [ 0.94, 2.81 ], "fq": 39
  },
  "comfort": {
    "dict": "anew", "word": "comfort", "stem": "comfort",
    "avg": [ 7.07, 3.93 ], "std": [ 2.14, 2.85 ], "fq": 43
  },
  "computer": {
    "dict": "anew", "word": "computer", "stem": "comput",
    "avg": [ 6.24, 4.75 ], "std": [ 1.61, 1.93 ], "fq": 13
  },
  "concentrate": {
    "dict": "anew", "word": "concentrate", "stem": "concentr",
    "avg": [ 5.20, 4.65 ], "std": [ 1.28, 2.13 ], "fq": 11
  },
  "confident": {
    "dict": "anew", "word": "confident", "stem": "confid",
    "avg": [ 7.98, 6.22 ], "std": [ 1.29, 2.41 ], "fq": 16
  },
  "confused": {
    "dict": "anew", "word": "confused", "stem": "confus",
    "avg": [ 3.21, 6.03 ], "std": [ 1.51, 1.88 ], "fq": 44
  },
  "consoled": {
    "dict": "anew", "word": "consoled", "stem": "consol",
    "avg": [ 5.78, 4.53 ], "std": [ 1.64, 2.22 ], "fq": 2
  },
  "contempt": {
    "dict": "anew", "word": "contempt", "stem": "contempt",
    "avg": [ 3.85, 5.28 ], "std": [ 2.13, 2.04 ], "fq": 15
  },
  "contents": {
    "dict": "anew", "word": "contents", "stem": "content",
    "avg": [ 4.89, 4.32 ], "std": [ 0.89, 2.14 ], "fq": 16
  },
  "context": {
    "dict": "anew", "word": "context", "stem": "context",
    "avg": [ 5.20, 4.22 ], "std": [ 1.38, 2.24 ], "fq": 2
  },
  "controlling": {
    "dict": "anew", "word": "controlling", "stem": "control",
    "avg": [ 3.80, 6.10 ], "std": [ 2.25, 2.19 ], "fq": 23
  },
  "cook": {
    "dict": "anew", "word": "cook", "stem": "cook",
    "avg": [ 6.16, 4.44 ], "std": [ 1.89, 1.96 ], "fq": 47
  },
  "cord": {
    "dict": "anew", "word": "cord", "stem": "cord",
    "avg": [ 5.10, 3.54 ], "std": [ 1.09, 2.09 ], "fq": 6
  },
  "cork": {
    "dict": "anew", "word": "cork", "stem": "cork",
    "avg": [ 5.22, 3.80 ], "std": [ 1.13, 2.18 ], "fq": 9
  },
  "corner": {
    "dict": "anew", "word": "corner", "stem": "corner",
    "avg": [ 4.36, 3.91 ], "std": [ 1.21, 1.92 ], "fq": 115
  },
  "corpse": {
    "dict": "anew", "word": "corpse", "stem": "corps",
    "avg": [ 2.18, 4.74 ], "std": [ 1.48, 2.94 ], "fq": 7
  },
  "corridor": {
    "dict": "anew", "word": "corridor", "stem": "corridor",
    "avg": [ 4.88, 3.63 ], "std": [ 1.14, 2.41 ], "fq": 17
  },
  "corrupt": {
    "dict": "anew", "word": "corrupt", "stem": "corrupt",
    "avg": [ 3.32, 4.67 ], "std": [ 2.32, 2.35 ], "fq": 8
  },
  "cottage": {
    "dict": "anew", "word": "cottage", "stem": "cottag",
    "avg": [ 6.45, 3.39 ], "std": [ 1.52, 2.54 ], "fq": 19
  },
  "couple": {
    "dict": "anew", "word": "couple", "stem": "coupl",
    "avg": [ 7.41, 6.39 ], "std": [ 1.97, 2.31 ], "fq": 122
  },
  "cow": {
    "dict": "anew", "word": "cow", "stem": "cow",
    "avg": [ 5.57, 3.49 ], "std": [ 1.53, 2.13 ], "fq": 29
  },
  "coward": {
    "dict": "anew", "word": "coward", "stem": "coward",
    "avg": [ 2.74, 4.07 ], "std": [ 1.64, 2.19 ], "fq": 8
  },
  "cozy": {
    "dict": "anew", "word": "cozy", "stem": "cozi",
    "avg": [ 7.39, 3.32 ], "std": [ 1.53, 2.28 ], "fq": 1
  },
  "crash": {
    "dict": "anew", "word": "crash", "stem": "crash",
    "avg": [ 2.31, 6.95 ], "std": [ 1.44, 2.44 ], "fq": 20
  },
  "crime": {
    "dict": "anew", "word": "crime", "stem": "crime",
    "avg": [ 2.89, 5.41 ], "std": [ 2.06, 2.69 ], "fq": 34
  },
  "criminal": {
    "dict": "anew", "word": "criminal", "stem": "crimin",
    "avg": [ 2.93, 4.79 ], "std": [ 1.66, 2.51 ], "fq": 24
  },
  "crisis": {
    "dict": "anew", "word": "crisis", "stem": "crisi",
    "avg": [ 2.74, 5.44 ], "std": [ 2.23, 3.07 ], "fq": 82
  },
  "crown": {
    "dict": "anew", "word": "crown", "stem": "crown",
    "avg": [ 6.58, 4.28 ], "std": [ 1.42, 2.53 ], "fq": 19
  },
  "crucify": {
    "dict": "anew", "word": "crucify", "stem": "crucifi",
    "avg": [ 2.23, 6.47 ], "std": [ 1.72, 2.47 ], "fq": 2
  },
  "crude": {
    "dict": "anew", "word": "crude", "stem": "crude",
    "avg": [ 3.12, 5.07 ], "std": [ 1.65, 2.37 ], "fq": 15
  },
  "cruel": {
    "dict": "anew", "word": "cruel", "stem": "cruel",
    "avg": [ 1.97, 5.68 ], "std": [ 1.67, 2.65 ], "fq": 15
  },
  "crushed": {
    "dict": "anew", "word": "crushed", "stem": "crush",
    "avg": [ 2.21, 5.52 ], "std": [ 1.74, 2.87 ], "fq": 10
  },
  "crutch": {
    "dict": "anew", "word": "crutch", "stem": "crutch",
    "avg": [ 3.43, 4.14 ], "std": [ 1.62, 2.05 ], "fq": 1
  },
  "cuddle": {
    "dict": "anew", "word": "cuddle", "stem": "cuddl",
    "avg": [ 7.72, 4.40 ], "std": [ 1.92, 2.67 ], "fq": 0
  },
  "cuisine": {
    "dict": "anew", "word": "cuisine", "stem": "cuisin",
    "avg": [ 6.64, 4.39 ], "std": [ 1.48, 1.99 ], "fq": 1
  },
  "curious": {
    "dict": "anew", "word": "curious", "stem": "curious",
    "avg": [ 6.08, 5.82 ], "std": [ 1.63, 1.64 ], "fq": 46
  },
  "curtains": {
    "dict": "anew", "word": "curtains", "stem": "curtain",
    "avg": [ 4.83, 3.67 ], "std": [ 0.83, 1.83 ], "fq": 8
  },
  "custom": {
    "dict": "anew", "word": "custom", "stem": "custom",
    "avg": [ 5.85, 4.66 ], "std": [ 1.53, 2.12 ], "fq": 14
  },
  "cut": {
    "dict": "anew", "word": "cut", "stem": "cut",
    "avg": [ 3.64, 5.00 ], "std": [ 2.08, 2.32 ], "fq": 192
  },
  "cute": {
    "dict": "anew", "word": "cute", "stem": "cute",
    "avg": [ 7.62, 5.53 ], "std": [ 1.01, 2.71 ], "fq": 5
  },
  "cyclone": {
    "dict": "anew", "word": "cyclone", "stem": "cyclon",
    "avg": [ 3.60, 6.36 ], "std": [ 2.38, 2.89 ], "fq": 0
  },
  "dagger": {
    "dict": "anew", "word": "dagger", "stem": "dagger",
    "avg": [ 3.38, 6.14 ], "std": [ 1.77, 2.64 ], "fq": 1
  },
  "damage": {
    "dict": "anew", "word": "damage", "stem": "damag",
    "avg": [ 3.05, 5.57 ], "std": [ 1.65, 2.26 ], "fq": 33
  },
  "dancer": {
    "dict": "anew", "word": "dancer", "stem": "dancer",
    "avg": [ 7.14, 6.00 ], "std": [ 1.56, 2.20 ], "fq": 31
  },
  "danger": {
    "dict": "anew", "word": "danger", "stem": "danger",
    "avg": [ 2.95, 7.32 ], "std": [ 2.22, 2.07 ], "fq": 70
  },
  "dark": {
    "dict": "anew", "word": "dark", "stem": "dark",
    "avg": [ 4.71, 4.28 ], "std": [ 2.36, 2.21 ], "fq": 185
  },
  "dawn": {
    "dict": "anew", "word": "dawn", "stem": "dawn",
    "avg": [ 6.16, 4.39 ], "std": [ 2.33, 2.81 ], "fq": 28
  },
  "daylight": {
    "dict": "anew", "word": "daylight", "stem": "daylight",
    "avg": [ 6.80, 4.77 ], "std": [ 2.17, 2.50 ], "fq": 15
  },
  "dazzle": {
    "dict": "anew", "word": "dazzle", "stem": "dazzl",
    "avg": [ 7.29, 6.33 ], "std": [ 1.09, 2.02 ], "fq": 1
  },
  "dead": {
    "dict": "anew", "word": "dead", "stem": "dead",
    "avg": [ 1.94, 5.73 ], "std": [ 1.76, 2.73 ], "fq": 174
  },
  "death": {
    "dict": "anew", "word": "death", "stem": "death",
    "avg": [ 1.61, 4.59 ], "std": [ 1.40, 3.07 ], "fq": 277
  },
  "debt": {
    "dict": "anew", "word": "debt", "stem": "debt",
    "avg": [ 2.22, 5.68 ], "std": [ 1.17, 2.74 ], "fq": 13
  },
  "deceit": {
    "dict": "anew", "word": "deceit", "stem": "deceit",
    "avg": [ 2.90, 5.68 ], "std": [ 1.63, 2.46 ], "fq": 2
  },
  "decompose": {
    "dict": "anew", "word": "decompose", "stem": "decompos",
    "avg": [ 3.20, 4.65 ], "std": [ 1.81, 2.39 ], "fq": 1
  },
  "decorate": {
    "dict": "anew", "word": "decorate", "stem": "decor",
    "avg": [ 6.93, 5.14 ], "std": [ 1.30, 2.39 ], "fq": 2
  },
  "defeated": {
    "dict": "anew", "word": "defeated", "stem": "defeat",
    "avg": [ 2.34, 5.09 ], "std": [ 1.66, 3.00 ], "fq": 15
  },
  "defiant": {
    "dict": "anew", "word": "defiant", "stem": "defiant",
    "avg": [ 4.26, 6.10 ], "std": [ 2.12, 2.51 ], "fq": 3
  },
  "deformed": {
    "dict": "anew", "word": "deformed", "stem": "deform",
    "avg": [ 2.41, 4.07 ], "std": [ 1.66, 2.34 ], "fq": 0
  },
  "delayed": {
    "dict": "anew", "word": "delayed", "stem": "delay",
    "avg": [ 3.07, 5.62 ], "std": [ 1.74, 2.39 ], "fq": 25
  },
  "delight": {
    "dict": "anew", "word": "delight", "stem": "delight",
    "avg": [ 8.26, 5.44 ], "std": [ 1.04, 2.88 ], "fq": 29
  },
  "demon": {
    "dict": "anew", "word": "demon", "stem": "demon",
    "avg": [ 2.11, 6.76 ], "std": [ 1.56, 2.68 ], "fq": 9
  },
  "dentist": {
    "dict": "anew", "word": "dentist", "stem": "dentist",
    "avg": [ 4.02, 5.73 ], "std": [ 2.23, 2.13 ], "fq": 12
  },
  "depressed": {
    "dict": "anew", "word": "depressed", "stem": "depress",
    "avg": [ 1.83, 4.72 ], "std": [ 1.42, 2.95 ], "fq": 11
  },
  "depression": {
    "dict": "anew", "word": "depression", "stem": "depress",
    "avg": [ 1.85, 4.54 ], "std": [ 1.67, 3.19 ], "fq": 24
  },
  "derelict": {
    "dict": "anew", "word": "derelict", "stem": "derelict",
    "avg": [ 4.28, 4.10 ], "std": [ 1.84, 1.94 ], "fq": 1
  },
  "deserter": {
    "dict": "anew", "word": "deserter", "stem": "desert",
    "avg": [ 2.45, 5.50 ], "std": [ 1.80, 2.55 ], "fq": 0
  },
  "desire": {
    "dict": "anew", "word": "desire", "stem": "desir",
    "avg": [ 7.69, 7.35 ], "std": [ 1.39, 1.76 ], "fq": 79
  },
  "despairing": {
    "dict": "anew", "word": "despairing", "stem": "despair",
    "avg": [ 2.43, 5.68 ], "std": [ 1.47, 2.37 ], "fq": 4
  },
  "despise": {
    "dict": "anew", "word": "despise", "stem": "despis",
    "avg": [ 2.03, 6.28 ], "std": [ 1.38, 2.43 ], "fq": 7
  },
  "destroy": {
    "dict": "anew", "word": "destroy", "stem": "destroy",
    "avg": [ 2.64, 6.83 ], "std": [ 2.03, 2.38 ], "fq": 48
  },
  "destruction": {
    "dict": "anew", "word": "destruction", "stem": "destruct",
    "avg": [ 3.16, 5.82 ], "std": [ 2.44, 2.71 ], "fq": 38
  },
  "detached": {
    "dict": "anew", "word": "detached", "stem": "detach",
    "avg": [ 3.86, 4.26 ], "std": [ 1.88, 2.57 ], "fq": 12
  },
  "detail": {
    "dict": "anew", "word": "detail", "stem": "detail",
    "avg": [ 5.55, 4.10 ], "std": [ 1.58, 2.24 ], "fq": 72
  },
  "detest": {
    "dict": "anew", "word": "detest", "stem": "detest",
    "avg": [ 2.17, 6.06 ], "std": [ 1.30, 2.39 ], "fq": 1
  },
  "devil": {
    "dict": "anew", "word": "devil", "stem": "devil",
    "avg": [ 2.21, 6.07 ], "std": [ 1.99, 2.61 ], "fq": 25
  },
  "devoted": {
    "dict": "anew", "word": "devoted", "stem": "devot",
    "avg": [ 7.41, 5.23 ], "std": [ 1.37, 2.21 ], "fq": 51
  },
  "diamond": {
    "dict": "anew", "word": "diamond", "stem": "diamond",
    "avg": [ 7.92, 5.53 ], "std": [ 1.20, 2.96 ], "fq": 8
  },
  "dignified": {
    "dict": "anew", "word": "dignified", "stem": "dignifi",
    "avg": [ 7.10, 4.12 ], "std": [ 1.26, 2.29 ], "fq": 7
  },
  "dinner": {
    "dict": "anew", "word": "dinner", "stem": "dinner",
    "avg": [ 7.16, 5.43 ], "std": [ 1.50, 2.14 ], "fq": 91
  },
  "diploma": {
    "dict": "anew", "word": "diploma", "stem": "diploma",
    "avg": [ 8.00, 5.67 ], "std": [ 1.39, 2.80 ], "fq": 0
  },
  "dirt": {
    "dict": "anew", "word": "dirt", "stem": "dirt",
    "avg": [ 4.17, 3.76 ], "std": [ 1.77, 2.26 ], "fq": 43
  },
  "dirty": {
    "dict": "anew", "word": "dirty", "stem": "dirti",
    "avg": [ 3.08, 4.88 ], "std": [ 2.05, 2.29 ], "fq": 36
  },
  "disappoint": {
    "dict": "anew", "word": "disappoint", "stem": "disappoint",
    "avg": [ 2.39, 4.92 ], "std": [ 1.44, 2.64 ], "fq": 0
  },
  "disaster": {
    "dict": "anew", "word": "disaster", "stem": "disast",
    "avg": [ 1.73, 6.33 ], "std": [ 1.13, 2.70 ], "fq": 26
  },
  "discomfort": {
    "dict": "anew", "word": "discomfort", "stem": "discomfort",
    "avg": [ 2.19, 4.17 ], "std": [ 1.23, 2.44 ], "fq": 7
  },
  "discouraged": {
    "dict": "anew", "word": "discouraged", "stem": "discourag",
    "avg": [ 3.00, 4.53 ], "std": [ 2.16, 2.11 ], "fq": 15
  },
  "disdainful": {
    "dict": "anew", "word": "disdainful", "stem": "disdain",
    "avg": [ 3.68, 5.04 ], "std": [ 1.90, 2.14 ], "fq": 2
  },
  "disgusted": {
    "dict": "anew", "word": "disgusted", "stem": "disgust",
    "avg": [ 2.45, 5.42 ], "std": [ 1.41, 2.59 ], "fq": 6
  },
  "disloyal": {
    "dict": "anew", "word": "disloyal", "stem": "disloy",
    "avg": [ 1.93, 6.56 ], "std": [ 1.61, 2.21 ], "fq": 2
  },
  "displeased": {
    "dict": "anew", "word": "displeased", "stem": "displeas",
    "avg": [ 2.79, 5.64 ], "std": [ 2.23, 2.48 ], "fq": 7
  },
  "distressed": {
    "dict": "anew", "word": "distressed", "stem": "distress",
    "avg": [ 1.94, 6.40 ], "std": [ 1.10, 2.38 ], "fq": 4
  },
  "disturb": {
    "dict": "anew", "word": "disturb", "stem": "disturb",
    "avg": [ 3.66, 5.80 ], "std": [ 2.00, 2.39 ], "fq": 10
  },
  "diver": {
    "dict": "anew", "word": "diver", "stem": "diver",
    "avg": [ 6.45, 5.04 ], "std": [ 1.55, 2.10 ], "fq": 1
  },
  "divorce": {
    "dict": "anew", "word": "divorce", "stem": "divorc",
    "avg": [ 2.22, 6.33 ], "std": [ 1.88, 2.71 ], "fq": 29
  },
  "doctor": {
    "dict": "anew", "word": "doctor", "stem": "doctor",
    "avg": [ 5.20, 5.86 ], "std": [ 2.54, 2.70 ], "fq": 100
  },
  "dog": {
    "dict": "anew", "word": "dog", "stem": "dog",
    "avg": [ 7.57, 5.76 ], "std": [ 1.66, 2.50 ], "fq": 75
  },
  "doll": {
    "dict": "anew", "word": "doll", "stem": "doll",
    "avg": [ 6.09, 4.24 ], "std": [ 1.96, 2.43 ], "fq": 10
  },
  "dollar": {
    "dict": "anew", "word": "dollar", "stem": "dollar",
    "avg": [ 7.47, 6.07 ], "std": [ 1.72, 2.67 ], "fq": 46
  },
  "door": {
    "dict": "anew", "word": "door", "stem": "door",
    "avg": [ 5.13, 3.80 ], "std": [ 1.44, 2.29 ], "fq": 312
  },
  "dove": {
    "dict": "anew", "word": "dove", "stem": "dove",
    "avg": [ 6.90, 3.79 ], "std": [ 1.54, 2.28 ], "fq": 4
  },
  "dreadful": {
    "dict": "anew", "word": "dreadful", "stem": "dread",
    "avg": [ 2.26, 5.84 ], "std": [ 1.91, 2.62 ], "fq": 10
  },
  "dream": {
    "dict": "anew", "word": "dream", "stem": "dream",
    "avg": [ 6.73, 4.53 ], "std": [ 1.75, 2.72 ], "fq": 64
  },
  "dreary": {
    "dict": "anew", "word": "dreary", "stem": "dreari",
    "avg": [ 3.05, 2.98 ], "std": [ 1.58, 2.18 ], "fq": 6
  },
  "dress": {
    "dict": "anew", "word": "dress", "stem": "dress",
    "avg": [ 6.41, 4.05 ], "std": [ 1.34, 1.89 ], "fq": 67
  },
  "drown": {
    "dict": "anew", "word": "drown", "stem": "drown",
    "avg": [ 1.92, 6.57 ], "std": [ 1.48, 2.33 ], "fq": 3
  },
  "dummy": {
    "dict": "anew", "word": "dummy", "stem": "dummi",
    "avg": [ 3.38, 4.35 ], "std": [ 1.70, 2.25 ], "fq": 3
  },
  "dump": {
    "dict": "anew", "word": "dump", "stem": "dump",
    "avg": [ 3.21, 4.12 ], "std": [ 1.87, 2.36 ], "fq": 4
  },
  "dustpan": {
    "dict": "anew", "word": "dustpan", "stem": "dustpan",
    "avg": [ 3.98, 3.43 ], "std": [ 1.68, 2.00 ], "fq": 0
  },
  "earth": {
    "dict": "anew", "word": "earth", "stem": "earth",
    "avg": [ 7.15, 4.24 ], "std": [ 1.67, 2.49 ], "fq": 150
  },
  "easy": {
    "dict": "anew", "word": "easy", "stem": "easi",
    "avg": [ 7.10, 4.48 ], "std": [ 1.91, 2.82 ], "fq": 125
  },
  "easygoing": {
    "dict": "anew", "word": "easygoing", "stem": "easygo",
    "avg": [ 7.20, 4.30 ], "std": [ 1.50, 2.52 ], "fq": 1
  },
  "eat": {
    "dict": "anew", "word": "eat", "stem": "eat",
    "avg": [ 7.47, 5.69 ], "std": [ 1.73, 2.51 ], "fq": 61
  },
  "ecstasy": {
    "dict": "anew", "word": "ecstasy", "stem": "ecstasi",
    "avg": [ 7.98, 7.38 ], "std": [ 1.52, 1.92 ], "fq": 6
  },
  "education": {
    "dict": "anew", "word": "education", "stem": "educ",
    "avg": [ 6.69, 5.74 ], "std": [ 1.77, 2.46 ], "fq": 214
  },
  "egg": {
    "dict": "anew", "word": "egg", "stem": "egg",
    "avg": [ 5.29, 3.76 ], "std": [ 1.82, 2.39 ], "fq": 12
  },
  "elated": {
    "dict": "anew", "word": "elated", "stem": "elat",
    "avg": [ 7.45, 6.21 ], "std": [ 1.77, 2.30 ], "fq": 3
  },
  "elbow": {
    "dict": "anew", "word": "elbow", "stem": "elbow",
    "avg": [ 5.12, 3.81 ], "std": [ 0.92, 2.14 ], "fq": 10
  },
  "elegant": {
    "dict": "anew", "word": "elegant", "stem": "eleg",
    "avg": [ 7.43, 4.53 ], "std": [ 1.26, 2.65 ], "fq": 14
  },
  "elevator": {
    "dict": "anew", "word": "elevator", "stem": "elev",
    "avg": [ 5.44, 4.16 ], "std": [ 1.18, 1.99 ], "fq": 12
  },
  "embarrassed": {
    "dict": "anew", "word": "embarrassed", "stem": "embarrass",
    "avg": [ 3.03, 5.87 ], "std": [ 1.85, 2.55 ], "fq": 8
  },
  "embattled": {
    "dict": "anew", "word": "embattled", "stem": "embattl",
    "avg": [ 4.39, 5.36 ], "std": [ 1.63, 2.37 ], "fq": 1
  },
  "employment": {
    "dict": "anew", "word": "employment", "stem": "employ",
    "avg": [ 6.47, 5.28 ], "std": [ 1.81, 2.12 ], "fq": 47
  },
  "engaged": {
    "dict": "anew", "word": "engaged", "stem": "engag",
    "avg": [ 8.00, 6.77 ], "std": [ 1.38, 2.07 ], "fq": 47
  },
  "engine": {
    "dict": "anew", "word": "engine", "stem": "engin",
    "avg": [ 5.20, 3.98 ], "std": [ 1.18, 2.33 ], "fq": 50
  },
  "enjoyment": {
    "dict": "anew", "word": "enjoyment", "stem": "enjoy",
    "avg": [ 7.80, 5.20 ], "std": [ 1.20, 2.72 ], "fq": 21
  },
  "ennui": {
    "dict": "anew", "word": "ennui", "stem": "ennui",
    "avg": [ 5.09, 4.40 ], "std": [ 1.76, 2.33 ], "fq": 0
  },
  "enraged": {
    "dict": "anew", "word": "enraged", "stem": "enrag",
    "avg": [ 2.46, 7.97 ], "std": [ 1.65, 2.17 ], "fq": 1
  },
  "erotic": {
    "dict": "anew", "word": "erotic", "stem": "erot",
    "avg": [ 7.43, 7.24 ], "std": [ 1.53, 1.97 ], "fq": 8
  },
  "errand": {
    "dict": "anew", "word": "errand", "stem": "errand",
    "avg": [ 4.58, 3.85 ], "std": [ 1.74, 1.92 ], "fq": 7
  },
  "event": {
    "dict": "anew", "word": "event", "stem": "event",
    "avg": [ 6.21, 5.10 ], "std": [ 1.63, 2.40 ], "fq": 81
  },
  "evil": {
    "dict": "anew", "word": "evil", "stem": "evil",
    "avg": [ 3.23, 6.39 ], "std": [ 2.64, 2.44 ], "fq": 72
  },
  "excellence": {
    "dict": "anew", "word": "excellence", "stem": "excel",
    "avg": [ 8.38, 5.54 ], "std": [ 0.96, 2.67 ], "fq": 15
  },
  "excitement": {
    "dict": "anew", "word": "excitement", "stem": "excit",
    "avg": [ 7.50, 7.67 ], "std": [ 2.20, 1.91 ], "fq": 32
  },
  "excuse": {
    "dict": "anew", "word": "excuse", "stem": "excus",
    "avg": [ 4.05, 4.48 ], "std": [ 1.41, 2.29 ], "fq": 27
  },
  "execution": {
    "dict": "anew", "word": "execution", "stem": "execut",
    "avg": [ 2.37, 5.71 ], "std": [ 2.06, 2.74 ], "fq": 15
  },
  "exercise": {
    "dict": "anew", "word": "exercise", "stem": "exercis",
    "avg": [ 7.13, 6.84 ], "std": [ 1.58, 2.06 ], "fq": 58
  },
  "fabric": {
    "dict": "anew", "word": "fabric", "stem": "fabric",
    "avg": [ 5.30, 4.14 ], "std": [ 1.20, 1.98 ], "fq": 15
  },
  "face": {
    "dict": "anew", "word": "face", "stem": "face",
    "avg": [ 6.39, 5.04 ], "std": [ 1.60, 2.18 ], "fq": 371
  },
  "failure": {
    "dict": "anew", "word": "failure", "stem": "failur",
    "avg": [ 1.70, 4.95 ], "std": [ 1.07, 2.81 ], "fq": 89
  },
  "fall": {
    "dict": "anew", "word": "fall", "stem": "fall",
    "avg": [ 4.09, 4.70 ], "std": [ 2.21, 2.48 ], "fq": 147
  },
  "FALSE": {
    "dict": "anew", "word": "FALSE", "stem": "fals",
    "avg": [ 3.27, 3.43 ], "std": [ 1.40, 2.09 ], "fq": 29
  },
  "fame": {
    "dict": "anew", "word": "fame", "stem": "fame",
    "avg": [ 7.93, 6.55 ], "std": [ 1.29, 2.46 ], "fq": 18
  },
  "family": {
    "dict": "anew", "word": "family", "stem": "famili",
    "avg": [ 7.65, 4.80 ], "std": [ 1.55, 2.71 ], "fq": 331
  },
  "famous": {
    "dict": "anew", "word": "famous", "stem": "famous",
    "avg": [ 6.98, 5.73 ], "std": [ 2.07, 2.68 ], "fq": 89
  },
  "fantasy": {
    "dict": "anew", "word": "fantasy", "stem": "fantasi",
    "avg": [ 7.41, 5.14 ], "std": [ 1.90, 2.82 ], "fq": 14
  },
  "farm": {
    "dict": "anew", "word": "farm", "stem": "farm",
    "avg": [ 5.53, 3.90 ], "std": [ 1.85, 1.95 ], "fq": 125
  },
  "fascinate": {
    "dict": "anew", "word": "fascinate", "stem": "fascin",
    "avg": [ 7.34, 5.83 ], "std": [ 1.68, 2.73 ], "fq": 3
  },
  "fat": {
    "dict": "anew", "word": "fat", "stem": "fat",
    "avg": [ 2.28, 4.81 ], "std": [ 1.92, 2.80 ], "fq": 60
  },
  "father": {
    "dict": "anew", "word": "father", "stem": "father",
    "avg": [ 7.08, 5.92 ], "std": [ 2.20, 2.60 ], "fq": 383
  },
  "fatigued": {
    "dict": "anew", "word": "fatigued", "stem": "fatigu",
    "avg": [ 3.28, 2.64 ], "std": [ 1.43, 2.19 ], "fq": 3
  },
  "fault": {
    "dict": "anew", "word": "fault", "stem": "fault",
    "avg": [ 3.43, 4.07 ], "std": [ 1.38, 1.69 ], "fq": 22
  },
  "favor": {
    "dict": "anew", "word": "favor", "stem": "favor",
    "avg": [ 6.46, 4.54 ], "std": [ 1.52, 1.86 ], "fq": 78
  },
  "fear": {
    "dict": "anew", "word": "fear", "stem": "fear",
    "avg": [ 2.76, 6.96 ], "std": [ 2.12, 2.17 ], "fq": 127
  },
  "fearful": {
    "dict": "anew", "word": "fearful", "stem": "fear",
    "avg": [ 2.25, 6.33 ], "std": [ 1.18, 2.28 ], "fq": 13
  },
  "feeble": {
    "dict": "anew", "word": "feeble", "stem": "feebl",
    "avg": [ 3.26, 4.10 ], "std": [ 1.47, 2.07 ], "fq": 8
  },
  "festive": {
    "dict": "anew", "word": "festive", "stem": "festiv",
    "avg": [ 7.30, 6.58 ], "std": [ 2.26, 2.29 ], "fq": 2
  },
  "fever": {
    "dict": "anew", "word": "fever", "stem": "fever",
    "avg": [ 2.76, 4.29 ], "std": [ 1.64, 2.31 ], "fq": 19
  },
  "field": {
    "dict": "anew", "word": "field", "stem": "field",
    "avg": [ 6.20, 4.08 ], "std": [ 1.37, 2.41 ], "fq": 274
  },
  "fight": {
    "dict": "anew", "word": "fight", "stem": "fight",
    "avg": [ 3.76, 7.15 ], "std": [ 2.63, 2.19 ], "fq": 98
  },
  "filth": {
    "dict": "anew", "word": "filth", "stem": "filth",
    "avg": [ 2.47, 5.12 ], "std": [ 1.68, 2.32 ], "fq": 2
  },
  "finger": {
    "dict": "anew", "word": "finger", "stem": "finger",
    "avg": [ 5.29, 3.78 ], "std": [ 1.42, 2.42 ], "fq": 40
  },
  "fire": {
    "dict": "anew", "word": "fire", "stem": "fire",
    "avg": [ 3.22, 7.17 ], "std": [ 2.06, 2.06 ], "fq": 187
  },
  "fireworks": {
    "dict": "anew", "word": "fireworks", "stem": "firework",
    "avg": [ 7.55, 6.67 ], "std": [ 1.50, 2.12 ], "fq": 5
  },
  "fish": {
    "dict": "anew", "word": "fish", "stem": "fish",
    "avg": [ 6.04, 4.00 ], "std": [ 1.94, 2.19 ], "fq": 35
  },
  "flabby": {
    "dict": "anew", "word": "flabby", "stem": "flabbi",
    "avg": [ 2.66, 4.82 ], "std": [ 1.87, 2.81 ], "fq": 0
  },
  "flag": {
    "dict": "anew", "word": "flag", "stem": "flag",
    "avg": [ 6.02, 4.60 ], "std": [ 1.66, 2.35 ], "fq": 16
  },
  "flirt": {
    "dict": "anew", "word": "flirt", "stem": "flirt",
    "avg": [ 7.52, 6.91 ], "std": [ 1.19, 1.69 ], "fq": 1
  },
  "flood": {
    "dict": "anew", "word": "flood", "stem": "flood",
    "avg": [ 3.19, 6.00 ], "std": [ 1.66, 2.02 ], "fq": 19
  },
  "flower": {
    "dict": "anew", "word": "flower", "stem": "flower",
    "avg": [ 6.64, 4.00 ], "std": [ 1.78, 2.44 ], "fq": 23
  },
  "foam": {
    "dict": "anew", "word": "foam", "stem": "foam",
    "avg": [ 6.07, 5.26 ], "std": [ 2.03, 2.54 ], "fq": 37
  },
  "food": {
    "dict": "anew", "word": "food", "stem": "food",
    "avg": [ 7.65, 5.92 ], "std": [ 1.37, 2.11 ], "fq": 147
  },
  "foot": {
    "dict": "anew", "word": "foot", "stem": "foot",
    "avg": [ 5.02, 3.27 ], "std": [ 0.93, 1.98 ], "fq": 70
  },
  "fork": {
    "dict": "anew", "word": "fork", "stem": "fork",
    "avg": [ 5.29, 3.96 ], "std": [ 0.97, 1.94 ], "fq": 14
  },
  "foul": {
    "dict": "anew", "word": "foul", "stem": "foul",
    "avg": [ 2.81, 4.93 ], "std": [ 1.52, 2.23 ], "fq": 4
  },
  "fragrance": {
    "dict": "anew", "word": "fragrance", "stem": "fragranc",
    "avg": [ 6.07, 4.79 ], "std": [ 1.97, 2.54 ], "fq": 6
  },
  "fraud": {
    "dict": "anew", "word": "fraud", "stem": "fraud",
    "avg": [ 2.67, 5.75 ], "std": [ 1.66, 2.45 ], "fq": 8
  },
  "free": {
    "dict": "anew", "word": "free", "stem": "free",
    "avg": [ 8.26, 5.15 ], "std": [ 1.31, 3.04 ], "fq": 260
  },
  "freedom": {
    "dict": "anew", "word": "freedom", "stem": "freedom",
    "avg": [ 7.58, 5.52 ], "std": [ 2.04, 2.72 ], "fq": 128
  },
  "friend": {
    "dict": "anew", "word": "friend", "stem": "friend",
    "avg": [ 7.74, 5.74 ], "std": [ 1.24, 2.57 ], "fq": 133
  },
  "friendly": {
    "dict": "anew", "word": "friendly", "stem": "friend",
    "avg": [ 8.43, 5.11 ], "std": [ 1.08, 2.96 ], "fq": 61
  },
  "frigid": {
    "dict": "anew", "word": "frigid", "stem": "frigid",
    "avg": [ 3.50, 4.75 ], "std": [ 1.85, 2.56 ], "fq": 5
  },
  "frog": {
    "dict": "anew", "word": "frog", "stem": "frog",
    "avg": [ 5.71, 4.54 ], "std": [ 1.74, 2.03 ], "fq": 1
  },
  "frustrated": {
    "dict": "anew", "word": "frustrated", "stem": "frustrat",
    "avg": [ 2.48, 5.61 ], "std": [ 1.64, 2.76 ], "fq": 10
  },
  "fun": {
    "dict": "anew", "word": "fun", "stem": "fun",
    "avg": [ 8.37, 7.22 ], "std": [ 1.11, 2.01 ], "fq": 44
  },
  "funeral": {
    "dict": "anew", "word": "funeral", "stem": "funer",
    "avg": [ 1.39, 4.94 ], "std": [ 0.87, 3.21 ], "fq": 33
  },
  "fungus": {
    "dict": "anew", "word": "fungus", "stem": "fungus",
    "avg": [ 3.06, 4.68 ], "std": [ 1.75, 2.33 ], "fq": 2
  },
  "fur": {
    "dict": "anew", "word": "fur", "stem": "fur",
    "avg": [ 4.51, 4.18 ], "std": [ 1.88, 2.44 ], "fq": 13
  },
  "game": {
    "dict": "anew", "word": "game", "stem": "game",
    "avg": [ 6.98, 5.89 ], "std": [ 1.97, 2.37 ], "fq": 123
  },
  "gangrene": {
    "dict": "anew", "word": "gangrene", "stem": "gangren",
    "avg": [ 2.28, 5.70 ], "std": [ 1.91, 2.96 ], "fq": 0
  },
  "garbage": {
    "dict": "anew", "word": "garbage", "stem": "garbag",
    "avg": [ 2.98, 5.04 ], "std": [ 1.96, 2.50 ], "fq": 7
  },
  "garden": {
    "dict": "anew", "word": "garden", "stem": "garden",
    "avg": [ 6.71, 4.39 ], "std": [ 1.74, 2.35 ], "fq": 60
  },
  "garment": {
    "dict": "anew", "word": "garment", "stem": "garment",
    "avg": [ 6.07, 4.49 ], "std": [ 1.61, 2.50 ], "fq": 6
  },
  "garter": {
    "dict": "anew", "word": "garter", "stem": "garter",
    "avg": [ 6.22, 5.47 ], "std": [ 1.59, 2.15 ], "fq": 2
  },
  "gender": {
    "dict": "anew", "word": "gender", "stem": "gender",
    "avg": [ 5.73, 4.38 ], "std": [ 1.55, 2.13 ], "fq": 2
  },
  "gentle": {
    "dict": "anew", "word": "gentle", "stem": "gentl",
    "avg": [ 7.31, 3.21 ], "std": [ 1.30, 2.57 ], "fq": 27
  },
  "germs": {
    "dict": "anew", "word": "germs", "stem": "germ",
    "avg": [ 2.86, 4.49 ], "std": [ 1.39, 2.24 ], "fq": 1
  },
  "gift": {
    "dict": "anew", "word": "gift", "stem": "gift",
    "avg": [ 7.77, 6.14 ], "std": [ 2.24, 2.76 ], "fq": 33
  },
  "girl": {
    "dict": "anew", "word": "girl", "stem": "girl",
    "avg": [ 6.87, 4.29 ], "std": [ 1.64, 2.69 ], "fq": 220
  },
  "glacier": {
    "dict": "anew", "word": "glacier", "stem": "glacier",
    "avg": [ 5.50, 4.24 ], "std": [ 1.25, 2.29 ], "fq": 1
  },
  "glamour": {
    "dict": "anew", "word": "glamour", "stem": "glamour",
    "avg": [ 6.76, 4.68 ], "std": [ 1.60, 2.23 ], "fq": 5
  },
  "glass": {
    "dict": "anew", "word": "glass", "stem": "glass",
    "avg": [ 4.75, 4.27 ], "std": [ 1.38, 2.07 ], "fq": 99
  },
  "gloom": {
    "dict": "anew", "word": "gloom", "stem": "gloom",
    "avg": [ 1.88, 3.83 ], "std": [ 1.23, 2.33 ], "fq": 14
  },
  "glory": {
    "dict": "anew", "word": "glory", "stem": "glori",
    "avg": [ 7.55, 6.02 ], "std": [ 1.68, 2.71 ], "fq": 21
  },
  "god": {
    "dict": "anew", "word": "god", "stem": "god",
    "avg": [ 8.15, 5.95 ], "std": [ 1.27, 2.84 ], "fq": 318
  },
  "gold": {
    "dict": "anew", "word": "gold", "stem": "gold",
    "avg": [ 7.54, 5.76 ], "std": [ 1.63, 2.79 ], "fq": 52
  },
  "golfer": {
    "dict": "anew", "word": "golfer", "stem": "golfer",
    "avg": [ 5.61, 3.73 ], "std": [ 1.93, 2.26 ], "fq": 3
  },
  "good": {
    "dict": "anew", "word": "good", "stem": "good",
    "avg": [ 7.47, 5.43 ], "std": [ 1.45, 2.85 ], "fq": 807
  },
  "gossip": {
    "dict": "anew", "word": "gossip", "stem": "gossip",
    "avg": [ 3.48, 5.74 ], "std": [ 2.33, 2.38 ], "fq": 13
  },
  "graduate": {
    "dict": "anew", "word": "graduate", "stem": "graduat",
    "avg": [ 8.19, 7.25 ], "std": [ 1.13, 2.25 ], "fq": 30
  },
  "grass": {
    "dict": "anew", "word": "grass", "stem": "grass",
    "avg": [ 6.12, 4.14 ], "std": [ 1.44, 2.11 ], "fq": 53
  },
  "grateful": {
    "dict": "anew", "word": "grateful", "stem": "grate",
    "avg": [ 7.37, 4.58 ], "std": [ 0.97, 2.14 ], "fq": 25
  },
  "greed": {
    "dict": "anew", "word": "greed", "stem": "greed",
    "avg": [ 3.51, 4.71 ], "std": [ 1.93, 2.26 ], "fq": 3
  },
  "green": {
    "dict": "anew", "word": "green", "stem": "green",
    "avg": [ 6.18, 4.28 ], "std": [ 2.05, 2.46 ], "fq": 116
  },
  "greet": {
    "dict": "anew", "word": "greet", "stem": "greet",
    "avg": [ 7.00, 5.27 ], "std": [ 1.52, 2.31 ], "fq": 7
  },
  "grenade": {
    "dict": "anew", "word": "grenade", "stem": "grenad",
    "avg": [ 3.60, 5.70 ], "std": [ 1.88, 2.52 ], "fq": 3
  },
  "grief": {
    "dict": "anew", "word": "grief", "stem": "grief",
    "avg": [ 1.69, 4.78 ], "std": [ 1.04, 2.84 ], "fq": 10
  },
  "grime": {
    "dict": "anew", "word": "grime", "stem": "grime",
    "avg": [ 3.37, 3.98 ], "std": [ 1.34, 2.29 ], "fq": 0
  },
  "gripe": {
    "dict": "anew", "word": "gripe", "stem": "gripe",
    "avg": [ 3.14, 5.00 ], "std": [ 1.56, 2.19 ], "fq": 0
  },
  "guillotine": {
    "dict": "anew", "word": "guillotine", "stem": "guillotin",
    "avg": [ 2.48, 6.56 ], "std": [ 2.11, 2.54 ], "fq": 0
  },
  "guilty": {
    "dict": "anew", "word": "guilty", "stem": "guilti",
    "avg": [ 2.63, 6.04 ], "std": [ 1.98, 2.76 ], "fq": 29
  },
  "gun": {
    "dict": "anew", "word": "gun", "stem": "gun",
    "avg": [ 3.47, 7.02 ], "std": [ 2.48, 1.84 ], "fq": 118
  },
  "gymnast": {
    "dict": "anew", "word": "gymnast", "stem": "gymnast",
    "avg": [ 6.35, 5.02 ], "std": [ 1.79, 2.20 ], "fq": 1
  },
  "habit": {
    "dict": "anew", "word": "habit", "stem": "habit",
    "avg": [ 4.11, 3.95 ], "std": [ 1.77, 2.11 ], "fq": 23
  },
  "hairdryer": {
    "dict": "anew", "word": "hairdryer", "stem": "hairdryer",
    "avg": [ 4.84, 3.71 ], "std": [ 0.84, 1.75 ], "fq": 0
  },
  "hairpin": {
    "dict": "anew", "word": "hairpin", "stem": "hairpin",
    "avg": [ 5.26, 3.27 ], "std": [ 1.45, 2.41 ], "fq": 1
  },
  "hamburger": {
    "dict": "anew", "word": "hamburger", "stem": "hamburg",
    "avg": [ 6.27, 4.55 ], "std": [ 1.50, 2.14 ], "fq": 6
  },
  "hammer": {
    "dict": "anew", "word": "hammer", "stem": "hammer",
    "avg": [ 4.88, 4.58 ], "std": [ 1.16, 2.02 ], "fq": 9
  },
  "hand": {
    "dict": "anew", "word": "hand", "stem": "hand",
    "avg": [ 5.95, 4.40 ], "std": [ 1.38, 2.07 ], "fq": 431
  },
  "handicap": {
    "dict": "anew", "word": "handicap", "stem": "handicap",
    "avg": [ 3.29, 3.81 ], "std": [ 1.69, 2.27 ], "fq": 6
  },
  "handsome": {
    "dict": "anew", "word": "handsome", "stem": "handsom",
    "avg": [ 7.93, 5.95 ], "std": [ 1.47, 2.73 ], "fq": 40
  },
  "haphazard": {
    "dict": "anew", "word": "haphazard", "stem": "haphazard",
    "avg": [ 4.02, 4.07 ], "std": [ 1.41, 2.18 ], "fq": 2
  },
  "happy": {
    "dict": "anew", "word": "happy", "stem": "happi",
    "avg": [ 8.21, 6.49 ], "std": [ 1.82, 2.77 ], "fq": 98
  },
  "hard": {
    "dict": "anew", "word": "hard", "stem": "hard",
    "avg": [ 5.22, 5.12 ], "std": [ 1.82, 2.19 ], "fq": 202
  },
  "hardship": {
    "dict": "anew", "word": "hardship", "stem": "hardship",
    "avg": [ 2.45, 4.76 ], "std": [ 1.61, 2.55 ], "fq": 9
  },
  "hat": {
    "dict": "anew", "word": "hat", "stem": "hat",
    "avg": [ 5.46, 4.10 ], "std": [ 1.36, 2.00 ], "fq": 56
  },
  "hate": {
    "dict": "anew", "word": "hate", "stem": "hate",
    "avg": [ 2.12, 6.95 ], "std": [ 1.72, 2.56 ], "fq": 42
  },
  "hatred": {
    "dict": "anew", "word": "hatred", "stem": "hatr",
    "avg": [ 1.98, 6.66 ], "std": [ 1.92, 2.56 ], "fq": 20
  },
  "hawk": {
    "dict": "anew", "word": "hawk", "stem": "hawk",
    "avg": [ 5.88, 4.39 ], "std": [ 1.62, 2.29 ], "fq": 14
  },
  "hay": {
    "dict": "anew", "word": "hay", "stem": "hay",
    "avg": [ 5.24, 3.95 ], "std": [ 1.24, 2.58 ], "fq": 19
  },
  "headache": {
    "dict": "anew", "word": "headache", "stem": "headach",
    "avg": [ 2.02, 5.07 ], "std": [ 1.06, 2.74 ], "fq": 5
  },
  "headlight": {
    "dict": "anew", "word": "headlight", "stem": "headlight",
    "avg": [ 5.24, 3.81 ], "std": [ 1.51, 2.22 ], "fq": 0
  },
  "heal": {
    "dict": "anew", "word": "heal", "stem": "heal",
    "avg": [ 7.09, 4.77 ], "std": [ 1.46, 2.23 ], "fq": 2
  },
  "health": {
    "dict": "anew", "word": "health", "stem": "health",
    "avg": [ 6.81, 5.13 ], "std": [ 1.88, 2.35 ], "fq": 105
  },
  "heart": {
    "dict": "anew", "word": "heart", "stem": "heart",
    "avg": [ 7.39, 6.34 ], "std": [ 1.53, 2.25 ], "fq": 173
  },
  "heaven": {
    "dict": "anew", "word": "heaven", "stem": "heaven",
    "avg": [ 7.30, 5.61 ], "std": [ 2.39, 3.20 ], "fq": 43
  },
  "hell": {
    "dict": "anew", "word": "hell", "stem": "hell",
    "avg": [ 2.24, 5.38 ], "std": [ 1.62, 2.62 ], "fq": 95
  },
  "helpless": {
    "dict": "anew", "word": "helpless", "stem": "helpless",
    "avg": [ 2.20, 5.34 ], "std": [ 1.42, 2.52 ], "fq": 21
  },
  "heroin": {
    "dict": "anew", "word": "heroin", "stem": "heroin",
    "avg": [ 4.36, 5.11 ], "std": [ 2.73, 2.72 ], "fq": 2
  },
  "hide": {
    "dict": "anew", "word": "hide", "stem": "hide",
    "avg": [ 4.32, 5.28 ], "std": [ 1.91, 2.51 ], "fq": 22
  },
  "highway": {
    "dict": "anew", "word": "highway", "stem": "highway",
    "avg": [ 5.92, 5.16 ], "std": [ 1.72, 2.44 ], "fq": 40
  },
  "hinder": {
    "dict": "anew", "word": "hinder", "stem": "hinder",
    "avg": [ 3.81, 4.12 ], "std": [ 1.42, 2.01 ], "fq": 0
  },
  "history": {
    "dict": "anew", "word": "history", "stem": "histori",
    "avg": [ 5.24, 3.93 ], "std": [ 2.01, 2.29 ], "fq": 286
  },
  "hit": {
    "dict": "anew", "word": "hit", "stem": "hit",
    "avg": [ 4.33, 5.73 ], "std": [ 2.35, 2.09 ], "fq": 115
  },
  "holiday": {
    "dict": "anew", "word": "holiday", "stem": "holiday",
    "avg": [ 7.55, 6.59 ], "std": [ 2.14, 2.73 ], "fq": 17
  },
  "home": {
    "dict": "anew", "word": "home", "stem": "home",
    "avg": [ 7.91, 4.21 ], "std": [ 1.63, 2.94 ], "fq": 547
  },
  "honest": {
    "dict": "anew", "word": "honest", "stem": "honest",
    "avg": [ 7.70, 5.32 ], "std": [ 1.43, 1.92 ], "fq": 47
  },
  "honey": {
    "dict": "anew", "word": "honey", "stem": "honey",
    "avg": [ 6.73, 4.51 ], "std": [ 1.70, 2.25 ], "fq": 25
  },
  "honor": {
    "dict": "anew", "word": "honor", "stem": "honor",
    "avg": [ 7.66, 5.90 ], "std": [ 1.24, 1.83 ], "fq": 66
  },
  "hooker": {
    "dict": "anew", "word": "hooker", "stem": "hooker",
    "avg": [ 3.34, 4.93 ], "std": [ 2.31, 2.82 ], "fq": 0
  },
  "hope": {
    "dict": "anew", "word": "hope", "stem": "hope",
    "avg": [ 7.05, 5.44 ], "std": [ 1.96, 2.47 ], "fq": 178
  },
  "hopeful": {
    "dict": "anew", "word": "hopeful", "stem": "hope",
    "avg": [ 7.10, 5.78 ], "std": [ 1.46, 2.09 ], "fq": 12
  },
  "horror": {
    "dict": "anew", "word": "horror", "stem": "horror",
    "avg": [ 2.76, 7.21 ], "std": [ 2.25, 2.14 ], "fq": 17
  },
  "horse": {
    "dict": "anew", "word": "horse", "stem": "hors",
    "avg": [ 5.89, 3.89 ], "std": [ 1.55, 2.17 ], "fq": 117
  },
  "hospital": {
    "dict": "anew", "word": "hospital", "stem": "hospit",
    "avg": [ 5.04, 5.98 ], "std": [ 2.45, 2.54 ], "fq": 110
  },
  "hostage": {
    "dict": "anew", "word": "hostage", "stem": "hostag",
    "avg": [ 2.20, 6.76 ], "std": [ 1.80, 2.63 ], "fq": 2
  },
  "hostile": {
    "dict": "anew", "word": "hostile", "stem": "hostil",
    "avg": [ 2.73, 6.44 ], "std": [ 1.50, 2.28 ], "fq": 19
  },
  "hotel": {
    "dict": "anew", "word": "hotel", "stem": "hotel",
    "avg": [ 6.00, 4.80 ], "std": [ 1.77, 2.53 ], "fq": 126
  },
  "house": {
    "dict": "anew", "word": "house", "stem": "hous",
    "avg": [ 7.26, 4.56 ], "std": [ 1.72, 2.41 ], "fq": 591
  },
  "hug": {
    "dict": "anew", "word": "hug", "stem": "hug",
    "avg": [ 8.00, 5.35 ], "std": [ 1.55, 2.76 ], "fq": 3
  },
  "humane": {
    "dict": "anew", "word": "humane", "stem": "human",
    "avg": [ 6.89, 4.50 ], "std": [ 1.70, 1.91 ], "fq": 5
  },
  "humble": {
    "dict": "anew", "word": "humble", "stem": "humbl",
    "avg": [ 5.86, 3.74 ], "std": [ 1.42, 2.33 ], "fq": 18
  },
  "humiliate": {
    "dict": "anew", "word": "humiliate", "stem": "humili",
    "avg": [ 2.24, 6.14 ], "std": [ 1.34, 2.42 ], "fq": 0
  },
  "humor": {
    "dict": "anew", "word": "humor", "stem": "humor",
    "avg": [ 8.56, 5.50 ], "std": [ 0.81, 2.91 ], "fq": 47
  },
  "hungry": {
    "dict": "anew", "word": "hungry", "stem": "hungri",
    "avg": [ 3.58, 5.13 ], "std": [ 2.01, 2.44 ], "fq": 23
  },
  "hurricane": {
    "dict": "anew", "word": "hurricane", "stem": "hurrican",
    "avg": [ 3.34, 6.83 ], "std": [ 2.12, 2.06 ], "fq": 8
  },
  "hurt": {
    "dict": "anew", "word": "hurt", "stem": "hurt",
    "avg": [ 1.90, 5.85 ], "std": [ 1.26, 2.49 ], "fq": 37
  },
  "hydrant": {
    "dict": "anew", "word": "hydrant", "stem": "hydrant",
    "avg": [ 5.02, 3.71 ], "std": [ 0.93, 1.75 ], "fq": 0
  },
  "icebox": {
    "dict": "anew", "word": "icebox", "stem": "icebox",
    "avg": [ 4.95, 4.17 ], "std": [ 1.00, 2.11 ], "fq": 3
  },
  "idea": {
    "dict": "anew", "word": "idea", "stem": "idea",
    "avg": [ 7.00, 5.86 ], "std": [ 1.34, 1.81 ], "fq": 195
  },
  "identity": {
    "dict": "anew", "word": "identity", "stem": "ident",
    "avg": [ 6.57, 4.95 ], "std": [ 1.99, 2.24 ], "fq": 55
  },
  "idiot": {
    "dict": "anew", "word": "idiot", "stem": "idiot",
    "avg": [ 3.16, 4.21 ], "std": [ 1.91, 2.47 ], "fq": 2
  },
  "idol": {
    "dict": "anew", "word": "idol", "stem": "idol",
    "avg": [ 6.12, 4.95 ], "std": [ 1.86, 2.14 ], "fq": 7
  },
  "ignorance": {
    "dict": "anew", "word": "ignorance", "stem": "ignor",
    "avg": [ 3.07, 4.39 ], "std": [ 2.25, 2.49 ], "fq": 16
  },
  "illness": {
    "dict": "anew", "word": "illness", "stem": "ill",
    "avg": [ 2.48, 4.71 ], "std": [ 1.40, 2.24 ], "fq": 20
  },
  "imagine": {
    "dict": "anew", "word": "imagine", "stem": "imagin",
    "avg": [ 7.32, 5.98 ], "std": [ 1.52, 2.14 ], "fq": 61
  },
  "immature": {
    "dict": "anew", "word": "immature", "stem": "immatur",
    "avg": [ 3.39, 4.15 ], "std": [ 1.70, 1.96 ], "fq": 7
  },
  "immoral": {
    "dict": "anew", "word": "immoral", "stem": "immor",
    "avg": [ 3.50, 4.98 ], "std": [ 2.16, 2.48 ], "fq": 5
  },
  "impair": {
    "dict": "anew", "word": "impair", "stem": "impair",
    "avg": [ 3.18, 4.04 ], "std": [ 1.86, 2.14 ], "fq": 4
  },
  "impotent": {
    "dict": "anew", "word": "impotent", "stem": "impot",
    "avg": [ 2.81, 4.57 ], "std": [ 1.92, 2.59 ], "fq": 2
  },
  "impressed": {
    "dict": "anew", "word": "impressed", "stem": "impress",
    "avg": [ 7.33, 5.42 ], "std": [ 1.84, 2.65 ], "fq": 30
  },
  "improve": {
    "dict": "anew", "word": "improve", "stem": "improv",
    "avg": [ 7.65, 5.69 ], "std": [ 1.16, 2.15 ], "fq": 39
  },
  "incentive": {
    "dict": "anew", "word": "incentive", "stem": "incent",
    "avg": [ 7.00, 5.69 ], "std": [ 1.72, 2.45 ], "fq": 12
  },
  "indifferent": {
    "dict": "anew", "word": "indifferent", "stem": "indiffer",
    "avg": [ 4.61, 3.18 ], "std": [ 1.28, 1.85 ], "fq": 11
  },
  "industry": {
    "dict": "anew", "word": "industry", "stem": "industri",
    "avg": [ 5.30, 4.47 ], "std": [ 1.61, 2.43 ], "fq": 171
  },
  "infant": {
    "dict": "anew", "word": "infant", "stem": "infant",
    "avg": [ 6.95, 5.05 ], "std": [ 2.08, 2.66 ], "fq": 11
  },
  "infatuation": {
    "dict": "anew", "word": "infatuation", "stem": "infatu",
    "avg": [ 6.73, 7.02 ], "std": [ 2.08, 1.87 ], "fq": 4
  },
  "infection": {
    "dict": "anew", "word": "infection", "stem": "infect",
    "avg": [ 1.66, 5.03 ], "std": [ 1.34, 2.77 ], "fq": 8
  },
  "inferior": {
    "dict": "anew", "word": "inferior", "stem": "inferior",
    "avg": [ 3.07, 3.83 ], "std": [ 1.57, 2.05 ], "fq": 7
  },
  "inhabitant": {
    "dict": "anew", "word": "inhabitant", "stem": "inhabit",
    "avg": [ 5.05, 3.95 ], "std": [ 1.34, 1.97 ], "fq": 0
  },
  "injury": {
    "dict": "anew", "word": "injury", "stem": "injuri",
    "avg": [ 2.49, 5.69 ], "std": [ 1.76, 2.06 ], "fq": 27
  },
  "ink": {
    "dict": "anew", "word": "ink", "stem": "ink",
    "avg": [ 5.05, 3.84 ], "std": [ 0.81, 1.88 ], "fq": 7
  },
  "innocent": {
    "dict": "anew", "word": "innocent", "stem": "innoc",
    "avg": [ 6.51, 4.21 ], "std": [ 1.34, 1.99 ], "fq": 37
  },
  "insane": {
    "dict": "anew", "word": "insane", "stem": "insan",
    "avg": [ 2.85, 5.83 ], "std": [ 1.94, 2.45 ], "fq": 13
  },
  "insect": {
    "dict": "anew", "word": "insect", "stem": "insect",
    "avg": [ 4.07, 4.07 ], "std": [ 2.16, 2.46 ], "fq": 14
  },
  "insecure": {
    "dict": "anew", "word": "insecure", "stem": "insecur",
    "avg": [ 2.36, 5.56 ], "std": [ 1.33, 2.34 ], "fq": 3
  },
  "insolent": {
    "dict": "anew", "word": "insolent", "stem": "insol",
    "avg": [ 4.35, 5.38 ], "std": [ 1.76, 2.37 ], "fq": 2
  },
  "inspire": {
    "dict": "anew", "word": "inspire", "stem": "inspir",
    "avg": [ 6.97, 5.00 ], "std": [ 1.91, 2.53 ], "fq": 3
  },
  "inspired": {
    "dict": "anew", "word": "inspired", "stem": "inspir",
    "avg": [ 7.15, 6.02 ], "std": [ 1.85, 2.67 ], "fq": 25
  },
  "insult": {
    "dict": "anew", "word": "insult", "stem": "insult",
    "avg": [ 2.29, 6.00 ], "std": [ 1.33, 2.46 ], "fq": 7
  },
  "intellect": {
    "dict": "anew", "word": "intellect", "stem": "intellect",
    "avg": [ 6.82, 4.75 ], "std": [ 1.96, 2.50 ], "fq": 5
  },
  "intercourse": {
    "dict": "anew", "word": "intercourse", "stem": "intercours",
    "avg": [ 7.36, 7.00 ], "std": [ 1.57, 2.07 ], "fq": 9
  },
  "interest": {
    "dict": "anew", "word": "interest", "stem": "interest",
    "avg": [ 6.97, 5.66 ], "std": [ 1.53, 2.26 ], "fq": 330
  },
  "intimate": {
    "dict": "anew", "word": "intimate", "stem": "intim",
    "avg": [ 7.61, 6.98 ], "std": [ 1.51, 2.21 ], "fq": 21
  },
  "intruder": {
    "dict": "anew", "word": "intruder", "stem": "intrud",
    "avg": [ 2.77, 6.86 ], "std": [ 2.32, 2.41 ], "fq": 1
  },
  "invader": {
    "dict": "anew", "word": "invader", "stem": "invad",
    "avg": [ 3.05, 5.50 ], "std": [ 2.01, 2.40 ], "fq": 1
  },
  "invest": {
    "dict": "anew", "word": "invest", "stem": "invest",
    "avg": [ 5.93, 5.12 ], "std": [ 2.10, 2.42 ], "fq": 3
  },
  "iron": {
    "dict": "anew", "word": "iron", "stem": "iron",
    "avg": [ 4.90, 3.76 ], "std": [ 1.02, 2.06 ], "fq": 43
  },
  "irritate": {
    "dict": "anew", "word": "irritate", "stem": "irrit",
    "avg": [ 3.11, 5.76 ], "std": [ 1.67, 2.15 ], "fq": 0
  },
  "item": {
    "dict": "anew", "word": "item", "stem": "item",
    "avg": [ 5.26, 3.24 ], "std": [ 0.86, 2.08 ], "fq": 54
  },
  "jail": {
    "dict": "anew", "word": "jail", "stem": "jail",
    "avg": [ 1.95, 5.49 ], "std": [ 1.27, 2.67 ], "fq": 21
  },
  "jealousy": {
    "dict": "anew", "word": "jealousy", "stem": "jealousi",
    "avg": [ 2.51, 6.36 ], "std": [ 1.83, 2.66 ], "fq": 4
  },
  "jelly": {
    "dict": "anew", "word": "jelly", "stem": "jelli",
    "avg": [ 5.66, 3.70 ], "std": [ 1.44, 2.29 ], "fq": 3
  },
  "jewel": {
    "dict": "anew", "word": "jewel", "stem": "jewel",
    "avg": [ 7.00, 5.38 ], "std": [ 1.72, 2.54 ], "fq": 1
  },
  "joke": {
    "dict": "anew", "word": "joke", "stem": "joke",
    "avg": [ 8.10, 6.74 ], "std": [ 1.36, 1.84 ], "fq": 22
  },
  "jolly": {
    "dict": "anew", "word": "jolly", "stem": "jolli",
    "avg": [ 7.41, 5.57 ], "std": [ 1.92, 2.80 ], "fq": 4
  },
  "journal": {
    "dict": "anew", "word": "journal", "stem": "journal",
    "avg": [ 5.14, 4.05 ], "std": [ 1.49, 1.96 ], "fq": 42
  },
  "joy": {
    "dict": "anew", "word": "joy", "stem": "joy",
    "avg": [ 8.60, 7.22 ], "std": [ 0.71, 2.13 ], "fq": 40
  },
  "joyful": {
    "dict": "anew", "word": "joyful", "stem": "joy",
    "avg": [ 8.22, 5.98 ], "std": [ 1.22, 2.54 ], "fq": 1
  },
  "jug": {
    "dict": "anew", "word": "jug", "stem": "jug",
    "avg": [ 5.24, 3.88 ], "std": [ 1.65, 2.15 ], "fq": 6
  },
  "justice": {
    "dict": "anew", "word": "justice", "stem": "justic",
    "avg": [ 7.78, 5.47 ], "std": [ 1.35, 2.54 ], "fq": 114
  },
  "kerchief": {
    "dict": "anew", "word": "kerchief", "stem": "kerchief",
    "avg": [ 5.11, 3.43 ], "std": [ 1.33, 2.08 ], "fq": 1
  },
  "kerosene": {
    "dict": "anew", "word": "kerosene", "stem": "kerosen",
    "avg": [ 4.80, 4.34 ], "std": [ 1.59, 2.51 ], "fq": 6
  },
  "ketchup": {
    "dict": "anew", "word": "ketchup", "stem": "ketchup",
    "avg": [ 5.60, 4.09 ], "std": [ 1.35, 2.08 ], "fq": 1
  },
  "kettle": {
    "dict": "anew", "word": "kettle", "stem": "kettl",
    "avg": [ 5.22, 3.22 ], "std": [ 0.91, 2.23 ], "fq": 3
  },
  "key": {
    "dict": "anew", "word": "key", "stem": "key",
    "avg": [ 5.68, 3.70 ], "std": [ 1.62, 2.18 ], "fq": 88
  },
  "kick": {
    "dict": "anew", "word": "kick", "stem": "kick",
    "avg": [ 4.31, 4.90 ], "std": [ 2.18, 2.35 ], "fq": 16
  },
  "kids": {
    "dict": "anew", "word": "kids", "stem": "kid",
    "avg": [ 6.91, 5.27 ], "std": [ 1.99, 2.36 ], "fq": 32
  },
  "killer": {
    "dict": "anew", "word": "killer", "stem": "killer",
    "avg": [ 1.89, 7.86 ], "std": [ 1.39, 1.89 ], "fq": 21
  },
  "kind": {
    "dict": "anew", "word": "kind", "stem": "kind",
    "avg": [ 7.59, 4.46 ], "std": [ 1.67, 2.55 ], "fq": 313
  },
  "kindness": {
    "dict": "anew", "word": "kindness", "stem": "kind",
    "avg": [ 7.82, 4.30 ], "std": [ 1.39, 2.62 ], "fq": 5
  },
  "king": {
    "dict": "anew", "word": "king", "stem": "king",
    "avg": [ 7.26, 5.51 ], "std": [ 1.67, 2.77 ], "fq": 88
  },
  "kiss": {
    "dict": "anew", "word": "kiss", "stem": "kiss",
    "avg": [ 8.26, 7.32 ], "std": [ 1.54, 2.03 ], "fq": 17
  },
  "kitten": {
    "dict": "anew", "word": "kitten", "stem": "kitten",
    "avg": [ 6.86, 5.08 ], "std": [ 2.13, 2.45 ], "fq": 5
  },
  "knife": {
    "dict": "anew", "word": "knife", "stem": "knife",
    "avg": [ 3.62, 5.80 ], "std": [ 2.18, 2.00 ], "fq": 76
  },
  "knot": {
    "dict": "anew", "word": "knot", "stem": "knot",
    "avg": [ 4.64, 4.07 ], "std": [ 1.36, 2.15 ], "fq": 8
  },
  "knowledge": {
    "dict": "anew", "word": "knowledge", "stem": "knowledg",
    "avg": [ 7.58, 5.92 ], "std": [ 1.32, 2.32 ], "fq": 145
  },
  "lake": {
    "dict": "anew", "word": "lake", "stem": "lake",
    "avg": [ 6.82, 3.95 ], "std": [ 1.54, 2.44 ], "fq": 54
  },
  "lamb": {
    "dict": "anew", "word": "lamb", "stem": "lamb",
    "avg": [ 5.89, 3.36 ], "std": [ 1.73, 2.18 ], "fq": 7
  },
  "lamp": {
    "dict": "anew", "word": "lamp", "stem": "lamp",
    "avg": [ 5.41, 3.80 ], "std": [ 1.00, 2.12 ], "fq": 18
  },
  "lantern": {
    "dict": "anew", "word": "lantern", "stem": "lantern",
    "avg": [ 5.57, 4.05 ], "std": [ 1.19, 2.28 ], "fq": 13
  },
  "laughter": {
    "dict": "anew", "word": "laughter", "stem": "laughter",
    "avg": [ 8.45, 6.75 ], "std": [ 1.08, 2.50 ], "fq": 22
  },
  "lavish": {
    "dict": "anew", "word": "lavish", "stem": "lavish",
    "avg": [ 6.21, 4.93 ], "std": [ 2.03, 2.40 ], "fq": 3
  },
  "lawn": {
    "dict": "anew", "word": "lawn", "stem": "lawn",
    "avg": [ 5.24, 4.00 ], "std": [ 0.86, 1.79 ], "fq": 15
  },
  "lawsuit": {
    "dict": "anew", "word": "lawsuit", "stem": "lawsuit",
    "avg": [ 3.37, 4.93 ], "std": [ 2.00, 2.44 ], "fq": 1
  },
  "lazy": {
    "dict": "anew", "word": "lazy", "stem": "lazi",
    "avg": [ 4.38, 2.65 ], "std": [ 2.02, 2.06 ], "fq": 9
  },
  "leader": {
    "dict": "anew", "word": "leader", "stem": "leader",
    "avg": [ 7.63, 6.27 ], "std": [ 1.59, 2.18 ], "fq": 74
  },
  "learn": {
    "dict": "anew", "word": "learn", "stem": "learn",
    "avg": [ 7.15, 5.39 ], "std": [ 1.49, 2.22 ], "fq": 84
  },
  "legend": {
    "dict": "anew", "word": "legend", "stem": "legend",
    "avg": [ 6.39, 4.88 ], "std": [ 1.34, 1.76 ], "fq": 26
  },
  "leisurely": {
    "dict": "anew", "word": "leisurely", "stem": "leisur",
    "avg": [ 6.88, 3.80 ], "std": [ 1.81, 2.38 ], "fq": 5
  },
  "leprosy": {
    "dict": "anew", "word": "leprosy", "stem": "leprosi",
    "avg": [ 2.09, 6.29 ], "std": [ 1.40, 2.23 ], "fq": 1
  },
  "lesbian": {
    "dict": "anew", "word": "lesbian", "stem": "lesbian",
    "avg": [ 4.67, 5.12 ], "std": [ 2.45, 2.27 ], "fq": 0
  },
  "letter": {
    "dict": "anew", "word": "letter", "stem": "letter",
    "avg": [ 6.61, 4.90 ], "std": [ 1.59, 2.37 ], "fq": 145
  },
  "liberty": {
    "dict": "anew", "word": "liberty", "stem": "liberti",
    "avg": [ 7.98, 5.60 ], "std": [ 1.22, 2.65 ], "fq": 46
  },
  "lice": {
    "dict": "anew", "word": "lice", "stem": "lice",
    "avg": [ 2.31, 5.00 ], "std": [ 1.78, 2.26 ], "fq": 2
  },
  "lie": {
    "dict": "anew", "word": "lie", "stem": "lie",
    "avg": [ 2.79, 5.96 ], "std": [ 1.92, 2.63 ], "fq": 59
  },
  "life": {
    "dict": "anew", "word": "life", "stem": "life",
    "avg": [ 7.27, 6.02 ], "std": [ 1.88, 2.62 ], "fq": 715
  },
  "lightbulb": {
    "dict": "anew", "word": "lightbulb", "stem": "lightbulb",
    "avg": [ 5.61, 4.10 ], "std": [ 1.28, 2.02 ], "fq": 0
  },
  "lighthouse": {
    "dict": "anew", "word": "lighthouse", "stem": "lighthous",
    "avg": [ 5.89, 4.41 ], "std": [ 2.08, 2.44 ], "fq": 0
  },
  "lightning": {
    "dict": "anew", "word": "lightning", "stem": "lightn",
    "avg": [ 4.57, 6.61 ], "std": [ 2.66, 1.77 ], "fq": 14
  },
  "limber": {
    "dict": "anew", "word": "limber", "stem": "limber",
    "avg": [ 5.68, 4.57 ], "std": [ 1.49, 2.26 ], "fq": 2
  },
  "lion": {
    "dict": "anew", "word": "lion", "stem": "lion",
    "avg": [ 5.57, 6.20 ], "std": [ 1.99, 2.16 ], "fq": 17
  },
  "listless": {
    "dict": "anew", "word": "listless", "stem": "listless",
    "avg": [ 4.12, 4.10 ], "std": [ 1.73, 2.31 ], "fq": 1
  },
  "lively": {
    "dict": "anew", "word": "lively", "stem": "live",
    "avg": [ 7.20, 5.53 ], "std": [ 1.97, 2.90 ], "fq": 26
  },
  "locker": {
    "dict": "anew", "word": "locker", "stem": "locker",
    "avg": [ 5.19, 3.38 ], "std": [ 1.31, 2.13 ], "fq": 9
  },
  "loneliness": {
    "dict": "anew", "word": "loneliness", "stem": "loneli",
    "avg": [ 1.61, 4.56 ], "std": [ 1.02, 2.97 ], "fq": 9
  },
  "lonely": {
    "dict": "anew", "word": "lonely", "stem": "lone",
    "avg": [ 2.17, 4.51 ], "std": [ 1.76, 2.68 ], "fq": 25
  },
  "loser": {
    "dict": "anew", "word": "loser", "stem": "loser",
    "avg": [ 2.25, 4.95 ], "std": [ 1.48, 2.57 ], "fq": 1
  },
  "lost": {
    "dict": "anew", "word": "lost", "stem": "lost",
    "avg": [ 2.82, 5.82 ], "std": [ 1.83, 2.62 ], "fq": 173
  },
  "lottery": {
    "dict": "anew", "word": "lottery", "stem": "lotteri",
    "avg": [ 6.57, 5.36 ], "std": [ 2.04, 2.45 ], "fq": 1
  },
  "louse": {
    "dict": "anew", "word": "louse", "stem": "lous",
    "avg": [ 2.81, 4.98 ], "std": [ 1.92, 2.03 ], "fq": 3
  },
  "love": {
    "dict": "anew", "word": "love", "stem": "love",
    "avg": [ 8.72, 6.44 ], "std": [ 0.70, 3.35 ], "fq": 232
  },
  "loved": {
    "dict": "anew", "word": "loved", "stem": "love",
    "avg": [ 8.64, 6.38 ], "std": [ 0.71, 2.68 ], "fq": 56
  },
  "loyal": {
    "dict": "anew", "word": "loyal", "stem": "loyal",
    "avg": [ 7.55, 5.16 ], "std": [ 1.90, 2.42 ], "fq": 18
  },
  "lucky": {
    "dict": "anew", "word": "lucky", "stem": "lucki",
    "avg": [ 8.17, 6.53 ], "std": [ 1.06, 2.34 ], "fq": 21
  },
  "lump": {
    "dict": "anew", "word": "lump", "stem": "lump",
    "avg": [ 4.16, 4.80 ], "std": [ 2.34, 2.82 ], "fq": 7
  },
  "luscious": {
    "dict": "anew", "word": "luscious", "stem": "luscious",
    "avg": [ 7.50, 5.34 ], "std": [ 1.08, 2.51 ], "fq": 2
  },
  "lust": {
    "dict": "anew", "word": "lust", "stem": "lust",
    "avg": [ 7.12, 6.88 ], "std": [ 1.62, 1.85 ], "fq": 5
  },
  "luxury": {
    "dict": "anew", "word": "luxury", "stem": "luxuri",
    "avg": [ 7.88, 4.75 ], "std": [ 1.49, 2.91 ], "fq": 21
  },
  "machine": {
    "dict": "anew", "word": "machine", "stem": "machin",
    "avg": [ 5.09, 3.82 ], "std": [ 1.67, 2.40 ], "fq": 103
  },
  "mad": {
    "dict": "anew", "word": "mad", "stem": "mad",
    "avg": [ 2.44, 6.76 ], "std": [ 1.72, 2.26 ], "fq": 39
  },
  "madman": {
    "dict": "anew", "word": "madman", "stem": "madman",
    "avg": [ 3.91, 5.56 ], "std": [ 2.49, 2.78 ], "fq": 2
  },
  "maggot": {
    "dict": "anew", "word": "maggot", "stem": "maggot",
    "avg": [ 2.06, 5.28 ], "std": [ 1.47, 2.96 ], "fq": 2
  },
  "magical": {
    "dict": "anew", "word": "magical", "stem": "magic",
    "avg": [ 7.46, 5.95 ], "std": [ 1.64, 2.36 ], "fq": 12
  },
  "mail": {
    "dict": "anew", "word": "mail", "stem": "mail",
    "avg": [ 6.88, 5.63 ], "std": [ 1.74, 2.36 ], "fq": 47
  },
  "malaria": {
    "dict": "anew", "word": "malaria", "stem": "malaria",
    "avg": [ 2.40, 4.40 ], "std": [ 1.38, 2.54 ], "fq": 3
  },
  "malice": {
    "dict": "anew", "word": "malice", "stem": "malic",
    "avg": [ 2.69, 5.86 ], "std": [ 1.84, 2.75 ], "fq": 2
  },
  "man": {
    "dict": "anew", "word": "man", "stem": "man",
    "avg": [ 6.73, 5.24 ], "std": [ 1.70, 2.31 ], "fq": 1207
  },
  "mangle": {
    "dict": "anew", "word": "mangle", "stem": "mangl",
    "avg": [ 3.90, 5.44 ], "std": [ 2.01, 2.10 ], "fq": 0
  },
  "maniac": {
    "dict": "anew", "word": "maniac", "stem": "maniac",
    "avg": [ 3.76, 5.39 ], "std": [ 2.00, 2.46 ], "fq": 4
  },
  "manner": {
    "dict": "anew", "word": "manner", "stem": "manner",
    "avg": [ 5.64, 4.56 ], "std": [ 1.34, 1.78 ], "fq": 124
  },
  "mantel": {
    "dict": "anew", "word": "mantel", "stem": "mantel",
    "avg": [ 4.93, 3.27 ], "std": [ 1.40, 2.23 ], "fq": 3
  },
  "manure": {
    "dict": "anew", "word": "manure", "stem": "manur",
    "avg": [ 3.10, 4.17 ], "std": [ 1.74, 2.09 ], "fq": 6
  },
  "market": {
    "dict": "anew", "word": "market", "stem": "market",
    "avg": [ 5.66, 4.12 ], "std": [ 1.02, 1.83 ], "fq": 155
  },
  "massacre": {
    "dict": "anew", "word": "massacre", "stem": "massacr",
    "avg": [ 2.28, 5.33 ], "std": [ 1.74, 2.63 ], "fq": 1
  },
  "masterful": {
    "dict": "anew", "word": "masterful", "stem": "master",
    "avg": [ 7.09, 5.20 ], "std": [ 1.78, 2.85 ], "fq": 2
  },
  "masturbate": {
    "dict": "anew", "word": "masturbate", "stem": "masturb",
    "avg": [ 5.45, 5.67 ], "std": [ 2.02, 2.18 ], "fq": 0
  },
  "material": {
    "dict": "anew", "word": "material", "stem": "materi",
    "avg": [ 5.26, 4.05 ], "std": [ 1.29, 2.34 ], "fq": 174
  },
  "measles": {
    "dict": "anew", "word": "measles", "stem": "measl",
    "avg": [ 2.74, 5.06 ], "std": [ 1.97, 2.44 ], "fq": 2
  },
  "medicine": {
    "dict": "anew", "word": "medicine", "stem": "medicin",
    "avg": [ 5.67, 4.40 ], "std": [ 2.06, 2.36 ], "fq": 30
  },
  "meek": {
    "dict": "anew", "word": "meek", "stem": "meek",
    "avg": [ 3.87, 3.80 ], "std": [ 1.69, 2.13 ], "fq": 10
  },
  "melody": {
    "dict": "anew", "word": "melody", "stem": "melodi",
    "avg": [ 7.07, 4.98 ], "std": [ 1.79, 2.52 ], "fq": 21
  },
  "memories": {
    "dict": "anew", "word": "memories", "stem": "memori",
    "avg": [ 7.48, 6.10 ], "std": [ 1.61, 2.10 ], "fq": 15
  },
  "memory": {
    "dict": "anew", "word": "memory", "stem": "memori",
    "avg": [ 6.62, 5.42 ], "std": [ 1.50, 2.25 ], "fq": 76
  },
  "menace": {
    "dict": "anew", "word": "menace", "stem": "menac",
    "avg": [ 2.88, 5.52 ], "std": [ 1.64, 2.45 ], "fq": 9
  },
  "merry": {
    "dict": "anew", "word": "merry", "stem": "merri",
    "avg": [ 7.90, 5.90 ], "std": [ 1.49, 2.42 ], "fq": 8
  },
  "messy": {
    "dict": "anew", "word": "messy", "stem": "messi",
    "avg": [ 3.15, 3.34 ], "std": [ 1.73, 2.37 ], "fq": 3
  },
  "metal": {
    "dict": "anew", "word": "metal", "stem": "metal",
    "avg": [ 4.95, 3.79 ], "std": [ 1.17, 1.96 ], "fq": 61
  },
  "method": {
    "dict": "anew", "word": "method", "stem": "method",
    "avg": [ 5.56, 3.85 ], "std": [ 1.76, 2.58 ], "fq": 142
  },
  "mighty": {
    "dict": "anew", "word": "mighty", "stem": "mighti",
    "avg": [ 6.54, 5.61 ], "std": [ 2.19, 2.38 ], "fq": 29
  },
  "mildew": {
    "dict": "anew", "word": "mildew", "stem": "mildew",
    "avg": [ 3.17, 4.08 ], "std": [ 1.36, 1.79 ], "fq": 1
  },
  "milk": {
    "dict": "anew", "word": "milk", "stem": "milk",
    "avg": [ 5.95, 3.68 ], "std": [ 2.16, 2.57 ], "fq": 49
  },
  "millionaire": {
    "dict": "anew", "word": "millionaire", "stem": "millionair",
    "avg": [ 8.03, 6.14 ], "std": [ 1.42, 2.70 ], "fq": 2
  },
  "mind": {
    "dict": "anew", "word": "mind", "stem": "mind",
    "avg": [ 6.68, 5.00 ], "std": [ 1.84, 2.68 ], "fq": 325
  },
  "miracle": {
    "dict": "anew", "word": "miracle", "stem": "miracl",
    "avg": [ 8.60, 7.65 ], "std": [ 0.71, 1.67 ], "fq": 16
  },
  "mischief": {
    "dict": "anew", "word": "mischief", "stem": "mischief",
    "avg": [ 5.57, 5.76 ], "std": [ 2.05, 1.95 ], "fq": 5
  },
  "misery": {
    "dict": "anew", "word": "misery", "stem": "miseri",
    "avg": [ 1.93, 5.17 ], "std": [ 1.60, 2.69 ], "fq": 15
  },
  "mistake": {
    "dict": "anew", "word": "mistake", "stem": "mistak",
    "avg": [ 2.86, 5.18 ], "std": [ 1.79, 2.42 ], "fq": 34
  },
  "mobility": {
    "dict": "anew", "word": "mobility", "stem": "mobil",
    "avg": [ 6.83, 5.00 ], "std": [ 1.79, 2.18 ], "fq": 8
  },
  "modest": {
    "dict": "anew", "word": "modest", "stem": "modest",
    "avg": [ 5.76, 3.98 ], "std": [ 1.28, 2.24 ], "fq": 29
  },
  "mold": {
    "dict": "anew", "word": "mold", "stem": "mold",
    "avg": [ 3.55, 4.07 ], "std": [ 1.70, 1.98 ], "fq": 45
  },
  "moment": {
    "dict": "anew", "word": "moment", "stem": "moment",
    "avg": [ 5.76, 3.83 ], "std": [ 1.65, 2.29 ], "fq": 246
  },
  "money": {
    "dict": "anew", "word": "money", "stem": "money",
    "avg": [ 7.59, 5.70 ], "std": [ 1.40, 2.66 ], "fq": 265
  },
  "month": {
    "dict": "anew", "word": "month", "stem": "month",
    "avg": [ 5.15, 4.03 ], "std": [ 1.09, 1.77 ], "fq": 130
  },
  "moody": {
    "dict": "anew", "word": "moody", "stem": "moodi",
    "avg": [ 3.20, 4.18 ], "std": [ 1.58, 2.38 ], "fq": 5
  },
  "moral": {
    "dict": "anew", "word": "moral", "stem": "moral",
    "avg": [ 6.20, 4.49 ], "std": [ 1.85, 2.28 ], "fq": 142
  },
  "morbid": {
    "dict": "anew", "word": "morbid", "stem": "morbid",
    "avg": [ 2.87, 5.06 ], "std": [ 2.14, 2.68 ], "fq": 1
  },
  "morgue": {
    "dict": "anew", "word": "morgue", "stem": "morgu",
    "avg": [ 1.92, 4.84 ], "std": [ 1.32, 2.96 ], "fq": 1
  },
  "mosquito": {
    "dict": "anew", "word": "mosquito", "stem": "mosquito",
    "avg": [ 2.80, 4.78 ], "std": [ 1.91, 2.72 ], "fq": 1
  },
  "mother": {
    "dict": "anew", "word": "mother", "stem": "mother",
    "avg": [ 8.39, 6.13 ], "std": [ 1.15, 2.71 ], "fq": 216
  },
  "mountain": {
    "dict": "anew", "word": "mountain", "stem": "mountain",
    "avg": [ 6.59, 5.49 ], "std": [ 1.66, 2.43 ], "fq": 33
  },
  "movie": {
    "dict": "anew", "word": "movie", "stem": "movi",
    "avg": [ 6.86, 4.93 ], "std": [ 1.81, 2.54 ], "fq": 29
  },
  "mucus": {
    "dict": "anew", "word": "mucus", "stem": "mucus",
    "avg": [ 3.34, 3.41 ], "std": [ 2.29, 2.17 ], "fq": 2
  },
  "muddy": {
    "dict": "anew", "word": "muddy", "stem": "muddi",
    "avg": [ 4.44, 4.13 ], "std": [ 2.07, 2.13 ], "fq": 10
  },
  "muffin": {
    "dict": "anew", "word": "muffin", "stem": "muffin",
    "avg": [ 6.57, 4.76 ], "std": [ 2.04, 2.42 ], "fq": 0
  },
  "murderer": {
    "dict": "anew", "word": "murderer", "stem": "murder",
    "avg": [ 1.53, 7.47 ], "std": [ 0.96, 2.18 ], "fq": 19
  },
  "muscular": {
    "dict": "anew", "word": "muscular", "stem": "muscular",
    "avg": [ 6.82, 5.47 ], "std": [ 1.63, 2.20 ], "fq": 16
  },
  "museum": {
    "dict": "anew", "word": "museum", "stem": "museum",
    "avg": [ 5.54, 3.60 ], "std": [ 1.86, 2.13 ], "fq": 32
  },
  "mushroom": {
    "dict": "anew", "word": "mushroom", "stem": "mushroom",
    "avg": [ 5.78, 4.72 ], "std": [ 2.22, 2.33 ], "fq": 2
  },
  "music": {
    "dict": "anew", "word": "music", "stem": "music",
    "avg": [ 8.13, 5.32 ], "std": [ 1.09, 3.19 ], "fq": 216
  },
  "mutation": {
    "dict": "anew", "word": "mutation", "stem": "mutat",
    "avg": [ 3.91, 4.84 ], "std": [ 2.44, 2.52 ], "fq": 0
  },
  "mutilate": {
    "dict": "anew", "word": "mutilate", "stem": "mutil",
    "avg": [ 1.82, 6.41 ], "std": [ 1.45, 2.94 ], "fq": 3
  },
  "mystic": {
    "dict": "anew", "word": "mystic", "stem": "mystic",
    "avg": [ 6.00, 4.84 ], "std": [ 2.21, 2.57 ], "fq": 3
  },
  "naked": {
    "dict": "anew", "word": "naked", "stem": "nake",
    "avg": [ 6.34, 5.80 ], "std": [ 2.42, 2.80 ], "fq": 32
  },
  "name": {
    "dict": "anew", "word": "name", "stem": "name",
    "avg": [ 5.55, 4.25 ], "std": [ 2.24, 2.47 ], "fq": 294
  },
  "narcotic": {
    "dict": "anew", "word": "narcotic", "stem": "narcot",
    "avg": [ 4.29, 4.93 ], "std": [ 2.30, 2.57 ], "fq": 2
  },
  "nasty": {
    "dict": "anew", "word": "nasty", "stem": "nasti",
    "avg": [ 3.58, 4.89 ], "std": [ 2.38, 2.50 ], "fq": 5
  },
  "natural": {
    "dict": "anew", "word": "natural", "stem": "natur",
    "avg": [ 6.59, 4.09 ], "std": [ 1.57, 2.37 ], "fq": 156
  },
  "nature": {
    "dict": "anew", "word": "nature", "stem": "natur",
    "avg": [ 7.65, 4.37 ], "std": [ 1.37, 2.51 ], "fq": 191
  },
  "nectar": {
    "dict": "anew", "word": "nectar", "stem": "nectar",
    "avg": [ 6.90, 3.89 ], "std": [ 1.53, 2.48 ], "fq": 3
  },
  "needle": {
    "dict": "anew", "word": "needle", "stem": "needl",
    "avg": [ 3.82, 5.36 ], "std": [ 1.73, 2.89 ], "fq": 15
  },
  "neglect": {
    "dict": "anew", "word": "neglect", "stem": "neglect",
    "avg": [ 2.63, 4.83 ], "std": [ 1.64, 2.31 ], "fq": 12
  },
  "nervous": {
    "dict": "anew", "word": "nervous", "stem": "nervous",
    "avg": [ 3.29, 6.59 ], "std": [ 1.47, 2.07 ], "fq": 24
  },
  "neurotic": {
    "dict": "anew", "word": "neurotic", "stem": "neurot",
    "avg": [ 4.45, 5.13 ], "std": [ 2.23, 2.76 ], "fq": 10
  },
  "news": {
    "dict": "anew", "word": "news", "stem": "news",
    "avg": [ 5.30, 5.17 ], "std": [ 1.67, 2.11 ], "fq": 102
  },
  "nice": {
    "dict": "anew", "word": "nice", "stem": "nice",
    "avg": [ 6.55, 4.38 ], "std": [ 2.44, 2.69 ], "fq": 75
  },
  "nightmare": {
    "dict": "anew", "word": "nightmare", "stem": "nightmar",
    "avg": [ 1.91, 7.59 ], "std": [ 1.54, 2.23 ], "fq": 9
  },
  "nipple": {
    "dict": "anew", "word": "nipple", "stem": "nippl",
    "avg": [ 6.27, 5.56 ], "std": [ 1.81, 2.55 ], "fq": 0
  },
  "noisy": {
    "dict": "anew", "word": "noisy", "stem": "noisi",
    "avg": [ 5.02, 6.38 ], "std": [ 2.02, 1.78 ], "fq": 6
  },
  "nonchalant": {
    "dict": "anew", "word": "nonchalant", "stem": "nonchal",
    "avg": [ 4.74, 3.12 ], "std": [ 1.11, 1.93 ], "fq": 1
  },
  "nonsense": {
    "dict": "anew", "word": "nonsense", "stem": "nonsens",
    "avg": [ 4.61, 4.17 ], "std": [ 1.63, 2.02 ], "fq": 13
  },
  "noose": {
    "dict": "anew", "word": "noose", "stem": "noos",
    "avg": [ 3.76, 4.39 ], "std": [ 1.64, 2.08 ], "fq": 3
  },
  "nourish": {
    "dict": "anew", "word": "nourish", "stem": "nourish",
    "avg": [ 6.46, 4.29 ], "std": [ 1.69, 2.51 ], "fq": 0
  },
  "nude": {
    "dict": "anew", "word": "nude", "stem": "nude",
    "avg": [ 6.82, 6.41 ], "std": [ 1.63, 2.09 ], "fq": 20
  },
  "nuisance": {
    "dict": "anew", "word": "nuisance", "stem": "nuisanc",
    "avg": [ 3.27, 4.49 ], "std": [ 1.86, 2.69 ], "fq": 5
  },
  "nun": {
    "dict": "anew", "word": "nun", "stem": "nun",
    "avg": [ 4.93, 2.93 ], "std": [ 1.89, 1.80 ], "fq": 2
  },
  "nurse": {
    "dict": "anew", "word": "nurse", "stem": "nurs",
    "avg": [ 6.08, 4.84 ], "std": [ 2.08, 2.04 ], "fq": 17
  },
  "nursery": {
    "dict": "anew", "word": "nursery", "stem": "nurseri",
    "avg": [ 5.73, 4.04 ], "std": [ 2.30, 2.74 ], "fq": 13
  },
  "obesity": {
    "dict": "anew", "word": "obesity", "stem": "obes",
    "avg": [ 2.73, 3.87 ], "std": [ 1.85, 2.82 ], "fq": 5
  },
  "obey": {
    "dict": "anew", "word": "obey", "stem": "obey",
    "avg": [ 4.52, 4.23 ], "std": [ 1.88, 1.72 ], "fq": 8
  },
  "obnoxious": {
    "dict": "anew", "word": "obnoxious", "stem": "obnoxi",
    "avg": [ 3.50, 4.74 ], "std": [ 2.18, 2.42 ], "fq": 5
  },
  "obscene": {
    "dict": "anew", "word": "obscene", "stem": "obscen",
    "avg": [ 4.23, 5.04 ], "std": [ 2.30, 2.30 ], "fq": 2
  },
  "obsession": {
    "dict": "anew", "word": "obsession", "stem": "obsess",
    "avg": [ 4.52, 6.41 ], "std": [ 2.13, 2.13 ], "fq": 5
  },
  "ocean": {
    "dict": "anew", "word": "ocean", "stem": "ocean",
    "avg": [ 7.12, 4.95 ], "std": [ 1.72, 2.79 ], "fq": 34
  },
  "odd": {
    "dict": "anew", "word": "odd", "stem": "odd",
    "avg": [ 4.82, 4.27 ], "std": [ 2.04, 2.46 ], "fq": 44
  },
  "offend": {
    "dict": "anew", "word": "offend", "stem": "offend",
    "avg": [ 2.76, 5.56 ], "std": [ 1.50, 2.06 ], "fq": 4
  },
  "office": {
    "dict": "anew", "word": "office", "stem": "offic",
    "avg": [ 5.24, 4.08 ], "std": [ 1.59, 1.92 ], "fq": 255
  },
  "opinion": {
    "dict": "anew", "word": "opinion", "stem": "opinion",
    "avg": [ 6.28, 4.89 ], "std": [ 1.45, 2.46 ], "fq": 96
  },
  "optimism": {
    "dict": "anew", "word": "optimism", "stem": "optim",
    "avg": [ 6.95, 5.34 ], "std": [ 2.24, 2.58 ], "fq": 15
  },
  "option": {
    "dict": "anew", "word": "option", "stem": "option",
    "avg": [ 6.49, 4.74 ], "std": [ 1.31, 2.23 ], "fq": 5
  },
  "orchestra": {
    "dict": "anew", "word": "orchestra", "stem": "orchestra",
    "avg": [ 6.02, 3.52 ], "std": [ 1.89, 2.29 ], "fq": 60
  },
  "orgasm": {
    "dict": "anew", "word": "orgasm", "stem": "orgasm",
    "avg": [ 8.32, 8.10 ], "std": [ 1.31, 1.45 ], "fq": 7
  },
  "outdoors": {
    "dict": "anew", "word": "outdoors", "stem": "outdoor",
    "avg": [ 7.47, 5.92 ], "std": [ 1.80, 2.55 ], "fq": 6
  },
  "outrage": {
    "dict": "anew", "word": "outrage", "stem": "outrag",
    "avg": [ 3.52, 6.83 ], "std": [ 2.12, 2.26 ], "fq": 4
  },
  "outstanding": {
    "dict": "anew", "word": "outstanding", "stem": "outstand",
    "avg": [ 7.75, 6.24 ], "std": [ 1.75, 2.59 ], "fq": 37
  },
  "overcast": {
    "dict": "anew", "word": "overcast", "stem": "overcast",
    "avg": [ 3.65, 3.46 ], "std": [ 1.61, 1.92 ], "fq": 9
  },
  "overwhelmed": {
    "dict": "anew", "word": "overwhelmed", "stem": "overwhelm",
    "avg": [ 4.19, 7.00 ], "std": [ 2.61, 2.37 ], "fq": 4
  },
  "owl": {
    "dict": "anew", "word": "owl", "stem": "owl",
    "avg": [ 5.80, 3.98 ], "std": [ 1.31, 1.87 ], "fq": 2
  },
  "pain": {
    "dict": "anew", "word": "pain", "stem": "pain",
    "avg": [ 2.13, 6.50 ], "std": [ 1.81, 2.49 ], "fq": 88
  },
  "paint": {
    "dict": "anew", "word": "paint", "stem": "paint",
    "avg": [ 5.62, 4.10 ], "std": [ 1.72, 2.36 ], "fq": 37
  },
  "palace": {
    "dict": "anew", "word": "palace", "stem": "palac",
    "avg": [ 7.19, 5.10 ], "std": [ 1.78, 2.75 ], "fq": 38
  },
  "pamphlet": {
    "dict": "anew", "word": "pamphlet", "stem": "pamphlet",
    "avg": [ 4.79, 3.62 ], "std": [ 1.05, 2.02 ], "fq": 3
  },
  "pancakes": {
    "dict": "anew", "word": "pancakes", "stem": "pancak",
    "avg": [ 6.08, 4.06 ], "std": [ 1.83, 2.13 ], "fq": 0
  },
  "panic": {
    "dict": "anew", "word": "panic", "stem": "panic",
    "avg": [ 3.12, 7.02 ], "std": [ 1.84, 2.02 ], "fq": 22
  },
  "paper": {
    "dict": "anew", "word": "paper", "stem": "paper",
    "avg": [ 5.20, 2.50 ], "std": [ 1.21, 1.85 ], "fq": 157
  },
  "paradise": {
    "dict": "anew", "word": "paradise", "stem": "paradis",
    "avg": [ 8.72, 5.12 ], "std": [ 0.60, 3.38 ], "fq": 12
  },
  "paralysis": {
    "dict": "anew", "word": "paralysis", "stem": "paralysi",
    "avg": [ 1.98, 4.73 ], "std": [ 1.44, 2.83 ], "fq": 6
  },
  "part": {
    "dict": "anew", "word": "part", "stem": "part",
    "avg": [ 5.11, 3.82 ], "std": [ 1.78, 2.24 ], "fq": 500
  },
  "party": {
    "dict": "anew", "word": "party", "stem": "parti",
    "avg": [ 7.86, 6.69 ], "std": [ 1.83, 2.84 ], "fq": 216
  },
  "passage": {
    "dict": "anew", "word": "passage", "stem": "passag",
    "avg": [ 5.28, 4.36 ], "std": [ 1.44, 2.13 ], "fq": 49
  },
  "passion": {
    "dict": "anew", "word": "passion", "stem": "passion",
    "avg": [ 8.03, 7.26 ], "std": [ 1.27, 2.57 ], "fq": 28
  },
  "pasta": {
    "dict": "anew", "word": "pasta", "stem": "pasta",
    "avg": [ 6.69, 4.94 ], "std": [ 1.64, 2.04 ], "fq": 0
  },
  "patent": {
    "dict": "anew", "word": "patent", "stem": "patent",
    "avg": [ 5.29, 3.50 ], "std": [ 1.08, 1.84 ], "fq": 35
  },
  "patient": {
    "dict": "anew", "word": "patient", "stem": "patient",
    "avg": [ 5.29, 4.21 ], "std": [ 1.89, 2.37 ], "fq": 86
  },
  "patriot": {
    "dict": "anew", "word": "patriot", "stem": "patriot",
    "avg": [ 6.71, 5.17 ], "std": [ 1.69, 2.53 ], "fq": 10
  },
  "peace": {
    "dict": "anew", "word": "peace", "stem": "peac",
    "avg": [ 7.72, 2.95 ], "std": [ 1.75, 2.55 ], "fq": 198
  },
  "penalty": {
    "dict": "anew", "word": "penalty", "stem": "penalti",
    "avg": [ 2.83, 5.10 ], "std": [ 1.56, 2.31 ], "fq": 14
  },
  "pencil": {
    "dict": "anew", "word": "pencil", "stem": "pencil",
    "avg": [ 5.22, 3.14 ], "std": [ 0.68, 1.90 ], "fq": 34
  },
  "penis": {
    "dict": "anew", "word": "penis", "stem": "peni",
    "avg": [ 5.90, 5.54 ], "std": [ 1.72, 2.63 ], "fq": 0
  },
  "penthouse": {
    "dict": "anew", "word": "penthouse", "stem": "penthous",
    "avg": [ 6.81, 5.52 ], "std": [ 1.64, 2.49 ], "fq": 1
  },
  "people": {
    "dict": "anew", "word": "people", "stem": "peopl",
    "avg": [ 7.33, 5.94 ], "std": [ 1.70, 2.09 ], "fq": 847
  },
  "perfection": {
    "dict": "anew", "word": "perfection", "stem": "perfect",
    "avg": [ 7.25, 5.95 ], "std": [ 2.05, 2.73 ], "fq": 11
  },
  "perfume": {
    "dict": "anew", "word": "perfume", "stem": "perfum",
    "avg": [ 6.76, 5.05 ], "std": [ 1.48, 2.36 ], "fq": 10
  },
  "person": {
    "dict": "anew", "word": "person", "stem": "person",
    "avg": [ 6.32, 4.19 ], "std": [ 1.74, 2.45 ], "fq": 175
  },
  "pervert": {
    "dict": "anew", "word": "pervert", "stem": "pervert",
    "avg": [ 2.79, 6.26 ], "std": [ 2.12, 2.61 ], "fq": 1
  },
  "pest": {
    "dict": "anew", "word": "pest", "stem": "pest",
    "avg": [ 3.13, 5.62 ], "std": [ 1.82, 2.15 ], "fq": 4
  },
  "pet": {
    "dict": "anew", "word": "pet", "stem": "pet",
    "avg": [ 6.79, 5.10 ], "std": [ 2.32, 2.59 ], "fq": 8
  },
  "phase": {
    "dict": "anew", "word": "phase", "stem": "phase",
    "avg": [ 5.17, 3.98 ], "std": [ 0.79, 1.82 ], "fq": 72
  },
  "pie": {
    "dict": "anew", "word": "pie", "stem": "pie",
    "avg": [ 6.41, 4.20 ], "std": [ 1.89, 2.40 ], "fq": 14
  },
  "pig": {
    "dict": "anew", "word": "pig", "stem": "pig",
    "avg": [ 5.07, 4.20 ], "std": [ 1.97, 2.42 ], "fq": 8
  },
  "pillow": {
    "dict": "anew", "word": "pillow", "stem": "pillow",
    "avg": [ 7.92, 2.97 ], "std": [ 1.40, 2.52 ], "fq": 8
  },
  "pinch": {
    "dict": "anew", "word": "pinch", "stem": "pinch",
    "avg": [ 3.83, 4.59 ], "std": [ 1.70, 2.10 ], "fq": 6
  },
  "pistol": {
    "dict": "anew", "word": "pistol", "stem": "pistol",
    "avg": [ 4.20, 6.15 ], "std": [ 2.58, 2.19 ], "fq": 27
  },
  "pity": {
    "dict": "anew", "word": "pity", "stem": "piti",
    "avg": [ 3.37, 3.72 ], "std": [ 1.57, 2.02 ], "fq": 14
  },
  "pizza": {
    "dict": "anew", "word": "pizza", "stem": "pizza",
    "avg": [ 6.65, 5.24 ], "std": [ 2.23, 2.09 ], "fq": 3
  },
  "plain": {
    "dict": "anew", "word": "plain", "stem": "plain",
    "avg": [ 4.39, 3.52 ], "std": [ 1.46, 2.05 ], "fq": 48
  },
  "plane": {
    "dict": "anew", "word": "plane", "stem": "plane",
    "avg": [ 6.43, 6.14 ], "std": [ 1.98, 2.39 ], "fq": 114
  },
  "plant": {
    "dict": "anew", "word": "plant", "stem": "plant",
    "avg": [ 5.98, 3.62 ], "std": [ 1.83, 2.25 ], "fq": 125
  },
  "pleasure": {
    "dict": "anew", "word": "pleasure", "stem": "pleasur",
    "avg": [ 8.28, 5.74 ], "std": [ 0.92, 2.81 ], "fq": 62
  },
  "poetry": {
    "dict": "anew", "word": "poetry", "stem": "poetri",
    "avg": [ 5.86, 4.00 ], "std": [ 1.91, 2.85 ], "fq": 88
  },
  "poison": {
    "dict": "anew", "word": "poison", "stem": "poison",
    "avg": [ 1.98, 6.05 ], "std": [ 1.44, 2.82 ], "fq": 10
  },
  "politeness": {
    "dict": "anew", "word": "politeness", "stem": "polit",
    "avg": [ 7.18, 3.74 ], "std": [ 1.50, 2.37 ], "fq": 5
  },
  "pollute": {
    "dict": "anew", "word": "pollute", "stem": "pollut",
    "avg": [ 1.85, 6.08 ], "std": [ 1.11, 2.42 ], "fq": 1
  },
  "poster": {
    "dict": "anew", "word": "poster", "stem": "poster",
    "avg": [ 5.34, 3.93 ], "std": [ 1.75, 2.56 ], "fq": 4
  },
  "poverty": {
    "dict": "anew", "word": "poverty", "stem": "poverti",
    "avg": [ 1.67, 4.87 ], "std": [ 0.90, 2.66 ], "fq": 20
  },
  "power": {
    "dict": "anew", "word": "power", "stem": "power",
    "avg": [ 6.54, 6.67 ], "std": [ 2.21, 1.87 ], "fq": 342
  },
  "powerful": {
    "dict": "anew", "word": "powerful", "stem": "power",
    "avg": [ 6.84, 5.83 ], "std": [ 1.80, 2.69 ], "fq": 63
  },
  "prairie": {
    "dict": "anew", "word": "prairie", "stem": "prairi",
    "avg": [ 5.75, 3.41 ], "std": [ 1.43, 2.17 ], "fq": 21
  },
  "present": {
    "dict": "anew", "word": "present", "stem": "present",
    "avg": [ 6.95, 5.12 ], "std": [ 1.85, 2.39 ], "fq": 377
  },
  "pressure": {
    "dict": "anew", "word": "pressure", "stem": "pressur",
    "avg": [ 3.38, 6.07 ], "std": [ 1.61, 2.26 ], "fq": 185
  },
  "prestige": {
    "dict": "anew", "word": "prestige", "stem": "prestig",
    "avg": [ 7.26, 5.86 ], "std": [ 1.90, 2.08 ], "fq": 29
  },
  "pretty": {
    "dict": "anew", "word": "pretty", "stem": "pretti",
    "avg": [ 7.75, 6.03 ], "std": [ 1.26, 2.22 ], "fq": 107
  },
  "prick": {
    "dict": "anew", "word": "prick", "stem": "prick",
    "avg": [ 3.98, 4.70 ], "std": [ 1.73, 2.59 ], "fq": 2
  },
  "pride": {
    "dict": "anew", "word": "pride", "stem": "pride",
    "avg": [ 7.00, 5.83 ], "std": [ 2.11, 2.48 ], "fq": 42
  },
  "priest": {
    "dict": "anew", "word": "priest", "stem": "priest",
    "avg": [ 6.42, 4.41 ], "std": [ 2.00, 2.71 ], "fq": 16
  },
  "prison": {
    "dict": "anew", "word": "prison", "stem": "prison",
    "avg": [ 2.05, 5.70 ], "std": [ 1.34, 2.56 ], "fq": 42
  },
  "privacy": {
    "dict": "anew", "word": "privacy", "stem": "privaci",
    "avg": [ 5.88, 4.12 ], "std": [ 1.50, 1.83 ], "fq": 12
  },
  "profit": {
    "dict": "anew", "word": "profit", "stem": "profit",
    "avg": [ 7.63, 6.68 ], "std": [ 1.30, 1.78 ], "fq": 28
  },
  "progress": {
    "dict": "anew", "word": "progress", "stem": "progress",
    "avg": [ 7.73, 6.02 ], "std": [ 1.34, 2.58 ], "fq": 120
  },
  "promotion": {
    "dict": "anew", "word": "promotion", "stem": "promot",
    "avg": [ 8.20, 6.44 ], "std": [ 1.15, 2.58 ], "fq": 26
  },
  "protected": {
    "dict": "anew", "word": "protected", "stem": "protect",
    "avg": [ 7.29, 4.09 ], "std": [ 1.79, 2.77 ], "fq": 31
  },
  "proud": {
    "dict": "anew", "word": "proud", "stem": "proud",
    "avg": [ 8.03, 5.56 ], "std": [ 1.56, 3.01 ], "fq": 50
  },
  "pungent": {
    "dict": "anew", "word": "pungent", "stem": "pungent",
    "avg": [ 3.95, 4.24 ], "std": [ 2.09, 2.17 ], "fq": 4
  },
  "punishment": {
    "dict": "anew", "word": "punishment", "stem": "punish",
    "avg": [ 2.22, 5.93 ], "std": [ 1.41, 2.40 ], "fq": 21
  },
  "puppy": {
    "dict": "anew", "word": "puppy", "stem": "puppi",
    "avg": [ 7.56, 5.85 ], "std": [ 1.90, 2.78 ], "fq": 2
  },
  "pus": {
    "dict": "anew", "word": "pus", "stem": "pus",
    "avg": [ 2.86, 4.82 ], "std": [ 1.91, 2.06 ], "fq": 0
  },
  "putrid": {
    "dict": "anew", "word": "putrid", "stem": "putrid",
    "avg": [ 2.38, 5.74 ], "std": [ 1.71, 2.26 ], "fq": 0
  },
  "python": {
    "dict": "anew", "word": "python", "stem": "python",
    "avg": [ 4.05, 6.18 ], "std": [ 2.48, 2.25 ], "fq": 14
  },
  "quality": {
    "dict": "anew", "word": "quality", "stem": "qualiti",
    "avg": [ 6.25, 4.48 ], "std": [ 1.59, 2.12 ], "fq": 114
  },
  "quarrel": {
    "dict": "anew", "word": "quarrel", "stem": "quarrel",
    "avg": [ 2.93, 6.29 ], "std": [ 2.06, 2.56 ], "fq": 20
  },
  "quart": {
    "dict": "anew", "word": "quart", "stem": "quart",
    "avg": [ 5.39, 3.59 ], "std": [ 2.01, 2.51 ], "fq": 3
  },
  "queen": {
    "dict": "anew", "word": "queen", "stem": "queen",
    "avg": [ 6.44, 4.76 ], "std": [ 1.43, 2.18 ], "fq": 41
  },
  "quick": {
    "dict": "anew", "word": "quick", "stem": "quick",
    "avg": [ 6.64, 6.57 ], "std": [ 1.61, 1.78 ], "fq": 68
  },
  "quiet": {
    "dict": "anew", "word": "quiet", "stem": "quiet",
    "avg": [ 5.58, 2.82 ], "std": [ 1.83, 2.13 ], "fq": 76
  },
  "rabbit": {
    "dict": "anew", "word": "rabbit", "stem": "rabbit",
    "avg": [ 6.57, 4.02 ], "std": [ 1.92, 2.19 ], "fq": 11
  },
  "rabies": {
    "dict": "anew", "word": "rabies", "stem": "rabi",
    "avg": [ 1.77, 6.10 ], "std": [ 0.97, 2.62 ], "fq": 1
  },
  "radiant": {
    "dict": "anew", "word": "radiant", "stem": "radiant",
    "avg": [ 6.73, 5.39 ], "std": [ 2.17, 2.82 ], "fq": 8
  },
  "radiator": {
    "dict": "anew", "word": "radiator", "stem": "radiat",
    "avg": [ 4.67, 4.02 ], "std": [ 1.05, 1.94 ], "fq": 4
  },
  "radio": {
    "dict": "anew", "word": "radio", "stem": "radio",
    "avg": [ 6.73, 4.78 ], "std": [ 1.47, 2.82 ], "fq": 120
  },
  "rage": {
    "dict": "anew", "word": "rage", "stem": "rage",
    "avg": [ 2.41, 8.17 ], "std": [ 1.86, 1.40 ], "fq": 16
  },
  "rain": {
    "dict": "anew", "word": "rain", "stem": "rain",
    "avg": [ 5.08, 3.65 ], "std": [ 2.51, 2.35 ], "fq": 70
  },
  "rainbow": {
    "dict": "anew", "word": "rainbow", "stem": "rainbow",
    "avg": [ 8.14, 4.64 ], "std": [ 1.23, 2.88 ], "fq": 4
  },
  "rancid": {
    "dict": "anew", "word": "rancid", "stem": "rancid",
    "avg": [ 4.34, 5.04 ], "std": [ 2.28, 2.27 ], "fq": 0
  },
  "rape": {
    "dict": "anew", "word": "rape", "stem": "rape",
    "avg": [ 1.25, 6.81 ], "std": [ 0.91, 3.17 ], "fq": 5
  },
  "rat": {
    "dict": "anew", "word": "rat", "stem": "rat",
    "avg": [ 3.02, 4.95 ], "std": [ 1.66, 2.36 ], "fq": 6
  },
  "rattle": {
    "dict": "anew", "word": "rattle", "stem": "rattl",
    "avg": [ 5.03, 4.36 ], "std": [ 1.23, 2.18 ], "fq": 5
  },
  "razor": {
    "dict": "anew", "word": "razor", "stem": "razor",
    "avg": [ 4.81, 5.36 ], "std": [ 2.16, 2.44 ], "fq": 15
  },
  "red": {
    "dict": "anew", "word": "red", "stem": "red",
    "avg": [ 6.41, 5.29 ], "std": [ 1.61, 2.04 ], "fq": 197
  },
  "refreshment": {
    "dict": "anew", "word": "refreshment", "stem": "refresh",
    "avg": [ 7.44, 4.45 ], "std": [ 1.29, 2.70 ], "fq": 2
  },
  "regretful": {
    "dict": "anew", "word": "regretful", "stem": "regret",
    "avg": [ 2.28, 5.74 ], "std": [ 1.42, 2.32 ], "fq": 1
  },
  "rejected": {
    "dict": "anew", "word": "rejected", "stem": "reject",
    "avg": [ 1.50, 6.37 ], "std": [ 1.09, 2.56 ], "fq": 33
  },
  "relaxed": {
    "dict": "anew", "word": "relaxed", "stem": "relax",
    "avg": [ 7.00, 2.39 ], "std": [ 1.77, 2.13 ], "fq": 14
  },
  "repentant": {
    "dict": "anew", "word": "repentant", "stem": "repent",
    "avg": [ 5.53, 4.69 ], "std": [ 1.86, 1.98 ], "fq": 1
  },
  "reptile": {
    "dict": "anew", "word": "reptile", "stem": "reptil",
    "avg": [ 4.77, 5.18 ], "std": [ 2.00, 2.19 ], "fq": 0
  },
  "rescue": {
    "dict": "anew", "word": "rescue", "stem": "rescu",
    "avg": [ 7.70, 6.53 ], "std": [ 1.24, 2.56 ], "fq": 15
  },
  "resent": {
    "dict": "anew", "word": "resent", "stem": "resent",
    "avg": [ 3.76, 4.47 ], "std": [ 1.90, 2.12 ], "fq": 8
  },
  "reserved": {
    "dict": "anew", "word": "reserved", "stem": "reserv",
    "avg": [ 4.88, 3.27 ], "std": [ 1.83, 2.05 ], "fq": 27
  },
  "respect": {
    "dict": "anew", "word": "respect", "stem": "respect",
    "avg": [ 7.64, 5.19 ], "std": [ 1.29, 2.39 ], "fq": 125
  },
  "respectful": {
    "dict": "anew", "word": "respectful", "stem": "respect",
    "avg": [ 7.22, 4.60 ], "std": [ 1.27, 2.67 ], "fq": 4
  },
  "restaurant": {
    "dict": "anew", "word": "restaurant", "stem": "restaur",
    "avg": [ 6.76, 5.41 ], "std": [ 1.85, 2.55 ], "fq": 41
  },
  "reunion": {
    "dict": "anew", "word": "reunion", "stem": "reunion",
    "avg": [ 6.48, 6.34 ], "std": [ 2.45, 2.35 ], "fq": 11
  },
  "reverent": {
    "dict": "anew", "word": "reverent", "stem": "rever",
    "avg": [ 5.35, 4.00 ], "std": [ 1.21, 1.60 ], "fq": 3
  },
  "revolt": {
    "dict": "anew", "word": "revolt", "stem": "revolt",
    "avg": [ 4.13, 6.56 ], "std": [ 1.78, 2.34 ], "fq": 8
  },
  "revolver": {
    "dict": "anew", "word": "revolver", "stem": "revolv",
    "avg": [ 4.02, 5.55 ], "std": [ 2.44, 2.39 ], "fq": 14
  },
  "reward": {
    "dict": "anew", "word": "reward", "stem": "reward",
    "avg": [ 7.53, 4.95 ], "std": [ 1.67, 2.62 ], "fq": 15
  },
  "riches": {
    "dict": "anew", "word": "riches", "stem": "rich",
    "avg": [ 7.70, 6.17 ], "std": [ 1.95, 2.70 ], "fq": 2
  },
  "ridicule": {
    "dict": "anew", "word": "ridicule", "stem": "ridicul",
    "avg": [ 3.13, 5.83 ], "std": [ 2.24, 2.73 ], "fq": 5
  },
  "rifle": {
    "dict": "anew", "word": "rifle", "stem": "rifl",
    "avg": [ 4.02, 6.35 ], "std": [ 2.76, 2.04 ], "fq": 63
  },
  "rigid": {
    "dict": "anew", "word": "rigid", "stem": "rigid",
    "avg": [ 3.66, 4.66 ], "std": [ 2.12, 2.47 ], "fq": 24
  },
  "riot": {
    "dict": "anew", "word": "riot", "stem": "riot",
    "avg": [ 2.96, 6.39 ], "std": [ 1.93, 2.63 ], "fq": 7
  },
  "river": {
    "dict": "anew", "word": "river", "stem": "river",
    "avg": [ 6.85, 4.51 ], "std": [ 1.69, 2.42 ], "fq": 165
  },
  "roach": {
    "dict": "anew", "word": "roach", "stem": "roach",
    "avg": [ 2.35, 6.64 ], "std": [ 1.70, 2.64 ], "fq": 2
  },
  "robber": {
    "dict": "anew", "word": "robber", "stem": "robber",
    "avg": [ 2.61, 5.62 ], "std": [ 1.69, 2.72 ], "fq": 2
  },
  "rock": {
    "dict": "anew", "word": "rock", "stem": "rock",
    "avg": [ 5.56, 4.52 ], "std": [ 1.38, 2.37 ], "fq": 75
  },
  "rollercoaster": {
    "dict": "anew", "word": "rollercoaster", "stem": "rollercoast",
    "avg": [ 8.02, 8.06 ], "std": [ 1.63, 1.71 ], "fq": 0
  },
  "romantic": {
    "dict": "anew", "word": "romantic", "stem": "romant",
    "avg": [ 8.32, 7.59 ], "std": [ 1.00, 2.07 ], "fq": 32
  },
  "rotten": {
    "dict": "anew", "word": "rotten", "stem": "rotten",
    "avg": [ 2.26, 4.53 ], "std": [ 1.37, 2.38 ], "fq": 2
  },
  "rough": {
    "dict": "anew", "word": "rough", "stem": "rough",
    "avg": [ 4.74, 5.33 ], "std": [ 2.00, 2.04 ], "fq": 41
  },
  "rude": {
    "dict": "anew", "word": "rude", "stem": "rude",
    "avg": [ 2.50, 6.31 ], "std": [ 2.11, 2.47 ], "fq": 6
  },
  "runner": {
    "dict": "anew", "word": "runner", "stem": "runner",
    "avg": [ 5.67, 4.76 ], "std": [ 1.91, 2.40 ], "fq": 1
  },
  "rusty": {
    "dict": "anew", "word": "rusty", "stem": "rusti",
    "avg": [ 3.86, 3.77 ], "std": [ 1.47, 2.16 ], "fq": 8
  },
  "sad": {
    "dict": "anew", "word": "sad", "stem": "sad",
    "avg": [ 1.61, 4.13 ], "std": [ 0.95, 2.38 ], "fq": 35
  },
  "safe": {
    "dict": "anew", "word": "safe", "stem": "safe",
    "avg": [ 7.07, 3.86 ], "std": [ 1.90, 2.72 ], "fq": 58
  },
  "sailboat": {
    "dict": "anew", "word": "sailboat", "stem": "sailboat",
    "avg": [ 7.25, 4.88 ], "std": [ 1.71, 2.73 ], "fq": 1
  },
  "saint": {
    "dict": "anew", "word": "saint", "stem": "saint",
    "avg": [ 6.49, 4.49 ], "std": [ 1.70, 1.90 ], "fq": 16
  },
  "salad": {
    "dict": "anew", "word": "salad", "stem": "salad",
    "avg": [ 5.74, 3.81 ], "std": [ 1.62, 2.29 ], "fq": 9
  },
  "salute": {
    "dict": "anew", "word": "salute", "stem": "salut",
    "avg": [ 5.92, 5.31 ], "std": [ 1.57, 2.23 ], "fq": 3
  },
  "sapphire": {
    "dict": "anew", "word": "sapphire", "stem": "sapphir",
    "avg": [ 7.00, 5.00 ], "std": [ 1.88, 2.72 ], "fq": 0
  },
  "satisfied": {
    "dict": "anew", "word": "satisfied", "stem": "satisfi",
    "avg": [ 7.94, 4.94 ], "std": [ 1.19, 2.63 ], "fq": 36
  },
  "save": {
    "dict": "anew", "word": "save", "stem": "save",
    "avg": [ 6.45, 4.95 ], "std": [ 1.93, 2.19 ], "fq": 62
  },
  "savior": {
    "dict": "anew", "word": "savior", "stem": "savior",
    "avg": [ 7.73, 5.80 ], "std": [ 1.56, 3.01 ], "fq": 6
  },
  "scalding": {
    "dict": "anew", "word": "scalding", "stem": "scald",
    "avg": [ 2.82, 5.95 ], "std": [ 2.12, 2.55 ], "fq": 1
  },
  "scandal": {
    "dict": "anew", "word": "scandal", "stem": "scandal",
    "avg": [ 3.32, 5.12 ], "std": [ 1.81, 2.22 ], "fq": 8
  },
  "scapegoat": {
    "dict": "anew", "word": "scapegoat", "stem": "scapegoat",
    "avg": [ 3.67, 4.53 ], "std": [ 1.65, 2.13 ], "fq": 1
  },
  "scar": {
    "dict": "anew", "word": "scar", "stem": "scar",
    "avg": [ 3.38, 4.79 ], "std": [ 1.70, 2.11 ], "fq": 10
  },
  "scared": {
    "dict": "anew", "word": "scared", "stem": "scare",
    "avg": [ 2.78, 6.82 ], "std": [ 1.99, 2.03 ], "fq": 21
  },
  "scholar": {
    "dict": "anew", "word": "scholar", "stem": "scholar",
    "avg": [ 7.26, 5.12 ], "std": [ 1.42, 2.46 ], "fq": 15
  },
  "scissors": {
    "dict": "anew", "word": "scissors", "stem": "scissor",
    "avg": [ 5.05, 4.47 ], "std": [ 0.96, 1.76 ], "fq": 1
  },
  "scorching": {
    "dict": "anew", "word": "scorching", "stem": "scorch",
    "avg": [ 3.76, 5.00 ], "std": [ 1.83, 2.74 ], "fq": 0
  },
  "scorn": {
    "dict": "anew", "word": "scorn", "stem": "scorn",
    "avg": [ 2.84, 5.48 ], "std": [ 2.07, 2.52 ], "fq": 4
  },
  "scornful": {
    "dict": "anew", "word": "scornful", "stem": "scorn",
    "avg": [ 3.02, 5.04 ], "std": [ 2.03, 2.56 ], "fq": 5
  },
  "scorpion": {
    "dict": "anew", "word": "scorpion", "stem": "scorpion",
    "avg": [ 3.69, 5.38 ], "std": [ 2.63, 3.08 ], "fq": 0
  },
  "scream": {
    "dict": "anew", "word": "scream", "stem": "scream",
    "avg": [ 3.88, 7.04 ], "std": [ 2.07, 1.96 ], "fq": 13
  },
  "scum": {
    "dict": "anew", "word": "scum", "stem": "scum",
    "avg": [ 2.43, 4.88 ], "std": [ 1.56, 2.36 ], "fq": 0
  },
  "scurvy": {
    "dict": "anew", "word": "scurvy", "stem": "scurvi",
    "avg": [ 3.19, 4.71 ], "std": [ 2.00, 2.72 ], "fq": 1
  },
  "seasick": {
    "dict": "anew", "word": "seasick", "stem": "seasick",
    "avg": [ 2.05, 5.80 ], "std": [ 1.20, 2.88 ], "fq": 0
  },
  "seat": {
    "dict": "anew", "word": "seat", "stem": "seat",
    "avg": [ 4.95, 2.95 ], "std": [ 0.98, 1.72 ], "fq": 54
  },
  "secure": {
    "dict": "anew", "word": "secure", "stem": "secur",
    "avg": [ 7.57, 3.14 ], "std": [ 1.76, 2.47 ], "fq": 30
  },
  "selfish": {
    "dict": "anew", "word": "selfish", "stem": "selfish",
    "avg": [ 2.42, 5.50 ], "std": [ 1.62, 2.62 ], "fq": 8
  },
  "sentiment": {
    "dict": "anew", "word": "sentiment", "stem": "sentiment",
    "avg": [ 5.98, 4.41 ], "std": [ 1.71, 2.30 ], "fq": 23
  },
  "serious": {
    "dict": "anew", "word": "serious", "stem": "serious",
    "avg": [ 5.08, 4.00 ], "std": [ 1.59, 1.87 ], "fq": 116
  },
  "severe": {
    "dict": "anew", "word": "severe", "stem": "sever",
    "avg": [ 3.20, 5.26 ], "std": [ 1.74, 2.36 ], "fq": 39
  },
  "sex": {
    "dict": "anew", "word": "sex", "stem": "sex",
    "avg": [ 8.05, 7.36 ], "std": [ 1.53, 1.91 ], "fq": 84
  },
  "sexy": {
    "dict": "anew", "word": "sexy", "stem": "sexi",
    "avg": [ 8.02, 7.36 ], "std": [ 1.12, 1.91 ], "fq": 2
  },
  "shadow": {
    "dict": "anew", "word": "shadow", "stem": "shadow",
    "avg": [ 4.35, 4.30 ], "std": [ 1.23, 2.26 ], "fq": 36
  },
  "shamed": {
    "dict": "anew", "word": "shamed", "stem": "shame",
    "avg": [ 2.50, 4.88 ], "std": [ 1.34, 2.27 ], "fq": 1
  },
  "shark": {
    "dict": "anew", "word": "shark", "stem": "shark",
    "avg": [ 3.65, 7.16 ], "std": [ 2.47, 1.96 ], "fq": 0
  },
  "sheltered": {
    "dict": "anew", "word": "sheltered", "stem": "shelter",
    "avg": [ 5.75, 4.28 ], "std": [ 1.92, 1.77 ], "fq": 4
  },
  "ship": {
    "dict": "anew", "word": "ship", "stem": "ship",
    "avg": [ 5.55, 4.38 ], "std": [ 1.40, 2.29 ], "fq": 83
  },
  "shotgun": {
    "dict": "anew", "word": "shotgun", "stem": "shotgun",
    "avg": [ 4.37, 6.27 ], "std": [ 2.75, 1.94 ], "fq": 8
  },
  "shriek": {
    "dict": "anew", "word": "shriek", "stem": "shriek",
    "avg": [ 3.93, 5.36 ], "std": [ 2.22, 2.91 ], "fq": 5
  },
  "shy": {
    "dict": "anew", "word": "shy", "stem": "shi",
    "avg": [ 4.64, 3.77 ], "std": [ 1.83, 2.29 ], "fq": 13
  },
  "sick": {
    "dict": "anew", "word": "sick", "stem": "sick",
    "avg": [ 1.90, 4.29 ], "std": [ 1.14, 2.45 ], "fq": 51
  },
  "sickness": {
    "dict": "anew", "word": "sickness", "stem": "sick",
    "avg": [ 2.25, 5.61 ], "std": [ 1.71, 2.67 ], "fq": 6
  },
  "silk": {
    "dict": "anew", "word": "silk", "stem": "silk",
    "avg": [ 6.90, 3.71 ], "std": [ 1.27, 2.51 ], "fq": 12
  },
  "silly": {
    "dict": "anew", "word": "silly", "stem": "silli",
    "avg": [ 7.41, 5.88 ], "std": [ 1.80, 2.38 ], "fq": 15
  },
  "sin": {
    "dict": "anew", "word": "sin", "stem": "sin",
    "avg": [ 2.80, 5.78 ], "std": [ 1.67, 2.21 ], "fq": 53
  },
  "sinful": {
    "dict": "anew", "word": "sinful", "stem": "sin",
    "avg": [ 2.93, 6.29 ], "std": [ 2.15, 2.43 ], "fq": 3
  },
  "sissy": {
    "dict": "anew", "word": "sissy", "stem": "sissi",
    "avg": [ 3.14, 5.17 ], "std": [ 1.96, 2.57 ], "fq": 0
  },
  "skeptical": {
    "dict": "anew", "word": "skeptical", "stem": "skeptic",
    "avg": [ 4.52, 4.91 ], "std": [ 1.63, 1.92 ], "fq": 7
  },
  "skijump": {
    "dict": "anew", "word": "skijump", "stem": "skijump",
    "avg": [ 7.06, 7.06 ], "std": [ 1.73, 2.10 ], "fq": 0
  },
  "skull": {
    "dict": "anew", "word": "skull", "stem": "skull",
    "avg": [ 4.27, 4.75 ], "std": [ 1.83, 1.85 ], "fq": 3
  },
  "sky": {
    "dict": "anew", "word": "sky", "stem": "sky",
    "avg": [ 7.37, 4.27 ], "std": [ 1.40, 2.17 ], "fq": 58
  },
  "skyscraper": {
    "dict": "anew", "word": "skyscraper", "stem": "skyscrap",
    "avg": [ 5.88, 5.71 ], "std": [ 1.87, 2.17 ], "fq": 2
  },
  "slap": {
    "dict": "anew", "word": "slap", "stem": "slap",
    "avg": [ 2.95, 6.46 ], "std": [ 1.79, 2.58 ], "fq": 2
  },
  "slaughter": {
    "dict": "anew", "word": "slaughter", "stem": "slaughter",
    "avg": [ 1.64, 6.77 ], "std": [ 1.18, 2.42 ], "fq": 10
  },
  "slave": {
    "dict": "anew", "word": "slave", "stem": "slave",
    "avg": [ 1.84, 6.21 ], "std": [ 1.13, 2.93 ], "fq": 30
  },
  "sleep": {
    "dict": "anew", "word": "sleep", "stem": "sleep",
    "avg": [ 7.20, 2.80 ], "std": [ 1.77, 2.66 ], "fq": 65
  },
  "slime": {
    "dict": "anew", "word": "slime", "stem": "slime",
    "avg": [ 2.68, 5.36 ], "std": [ 1.66, 2.63 ], "fq": 1
  },
  "slow": {
    "dict": "anew", "word": "slow", "stem": "slow",
    "avg": [ 3.93, 3.39 ], "std": [ 1.60, 2.22 ], "fq": 60
  },
  "slum": {
    "dict": "anew", "word": "slum", "stem": "slum",
    "avg": [ 2.39, 4.78 ], "std": [ 1.25, 2.52 ], "fq": 8
  },
  "slush": {
    "dict": "anew", "word": "slush", "stem": "slush",
    "avg": [ 4.66, 3.73 ], "std": [ 1.88, 2.23 ], "fq": 0
  },
  "smallpox": {
    "dict": "anew", "word": "smallpox", "stem": "smallpox",
    "avg": [ 2.52, 5.58 ], "std": [ 2.08, 2.13 ], "fq": 2
  },
  "smooth": {
    "dict": "anew", "word": "smooth", "stem": "smooth",
    "avg": [ 6.58, 4.91 ], "std": [ 1.78, 2.57 ], "fq": 42
  },
  "snake": {
    "dict": "anew", "word": "snake", "stem": "snake",
    "avg": [ 3.31, 6.82 ], "std": [ 2.20, 2.10 ], "fq": 44
  },
  "snob": {
    "dict": "anew", "word": "snob", "stem": "snob",
    "avg": [ 3.36, 5.65 ], "std": [ 1.81, 2.36 ], "fq": 1
  },
  "snow": {
    "dict": "anew", "word": "snow", "stem": "snow",
    "avg": [ 7.08, 5.75 ], "std": [ 1.83, 2.47 ], "fq": 59
  },
  "snuggle": {
    "dict": "anew", "word": "snuggle", "stem": "snuggl",
    "avg": [ 7.92, 4.16 ], "std": [ 1.24, 2.80 ], "fq": 4
  },
  "social": {
    "dict": "anew", "word": "social", "stem": "social",
    "avg": [ 6.88, 4.98 ], "std": [ 1.82, 2.59 ], "fq": 380
  },
  "soft": {
    "dict": "anew", "word": "soft", "stem": "soft",
    "avg": [ 7.12, 4.63 ], "std": [ 1.34, 2.61 ], "fq": 61
  },
  "solemn": {
    "dict": "anew", "word": "solemn", "stem": "solemn",
    "avg": [ 4.32, 3.56 ], "std": [ 1.51, 1.95 ], "fq": 12
  },
  "song": {
    "dict": "anew", "word": "song", "stem": "song",
    "avg": [ 7.10, 6.07 ], "std": [ 1.97, 2.42 ], "fq": 70
  },
  "soothe": {
    "dict": "anew", "word": "soothe", "stem": "sooth",
    "avg": [ 7.30, 4.40 ], "std": [ 1.85, 3.08 ], "fq": 2
  },
  "sour": {
    "dict": "anew", "word": "sour", "stem": "sour",
    "avg": [ 3.93, 5.10 ], "std": [ 1.98, 1.95 ], "fq": 3
  },
  "space": {
    "dict": "anew", "word": "space", "stem": "space",
    "avg": [ 6.78, 5.14 ], "std": [ 1.66, 2.54 ], "fq": 184
  },
  "spanking": {
    "dict": "anew", "word": "spanking", "stem": "spank",
    "avg": [ 3.55, 5.41 ], "std": [ 2.54, 2.73 ], "fq": 0
  },
  "sphere": {
    "dict": "anew", "word": "sphere", "stem": "sphere",
    "avg": [ 5.33, 3.88 ], "std": [ 0.87, 1.99 ], "fq": 22
  },
  "spider": {
    "dict": "anew", "word": "spider", "stem": "spider",
    "avg": [ 3.33, 5.71 ], "std": [ 1.72, 2.21 ], "fq": 2
  },
  "spirit": {
    "dict": "anew", "word": "spirit", "stem": "spirit",
    "avg": [ 7.00, 5.56 ], "std": [ 1.32, 2.62 ], "fq": 182
  },
  "spouse": {
    "dict": "anew", "word": "spouse", "stem": "spous",
    "avg": [ 7.58, 5.21 ], "std": [ 1.48, 2.75 ], "fq": 3
  },
  "spray": {
    "dict": "anew", "word": "spray", "stem": "spray",
    "avg": [ 5.45, 4.14 ], "std": [ 1.63, 2.28 ], "fq": 16
  },
  "spring": {
    "dict": "anew", "word": "spring", "stem": "spring",
    "avg": [ 7.76, 5.67 ], "std": [ 1.51, 2.51 ], "fq": 127
  },
  "square": {
    "dict": "anew", "word": "square", "stem": "squar",
    "avg": [ 4.74, 3.18 ], "std": [ 1.02, 1.76 ], "fq": 143
  },
  "stagnant": {
    "dict": "anew", "word": "stagnant", "stem": "stagnant",
    "avg": [ 4.15, 3.93 ], "std": [ 1.57, 1.94 ], "fq": 5
  },
  "star": {
    "dict": "anew", "word": "star", "stem": "star",
    "avg": [ 7.27, 5.83 ], "std": [ 1.66, 2.44 ], "fq": 25
  },
  "startled": {
    "dict": "anew", "word": "startled", "stem": "startl",
    "avg": [ 4.50, 6.93 ], "std": [ 1.67, 2.24 ], "fq": 21
  },
  "starving": {
    "dict": "anew", "word": "starving", "stem": "starv",
    "avg": [ 2.39, 5.61 ], "std": [ 1.82, 2.53 ], "fq": 6
  },
  "statue": {
    "dict": "anew", "word": "statue", "stem": "statu",
    "avg": [ 5.17, 3.46 ], "std": [ 0.70, 1.72 ], "fq": 17
  },
  "stench": {
    "dict": "anew", "word": "stench", "stem": "stench",
    "avg": [ 2.19, 4.36 ], "std": [ 1.37, 2.46 ], "fq": 1
  },
  "stiff": {
    "dict": "anew", "word": "stiff", "stem": "stiff",
    "avg": [ 4.68, 4.02 ], "std": [ 1.97, 2.41 ], "fq": 21
  },
  "stink": {
    "dict": "anew", "word": "stink", "stem": "stink",
    "avg": [ 3.00, 4.26 ], "std": [ 1.79, 2.10 ], "fq": 3
  },
  "stomach": {
    "dict": "anew", "word": "stomach", "stem": "stomach",
    "avg": [ 4.82, 3.93 ], "std": [ 2.06, 2.49 ], "fq": 37
  },
  "stool": {
    "dict": "anew", "word": "stool", "stem": "stool",
    "avg": [ 4.56, 4.00 ], "std": [ 1.72, 2.14 ], "fq": 8
  },
  "storm": {
    "dict": "anew", "word": "storm", "stem": "storm",
    "avg": [ 4.95, 5.71 ], "std": [ 2.22, 2.34 ], "fq": 26
  },
  "stove": {
    "dict": "anew", "word": "stove", "stem": "stove",
    "avg": [ 4.98, 4.51 ], "std": [ 1.69, 2.14 ], "fq": 15
  },
  "street": {
    "dict": "anew", "word": "street", "stem": "street",
    "avg": [ 5.22, 3.39 ], "std": [ 0.72, 1.87 ], "fq": 244
  },
  "stress": {
    "dict": "anew", "word": "stress", "stem": "stress",
    "avg": [ 2.09, 7.45 ], "std": [ 1.41, 2.38 ], "fq": 107
  },
  "strong": {
    "dict": "anew", "word": "strong", "stem": "strong",
    "avg": [ 7.11, 5.92 ], "std": [ 1.48, 2.28 ], "fq": 202
  },
  "stupid": {
    "dict": "anew", "word": "stupid", "stem": "stupid",
    "avg": [ 2.31, 4.72 ], "std": [ 1.37, 2.71 ], "fq": 24
  },
  "subdued": {
    "dict": "anew", "word": "subdued", "stem": "subdu",
    "avg": [ 4.67, 2.90 ], "std": [ 1.31, 1.81 ], "fq": 8
  },
  "success": {
    "dict": "anew", "word": "success", "stem": "success",
    "avg": [ 8.29, 6.11 ], "std": [ 0.93, 2.65 ], "fq": 93
  },
  "suffocate": {
    "dict": "anew", "word": "suffocate", "stem": "suffoc",
    "avg": [ 1.56, 6.03 ], "std": [ 0.96, 3.19 ], "fq": 1
  },
  "sugar": {
    "dict": "anew", "word": "sugar", "stem": "sugar",
    "avg": [ 6.74, 5.64 ], "std": [ 1.73, 2.18 ], "fq": 34
  },
  "suicide": {
    "dict": "anew", "word": "suicide", "stem": "suicid",
    "avg": [ 1.25, 5.73 ], "std": [ 0.69, 3.14 ], "fq": 17
  },
  "sun": {
    "dict": "anew", "word": "sun", "stem": "sun",
    "avg": [ 7.55, 5.04 ], "std": [ 1.85, 2.66 ], "fq": 112
  },
  "sunlight": {
    "dict": "anew", "word": "sunlight", "stem": "sunlight",
    "avg": [ 7.76, 6.10 ], "std": [ 1.43, 2.30 ], "fq": 17
  },
  "sunrise": {
    "dict": "anew", "word": "sunrise", "stem": "sunris",
    "avg": [ 7.86, 5.06 ], "std": [ 1.35, 3.05 ], "fq": 10
  },
  "sunset": {
    "dict": "anew", "word": "sunset", "stem": "sunset",
    "avg": [ 7.68, 4.20 ], "std": [ 1.72, 2.99 ], "fq": 14
  },
  "surgery": {
    "dict": "anew", "word": "surgery", "stem": "surgeri",
    "avg": [ 2.86, 6.35 ], "std": [ 2.19, 2.32 ], "fq": 6
  },
  "surprised": {
    "dict": "anew", "word": "surprised", "stem": "surpris",
    "avg": [ 7.47, 7.47 ], "std": [ 1.56, 2.09 ], "fq": 58
  },
  "suspicious": {
    "dict": "anew", "word": "suspicious", "stem": "suspici",
    "avg": [ 3.76, 6.25 ], "std": [ 1.42, 1.59 ], "fq": 13
  },
  "swamp": {
    "dict": "anew", "word": "swamp", "stem": "swamp",
    "avg": [ 5.14, 4.86 ], "std": [ 2.24, 2.36 ], "fq": 5
  },
  "sweetheart": {
    "dict": "anew", "word": "sweetheart", "stem": "sweetheart",
    "avg": [ 8.42, 5.50 ], "std": [ 0.83, 2.73 ], "fq": 9
  },
  "swift": {
    "dict": "anew", "word": "swift", "stem": "swift",
    "avg": [ 6.46, 5.39 ], "std": [ 1.76, 2.53 ], "fq": 32
  },
  "swimmer": {
    "dict": "anew", "word": "swimmer", "stem": "swimmer",
    "avg": [ 6.54, 4.82 ], "std": [ 1.64, 2.49 ], "fq": 0
  },
  "syphilis": {
    "dict": "anew", "word": "syphilis", "stem": "syphili",
    "avg": [ 1.68, 5.69 ], "std": [ 1.23, 3.25 ], "fq": 0
  },
  "table": {
    "dict": "anew", "word": "table", "stem": "tabl",
    "avg": [ 5.22, 2.92 ], "std": [ 0.72, 2.16 ], "fq": 198
  },
  "talent": {
    "dict": "anew", "word": "talent", "stem": "talent",
    "avg": [ 7.56, 6.27 ], "std": [ 1.25, 1.80 ], "fq": 40
  },
  "tamper": {
    "dict": "anew", "word": "tamper", "stem": "tamper",
    "avg": [ 4.10, 4.95 ], "std": [ 1.88, 2.01 ], "fq": 1
  },
  "tank": {
    "dict": "anew", "word": "tank", "stem": "tank",
    "avg": [ 5.16, 4.88 ], "std": [ 1.87, 1.86 ], "fq": 12
  },
  "taste": {
    "dict": "anew", "word": "taste", "stem": "tast",
    "avg": [ 6.66, 5.22 ], "std": [ 1.57, 2.38 ], "fq": 59
  },
  "taxi": {
    "dict": "anew", "word": "taxi", "stem": "taxi",
    "avg": [ 5.00, 3.41 ], "std": [ 1.96, 2.14 ], "fq": 16
  },
  "teacher": {
    "dict": "anew", "word": "teacher", "stem": "teacher",
    "avg": [ 5.68, 4.05 ], "std": [ 2.12, 2.61 ], "fq": 80
  },
  "tease": {
    "dict": "anew", "word": "tease", "stem": "teas",
    "avg": [ 4.84, 5.87 ], "std": [ 2.51, 2.56 ], "fq": 6
  },
  "tender": {
    "dict": "anew", "word": "tender", "stem": "tender",
    "avg": [ 6.93, 4.88 ], "std": [ 1.28, 2.30 ], "fq": 11
  },
  "tennis": {
    "dict": "anew", "word": "tennis", "stem": "tenni",
    "avg": [ 6.02, 4.61 ], "std": [ 1.97, 2.60 ], "fq": 15
  },
  "tense": {
    "dict": "anew", "word": "tense", "stem": "tens",
    "avg": [ 3.56, 6.53 ], "std": [ 1.36, 2.10 ], "fq": 15
  },
  "termite": {
    "dict": "anew", "word": "termite", "stem": "termit",
    "avg": [ 3.58, 5.39 ], "std": [ 2.08, 2.43 ], "fq": 0
  },
  "terrible": {
    "dict": "anew", "word": "terrible", "stem": "terribl",
    "avg": [ 1.93, 6.27 ], "std": [ 1.44, 2.44 ], "fq": 45
  },
  "terrific": {
    "dict": "anew", "word": "terrific", "stem": "terrif",
    "avg": [ 8.16, 6.23 ], "std": [ 1.12, 2.73 ], "fq": 5
  },
  "terrified": {
    "dict": "anew", "word": "terrified", "stem": "terrifi",
    "avg": [ 1.72, 7.86 ], "std": [ 1.14, 2.27 ], "fq": 7
  },
  "terrorist": {
    "dict": "anew", "word": "terrorist", "stem": "terrorist",
    "avg": [ 1.69, 7.27 ], "std": [ 1.42, 2.38 ], "fq": 0
  },
  "thankful": {
    "dict": "anew", "word": "thankful", "stem": "thank",
    "avg": [ 6.89, 4.34 ], "std": [ 2.29, 2.31 ], "fq": 6
  },
  "theory": {
    "dict": "anew", "word": "theory", "stem": "theori",
    "avg": [ 5.30, 4.62 ], "std": [ 1.49, 1.94 ], "fq": 129
  },
  "thermometer": {
    "dict": "anew", "word": "thermometer", "stem": "thermomet",
    "avg": [ 4.73, 3.79 ], "std": [ 1.05, 2.02 ], "fq": 0
  },
  "thief": {
    "dict": "anew", "word": "thief", "stem": "thief",
    "avg": [ 2.13, 6.89 ], "std": [ 1.69, 2.13 ], "fq": 8
  },
  "thorn": {
    "dict": "anew", "word": "thorn", "stem": "thorn",
    "avg": [ 3.64, 5.14 ], "std": [ 1.76, 2.14 ], "fq": 3
  },
  "thought": {
    "dict": "anew", "word": "thought", "stem": "thought",
    "avg": [ 6.39, 4.83 ], "std": [ 1.58, 2.46 ], "fq": 515
  },
  "thoughtful": {
    "dict": "anew", "word": "thoughtful", "stem": "thought",
    "avg": [ 7.65, 5.72 ], "std": [ 1.03, 2.30 ], "fq": 11
  },
  "thrill": {
    "dict": "anew", "word": "thrill", "stem": "thrill",
    "avg": [ 8.05, 8.02 ], "std": [ 1.48, 1.65 ], "fq": 5
  },
  "tidy": {
    "dict": "anew", "word": "tidy", "stem": "tidi",
    "avg": [ 6.30, 3.98 ], "std": [ 1.56, 2.22 ], "fq": 1
  },
  "time": {
    "dict": "anew", "word": "time", "stem": "time",
    "avg": [ 5.31, 4.64 ], "std": [ 2.02, 2.75 ], "fq": 1599
  },
  "timid": {
    "dict": "anew", "word": "timid", "stem": "timid",
    "avg": [ 3.86, 4.11 ], "std": [ 1.55, 2.09 ], "fq": 5
  },
  "tobacco": {
    "dict": "anew", "word": "tobacco", "stem": "tobacco",
    "avg": [ 3.28, 4.83 ], "std": [ 2.16, 2.90 ], "fq": 19
  },
  "tomb": {
    "dict": "anew", "word": "tomb", "stem": "tomb",
    "avg": [ 2.94, 4.73 ], "std": [ 1.88, 2.72 ], "fq": 11
  },
  "tool": {
    "dict": "anew", "word": "tool", "stem": "tool",
    "avg": [ 5.19, 4.33 ], "std": [ 1.27, 1.78 ], "fq": 40
  },
  "toothache": {
    "dict": "anew", "word": "toothache", "stem": "toothach",
    "avg": [ 1.98, 5.55 ], "std": [ 1.15, 2.51 ], "fq": 0
  },
  "tornado": {
    "dict": "anew", "word": "tornado", "stem": "tornado",
    "avg": [ 2.55, 6.83 ], "std": [ 1.78, 2.49 ], "fq": 1
  },
  "torture": {
    "dict": "anew", "word": "torture", "stem": "tortur",
    "avg": [ 1.56, 6.10 ], "std": [ 0.79, 2.77 ], "fq": 3
  },
  "tower": {
    "dict": "anew", "word": "tower", "stem": "tower",
    "avg": [ 5.46, 3.95 ], "std": [ 1.75, 2.28 ], "fq": 13
  },
  "toxic": {
    "dict": "anew", "word": "toxic", "stem": "toxic",
    "avg": [ 2.10, 6.40 ], "std": [ 1.48, 2.41 ], "fq": 3
  },
  "toy": {
    "dict": "anew", "word": "toy", "stem": "toy",
    "avg": [ 7.00, 5.11 ], "std": [ 2.01, 2.84 ], "fq": 4
  },
  "tragedy": {
    "dict": "anew", "word": "tragedy", "stem": "tragedi",
    "avg": [ 1.78, 6.24 ], "std": [ 1.31, 2.64 ], "fq": 49
  },
  "traitor": {
    "dict": "anew", "word": "traitor", "stem": "traitor",
    "avg": [ 2.22, 5.78 ], "std": [ 1.69, 2.47 ], "fq": 2
  },
  "trash": {
    "dict": "anew", "word": "trash", "stem": "trash",
    "avg": [ 2.67, 4.16 ], "std": [ 1.45, 2.16 ], "fq": 2
  },
  "trauma": {
    "dict": "anew", "word": "trauma", "stem": "trauma",
    "avg": [ 2.10, 6.33 ], "std": [ 1.49, 2.45 ], "fq": 1
  },
  "travel": {
    "dict": "anew", "word": "travel", "stem": "travel",
    "avg": [ 7.10, 6.21 ], "std": [ 2.00, 2.51 ], "fq": 61
  },
  "treasure": {
    "dict": "anew", "word": "treasure", "stem": "treasur",
    "avg": [ 8.27, 6.75 ], "std": [ 0.90, 2.30 ], "fq": 4
  },
  "treat": {
    "dict": "anew", "word": "treat", "stem": "treat",
    "avg": [ 7.36, 5.62 ], "std": [ 1.38, 2.25 ], "fq": 26
  },
  "tree": {
    "dict": "anew", "word": "tree", "stem": "tree",
    "avg": [ 6.32, 3.42 ], "std": [ 1.56, 2.21 ], "fq": 59
  },
  "triumph": {
    "dict": "anew", "word": "triumph", "stem": "triumph",
    "avg": [ 7.80, 5.78 ], "std": [ 1.83, 2.60 ], "fq": 22
  },
  "triumphant": {
    "dict": "anew", "word": "triumphant", "stem": "triumphant",
    "avg": [ 8.82, 6.78 ], "std": [ 0.73, 2.58 ], "fq": 5
  },
  "trophy": {
    "dict": "anew", "word": "trophy", "stem": "trophi",
    "avg": [ 7.78, 5.39 ], "std": [ 1.22, 2.44 ], "fq": 8
  },
  "trouble": {
    "dict": "anew", "word": "trouble", "stem": "troubl",
    "avg": [ 3.03, 6.85 ], "std": [ 2.09, 2.03 ], "fq": 134
  },
  "troubled": {
    "dict": "anew", "word": "troubled", "stem": "troubl",
    "avg": [ 2.17, 5.94 ], "std": [ 1.21, 2.36 ], "fq": 31
  },
  "truck": {
    "dict": "anew", "word": "truck", "stem": "truck",
    "avg": [ 5.47, 4.84 ], "std": [ 1.88, 2.17 ], "fq": 57
  },
  "trumpet": {
    "dict": "anew", "word": "trumpet", "stem": "trumpet",
    "avg": [ 5.75, 4.97 ], "std": [ 1.38, 2.13 ], "fq": 7
  },
  "trunk": {
    "dict": "anew", "word": "trunk", "stem": "trunk",
    "avg": [ 5.09, 4.18 ], "std": [ 1.57, 2.19 ], "fq": 8
  },
  "trust": {
    "dict": "anew", "word": "trust", "stem": "trust",
    "avg": [ 6.68, 5.30 ], "std": [ 2.71, 2.66 ], "fq": 52
  },
  "truth": {
    "dict": "anew", "word": "truth", "stem": "truth",
    "avg": [ 7.80, 5.00 ], "std": [ 1.29, 2.77 ], "fq": 126
  },
  "tumor": {
    "dict": "anew", "word": "tumor", "stem": "tumor",
    "avg": [ 2.36, 6.51 ], "std": [ 2.04, 2.85 ], "fq": 17
  },
  "tune": {
    "dict": "anew", "word": "tune", "stem": "tune",
    "avg": [ 6.93, 4.71 ], "std": [ 1.47, 2.09 ], "fq": 10
  },
  "twilight": {
    "dict": "anew", "word": "twilight", "stem": "twilight",
    "avg": [ 7.23, 4.70 ], "std": [ 1.80, 2.41 ], "fq": 4
  },
  "ugly": {
    "dict": "anew", "word": "ugly", "stem": "ugli",
    "avg": [ 2.43, 5.38 ], "std": [ 1.27, 2.23 ], "fq": 21
  },
  "ulcer": {
    "dict": "anew", "word": "ulcer", "stem": "ulcer",
    "avg": [ 1.78, 6.12 ], "std": [ 1.17, 2.68 ], "fq": 5
  },
  "umbrella": {
    "dict": "anew", "word": "umbrella", "stem": "umbrella",
    "avg": [ 5.16, 3.68 ], "std": [ 1.57, 1.99 ], "fq": 8
  },
  "unfaithful": {
    "dict": "anew", "word": "unfaithful", "stem": "unfaith",
    "avg": [ 2.05, 6.20 ], "std": [ 1.55, 2.70 ], "fq": 1
  },
  "unhappy": {
    "dict": "anew", "word": "unhappy", "stem": "unhappi",
    "avg": [ 1.57, 4.18 ], "std": [ 0.96, 2.50 ], "fq": 26
  },
  "unit": {
    "dict": "anew", "word": "unit", "stem": "unit",
    "avg": [ 5.59, 3.75 ], "std": [ 1.87, 2.49 ], "fq": 103
  },
  "untroubled": {
    "dict": "anew", "word": "untroubled", "stem": "untroubl",
    "avg": [ 7.62, 3.89 ], "std": [ 1.41, 2.54 ], "fq": 0
  },
  "upset": {
    "dict": "anew", "word": "upset", "stem": "upset",
    "avg": [ 2.00, 5.86 ], "std": [ 1.18, 2.40 ], "fq": 14
  },
  "urine": {
    "dict": "anew", "word": "urine", "stem": "urin",
    "avg": [ 3.25, 4.20 ], "std": [ 1.71, 2.18 ], "fq": 1
  },
  "useful": {
    "dict": "anew", "word": "useful", "stem": "use",
    "avg": [ 7.14, 4.26 ], "std": [ 1.60, 2.47 ], "fq": 58
  },
  "useless": {
    "dict": "anew", "word": "useless", "stem": "useless",
    "avg": [ 2.13, 4.87 ], "std": [ 1.42, 2.58 ], "fq": 17
  },
  "utensil": {
    "dict": "anew", "word": "utensil", "stem": "utensil",
    "avg": [ 5.14, 3.57 ], "std": [ 1.39, 1.98 ], "fq": 0
  },
  "vacation": {
    "dict": "anew", "word": "vacation", "stem": "vacat",
    "avg": [ 8.16, 5.64 ], "std": [ 1.36, 2.99 ], "fq": 47
  },
  "vagina": {
    "dict": "anew", "word": "vagina", "stem": "vagina",
    "avg": [ 6.14, 5.55 ], "std": [ 1.77, 2.55 ], "fq": 10
  },
  "valentine": {
    "dict": "anew", "word": "valentine", "stem": "valentin",
    "avg": [ 8.11, 6.06 ], "std": [ 1.35, 2.91 ], "fq": 2
  },
  "vampire": {
    "dict": "anew", "word": "vampire", "stem": "vampir",
    "avg": [ 4.26, 6.37 ], "std": [ 1.86, 2.35 ], "fq": 1
  },
  "vandal": {
    "dict": "anew", "word": "vandal", "stem": "vandal",
    "avg": [ 2.71, 6.40 ], "std": [ 1.91, 1.88 ], "fq": 1
  },
  "vanity": {
    "dict": "anew", "word": "vanity", "stem": "vaniti",
    "avg": [ 4.30, 4.98 ], "std": [ 1.91, 2.31 ], "fq": 7
  },
  "vehicle": {
    "dict": "anew", "word": "vehicle", "stem": "vehicl",
    "avg": [ 6.27, 4.63 ], "std": [ 2.34, 2.81 ], "fq": 35
  },
  "venom": {
    "dict": "anew", "word": "venom", "stem": "venom",
    "avg": [ 2.68, 6.08 ], "std": [ 1.81, 2.44 ], "fq": 2
  },
  "vest": {
    "dict": "anew", "word": "vest", "stem": "vest",
    "avg": [ 5.25, 3.95 ], "std": [ 1.33, 2.09 ], "fq": 4
  },
  "victim": {
    "dict": "anew", "word": "victim", "stem": "victim",
    "avg": [ 2.18, 6.06 ], "std": [ 1.48, 2.32 ], "fq": 27
  },
  "victory": {
    "dict": "anew", "word": "victory", "stem": "victori",
    "avg": [ 8.32, 6.63 ], "std": [ 1.16, 2.84 ], "fq": 61
  },
  "vigorous": {
    "dict": "anew", "word": "vigorous", "stem": "vigor",
    "avg": [ 6.79, 5.90 ], "std": [ 1.54, 2.66 ], "fq": 29
  },
  "village": {
    "dict": "anew", "word": "village", "stem": "villag",
    "avg": [ 5.92, 4.08 ], "std": [ 1.34, 1.87 ], "fq": 72
  },
  "violent": {
    "dict": "anew", "word": "violent", "stem": "violent",
    "avg": [ 2.29, 6.89 ], "std": [ 1.78, 2.47 ], "fq": 33
  },
  "violin": {
    "dict": "anew", "word": "violin", "stem": "violin",
    "avg": [ 5.43, 3.49 ], "std": [ 1.98, 2.26 ], "fq": 11
  },
  "virgin": {
    "dict": "anew", "word": "virgin", "stem": "virgin",
    "avg": [ 6.45, 5.51 ], "std": [ 1.76, 2.06 ], "fq": 35
  },
  "virtue": {
    "dict": "anew", "word": "virtue", "stem": "virtu",
    "avg": [ 6.22, 4.52 ], "std": [ 2.06, 2.52 ], "fq": 30
  },
  "vision": {
    "dict": "anew", "word": "vision", "stem": "vision",
    "avg": [ 6.62, 4.66 ], "std": [ 1.84, 2.43 ], "fq": 56
  },
  "volcano": {
    "dict": "anew", "word": "volcano", "stem": "volcano",
    "avg": [ 4.84, 6.33 ], "std": [ 2.14, 2.21 ], "fq": 2
  },
  "vomit": {
    "dict": "anew", "word": "vomit", "stem": "vomit",
    "avg": [ 2.06, 5.75 ], "std": [ 1.57, 2.84 ], "fq": 3
  },
  "voyage": {
    "dict": "anew", "word": "voyage", "stem": "voyag",
    "avg": [ 6.25, 5.55 ], "std": [ 1.91, 2.23 ], "fq": 17
  },
  "wagon": {
    "dict": "anew", "word": "wagon", "stem": "wagon",
    "avg": [ 5.37, 3.98 ], "std": [ 0.97, 2.04 ], "fq": 55
  },
  "war": {
    "dict": "anew", "word": "war", "stem": "war",
    "avg": [ 2.08, 7.49 ], "std": [ 1.91, 2.16 ], "fq": 464
  },
  "warmth": {
    "dict": "anew", "word": "warmth", "stem": "warmth",
    "avg": [ 7.41, 3.73 ], "std": [ 1.81, 2.40 ], "fq": 28
  },
  "wasp": {
    "dict": "anew", "word": "wasp", "stem": "wasp",
    "avg": [ 3.37, 5.50 ], "std": [ 1.63, 2.17 ], "fq": 2
  },
  "waste": {
    "dict": "anew", "word": "waste", "stem": "wast",
    "avg": [ 2.93, 4.14 ], "std": [ 1.76, 2.30 ], "fq": 35
  },
  "watch": {
    "dict": "anew", "word": "watch", "stem": "watch",
    "avg": [ 5.78, 4.10 ], "std": [ 1.51, 2.12 ], "fq": 81
  },
  "water": {
    "dict": "anew", "word": "water", "stem": "water",
    "avg": [ 6.61, 4.97 ], "std": [ 1.78, 2.49 ], "fq": 442
  },
  "waterfall": {
    "dict": "anew", "word": "waterfall", "stem": "waterfal",
    "avg": [ 7.88, 5.37 ], "std": [ 1.03, 2.84 ], "fq": 2
  },
  "wealthy": {
    "dict": "anew", "word": "wealthy", "stem": "wealthi",
    "avg": [ 7.70, 5.80 ], "std": [ 1.34, 2.73 ], "fq": 12
  },
  "weapon": {
    "dict": "anew", "word": "weapon", "stem": "weapon",
    "avg": [ 3.97, 6.03 ], "std": [ 1.92, 1.89 ], "fq": 42
  },
  "weary": {
    "dict": "anew", "word": "weary", "stem": "weari",
    "avg": [ 3.79, 3.81 ], "std": [ 2.12, 2.29 ], "fq": 17
  },
  "wedding": {
    "dict": "anew", "word": "wedding", "stem": "wed",
    "avg": [ 7.82, 5.97 ], "std": [ 1.56, 2.85 ], "fq": 32
  },
  "whistle": {
    "dict": "anew", "word": "whistle", "stem": "whistl",
    "avg": [ 5.81, 4.69 ], "std": [ 1.21, 1.99 ], "fq": 4
  },
  "white": {
    "dict": "anew", "word": "white", "stem": "white",
    "avg": [ 6.47, 4.37 ], "std": [ 1.59, 2.14 ], "fq": 365
  },
  "whore": {
    "dict": "anew", "word": "whore", "stem": "whore",
    "avg": [ 2.30, 5.85 ], "std": [ 2.11, 2.93 ], "fq": 2
  },
  "wicked": {
    "dict": "anew", "word": "wicked", "stem": "wick",
    "avg": [ 2.96, 6.09 ], "std": [ 2.37, 2.44 ], "fq": 9
  },
  "wife": {
    "dict": "anew", "word": "wife", "stem": "wife",
    "avg": [ 6.33, 4.93 ], "std": [ 1.97, 2.22 ], "fq": 228
  },
  "win": {
    "dict": "anew", "word": "win", "stem": "win",
    "avg": [ 8.38, 7.72 ], "std": [ 0.92, 2.16 ], "fq": 55
  },
  "windmill": {
    "dict": "anew", "word": "windmill", "stem": "windmil",
    "avg": [ 5.60, 3.74 ], "std": [ 1.65, 2.13 ], "fq": 1
  },
  "window": {
    "dict": "anew", "word": "window", "stem": "window",
    "avg": [ 5.91, 3.97 ], "std": [ 1.38, 2.01 ], "fq": 119
  },
  "wine": {
    "dict": "anew", "word": "wine", "stem": "wine",
    "avg": [ 5.95, 4.78 ], "std": [ 2.19, 2.34 ], "fq": 72
  },
  "wink": {
    "dict": "anew", "word": "wink", "stem": "wink",
    "avg": [ 6.93, 5.44 ], "std": [ 1.83, 2.68 ], "fq": 7
  },
  "wise": {
    "dict": "anew", "word": "wise", "stem": "wise",
    "avg": [ 7.52, 3.91 ], "std": [ 1.23, 2.64 ], "fq": 36
  },
  "wish": {
    "dict": "anew", "word": "wish", "stem": "wish",
    "avg": [ 7.09, 5.16 ], "std": [ 2.00, 2.62 ], "fq": 110
  },
  "wit": {
    "dict": "anew", "word": "wit", "stem": "wit",
    "avg": [ 7.32, 5.42 ], "std": [ 1.90, 2.44 ], "fq": 20
  },
  "woman": {
    "dict": "anew", "word": "woman", "stem": "woman",
    "avg": [ 6.64, 5.32 ], "std": [ 1.76, 2.59 ], "fq": 224
  },
  "wonder": {
    "dict": "anew", "word": "wonder", "stem": "wonder",
    "avg": [ 6.03, 5.00 ], "std": [ 1.58, 2.23 ], "fq": 67
  },
  "world": {
    "dict": "anew", "word": "world", "stem": "world",
    "avg": [ 6.50, 5.32 ], "std": [ 2.03, 2.39 ], "fq": 787
  },
  "wounds": {
    "dict": "anew", "word": "wounds", "stem": "wound",
    "avg": [ 2.51, 5.82 ], "std": [ 1.58, 2.01 ], "fq": 8
  },
  "writer": {
    "dict": "anew", "word": "writer", "stem": "writer",
    "avg": [ 5.52, 4.33 ], "std": [ 1.90, 2.45 ], "fq": 73
  },
  "yacht": {
    "dict": "anew", "word": "yacht", "stem": "yacht",
    "avg": [ 6.95, 5.61 ], "std": [ 1.79, 2.72 ], "fq": 4
  },
  "yellow": {
    "dict": "anew", "word": "yellow", "stem": "yellow",
    "avg": [ 5.61, 4.43 ], "std": [ 1.94, 2.05 ], "fq": 55
  },
  "young": {
    "dict": "anew", "word": "young", "stem": "young",
    "avg": [ 6.89, 5.64 ], "std": [ 2.12, 2.51 ], "fq": 385
  },
  "youth": {
    "dict": "anew", "word": "youth", "stem": "youth",
    "avg": [ 6.75, 5.67 ], "std": [ 2.29, 2.52 ], "fq": 82
  },
  "zest": {
    "dict": "anew", "word": "zest", "stem": "zest",
    "avg": [ 6.79, 5.59 ], "std": [ 2.04, 2.66 ], "fq": 5
  }
}

#  ANEW stemmed terms w/word, stem, avg valence and arousal, stdev of
#  valience and arousal, and number of evaluations

anew_stem = {
  "abduct": {
    "dict": "anew", "word": "abduction", "stem": "abduct",
    "avg": [ 2.76, 5.53 ], "std": [ 2.06, 2.43 ], "fq": 1
  },
  "abort": {
    "dict": "anew", "word": "abortion", "stem": "abort",
    "avg": [ 3.50, 5.39 ], "std": [ 2.30, 2.80 ], "fq": 6
  },
  "absurd": {
    "dict": "anew", "word": "absurd", "stem": "absurd",
    "avg": [ 4.26, 4.36 ], "std": [ 1.82, 2.20 ], "fq": 17
  },
  "abund": {
    "dict": "anew", "word": "abundance", "stem": "abund",
    "avg": [ 6.59, 5.51 ], "std": [ 2.01, 2.63 ], "fq": 13
  },
  "abus": {
    "dict": "anew", "word": "abuse", "stem": "abus",
    "avg": [ 1.80, 6.83 ], "std": [ 1.23, 2.70 ], "fq": 18
  },
  "accept": {
    "dict": "anew", "word": "acceptance", "stem": "accept",
    "avg": [ 7.98, 5.40 ], "std": [ 1.42, 2.70 ], "fq": 49
  },
  "accid": {
    "dict": "anew", "word": "accident", "stem": "accid",
    "avg": [ 2.05, 6.26 ], "std": [ 1.19, 2.87 ], "fq": 33
  },
  "ace": {
    "dict": "anew", "word": "ace", "stem": "ace",
    "avg": [ 6.88, 5.50 ], "std": [ 1.93, 2.66 ], "fq": 15
  },
  "ach": {
    "dict": "anew", "word": "ache", "stem": "ach",
    "avg": [ 2.46, 5.00 ], "std": [ 1.52, 2.45 ], "fq": 4
  },
  "achiev": {
    "dict": "anew", "word": "achievement", "stem": "achiev",
    "avg": [ 7.89, 5.53 ], "std": [ 1.38, 2.81 ], "fq": 65
  },
  "activ": {
    "dict": "anew", "word": "activate", "stem": "activ",
    "avg": [ 5.46, 4.86 ], "std": [ 0.98, 2.56 ], "fq": 2
  },
  "addict": {
    "dict": "anew", "word": "addict", "stem": "addict",
    "avg": [ 2.48, 5.66 ], "std": [ 2.08, 2.26 ], "fq": 1
  },
  "addict": {
    "dict": "anew", "word": "addicted", "stem": "addict",
    "avg": [ 2.51, 4.81 ], "std": [ 1.42, 2.46 ], "fq": 3
  },
  "admir": {
    "dict": "anew", "word": "admired", "stem": "admir",
    "avg": [ 7.74, 6.11 ], "std": [ 1.84, 2.36 ], "fq": 17
  },
  "ador": {
    "dict": "anew", "word": "adorable", "stem": "ador",
    "avg": [ 7.81, 5.12 ], "std": [ 1.24, 2.71 ], "fq": 3
  },
  "adult": {
    "dict": "anew", "word": "adult", "stem": "adult",
    "avg": [ 6.49, 4.76 ], "std": [ 1.50, 1.95 ], "fq": 25
  },
  "advantag": {
    "dict": "anew", "word": "advantage", "stem": "advantag",
    "avg": [ 6.95, 4.76 ], "std": [ 1.85, 2.18 ], "fq": 73
  },
  "adventur": {
    "dict": "anew", "word": "adventure", "stem": "adventur",
    "avg": [ 7.60, 6.98 ], "std": [ 1.50, 2.15 ], "fq": 14
  },
  "affect": {
    "dict": "anew", "word": "affection", "stem": "affect",
    "avg": [ 8.39, 6.21 ], "std": [ 0.86, 2.75 ], "fq": 18
  },
  "afraid": {
    "dict": "anew", "word": "afraid", "stem": "afraid",
    "avg": [ 2.00, 6.67 ], "std": [ 1.28, 2.54 ], "fq": 57
  },
  "aggress": {
    "dict": "anew", "word": "aggressive", "stem": "aggress",
    "avg": [ 5.10, 5.83 ], "std": [ 1.68, 2.33 ], "fq": 17
  },
  "agil": {
    "dict": "anew", "word": "agility", "stem": "agil",
    "avg": [ 6.46, 4.85 ], "std": [ 1.57, 1.80 ], "fq": 3
  },
  "agoni": {
    "dict": "anew", "word": "agony", "stem": "agoni",
    "avg": [ 2.43, 6.06 ], "std": [ 2.17, 2.67 ], "fq": 9
  },
  "agreement": {
    "dict": "anew", "word": "agreement", "stem": "agreement",
    "avg": [ 7.08, 5.02 ], "std": [ 1.59, 2.24 ], "fq": 106
  },
  "air": {
    "dict": "anew", "word": "air", "stem": "air",
    "avg": [ 6.34, 4.12 ], "std": [ 1.56, 2.30 ], "fq": 257
  },
  "alcohol": {
    "dict": "anew", "word": "alcoholic", "stem": "alcohol",
    "avg": [ 2.84, 5.69 ], "std": [ 2.34, 2.36 ], "fq": 3
  },
  "alert": {
    "dict": "anew", "word": "alert", "stem": "alert",
    "avg": [ 6.20, 6.85 ], "std": [ 1.76, 2.53 ], "fq": 33
  },
  "alien": {
    "dict": "anew", "word": "alien", "stem": "alien",
    "avg": [ 5.60, 5.45 ], "std": [ 1.82, 2.15 ], "fq": 16
  },
  "alimoni": {
    "dict": "anew", "word": "alimony", "stem": "alimoni",
    "avg": [ 3.95, 4.30 ], "std": [ 2.00, 2.29 ], "fq": 2
  },
  "aliv": {
    "dict": "anew", "word": "alive", "stem": "aliv",
    "avg": [ 7.25, 5.50 ], "std": [ 2.22, 2.74 ], "fq": 57
  },
  "allergi": {
    "dict": "anew", "word": "allergy", "stem": "allergi",
    "avg": [ 3.07, 4.64 ], "std": [ 1.64, 2.34 ], "fq": 1
  },
  "alley": {
    "dict": "anew", "word": "alley", "stem": "alley",
    "avg": [ 4.48, 4.91 ], "std": [ 1.97, 2.42 ], "fq": 8
  },
  "alon": {
    "dict": "anew", "word": "alone", "stem": "alon",
    "avg": [ 2.41, 4.83 ], "std": [ 1.77, 2.66 ], "fq": 195
  },
  "aloof": {
    "dict": "anew", "word": "aloof", "stem": "aloof",
    "avg": [ 4.90, 4.28 ], "std": [ 1.92, 2.10 ], "fq": 5
  },
  "ambit": {
    "dict": "anew", "word": "ambition", "stem": "ambit",
    "avg": [ 7.04, 5.61 ], "std": [ 1.98, 2.92 ], "fq": 19
  },
  "ambul": {
    "dict": "anew", "word": "ambulance", "stem": "ambul",
    "avg": [ 2.47, 7.33 ], "std": [ 1.50, 1.96 ], "fq": 6
  },
  "angel": {
    "dict": "anew", "word": "angel", "stem": "angel",
    "avg": [ 7.53, 4.83 ], "std": [ 1.58, 2.63 ], "fq": 18
  },
  "anger": {
    "dict": "anew", "word": "anger", "stem": "anger",
    "avg": [ 2.34, 7.63 ], "std": [ 1.32, 1.91 ], "fq": 48
  },
  "angri": {
    "dict": "anew", "word": "angry", "stem": "angri",
    "avg": [ 2.85, 7.17 ], "std": [ 1.70, 2.07 ], "fq": 45
  },
  "anguish": {
    "dict": "anew", "word": "anguished", "stem": "anguish",
    "avg": [ 2.12, 5.33 ], "std": [ 1.56, 2.69 ], "fq": 2
  },
  "ankl": {
    "dict": "anew", "word": "ankle", "stem": "ankl",
    "avg": [ 5.27, 4.16 ], "std": [ 1.54, 2.03 ], "fq": 8
  },
  "annoy": {
    "dict": "anew", "word": "annoy", "stem": "annoy",
    "avg": [ 2.74, 6.49 ], "std": [ 1.81, 2.17 ], "fq": 2
  },
  "answer": {
    "dict": "anew", "word": "answer", "stem": "answer",
    "avg": [ 6.63, 5.41 ], "std": [ 1.68, 2.43 ], "fq": 152
  },
  "anxious": {
    "dict": "anew", "word": "anxious", "stem": "anxious",
    "avg": [ 4.81, 6.92 ], "std": [ 1.98, 1.81 ], "fq": 29
  },
  "applaus": {
    "dict": "anew", "word": "applause", "stem": "applaus",
    "avg": [ 7.50, 5.80 ], "std": [ 1.50, 2.79 ], "fq": 14
  },
  "applianc": {
    "dict": "anew", "word": "appliance", "stem": "applianc",
    "avg": [ 5.10, 4.05 ], "std": [ 1.21, 2.06 ], "fq": 5
  },
  "arm": {
    "dict": "anew", "word": "arm", "stem": "arm",
    "avg": [ 5.34, 3.59 ], "std": [ 1.82, 2.40 ], "fq": 94
  },
  "armi": {
    "dict": "anew", "word": "army", "stem": "armi",
    "avg": [ 4.72, 5.03 ], "std": [ 1.75, 2.03 ], "fq": 132
  },
  "arous": {
    "dict": "anew", "word": "aroused", "stem": "arous",
    "avg": [ 7.97, 6.63 ], "std": [ 1.00, 2.70 ], "fq": 20
  },
  "arrog": {
    "dict": "anew", "word": "arrogant", "stem": "arrog",
    "avg": [ 3.69, 5.65 ], "std": [ 2.40, 2.23 ], "fq": 2
  },
  "art": {
    "dict": "anew", "word": "art", "stem": "art",
    "avg": [ 6.68, 4.86 ], "std": [ 2.10, 2.88 ], "fq": 208
  },
  "assassin": {
    "dict": "anew", "word": "assassin", "stem": "assassin",
    "avg": [ 3.09, 6.28 ], "std": [ 2.09, 2.53 ], "fq": 6
  },
  "assault": {
    "dict": "anew", "word": "assault", "stem": "assault",
    "avg": [ 2.03, 7.51 ], "std": [ 1.55, 2.28 ], "fq": 15
  },
  "astonish": {
    "dict": "anew", "word": "astonished", "stem": "astonish",
    "avg": [ 6.56, 6.58 ], "std": [ 1.61, 2.22 ], "fq": 6
  },
  "astronaut": {
    "dict": "anew", "word": "astronaut", "stem": "astronaut",
    "avg": [ 6.66, 5.28 ], "std": [ 1.60, 2.11 ], "fq": 2
  },
  "athlet": {
    "dict": "anew", "word": "athletics", "stem": "athlet",
    "avg": [ 6.61, 6.10 ], "std": [ 2.08, 2.29 ], "fq": 9
  },
  "autumn": {
    "dict": "anew", "word": "autumn", "stem": "autumn",
    "avg": [ 6.30, 4.51 ], "std": [ 2.14, 2.50 ], "fq": 22
  },
  "avalanch": {
    "dict": "anew", "word": "avalanche", "stem": "avalanch",
    "avg": [ 3.29, 5.54 ], "std": [ 1.95, 2.37 ], "fq": 1
  },
  "avenu": {
    "dict": "anew", "word": "avenue", "stem": "avenu",
    "avg": [ 5.50, 4.12 ], "std": [ 1.37, 2.01 ], "fq": 46
  },
  "awe": {
    "dict": "anew", "word": "awed", "stem": "awe",
    "avg": [ 6.70, 5.74 ], "std": [ 1.38, 2.31 ], "fq": 5
  },
  "babi": {
    "dict": "anew", "word": "baby", "stem": "babi",
    "avg": [ 8.22, 5.53 ], "std": [ 1.20, 2.80 ], "fq": 62
  },
  "bake": {
    "dict": "anew", "word": "bake", "stem": "bake",
    "avg": [ 6.17, 5.10 ], "std": [ 1.71, 2.30 ], "fq": 12
  },
  "bandag": {
    "dict": "anew", "word": "bandage", "stem": "bandag",
    "avg": [ 4.54, 3.90 ], "std": [ 1.75, 2.07 ], "fq": 4
  },
  "bankrupt": {
    "dict": "anew", "word": "bankrupt", "stem": "bankrupt",
    "avg": [ 2.00, 6.21 ], "std": [ 1.31, 2.79 ], "fq": 5
  },
  "banner": {
    "dict": "anew", "word": "banner", "stem": "banner",
    "avg": [ 5.40, 3.83 ], "std": [ 0.83, 1.95 ], "fq": 8
  },
  "bar": {
    "dict": "anew", "word": "bar", "stem": "bar",
    "avg": [ 6.42, 5.00 ], "std": [ 2.05, 2.83 ], "fq": 82
  },
  "barrel": {
    "dict": "anew", "word": "barrel", "stem": "barrel",
    "avg": [ 5.05, 3.36 ], "std": [ 1.46, 2.28 ], "fq": 24
  },
  "basket": {
    "dict": "anew", "word": "basket", "stem": "basket",
    "avg": [ 5.45, 3.63 ], "std": [ 1.15, 2.02 ], "fq": 17
  },
  "bastard": {
    "dict": "anew", "word": "bastard", "stem": "bastard",
    "avg": [ 3.36, 6.07 ], "std": [ 2.16, 2.15 ], "fq": 12
  },
  "bath": {
    "dict": "anew", "word": "bath", "stem": "bath",
    "avg": [ 7.33, 4.16 ], "std": [ 1.45, 2.31 ], "fq": 26
  },
  "bathroom": {
    "dict": "anew", "word": "bathroom", "stem": "bathroom",
    "avg": [ 5.55, 3.88 ], "std": [ 1.36, 1.72 ], "fq": 18
  },
  "bathtub": {
    "dict": "anew", "word": "bathtub", "stem": "bathtub",
    "avg": [ 6.69, 4.36 ], "std": [ 1.57, 2.59 ], "fq": 4
  },
  "beach": {
    "dict": "anew", "word": "beach", "stem": "beach",
    "avg": [ 8.03, 5.53 ], "std": [ 1.59, 3.07 ], "fq": 61
  },
  "beast": {
    "dict": "anew", "word": "beast", "stem": "beast",
    "avg": [ 4.23, 5.57 ], "std": [ 2.41, 2.61 ], "fq": 7
  },
  "beauti": {
    "dict": "anew", "word": "beautiful", "stem": "beauti",
    "avg": [ 7.60, 6.17 ], "std": [ 1.64, 2.34 ], "fq": 127
  },
  "beauti": {
    "dict": "anew", "word": "beauty", "stem": "beauti",
    "avg": [ 7.82, 4.95 ], "std": [ 1.16, 2.57 ], "fq": 71
  },
  "bed": {
    "dict": "anew", "word": "bed", "stem": "bed",
    "avg": [ 7.51, 3.61 ], "std": [ 1.38, 2.56 ], "fq": 127
  },
  "bee": {
    "dict": "anew", "word": "bees", "stem": "bee",
    "avg": [ 3.20, 6.51 ], "std": [ 2.07, 2.14 ], "fq": 15
  },
  "beggar": {
    "dict": "anew", "word": "beggar", "stem": "beggar",
    "avg": [ 3.22, 4.91 ], "std": [ 2.02, 2.45 ], "fq": 2
  },
  "bench": {
    "dict": "anew", "word": "bench", "stem": "bench",
    "avg": [ 4.61, 3.59 ], "std": [ 1.40, 2.07 ], "fq": 35
  },
  "bereav": {
    "dict": "anew", "word": "bereavement", "stem": "bereav",
    "avg": [ 4.57, 4.20 ], "std": [ 1.70, 2.15 ], "fq": 4
  },
  "betray": {
    "dict": "anew", "word": "betray", "stem": "betray",
    "avg": [ 1.68, 7.24 ], "std": [ 1.02, 2.06 ], "fq": 4
  },
  "beverag": {
    "dict": "anew", "word": "beverage", "stem": "beverag",
    "avg": [ 6.83, 5.21 ], "std": [ 1.48, 2.46 ], "fq": 5
  },
  "bird": {
    "dict": "anew", "word": "bird", "stem": "bird",
    "avg": [ 7.27, 3.17 ], "std": [ 1.36, 2.23 ], "fq": 31
  },
  "birthday": {
    "dict": "anew", "word": "birthday", "stem": "birthday",
    "avg": [ 7.84, 6.68 ], "std": [ 1.92, 2.11 ], "fq": 18
  },
  "black": {
    "dict": "anew", "word": "black", "stem": "black",
    "avg": [ 5.39, 4.61 ], "std": [ 1.80, 2.24 ], "fq": 203
  },
  "blackmail": {
    "dict": "anew", "word": "blackmail", "stem": "blackmail",
    "avg": [ 2.95, 6.03 ], "std": [ 1.95, 2.70 ], "fq": 2
  },
  "bland": {
    "dict": "anew", "word": "bland", "stem": "bland",
    "avg": [ 4.10, 3.29 ], "std": [ 1.08, 1.89 ], "fq": 3
  },
  "blase": {
    "dict": "anew", "word": "blase", "stem": "blase",
    "avg": [ 4.89, 3.94 ], "std": [ 1.16, 1.76 ], "fq": 7
  },
  "blasphemi": {
    "dict": "anew", "word": "blasphemy", "stem": "blasphemi",
    "avg": [ 3.75, 4.93 ], "std": [ 2.26, 2.34 ], "fq": 4
  },
  "bless": {
    "dict": "anew", "word": "bless", "stem": "bless",
    "avg": [ 7.19, 4.05 ], "std": [ 1.69, 2.59 ], "fq": 9
  },
  "blind": {
    "dict": "anew", "word": "blind", "stem": "blind",
    "avg": [ 3.05, 4.39 ], "std": [ 1.99, 2.36 ], "fq": 47
  },
  "bliss": {
    "dict": "anew", "word": "bliss", "stem": "bliss",
    "avg": [ 6.95, 4.41 ], "std": [ 2.24, 2.95 ], "fq": 4
  },
  "blister": {
    "dict": "anew", "word": "blister", "stem": "blister",
    "avg": [ 2.88, 4.10 ], "std": [ 1.75, 2.34 ], "fq": 3
  },
  "blond": {
    "dict": "anew", "word": "blond", "stem": "blond",
    "avg": [ 6.43, 5.07 ], "std": [ 2.04, 2.70 ], "fq": 11
  },
  "bloodi": {
    "dict": "anew", "word": "bloody", "stem": "bloodi",
    "avg": [ 2.90, 6.41 ], "std": [ 1.98, 2.00 ], "fq": 8
  },
  "blossom": {
    "dict": "anew", "word": "blossom", "stem": "blossom",
    "avg": [ 7.26, 5.03 ], "std": [ 1.18, 2.65 ], "fq": 7
  },
  "blubber": {
    "dict": "anew", "word": "blubber", "stem": "blubber",
    "avg": [ 3.52, 4.57 ], "std": [ 1.99, 2.38 ], "fq": 1
  },
  "blue": {
    "dict": "anew", "word": "blue", "stem": "blue",
    "avg": [ 6.76, 4.31 ], "std": [ 1.78, 2.20 ], "fq": 143
  },
  "board": {
    "dict": "anew", "word": "board", "stem": "board",
    "avg": [ 4.82, 3.36 ], "std": [ 1.23, 2.12 ], "fq": 239
  },
  "bodi": {
    "dict": "anew", "word": "body", "stem": "bodi",
    "avg": [ 5.55, 5.52 ], "std": [ 2.37, 2.63 ], "fq": 276
  },
  "bold": {
    "dict": "anew", "word": "bold", "stem": "bold",
    "avg": [ 6.80, 5.60 ], "std": [ 1.61, 2.21 ], "fq": 21
  },
  "bomb": {
    "dict": "anew", "word": "bomb", "stem": "bomb",
    "avg": [ 2.10, 7.15 ], "std": [ 1.19, 2.40 ], "fq": 36
  },
  "book": {
    "dict": "anew", "word": "book", "stem": "book",
    "avg": [ 5.72, 4.17 ], "std": [ 1.54, 2.49 ], "fq": 193
  },
  "bore": {
    "dict": "anew", "word": "bored", "stem": "bore",
    "avg": [ 2.95, 2.83 ], "std": [ 1.35, 2.31 ], "fq": 14
  },
  "bottl": {
    "dict": "anew", "word": "bottle", "stem": "bottl",
    "avg": [ 6.15, 4.79 ], "std": [ 1.49, 2.44 ], "fq": 76
  },
  "bouquet": {
    "dict": "anew", "word": "bouquet", "stem": "bouquet",
    "avg": [ 7.02, 5.46 ], "std": [ 1.84, 2.47 ], "fq": 4
  },
  "bowl": {
    "dict": "anew", "word": "bowl", "stem": "bowl",
    "avg": [ 5.33, 3.47 ], "std": [ 1.33, 2.12 ], "fq": 23
  },
  "boxer": {
    "dict": "anew", "word": "boxer", "stem": "boxer",
    "avg": [ 5.51, 5.12 ], "std": [ 1.80, 2.26 ], "fq": 1
  },
  "boy": {
    "dict": "anew", "word": "boy", "stem": "boy",
    "avg": [ 6.32, 4.58 ], "std": [ 1.60, 2.37 ], "fq": 242
  },
  "brave": {
    "dict": "anew", "word": "brave", "stem": "brave",
    "avg": [ 7.15, 6.15 ], "std": [ 1.64, 2.45 ], "fq": 24
  },
  "breast": {
    "dict": "anew", "word": "breast", "stem": "breast",
    "avg": [ 6.50, 5.37 ], "std": [ 1.78, 2.39 ], "fq": 11
  },
  "breez": {
    "dict": "anew", "word": "breeze", "stem": "breez",
    "avg": [ 6.85, 4.37 ], "std": [ 1.71, 2.32 ], "fq": 14
  },
  "bride": {
    "dict": "anew", "word": "bride", "stem": "bride",
    "avg": [ 7.34, 5.55 ], "std": [ 1.71, 2.74 ], "fq": 33
  },
  "bright": {
    "dict": "anew", "word": "bright", "stem": "bright",
    "avg": [ 7.50, 5.40 ], "std": [ 1.55, 2.33 ], "fq": 87
  },
  "broken": {
    "dict": "anew", "word": "broken", "stem": "broken",
    "avg": [ 3.05, 5.43 ], "std": [ 1.92, 2.42 ], "fq": 63
  },
  "brother": {
    "dict": "anew", "word": "brother", "stem": "brother",
    "avg": [ 7.11, 4.71 ], "std": [ 2.17, 2.68 ], "fq": 73
  },
  "brutal": {
    "dict": "anew", "word": "brutal", "stem": "brutal",
    "avg": [ 2.80, 6.60 ], "std": [ 1.90, 2.36 ], "fq": 7
  },
  "build": {
    "dict": "anew", "word": "building", "stem": "build",
    "avg": [ 5.29, 3.92 ], "std": [ 1.15, 1.94 ], "fq": 160
  },
  "bullet": {
    "dict": "anew", "word": "bullet", "stem": "bullet",
    "avg": [ 3.29, 5.33 ], "std": [ 2.06, 2.48 ], "fq": 28
  },
  "bunni": {
    "dict": "anew", "word": "bunny", "stem": "bunni",
    "avg": [ 7.24, 4.06 ], "std": [ 1.32, 2.61 ], "fq": 1
  },
  "burden": {
    "dict": "anew", "word": "burdened", "stem": "burden",
    "avg": [ 2.50, 5.63 ], "std": [ 1.32, 2.07 ], "fq": 4
  },
  "burial": {
    "dict": "anew", "word": "burial", "stem": "burial",
    "avg": [ 2.05, 5.08 ], "std": [ 1.41, 2.40 ], "fq": 11
  },
  "burn": {
    "dict": "anew", "word": "burn", "stem": "burn",
    "avg": [ 2.73, 6.22 ], "std": [ 1.72, 1.91 ], "fq": 15
  },
  "bus": {
    "dict": "anew", "word": "bus", "stem": "bus",
    "avg": [ 4.51, 3.55 ], "std": [ 1.57, 1.80 ], "fq": 34
  },
  "busybodi": {
    "dict": "anew", "word": "busybody", "stem": "busybodi",
    "avg": [ 5.17, 4.84 ], "std": [ 2.02, 2.41 ], "fq": 0
  },
  "butter": {
    "dict": "anew", "word": "butter", "stem": "butter",
    "avg": [ 5.33, 3.17 ], "std": [ 1.20, 1.84 ], "fq": 27
  },
  "butterfli": {
    "dict": "anew", "word": "butterfly", "stem": "butterfli",
    "avg": [ 7.17, 3.47 ], "std": [ 1.20, 2.39 ], "fq": 2
  },
  "cabinet": {
    "dict": "anew", "word": "cabinet", "stem": "cabinet",
    "avg": [ 5.05, 3.43 ], "std": [ 0.31, 1.85 ], "fq": 17
  },
  "cake": {
    "dict": "anew", "word": "cake", "stem": "cake",
    "avg": [ 7.26, 5.00 ], "std": [ 1.27, 2.37 ], "fq": 9
  },
  "cancer": {
    "dict": "anew", "word": "cancer", "stem": "cancer",
    "avg": [ 1.50, 6.42 ], "std": [ 0.85, 2.83 ], "fq": 25
  },
  "candi": {
    "dict": "anew", "word": "candy", "stem": "candi",
    "avg": [ 6.54, 4.58 ], "std": [ 2.09, 2.40 ], "fq": 16
  },
  "cane": {
    "dict": "anew", "word": "cane", "stem": "cane",
    "avg": [ 4.00, 4.20 ], "std": [ 1.80, 1.93 ], "fq": 12
  },
  "cannon": {
    "dict": "anew", "word": "cannon", "stem": "cannon",
    "avg": [ 4.90, 4.71 ], "std": [ 2.20, 2.84 ], "fq": 7
  },
  "capabl": {
    "dict": "anew", "word": "capable", "stem": "capabl",
    "avg": [ 7.16, 5.08 ], "std": [ 1.39, 2.07 ], "fq": 66
  },
  "car": {
    "dict": "anew", "word": "car", "stem": "car",
    "avg": [ 7.73, 6.24 ], "std": [ 1.63, 2.04 ], "fq": 274
  },
  "carcass": {
    "dict": "anew", "word": "carcass", "stem": "carcass",
    "avg": [ 3.34, 4.83 ], "std": [ 1.92, 2.07 ], "fq": 7
  },
  "carefre": {
    "dict": "anew", "word": "carefree", "stem": "carefre",
    "avg": [ 7.54, 4.17 ], "std": [ 1.38, 2.84 ], "fq": 9
  },
  "caress": {
    "dict": "anew", "word": "caress", "stem": "caress",
    "avg": [ 7.84, 5.14 ], "std": [ 1.16, 3.00 ], "fq": 1
  },
  "cash": {
    "dict": "anew", "word": "cash", "stem": "cash",
    "avg": [ 8.37, 7.37 ], "std": [ 1.00, 2.21 ], "fq": 36
  },
  "casino": {
    "dict": "anew", "word": "casino", "stem": "casino",
    "avg": [ 6.81, 6.51 ], "std": [ 1.66, 2.12 ], "fq": 2
  },
  "cat": {
    "dict": "anew", "word": "cat", "stem": "cat",
    "avg": [ 5.72, 4.38 ], "std": [ 2.43, 2.24 ], "fq": 0
  },
  "cell": {
    "dict": "anew", "word": "cell", "stem": "cell",
    "avg": [ 3.82, 4.08 ], "std": [ 1.70, 2.19 ], "fq": 65
  },
  "cellar": {
    "dict": "anew", "word": "cellar", "stem": "cellar",
    "avg": [ 4.32, 4.39 ], "std": [ 1.68, 2.33 ], "fq": 26
  },
  "cemeteri": {
    "dict": "anew", "word": "cemetery", "stem": "cemeteri",
    "avg": [ 2.63, 4.82 ], "std": [ 1.40, 2.66 ], "fq": 15
  },
  "chair": {
    "dict": "anew", "word": "chair", "stem": "chair",
    "avg": [ 5.08, 3.15 ], "std": [ 0.98, 1.77 ], "fq": 66
  },
  "champ": {
    "dict": "anew", "word": "champ", "stem": "champ",
    "avg": [ 7.18, 6.00 ], "std": [ 1.97, 2.43 ], "fq": 1
  },
  "champion": {
    "dict": "anew", "word": "champion", "stem": "champion",
    "avg": [ 8.44, 5.85 ], "std": [ 0.90, 3.15 ], "fq": 23
  },
  "chanc": {
    "dict": "anew", "word": "chance", "stem": "chanc",
    "avg": [ 6.02, 5.38 ], "std": [ 1.77, 2.58 ], "fq": 131
  },
  "chao": {
    "dict": "anew", "word": "chaos", "stem": "chao",
    "avg": [ 4.17, 6.67 ], "std": [ 2.36, 2.06 ], "fq": 17
  },
  "charm": {
    "dict": "anew", "word": "charm", "stem": "charm",
    "avg": [ 6.77, 5.16 ], "std": [ 1.58, 2.25 ], "fq": 26
  },
  "cheer": {
    "dict": "anew", "word": "cheer", "stem": "cheer",
    "avg": [ 8.10, 6.12 ], "std": [ 1.17, 2.45 ], "fq": 8
  },
  "child": {
    "dict": "anew", "word": "child", "stem": "child",
    "avg": [ 7.08, 5.55 ], "std": [ 1.98, 2.29 ], "fq": 213
  },
  "chin": {
    "dict": "anew", "word": "chin", "stem": "chin",
    "avg": [ 5.29, 3.31 ], "std": [ 1.27, 1.98 ], "fq": 27
  },
  "chocol": {
    "dict": "anew", "word": "chocolate", "stem": "chocol",
    "avg": [ 6.88, 5.29 ], "std": [ 1.89, 2.55 ], "fq": 9
  },
  "christma": {
    "dict": "anew", "word": "christmas", "stem": "christma",
    "avg": [ 7.80, 6.27 ], "std": [ 1.55, 2.56 ], "fq": 27
  },
  "church": {
    "dict": "anew", "word": "church", "stem": "church",
    "avg": [ 6.28, 4.34 ], "std": [ 2.31, 2.45 ], "fq": 348
  },
  "circl": {
    "dict": "anew", "word": "circle", "stem": "circl",
    "avg": [ 5.67, 3.86 ], "std": [ 1.26, 2.13 ], "fq": 60
  },
  "circus": {
    "dict": "anew", "word": "circus", "stem": "circus",
    "avg": [ 7.30, 5.97 ], "std": [ 1.84, 2.59 ], "fq": 7
  },
  "citi": {
    "dict": "anew", "word": "city", "stem": "citi",
    "avg": [ 6.03, 5.24 ], "std": [ 1.37, 2.53 ], "fq": 393
  },
  "cliff": {
    "dict": "anew", "word": "cliff", "stem": "cliff",
    "avg": [ 4.67, 6.25 ], "std": [ 2.08, 2.15 ], "fq": 11
  },
  "clock": {
    "dict": "anew", "word": "clock", "stem": "clock",
    "avg": [ 5.14, 4.02 ], "std": [ 1.54, 2.54 ], "fq": 20
  },
  "cloth": {
    "dict": "anew", "word": "clothing", "stem": "cloth",
    "avg": [ 6.54, 4.78 ], "std": [ 1.85, 2.88 ], "fq": 20
  },
  "cloud": {
    "dict": "anew", "word": "clouds", "stem": "cloud",
    "avg": [ 6.18, 3.30 ], "std": [ 2.18, 2.08 ], "fq": 38
  },
  "clumsi": {
    "dict": "anew", "word": "clumsy", "stem": "clumsi",
    "avg": [ 4.00, 5.18 ], "std": [ 2.22, 2.40 ], "fq": 6
  },
  "coars": {
    "dict": "anew", "word": "coarse", "stem": "coars",
    "avg": [ 4.55, 4.21 ], "std": [ 1.42, 1.84 ], "fq": 10
  },
  "coast": {
    "dict": "anew", "word": "coast", "stem": "coast",
    "avg": [ 5.98, 4.59 ], "std": [ 1.86, 2.31 ], "fq": 61
  },
  "cockroach": {
    "dict": "anew", "word": "cockroach", "stem": "cockroach",
    "avg": [ 2.81, 6.11 ], "std": [ 2.11, 2.78 ], "fq": 2
  },
  "coffin": {
    "dict": "anew", "word": "coffin", "stem": "coffin",
    "avg": [ 2.56, 5.03 ], "std": [ 1.96, 2.79 ], "fq": 7
  },
  "coin": {
    "dict": "anew", "word": "coin", "stem": "coin",
    "avg": [ 6.02, 4.29 ], "std": [ 1.96, 2.48 ], "fq": 10
  },
  "cold": {
    "dict": "anew", "word": "cold", "stem": "cold",
    "avg": [ 4.02, 5.19 ], "std": [ 1.99, 2.23 ], "fq": 171
  },
  "color": {
    "dict": "anew", "word": "color", "stem": "color",
    "avg": [ 7.02, 4.73 ], "std": [ 1.57, 2.64 ], "fq": 141
  },
  "column": {
    "dict": "anew", "word": "column", "stem": "column",
    "avg": [ 5.17, 3.62 ], "std": [ 0.85, 1.91 ], "fq": 71
  },
  "comedi": {
    "dict": "anew", "word": "comedy", "stem": "comedi",
    "avg": [ 8.37, 5.85 ], "std": [ 0.94, 2.81 ], "fq": 39
  },
  "comfort": {
    "dict": "anew", "word": "comfort", "stem": "comfort",
    "avg": [ 7.07, 3.93 ], "std": [ 2.14, 2.85 ], "fq": 43
  },
  "comput": {
    "dict": "anew", "word": "computer", "stem": "comput",
    "avg": [ 6.24, 4.75 ], "std": [ 1.61, 1.93 ], "fq": 13
  },
  "concentr": {
    "dict": "anew", "word": "concentrate", "stem": "concentr",
    "avg": [ 5.20, 4.65 ], "std": [ 1.28, 2.13 ], "fq": 11
  },
  "confid": {
    "dict": "anew", "word": "confident", "stem": "confid",
    "avg": [ 7.98, 6.22 ], "std": [ 1.29, 2.41 ], "fq": 16
  },
  "confus": {
    "dict": "anew", "word": "confused", "stem": "confus",
    "avg": [ 3.21, 6.03 ], "std": [ 1.51, 1.88 ], "fq": 44
  },
  "consol": {
    "dict": "anew", "word": "consoled", "stem": "consol",
    "avg": [ 5.78, 4.53 ], "std": [ 1.64, 2.22 ], "fq": 2
  },
  "contempt": {
    "dict": "anew", "word": "contempt", "stem": "contempt",
    "avg": [ 3.85, 5.28 ], "std": [ 2.13, 2.04 ], "fq": 15
  },
  "content": {
    "dict": "anew", "word": "contents", "stem": "content",
    "avg": [ 4.89, 4.32 ], "std": [ 0.89, 2.14 ], "fq": 16
  },
  "context": {
    "dict": "anew", "word": "context", "stem": "context",
    "avg": [ 5.20, 4.22 ], "std": [ 1.38, 2.24 ], "fq": 2
  },
  "control": {
    "dict": "anew", "word": "controlling", "stem": "control",
    "avg": [ 3.80, 6.10 ], "std": [ 2.25, 2.19 ], "fq": 23
  },
  "cook": {
    "dict": "anew", "word": "cook", "stem": "cook",
    "avg": [ 6.16, 4.44 ], "std": [ 1.89, 1.96 ], "fq": 47
  },
  "cord": {
    "dict": "anew", "word": "cord", "stem": "cord",
    "avg": [ 5.10, 3.54 ], "std": [ 1.09, 2.09 ], "fq": 6
  },
  "cork": {
    "dict": "anew", "word": "cork", "stem": "cork",
    "avg": [ 5.22, 3.80 ], "std": [ 1.13, 2.18 ], "fq": 9
  },
  "corner": {
    "dict": "anew", "word": "corner", "stem": "corner",
    "avg": [ 4.36, 3.91 ], "std": [ 1.21, 1.92 ], "fq": 115
  },
  "corps": {
    "dict": "anew", "word": "corpse", "stem": "corps",
    "avg": [ 2.18, 4.74 ], "std": [ 1.48, 2.94 ], "fq": 7
  },
  "corridor": {
    "dict": "anew", "word": "corridor", "stem": "corridor",
    "avg": [ 4.88, 3.63 ], "std": [ 1.14, 2.41 ], "fq": 17
  },
  "corrupt": {
    "dict": "anew", "word": "corrupt", "stem": "corrupt",
    "avg": [ 3.32, 4.67 ], "std": [ 2.32, 2.35 ], "fq": 8
  },
  "cottag": {
    "dict": "anew", "word": "cottage", "stem": "cottag",
    "avg": [ 6.45, 3.39 ], "std": [ 1.52, 2.54 ], "fq": 19
  },
  "coupl": {
    "dict": "anew", "word": "couple", "stem": "coupl",
    "avg": [ 7.41, 6.39 ], "std": [ 1.97, 2.31 ], "fq": 122
  },
  "cow": {
    "dict": "anew", "word": "cow", "stem": "cow",
    "avg": [ 5.57, 3.49 ], "std": [ 1.53, 2.13 ], "fq": 29
  },
  "coward": {
    "dict": "anew", "word": "coward", "stem": "coward",
    "avg": [ 2.74, 4.07 ], "std": [ 1.64, 2.19 ], "fq": 8
  },
  "cozi": {
    "dict": "anew", "word": "cozy", "stem": "cozi",
    "avg": [ 7.39, 3.32 ], "std": [ 1.53, 2.28 ], "fq": 1
  },
  "crash": {
    "dict": "anew", "word": "crash", "stem": "crash",
    "avg": [ 2.31, 6.95 ], "std": [ 1.44, 2.44 ], "fq": 20
  },
  "crime": {
    "dict": "anew", "word": "crime", "stem": "crime",
    "avg": [ 2.89, 5.41 ], "std": [ 2.06, 2.69 ], "fq": 34
  },
  "crimin": {
    "dict": "anew", "word": "criminal", "stem": "crimin",
    "avg": [ 2.93, 4.79 ], "std": [ 1.66, 2.51 ], "fq": 24
  },
  "crisi": {
    "dict": "anew", "word": "crisis", "stem": "crisi",
    "avg": [ 2.74, 5.44 ], "std": [ 2.23, 3.07 ], "fq": 82
  },
  "crown": {
    "dict": "anew", "word": "crown", "stem": "crown",
    "avg": [ 6.58, 4.28 ], "std": [ 1.42, 2.53 ], "fq": 19
  },
  "crucifi": {
    "dict": "anew", "word": "crucify", "stem": "crucifi",
    "avg": [ 2.23, 6.47 ], "std": [ 1.72, 2.47 ], "fq": 2
  },
  "crude": {
    "dict": "anew", "word": "crude", "stem": "crude",
    "avg": [ 3.12, 5.07 ], "std": [ 1.65, 2.37 ], "fq": 15
  },
  "cruel": {
    "dict": "anew", "word": "cruel", "stem": "cruel",
    "avg": [ 1.97, 5.68 ], "std": [ 1.67, 2.65 ], "fq": 15
  },
  "crush": {
    "dict": "anew", "word": "crushed", "stem": "crush",
    "avg": [ 2.21, 5.52 ], "std": [ 1.74, 2.87 ], "fq": 10
  },
  "crutch": {
    "dict": "anew", "word": "crutch", "stem": "crutch",
    "avg": [ 3.43, 4.14 ], "std": [ 1.62, 2.05 ], "fq": 1
  },
  "cuddl": {
    "dict": "anew", "word": "cuddle", "stem": "cuddl",
    "avg": [ 7.72, 4.40 ], "std": [ 1.92, 2.67 ], "fq": 0
  },
  "cuisin": {
    "dict": "anew", "word": "cuisine", "stem": "cuisin",
    "avg": [ 6.64, 4.39 ], "std": [ 1.48, 1.99 ], "fq": 1
  },
  "curious": {
    "dict": "anew", "word": "curious", "stem": "curious",
    "avg": [ 6.08, 5.82 ], "std": [ 1.63, 1.64 ], "fq": 46
  },
  "curtain": {
    "dict": "anew", "word": "curtains", "stem": "curtain",
    "avg": [ 4.83, 3.67 ], "std": [ 0.83, 1.83 ], "fq": 8
  },
  "custom": {
    "dict": "anew", "word": "custom", "stem": "custom",
    "avg": [ 5.85, 4.66 ], "std": [ 1.53, 2.12 ], "fq": 14
  },
  "cut": {
    "dict": "anew", "word": "cut", "stem": "cut",
    "avg": [ 3.64, 5.00 ], "std": [ 2.08, 2.32 ], "fq": 192
  },
  "cute": {
    "dict": "anew", "word": "cute", "stem": "cute",
    "avg": [ 7.62, 5.53 ], "std": [ 1.01, 2.71 ], "fq": 5
  },
  "cyclon": {
    "dict": "anew", "word": "cyclone", "stem": "cyclon",
    "avg": [ 3.60, 6.36 ], "std": [ 2.38, 2.89 ], "fq": 0
  },
  "dagger": {
    "dict": "anew", "word": "dagger", "stem": "dagger",
    "avg": [ 3.38, 6.14 ], "std": [ 1.77, 2.64 ], "fq": 1
  },
  "damag": {
    "dict": "anew", "word": "damage", "stem": "damag",
    "avg": [ 3.05, 5.57 ], "std": [ 1.65, 2.26 ], "fq": 33
  },
  "dancer": {
    "dict": "anew", "word": "dancer", "stem": "dancer",
    "avg": [ 7.14, 6.00 ], "std": [ 1.56, 2.20 ], "fq": 31
  },
  "danger": {
    "dict": "anew", "word": "danger", "stem": "danger",
    "avg": [ 2.95, 7.32 ], "std": [ 2.22, 2.07 ], "fq": 70
  },
  "dark": {
    "dict": "anew", "word": "dark", "stem": "dark",
    "avg": [ 4.71, 4.28 ], "std": [ 2.36, 2.21 ], "fq": 185
  },
  "dawn": {
    "dict": "anew", "word": "dawn", "stem": "dawn",
    "avg": [ 6.16, 4.39 ], "std": [ 2.33, 2.81 ], "fq": 28
  },
  "daylight": {
    "dict": "anew", "word": "daylight", "stem": "daylight",
    "avg": [ 6.80, 4.77 ], "std": [ 2.17, 2.50 ], "fq": 15
  },
  "dazzl": {
    "dict": "anew", "word": "dazzle", "stem": "dazzl",
    "avg": [ 7.29, 6.33 ], "std": [ 1.09, 2.02 ], "fq": 1
  },
  "dead": {
    "dict": "anew", "word": "dead", "stem": "dead",
    "avg": [ 1.94, 5.73 ], "std": [ 1.76, 2.73 ], "fq": 174
  },
  "death": {
    "dict": "anew", "word": "death", "stem": "death",
    "avg": [ 1.61, 4.59 ], "std": [ 1.40, 3.07 ], "fq": 277
  },
  "debt": {
    "dict": "anew", "word": "debt", "stem": "debt",
    "avg": [ 2.22, 5.68 ], "std": [ 1.17, 2.74 ], "fq": 13
  },
  "deceit": {
    "dict": "anew", "word": "deceit", "stem": "deceit",
    "avg": [ 2.90, 5.68 ], "std": [ 1.63, 2.46 ], "fq": 2
  },
  "decompos": {
    "dict": "anew", "word": "decompose", "stem": "decompos",
    "avg": [ 3.20, 4.65 ], "std": [ 1.81, 2.39 ], "fq": 1
  },
  "decor": {
    "dict": "anew", "word": "decorate", "stem": "decor",
    "avg": [ 6.93, 5.14 ], "std": [ 1.30, 2.39 ], "fq": 2
  },
  "defeat": {
    "dict": "anew", "word": "defeated", "stem": "defeat",
    "avg": [ 2.34, 5.09 ], "std": [ 1.66, 3.00 ], "fq": 15
  },
  "defiant": {
    "dict": "anew", "word": "defiant", "stem": "defiant",
    "avg": [ 4.26, 6.10 ], "std": [ 2.12, 2.51 ], "fq": 3
  },
  "deform": {
    "dict": "anew", "word": "deformed", "stem": "deform",
    "avg": [ 2.41, 4.07 ], "std": [ 1.66, 2.34 ], "fq": 0
  },
  "delay": {
    "dict": "anew", "word": "delayed", "stem": "delay",
    "avg": [ 3.07, 5.62 ], "std": [ 1.74, 2.39 ], "fq": 25
  },
  "delight": {
    "dict": "anew", "word": "delight", "stem": "delight",
    "avg": [ 8.26, 5.44 ], "std": [ 1.04, 2.88 ], "fq": 29
  },
  "demon": {
    "dict": "anew", "word": "demon", "stem": "demon",
    "avg": [ 2.11, 6.76 ], "std": [ 1.56, 2.68 ], "fq": 9
  },
  "dentist": {
    "dict": "anew", "word": "dentist", "stem": "dentist",
    "avg": [ 4.02, 5.73 ], "std": [ 2.23, 2.13 ], "fq": 12
  },
  "depress": {
    "dict": "anew", "word": "depressed", "stem": "depress",
    "avg": [ 1.83, 4.72 ], "std": [ 1.42, 2.95 ], "fq": 11
  },
  "depress": {
    "dict": "anew", "word": "depression", "stem": "depress",
    "avg": [ 1.85, 4.54 ], "std": [ 1.67, 3.19 ], "fq": 24
  },
  "derelict": {
    "dict": "anew", "word": "derelict", "stem": "derelict",
    "avg": [ 4.28, 4.10 ], "std": [ 1.84, 1.94 ], "fq": 1
  },
  "desert": {
    "dict": "anew", "word": "deserter", "stem": "desert",
    "avg": [ 2.45, 5.50 ], "std": [ 1.80, 2.55 ], "fq": 0
  },
  "desir": {
    "dict": "anew", "word": "desire", "stem": "desir",
    "avg": [ 7.69, 7.35 ], "std": [ 1.39, 1.76 ], "fq": 79
  },
  "despair": {
    "dict": "anew", "word": "despairing", "stem": "despair",
    "avg": [ 2.43, 5.68 ], "std": [ 1.47, 2.37 ], "fq": 4
  },
  "despis": {
    "dict": "anew", "word": "despise", "stem": "despis",
    "avg": [ 2.03, 6.28 ], "std": [ 1.38, 2.43 ], "fq": 7
  },
  "destroy": {
    "dict": "anew", "word": "destroy", "stem": "destroy",
    "avg": [ 2.64, 6.83 ], "std": [ 2.03, 2.38 ], "fq": 48
  },
  "destruct": {
    "dict": "anew", "word": "destruction", "stem": "destruct",
    "avg": [ 3.16, 5.82 ], "std": [ 2.44, 2.71 ], "fq": 38
  },
  "detach": {
    "dict": "anew", "word": "detached", "stem": "detach",
    "avg": [ 3.86, 4.26 ], "std": [ 1.88, 2.57 ], "fq": 12
  },
  "detail": {
    "dict": "anew", "word": "detail", "stem": "detail",
    "avg": [ 5.55, 4.10 ], "std": [ 1.58, 2.24 ], "fq": 72
  },
  "detest": {
    "dict": "anew", "word": "detest", "stem": "detest",
    "avg": [ 2.17, 6.06 ], "std": [ 1.30, 2.39 ], "fq": 1
  },
  "devil": {
    "dict": "anew", "word": "devil", "stem": "devil",
    "avg": [ 2.21, 6.07 ], "std": [ 1.99, 2.61 ], "fq": 25
  },
  "devot": {
    "dict": "anew", "word": "devoted", "stem": "devot",
    "avg": [ 7.41, 5.23 ], "std": [ 1.37, 2.21 ], "fq": 51
  },
  "diamond": {
    "dict": "anew", "word": "diamond", "stem": "diamond",
    "avg": [ 7.92, 5.53 ], "std": [ 1.20, 2.96 ], "fq": 8
  },
  "dignifi": {
    "dict": "anew", "word": "dignified", "stem": "dignifi",
    "avg": [ 7.10, 4.12 ], "std": [ 1.26, 2.29 ], "fq": 7
  },
  "dinner": {
    "dict": "anew", "word": "dinner", "stem": "dinner",
    "avg": [ 7.16, 5.43 ], "std": [ 1.50, 2.14 ], "fq": 91
  },
  "diploma": {
    "dict": "anew", "word": "diploma", "stem": "diploma",
    "avg": [ 8.00, 5.67 ], "std": [ 1.39, 2.80 ], "fq": 0
  },
  "dirt": {
    "dict": "anew", "word": "dirt", "stem": "dirt",
    "avg": [ 4.17, 3.76 ], "std": [ 1.77, 2.26 ], "fq": 43
  },
  "dirti": {
    "dict": "anew", "word": "dirty", "stem": "dirti",
    "avg": [ 3.08, 4.88 ], "std": [ 2.05, 2.29 ], "fq": 36
  },
  "disappoint": {
    "dict": "anew", "word": "disappoint", "stem": "disappoint",
    "avg": [ 2.39, 4.92 ], "std": [ 1.44, 2.64 ], "fq": 0
  },
  "disast": {
    "dict": "anew", "word": "disaster", "stem": "disast",
    "avg": [ 1.73, 6.33 ], "std": [ 1.13, 2.70 ], "fq": 26
  },
  "discomfort": {
    "dict": "anew", "word": "discomfort", "stem": "discomfort",
    "avg": [ 2.19, 4.17 ], "std": [ 1.23, 2.44 ], "fq": 7
  },
  "discourag": {
    "dict": "anew", "word": "discouraged", "stem": "discourag",
    "avg": [ 3.00, 4.53 ], "std": [ 2.16, 2.11 ], "fq": 15
  },
  "disdain": {
    "dict": "anew", "word": "disdainful", "stem": "disdain",
    "avg": [ 3.68, 5.04 ], "std": [ 1.90, 2.14 ], "fq": 2
  },
  "disgust": {
    "dict": "anew", "word": "disgusted", "stem": "disgust",
    "avg": [ 2.45, 5.42 ], "std": [ 1.41, 2.59 ], "fq": 6
  },
  "disloy": {
    "dict": "anew", "word": "disloyal", "stem": "disloy",
    "avg": [ 1.93, 6.56 ], "std": [ 1.61, 2.21 ], "fq": 2
  },
  "displeas": {
    "dict": "anew", "word": "displeased", "stem": "displeas",
    "avg": [ 2.79, 5.64 ], "std": [ 2.23, 2.48 ], "fq": 7
  },
  "distress": {
    "dict": "anew", "word": "distressed", "stem": "distress",
    "avg": [ 1.94, 6.40 ], "std": [ 1.10, 2.38 ], "fq": 4
  },
  "disturb": {
    "dict": "anew", "word": "disturb", "stem": "disturb",
    "avg": [ 3.66, 5.80 ], "std": [ 2.00, 2.39 ], "fq": 10
  },
  "diver": {
    "dict": "anew", "word": "diver", "stem": "diver",
    "avg": [ 6.45, 5.04 ], "std": [ 1.55, 2.10 ], "fq": 1
  },
  "divorc": {
    "dict": "anew", "word": "divorce", "stem": "divorc",
    "avg": [ 2.22, 6.33 ], "std": [ 1.88, 2.71 ], "fq": 29
  },
  "doctor": {
    "dict": "anew", "word": "doctor", "stem": "doctor",
    "avg": [ 5.20, 5.86 ], "std": [ 2.54, 2.70 ], "fq": 100
  },
  "dog": {
    "dict": "anew", "word": "dog", "stem": "dog",
    "avg": [ 7.57, 5.76 ], "std": [ 1.66, 2.50 ], "fq": 75
  },
  "doll": {
    "dict": "anew", "word": "doll", "stem": "doll",
    "avg": [ 6.09, 4.24 ], "std": [ 1.96, 2.43 ], "fq": 10
  },
  "dollar": {
    "dict": "anew", "word": "dollar", "stem": "dollar",
    "avg": [ 7.47, 6.07 ], "std": [ 1.72, 2.67 ], "fq": 46
  },
  "door": {
    "dict": "anew", "word": "door", "stem": "door",
    "avg": [ 5.13, 3.80 ], "std": [ 1.44, 2.29 ], "fq": 312
  },
  "dove": {
    "dict": "anew", "word": "dove", "stem": "dove",
    "avg": [ 6.90, 3.79 ], "std": [ 1.54, 2.28 ], "fq": 4
  },
  "dread": {
    "dict": "anew", "word": "dreadful", "stem": "dread",
    "avg": [ 2.26, 5.84 ], "std": [ 1.91, 2.62 ], "fq": 10
  },
  "dream": {
    "dict": "anew", "word": "dream", "stem": "dream",
    "avg": [ 6.73, 4.53 ], "std": [ 1.75, 2.72 ], "fq": 64
  },
  "dreari": {
    "dict": "anew", "word": "dreary", "stem": "dreari",
    "avg": [ 3.05, 2.98 ], "std": [ 1.58, 2.18 ], "fq": 6
  },
  "dress": {
    "dict": "anew", "word": "dress", "stem": "dress",
    "avg": [ 6.41, 4.05 ], "std": [ 1.34, 1.89 ], "fq": 67
  },
  "drown": {
    "dict": "anew", "word": "drown", "stem": "drown",
    "avg": [ 1.92, 6.57 ], "std": [ 1.48, 2.33 ], "fq": 3
  },
  "dummi": {
    "dict": "anew", "word": "dummy", "stem": "dummi",
    "avg": [ 3.38, 4.35 ], "std": [ 1.70, 2.25 ], "fq": 3
  },
  "dump": {
    "dict": "anew", "word": "dump", "stem": "dump",
    "avg": [ 3.21, 4.12 ], "std": [ 1.87, 2.36 ], "fq": 4
  },
  "dustpan": {
    "dict": "anew", "word": "dustpan", "stem": "dustpan",
    "avg": [ 3.98, 3.43 ], "std": [ 1.68, 2.00 ], "fq": 0
  },
  "earth": {
    "dict": "anew", "word": "earth", "stem": "earth",
    "avg": [ 7.15, 4.24 ], "std": [ 1.67, 2.49 ], "fq": 150
  },
  "easi": {
    "dict": "anew", "word": "easy", "stem": "easi",
    "avg": [ 7.10, 4.48 ], "std": [ 1.91, 2.82 ], "fq": 125
  },
  "easygo": {
    "dict": "anew", "word": "easygoing", "stem": "easygo",
    "avg": [ 7.20, 4.30 ], "std": [ 1.50, 2.52 ], "fq": 1
  },
  "eat": {
    "dict": "anew", "word": "eat", "stem": "eat",
    "avg": [ 7.47, 5.69 ], "std": [ 1.73, 2.51 ], "fq": 61
  },
  "ecstasi": {
    "dict": "anew", "word": "ecstasy", "stem": "ecstasi",
    "avg": [ 7.98, 7.38 ], "std": [ 1.52, 1.92 ], "fq": 6
  },
  "educ": {
    "dict": "anew", "word": "education", "stem": "educ",
    "avg": [ 6.69, 5.74 ], "std": [ 1.77, 2.46 ], "fq": 214
  },
  "egg": {
    "dict": "anew", "word": "egg", "stem": "egg",
    "avg": [ 5.29, 3.76 ], "std": [ 1.82, 2.39 ], "fq": 12
  },
  "elat": {
    "dict": "anew", "word": "elated", "stem": "elat",
    "avg": [ 7.45, 6.21 ], "std": [ 1.77, 2.30 ], "fq": 3
  },
  "elbow": {
    "dict": "anew", "word": "elbow", "stem": "elbow",
    "avg": [ 5.12, 3.81 ], "std": [ 0.92, 2.14 ], "fq": 10
  },
  "eleg": {
    "dict": "anew", "word": "elegant", "stem": "eleg",
    "avg": [ 7.43, 4.53 ], "std": [ 1.26, 2.65 ], "fq": 14
  },
  "elev": {
    "dict": "anew", "word": "elevator", "stem": "elev",
    "avg": [ 5.44, 4.16 ], "std": [ 1.18, 1.99 ], "fq": 12
  },
  "embarrass": {
    "dict": "anew", "word": "embarrassed", "stem": "embarrass",
    "avg": [ 3.03, 5.87 ], "std": [ 1.85, 2.55 ], "fq": 8
  },
  "embattl": {
    "dict": "anew", "word": "embattled", "stem": "embattl",
    "avg": [ 4.39, 5.36 ], "std": [ 1.63, 2.37 ], "fq": 1
  },
  "employ": {
    "dict": "anew", "word": "employment", "stem": "employ",
    "avg": [ 6.47, 5.28 ], "std": [ 1.81, 2.12 ], "fq": 47
  },
  "engag": {
    "dict": "anew", "word": "engaged", "stem": "engag",
    "avg": [ 8.00, 6.77 ], "std": [ 1.38, 2.07 ], "fq": 47
  },
  "engin": {
    "dict": "anew", "word": "engine", "stem": "engin",
    "avg": [ 5.20, 3.98 ], "std": [ 1.18, 2.33 ], "fq": 50
  },
  "enjoy": {
    "dict": "anew", "word": "enjoyment", "stem": "enjoy",
    "avg": [ 7.80, 5.20 ], "std": [ 1.20, 2.72 ], "fq": 21
  },
  "ennui": {
    "dict": "anew", "word": "ennui", "stem": "ennui",
    "avg": [ 5.09, 4.40 ], "std": [ 1.76, 2.33 ], "fq": 0
  },
  "enrag": {
    "dict": "anew", "word": "enraged", "stem": "enrag",
    "avg": [ 2.46, 7.97 ], "std": [ 1.65, 2.17 ], "fq": 1
  },
  "erot": {
    "dict": "anew", "word": "erotic", "stem": "erot",
    "avg": [ 7.43, 7.24 ], "std": [ 1.53, 1.97 ], "fq": 8
  },
  "errand": {
    "dict": "anew", "word": "errand", "stem": "errand",
    "avg": [ 4.58, 3.85 ], "std": [ 1.74, 1.92 ], "fq": 7
  },
  "event": {
    "dict": "anew", "word": "event", "stem": "event",
    "avg": [ 6.21, 5.10 ], "std": [ 1.63, 2.40 ], "fq": 81
  },
  "evil": {
    "dict": "anew", "word": "evil", "stem": "evil",
    "avg": [ 3.23, 6.39 ], "std": [ 2.64, 2.44 ], "fq": 72
  },
  "excel": {
    "dict": "anew", "word": "excellence", "stem": "excel",
    "avg": [ 8.38, 5.54 ], "std": [ 0.96, 2.67 ], "fq": 15
  },
  "excit": {
    "dict": "anew", "word": "excitement", "stem": "excit",
    "avg": [ 7.50, 7.67 ], "std": [ 2.20, 1.91 ], "fq": 32
  },
  "excus": {
    "dict": "anew", "word": "excuse", "stem": "excus",
    "avg": [ 4.05, 4.48 ], "std": [ 1.41, 2.29 ], "fq": 27
  },
  "execut": {
    "dict": "anew", "word": "execution", "stem": "execut",
    "avg": [ 2.37, 5.71 ], "std": [ 2.06, 2.74 ], "fq": 15
  },
  "exercis": {
    "dict": "anew", "word": "exercise", "stem": "exercis",
    "avg": [ 7.13, 6.84 ], "std": [ 1.58, 2.06 ], "fq": 58
  },
  "fabric": {
    "dict": "anew", "word": "fabric", "stem": "fabric",
    "avg": [ 5.30, 4.14 ], "std": [ 1.20, 1.98 ], "fq": 15
  },
  "face": {
    "dict": "anew", "word": "face", "stem": "face",
    "avg": [ 6.39, 5.04 ], "std": [ 1.60, 2.18 ], "fq": 371
  },
  "failur": {
    "dict": "anew", "word": "failure", "stem": "failur",
    "avg": [ 1.70, 4.95 ], "std": [ 1.07, 2.81 ], "fq": 89
  },
  "fall": {
    "dict": "anew", "word": "fall", "stem": "fall",
    "avg": [ 4.09, 4.70 ], "std": [ 2.21, 2.48 ], "fq": 147
  },
  "fals": {
    "dict": "anew", "word": "FALSE", "stem": "fals",
    "avg": [ 3.27, 3.43 ], "std": [ 1.40, 2.09 ], "fq": 29
  },
  "fame": {
    "dict": "anew", "word": "fame", "stem": "fame",
    "avg": [ 7.93, 6.55 ], "std": [ 1.29, 2.46 ], "fq": 18
  },
  "famili": {
    "dict": "anew", "word": "family", "stem": "famili",
    "avg": [ 7.65, 4.80 ], "std": [ 1.55, 2.71 ], "fq": 331
  },
  "famous": {
    "dict": "anew", "word": "famous", "stem": "famous",
    "avg": [ 6.98, 5.73 ], "std": [ 2.07, 2.68 ], "fq": 89
  },
  "fantasi": {
    "dict": "anew", "word": "fantasy", "stem": "fantasi",
    "avg": [ 7.41, 5.14 ], "std": [ 1.90, 2.82 ], "fq": 14
  },
  "farm": {
    "dict": "anew", "word": "farm", "stem": "farm",
    "avg": [ 5.53, 3.90 ], "std": [ 1.85, 1.95 ], "fq": 125
  },
  "fascin": {
    "dict": "anew", "word": "fascinate", "stem": "fascin",
    "avg": [ 7.34, 5.83 ], "std": [ 1.68, 2.73 ], "fq": 3
  },
  "fat": {
    "dict": "anew", "word": "fat", "stem": "fat",
    "avg": [ 2.28, 4.81 ], "std": [ 1.92, 2.80 ], "fq": 60
  },
  "father": {
    "dict": "anew", "word": "father", "stem": "father",
    "avg": [ 7.08, 5.92 ], "std": [ 2.20, 2.60 ], "fq": 383
  },
  "fatigu": {
    "dict": "anew", "word": "fatigued", "stem": "fatigu",
    "avg": [ 3.28, 2.64 ], "std": [ 1.43, 2.19 ], "fq": 3
  },
  "fault": {
    "dict": "anew", "word": "fault", "stem": "fault",
    "avg": [ 3.43, 4.07 ], "std": [ 1.38, 1.69 ], "fq": 22
  },
  "favor": {
    "dict": "anew", "word": "favor", "stem": "favor",
    "avg": [ 6.46, 4.54 ], "std": [ 1.52, 1.86 ], "fq": 78
  },
  "fear": {
    "dict": "anew", "word": "fear", "stem": "fear",
    "avg": [ 2.76, 6.96 ], "std": [ 2.12, 2.17 ], "fq": 127
  },
  "fear": {
    "dict": "anew", "word": "fearful", "stem": "fear",
    "avg": [ 2.25, 6.33 ], "std": [ 1.18, 2.28 ], "fq": 13
  },
  "feebl": {
    "dict": "anew", "word": "feeble", "stem": "feebl",
    "avg": [ 3.26, 4.10 ], "std": [ 1.47, 2.07 ], "fq": 8
  },
  "festiv": {
    "dict": "anew", "word": "festive", "stem": "festiv",
    "avg": [ 7.30, 6.58 ], "std": [ 2.26, 2.29 ], "fq": 2
  },
  "fever": {
    "dict": "anew", "word": "fever", "stem": "fever",
    "avg": [ 2.76, 4.29 ], "std": [ 1.64, 2.31 ], "fq": 19
  },
  "field": {
    "dict": "anew", "word": "field", "stem": "field",
    "avg": [ 6.20, 4.08 ], "std": [ 1.37, 2.41 ], "fq": 274
  },
  "fight": {
    "dict": "anew", "word": "fight", "stem": "fight",
    "avg": [ 3.76, 7.15 ], "std": [ 2.63, 2.19 ], "fq": 98
  },
  "filth": {
    "dict": "anew", "word": "filth", "stem": "filth",
    "avg": [ 2.47, 5.12 ], "std": [ 1.68, 2.32 ], "fq": 2
  },
  "finger": {
    "dict": "anew", "word": "finger", "stem": "finger",
    "avg": [ 5.29, 3.78 ], "std": [ 1.42, 2.42 ], "fq": 40
  },
  "fire": {
    "dict": "anew", "word": "fire", "stem": "fire",
    "avg": [ 3.22, 7.17 ], "std": [ 2.06, 2.06 ], "fq": 187
  },
  "firework": {
    "dict": "anew", "word": "fireworks", "stem": "firework",
    "avg": [ 7.55, 6.67 ], "std": [ 1.50, 2.12 ], "fq": 5
  },
  "fish": {
    "dict": "anew", "word": "fish", "stem": "fish",
    "avg": [ 6.04, 4.00 ], "std": [ 1.94, 2.19 ], "fq": 35
  },
  "flabbi": {
    "dict": "anew", "word": "flabby", "stem": "flabbi",
    "avg": [ 2.66, 4.82 ], "std": [ 1.87, 2.81 ], "fq": 0
  },
  "flag": {
    "dict": "anew", "word": "flag", "stem": "flag",
    "avg": [ 6.02, 4.60 ], "std": [ 1.66, 2.35 ], "fq": 16
  },
  "flirt": {
    "dict": "anew", "word": "flirt", "stem": "flirt",
    "avg": [ 7.52, 6.91 ], "std": [ 1.19, 1.69 ], "fq": 1
  },
  "flood": {
    "dict": "anew", "word": "flood", "stem": "flood",
    "avg": [ 3.19, 6.00 ], "std": [ 1.66, 2.02 ], "fq": 19
  },
  "flower": {
    "dict": "anew", "word": "flower", "stem": "flower",
    "avg": [ 6.64, 4.00 ], "std": [ 1.78, 2.44 ], "fq": 23
  },
  "foam": {
    "dict": "anew", "word": "foam", "stem": "foam",
    "avg": [ 6.07, 5.26 ], "std": [ 2.03, 2.54 ], "fq": 37
  },
  "food": {
    "dict": "anew", "word": "food", "stem": "food",
    "avg": [ 7.65, 5.92 ], "std": [ 1.37, 2.11 ], "fq": 147
  },
  "foot": {
    "dict": "anew", "word": "foot", "stem": "foot",
    "avg": [ 5.02, 3.27 ], "std": [ 0.93, 1.98 ], "fq": 70
  },
  "fork": {
    "dict": "anew", "word": "fork", "stem": "fork",
    "avg": [ 5.29, 3.96 ], "std": [ 0.97, 1.94 ], "fq": 14
  },
  "foul": {
    "dict": "anew", "word": "foul", "stem": "foul",
    "avg": [ 2.81, 4.93 ], "std": [ 1.52, 2.23 ], "fq": 4
  },
  "fragranc": {
    "dict": "anew", "word": "fragrance", "stem": "fragranc",
    "avg": [ 6.07, 4.79 ], "std": [ 1.97, 2.54 ], "fq": 6
  },
  "fraud": {
    "dict": "anew", "word": "fraud", "stem": "fraud",
    "avg": [ 2.67, 5.75 ], "std": [ 1.66, 2.45 ], "fq": 8
  },
  "free": {
    "dict": "anew", "word": "free", "stem": "free",
    "avg": [ 8.26, 5.15 ], "std": [ 1.31, 3.04 ], "fq": 260
  },
  "freedom": {
    "dict": "anew", "word": "freedom", "stem": "freedom",
    "avg": [ 7.58, 5.52 ], "std": [ 2.04, 2.72 ], "fq": 128
  },
  "friend": {
    "dict": "anew", "word": "friend", "stem": "friend",
    "avg": [ 7.74, 5.74 ], "std": [ 1.24, 2.57 ], "fq": 133
  },
  "friend": {
    "dict": "anew", "word": "friendly", "stem": "friend",
    "avg": [ 8.43, 5.11 ], "std": [ 1.08, 2.96 ], "fq": 61
  },
  "frigid": {
    "dict": "anew", "word": "frigid", "stem": "frigid",
    "avg": [ 3.50, 4.75 ], "std": [ 1.85, 2.56 ], "fq": 5
  },
  "frog": {
    "dict": "anew", "word": "frog", "stem": "frog",
    "avg": [ 5.71, 4.54 ], "std": [ 1.74, 2.03 ], "fq": 1
  },
  "frustrat": {
    "dict": "anew", "word": "frustrated", "stem": "frustrat",
    "avg": [ 2.48, 5.61 ], "std": [ 1.64, 2.76 ], "fq": 10
  },
  "fun": {
    "dict": "anew", "word": "fun", "stem": "fun",
    "avg": [ 8.37, 7.22 ], "std": [ 1.11, 2.01 ], "fq": 44
  },
  "funer": {
    "dict": "anew", "word": "funeral", "stem": "funer",
    "avg": [ 1.39, 4.94 ], "std": [ 0.87, 3.21 ], "fq": 33
  },
  "fungus": {
    "dict": "anew", "word": "fungus", "stem": "fungus",
    "avg": [ 3.06, 4.68 ], "std": [ 1.75, 2.33 ], "fq": 2
  },
  "fur": {
    "dict": "anew", "word": "fur", "stem": "fur",
    "avg": [ 4.51, 4.18 ], "std": [ 1.88, 2.44 ], "fq": 13
  },
  "game": {
    "dict": "anew", "word": "game", "stem": "game",
    "avg": [ 6.98, 5.89 ], "std": [ 1.97, 2.37 ], "fq": 123
  },
  "gangren": {
    "dict": "anew", "word": "gangrene", "stem": "gangren",
    "avg": [ 2.28, 5.70 ], "std": [ 1.91, 2.96 ], "fq": 0
  },
  "garbag": {
    "dict": "anew", "word": "garbage", "stem": "garbag",
    "avg": [ 2.98, 5.04 ], "std": [ 1.96, 2.50 ], "fq": 7
  },
  "garden": {
    "dict": "anew", "word": "garden", "stem": "garden",
    "avg": [ 6.71, 4.39 ], "std": [ 1.74, 2.35 ], "fq": 60
  },
  "garment": {
    "dict": "anew", "word": "garment", "stem": "garment",
    "avg": [ 6.07, 4.49 ], "std": [ 1.61, 2.50 ], "fq": 6
  },
  "garter": {
    "dict": "anew", "word": "garter", "stem": "garter",
    "avg": [ 6.22, 5.47 ], "std": [ 1.59, 2.15 ], "fq": 2
  },
  "gender": {
    "dict": "anew", "word": "gender", "stem": "gender",
    "avg": [ 5.73, 4.38 ], "std": [ 1.55, 2.13 ], "fq": 2
  },
  "gentl": {
    "dict": "anew", "word": "gentle", "stem": "gentl",
    "avg": [ 7.31, 3.21 ], "std": [ 1.30, 2.57 ], "fq": 27
  },
  "germ": {
    "dict": "anew", "word": "germs", "stem": "germ",
    "avg": [ 2.86, 4.49 ], "std": [ 1.39, 2.24 ], "fq": 1
  },
  "gift": {
    "dict": "anew", "word": "gift", "stem": "gift",
    "avg": [ 7.77, 6.14 ], "std": [ 2.24, 2.76 ], "fq": 33
  },
  "girl": {
    "dict": "anew", "word": "girl", "stem": "girl",
    "avg": [ 6.87, 4.29 ], "std": [ 1.64, 2.69 ], "fq": 220
  },
  "glacier": {
    "dict": "anew", "word": "glacier", "stem": "glacier",
    "avg": [ 5.50, 4.24 ], "std": [ 1.25, 2.29 ], "fq": 1
  },
  "glamour": {
    "dict": "anew", "word": "glamour", "stem": "glamour",
    "avg": [ 6.76, 4.68 ], "std": [ 1.60, 2.23 ], "fq": 5
  },
  "glass": {
    "dict": "anew", "word": "glass", "stem": "glass",
    "avg": [ 4.75, 4.27 ], "std": [ 1.38, 2.07 ], "fq": 99
  },
  "gloom": {
    "dict": "anew", "word": "gloom", "stem": "gloom",
    "avg": [ 1.88, 3.83 ], "std": [ 1.23, 2.33 ], "fq": 14
  },
  "glori": {
    "dict": "anew", "word": "glory", "stem": "glori",
    "avg": [ 7.55, 6.02 ], "std": [ 1.68, 2.71 ], "fq": 21
  },
  "god": {
    "dict": "anew", "word": "god", "stem": "god",
    "avg": [ 8.15, 5.95 ], "std": [ 1.27, 2.84 ], "fq": 318
  },
  "gold": {
    "dict": "anew", "word": "gold", "stem": "gold",
    "avg": [ 7.54, 5.76 ], "std": [ 1.63, 2.79 ], "fq": 52
  },
  "golfer": {
    "dict": "anew", "word": "golfer", "stem": "golfer",
    "avg": [ 5.61, 3.73 ], "std": [ 1.93, 2.26 ], "fq": 3
  },
  "good": {
    "dict": "anew", "word": "good", "stem": "good",
    "avg": [ 7.47, 5.43 ], "std": [ 1.45, 2.85 ], "fq": 807
  },
  "gossip": {
    "dict": "anew", "word": "gossip", "stem": "gossip",
    "avg": [ 3.48, 5.74 ], "std": [ 2.33, 2.38 ], "fq": 13
  },
  "graduat": {
    "dict": "anew", "word": "graduate", "stem": "graduat",
    "avg": [ 8.19, 7.25 ], "std": [ 1.13, 2.25 ], "fq": 30
  },
  "grass": {
    "dict": "anew", "word": "grass", "stem": "grass",
    "avg": [ 6.12, 4.14 ], "std": [ 1.44, 2.11 ], "fq": 53
  },
  "grate": {
    "dict": "anew", "word": "grateful", "stem": "grate",
    "avg": [ 7.37, 4.58 ], "std": [ 0.97, 2.14 ], "fq": 25
  },
  "greed": {
    "dict": "anew", "word": "greed", "stem": "greed",
    "avg": [ 3.51, 4.71 ], "std": [ 1.93, 2.26 ], "fq": 3
  },
  "green": {
    "dict": "anew", "word": "green", "stem": "green",
    "avg": [ 6.18, 4.28 ], "std": [ 2.05, 2.46 ], "fq": 116
  },
  "greet": {
    "dict": "anew", "word": "greet", "stem": "greet",
    "avg": [ 7.00, 5.27 ], "std": [ 1.52, 2.31 ], "fq": 7
  },
  "grenad": {
    "dict": "anew", "word": "grenade", "stem": "grenad",
    "avg": [ 3.60, 5.70 ], "std": [ 1.88, 2.52 ], "fq": 3
  },
  "grief": {
    "dict": "anew", "word": "grief", "stem": "grief",
    "avg": [ 1.69, 4.78 ], "std": [ 1.04, 2.84 ], "fq": 10
  },
  "grime": {
    "dict": "anew", "word": "grime", "stem": "grime",
    "avg": [ 3.37, 3.98 ], "std": [ 1.34, 2.29 ], "fq": 0
  },
  "gripe": {
    "dict": "anew", "word": "gripe", "stem": "gripe",
    "avg": [ 3.14, 5.00 ], "std": [ 1.56, 2.19 ], "fq": 0
  },
  "guillotin": {
    "dict": "anew", "word": "guillotine", "stem": "guillotin",
    "avg": [ 2.48, 6.56 ], "std": [ 2.11, 2.54 ], "fq": 0
  },
  "guilti": {
    "dict": "anew", "word": "guilty", "stem": "guilti",
    "avg": [ 2.63, 6.04 ], "std": [ 1.98, 2.76 ], "fq": 29
  },
  "gun": {
    "dict": "anew", "word": "gun", "stem": "gun",
    "avg": [ 3.47, 7.02 ], "std": [ 2.48, 1.84 ], "fq": 118
  },
  "gymnast": {
    "dict": "anew", "word": "gymnast", "stem": "gymnast",
    "avg": [ 6.35, 5.02 ], "std": [ 1.79, 2.20 ], "fq": 1
  },
  "habit": {
    "dict": "anew", "word": "habit", "stem": "habit",
    "avg": [ 4.11, 3.95 ], "std": [ 1.77, 2.11 ], "fq": 23
  },
  "hairdryer": {
    "dict": "anew", "word": "hairdryer", "stem": "hairdryer",
    "avg": [ 4.84, 3.71 ], "std": [ 0.84, 1.75 ], "fq": 0
  },
  "hairpin": {
    "dict": "anew", "word": "hairpin", "stem": "hairpin",
    "avg": [ 5.26, 3.27 ], "std": [ 1.45, 2.41 ], "fq": 1
  },
  "hamburg": {
    "dict": "anew", "word": "hamburger", "stem": "hamburg",
    "avg": [ 6.27, 4.55 ], "std": [ 1.50, 2.14 ], "fq": 6
  },
  "hammer": {
    "dict": "anew", "word": "hammer", "stem": "hammer",
    "avg": [ 4.88, 4.58 ], "std": [ 1.16, 2.02 ], "fq": 9
  },
  "hand": {
    "dict": "anew", "word": "hand", "stem": "hand",
    "avg": [ 5.95, 4.40 ], "std": [ 1.38, 2.07 ], "fq": 431
  },
  "handicap": {
    "dict": "anew", "word": "handicap", "stem": "handicap",
    "avg": [ 3.29, 3.81 ], "std": [ 1.69, 2.27 ], "fq": 6
  },
  "handsom": {
    "dict": "anew", "word": "handsome", "stem": "handsom",
    "avg": [ 7.93, 5.95 ], "std": [ 1.47, 2.73 ], "fq": 40
  },
  "haphazard": {
    "dict": "anew", "word": "haphazard", "stem": "haphazard",
    "avg": [ 4.02, 4.07 ], "std": [ 1.41, 2.18 ], "fq": 2
  },
  "happi": {
    "dict": "anew", "word": "happy", "stem": "happi",
    "avg": [ 8.21, 6.49 ], "std": [ 1.82, 2.77 ], "fq": 98
  },
  "hard": {
    "dict": "anew", "word": "hard", "stem": "hard",
    "avg": [ 5.22, 5.12 ], "std": [ 1.82, 2.19 ], "fq": 202
  },
  "hardship": {
    "dict": "anew", "word": "hardship", "stem": "hardship",
    "avg": [ 2.45, 4.76 ], "std": [ 1.61, 2.55 ], "fq": 9
  },
  "hat": {
    "dict": "anew", "word": "hat", "stem": "hat",
    "avg": [ 5.46, 4.10 ], "std": [ 1.36, 2.00 ], "fq": 56
  },
  "hate": {
    "dict": "anew", "word": "hate", "stem": "hate",
    "avg": [ 2.12, 6.95 ], "std": [ 1.72, 2.56 ], "fq": 42
  },
  "hatr": {
    "dict": "anew", "word": "hatred", "stem": "hatr",
    "avg": [ 1.98, 6.66 ], "std": [ 1.92, 2.56 ], "fq": 20
  },
  "hawk": {
    "dict": "anew", "word": "hawk", "stem": "hawk",
    "avg": [ 5.88, 4.39 ], "std": [ 1.62, 2.29 ], "fq": 14
  },
  "hay": {
    "dict": "anew", "word": "hay", "stem": "hay",
    "avg": [ 5.24, 3.95 ], "std": [ 1.24, 2.58 ], "fq": 19
  },
  "headach": {
    "dict": "anew", "word": "headache", "stem": "headach",
    "avg": [ 2.02, 5.07 ], "std": [ 1.06, 2.74 ], "fq": 5
  },
  "headlight": {
    "dict": "anew", "word": "headlight", "stem": "headlight",
    "avg": [ 5.24, 3.81 ], "std": [ 1.51, 2.22 ], "fq": 0
  },
  "heal": {
    "dict": "anew", "word": "heal", "stem": "heal",
    "avg": [ 7.09, 4.77 ], "std": [ 1.46, 2.23 ], "fq": 2
  },
  "health": {
    "dict": "anew", "word": "health", "stem": "health",
    "avg": [ 6.81, 5.13 ], "std": [ 1.88, 2.35 ], "fq": 105
  },
  "heart": {
    "dict": "anew", "word": "heart", "stem": "heart",
    "avg": [ 7.39, 6.34 ], "std": [ 1.53, 2.25 ], "fq": 173
  },
  "heaven": {
    "dict": "anew", "word": "heaven", "stem": "heaven",
    "avg": [ 7.30, 5.61 ], "std": [ 2.39, 3.20 ], "fq": 43
  },
  "hell": {
    "dict": "anew", "word": "hell", "stem": "hell",
    "avg": [ 2.24, 5.38 ], "std": [ 1.62, 2.62 ], "fq": 95
  },
  "helpless": {
    "dict": "anew", "word": "helpless", "stem": "helpless",
    "avg": [ 2.20, 5.34 ], "std": [ 1.42, 2.52 ], "fq": 21
  },
  "heroin": {
    "dict": "anew", "word": "heroin", "stem": "heroin",
    "avg": [ 4.36, 5.11 ], "std": [ 2.73, 2.72 ], "fq": 2
  },
  "hide": {
    "dict": "anew", "word": "hide", "stem": "hide",
    "avg": [ 4.32, 5.28 ], "std": [ 1.91, 2.51 ], "fq": 22
  },
  "highway": {
    "dict": "anew", "word": "highway", "stem": "highway",
    "avg": [ 5.92, 5.16 ], "std": [ 1.72, 2.44 ], "fq": 40
  },
  "hinder": {
    "dict": "anew", "word": "hinder", "stem": "hinder",
    "avg": [ 3.81, 4.12 ], "std": [ 1.42, 2.01 ], "fq": 0
  },
  "histori": {
    "dict": "anew", "word": "history", "stem": "histori",
    "avg": [ 5.24, 3.93 ], "std": [ 2.01, 2.29 ], "fq": 286
  },
  "hit": {
    "dict": "anew", "word": "hit", "stem": "hit",
    "avg": [ 4.33, 5.73 ], "std": [ 2.35, 2.09 ], "fq": 115
  },
  "holiday": {
    "dict": "anew", "word": "holiday", "stem": "holiday",
    "avg": [ 7.55, 6.59 ], "std": [ 2.14, 2.73 ], "fq": 17
  },
  "home": {
    "dict": "anew", "word": "home", "stem": "home",
    "avg": [ 7.91, 4.21 ], "std": [ 1.63, 2.94 ], "fq": 547
  },
  "honest": {
    "dict": "anew", "word": "honest", "stem": "honest",
    "avg": [ 7.70, 5.32 ], "std": [ 1.43, 1.92 ], "fq": 47
  },
  "honey": {
    "dict": "anew", "word": "honey", "stem": "honey",
    "avg": [ 6.73, 4.51 ], "std": [ 1.70, 2.25 ], "fq": 25
  },
  "honor": {
    "dict": "anew", "word": "honor", "stem": "honor",
    "avg": [ 7.66, 5.90 ], "std": [ 1.24, 1.83 ], "fq": 66
  },
  "hooker": {
    "dict": "anew", "word": "hooker", "stem": "hooker",
    "avg": [ 3.34, 4.93 ], "std": [ 2.31, 2.82 ], "fq": 0
  },
  "hope": {
    "dict": "anew", "word": "hope", "stem": "hope",
    "avg": [ 7.05, 5.44 ], "std": [ 1.96, 2.47 ], "fq": 178
  },
  "hope": {
    "dict": "anew", "word": "hopeful", "stem": "hope",
    "avg": [ 7.10, 5.78 ], "std": [ 1.46, 2.09 ], "fq": 12
  },
  "horror": {
    "dict": "anew", "word": "horror", "stem": "horror",
    "avg": [ 2.76, 7.21 ], "std": [ 2.25, 2.14 ], "fq": 17
  },
  "hors": {
    "dict": "anew", "word": "horse", "stem": "hors",
    "avg": [ 5.89, 3.89 ], "std": [ 1.55, 2.17 ], "fq": 117
  },
  "hospit": {
    "dict": "anew", "word": "hospital", "stem": "hospit",
    "avg": [ 5.04, 5.98 ], "std": [ 2.45, 2.54 ], "fq": 110
  },
  "hostag": {
    "dict": "anew", "word": "hostage", "stem": "hostag",
    "avg": [ 2.20, 6.76 ], "std": [ 1.80, 2.63 ], "fq": 2
  },
  "hostil": {
    "dict": "anew", "word": "hostile", "stem": "hostil",
    "avg": [ 2.73, 6.44 ], "std": [ 1.50, 2.28 ], "fq": 19
  },
  "hotel": {
    "dict": "anew", "word": "hotel", "stem": "hotel",
    "avg": [ 6.00, 4.80 ], "std": [ 1.77, 2.53 ], "fq": 126
  },
  "hous": {
    "dict": "anew", "word": "house", "stem": "hous",
    "avg": [ 7.26, 4.56 ], "std": [ 1.72, 2.41 ], "fq": 591
  },
  "hug": {
    "dict": "anew", "word": "hug", "stem": "hug",
    "avg": [ 8.00, 5.35 ], "std": [ 1.55, 2.76 ], "fq": 3
  },
  "human": {
    "dict": "anew", "word": "humane", "stem": "human",
    "avg": [ 6.89, 4.50 ], "std": [ 1.70, 1.91 ], "fq": 5
  },
  "humbl": {
    "dict": "anew", "word": "humble", "stem": "humbl",
    "avg": [ 5.86, 3.74 ], "std": [ 1.42, 2.33 ], "fq": 18
  },
  "humili": {
    "dict": "anew", "word": "humiliate", "stem": "humili",
    "avg": [ 2.24, 6.14 ], "std": [ 1.34, 2.42 ], "fq": 0
  },
  "humor": {
    "dict": "anew", "word": "humor", "stem": "humor",
    "avg": [ 8.56, 5.50 ], "std": [ 0.81, 2.91 ], "fq": 47
  },
  "hungri": {
    "dict": "anew", "word": "hungry", "stem": "hungri",
    "avg": [ 3.58, 5.13 ], "std": [ 2.01, 2.44 ], "fq": 23
  },
  "hurrican": {
    "dict": "anew", "word": "hurricane", "stem": "hurrican",
    "avg": [ 3.34, 6.83 ], "std": [ 2.12, 2.06 ], "fq": 8
  },
  "hurt": {
    "dict": "anew", "word": "hurt", "stem": "hurt",
    "avg": [ 1.90, 5.85 ], "std": [ 1.26, 2.49 ], "fq": 37
  },
  "hydrant": {
    "dict": "anew", "word": "hydrant", "stem": "hydrant",
    "avg": [ 5.02, 3.71 ], "std": [ 0.93, 1.75 ], "fq": 0
  },
  "icebox": {
    "dict": "anew", "word": "icebox", "stem": "icebox",
    "avg": [ 4.95, 4.17 ], "std": [ 1.00, 2.11 ], "fq": 3
  },
  "idea": {
    "dict": "anew", "word": "idea", "stem": "idea",
    "avg": [ 7.00, 5.86 ], "std": [ 1.34, 1.81 ], "fq": 195
  },
  "ident": {
    "dict": "anew", "word": "identity", "stem": "ident",
    "avg": [ 6.57, 4.95 ], "std": [ 1.99, 2.24 ], "fq": 55
  },
  "idiot": {
    "dict": "anew", "word": "idiot", "stem": "idiot",
    "avg": [ 3.16, 4.21 ], "std": [ 1.91, 2.47 ], "fq": 2
  },
  "idol": {
    "dict": "anew", "word": "idol", "stem": "idol",
    "avg": [ 6.12, 4.95 ], "std": [ 1.86, 2.14 ], "fq": 7
  },
  "ignor": {
    "dict": "anew", "word": "ignorance", "stem": "ignor",
    "avg": [ 3.07, 4.39 ], "std": [ 2.25, 2.49 ], "fq": 16
  },
  "ill": {
    "dict": "anew", "word": "illness", "stem": "ill",
    "avg": [ 2.48, 4.71 ], "std": [ 1.40, 2.24 ], "fq": 20
  },
  "imagin": {
    "dict": "anew", "word": "imagine", "stem": "imagin",
    "avg": [ 7.32, 5.98 ], "std": [ 1.52, 2.14 ], "fq": 61
  },
  "immatur": {
    "dict": "anew", "word": "immature", "stem": "immatur",
    "avg": [ 3.39, 4.15 ], "std": [ 1.70, 1.96 ], "fq": 7
  },
  "immor": {
    "dict": "anew", "word": "immoral", "stem": "immor",
    "avg": [ 3.50, 4.98 ], "std": [ 2.16, 2.48 ], "fq": 5
  },
  "impair": {
    "dict": "anew", "word": "impair", "stem": "impair",
    "avg": [ 3.18, 4.04 ], "std": [ 1.86, 2.14 ], "fq": 4
  },
  "impot": {
    "dict": "anew", "word": "impotent", "stem": "impot",
    "avg": [ 2.81, 4.57 ], "std": [ 1.92, 2.59 ], "fq": 2
  },
  "impress": {
    "dict": "anew", "word": "impressed", "stem": "impress",
    "avg": [ 7.33, 5.42 ], "std": [ 1.84, 2.65 ], "fq": 30
  },
  "improv": {
    "dict": "anew", "word": "improve", "stem": "improv",
    "avg": [ 7.65, 5.69 ], "std": [ 1.16, 2.15 ], "fq": 39
  },
  "incent": {
    "dict": "anew", "word": "incentive", "stem": "incent",
    "avg": [ 7.00, 5.69 ], "std": [ 1.72, 2.45 ], "fq": 12
  },
  "indiffer": {
    "dict": "anew", "word": "indifferent", "stem": "indiffer",
    "avg": [ 4.61, 3.18 ], "std": [ 1.28, 1.85 ], "fq": 11
  },
  "industri": {
    "dict": "anew", "word": "industry", "stem": "industri",
    "avg": [ 5.30, 4.47 ], "std": [ 1.61, 2.43 ], "fq": 171
  },
  "infant": {
    "dict": "anew", "word": "infant", "stem": "infant",
    "avg": [ 6.95, 5.05 ], "std": [ 2.08, 2.66 ], "fq": 11
  },
  "infatu": {
    "dict": "anew", "word": "infatuation", "stem": "infatu",
    "avg": [ 6.73, 7.02 ], "std": [ 2.08, 1.87 ], "fq": 4
  },
  "infect": {
    "dict": "anew", "word": "infection", "stem": "infect",
    "avg": [ 1.66, 5.03 ], "std": [ 1.34, 2.77 ], "fq": 8
  },
  "inferior": {
    "dict": "anew", "word": "inferior", "stem": "inferior",
    "avg": [ 3.07, 3.83 ], "std": [ 1.57, 2.05 ], "fq": 7
  },
  "inhabit": {
    "dict": "anew", "word": "inhabitant", "stem": "inhabit",
    "avg": [ 5.05, 3.95 ], "std": [ 1.34, 1.97 ], "fq": 0
  },
  "injuri": {
    "dict": "anew", "word": "injury", "stem": "injuri",
    "avg": [ 2.49, 5.69 ], "std": [ 1.76, 2.06 ], "fq": 27
  },
  "ink": {
    "dict": "anew", "word": "ink", "stem": "ink",
    "avg": [ 5.05, 3.84 ], "std": [ 0.81, 1.88 ], "fq": 7
  },
  "innoc": {
    "dict": "anew", "word": "innocent", "stem": "innoc",
    "avg": [ 6.51, 4.21 ], "std": [ 1.34, 1.99 ], "fq": 37
  },
  "insan": {
    "dict": "anew", "word": "insane", "stem": "insan",
    "avg": [ 2.85, 5.83 ], "std": [ 1.94, 2.45 ], "fq": 13
  },
  "insect": {
    "dict": "anew", "word": "insect", "stem": "insect",
    "avg": [ 4.07, 4.07 ], "std": [ 2.16, 2.46 ], "fq": 14
  },
  "insecur": {
    "dict": "anew", "word": "insecure", "stem": "insecur",
    "avg": [ 2.36, 5.56 ], "std": [ 1.33, 2.34 ], "fq": 3
  },
  "insol": {
    "dict": "anew", "word": "insolent", "stem": "insol",
    "avg": [ 4.35, 5.38 ], "std": [ 1.76, 2.37 ], "fq": 2
  },
  "inspir": {
    "dict": "anew", "word": "inspire", "stem": "inspir",
    "avg": [ 6.97, 5.00 ], "std": [ 1.91, 2.53 ], "fq": 3
  },
  "inspir": {
    "dict": "anew", "word": "inspired", "stem": "inspir",
    "avg": [ 7.15, 6.02 ], "std": [ 1.85, 2.67 ], "fq": 25
  },
  "insult": {
    "dict": "anew", "word": "insult", "stem": "insult",
    "avg": [ 2.29, 6.00 ], "std": [ 1.33, 2.46 ], "fq": 7
  },
  "intellect": {
    "dict": "anew", "word": "intellect", "stem": "intellect",
    "avg": [ 6.82, 4.75 ], "std": [ 1.96, 2.50 ], "fq": 5
  },
  "intercours": {
    "dict": "anew", "word": "intercourse", "stem": "intercours",
    "avg": [ 7.36, 7.00 ], "std": [ 1.57, 2.07 ], "fq": 9
  },
  "interest": {
    "dict": "anew", "word": "interest", "stem": "interest",
    "avg": [ 6.97, 5.66 ], "std": [ 1.53, 2.26 ], "fq": 330
  },
  "intim": {
    "dict": "anew", "word": "intimate", "stem": "intim",
    "avg": [ 7.61, 6.98 ], "std": [ 1.51, 2.21 ], "fq": 21
  },
  "intrud": {
    "dict": "anew", "word": "intruder", "stem": "intrud",
    "avg": [ 2.77, 6.86 ], "std": [ 2.32, 2.41 ], "fq": 1
  },
  "invad": {
    "dict": "anew", "word": "invader", "stem": "invad",
    "avg": [ 3.05, 5.50 ], "std": [ 2.01, 2.40 ], "fq": 1
  },
  "invest": {
    "dict": "anew", "word": "invest", "stem": "invest",
    "avg": [ 5.93, 5.12 ], "std": [ 2.10, 2.42 ], "fq": 3
  },
  "iron": {
    "dict": "anew", "word": "iron", "stem": "iron",
    "avg": [ 4.90, 3.76 ], "std": [ 1.02, 2.06 ], "fq": 43
  },
  "irrit": {
    "dict": "anew", "word": "irritate", "stem": "irrit",
    "avg": [ 3.11, 5.76 ], "std": [ 1.67, 2.15 ], "fq": 0
  },
  "item": {
    "dict": "anew", "word": "item", "stem": "item",
    "avg": [ 5.26, 3.24 ], "std": [ 0.86, 2.08 ], "fq": 54
  },
  "jail": {
    "dict": "anew", "word": "jail", "stem": "jail",
    "avg": [ 1.95, 5.49 ], "std": [ 1.27, 2.67 ], "fq": 21
  },
  "jealousi": {
    "dict": "anew", "word": "jealousy", "stem": "jealousi",
    "avg": [ 2.51, 6.36 ], "std": [ 1.83, 2.66 ], "fq": 4
  },
  "jelli": {
    "dict": "anew", "word": "jelly", "stem": "jelli",
    "avg": [ 5.66, 3.70 ], "std": [ 1.44, 2.29 ], "fq": 3
  },
  "jewel": {
    "dict": "anew", "word": "jewel", "stem": "jewel",
    "avg": [ 7.00, 5.38 ], "std": [ 1.72, 2.54 ], "fq": 1
  },
  "joke": {
    "dict": "anew", "word": "joke", "stem": "joke",
    "avg": [ 8.10, 6.74 ], "std": [ 1.36, 1.84 ], "fq": 22
  },
  "jolli": {
    "dict": "anew", "word": "jolly", "stem": "jolli",
    "avg": [ 7.41, 5.57 ], "std": [ 1.92, 2.80 ], "fq": 4
  },
  "journal": {
    "dict": "anew", "word": "journal", "stem": "journal",
    "avg": [ 5.14, 4.05 ], "std": [ 1.49, 1.96 ], "fq": 42
  },
  "joy": {
    "dict": "anew", "word": "joy", "stem": "joy",
    "avg": [ 8.60, 7.22 ], "std": [ 0.71, 2.13 ], "fq": 40
  },
  "joy": {
    "dict": "anew", "word": "joyful", "stem": "joy",
    "avg": [ 8.22, 5.98 ], "std": [ 1.22, 2.54 ], "fq": 1
  },
  "jug": {
    "dict": "anew", "word": "jug", "stem": "jug",
    "avg": [ 5.24, 3.88 ], "std": [ 1.65, 2.15 ], "fq": 6
  },
  "justic": {
    "dict": "anew", "word": "justice", "stem": "justic",
    "avg": [ 7.78, 5.47 ], "std": [ 1.35, 2.54 ], "fq": 114
  },
  "kerchief": {
    "dict": "anew", "word": "kerchief", "stem": "kerchief",
    "avg": [ 5.11, 3.43 ], "std": [ 1.33, 2.08 ], "fq": 1
  },
  "kerosen": {
    "dict": "anew", "word": "kerosene", "stem": "kerosen",
    "avg": [ 4.80, 4.34 ], "std": [ 1.59, 2.51 ], "fq": 6
  },
  "ketchup": {
    "dict": "anew", "word": "ketchup", "stem": "ketchup",
    "avg": [ 5.60, 4.09 ], "std": [ 1.35, 2.08 ], "fq": 1
  },
  "kettl": {
    "dict": "anew", "word": "kettle", "stem": "kettl",
    "avg": [ 5.22, 3.22 ], "std": [ 0.91, 2.23 ], "fq": 3
  },
  "key": {
    "dict": "anew", "word": "key", "stem": "key",
    "avg": [ 5.68, 3.70 ], "std": [ 1.62, 2.18 ], "fq": 88
  },
  "kick": {
    "dict": "anew", "word": "kick", "stem": "kick",
    "avg": [ 4.31, 4.90 ], "std": [ 2.18, 2.35 ], "fq": 16
  },
  "kid": {
    "dict": "anew", "word": "kids", "stem": "kid",
    "avg": [ 6.91, 5.27 ], "std": [ 1.99, 2.36 ], "fq": 32
  },
  "killer": {
    "dict": "anew", "word": "killer", "stem": "killer",
    "avg": [ 1.89, 7.86 ], "std": [ 1.39, 1.89 ], "fq": 21
  },
  "kind": {
    "dict": "anew", "word": "kind", "stem": "kind",
    "avg": [ 7.59, 4.46 ], "std": [ 1.67, 2.55 ], "fq": 313
  },
  "kind": {
    "dict": "anew", "word": "kindness", "stem": "kind",
    "avg": [ 7.82, 4.30 ], "std": [ 1.39, 2.62 ], "fq": 5
  },
  "king": {
    "dict": "anew", "word": "king", "stem": "king",
    "avg": [ 7.26, 5.51 ], "std": [ 1.67, 2.77 ], "fq": 88
  },
  "kiss": {
    "dict": "anew", "word": "kiss", "stem": "kiss",
    "avg": [ 8.26, 7.32 ], "std": [ 1.54, 2.03 ], "fq": 17
  },
  "kitten": {
    "dict": "anew", "word": "kitten", "stem": "kitten",
    "avg": [ 6.86, 5.08 ], "std": [ 2.13, 2.45 ], "fq": 5
  },
  "knife": {
    "dict": "anew", "word": "knife", "stem": "knife",
    "avg": [ 3.62, 5.80 ], "std": [ 2.18, 2.00 ], "fq": 76
  },
  "knot": {
    "dict": "anew", "word": "knot", "stem": "knot",
    "avg": [ 4.64, 4.07 ], "std": [ 1.36, 2.15 ], "fq": 8
  },
  "knowledg": {
    "dict": "anew", "word": "knowledge", "stem": "knowledg",
    "avg": [ 7.58, 5.92 ], "std": [ 1.32, 2.32 ], "fq": 145
  },
  "lake": {
    "dict": "anew", "word": "lake", "stem": "lake",
    "avg": [ 6.82, 3.95 ], "std": [ 1.54, 2.44 ], "fq": 54
  },
  "lamb": {
    "dict": "anew", "word": "lamb", "stem": "lamb",
    "avg": [ 5.89, 3.36 ], "std": [ 1.73, 2.18 ], "fq": 7
  },
  "lamp": {
    "dict": "anew", "word": "lamp", "stem": "lamp",
    "avg": [ 5.41, 3.80 ], "std": [ 1.00, 2.12 ], "fq": 18
  },
  "lantern": {
    "dict": "anew", "word": "lantern", "stem": "lantern",
    "avg": [ 5.57, 4.05 ], "std": [ 1.19, 2.28 ], "fq": 13
  },
  "laughter": {
    "dict": "anew", "word": "laughter", "stem": "laughter",
    "avg": [ 8.45, 6.75 ], "std": [ 1.08, 2.50 ], "fq": 22
  },
  "lavish": {
    "dict": "anew", "word": "lavish", "stem": "lavish",
    "avg": [ 6.21, 4.93 ], "std": [ 2.03, 2.40 ], "fq": 3
  },
  "lawn": {
    "dict": "anew", "word": "lawn", "stem": "lawn",
    "avg": [ 5.24, 4.00 ], "std": [ 0.86, 1.79 ], "fq": 15
  },
  "lawsuit": {
    "dict": "anew", "word": "lawsuit", "stem": "lawsuit",
    "avg": [ 3.37, 4.93 ], "std": [ 2.00, 2.44 ], "fq": 1
  },
  "lazi": {
    "dict": "anew", "word": "lazy", "stem": "lazi",
    "avg": [ 4.38, 2.65 ], "std": [ 2.02, 2.06 ], "fq": 9
  },
  "leader": {
    "dict": "anew", "word": "leader", "stem": "leader",
    "avg": [ 7.63, 6.27 ], "std": [ 1.59, 2.18 ], "fq": 74
  },
  "learn": {
    "dict": "anew", "word": "learn", "stem": "learn",
    "avg": [ 7.15, 5.39 ], "std": [ 1.49, 2.22 ], "fq": 84
  },
  "legend": {
    "dict": "anew", "word": "legend", "stem": "legend",
    "avg": [ 6.39, 4.88 ], "std": [ 1.34, 1.76 ], "fq": 26
  },
  "leisur": {
    "dict": "anew", "word": "leisurely", "stem": "leisur",
    "avg": [ 6.88, 3.80 ], "std": [ 1.81, 2.38 ], "fq": 5
  },
  "leprosi": {
    "dict": "anew", "word": "leprosy", "stem": "leprosi",
    "avg": [ 2.09, 6.29 ], "std": [ 1.40, 2.23 ], "fq": 1
  },
  "lesbian": {
    "dict": "anew", "word": "lesbian", "stem": "lesbian",
    "avg": [ 4.67, 5.12 ], "std": [ 2.45, 2.27 ], "fq": 0
  },
  "letter": {
    "dict": "anew", "word": "letter", "stem": "letter",
    "avg": [ 6.61, 4.90 ], "std": [ 1.59, 2.37 ], "fq": 145
  },
  "liberti": {
    "dict": "anew", "word": "liberty", "stem": "liberti",
    "avg": [ 7.98, 5.60 ], "std": [ 1.22, 2.65 ], "fq": 46
  },
  "lice": {
    "dict": "anew", "word": "lice", "stem": "lice",
    "avg": [ 2.31, 5.00 ], "std": [ 1.78, 2.26 ], "fq": 2
  },
  "lie": {
    "dict": "anew", "word": "lie", "stem": "lie",
    "avg": [ 2.79, 5.96 ], "std": [ 1.92, 2.63 ], "fq": 59
  },
  "life": {
    "dict": "anew", "word": "life", "stem": "life",
    "avg": [ 7.27, 6.02 ], "std": [ 1.88, 2.62 ], "fq": 715
  },
  "lightbulb": {
    "dict": "anew", "word": "lightbulb", "stem": "lightbulb",
    "avg": [ 5.61, 4.10 ], "std": [ 1.28, 2.02 ], "fq": 0
  },
  "lighthous": {
    "dict": "anew", "word": "lighthouse", "stem": "lighthous",
    "avg": [ 5.89, 4.41 ], "std": [ 2.08, 2.44 ], "fq": 0
  },
  "lightn": {
    "dict": "anew", "word": "lightning", "stem": "lightn",
    "avg": [ 4.57, 6.61 ], "std": [ 2.66, 1.77 ], "fq": 14
  },
  "limber": {
    "dict": "anew", "word": "limber", "stem": "limber",
    "avg": [ 5.68, 4.57 ], "std": [ 1.49, 2.26 ], "fq": 2
  },
  "lion": {
    "dict": "anew", "word": "lion", "stem": "lion",
    "avg": [ 5.57, 6.20 ], "std": [ 1.99, 2.16 ], "fq": 17
  },
  "listless": {
    "dict": "anew", "word": "listless", "stem": "listless",
    "avg": [ 4.12, 4.10 ], "std": [ 1.73, 2.31 ], "fq": 1
  },
  "live": {
    "dict": "anew", "word": "lively", "stem": "live",
    "avg": [ 7.20, 5.53 ], "std": [ 1.97, 2.90 ], "fq": 26
  },
  "locker": {
    "dict": "anew", "word": "locker", "stem": "locker",
    "avg": [ 5.19, 3.38 ], "std": [ 1.31, 2.13 ], "fq": 9
  },
  "loneli": {
    "dict": "anew", "word": "loneliness", "stem": "loneli",
    "avg": [ 1.61, 4.56 ], "std": [ 1.02, 2.97 ], "fq": 9
  },
  "lone": {
    "dict": "anew", "word": "lonely", "stem": "lone",
    "avg": [ 2.17, 4.51 ], "std": [ 1.76, 2.68 ], "fq": 25
  },
  "loser": {
    "dict": "anew", "word": "loser", "stem": "loser",
    "avg": [ 2.25, 4.95 ], "std": [ 1.48, 2.57 ], "fq": 1
  },
  "lost": {
    "dict": "anew", "word": "lost", "stem": "lost",
    "avg": [ 2.82, 5.82 ], "std": [ 1.83, 2.62 ], "fq": 173
  },
  "lotteri": {
    "dict": "anew", "word": "lottery", "stem": "lotteri",
    "avg": [ 6.57, 5.36 ], "std": [ 2.04, 2.45 ], "fq": 1
  },
  "lous": {
    "dict": "anew", "word": "louse", "stem": "lous",
    "avg": [ 2.81, 4.98 ], "std": [ 1.92, 2.03 ], "fq": 3
  },
  "love": {
    "dict": "anew", "word": "love", "stem": "love",
    "avg": [ 8.72, 6.44 ], "std": [ 0.70, 3.35 ], "fq": 232
  },
  "love": {
    "dict": "anew", "word": "loved", "stem": "love",
    "avg": [ 8.64, 6.38 ], "std": [ 0.71, 2.68 ], "fq": 56
  },
  "loyal": {
    "dict": "anew", "word": "loyal", "stem": "loyal",
    "avg": [ 7.55, 5.16 ], "std": [ 1.90, 2.42 ], "fq": 18
  },
  "lucki": {
    "dict": "anew", "word": "lucky", "stem": "lucki",
    "avg": [ 8.17, 6.53 ], "std": [ 1.06, 2.34 ], "fq": 21
  },
  "lump": {
    "dict": "anew", "word": "lump", "stem": "lump",
    "avg": [ 4.16, 4.80 ], "std": [ 2.34, 2.82 ], "fq": 7
  },
  "luscious": {
    "dict": "anew", "word": "luscious", "stem": "luscious",
    "avg": [ 7.50, 5.34 ], "std": [ 1.08, 2.51 ], "fq": 2
  },
  "lust": {
    "dict": "anew", "word": "lust", "stem": "lust",
    "avg": [ 7.12, 6.88 ], "std": [ 1.62, 1.85 ], "fq": 5
  },
  "luxuri": {
    "dict": "anew", "word": "luxury", "stem": "luxuri",
    "avg": [ 7.88, 4.75 ], "std": [ 1.49, 2.91 ], "fq": 21
  },
  "machin": {
    "dict": "anew", "word": "machine", "stem": "machin",
    "avg": [ 5.09, 3.82 ], "std": [ 1.67, 2.40 ], "fq": 103
  },
  "mad": {
    "dict": "anew", "word": "mad", "stem": "mad",
    "avg": [ 2.44, 6.76 ], "std": [ 1.72, 2.26 ], "fq": 39
  },
  "madman": {
    "dict": "anew", "word": "madman", "stem": "madman",
    "avg": [ 3.91, 5.56 ], "std": [ 2.49, 2.78 ], "fq": 2
  },
  "maggot": {
    "dict": "anew", "word": "maggot", "stem": "maggot",
    "avg": [ 2.06, 5.28 ], "std": [ 1.47, 2.96 ], "fq": 2
  },
  "magic": {
    "dict": "anew", "word": "magical", "stem": "magic",
    "avg": [ 7.46, 5.95 ], "std": [ 1.64, 2.36 ], "fq": 12
  },
  "mail": {
    "dict": "anew", "word": "mail", "stem": "mail",
    "avg": [ 6.88, 5.63 ], "std": [ 1.74, 2.36 ], "fq": 47
  },
  "malaria": {
    "dict": "anew", "word": "malaria", "stem": "malaria",
    "avg": [ 2.40, 4.40 ], "std": [ 1.38, 2.54 ], "fq": 3
  },
  "malic": {
    "dict": "anew", "word": "malice", "stem": "malic",
    "avg": [ 2.69, 5.86 ], "std": [ 1.84, 2.75 ], "fq": 2
  },
  "man": {
    "dict": "anew", "word": "man", "stem": "man",
    "avg": [ 6.73, 5.24 ], "std": [ 1.70, 2.31 ], "fq": 1207
  },
  "mangl": {
    "dict": "anew", "word": "mangle", "stem": "mangl",
    "avg": [ 3.90, 5.44 ], "std": [ 2.01, 2.10 ], "fq": 0
  },
  "maniac": {
    "dict": "anew", "word": "maniac", "stem": "maniac",
    "avg": [ 3.76, 5.39 ], "std": [ 2.00, 2.46 ], "fq": 4
  },
  "manner": {
    "dict": "anew", "word": "manner", "stem": "manner",
    "avg": [ 5.64, 4.56 ], "std": [ 1.34, 1.78 ], "fq": 124
  },
  "mantel": {
    "dict": "anew", "word": "mantel", "stem": "mantel",
    "avg": [ 4.93, 3.27 ], "std": [ 1.40, 2.23 ], "fq": 3
  },
  "manur": {
    "dict": "anew", "word": "manure", "stem": "manur",
    "avg": [ 3.10, 4.17 ], "std": [ 1.74, 2.09 ], "fq": 6
  },
  "market": {
    "dict": "anew", "word": "market", "stem": "market",
    "avg": [ 5.66, 4.12 ], "std": [ 1.02, 1.83 ], "fq": 155
  },
  "massacr": {
    "dict": "anew", "word": "massacre", "stem": "massacr",
    "avg": [ 2.28, 5.33 ], "std": [ 1.74, 2.63 ], "fq": 1
  },
  "master": {
    "dict": "anew", "word": "masterful", "stem": "master",
    "avg": [ 7.09, 5.20 ], "std": [ 1.78, 2.85 ], "fq": 2
  },
  "masturb": {
    "dict": "anew", "word": "masturbate", "stem": "masturb",
    "avg": [ 5.45, 5.67 ], "std": [ 2.02, 2.18 ], "fq": 0
  },
  "materi": {
    "dict": "anew", "word": "material", "stem": "materi",
    "avg": [ 5.26, 4.05 ], "std": [ 1.29, 2.34 ], "fq": 174
  },
  "measl": {
    "dict": "anew", "word": "measles", "stem": "measl",
    "avg": [ 2.74, 5.06 ], "std": [ 1.97, 2.44 ], "fq": 2
  },
  "medicin": {
    "dict": "anew", "word": "medicine", "stem": "medicin",
    "avg": [ 5.67, 4.40 ], "std": [ 2.06, 2.36 ], "fq": 30
  },
  "meek": {
    "dict": "anew", "word": "meek", "stem": "meek",
    "avg": [ 3.87, 3.80 ], "std": [ 1.69, 2.13 ], "fq": 10
  },
  "melodi": {
    "dict": "anew", "word": "melody", "stem": "melodi",
    "avg": [ 7.07, 4.98 ], "std": [ 1.79, 2.52 ], "fq": 21
  },
  "memori": {
    "dict": "anew", "word": "memories", "stem": "memori",
    "avg": [ 7.48, 6.10 ], "std": [ 1.61, 2.10 ], "fq": 15
  },
  "memori": {
    "dict": "anew", "word": "memory", "stem": "memori",
    "avg": [ 6.62, 5.42 ], "std": [ 1.50, 2.25 ], "fq": 76
  },
  "menac": {
    "dict": "anew", "word": "menace", "stem": "menac",
    "avg": [ 2.88, 5.52 ], "std": [ 1.64, 2.45 ], "fq": 9
  },
  "merri": {
    "dict": "anew", "word": "merry", "stem": "merri",
    "avg": [ 7.90, 5.90 ], "std": [ 1.49, 2.42 ], "fq": 8
  },
  "messi": {
    "dict": "anew", "word": "messy", "stem": "messi",
    "avg": [ 3.15, 3.34 ], "std": [ 1.73, 2.37 ], "fq": 3
  },
  "metal": {
    "dict": "anew", "word": "metal", "stem": "metal",
    "avg": [ 4.95, 3.79 ], "std": [ 1.17, 1.96 ], "fq": 61
  },
  "method": {
    "dict": "anew", "word": "method", "stem": "method",
    "avg": [ 5.56, 3.85 ], "std": [ 1.76, 2.58 ], "fq": 142
  },
  "mighti": {
    "dict": "anew", "word": "mighty", "stem": "mighti",
    "avg": [ 6.54, 5.61 ], "std": [ 2.19, 2.38 ], "fq": 29
  },
  "mildew": {
    "dict": "anew", "word": "mildew", "stem": "mildew",
    "avg": [ 3.17, 4.08 ], "std": [ 1.36, 1.79 ], "fq": 1
  },
  "milk": {
    "dict": "anew", "word": "milk", "stem": "milk",
    "avg": [ 5.95, 3.68 ], "std": [ 2.16, 2.57 ], "fq": 49
  },
  "millionair": {
    "dict": "anew", "word": "millionaire", "stem": "millionair",
    "avg": [ 8.03, 6.14 ], "std": [ 1.42, 2.70 ], "fq": 2
  },
  "mind": {
    "dict": "anew", "word": "mind", "stem": "mind",
    "avg": [ 6.68, 5.00 ], "std": [ 1.84, 2.68 ], "fq": 325
  },
  "miracl": {
    "dict": "anew", "word": "miracle", "stem": "miracl",
    "avg": [ 8.60, 7.65 ], "std": [ 0.71, 1.67 ], "fq": 16
  },
  "mischief": {
    "dict": "anew", "word": "mischief", "stem": "mischief",
    "avg": [ 5.57, 5.76 ], "std": [ 2.05, 1.95 ], "fq": 5
  },
  "miseri": {
    "dict": "anew", "word": "misery", "stem": "miseri",
    "avg": [ 1.93, 5.17 ], "std": [ 1.60, 2.69 ], "fq": 15
  },
  "mistak": {
    "dict": "anew", "word": "mistake", "stem": "mistak",
    "avg": [ 2.86, 5.18 ], "std": [ 1.79, 2.42 ], "fq": 34
  },
  "mobil": {
    "dict": "anew", "word": "mobility", "stem": "mobil",
    "avg": [ 6.83, 5.00 ], "std": [ 1.79, 2.18 ], "fq": 8
  },
  "modest": {
    "dict": "anew", "word": "modest", "stem": "modest",
    "avg": [ 5.76, 3.98 ], "std": [ 1.28, 2.24 ], "fq": 29
  },
  "mold": {
    "dict": "anew", "word": "mold", "stem": "mold",
    "avg": [ 3.55, 4.07 ], "std": [ 1.70, 1.98 ], "fq": 45
  },
  "moment": {
    "dict": "anew", "word": "moment", "stem": "moment",
    "avg": [ 5.76, 3.83 ], "std": [ 1.65, 2.29 ], "fq": 246
  },
  "money": {
    "dict": "anew", "word": "money", "stem": "money",
    "avg": [ 7.59, 5.70 ], "std": [ 1.40, 2.66 ], "fq": 265
  },
  "month": {
    "dict": "anew", "word": "month", "stem": "month",
    "avg": [ 5.15, 4.03 ], "std": [ 1.09, 1.77 ], "fq": 130
  },
  "moodi": {
    "dict": "anew", "word": "moody", "stem": "moodi",
    "avg": [ 3.20, 4.18 ], "std": [ 1.58, 2.38 ], "fq": 5
  },
  "moral": {
    "dict": "anew", "word": "moral", "stem": "moral",
    "avg": [ 6.20, 4.49 ], "std": [ 1.85, 2.28 ], "fq": 142
  },
  "morbid": {
    "dict": "anew", "word": "morbid", "stem": "morbid",
    "avg": [ 2.87, 5.06 ], "std": [ 2.14, 2.68 ], "fq": 1
  },
  "morgu": {
    "dict": "anew", "word": "morgue", "stem": "morgu",
    "avg": [ 1.92, 4.84 ], "std": [ 1.32, 2.96 ], "fq": 1
  },
  "mosquito": {
    "dict": "anew", "word": "mosquito", "stem": "mosquito",
    "avg": [ 2.80, 4.78 ], "std": [ 1.91, 2.72 ], "fq": 1
  },
  "mother": {
    "dict": "anew", "word": "mother", "stem": "mother",
    "avg": [ 8.39, 6.13 ], "std": [ 1.15, 2.71 ], "fq": 216
  },
  "mountain": {
    "dict": "anew", "word": "mountain", "stem": "mountain",
    "avg": [ 6.59, 5.49 ], "std": [ 1.66, 2.43 ], "fq": 33
  },
  "movi": {
    "dict": "anew", "word": "movie", "stem": "movi",
    "avg": [ 6.86, 4.93 ], "std": [ 1.81, 2.54 ], "fq": 29
  },
  "mucus": {
    "dict": "anew", "word": "mucus", "stem": "mucus",
    "avg": [ 3.34, 3.41 ], "std": [ 2.29, 2.17 ], "fq": 2
  },
  "muddi": {
    "dict": "anew", "word": "muddy", "stem": "muddi",
    "avg": [ 4.44, 4.13 ], "std": [ 2.07, 2.13 ], "fq": 10
  },
  "muffin": {
    "dict": "anew", "word": "muffin", "stem": "muffin",
    "avg": [ 6.57, 4.76 ], "std": [ 2.04, 2.42 ], "fq": 0
  },
  "murder": {
    "dict": "anew", "word": "murderer", "stem": "murder",
    "avg": [ 1.53, 7.47 ], "std": [ 0.96, 2.18 ], "fq": 19
  },
  "muscular": {
    "dict": "anew", "word": "muscular", "stem": "muscular",
    "avg": [ 6.82, 5.47 ], "std": [ 1.63, 2.20 ], "fq": 16
  },
  "museum": {
    "dict": "anew", "word": "museum", "stem": "museum",
    "avg": [ 5.54, 3.60 ], "std": [ 1.86, 2.13 ], "fq": 32
  },
  "mushroom": {
    "dict": "anew", "word": "mushroom", "stem": "mushroom",
    "avg": [ 5.78, 4.72 ], "std": [ 2.22, 2.33 ], "fq": 2
  },
  "music": {
    "dict": "anew", "word": "music", "stem": "music",
    "avg": [ 8.13, 5.32 ], "std": [ 1.09, 3.19 ], "fq": 216
  },
  "mutat": {
    "dict": "anew", "word": "mutation", "stem": "mutat",
    "avg": [ 3.91, 4.84 ], "std": [ 2.44, 2.52 ], "fq": 0
  },
  "mutil": {
    "dict": "anew", "word": "mutilate", "stem": "mutil",
    "avg": [ 1.82, 6.41 ], "std": [ 1.45, 2.94 ], "fq": 3
  },
  "mystic": {
    "dict": "anew", "word": "mystic", "stem": "mystic",
    "avg": [ 6.00, 4.84 ], "std": [ 2.21, 2.57 ], "fq": 3
  },
  "nake": {
    "dict": "anew", "word": "naked", "stem": "nake",
    "avg": [ 6.34, 5.80 ], "std": [ 2.42, 2.80 ], "fq": 32
  },
  "name": {
    "dict": "anew", "word": "name", "stem": "name",
    "avg": [ 5.55, 4.25 ], "std": [ 2.24, 2.47 ], "fq": 294
  },
  "narcot": {
    "dict": "anew", "word": "narcotic", "stem": "narcot",
    "avg": [ 4.29, 4.93 ], "std": [ 2.30, 2.57 ], "fq": 2
  },
  "nasti": {
    "dict": "anew", "word": "nasty", "stem": "nasti",
    "avg": [ 3.58, 4.89 ], "std": [ 2.38, 2.50 ], "fq": 5
  },
  "natur": {
    "dict": "anew", "word": "natural", "stem": "natur",
    "avg": [ 6.59, 4.09 ], "std": [ 1.57, 2.37 ], "fq": 156
  },
  "natur": {
    "dict": "anew", "word": "nature", "stem": "natur",
    "avg": [ 7.65, 4.37 ], "std": [ 1.37, 2.51 ], "fq": 191
  },
  "nectar": {
    "dict": "anew", "word": "nectar", "stem": "nectar",
    "avg": [ 6.90, 3.89 ], "std": [ 1.53, 2.48 ], "fq": 3
  },
  "needl": {
    "dict": "anew", "word": "needle", "stem": "needl",
    "avg": [ 3.82, 5.36 ], "std": [ 1.73, 2.89 ], "fq": 15
  },
  "neglect": {
    "dict": "anew", "word": "neglect", "stem": "neglect",
    "avg": [ 2.63, 4.83 ], "std": [ 1.64, 2.31 ], "fq": 12
  },
  "nervous": {
    "dict": "anew", "word": "nervous", "stem": "nervous",
    "avg": [ 3.29, 6.59 ], "std": [ 1.47, 2.07 ], "fq": 24
  },
  "neurot": {
    "dict": "anew", "word": "neurotic", "stem": "neurot",
    "avg": [ 4.45, 5.13 ], "std": [ 2.23, 2.76 ], "fq": 10
  },
  "news": {
    "dict": "anew", "word": "news", "stem": "news",
    "avg": [ 5.30, 5.17 ], "std": [ 1.67, 2.11 ], "fq": 102
  },
  "nice": {
    "dict": "anew", "word": "nice", "stem": "nice",
    "avg": [ 6.55, 4.38 ], "std": [ 2.44, 2.69 ], "fq": 75
  },
  "nightmar": {
    "dict": "anew", "word": "nightmare", "stem": "nightmar",
    "avg": [ 1.91, 7.59 ], "std": [ 1.54, 2.23 ], "fq": 9
  },
  "nippl": {
    "dict": "anew", "word": "nipple", "stem": "nippl",
    "avg": [ 6.27, 5.56 ], "std": [ 1.81, 2.55 ], "fq": 0
  },
  "noisi": {
    "dict": "anew", "word": "noisy", "stem": "noisi",
    "avg": [ 5.02, 6.38 ], "std": [ 2.02, 1.78 ], "fq": 6
  },
  "nonchal": {
    "dict": "anew", "word": "nonchalant", "stem": "nonchal",
    "avg": [ 4.74, 3.12 ], "std": [ 1.11, 1.93 ], "fq": 1
  },
  "nonsens": {
    "dict": "anew", "word": "nonsense", "stem": "nonsens",
    "avg": [ 4.61, 4.17 ], "std": [ 1.63, 2.02 ], "fq": 13
  },
  "noos": {
    "dict": "anew", "word": "noose", "stem": "noos",
    "avg": [ 3.76, 4.39 ], "std": [ 1.64, 2.08 ], "fq": 3
  },
  "nourish": {
    "dict": "anew", "word": "nourish", "stem": "nourish",
    "avg": [ 6.46, 4.29 ], "std": [ 1.69, 2.51 ], "fq": 0
  },
  "nude": {
    "dict": "anew", "word": "nude", "stem": "nude",
    "avg": [ 6.82, 6.41 ], "std": [ 1.63, 2.09 ], "fq": 20
  },
  "nuisanc": {
    "dict": "anew", "word": "nuisance", "stem": "nuisanc",
    "avg": [ 3.27, 4.49 ], "std": [ 1.86, 2.69 ], "fq": 5
  },
  "nun": {
    "dict": "anew", "word": "nun", "stem": "nun",
    "avg": [ 4.93, 2.93 ], "std": [ 1.89, 1.80 ], "fq": 2
  },
  "nurs": {
    "dict": "anew", "word": "nurse", "stem": "nurs",
    "avg": [ 6.08, 4.84 ], "std": [ 2.08, 2.04 ], "fq": 17
  },
  "nurseri": {
    "dict": "anew", "word": "nursery", "stem": "nurseri",
    "avg": [ 5.73, 4.04 ], "std": [ 2.30, 2.74 ], "fq": 13
  },
  "obes": {
    "dict": "anew", "word": "obesity", "stem": "obes",
    "avg": [ 2.73, 3.87 ], "std": [ 1.85, 2.82 ], "fq": 5
  },
  "obey": {
    "dict": "anew", "word": "obey", "stem": "obey",
    "avg": [ 4.52, 4.23 ], "std": [ 1.88, 1.72 ], "fq": 8
  },
  "obnoxi": {
    "dict": "anew", "word": "obnoxious", "stem": "obnoxi",
    "avg": [ 3.50, 4.74 ], "std": [ 2.18, 2.42 ], "fq": 5
  },
  "obscen": {
    "dict": "anew", "word": "obscene", "stem": "obscen",
    "avg": [ 4.23, 5.04 ], "std": [ 2.30, 2.30 ], "fq": 2
  },
  "obsess": {
    "dict": "anew", "word": "obsession", "stem": "obsess",
    "avg": [ 4.52, 6.41 ], "std": [ 2.13, 2.13 ], "fq": 5
  },
  "ocean": {
    "dict": "anew", "word": "ocean", "stem": "ocean",
    "avg": [ 7.12, 4.95 ], "std": [ 1.72, 2.79 ], "fq": 34
  },
  "odd": {
    "dict": "anew", "word": "odd", "stem": "odd",
    "avg": [ 4.82, 4.27 ], "std": [ 2.04, 2.46 ], "fq": 44
  },
  "offend": {
    "dict": "anew", "word": "offend", "stem": "offend",
    "avg": [ 2.76, 5.56 ], "std": [ 1.50, 2.06 ], "fq": 4
  },
  "offic": {
    "dict": "anew", "word": "office", "stem": "offic",
    "avg": [ 5.24, 4.08 ], "std": [ 1.59, 1.92 ], "fq": 255
  },
  "opinion": {
    "dict": "anew", "word": "opinion", "stem": "opinion",
    "avg": [ 6.28, 4.89 ], "std": [ 1.45, 2.46 ], "fq": 96
  },
  "optim": {
    "dict": "anew", "word": "optimism", "stem": "optim",
    "avg": [ 6.95, 5.34 ], "std": [ 2.24, 2.58 ], "fq": 15
  },
  "option": {
    "dict": "anew", "word": "option", "stem": "option",
    "avg": [ 6.49, 4.74 ], "std": [ 1.31, 2.23 ], "fq": 5
  },
  "orchestra": {
    "dict": "anew", "word": "orchestra", "stem": "orchestra",
    "avg": [ 6.02, 3.52 ], "std": [ 1.89, 2.29 ], "fq": 60
  },
  "orgasm": {
    "dict": "anew", "word": "orgasm", "stem": "orgasm",
    "avg": [ 8.32, 8.10 ], "std": [ 1.31, 1.45 ], "fq": 7
  },
  "outdoor": {
    "dict": "anew", "word": "outdoors", "stem": "outdoor",
    "avg": [ 7.47, 5.92 ], "std": [ 1.80, 2.55 ], "fq": 6
  },
  "outrag": {
    "dict": "anew", "word": "outrage", "stem": "outrag",
    "avg": [ 3.52, 6.83 ], "std": [ 2.12, 2.26 ], "fq": 4
  },
  "outstand": {
    "dict": "anew", "word": "outstanding", "stem": "outstand",
    "avg": [ 7.75, 6.24 ], "std": [ 1.75, 2.59 ], "fq": 37
  },
  "overcast": {
    "dict": "anew", "word": "overcast", "stem": "overcast",
    "avg": [ 3.65, 3.46 ], "std": [ 1.61, 1.92 ], "fq": 9
  },
  "overwhelm": {
    "dict": "anew", "word": "overwhelmed", "stem": "overwhelm",
    "avg": [ 4.19, 7.00 ], "std": [ 2.61, 2.37 ], "fq": 4
  },
  "owl": {
    "dict": "anew", "word": "owl", "stem": "owl",
    "avg": [ 5.80, 3.98 ], "std": [ 1.31, 1.87 ], "fq": 2
  },
  "pain": {
    "dict": "anew", "word": "pain", "stem": "pain",
    "avg": [ 2.13, 6.50 ], "std": [ 1.81, 2.49 ], "fq": 88
  },
  "paint": {
    "dict": "anew", "word": "paint", "stem": "paint",
    "avg": [ 5.62, 4.10 ], "std": [ 1.72, 2.36 ], "fq": 37
  },
  "palac": {
    "dict": "anew", "word": "palace", "stem": "palac",
    "avg": [ 7.19, 5.10 ], "std": [ 1.78, 2.75 ], "fq": 38
  },
  "pamphlet": {
    "dict": "anew", "word": "pamphlet", "stem": "pamphlet",
    "avg": [ 4.79, 3.62 ], "std": [ 1.05, 2.02 ], "fq": 3
  },
  "pancak": {
    "dict": "anew", "word": "pancakes", "stem": "pancak",
    "avg": [ 6.08, 4.06 ], "std": [ 1.83, 2.13 ], "fq": 0
  },
  "panic": {
    "dict": "anew", "word": "panic", "stem": "panic",
    "avg": [ 3.12, 7.02 ], "std": [ 1.84, 2.02 ], "fq": 22
  },
  "paper": {
    "dict": "anew", "word": "paper", "stem": "paper",
    "avg": [ 5.20, 2.50 ], "std": [ 1.21, 1.85 ], "fq": 157
  },
  "paradis": {
    "dict": "anew", "word": "paradise", "stem": "paradis",
    "avg": [ 8.72, 5.12 ], "std": [ 0.60, 3.38 ], "fq": 12
  },
  "paralysi": {
    "dict": "anew", "word": "paralysis", "stem": "paralysi",
    "avg": [ 1.98, 4.73 ], "std": [ 1.44, 2.83 ], "fq": 6
  },
  "part": {
    "dict": "anew", "word": "part", "stem": "part",
    "avg": [ 5.11, 3.82 ], "std": [ 1.78, 2.24 ], "fq": 500
  },
  "parti": {
    "dict": "anew", "word": "party", "stem": "parti",
    "avg": [ 7.86, 6.69 ], "std": [ 1.83, 2.84 ], "fq": 216
  },
  "passag": {
    "dict": "anew", "word": "passage", "stem": "passag",
    "avg": [ 5.28, 4.36 ], "std": [ 1.44, 2.13 ], "fq": 49
  },
  "passion": {
    "dict": "anew", "word": "passion", "stem": "passion",
    "avg": [ 8.03, 7.26 ], "std": [ 1.27, 2.57 ], "fq": 28
  },
  "pasta": {
    "dict": "anew", "word": "pasta", "stem": "pasta",
    "avg": [ 6.69, 4.94 ], "std": [ 1.64, 2.04 ], "fq": 0
  },
  "patent": {
    "dict": "anew", "word": "patent", "stem": "patent",
    "avg": [ 5.29, 3.50 ], "std": [ 1.08, 1.84 ], "fq": 35
  },
  "patient": {
    "dict": "anew", "word": "patient", "stem": "patient",
    "avg": [ 5.29, 4.21 ], "std": [ 1.89, 2.37 ], "fq": 86
  },
  "patriot": {
    "dict": "anew", "word": "patriot", "stem": "patriot",
    "avg": [ 6.71, 5.17 ], "std": [ 1.69, 2.53 ], "fq": 10
  },
  "peac": {
    "dict": "anew", "word": "peace", "stem": "peac",
    "avg": [ 7.72, 2.95 ], "std": [ 1.75, 2.55 ], "fq": 198
  },
  "penalti": {
    "dict": "anew", "word": "penalty", "stem": "penalti",
    "avg": [ 2.83, 5.10 ], "std": [ 1.56, 2.31 ], "fq": 14
  },
  "pencil": {
    "dict": "anew", "word": "pencil", "stem": "pencil",
    "avg": [ 5.22, 3.14 ], "std": [ 0.68, 1.90 ], "fq": 34
  },
  "peni": {
    "dict": "anew", "word": "penis", "stem": "peni",
    "avg": [ 5.90, 5.54 ], "std": [ 1.72, 2.63 ], "fq": 0
  },
  "penthous": {
    "dict": "anew", "word": "penthouse", "stem": "penthous",
    "avg": [ 6.81, 5.52 ], "std": [ 1.64, 2.49 ], "fq": 1
  },
  "peopl": {
    "dict": "anew", "word": "people", "stem": "peopl",
    "avg": [ 7.33, 5.94 ], "std": [ 1.70, 2.09 ], "fq": 847
  },
  "perfect": {
    "dict": "anew", "word": "perfection", "stem": "perfect",
    "avg": [ 7.25, 5.95 ], "std": [ 2.05, 2.73 ], "fq": 11
  },
  "perfum": {
    "dict": "anew", "word": "perfume", "stem": "perfum",
    "avg": [ 6.76, 5.05 ], "std": [ 1.48, 2.36 ], "fq": 10
  },
  "person": {
    "dict": "anew", "word": "person", "stem": "person",
    "avg": [ 6.32, 4.19 ], "std": [ 1.74, 2.45 ], "fq": 175
  },
  "pervert": {
    "dict": "anew", "word": "pervert", "stem": "pervert",
    "avg": [ 2.79, 6.26 ], "std": [ 2.12, 2.61 ], "fq": 1
  },
  "pest": {
    "dict": "anew", "word": "pest", "stem": "pest",
    "avg": [ 3.13, 5.62 ], "std": [ 1.82, 2.15 ], "fq": 4
  },
  "pet": {
    "dict": "anew", "word": "pet", "stem": "pet",
    "avg": [ 6.79, 5.10 ], "std": [ 2.32, 2.59 ], "fq": 8
  },
  "phase": {
    "dict": "anew", "word": "phase", "stem": "phase",
    "avg": [ 5.17, 3.98 ], "std": [ 0.79, 1.82 ], "fq": 72
  },
  "pie": {
    "dict": "anew", "word": "pie", "stem": "pie",
    "avg": [ 6.41, 4.20 ], "std": [ 1.89, 2.40 ], "fq": 14
  },
  "pig": {
    "dict": "anew", "word": "pig", "stem": "pig",
    "avg": [ 5.07, 4.20 ], "std": [ 1.97, 2.42 ], "fq": 8
  },
  "pillow": {
    "dict": "anew", "word": "pillow", "stem": "pillow",
    "avg": [ 7.92, 2.97 ], "std": [ 1.40, 2.52 ], "fq": 8
  },
  "pinch": {
    "dict": "anew", "word": "pinch", "stem": "pinch",
    "avg": [ 3.83, 4.59 ], "std": [ 1.70, 2.10 ], "fq": 6
  },
  "pistol": {
    "dict": "anew", "word": "pistol", "stem": "pistol",
    "avg": [ 4.20, 6.15 ], "std": [ 2.58, 2.19 ], "fq": 27
  },
  "piti": {
    "dict": "anew", "word": "pity", "stem": "piti",
    "avg": [ 3.37, 3.72 ], "std": [ 1.57, 2.02 ], "fq": 14
  },
  "pizza": {
    "dict": "anew", "word": "pizza", "stem": "pizza",
    "avg": [ 6.65, 5.24 ], "std": [ 2.23, 2.09 ], "fq": 3
  },
  "plain": {
    "dict": "anew", "word": "plain", "stem": "plain",
    "avg": [ 4.39, 3.52 ], "std": [ 1.46, 2.05 ], "fq": 48
  },
  "plane": {
    "dict": "anew", "word": "plane", "stem": "plane",
    "avg": [ 6.43, 6.14 ], "std": [ 1.98, 2.39 ], "fq": 114
  },
  "plant": {
    "dict": "anew", "word": "plant", "stem": "plant",
    "avg": [ 5.98, 3.62 ], "std": [ 1.83, 2.25 ], "fq": 125
  },
  "pleasur": {
    "dict": "anew", "word": "pleasure", "stem": "pleasur",
    "avg": [ 8.28, 5.74 ], "std": [ 0.92, 2.81 ], "fq": 62
  },
  "poetri": {
    "dict": "anew", "word": "poetry", "stem": "poetri",
    "avg": [ 5.86, 4.00 ], "std": [ 1.91, 2.85 ], "fq": 88
  },
  "poison": {
    "dict": "anew", "word": "poison", "stem": "poison",
    "avg": [ 1.98, 6.05 ], "std": [ 1.44, 2.82 ], "fq": 10
  },
  "polit": {
    "dict": "anew", "word": "politeness", "stem": "polit",
    "avg": [ 7.18, 3.74 ], "std": [ 1.50, 2.37 ], "fq": 5
  },
  "pollut": {
    "dict": "anew", "word": "pollute", "stem": "pollut",
    "avg": [ 1.85, 6.08 ], "std": [ 1.11, 2.42 ], "fq": 1
  },
  "poster": {
    "dict": "anew", "word": "poster", "stem": "poster",
    "avg": [ 5.34, 3.93 ], "std": [ 1.75, 2.56 ], "fq": 4
  },
  "poverti": {
    "dict": "anew", "word": "poverty", "stem": "poverti",
    "avg": [ 1.67, 4.87 ], "std": [ 0.90, 2.66 ], "fq": 20
  },
  "power": {
    "dict": "anew", "word": "power", "stem": "power",
    "avg": [ 6.54, 6.67 ], "std": [ 2.21, 1.87 ], "fq": 342
  },
  "power": {
    "dict": "anew", "word": "powerful", "stem": "power",
    "avg": [ 6.84, 5.83 ], "std": [ 1.80, 2.69 ], "fq": 63
  },
  "prairi": {
    "dict": "anew", "word": "prairie", "stem": "prairi",
    "avg": [ 5.75, 3.41 ], "std": [ 1.43, 2.17 ], "fq": 21
  },
  "present": {
    "dict": "anew", "word": "present", "stem": "present",
    "avg": [ 6.95, 5.12 ], "std": [ 1.85, 2.39 ], "fq": 377
  },
  "pressur": {
    "dict": "anew", "word": "pressure", "stem": "pressur",
    "avg": [ 3.38, 6.07 ], "std": [ 1.61, 2.26 ], "fq": 185
  },
  "prestig": {
    "dict": "anew", "word": "prestige", "stem": "prestig",
    "avg": [ 7.26, 5.86 ], "std": [ 1.90, 2.08 ], "fq": 29
  },
  "pretti": {
    "dict": "anew", "word": "pretty", "stem": "pretti",
    "avg": [ 7.75, 6.03 ], "std": [ 1.26, 2.22 ], "fq": 107
  },
  "prick": {
    "dict": "anew", "word": "prick", "stem": "prick",
    "avg": [ 3.98, 4.70 ], "std": [ 1.73, 2.59 ], "fq": 2
  },
  "pride": {
    "dict": "anew", "word": "pride", "stem": "pride",
    "avg": [ 7.00, 5.83 ], "std": [ 2.11, 2.48 ], "fq": 42
  },
  "priest": {
    "dict": "anew", "word": "priest", "stem": "priest",
    "avg": [ 6.42, 4.41 ], "std": [ 2.00, 2.71 ], "fq": 16
  },
  "prison": {
    "dict": "anew", "word": "prison", "stem": "prison",
    "avg": [ 2.05, 5.70 ], "std": [ 1.34, 2.56 ], "fq": 42
  },
  "privaci": {
    "dict": "anew", "word": "privacy", "stem": "privaci",
    "avg": [ 5.88, 4.12 ], "std": [ 1.50, 1.83 ], "fq": 12
  },
  "profit": {
    "dict": "anew", "word": "profit", "stem": "profit",
    "avg": [ 7.63, 6.68 ], "std": [ 1.30, 1.78 ], "fq": 28
  },
  "progress": {
    "dict": "anew", "word": "progress", "stem": "progress",
    "avg": [ 7.73, 6.02 ], "std": [ 1.34, 2.58 ], "fq": 120
  },
  "promot": {
    "dict": "anew", "word": "promotion", "stem": "promot",
    "avg": [ 8.20, 6.44 ], "std": [ 1.15, 2.58 ], "fq": 26
  },
  "protect": {
    "dict": "anew", "word": "protected", "stem": "protect",
    "avg": [ 7.29, 4.09 ], "std": [ 1.79, 2.77 ], "fq": 31
  },
  "proud": {
    "dict": "anew", "word": "proud", "stem": "proud",
    "avg": [ 8.03, 5.56 ], "std": [ 1.56, 3.01 ], "fq": 50
  },
  "pungent": {
    "dict": "anew", "word": "pungent", "stem": "pungent",
    "avg": [ 3.95, 4.24 ], "std": [ 2.09, 2.17 ], "fq": 4
  },
  "punish": {
    "dict": "anew", "word": "punishment", "stem": "punish",
    "avg": [ 2.22, 5.93 ], "std": [ 1.41, 2.40 ], "fq": 21
  },
  "puppi": {
    "dict": "anew", "word": "puppy", "stem": "puppi",
    "avg": [ 7.56, 5.85 ], "std": [ 1.90, 2.78 ], "fq": 2
  },
  "pus": {
    "dict": "anew", "word": "pus", "stem": "pus",
    "avg": [ 2.86, 4.82 ], "std": [ 1.91, 2.06 ], "fq": 0
  },
  "putrid": {
    "dict": "anew", "word": "putrid", "stem": "putrid",
    "avg": [ 2.38, 5.74 ], "std": [ 1.71, 2.26 ], "fq": 0
  },
  "python": {
    "dict": "anew", "word": "python", "stem": "python",
    "avg": [ 4.05, 6.18 ], "std": [ 2.48, 2.25 ], "fq": 14
  },
  "qualiti": {
    "dict": "anew", "word": "quality", "stem": "qualiti",
    "avg": [ 6.25, 4.48 ], "std": [ 1.59, 2.12 ], "fq": 114
  },
  "quarrel": {
    "dict": "anew", "word": "quarrel", "stem": "quarrel",
    "avg": [ 2.93, 6.29 ], "std": [ 2.06, 2.56 ], "fq": 20
  },
  "quart": {
    "dict": "anew", "word": "quart", "stem": "quart",
    "avg": [ 5.39, 3.59 ], "std": [ 2.01, 2.51 ], "fq": 3
  },
  "queen": {
    "dict": "anew", "word": "queen", "stem": "queen",
    "avg": [ 6.44, 4.76 ], "std": [ 1.43, 2.18 ], "fq": 41
  },
  "quick": {
    "dict": "anew", "word": "quick", "stem": "quick",
    "avg": [ 6.64, 6.57 ], "std": [ 1.61, 1.78 ], "fq": 68
  },
  "quiet": {
    "dict": "anew", "word": "quiet", "stem": "quiet",
    "avg": [ 5.58, 2.82 ], "std": [ 1.83, 2.13 ], "fq": 76
  },
  "rabbit": {
    "dict": "anew", "word": "rabbit", "stem": "rabbit",
    "avg": [ 6.57, 4.02 ], "std": [ 1.92, 2.19 ], "fq": 11
  },
  "rabi": {
    "dict": "anew", "word": "rabies", "stem": "rabi",
    "avg": [ 1.77, 6.10 ], "std": [ 0.97, 2.62 ], "fq": 1
  },
  "radiant": {
    "dict": "anew", "word": "radiant", "stem": "radiant",
    "avg": [ 6.73, 5.39 ], "std": [ 2.17, 2.82 ], "fq": 8
  },
  "radiat": {
    "dict": "anew", "word": "radiator", "stem": "radiat",
    "avg": [ 4.67, 4.02 ], "std": [ 1.05, 1.94 ], "fq": 4
  },
  "radio": {
    "dict": "anew", "word": "radio", "stem": "radio",
    "avg": [ 6.73, 4.78 ], "std": [ 1.47, 2.82 ], "fq": 120
  },
  "rage": {
    "dict": "anew", "word": "rage", "stem": "rage",
    "avg": [ 2.41, 8.17 ], "std": [ 1.86, 1.40 ], "fq": 16
  },
  "rain": {
    "dict": "anew", "word": "rain", "stem": "rain",
    "avg": [ 5.08, 3.65 ], "std": [ 2.51, 2.35 ], "fq": 70
  },
  "rainbow": {
    "dict": "anew", "word": "rainbow", "stem": "rainbow",
    "avg": [ 8.14, 4.64 ], "std": [ 1.23, 2.88 ], "fq": 4
  },
  "rancid": {
    "dict": "anew", "word": "rancid", "stem": "rancid",
    "avg": [ 4.34, 5.04 ], "std": [ 2.28, 2.27 ], "fq": 0
  },
  "rape": {
    "dict": "anew", "word": "rape", "stem": "rape",
    "avg": [ 1.25, 6.81 ], "std": [ 0.91, 3.17 ], "fq": 5
  },
  "rat": {
    "dict": "anew", "word": "rat", "stem": "rat",
    "avg": [ 3.02, 4.95 ], "std": [ 1.66, 2.36 ], "fq": 6
  },
  "rattl": {
    "dict": "anew", "word": "rattle", "stem": "rattl",
    "avg": [ 5.03, 4.36 ], "std": [ 1.23, 2.18 ], "fq": 5
  },
  "razor": {
    "dict": "anew", "word": "razor", "stem": "razor",
    "avg": [ 4.81, 5.36 ], "std": [ 2.16, 2.44 ], "fq": 15
  },
  "red": {
    "dict": "anew", "word": "red", "stem": "red",
    "avg": [ 6.41, 5.29 ], "std": [ 1.61, 2.04 ], "fq": 197
  },
  "refresh": {
    "dict": "anew", "word": "refreshment", "stem": "refresh",
    "avg": [ 7.44, 4.45 ], "std": [ 1.29, 2.70 ], "fq": 2
  },
  "regret": {
    "dict": "anew", "word": "regretful", "stem": "regret",
    "avg": [ 2.28, 5.74 ], "std": [ 1.42, 2.32 ], "fq": 1
  },
  "reject": {
    "dict": "anew", "word": "rejected", "stem": "reject",
    "avg": [ 1.50, 6.37 ], "std": [ 1.09, 2.56 ], "fq": 33
  },
  "relax": {
    "dict": "anew", "word": "relaxed", "stem": "relax",
    "avg": [ 7.00, 2.39 ], "std": [ 1.77, 2.13 ], "fq": 14
  },
  "repent": {
    "dict": "anew", "word": "repentant", "stem": "repent",
    "avg": [ 5.53, 4.69 ], "std": [ 1.86, 1.98 ], "fq": 1
  },
  "reptil": {
    "dict": "anew", "word": "reptile", "stem": "reptil",
    "avg": [ 4.77, 5.18 ], "std": [ 2.00, 2.19 ], "fq": 0
  },
  "rescu": {
    "dict": "anew", "word": "rescue", "stem": "rescu",
    "avg": [ 7.70, 6.53 ], "std": [ 1.24, 2.56 ], "fq": 15
  },
  "resent": {
    "dict": "anew", "word": "resent", "stem": "resent",
    "avg": [ 3.76, 4.47 ], "std": [ 1.90, 2.12 ], "fq": 8
  },
  "reserv": {
    "dict": "anew", "word": "reserved", "stem": "reserv",
    "avg": [ 4.88, 3.27 ], "std": [ 1.83, 2.05 ], "fq": 27
  },
  "respect": {
    "dict": "anew", "word": "respect", "stem": "respect",
    "avg": [ 7.64, 5.19 ], "std": [ 1.29, 2.39 ], "fq": 125
  },
  "respect": {
    "dict": "anew", "word": "respectful", "stem": "respect",
    "avg": [ 7.22, 4.60 ], "std": [ 1.27, 2.67 ], "fq": 4
  },
  "restaur": {
    "dict": "anew", "word": "restaurant", "stem": "restaur",
    "avg": [ 6.76, 5.41 ], "std": [ 1.85, 2.55 ], "fq": 41
  },
  "reunion": {
    "dict": "anew", "word": "reunion", "stem": "reunion",
    "avg": [ 6.48, 6.34 ], "std": [ 2.45, 2.35 ], "fq": 11
  },
  "rever": {
    "dict": "anew", "word": "reverent", "stem": "rever",
    "avg": [ 5.35, 4.00 ], "std": [ 1.21, 1.60 ], "fq": 3
  },
  "revolt": {
    "dict": "anew", "word": "revolt", "stem": "revolt",
    "avg": [ 4.13, 6.56 ], "std": [ 1.78, 2.34 ], "fq": 8
  },
  "revolv": {
    "dict": "anew", "word": "revolver", "stem": "revolv",
    "avg": [ 4.02, 5.55 ], "std": [ 2.44, 2.39 ], "fq": 14
  },
  "reward": {
    "dict": "anew", "word": "reward", "stem": "reward",
    "avg": [ 7.53, 4.95 ], "std": [ 1.67, 2.62 ], "fq": 15
  },
  "rich": {
    "dict": "anew", "word": "riches", "stem": "rich",
    "avg": [ 7.70, 6.17 ], "std": [ 1.95, 2.70 ], "fq": 2
  },
  "ridicul": {
    "dict": "anew", "word": "ridicule", "stem": "ridicul",
    "avg": [ 3.13, 5.83 ], "std": [ 2.24, 2.73 ], "fq": 5
  },
  "rifl": {
    "dict": "anew", "word": "rifle", "stem": "rifl",
    "avg": [ 4.02, 6.35 ], "std": [ 2.76, 2.04 ], "fq": 63
  },
  "rigid": {
    "dict": "anew", "word": "rigid", "stem": "rigid",
    "avg": [ 3.66, 4.66 ], "std": [ 2.12, 2.47 ], "fq": 24
  },
  "riot": {
    "dict": "anew", "word": "riot", "stem": "riot",
    "avg": [ 2.96, 6.39 ], "std": [ 1.93, 2.63 ], "fq": 7
  },
  "river": {
    "dict": "anew", "word": "river", "stem": "river",
    "avg": [ 6.85, 4.51 ], "std": [ 1.69, 2.42 ], "fq": 165
  },
  "roach": {
    "dict": "anew", "word": "roach", "stem": "roach",
    "avg": [ 2.35, 6.64 ], "std": [ 1.70, 2.64 ], "fq": 2
  },
  "robber": {
    "dict": "anew", "word": "robber", "stem": "robber",
    "avg": [ 2.61, 5.62 ], "std": [ 1.69, 2.72 ], "fq": 2
  },
  "rock": {
    "dict": "anew", "word": "rock", "stem": "rock",
    "avg": [ 5.56, 4.52 ], "std": [ 1.38, 2.37 ], "fq": 75
  },
  "rollercoast": {
    "dict": "anew", "word": "rollercoaster", "stem": "rollercoast",
    "avg": [ 8.02, 8.06 ], "std": [ 1.63, 1.71 ], "fq": 0
  },
  "romant": {
    "dict": "anew", "word": "romantic", "stem": "romant",
    "avg": [ 8.32, 7.59 ], "std": [ 1.00, 2.07 ], "fq": 32
  },
  "rotten": {
    "dict": "anew", "word": "rotten", "stem": "rotten",
    "avg": [ 2.26, 4.53 ], "std": [ 1.37, 2.38 ], "fq": 2
  },
  "rough": {
    "dict": "anew", "word": "rough", "stem": "rough",
    "avg": [ 4.74, 5.33 ], "std": [ 2.00, 2.04 ], "fq": 41
  },
  "rude": {
    "dict": "anew", "word": "rude", "stem": "rude",
    "avg": [ 2.50, 6.31 ], "std": [ 2.11, 2.47 ], "fq": 6
  },
  "runner": {
    "dict": "anew", "word": "runner", "stem": "runner",
    "avg": [ 5.67, 4.76 ], "std": [ 1.91, 2.40 ], "fq": 1
  },
  "rusti": {
    "dict": "anew", "word": "rusty", "stem": "rusti",
    "avg": [ 3.86, 3.77 ], "std": [ 1.47, 2.16 ], "fq": 8
  },
  "sad": {
    "dict": "anew", "word": "sad", "stem": "sad",
    "avg": [ 1.61, 4.13 ], "std": [ 0.95, 2.38 ], "fq": 35
  },
  "safe": {
    "dict": "anew", "word": "safe", "stem": "safe",
    "avg": [ 7.07, 3.86 ], "std": [ 1.90, 2.72 ], "fq": 58
  },
  "sailboat": {
    "dict": "anew", "word": "sailboat", "stem": "sailboat",
    "avg": [ 7.25, 4.88 ], "std": [ 1.71, 2.73 ], "fq": 1
  },
  "saint": {
    "dict": "anew", "word": "saint", "stem": "saint",
    "avg": [ 6.49, 4.49 ], "std": [ 1.70, 1.90 ], "fq": 16
  },
  "salad": {
    "dict": "anew", "word": "salad", "stem": "salad",
    "avg": [ 5.74, 3.81 ], "std": [ 1.62, 2.29 ], "fq": 9
  },
  "salut": {
    "dict": "anew", "word": "salute", "stem": "salut",
    "avg": [ 5.92, 5.31 ], "std": [ 1.57, 2.23 ], "fq": 3
  },
  "sapphir": {
    "dict": "anew", "word": "sapphire", "stem": "sapphir",
    "avg": [ 7.00, 5.00 ], "std": [ 1.88, 2.72 ], "fq": 0
  },
  "satisfi": {
    "dict": "anew", "word": "satisfied", "stem": "satisfi",
    "avg": [ 7.94, 4.94 ], "std": [ 1.19, 2.63 ], "fq": 36
  },
  "save": {
    "dict": "anew", "word": "save", "stem": "save",
    "avg": [ 6.45, 4.95 ], "std": [ 1.93, 2.19 ], "fq": 62
  },
  "savior": {
    "dict": "anew", "word": "savior", "stem": "savior",
    "avg": [ 7.73, 5.80 ], "std": [ 1.56, 3.01 ], "fq": 6
  },
  "scald": {
    "dict": "anew", "word": "scalding", "stem": "scald",
    "avg": [ 2.82, 5.95 ], "std": [ 2.12, 2.55 ], "fq": 1
  },
  "scandal": {
    "dict": "anew", "word": "scandal", "stem": "scandal",
    "avg": [ 3.32, 5.12 ], "std": [ 1.81, 2.22 ], "fq": 8
  },
  "scapegoat": {
    "dict": "anew", "word": "scapegoat", "stem": "scapegoat",
    "avg": [ 3.67, 4.53 ], "std": [ 1.65, 2.13 ], "fq": 1
  },
  "scar": {
    "dict": "anew", "word": "scar", "stem": "scar",
    "avg": [ 3.38, 4.79 ], "std": [ 1.70, 2.11 ], "fq": 10
  },
  "scare": {
    "dict": "anew", "word": "scared", "stem": "scare",
    "avg": [ 2.78, 6.82 ], "std": [ 1.99, 2.03 ], "fq": 21
  },
  "scholar": {
    "dict": "anew", "word": "scholar", "stem": "scholar",
    "avg": [ 7.26, 5.12 ], "std": [ 1.42, 2.46 ], "fq": 15
  },
  "scissor": {
    "dict": "anew", "word": "scissors", "stem": "scissor",
    "avg": [ 5.05, 4.47 ], "std": [ 0.96, 1.76 ], "fq": 1
  },
  "scorch": {
    "dict": "anew", "word": "scorching", "stem": "scorch",
    "avg": [ 3.76, 5.00 ], "std": [ 1.83, 2.74 ], "fq": 0
  },
  "scorn": {
    "dict": "anew", "word": "scorn", "stem": "scorn",
    "avg": [ 2.84, 5.48 ], "std": [ 2.07, 2.52 ], "fq": 4
  },
  "scorn": {
    "dict": "anew", "word": "scornful", "stem": "scorn",
    "avg": [ 3.02, 5.04 ], "std": [ 2.03, 2.56 ], "fq": 5
  },
  "scorpion": {
    "dict": "anew", "word": "scorpion", "stem": "scorpion",
    "avg": [ 3.69, 5.38 ], "std": [ 2.63, 3.08 ], "fq": 0
  },
  "scream": {
    "dict": "anew", "word": "scream", "stem": "scream",
    "avg": [ 3.88, 7.04 ], "std": [ 2.07, 1.96 ], "fq": 13
  },
  "scum": {
    "dict": "anew", "word": "scum", "stem": "scum",
    "avg": [ 2.43, 4.88 ], "std": [ 1.56, 2.36 ], "fq": 0
  },
  "scurvi": {
    "dict": "anew", "word": "scurvy", "stem": "scurvi",
    "avg": [ 3.19, 4.71 ], "std": [ 2.00, 2.72 ], "fq": 1
  },
  "seasick": {
    "dict": "anew", "word": "seasick", "stem": "seasick",
    "avg": [ 2.05, 5.80 ], "std": [ 1.20, 2.88 ], "fq": 0
  },
  "seat": {
    "dict": "anew", "word": "seat", "stem": "seat",
    "avg": [ 4.95, 2.95 ], "std": [ 0.98, 1.72 ], "fq": 54
  },
  "secur": {
    "dict": "anew", "word": "secure", "stem": "secur",
    "avg": [ 7.57, 3.14 ], "std": [ 1.76, 2.47 ], "fq": 30
  },
  "selfish": {
    "dict": "anew", "word": "selfish", "stem": "selfish",
    "avg": [ 2.42, 5.50 ], "std": [ 1.62, 2.62 ], "fq": 8
  },
  "sentiment": {
    "dict": "anew", "word": "sentiment", "stem": "sentiment",
    "avg": [ 5.98, 4.41 ], "std": [ 1.71, 2.30 ], "fq": 23
  },
  "serious": {
    "dict": "anew", "word": "serious", "stem": "serious",
    "avg": [ 5.08, 4.00 ], "std": [ 1.59, 1.87 ], "fq": 116
  },
  "sever": {
    "dict": "anew", "word": "severe", "stem": "sever",
    "avg": [ 3.20, 5.26 ], "std": [ 1.74, 2.36 ], "fq": 39
  },
  "sex": {
    "dict": "anew", "word": "sex", "stem": "sex",
    "avg": [ 8.05, 7.36 ], "std": [ 1.53, 1.91 ], "fq": 84
  },
  "sexi": {
    "dict": "anew", "word": "sexy", "stem": "sexi",
    "avg": [ 8.02, 7.36 ], "std": [ 1.12, 1.91 ], "fq": 2
  },
  "shadow": {
    "dict": "anew", "word": "shadow", "stem": "shadow",
    "avg": [ 4.35, 4.30 ], "std": [ 1.23, 2.26 ], "fq": 36
  },
  "shame": {
    "dict": "anew", "word": "shamed", "stem": "shame",
    "avg": [ 2.50, 4.88 ], "std": [ 1.34, 2.27 ], "fq": 1
  },
  "shark": {
    "dict": "anew", "word": "shark", "stem": "shark",
    "avg": [ 3.65, 7.16 ], "std": [ 2.47, 1.96 ], "fq": 0
  },
  "shelter": {
    "dict": "anew", "word": "sheltered", "stem": "shelter",
    "avg": [ 5.75, 4.28 ], "std": [ 1.92, 1.77 ], "fq": 4
  },
  "ship": {
    "dict": "anew", "word": "ship", "stem": "ship",
    "avg": [ 5.55, 4.38 ], "std": [ 1.40, 2.29 ], "fq": 83
  },
  "shotgun": {
    "dict": "anew", "word": "shotgun", "stem": "shotgun",
    "avg": [ 4.37, 6.27 ], "std": [ 2.75, 1.94 ], "fq": 8
  },
  "shriek": {
    "dict": "anew", "word": "shriek", "stem": "shriek",
    "avg": [ 3.93, 5.36 ], "std": [ 2.22, 2.91 ], "fq": 5
  },
  "shi": {
    "dict": "anew", "word": "shy", "stem": "shi",
    "avg": [ 4.64, 3.77 ], "std": [ 1.83, 2.29 ], "fq": 13
  },
  "sick": {
    "dict": "anew", "word": "sick", "stem": "sick",
    "avg": [ 1.90, 4.29 ], "std": [ 1.14, 2.45 ], "fq": 51
  },
  "sick": {
    "dict": "anew", "word": "sickness", "stem": "sick",
    "avg": [ 2.25, 5.61 ], "std": [ 1.71, 2.67 ], "fq": 6
  },
  "silk": {
    "dict": "anew", "word": "silk", "stem": "silk",
    "avg": [ 6.90, 3.71 ], "std": [ 1.27, 2.51 ], "fq": 12
  },
  "silli": {
    "dict": "anew", "word": "silly", "stem": "silli",
    "avg": [ 7.41, 5.88 ], "std": [ 1.80, 2.38 ], "fq": 15
  },
  "sin": {
    "dict": "anew", "word": "sin", "stem": "sin",
    "avg": [ 2.80, 5.78 ], "std": [ 1.67, 2.21 ], "fq": 53
  },
  "sin": {
    "dict": "anew", "word": "sinful", "stem": "sin",
    "avg": [ 2.93, 6.29 ], "std": [ 2.15, 2.43 ], "fq": 3
  },
  "sissi": {
    "dict": "anew", "word": "sissy", "stem": "sissi",
    "avg": [ 3.14, 5.17 ], "std": [ 1.96, 2.57 ], "fq": 0
  },
  "skeptic": {
    "dict": "anew", "word": "skeptical", "stem": "skeptic",
    "avg": [ 4.52, 4.91 ], "std": [ 1.63, 1.92 ], "fq": 7
  },
  "skijump": {
    "dict": "anew", "word": "skijump", "stem": "skijump",
    "avg": [ 7.06, 7.06 ], "std": [ 1.73, 2.10 ], "fq": 0
  },
  "skull": {
    "dict": "anew", "word": "skull", "stem": "skull",
    "avg": [ 4.27, 4.75 ], "std": [ 1.83, 1.85 ], "fq": 3
  },
  "sky": {
    "dict": "anew", "word": "sky", "stem": "sky",
    "avg": [ 7.37, 4.27 ], "std": [ 1.40, 2.17 ], "fq": 58
  },
  "skyscrap": {
    "dict": "anew", "word": "skyscraper", "stem": "skyscrap",
    "avg": [ 5.88, 5.71 ], "std": [ 1.87, 2.17 ], "fq": 2
  },
  "slap": {
    "dict": "anew", "word": "slap", "stem": "slap",
    "avg": [ 2.95, 6.46 ], "std": [ 1.79, 2.58 ], "fq": 2
  },
  "slaughter": {
    "dict": "anew", "word": "slaughter", "stem": "slaughter",
    "avg": [ 1.64, 6.77 ], "std": [ 1.18, 2.42 ], "fq": 10
  },
  "slave": {
    "dict": "anew", "word": "slave", "stem": "slave",
    "avg": [ 1.84, 6.21 ], "std": [ 1.13, 2.93 ], "fq": 30
  },
  "sleep": {
    "dict": "anew", "word": "sleep", "stem": "sleep",
    "avg": [ 7.20, 2.80 ], "std": [ 1.77, 2.66 ], "fq": 65
  },
  "slime": {
    "dict": "anew", "word": "slime", "stem": "slime",
    "avg": [ 2.68, 5.36 ], "std": [ 1.66, 2.63 ], "fq": 1
  },
  "slow": {
    "dict": "anew", "word": "slow", "stem": "slow",
    "avg": [ 3.93, 3.39 ], "std": [ 1.60, 2.22 ], "fq": 60
  },
  "slum": {
    "dict": "anew", "word": "slum", "stem": "slum",
    "avg": [ 2.39, 4.78 ], "std": [ 1.25, 2.52 ], "fq": 8
  },
  "slush": {
    "dict": "anew", "word": "slush", "stem": "slush",
    "avg": [ 4.66, 3.73 ], "std": [ 1.88, 2.23 ], "fq": 0
  },
  "smallpox": {
    "dict": "anew", "word": "smallpox", "stem": "smallpox",
    "avg": [ 2.52, 5.58 ], "std": [ 2.08, 2.13 ], "fq": 2
  },
  "smooth": {
    "dict": "anew", "word": "smooth", "stem": "smooth",
    "avg": [ 6.58, 4.91 ], "std": [ 1.78, 2.57 ], "fq": 42
  },
  "snake": {
    "dict": "anew", "word": "snake", "stem": "snake",
    "avg": [ 3.31, 6.82 ], "std": [ 2.20, 2.10 ], "fq": 44
  },
  "snob": {
    "dict": "anew", "word": "snob", "stem": "snob",
    "avg": [ 3.36, 5.65 ], "std": [ 1.81, 2.36 ], "fq": 1
  },
  "snow": {
    "dict": "anew", "word": "snow", "stem": "snow",
    "avg": [ 7.08, 5.75 ], "std": [ 1.83, 2.47 ], "fq": 59
  },
  "snuggl": {
    "dict": "anew", "word": "snuggle", "stem": "snuggl",
    "avg": [ 7.92, 4.16 ], "std": [ 1.24, 2.80 ], "fq": 4
  },
  "social": {
    "dict": "anew", "word": "social", "stem": "social",
    "avg": [ 6.88, 4.98 ], "std": [ 1.82, 2.59 ], "fq": 380
  },
  "soft": {
    "dict": "anew", "word": "soft", "stem": "soft",
    "avg": [ 7.12, 4.63 ], "std": [ 1.34, 2.61 ], "fq": 61
  },
  "solemn": {
    "dict": "anew", "word": "solemn", "stem": "solemn",
    "avg": [ 4.32, 3.56 ], "std": [ 1.51, 1.95 ], "fq": 12
  },
  "song": {
    "dict": "anew", "word": "song", "stem": "song",
    "avg": [ 7.10, 6.07 ], "std": [ 1.97, 2.42 ], "fq": 70
  },
  "sooth": {
    "dict": "anew", "word": "soothe", "stem": "sooth",
    "avg": [ 7.30, 4.40 ], "std": [ 1.85, 3.08 ], "fq": 2
  },
  "sour": {
    "dict": "anew", "word": "sour", "stem": "sour",
    "avg": [ 3.93, 5.10 ], "std": [ 1.98, 1.95 ], "fq": 3
  },
  "space": {
    "dict": "anew", "word": "space", "stem": "space",
    "avg": [ 6.78, 5.14 ], "std": [ 1.66, 2.54 ], "fq": 184
  },
  "spank": {
    "dict": "anew", "word": "spanking", "stem": "spank",
    "avg": [ 3.55, 5.41 ], "std": [ 2.54, 2.73 ], "fq": 0
  },
  "sphere": {
    "dict": "anew", "word": "sphere", "stem": "sphere",
    "avg": [ 5.33, 3.88 ], "std": [ 0.87, 1.99 ], "fq": 22
  },
  "spider": {
    "dict": "anew", "word": "spider", "stem": "spider",
    "avg": [ 3.33, 5.71 ], "std": [ 1.72, 2.21 ], "fq": 2
  },
  "spirit": {
    "dict": "anew", "word": "spirit", "stem": "spirit",
    "avg": [ 7.00, 5.56 ], "std": [ 1.32, 2.62 ], "fq": 182
  },
  "spous": {
    "dict": "anew", "word": "spouse", "stem": "spous",
    "avg": [ 7.58, 5.21 ], "std": [ 1.48, 2.75 ], "fq": 3
  },
  "spray": {
    "dict": "anew", "word": "spray", "stem": "spray",
    "avg": [ 5.45, 4.14 ], "std": [ 1.63, 2.28 ], "fq": 16
  },
  "spring": {
    "dict": "anew", "word": "spring", "stem": "spring",
    "avg": [ 7.76, 5.67 ], "std": [ 1.51, 2.51 ], "fq": 127
  },
  "squar": {
    "dict": "anew", "word": "square", "stem": "squar",
    "avg": [ 4.74, 3.18 ], "std": [ 1.02, 1.76 ], "fq": 143
  },
  "stagnant": {
    "dict": "anew", "word": "stagnant", "stem": "stagnant",
    "avg": [ 4.15, 3.93 ], "std": [ 1.57, 1.94 ], "fq": 5
  },
  "star": {
    "dict": "anew", "word": "star", "stem": "star",
    "avg": [ 7.27, 5.83 ], "std": [ 1.66, 2.44 ], "fq": 25
  },
  "startl": {
    "dict": "anew", "word": "startled", "stem": "startl",
    "avg": [ 4.50, 6.93 ], "std": [ 1.67, 2.24 ], "fq": 21
  },
  "starv": {
    "dict": "anew", "word": "starving", "stem": "starv",
    "avg": [ 2.39, 5.61 ], "std": [ 1.82, 2.53 ], "fq": 6
  },
  "statu": {
    "dict": "anew", "word": "statue", "stem": "statu",
    "avg": [ 5.17, 3.46 ], "std": [ 0.70, 1.72 ], "fq": 17
  },
  "stench": {
    "dict": "anew", "word": "stench", "stem": "stench",
    "avg": [ 2.19, 4.36 ], "std": [ 1.37, 2.46 ], "fq": 1
  },
  "stiff": {
    "dict": "anew", "word": "stiff", "stem": "stiff",
    "avg": [ 4.68, 4.02 ], "std": [ 1.97, 2.41 ], "fq": 21
  },
  "stink": {
    "dict": "anew", "word": "stink", "stem": "stink",
    "avg": [ 3.00, 4.26 ], "std": [ 1.79, 2.10 ], "fq": 3
  },
  "stomach": {
    "dict": "anew", "word": "stomach", "stem": "stomach",
    "avg": [ 4.82, 3.93 ], "std": [ 2.06, 2.49 ], "fq": 37
  },
  "stool": {
    "dict": "anew", "word": "stool", "stem": "stool",
    "avg": [ 4.56, 4.00 ], "std": [ 1.72, 2.14 ], "fq": 8
  },
  "storm": {
    "dict": "anew", "word": "storm", "stem": "storm",
    "avg": [ 4.95, 5.71 ], "std": [ 2.22, 2.34 ], "fq": 26
  },
  "stove": {
    "dict": "anew", "word": "stove", "stem": "stove",
    "avg": [ 4.98, 4.51 ], "std": [ 1.69, 2.14 ], "fq": 15
  },
  "street": {
    "dict": "anew", "word": "street", "stem": "street",
    "avg": [ 5.22, 3.39 ], "std": [ 0.72, 1.87 ], "fq": 244
  },
  "stress": {
    "dict": "anew", "word": "stress", "stem": "stress",
    "avg": [ 2.09, 7.45 ], "std": [ 1.41, 2.38 ], "fq": 107
  },
  "strong": {
    "dict": "anew", "word": "strong", "stem": "strong",
    "avg": [ 7.11, 5.92 ], "std": [ 1.48, 2.28 ], "fq": 202
  },
  "stupid": {
    "dict": "anew", "word": "stupid", "stem": "stupid",
    "avg": [ 2.31, 4.72 ], "std": [ 1.37, 2.71 ], "fq": 24
  },
  "subdu": {
    "dict": "anew", "word": "subdued", "stem": "subdu",
    "avg": [ 4.67, 2.90 ], "std": [ 1.31, 1.81 ], "fq": 8
  },
  "success": {
    "dict": "anew", "word": "success", "stem": "success",
    "avg": [ 8.29, 6.11 ], "std": [ 0.93, 2.65 ], "fq": 93
  },
  "suffoc": {
    "dict": "anew", "word": "suffocate", "stem": "suffoc",
    "avg": [ 1.56, 6.03 ], "std": [ 0.96, 3.19 ], "fq": 1
  },
  "sugar": {
    "dict": "anew", "word": "sugar", "stem": "sugar",
    "avg": [ 6.74, 5.64 ], "std": [ 1.73, 2.18 ], "fq": 34
  },
  "suicid": {
    "dict": "anew", "word": "suicide", "stem": "suicid",
    "avg": [ 1.25, 5.73 ], "std": [ 0.69, 3.14 ], "fq": 17
  },
  "sun": {
    "dict": "anew", "word": "sun", "stem": "sun",
    "avg": [ 7.55, 5.04 ], "std": [ 1.85, 2.66 ], "fq": 112
  },
  "sunlight": {
    "dict": "anew", "word": "sunlight", "stem": "sunlight",
    "avg": [ 7.76, 6.10 ], "std": [ 1.43, 2.30 ], "fq": 17
  },
  "sunris": {
    "dict": "anew", "word": "sunrise", "stem": "sunris",
    "avg": [ 7.86, 5.06 ], "std": [ 1.35, 3.05 ], "fq": 10
  },
  "sunset": {
    "dict": "anew", "word": "sunset", "stem": "sunset",
    "avg": [ 7.68, 4.20 ], "std": [ 1.72, 2.99 ], "fq": 14
  },
  "surgeri": {
    "dict": "anew", "word": "surgery", "stem": "surgeri",
    "avg": [ 2.86, 6.35 ], "std": [ 2.19, 2.32 ], "fq": 6
  },
  "surpris": {
    "dict": "anew", "word": "surprised", "stem": "surpris",
    "avg": [ 7.47, 7.47 ], "std": [ 1.56, 2.09 ], "fq": 58
  },
  "suspici": {
    "dict": "anew", "word": "suspicious", "stem": "suspici",
    "avg": [ 3.76, 6.25 ], "std": [ 1.42, 1.59 ], "fq": 13
  },
  "swamp": {
    "dict": "anew", "word": "swamp", "stem": "swamp",
    "avg": [ 5.14, 4.86 ], "std": [ 2.24, 2.36 ], "fq": 5
  },
  "sweetheart": {
    "dict": "anew", "word": "sweetheart", "stem": "sweetheart",
    "avg": [ 8.42, 5.50 ], "std": [ 0.83, 2.73 ], "fq": 9
  },
  "swift": {
    "dict": "anew", "word": "swift", "stem": "swift",
    "avg": [ 6.46, 5.39 ], "std": [ 1.76, 2.53 ], "fq": 32
  },
  "swimmer": {
    "dict": "anew", "word": "swimmer", "stem": "swimmer",
    "avg": [ 6.54, 4.82 ], "std": [ 1.64, 2.49 ], "fq": 0
  },
  "syphili": {
    "dict": "anew", "word": "syphilis", "stem": "syphili",
    "avg": [ 1.68, 5.69 ], "std": [ 1.23, 3.25 ], "fq": 0
  },
  "tabl": {
    "dict": "anew", "word": "table", "stem": "tabl",
    "avg": [ 5.22, 2.92 ], "std": [ 0.72, 2.16 ], "fq": 198
  },
  "talent": {
    "dict": "anew", "word": "talent", "stem": "talent",
    "avg": [ 7.56, 6.27 ], "std": [ 1.25, 1.80 ], "fq": 40
  },
  "tamper": {
    "dict": "anew", "word": "tamper", "stem": "tamper",
    "avg": [ 4.10, 4.95 ], "std": [ 1.88, 2.01 ], "fq": 1
  },
  "tank": {
    "dict": "anew", "word": "tank", "stem": "tank",
    "avg": [ 5.16, 4.88 ], "std": [ 1.87, 1.86 ], "fq": 12
  },
  "tast": {
    "dict": "anew", "word": "taste", "stem": "tast",
    "avg": [ 6.66, 5.22 ], "std": [ 1.57, 2.38 ], "fq": 59
  },
  "taxi": {
    "dict": "anew", "word": "taxi", "stem": "taxi",
    "avg": [ 5.00, 3.41 ], "std": [ 1.96, 2.14 ], "fq": 16
  },
  "teacher": {
    "dict": "anew", "word": "teacher", "stem": "teacher",
    "avg": [ 5.68, 4.05 ], "std": [ 2.12, 2.61 ], "fq": 80
  },
  "teas": {
    "dict": "anew", "word": "tease", "stem": "teas",
    "avg": [ 4.84, 5.87 ], "std": [ 2.51, 2.56 ], "fq": 6
  },
  "tender": {
    "dict": "anew", "word": "tender", "stem": "tender",
    "avg": [ 6.93, 4.88 ], "std": [ 1.28, 2.30 ], "fq": 11
  },
  "tenni": {
    "dict": "anew", "word": "tennis", "stem": "tenni",
    "avg": [ 6.02, 4.61 ], "std": [ 1.97, 2.60 ], "fq": 15
  },
  "tens": {
    "dict": "anew", "word": "tense", "stem": "tens",
    "avg": [ 3.56, 6.53 ], "std": [ 1.36, 2.10 ], "fq": 15
  },
  "termit": {
    "dict": "anew", "word": "termite", "stem": "termit",
    "avg": [ 3.58, 5.39 ], "std": [ 2.08, 2.43 ], "fq": 0
  },
  "terribl": {
    "dict": "anew", "word": "terrible", "stem": "terribl",
    "avg": [ 1.93, 6.27 ], "std": [ 1.44, 2.44 ], "fq": 45
  },
  "terrif": {
    "dict": "anew", "word": "terrific", "stem": "terrif",
    "avg": [ 8.16, 6.23 ], "std": [ 1.12, 2.73 ], "fq": 5
  },
  "terrifi": {
    "dict": "anew", "word": "terrified", "stem": "terrifi",
    "avg": [ 1.72, 7.86 ], "std": [ 1.14, 2.27 ], "fq": 7
  },
  "terrorist": {
    "dict": "anew", "word": "terrorist", "stem": "terrorist",
    "avg": [ 1.69, 7.27 ], "std": [ 1.42, 2.38 ], "fq": 0
  },
  "thank": {
    "dict": "anew", "word": "thankful", "stem": "thank",
    "avg": [ 6.89, 4.34 ], "std": [ 2.29, 2.31 ], "fq": 6
  },
  "theori": {
    "dict": "anew", "word": "theory", "stem": "theori",
    "avg": [ 5.30, 4.62 ], "std": [ 1.49, 1.94 ], "fq": 129
  },
  "thermomet": {
    "dict": "anew", "word": "thermometer", "stem": "thermomet",
    "avg": [ 4.73, 3.79 ], "std": [ 1.05, 2.02 ], "fq": 0
  },
  "thief": {
    "dict": "anew", "word": "thief", "stem": "thief",
    "avg": [ 2.13, 6.89 ], "std": [ 1.69, 2.13 ], "fq": 8
  },
  "thorn": {
    "dict": "anew", "word": "thorn", "stem": "thorn",
    "avg": [ 3.64, 5.14 ], "std": [ 1.76, 2.14 ], "fq": 3
  },
  "thought": {
    "dict": "anew", "word": "thought", "stem": "thought",
    "avg": [ 6.39, 4.83 ], "std": [ 1.58, 2.46 ], "fq": 515
  },
  "thought": {
    "dict": "anew", "word": "thoughtful", "stem": "thought",
    "avg": [ 7.65, 5.72 ], "std": [ 1.03, 2.30 ], "fq": 11
  },
  "thrill": {
    "dict": "anew", "word": "thrill", "stem": "thrill",
    "avg": [ 8.05, 8.02 ], "std": [ 1.48, 1.65 ], "fq": 5
  },
  "tidi": {
    "dict": "anew", "word": "tidy", "stem": "tidi",
    "avg": [ 6.30, 3.98 ], "std": [ 1.56, 2.22 ], "fq": 1
  },
  "time": {
    "dict": "anew", "word": "time", "stem": "time",
    "avg": [ 5.31, 4.64 ], "std": [ 2.02, 2.75 ], "fq": 1599
  },
  "timid": {
    "dict": "anew", "word": "timid", "stem": "timid",
    "avg": [ 3.86, 4.11 ], "std": [ 1.55, 2.09 ], "fq": 5
  },
  "tobacco": {
    "dict": "anew", "word": "tobacco", "stem": "tobacco",
    "avg": [ 3.28, 4.83 ], "std": [ 2.16, 2.90 ], "fq": 19
  },
  "tomb": {
    "dict": "anew", "word": "tomb", "stem": "tomb",
    "avg": [ 2.94, 4.73 ], "std": [ 1.88, 2.72 ], "fq": 11
  },
  "tool": {
    "dict": "anew", "word": "tool", "stem": "tool",
    "avg": [ 5.19, 4.33 ], "std": [ 1.27, 1.78 ], "fq": 40
  },
  "toothach": {
    "dict": "anew", "word": "toothache", "stem": "toothach",
    "avg": [ 1.98, 5.55 ], "std": [ 1.15, 2.51 ], "fq": 0
  },
  "tornado": {
    "dict": "anew", "word": "tornado", "stem": "tornado",
    "avg": [ 2.55, 6.83 ], "std": [ 1.78, 2.49 ], "fq": 1
  },
  "tortur": {
    "dict": "anew", "word": "torture", "stem": "tortur",
    "avg": [ 1.56, 6.10 ], "std": [ 0.79, 2.77 ], "fq": 3
  },
  "tower": {
    "dict": "anew", "word": "tower", "stem": "tower",
    "avg": [ 5.46, 3.95 ], "std": [ 1.75, 2.28 ], "fq": 13
  },
  "toxic": {
    "dict": "anew", "word": "toxic", "stem": "toxic",
    "avg": [ 2.10, 6.40 ], "std": [ 1.48, 2.41 ], "fq": 3
  },
  "toy": {
    "dict": "anew", "word": "toy", "stem": "toy",
    "avg": [ 7.00, 5.11 ], "std": [ 2.01, 2.84 ], "fq": 4
  },
  "tragedi": {
    "dict": "anew", "word": "tragedy", "stem": "tragedi",
    "avg": [ 1.78, 6.24 ], "std": [ 1.31, 2.64 ], "fq": 49
  },
  "traitor": {
    "dict": "anew", "word": "traitor", "stem": "traitor",
    "avg": [ 2.22, 5.78 ], "std": [ 1.69, 2.47 ], "fq": 2
  },
  "trash": {
    "dict": "anew", "word": "trash", "stem": "trash",
    "avg": [ 2.67, 4.16 ], "std": [ 1.45, 2.16 ], "fq": 2
  },
  "trauma": {
    "dict": "anew", "word": "trauma", "stem": "trauma",
    "avg": [ 2.10, 6.33 ], "std": [ 1.49, 2.45 ], "fq": 1
  },
  "travel": {
    "dict": "anew", "word": "travel", "stem": "travel",
    "avg": [ 7.10, 6.21 ], "std": [ 2.00, 2.51 ], "fq": 61
  },
  "treasur": {
    "dict": "anew", "word": "treasure", "stem": "treasur",
    "avg": [ 8.27, 6.75 ], "std": [ 0.90, 2.30 ], "fq": 4
  },
  "treat": {
    "dict": "anew", "word": "treat", "stem": "treat",
    "avg": [ 7.36, 5.62 ], "std": [ 1.38, 2.25 ], "fq": 26
  },
  "tree": {
    "dict": "anew", "word": "tree", "stem": "tree",
    "avg": [ 6.32, 3.42 ], "std": [ 1.56, 2.21 ], "fq": 59
  },
  "triumph": {
    "dict": "anew", "word": "triumph", "stem": "triumph",
    "avg": [ 7.80, 5.78 ], "std": [ 1.83, 2.60 ], "fq": 22
  },
  "triumphant": {
    "dict": "anew", "word": "triumphant", "stem": "triumphant",
    "avg": [ 8.82, 6.78 ], "std": [ 0.73, 2.58 ], "fq": 5
  },
  "trophi": {
    "dict": "anew", "word": "trophy", "stem": "trophi",
    "avg": [ 7.78, 5.39 ], "std": [ 1.22, 2.44 ], "fq": 8
  },
  "troubl": {
    "dict": "anew", "word": "trouble", "stem": "troubl",
    "avg": [ 3.03, 6.85 ], "std": [ 2.09, 2.03 ], "fq": 134
  },
  "troubl": {
    "dict": "anew", "word": "troubled", "stem": "troubl",
    "avg": [ 2.17, 5.94 ], "std": [ 1.21, 2.36 ], "fq": 31
  },
  "truck": {
    "dict": "anew", "word": "truck", "stem": "truck",
    "avg": [ 5.47, 4.84 ], "std": [ 1.88, 2.17 ], "fq": 57
  },
  "trumpet": {
    "dict": "anew", "word": "trumpet", "stem": "trumpet",
    "avg": [ 5.75, 4.97 ], "std": [ 1.38, 2.13 ], "fq": 7
  },
  "trunk": {
    "dict": "anew", "word": "trunk", "stem": "trunk",
    "avg": [ 5.09, 4.18 ], "std": [ 1.57, 2.19 ], "fq": 8
  },
  "trust": {
    "dict": "anew", "word": "trust", "stem": "trust",
    "avg": [ 6.68, 5.30 ], "std": [ 2.71, 2.66 ], "fq": 52
  },
  "truth": {
    "dict": "anew", "word": "truth", "stem": "truth",
    "avg": [ 7.80, 5.00 ], "std": [ 1.29, 2.77 ], "fq": 126
  },
  "tumor": {
    "dict": "anew", "word": "tumor", "stem": "tumor",
    "avg": [ 2.36, 6.51 ], "std": [ 2.04, 2.85 ], "fq": 17
  },
  "tune": {
    "dict": "anew", "word": "tune", "stem": "tune",
    "avg": [ 6.93, 4.71 ], "std": [ 1.47, 2.09 ], "fq": 10
  },
  "twilight": {
    "dict": "anew", "word": "twilight", "stem": "twilight",
    "avg": [ 7.23, 4.70 ], "std": [ 1.80, 2.41 ], "fq": 4
  },
  "ugli": {
    "dict": "anew", "word": "ugly", "stem": "ugli",
    "avg": [ 2.43, 5.38 ], "std": [ 1.27, 2.23 ], "fq": 21
  },
  "ulcer": {
    "dict": "anew", "word": "ulcer", "stem": "ulcer",
    "avg": [ 1.78, 6.12 ], "std": [ 1.17, 2.68 ], "fq": 5
  },
  "umbrella": {
    "dict": "anew", "word": "umbrella", "stem": "umbrella",
    "avg": [ 5.16, 3.68 ], "std": [ 1.57, 1.99 ], "fq": 8
  },
  "unfaith": {
    "dict": "anew", "word": "unfaithful", "stem": "unfaith",
    "avg": [ 2.05, 6.20 ], "std": [ 1.55, 2.70 ], "fq": 1
  },
  "unhappi": {
    "dict": "anew", "word": "unhappy", "stem": "unhappi",
    "avg": [ 1.57, 4.18 ], "std": [ 0.96, 2.50 ], "fq": 26
  },
  "unit": {
    "dict": "anew", "word": "unit", "stem": "unit",
    "avg": [ 5.59, 3.75 ], "std": [ 1.87, 2.49 ], "fq": 103
  },
  "untroubl": {
    "dict": "anew", "word": "untroubled", "stem": "untroubl",
    "avg": [ 7.62, 3.89 ], "std": [ 1.41, 2.54 ], "fq": 0
  },
  "upset": {
    "dict": "anew", "word": "upset", "stem": "upset",
    "avg": [ 2.00, 5.86 ], "std": [ 1.18, 2.40 ], "fq": 14
  },
  "urin": {
    "dict": "anew", "word": "urine", "stem": "urin",
    "avg": [ 3.25, 4.20 ], "std": [ 1.71, 2.18 ], "fq": 1
  },
  "use": {
    "dict": "anew", "word": "useful", "stem": "use",
    "avg": [ 7.14, 4.26 ], "std": [ 1.60, 2.47 ], "fq": 58
  },
  "useless": {
    "dict": "anew", "word": "useless", "stem": "useless",
    "avg": [ 2.13, 4.87 ], "std": [ 1.42, 2.58 ], "fq": 17
  },
  "utensil": {
    "dict": "anew", "word": "utensil", "stem": "utensil",
    "avg": [ 5.14, 3.57 ], "std": [ 1.39, 1.98 ], "fq": 0
  },
  "vacat": {
    "dict": "anew", "word": "vacation", "stem": "vacat",
    "avg": [ 8.16, 5.64 ], "std": [ 1.36, 2.99 ], "fq": 47
  },
  "vagina": {
    "dict": "anew", "word": "vagina", "stem": "vagina",
    "avg": [ 6.14, 5.55 ], "std": [ 1.77, 2.55 ], "fq": 10
  },
  "valentin": {
    "dict": "anew", "word": "valentine", "stem": "valentin",
    "avg": [ 8.11, 6.06 ], "std": [ 1.35, 2.91 ], "fq": 2
  },
  "vampir": {
    "dict": "anew", "word": "vampire", "stem": "vampir",
    "avg": [ 4.26, 6.37 ], "std": [ 1.86, 2.35 ], "fq": 1
  },
  "vandal": {
    "dict": "anew", "word": "vandal", "stem": "vandal",
    "avg": [ 2.71, 6.40 ], "std": [ 1.91, 1.88 ], "fq": 1
  },
  "vaniti": {
    "dict": "anew", "word": "vanity", "stem": "vaniti",
    "avg": [ 4.30, 4.98 ], "std": [ 1.91, 2.31 ], "fq": 7
  },
  "vehicl": {
    "dict": "anew", "word": "vehicle", "stem": "vehicl",
    "avg": [ 6.27, 4.63 ], "std": [ 2.34, 2.81 ], "fq": 35
  },
  "venom": {
    "dict": "anew", "word": "venom", "stem": "venom",
    "avg": [ 2.68, 6.08 ], "std": [ 1.81, 2.44 ], "fq": 2
  },
  "vest": {
    "dict": "anew", "word": "vest", "stem": "vest",
    "avg": [ 5.25, 3.95 ], "std": [ 1.33, 2.09 ], "fq": 4
  },
  "victim": {
    "dict": "anew", "word": "victim", "stem": "victim",
    "avg": [ 2.18, 6.06 ], "std": [ 1.48, 2.32 ], "fq": 27
  },
  "victori": {
    "dict": "anew", "word": "victory", "stem": "victori",
    "avg": [ 8.32, 6.63 ], "std": [ 1.16, 2.84 ], "fq": 61
  },
  "vigor": {
    "dict": "anew", "word": "vigorous", "stem": "vigor",
    "avg": [ 6.79, 5.90 ], "std": [ 1.54, 2.66 ], "fq": 29
  },
  "villag": {
    "dict": "anew", "word": "village", "stem": "villag",
    "avg": [ 5.92, 4.08 ], "std": [ 1.34, 1.87 ], "fq": 72
  },
  "violent": {
    "dict": "anew", "word": "violent", "stem": "violent",
    "avg": [ 2.29, 6.89 ], "std": [ 1.78, 2.47 ], "fq": 33
  },
  "violin": {
    "dict": "anew", "word": "violin", "stem": "violin",
    "avg": [ 5.43, 3.49 ], "std": [ 1.98, 2.26 ], "fq": 11
  },
  "virgin": {
    "dict": "anew", "word": "virgin", "stem": "virgin",
    "avg": [ 6.45, 5.51 ], "std": [ 1.76, 2.06 ], "fq": 35
  },
  "virtu": {
    "dict": "anew", "word": "virtue", "stem": "virtu",
    "avg": [ 6.22, 4.52 ], "std": [ 2.06, 2.52 ], "fq": 30
  },
  "vision": {
    "dict": "anew", "word": "vision", "stem": "vision",
    "avg": [ 6.62, 4.66 ], "std": [ 1.84, 2.43 ], "fq": 56
  },
  "volcano": {
    "dict": "anew", "word": "volcano", "stem": "volcano",
    "avg": [ 4.84, 6.33 ], "std": [ 2.14, 2.21 ], "fq": 2
  },
  "vomit": {
    "dict": "anew", "word": "vomit", "stem": "vomit",
    "avg": [ 2.06, 5.75 ], "std": [ 1.57, 2.84 ], "fq": 3
  },
  "voyag": {
    "dict": "anew", "word": "voyage", "stem": "voyag",
    "avg": [ 6.25, 5.55 ], "std": [ 1.91, 2.23 ], "fq": 17
  },
  "wagon": {
    "dict": "anew", "word": "wagon", "stem": "wagon",
    "avg": [ 5.37, 3.98 ], "std": [ 0.97, 2.04 ], "fq": 55
  },
  "war": {
    "dict": "anew", "word": "war", "stem": "war",
    "avg": [ 2.08, 7.49 ], "std": [ 1.91, 2.16 ], "fq": 464
  },
  "warmth": {
    "dict": "anew", "word": "warmth", "stem": "warmth",
    "avg": [ 7.41, 3.73 ], "std": [ 1.81, 2.40 ], "fq": 28
  },
  "wasp": {
    "dict": "anew", "word": "wasp", "stem": "wasp",
    "avg": [ 3.37, 5.50 ], "std": [ 1.63, 2.17 ], "fq": 2
  },
  "wast": {
    "dict": "anew", "word": "waste", "stem": "wast",
    "avg": [ 2.93, 4.14 ], "std": [ 1.76, 2.30 ], "fq": 35
  },
  "watch": {
    "dict": "anew", "word": "watch", "stem": "watch",
    "avg": [ 5.78, 4.10 ], "std": [ 1.51, 2.12 ], "fq": 81
  },
  "water": {
    "dict": "anew", "word": "water", "stem": "water",
    "avg": [ 6.61, 4.97 ], "std": [ 1.78, 2.49 ], "fq": 442
  },
  "waterfal": {
    "dict": "anew", "word": "waterfall", "stem": "waterfal",
    "avg": [ 7.88, 5.37 ], "std": [ 1.03, 2.84 ], "fq": 2
  },
  "wealthi": {
    "dict": "anew", "word": "wealthy", "stem": "wealthi",
    "avg": [ 7.70, 5.80 ], "std": [ 1.34, 2.73 ], "fq": 12
  },
  "weapon": {
    "dict": "anew", "word": "weapon", "stem": "weapon",
    "avg": [ 3.97, 6.03 ], "std": [ 1.92, 1.89 ], "fq": 42
  },
  "weari": {
    "dict": "anew", "word": "weary", "stem": "weari",
    "avg": [ 3.79, 3.81 ], "std": [ 2.12, 2.29 ], "fq": 17
  },
  "wed": {
    "dict": "anew", "word": "wedding", "stem": "wed",
    "avg": [ 7.82, 5.97 ], "std": [ 1.56, 2.85 ], "fq": 32
  },
  "whistl": {
    "dict": "anew", "word": "whistle", "stem": "whistl",
    "avg": [ 5.81, 4.69 ], "std": [ 1.21, 1.99 ], "fq": 4
  },
  "white": {
    "dict": "anew", "word": "white", "stem": "white",
    "avg": [ 6.47, 4.37 ], "std": [ 1.59, 2.14 ], "fq": 365
  },
  "whore": {
    "dict": "anew", "word": "whore", "stem": "whore",
    "avg": [ 2.30, 5.85 ], "std": [ 2.11, 2.93 ], "fq": 2
  },
  "wick": {
    "dict": "anew", "word": "wicked", "stem": "wick",
    "avg": [ 2.96, 6.09 ], "std": [ 2.37, 2.44 ], "fq": 9
  },
  "wife": {
    "dict": "anew", "word": "wife", "stem": "wife",
    "avg": [ 6.33, 4.93 ], "std": [ 1.97, 2.22 ], "fq": 228
  },
  "win": {
    "dict": "anew", "word": "win", "stem": "win",
    "avg": [ 8.38, 7.72 ], "std": [ 0.92, 2.16 ], "fq": 55
  },
  "windmil": {
    "dict": "anew", "word": "windmill", "stem": "windmil",
    "avg": [ 5.60, 3.74 ], "std": [ 1.65, 2.13 ], "fq": 1
  },
  "window": {
    "dict": "anew", "word": "window", "stem": "window",
    "avg": [ 5.91, 3.97 ], "std": [ 1.38, 2.01 ], "fq": 119
  },
  "wine": {
    "dict": "anew", "word": "wine", "stem": "wine",
    "avg": [ 5.95, 4.78 ], "std": [ 2.19, 2.34 ], "fq": 72
  },
  "wink": {
    "dict": "anew", "word": "wink", "stem": "wink",
    "avg": [ 6.93, 5.44 ], "std": [ 1.83, 2.68 ], "fq": 7
  },
  "wise": {
    "dict": "anew", "word": "wise", "stem": "wise",
    "avg": [ 7.52, 3.91 ], "std": [ 1.23, 2.64 ], "fq": 36
  },
  "wish": {
    "dict": "anew", "word": "wish", "stem": "wish",
    "avg": [ 7.09, 5.16 ], "std": [ 2.00, 2.62 ], "fq": 110
  },
  "wit": {
    "dict": "anew", "word": "wit", "stem": "wit",
    "avg": [ 7.32, 5.42 ], "std": [ 1.90, 2.44 ], "fq": 20
  },
  "woman": {
    "dict": "anew", "word": "woman", "stem": "woman",
    "avg": [ 6.64, 5.32 ], "std": [ 1.76, 2.59 ], "fq": 224
  },
  "wonder": {
    "dict": "anew", "word": "wonder", "stem": "wonder",
    "avg": [ 6.03, 5.00 ], "std": [ 1.58, 2.23 ], "fq": 67
  },
  "world": {
    "dict": "anew", "word": "world", "stem": "world",
    "avg": [ 6.50, 5.32 ], "std": [ 2.03, 2.39 ], "fq": 787
  },
  "wound": {
    "dict": "anew", "word": "wounds", "stem": "wound",
    "avg": [ 2.51, 5.82 ], "std": [ 1.58, 2.01 ], "fq": 8
  },
  "writer": {
    "dict": "anew", "word": "writer", "stem": "writer",
    "avg": [ 5.52, 4.33 ], "std": [ 1.90, 2.45 ], "fq": 73
  },
  "yacht": {
    "dict": "anew", "word": "yacht", "stem": "yacht",
    "avg": [ 6.95, 5.61 ], "std": [ 1.79, 2.72 ], "fq": 4
  },
  "yellow": {
    "dict": "anew", "word": "yellow", "stem": "yellow",
    "avg": [ 5.61, 4.43 ], "std": [ 1.94, 2.05 ], "fq": 55
  },
  "young": {
    "dict": "anew", "word": "young", "stem": "young",
    "avg": [ 6.89, 5.64 ], "std": [ 2.12, 2.51 ], "fq": 385
  },
  "youth": {
    "dict": "anew", "word": "youth", "stem": "youth",
    "avg": [ 6.75, 5.67 ], "std": [ 2.29, 2.52 ], "fq": 82
  },
  "zest": {
    "dict": "anew", "word": "zest", "stem": "zest",
    "avg": [ 6.79, 5.59 ], "std": [ 2.04, 2.66 ], "fq": 5
  }
}

#  Happiness terms w/word, stem, avg valence and arousal, stdev of
#  valience and arousal, and number of evaluations

hapi_word = {
  "laughter": {
    "dict": "happiness", "word": "laughter", "stem": "laughter",
    "avg": [ 6.75, 8.50 ], "std": [ 2.50, 0.93 ], "fq": 50 
  },
  "happiness": {
    "dict": "happiness", "word": "happiness", "stem": "happi",
    "avg": [ 6.49, 8.44 ], "std": [ 2.77, 0.97 ], "fq": 50 
  },
  "love": {
    "dict": "happiness", "word": "love", "stem": "love",
    "avg": [ 6.38, 8.42 ], "std": [ 2.68, 1.11 ], "fq": 50 
  },
  "happy": {
    "dict": "happiness", "word": "happy", "stem": "happi",
    "avg": [ 6.49, 8.30 ], "std": [ 2.77, 0.99 ], "fq": 50 
  },
  "laugh": {
    "dict": "happiness", "word": "laugh", "stem": "laugh",
    "avg": [ 6.74, 8.22 ], "std": [ 1.84, 1.37 ], "fq": 50 
  },
  "excellent": {
    "dict": "happiness", "word": "excellent", "stem": "excel",
    "avg": [ 5.54, 8.18 ], "std": [ 2.67, 1.10 ], "fq": 50 
  },
  "laughs": {
    "dict": "happiness", "word": "laughs", "stem": "laugh",
    "avg": [ 6.74, 8.18 ], "std": [ 1.84, 1.16 ], "fq": 50 
  },
  "joy": {
    "dict": "happiness", "word": "joy", "stem": "joy",
    "avg": [ 5.98, 8.16 ], "std": [ 2.54, 1.06 ], "fq": 50 
  },
  "successful": {
    "dict": "happiness", "word": "successful", "stem": "success",
    "avg": [ 6.11, 8.16 ], "std": [ 2.65, 1.08 ], "fq": 50 
  },
  "win": {
    "dict": "happiness", "word": "win", "stem": "win",
    "avg": [ 7.72, 8.12 ], "std": [ 2.16, 1.08 ], "fq": 50 
  },
  "rainbow": {
    "dict": "happiness", "word": "rainbow", "stem": "rainbow",
    "avg": [ 4.64, 8.10 ], "std": [ 2.88, 0.99 ], "fq": 50 
  },
  "won": {
    "dict": "happiness", "word": "won", "stem": "won",
    "avg": [ 7.72, 8.10 ], "std": [ 2.16, 1.22 ], "fq": 50 
  },
  "pleasure": {
    "dict": "happiness", "word": "pleasure", "stem": "pleasur",
    "avg": [ 5.74, 8.08 ], "std": [ 2.81, 0.97 ], "fq": 50 
  },
  "rainbows": {
    "dict": "happiness", "word": "rainbows", "stem": "rainbow",
    "avg": [ 4.64, 8.06 ], "std": [ 2.88, 1.36 ], "fq": 50 
  },
  "winning": {
    "dict": "happiness", "word": "winning", "stem": "win",
    "avg": [ 7.72, 8.04 ], "std": [ 2.16, 1.05 ], "fq": 50 
  },
  "celebration": {
    "dict": "happiness", "word": "celebration", "stem": "celebr",
    "avg": [ 3.56, 8.02 ], "std": [ 1.95, 1.53 ], "fq": 50 
  },
  "enjoyed": {
    "dict": "happiness", "word": "enjoyed", "stem": "enjoy",
    "avg": [ 5.20, 8.02 ], "std": [ 2.72, 1.53 ], "fq": 50 
  },
  "healthy": {
    "dict": "happiness", "word": "healthy", "stem": "healthi",
    "avg": [ 4.60, 8.02 ], "std": [ 2.67, 1.06 ], "fq": 50 
  },
  "music": {
    "dict": "happiness", "word": "music", "stem": "music",
    "avg": [ 5.32, 8.02 ], "std": [ 3.19, 1.12 ], "fq": 50 
  },
  "comedy": {
    "dict": "happiness", "word": "comedy", "stem": "comedi",
    "avg": [ 5.85, 7.98 ], "std": [ 2.81, 1.15 ], "fq": 50 
  },
  "jokes": {
    "dict": "happiness", "word": "jokes", "stem": "joke",
    "avg": [ 6.74, 7.98 ], "std": [ 1.84, 0.98 ], "fq": 50 
  },
  "rich": {
    "dict": "happiness", "word": "rich", "stem": "rich",
    "avg": [ 6.17, 7.98 ], "std": [ 2.70, 1.32 ], "fq": 50 
  },
  "victory": {
    "dict": "happiness", "word": "victory", "stem": "victori",
    "avg": [ 6.63, 7.98 ], "std": [ 2.84, 1.08 ], "fq": 50 
  },
  "christmas": {
    "dict": "happiness", "word": "christmas", "stem": "christma",
    "avg": [ 6.27, 7.96 ], "std": [ 2.56, 1.29 ], "fq": 50 
  },
  "free": {
    "dict": "happiness", "word": "free", "stem": "free",
    "avg": [ 5.15, 7.96 ], "std": [ 3.04, 1.26 ], "fq": 50 
  },
  "fun": {
    "dict": "happiness", "word": "fun", "stem": "fun",
    "avg": [ 7.22, 7.96 ], "std": [ 2.01, 1.31 ], "fq": 50 
  },
  "holidays": {
    "dict": "happiness", "word": "holidays", "stem": "holiday",
    "avg": [ 6.59, 7.96 ], "std": [ 2.73, 1.26 ], "fq": 50 
  },
  "loved": {
    "dict": "happiness", "word": "loved", "stem": "love",
    "avg": [ 6.38, 7.96 ], "std": [ 2.68, 1.16 ], "fq": 50 
  },
  "loves": {
    "dict": "happiness", "word": "loves", "stem": "love",
    "avg": [ 6.38, 7.96 ], "std": [ 2.68, 1.37 ], "fq": 50 
  },
  "loving": {
    "dict": "happiness", "word": "loving", "stem": "love",
    "avg": [ 6.38, 7.96 ], "std": [ 2.68, 1.01 ], "fq": 50 
  },
  "beach": {
    "dict": "happiness", "word": "beach", "stem": "beach",
    "avg": [ 5.53, 7.94 ], "std": [ 3.07, 1.06 ], "fq": 50 
  },
  "kissing": {
    "dict": "happiness", "word": "kissing", "stem": "kiss",
    "avg": [ 7.32, 7.94 ], "std": [ 2.03, 1.13 ], "fq": 50 
  },
  "sunshine": {
    "dict": "happiness", "word": "sunshine", "stem": "sunshin",
    "avg": [ 5.04, 7.94 ], "std": [ 2.66, 1.17 ], "fq": 50 
  },
  "beautiful": {
    "dict": "happiness", "word": "beautiful", "stem": "beauti",
    "avg": [ 4.95, 7.92 ], "std": [ 2.57, 1.18 ], "fq": 50 
  },
  "delicious": {
    "dict": "happiness", "word": "delicious", "stem": "delici",
    "avg": [ 5.44, 7.92 ], "std": [ 2.88, 1.26 ], "fq": 50 
  },
  "friends": {
    "dict": "happiness", "word": "friends", "stem": "friend",
    "avg": [ 5.11, 7.92 ], "std": [ 2.96, 1.19 ], "fq": 50 
  },
  "funny": {
    "dict": "happiness", "word": "funny", "stem": "funni",
    "avg": [ 6.25, 7.92 ], "std": [ 1.59, 1.05 ], "fq": 50 
  },
  "outstanding": {
    "dict": "happiness", "word": "outstanding", "stem": "outstand",
    "avg": [ 6.24, 7.92 ], "std": [ 2.59, 1.14 ], "fq": 50 
  },
  "paradise": {
    "dict": "happiness", "word": "paradise", "stem": "paradis",
    "avg": [ 5.12, 7.92 ], "std": [ 3.38, 1.40 ], "fq": 50 
  },
  "sweetest": {
    "dict": "happiness", "word": "sweetest", "stem": "sweetest",
    "avg": [ 4.83, 7.92 ], "std": [ 2.63, 1.29 ], "fq": 50 
  },
  "vacation": {
    "dict": "happiness", "word": "vacation", "stem": "vacat",
    "avg": [ 5.64, 7.92 ], "std": [ 2.99, 1.90 ], "fq": 50 
  },
  "butterflies": {
    "dict": "happiness", "word": "butterflies", "stem": "butterfli",
    "avg": [ 3.47, 7.92 ], "std": [ 2.39, 1.08 ], "fq": 50 
  },
  "freedom": {
    "dict": "happiness", "word": "freedom", "stem": "freedom",
    "avg": [ 5.52, 7.90 ], "std": [ 2.72, 1.42 ], "fq": 50 
  },
  "flower": {
    "dict": "happiness", "word": "flower", "stem": "flower",
    "avg": [ 4.00, 7.88 ], "std": [ 2.44, 1.17 ], "fq": 50 
  },
  "great": {
    "dict": "happiness", "word": "great", "stem": "great",
    "avg": [ 6.24, 7.88 ], "std": [ 2.59, 1.21 ], "fq": 50 
  },
  "sunlight": {
    "dict": "happiness", "word": "sunlight", "stem": "sunlight",
    "avg": [ 6.10, 7.88 ], "std": [ 2.30, 1.49 ], "fq": 50 
  },
  "sweetheart": {
    "dict": "happiness", "word": "sweetheart", "stem": "sweetheart",
    "avg": [ 5.50, 7.88 ], "std": [ 2.73, 1.27 ], "fq": 50 
  },
  "sweetness": {
    "dict": "happiness", "word": "sweetness", "stem": "sweet",
    "avg": [ 5.46, 7.88 ], "std": [ 2.47, 1.19 ], "fq": 50 
  },
  "award": {
    "dict": "happiness", "word": "award", "stem": "award",
    "avg": [ 5.90, 7.86 ], "std": [ 1.83, 1.57 ], "fq": 50 
  },
  "chocolate": {
    "dict": "happiness", "word": "chocolate", "stem": "chocol",
    "avg": [ 5.29, 7.86 ], "std": [ 2.55, 1.03 ], "fq": 50 
  },
  "heaven": {
    "dict": "happiness", "word": "heaven", "stem": "heaven",
    "avg": [ 5.61, 7.86 ], "std": [ 3.20, 1.58 ], "fq": 50 
  },
  "peace": {
    "dict": "happiness", "word": "peace", "stem": "peac",
    "avg": [ 2.95, 7.86 ], "std": [ 2.55, 1.34 ], "fq": 50 
  },
  "splendid": {
    "dict": "happiness", "word": "splendid", "stem": "splendid",
    "avg": [ 5.54, 7.86 ], "std": [ 2.67, 1.46 ], "fq": 50 
  },
  "success": {
    "dict": "happiness", "word": "success", "stem": "success",
    "avg": [ 6.11, 7.86 ], "std": [ 2.65, 1.64 ], "fq": 50 
  },
  "enjoying": {
    "dict": "happiness", "word": "enjoying", "stem": "enjoy",
    "avg": [ 5.20, 7.84 ], "std": [ 2.72, 1.50 ], "fq": 50 
  },
  "kissed": {
    "dict": "happiness", "word": "kissed", "stem": "kiss",
    "avg": [ 7.32, 7.84 ], "std": [ 2.03, 1.50 ], "fq": 50 
  },
  "celebrated": {
    "dict": "happiness", "word": "celebrated", "stem": "celebr",
    "avg": [ 3.93, 7.80 ], "std": [ 2.29, 1.18 ], "fq": 50 
  },
  "hero": {
    "dict": "happiness", "word": "hero", "stem": "hero",
    "avg": [ 5.85, 7.80 ], "std": [ 3.15, 1.40 ], "fq": 50 
  },
  "hugs": {
    "dict": "happiness", "word": "hugs", "stem": "hug",
    "avg": [ 5.35, 7.80 ], "std": [ 2.76, 1.44 ], "fq": 50 
  },
  "positive": {
    "dict": "happiness", "word": "positive", "stem": "posit",
    "avg": [ 6.22, 7.80 ], "std": [ 2.41, 1.25 ], "fq": 50 
  },
  "sun": {
    "dict": "happiness", "word": "sun", "stem": "sun",
    "avg": [ 5.04, 7.80 ], "std": [ 2.66, 1.36 ], "fq": 50 
  },
  "birthday": {
    "dict": "happiness", "word": "birthday", "stem": "birthday",
    "avg": [ 6.68, 7.78 ], "std": [ 2.11, 1.91 ], "fq": 50 
  },
  "blessed": {
    "dict": "happiness", "word": "blessed", "stem": "bless",
    "avg": [ 4.05, 7.78 ], "std": [ 2.59, 1.28 ], "fq": 50 
  },
  "fantastic": {
    "dict": "happiness", "word": "fantastic", "stem": "fantast",
    "avg": [ 6.23, 7.78 ], "std": [ 2.73, 1.09 ], "fq": 50 
  },
  "winner": {
    "dict": "happiness", "word": "winner", "stem": "winner",
    "avg": [ 5.53, 7.78 ], "std": [ 2.81, 1.69 ], "fq": 50 
  },
  "delight": {
    "dict": "happiness", "word": "delight", "stem": "delight",
    "avg": [ 5.44, 7.78 ], "std": [ 2.88, 1.42 ], "fq": 50 
  },
  "beauty": {
    "dict": "happiness", "word": "beauty", "stem": "beauti",
    "avg": [ 4.95, 7.76 ], "std": [ 2.57, 1.61 ], "fq": 50 
  },
  "butterfly": {
    "dict": "happiness", "word": "butterfly", "stem": "butterfli",
    "avg": [ 3.47, 7.76 ], "std": [ 2.39, 1.33 ], "fq": 50 
  },
  "funniest": {
    "dict": "happiness", "word": "funniest", "stem": "funniest",
    "avg": [ 6.25, 7.76 ], "std": [ 1.59, 1.56 ], "fq": 50 
  },
  "honesty": {
    "dict": "happiness", "word": "honesty", "stem": "honesti",
    "avg": [ 5.32, 7.76 ], "std": [ 1.92, 1.27 ], "fq": 50 
  },
  "sky": {
    "dict": "happiness", "word": "sky", "stem": "sky",
    "avg": [ 4.27, 7.76 ], "std": [ 2.17, 1.08 ], "fq": 50 
  },
  "succeed": {
    "dict": "happiness", "word": "succeed", "stem": "succeed",
    "avg": [ 7.72, 7.76 ], "std": [ 2.16, 1.70 ], "fq": 50 
  },
  "wonderful": {
    "dict": "happiness", "word": "wonderful", "stem": "wonder",
    "avg": [ 5.00, 7.76 ], "std": [ 2.23, 1.79 ], "fq": 50 
  },
  "kisses": {
    "dict": "happiness", "word": "kisses", "stem": "kiss",
    "avg": [ 7.32, 7.74 ], "std": [ 2.03, 1.19 ], "fq": 50 
  },
  "promotion": {
    "dict": "happiness", "word": "promotion", "stem": "promot",
    "avg": [ 6.44, 7.74 ], "std": [ 2.58, 1.38 ], "fq": 50 
  },
  "family": {
    "dict": "happiness", "word": "family", "stem": "famili",
    "avg": [ 4.80, 7.72 ], "std": [ 2.71, 1.31 ], "fq": 50 
  },
  "gift": {
    "dict": "happiness", "word": "gift", "stem": "gift",
    "avg": [ 6.14, 7.72 ], "std": [ 2.76, 1.34 ], "fq": 50 
  },
  "humor": {
    "dict": "happiness", "word": "humor", "stem": "humor",
    "avg": [ 5.50, 7.72 ], "std": [ 2.91, 1.09 ], "fq": 50 
  },
  "romantic": {
    "dict": "happiness", "word": "romantic", "stem": "romant",
    "avg": [ 7.59, 7.72 ], "std": [ 2.07, 1.20 ], "fq": 50 
  },
  "festival": {
    "dict": "happiness", "word": "festival", "stem": "festiv",
    "avg": [ 6.58, 7.70 ], "std": [ 2.29, 1.07 ], "fq": 50 
  },
  "honour": {
    "dict": "happiness", "word": "honour", "stem": "honour",
    "avg": [ 4.60, 7.70 ], "std": [ 2.67, 1.25 ], "fq": 50 
  },
  "relax": {
    "dict": "happiness", "word": "relax", "stem": "relax",
    "avg": [ 2.39, 7.70 ], "std": [ 2.13, 1.07 ], "fq": 50 
  },
  "angel": {
    "dict": "happiness", "word": "angel", "stem": "angel",
    "avg": [ 4.83, 7.68 ], "std": [ 2.63, 1.24 ], "fq": 50 
  },
  "bonus": {
    "dict": "happiness", "word": "bonus", "stem": "bonu",
    "avg": [ 5.69, 7.68 ], "std": [ 2.45, 1.46 ], "fq": 50 
  },
  "brilliant": {
    "dict": "happiness", "word": "brilliant", "stem": "brilliant",
    "avg": [ 5.40, 7.68 ], "std": [ 2.33, 1.62 ], "fq": 50 
  },
  "diamonds": {
    "dict": "happiness", "word": "diamonds", "stem": "diamond",
    "avg": [ 5.53, 7.68 ], "std": [ 2.96, 1.48 ], "fq": 50 
  },
  "holiday": {
    "dict": "happiness", "word": "holiday", "stem": "holiday",
    "avg": [ 6.59, 7.68 ], "std": [ 2.73, 1.30 ], "fq": 50 
  },
  "lucky": {
    "dict": "happiness", "word": "lucky", "stem": "lucki",
    "avg": [ 6.53, 7.68 ], "std": [ 2.34, 1.27 ], "fq": 50 
  },
  "mother": {
    "dict": "happiness", "word": "mother", "stem": "mother",
    "avg": [ 6.13, 7.68 ], "std": [ 2.71, 1.67 ], "fq": 50 
  },
  "super": {
    "dict": "happiness", "word": "super", "stem": "super",
    "avg": [ 5.50, 7.68 ], "std": [ 2.66, 1.60 ], "fq": 50 
  },
  "amazing": {
    "dict": "happiness", "word": "amazing", "stem": "amaz",
    "avg": [ 6.58, 7.66 ], "std": [ 2.22, 1.49 ], "fq": 50 
  },
  "angels": {
    "dict": "happiness", "word": "angels", "stem": "angel",
    "avg": [ 4.83, 7.66 ], "std": [ 2.63, 1.47 ], "fq": 50 
  },
  "enjoy": {
    "dict": "happiness", "word": "enjoy", "stem": "enjoy",
    "avg": [ 5.20, 7.66 ], "std": [ 2.72, 1.47 ], "fq": 50 
  },
  "friend": {
    "dict": "happiness", "word": "friend", "stem": "friend",
    "avg": [ 5.11, 7.66 ], "std": [ 2.96, 1.51 ], "fq": 50 
  },
  "friendly": {
    "dict": "happiness", "word": "friendly", "stem": "friendli",
    "avg": [ 4.54, 7.66 ], "std": [ 1.86, 1.55 ], "fq": 50 
  },
  "profit": {
    "dict": "happiness", "word": "profit", "stem": "profit",
    "avg": [ 6.68, 7.66 ], "std": [ 1.78, 1.24 ], "fq": 50 
  },
  "champion": {
    "dict": "happiness", "word": "champion", "stem": "champion",
    "avg": [ 5.85, 7.64 ], "std": [ 3.15, 1.22 ], "fq": 50 
  },
  "kiss": {
    "dict": "happiness", "word": "kiss", "stem": "kiss",
    "avg": [ 7.32, 7.64 ], "std": [ 2.03, 1.76 ], "fq": 50 
  },
  "kitten": {
    "dict": "happiness", "word": "kitten", "stem": "kitten",
    "avg": [ 5.08, 7.64 ], "std": [ 2.45, 1.29 ], "fq": 50 
  },
  "miracle": {
    "dict": "happiness", "word": "miracle", "stem": "miracl",
    "avg": [ 7.65, 7.64 ], "std": [ 1.67, 1.89 ], "fq": 50 
  },
  "sweet": {
    "dict": "happiness", "word": "sweet", "stem": "sweet",
    "avg": [ 4.83, 7.64 ], "std": [ 2.63, 1.06 ], "fq": 50 
  },
  "blessings": {
    "dict": "happiness", "word": "blessings", "stem": "bless",
    "avg": [ 4.05, 7.62 ], "std": [ 2.59, 1.63 ], "fq": 50 
  },
  "bright": {
    "dict": "happiness", "word": "bright", "stem": "bright",
    "avg": [ 5.40, 7.62 ], "std": [ 2.33, 1.14 ], "fq": 50 
  },
  "cutest": {
    "dict": "happiness", "word": "cutest", "stem": "cutest",
    "avg": [ 5.53, 7.62 ], "std": [ 2.71, 1.09 ], "fq": 50 
  },
  "entertaining": {
    "dict": "happiness", "word": "entertaining", "stem": "entertain",
    "avg": [ 4.84, 7.62 ], "std": [ 2.04, 1.09 ], "fq": 50 
  },
  "excited": {
    "dict": "happiness", "word": "excited", "stem": "excit",
    "avg": [ 7.67, 7.62 ], "std": [ 1.91, 1.40 ], "fq": 50 
  },
  "excitement": {
    "dict": "happiness", "word": "excitement", "stem": "excit",
    "avg": [ 7.67, 7.62 ], "std": [ 1.91, 1.65 ], "fq": 50 
  },
  "joke": {
    "dict": "happiness", "word": "joke", "stem": "joke",
    "avg": [ 6.74, 7.62 ], "std": [ 1.84, 1.40 ], "fq": 50 
  },
  "millionaire": {
    "dict": "happiness", "word": "millionaire", "stem": "millionair",
    "avg": [ 6.14, 7.62 ], "std": [ 2.70, 2.13 ], "fq": 50 
  },
  "prize": {
    "dict": "happiness", "word": "prize", "stem": "prize",
    "avg": [ 4.60, 7.62 ], "std": [ 2.67, 1.21 ], "fq": 50 
  },
  "succeeded": {
    "dict": "happiness", "word": "succeeded", "stem": "succeed",
    "avg": [ 7.72, 7.62 ], "std": [ 2.16, 1.14 ], "fq": 50 
  },
  "successfully": {
    "dict": "happiness", "word": "successfully", "stem": "success",
    "avg": [ 6.11, 7.62 ], "std": [ 2.65, 1.26 ], "fq": 50 
  },
  "winners": {
    "dict": "happiness", "word": "winners", "stem": "winner",
    "avg": [ 5.53, 7.62 ], "std": [ 2.81, 1.54 ], "fq": 50 
  },
  "shines": {
    "dict": "happiness", "word": "shines", "stem": "shine",
    "avg": [ 4.70, 7.60 ], "std": [ 2.48, 1.59 ], "fq": 50 
  },
  "awesome": {
    "dict": "happiness", "word": "awesome", "stem": "awesom",
    "avg": [ 5.74, 7.60 ], "std": [ 2.31, 1.59 ], "fq": 50 
  },
  "genius": {
    "dict": "happiness", "word": "genius", "stem": "geniu",
    "avg": [ 5.83, 7.60 ], "std": [ 2.44, 1.25 ], "fq": 50 
  },
  "achievement": {
    "dict": "happiness", "word": "achievement", "stem": "achiev",
    "avg": [ 5.53, 7.58 ], "std": [ 2.81, 1.43 ], "fq": 50 
  },
  "cake": {
    "dict": "happiness", "word": "cake", "stem": "cake",
    "avg": [ 5.00, 7.58 ], "std": [ 2.37, 1.11 ], "fq": 50 
  },
  "cheers": {
    "dict": "happiness", "word": "cheers", "stem": "cheer",
    "avg": [ 6.12, 7.58 ], "std": [ 2.45, 1.47 ], "fq": 50 
  },
  "exciting": {
    "dict": "happiness", "word": "exciting", "stem": "excit",
    "avg": [ 7.67, 7.58 ], "std": [ 1.91, 1.34 ], "fq": 50 
  },
  "goodness": {
    "dict": "happiness", "word": "goodness", "stem": "good",
    "avg": [ 5.43, 7.58 ], "std": [ 2.85, 1.37 ], "fq": 50 
  },
  "hug": {
    "dict": "happiness", "word": "hug", "stem": "hug",
    "avg": [ 5.35, 7.58 ], "std": [ 2.76, 1.47 ], "fq": 50 
  },
  "party": {
    "dict": "happiness", "word": "party", "stem": "parti",
    "avg": [ 6.69, 7.58 ], "std": [ 2.84, 1.46 ], "fq": 50 
  },
  "puppy": {
    "dict": "happiness", "word": "puppy", "stem": "puppi",
    "avg": [ 5.85, 7.58 ], "std": [ 2.78, 1.46 ], "fq": 50 
  },
  "song": {
    "dict": "happiness", "word": "song", "stem": "song",
    "avg": [ 6.07, 7.58 ], "std": [ 2.42, 1.34 ], "fq": 50 
  },
  "succeeding": {
    "dict": "happiness", "word": "succeeding", "stem": "succeed",
    "avg": [ 7.72, 7.58 ], "std": [ 2.16, 1.34 ], "fq": 50 
  },
  "victories": {
    "dict": "happiness", "word": "victories", "stem": "victori",
    "avg": [ 6.63, 7.58 ], "std": [ 2.84, 1.76 ], "fq": 50 
  },
  "achieved": {
    "dict": "happiness", "word": "achieved", "stem": "achiev",
    "avg": [ 5.53, 7.56 ], "std": [ 2.81, 1.37 ], "fq": 50 
  },
  "cakes": {
    "dict": "happiness", "word": "cakes", "stem": "cake",
    "avg": [ 5.00, 7.56 ], "std": [ 2.37, 1.46 ], "fq": 50 
  },
  "easier": {
    "dict": "happiness", "word": "easier", "stem": "easier",
    "avg": [ 3.80, 7.56 ], "std": [ 2.38, 1.15 ], "fq": 50 
  },
  "flowers": {
    "dict": "happiness", "word": "flowers", "stem": "flower",
    "avg": [ 4.00, 7.56 ], "std": [ 2.44, 1.43 ], "fq": 50 
  },
  "gifts": {
    "dict": "happiness", "word": "gifts", "stem": "gift",
    "avg": [ 6.14, 7.56 ], "std": [ 2.76, 1.94 ], "fq": 50 
  },
  "gold": {
    "dict": "happiness", "word": "gold", "stem": "gold",
    "avg": [ 5.76, 7.56 ], "std": [ 2.79, 1.11 ], "fq": 50 
  },
  "merry": {
    "dict": "happiness", "word": "merry", "stem": "merri",
    "avg": [ 5.90, 7.56 ], "std": [ 2.42, 1.15 ], "fq": 50 
  },
  "families": {
    "dict": "happiness", "word": "families", "stem": "famili",
    "avg": [ 4.80, 7.54 ], "std": [ 2.71, 1.28 ], "fq": 50 
  },
  "handsome": {
    "dict": "happiness", "word": "handsome", "stem": "handsom",
    "avg": [ 5.95, 7.54 ], "std": [ 2.73, 1.25 ], "fq": 50 
  },
  "affection": {
    "dict": "happiness", "word": "affection", "stem": "affect",
    "avg": [ 6.21, 7.53 ], "std": [ 2.75, 1.53 ], "fq": 50 
  },
  "candy": {
    "dict": "happiness", "word": "candy", "stem": "candi",
    "avg": [ 4.58, 7.52 ], "std": [ 2.40, 1.49 ], "fq": 50 
  },
  "cute": {
    "dict": "happiness", "word": "cute", "stem": "cute",
    "avg": [ 5.53, 7.52 ], "std": [ 2.71, 1.20 ], "fq": 50 
  },
  "diamond": {
    "dict": "happiness", "word": "diamond", "stem": "diamond",
    "avg": [ 5.53, 7.52 ], "std": [ 2.96, 1.72 ], "fq": 50 
  },
  "earnings": {
    "dict": "happiness", "word": "earnings", "stem": "earn",
    "avg": [ 6.68, 7.52 ], "std": [ 1.78, 1.42 ], "fq": 50 
  },
  "interesting": {
    "dict": "happiness", "word": "interesting", "stem": "interest",
    "avg": [ 5.66, 7.52 ], "std": [ 2.26, 1.18 ], "fq": 50 
  },
  "peacefully": {
    "dict": "happiness", "word": "peacefully", "stem": "peac",
    "avg": [ 2.95, 7.52 ], "std": [ 2.55, 1.05 ], "fq": 50 
  },
  "relaxing": {
    "dict": "happiness", "word": "relaxing", "stem": "relax",
    "avg": [ 2.39, 7.52 ], "std": [ 2.13, 1.22 ], "fq": 50 
  },
  "heavens": {
    "dict": "happiness", "word": "heavens", "stem": "heaven",
    "avg": [ 5.61, 7.51 ], "std": [ 3.20, 1.73 ], "fq": 50 
  },
  "cherish": {
    "dict": "happiness", "word": "cherish", "stem": "cherish",
    "avg": [ 6.75, 7.50 ], "std": [ 2.30, 1.47 ], "fq": 50 
  },
  "comfort": {
    "dict": "happiness", "word": "comfort", "stem": "comfort",
    "avg": [ 3.93, 7.50 ], "std": [ 2.85, 1.15 ], "fq": 50 
  },
  "extraordinary": {
    "dict": "happiness", "word": "extraordinary", "stem": "extraordinari",
    "avg": [ 6.29, 7.50 ], "std": [ 2.43, 1.37 ], "fq": 50 
  },
  "glory": {
    "dict": "happiness", "word": "glory", "stem": "glori",
    "avg": [ 6.02, 7.50 ], "std": [ 2.71, 1.61 ], "fq": 50 
  },
  "hilarious": {
    "dict": "happiness", "word": "hilarious", "stem": "hilari",
    "avg": [ 7.04, 7.50 ], "std": [ 1.96, 1.98 ], "fq": 50 
  },
  "peaceful": {
    "dict": "happiness", "word": "peaceful", "stem": "peac",
    "avg": [ 2.95, 7.50 ], "std": [ 2.55, 1.09 ], "fq": 50 
  },
  "romance": {
    "dict": "happiness", "word": "romance", "stem": "romanc",
    "avg": [ 6.91, 7.50 ], "std": [ 1.69, 1.43 ], "fq": 50 
  },
  "glad": {
    "dict": "happiness", "word": "glad", "stem": "glad",
    "avg": [ 6.49, 7.48 ], "std": [ 2.77, 1.52 ], "fq": 50 
  },
  "profits": {
    "dict": "happiness", "word": "profits", "stem": "profit",
    "avg": [ 6.68, 7.48 ], "std": [ 1.78, 1.33 ], "fq": 50 
  },
  "smart": {
    "dict": "happiness", "word": "smart", "stem": "smart",
    "avg": [ 5.00, 7.48 ], "std": [ 2.45, 1.37 ], "fq": 50 
  },
  "babies": {
    "dict": "happiness", "word": "babies", "stem": "babi",
    "avg": [ 5.53, 7.46 ], "std": [ 2.80, 1.50 ], "fq": 50 
  },
  "cheer": {
    "dict": "happiness", "word": "cheer", "stem": "cheer",
    "avg": [ 6.12, 7.46 ], "std": [ 2.45, 1.68 ], "fq": 50 
  },
  "courage": {
    "dict": "happiness", "word": "courage", "stem": "courag",
    "avg": [ 6.15, 7.46 ], "std": [ 2.45, 1.18 ], "fq": 50 
  },
  "honest": {
    "dict": "happiness", "word": "honest", "stem": "honest",
    "avg": [ 5.32, 7.46 ], "std": [ 1.92, 1.13 ], "fq": 50 
  },
  "loyal": {
    "dict": "happiness", "word": "loyal", "stem": "loyal",
    "avg": [ 5.16, 7.46 ], "std": [ 2.42, 1.25 ], "fq": 50 
  },
  "opportunities": {
    "dict": "happiness", "word": "opportunities", "stem": "opportun",
    "avg": [ 5.38, 7.46 ], "std": [ 2.58, 1.09 ], "fq": 50 
  },
  "triumph": {
    "dict": "happiness", "word": "triumph", "stem": "triumph",
    "avg": [ 5.78, 7.46 ], "std": [ 2.60, 1.83 ], "fq": 50 
  },
  "wow": {
    "dict": "happiness", "word": "wow", "stem": "wow",
    "avg": [ 6.39, 7.46 ], "std": [ 2.63, 1.45 ], "fq": 50 
  },
  "jewels": {
    "dict": "happiness", "word": "jewels", "stem": "jewel",
    "avg": [ 5.38, 7.46 ], "std": [ 2.54, 1.62 ], "fq": 50 
  },
  "dreams": {
    "dict": "happiness", "word": "dreams", "stem": "dream",
    "avg": [ 4.53, 7.44 ], "std": [ 2.72, 1.42 ], "fq": 50 
  },
  "fantasy": {
    "dict": "happiness", "word": "fantasy", "stem": "fantasi",
    "avg": [ 5.14, 7.44 ], "std": [ 2.82, 1.62 ], "fq": 50 
  },
  "food": {
    "dict": "happiness", "word": "food", "stem": "food",
    "avg": [ 5.92, 7.44 ], "std": [ 2.11, 1.21 ], "fq": 50 
  },
  "honey": {
    "dict": "happiness", "word": "honey", "stem": "honey",
    "avg": [ 4.51, 7.44 ], "std": [ 2.25, 1.59 ], "fq": 50 
  },
  "miracles": {
    "dict": "happiness", "word": "miracles", "stem": "miracl",
    "avg": [ 7.65, 7.44 ], "std": [ 1.67, 1.94 ], "fq": 50 
  },
  "sex": {
    "dict": "happiness", "word": "sex", "stem": "sex",
    "avg": [ 7.36, 7.44 ], "std": [ 1.91, 1.68 ], "fq": 50 
  },
  "sing": {
    "dict": "happiness", "word": "sing", "stem": "sing",
    "avg": [ 4.69, 7.44 ], "std": [ 1.99, 1.34 ], "fq": 50 
  },
  "thankful": {
    "dict": "happiness", "word": "thankful", "stem": "thank",
    "avg": [ 4.34, 7.44 ], "std": [ 2.31, 1.50 ], "fq": 50 
  },
  "wins": {
    "dict": "happiness", "word": "wins", "stem": "win",
    "avg": [ 7.72, 7.44 ], "std": [ 2.16, 1.26 ], "fq": 50 
  },
  "achieve": {
    "dict": "happiness", "word": "achieve", "stem": "achiev",
    "avg": [ 5.53, 7.42 ], "std": [ 2.81, 1.23 ], "fq": 50 
  },
  "adored": {
    "dict": "happiness", "word": "adored", "stem": "ador",
    "avg": [ 5.12, 7.42 ], "std": [ 2.71, 1.44 ], "fq": 50 
  },
  "cash": {
    "dict": "happiness", "word": "cash", "stem": "cash",
    "avg": [ 7.37, 7.42 ], "std": [ 2.21, 1.67 ], "fq": 50 
  },
  "parties": {
    "dict": "happiness", "word": "parties", "stem": "parti",
    "avg": [ 6.69, 7.42 ], "std": [ 2.84, 1.44 ], "fq": 50 
  },
  "perfect": {
    "dict": "happiness", "word": "perfect", "stem": "perfect",
    "avg": [ 5.95, 7.42 ], "std": [ 2.73, 1.72 ], "fq": 50 
  },
  "surprise": {
    "dict": "happiness", "word": "surprise", "stem": "surpris",
    "avg": [ 7.47, 7.42 ], "std": [ 2.09, 1.54 ], "fq": 50 
  },
  "truth": {
    "dict": "happiness", "word": "truth", "stem": "truth",
    "avg": [ 5.00, 7.42 ], "std": [ 2.77, 1.40 ], "fq": 50 
  },
  "blessing": {
    "dict": "happiness", "word": "blessing", "stem": "bless",
    "avg": [ 4.05, 7.40 ], "std": [ 2.59, 1.74 ], "fq": 50 
  },
  "dinner": {
    "dict": "happiness", "word": "dinner", "stem": "dinner",
    "avg": [ 5.43, 7.40 ], "std": [ 2.14, 1.14 ], "fq": 50 
  },
  "kindness": {
    "dict": "happiness", "word": "kindness", "stem": "kind",
    "avg": [ 4.30, 7.40 ], "std": [ 2.62, 1.09 ], "fq": 50 
  },
  "pleased": {
    "dict": "happiness", "word": "pleased", "stem": "pleas",
    "avg": [ 5.44, 7.40 ], "std": [ 2.88, 1.16 ], "fq": 50 
  },
  "sexy": {
    "dict": "happiness", "word": "sexy", "stem": "sexi",
    "avg": [ 7.36, 7.40 ], "std": [ 1.91, 1.23 ], "fq": 50 
  },
  "thank": {
    "dict": "happiness", "word": "thank", "stem": "thank",
    "avg": [ 4.34, 7.40 ], "std": [ 2.31, 1.12 ], "fq": 50 
  },
  "thanks": {
    "dict": "happiness", "word": "thanks", "stem": "thank",
    "avg": [ 4.34, 7.40 ], "std": [ 2.31, 1.51 ], "fq": 50 
  },
  "thanksgiving": {
    "dict": "happiness", "word": "thanksgiving", "stem": "thanksgiv",
    "avg": [ 4.05, 7.40 ], "std": [ 2.59, 1.41 ], "fq": 50 
  },
  "treasure": {
    "dict": "happiness", "word": "treasure", "stem": "treasur",
    "avg": [ 6.75, 7.40 ], "std": [ 2.30, 1.71 ], "fq": 50 
  },
  "valentine": {
    "dict": "happiness", "word": "valentine", "stem": "valentin",
    "avg": [ 6.06, 7.40 ], "std": [ 2.91, 1.70 ], "fq": 50 
  },
  "riches": {
    "dict": "happiness", "word": "riches", "stem": "rich",
    "avg": [ 6.17, 7.39 ], "std": [ 2.70, 1.67 ], "fq": 50 
  },
  "awarded": {
    "dict": "happiness", "word": "awarded", "stem": "award",
    "avg": [ 5.12, 7.38 ], "std": [ 2.39, 1.16 ], "fq": 50 
  },
  "hope": {
    "dict": "happiness", "word": "hope", "stem": "hope",
    "avg": [ 5.78, 7.38 ], "std": [ 2.09, 1.31 ], "fq": 50 
  },
  "kids": {
    "dict": "happiness", "word": "kids", "stem": "kid",
    "avg": [ 5.27, 7.38 ], "std": [ 2.36, 1.60 ], "fq": 50 
  },
  "magical": {
    "dict": "happiness", "word": "magical", "stem": "magic",
    "avg": [ 5.95, 7.38 ], "std": [ 2.36, 1.29 ], "fq": 50 
  },
  "nice": {
    "dict": "happiness", "word": "nice", "stem": "nice",
    "avg": [ 4.38, 7.38 ], "std": [ 2.69, 1.51 ], "fq": 50 
  },
  "wealth": {
    "dict": "happiness", "word": "wealth", "stem": "wealth",
    "avg": [ 6.17, 7.38 ], "std": [ 2.70, 1.23 ], "fq": 50 
  },
  "fantasies": {
    "dict": "happiness", "word": "fantasies", "stem": "fantasi",
    "avg": [ 5.14, 7.36 ], "std": [ 2.82, 1.39 ], "fq": 50 
  },
  "cares": {
    "dict": "happiness", "word": "cares", "stem": "care",
    "avg": [ 5.16, 7.36 ], "std": [ 2.62, 1.40 ], "fq": 50 
  },
  "daughters": {
    "dict": "happiness", "word": "daughters", "stem": "daughter",
    "avg": [ 4.29, 7.36 ], "std": [ 2.69, 1.22 ], "fq": 50 
  },
  "favorable": {
    "dict": "happiness", "word": "favorable", "stem": "favor",
    "avg": [ 4.54, 7.36 ], "std": [ 1.86, 1.51 ], "fq": 50 
  },
  "grateful": {
    "dict": "happiness", "word": "grateful", "stem": "grate",
    "avg": [ 4.58, 7.36 ], "std": [ 2.14, 1.47 ], "fq": 50 
  },
  "inspired": {
    "dict": "happiness", "word": "inspired", "stem": "inspir",
    "avg": [ 6.02, 7.36 ], "std": [ 2.67, 1.10 ], "fq": 50 
  },
  "mothers": {
    "dict": "happiness", "word": "mothers", "stem": "mother",
    "avg": [ 6.13, 7.36 ], "std": [ 2.71, 1.47 ], "fq": 50 
  },
  "liberation": {
    "dict": "happiness", "word": "liberation", "stem": "liber",
    "avg": [ 7.17, 7.35 ], "std": [ 2.06, 1.30 ], "fq": 50 
  },
  "melody": {
    "dict": "happiness", "word": "melody", "stem": "melodi",
    "avg": [ 4.98, 7.35 ], "std": [ 2.52, 1.77 ], "fq": 50 
  },
  "beloved": {
    "dict": "happiness", "word": "beloved", "stem": "belov",
    "avg": [ 6.38, 7.34 ], "std": [ 2.68, 1.27 ], "fq": 50 
  },
  "caring": {
    "dict": "happiness", "word": "caring", "stem": "care",
    "avg": [ 5.16, 7.34 ], "std": [ 2.62, 1.41 ], "fq": 50 
  },
  "inspiring": {
    "dict": "happiness", "word": "inspiring", "stem": "inspir",
    "avg": [ 6.02, 7.34 ], "std": [ 2.67, 1.19 ], "fq": 50 
  },
  "movies": {
    "dict": "happiness", "word": "movies", "stem": "movi",
    "avg": [ 4.93, 7.34 ], "std": [ 2.54, 1.45 ], "fq": 50 
  },
  "precious": {
    "dict": "happiness", "word": "precious", "stem": "preciou",
    "avg": [ 5.53, 7.34 ], "std": [ 2.71, 1.52 ], "fq": 50 
  },
  "respect": {
    "dict": "happiness", "word": "respect", "stem": "respect",
    "avg": [ 4.60, 7.34 ], "std": [ 2.67, 1.61 ], "fq": 50 
  },
  "satisfy": {
    "dict": "happiness", "word": "satisfy", "stem": "satisfi",
    "avg": [ 4.94, 7.34 ], "std": [ 2.63, 1.44 ], "fq": 50 
  },
  "wedding": {
    "dict": "happiness", "word": "wedding", "stem": "wed",
    "avg": [ 5.97, 7.34 ], "std": [ 2.85, 1.52 ], "fq": 50 
  },
  "accomplished": {
    "dict": "happiness", "word": "accomplished", "stem": "accomplish",
    "avg": [ 5.71, 7.32 ], "std": [ 2.74, 1.30 ], "fq": 50 
  },
  "adorable": {
    "dict": "happiness", "word": "adorable", "stem": "ador",
    "avg": [ 5.12, 7.32 ], "std": [ 2.71, 1.70 ], "fq": 50 
  },
  "comfortable": {
    "dict": "happiness", "word": "comfortable", "stem": "comfort",
    "avg": [ 3.93, 7.32 ], "std": [ 2.85, 1.10 ], "fq": 50 
  },
  "cuddle": {
    "dict": "happiness", "word": "cuddle", "stem": "cuddl",
    "avg": [ 4.40, 7.32 ], "std": [ 2.67, 1.73 ], "fq": 50 
  },
  "games": {
    "dict": "happiness", "word": "games", "stem": "game",
    "avg": [ 5.89, 7.32 ], "std": [ 2.37, 1.22 ], "fq": 50 
  },
  "life": {
    "dict": "happiness", "word": "life", "stem": "life",
    "avg": [ 6.02, 7.32 ], "std": [ 2.62, 1.70 ], "fq": 50 
  },
  "lovely": {
    "dict": "happiness", "word": "lovely", "stem": "love",
    "avg": [ 6.38, 7.32 ], "std": [ 2.68, 1.54 ], "fq": 50 
  },
  "pretty": {
    "dict": "happiness", "word": "pretty", "stem": "pretti",
    "avg": [ 6.03, 7.32 ], "std": [ 2.22, 1.70 ], "fq": 50 
  },
  "proud": {
    "dict": "happiness", "word": "proud", "stem": "proud",
    "avg": [ 5.56, 7.32 ], "std": [ 3.01, 1.43 ], "fq": 50 
  },
  "united": {
    "dict": "happiness", "word": "united", "stem": "unit",
    "avg": [ 3.75, 7.32 ], "std": [ 2.49, 1.20 ], "fq": 50 
  },
  "adventure": {
    "dict": "happiness", "word": "adventure", "stem": "adventur",
    "avg": [ 6.98, 7.30 ], "std": [ 2.15, 1.43 ], "fq": 50 
  },
  "couple": {
    "dict": "happiness", "word": "couple", "stem": "coupl",
    "avg": [ 6.39, 7.30 ], "std": [ 2.31, 1.27 ], "fq": 50 
  },
  "dollars": {
    "dict": "happiness", "word": "dollars", "stem": "dollar",
    "avg": [ 6.07, 7.30 ], "std": [ 2.67, 1.46 ], "fq": 50 
  },
  "eating": {
    "dict": "happiness", "word": "eating", "stem": "eat",
    "avg": [ 5.69, 7.30 ], "std": [ 2.51, 1.78 ], "fq": 50 
  },
  "fortune": {
    "dict": "happiness", "word": "fortune", "stem": "fortun",
    "avg": [ 5.38, 7.30 ], "std": [ 2.58, 1.39 ], "fq": 50 
  },
  "golden": {
    "dict": "happiness", "word": "golden", "stem": "golden",
    "avg": [ 5.76, 7.30 ], "std": [ 2.79, 1.34 ], "fq": 50 
  },
  "intelligence": {
    "dict": "happiness", "word": "intelligence", "stem": "intellig",
    "avg": [ 5.17, 7.30 ], "std": [ 2.11, 1.20 ], "fq": 50 
  },
  "luxury": {
    "dict": "happiness", "word": "luxury", "stem": "luxuri",
    "avg": [ 4.75, 7.30 ], "std": [ 2.91, 1.68 ], "fq": 50 
  },
  "money": {
    "dict": "happiness", "word": "money", "stem": "money",
    "avg": [ 5.70, 7.30 ], "std": [ 2.66, 1.84 ], "fq": 50 
  },
  "passion": {
    "dict": "happiness", "word": "passion", "stem": "passion",
    "avg": [ 7.26, 7.30 ], "std": [ 2.57, 1.47 ], "fq": 50 
  },
  "prosperity": {
    "dict": "happiness", "word": "prosperity", "stem": "prosper",
    "avg": [ 6.11, 7.30 ], "std": [ 2.65, 1.53 ], "fq": 50 
  },
  "sweetie": {
    "dict": "happiness", "word": "sweetie", "stem": "sweeti",
    "avg": [ 5.50, 7.30 ], "std": [ 2.73, 1.13 ], "fq": 50 
  },
  "valentines": {
    "dict": "happiness", "word": "valentines", "stem": "valentin",
    "avg": [ 6.06, 7.30 ], "std": [ 2.91, 1.78 ], "fq": 50 
  },
  "educated": {
    "dict": "happiness", "word": "educated", "stem": "educ",
    "avg": [ 5.74, 7.29 ], "std": [ 2.46, 1.31 ], "fq": 50 
  },
  "baby": {
    "dict": "happiness", "word": "baby", "stem": "babi",
    "avg": [ 5.53, 7.28 ], "std": [ 2.80, 1.85 ], "fq": 50 
  },
  "books": {
    "dict": "happiness", "word": "books", "stem": "book",
    "avg": [ 4.17, 7.28 ], "std": [ 2.49, 1.33 ], "fq": 50 
  },
  "bride": {
    "dict": "happiness", "word": "bride", "stem": "bride",
    "avg": [ 5.55, 7.28 ], "std": [ 2.74, 1.54 ], "fq": 50 
  },
  "cherished": {
    "dict": "happiness", "word": "cherished", "stem": "cherish",
    "avg": [ 6.75, 7.28 ], "std": [ 2.30, 1.58 ], "fq": 50 
  },
  "employed": {
    "dict": "happiness", "word": "employed", "stem": "employ",
    "avg": [ 5.28, 7.28 ], "std": [ 2.12, 1.36 ], "fq": 50 
  },
  "glow": {
    "dict": "happiness", "word": "glow", "stem": "glow",
    "avg": [ 6.22, 7.28 ], "std": [ 1.91, 1.29 ], "fq": 50 
  },
  "god": {
    "dict": "happiness", "word": "god", "stem": "god",
    "avg": [ 5.95, 7.28 ], "std": [ 2.84, 1.93 ], "fq": 50 
  },
  "likes": {
    "dict": "happiness", "word": "likes", "stem": "like",
    "avg": [ 5.16, 7.28 ], "std": [ 2.62, 1.54 ], "fq": 50 
  },
  "perfectly": {
    "dict": "happiness", "word": "perfectly", "stem": "perfectli",
    "avg": [ 5.73, 7.28 ], "std": [ 2.73, 1.59 ], "fq": 50 
  },
  "satisfied": {
    "dict": "happiness", "word": "satisfied", "stem": "satisfi",
    "avg": [ 4.94, 7.28 ], "std": [ 2.63, 1.53 ], "fq": 50 
  },
  "juicy": {
    "dict": "happiness", "word": "juicy", "stem": "juici",
    "avg": [ 4.31, 7.27 ], "std": [ 2.20, 1.20 ], "fq": 50 
  },
  "divine": {
    "dict": "happiness", "word": "divine", "stem": "divin",
    "avg": [ 6.02, 7.26 ], "std": [ 2.67, 1.41 ], "fq": 50 
  },
  "dreaming": {
    "dict": "happiness", "word": "dreaming", "stem": "dream",
    "avg": [ 4.53, 7.26 ], "std": [ 2.72, 1.26 ], "fq": 50 
  },
  "foods": {
    "dict": "happiness", "word": "foods", "stem": "food",
    "avg": [ 5.92, 7.26 ], "std": [ 2.11, 1.48 ], "fq": 50 
  },
  "fresh": {
    "dict": "happiness", "word": "fresh", "stem": "fresh",
    "avg": [ 3.91, 7.26 ], "std": [ 2.64, 1.32 ], "fq": 50 
  },
  "greatest": {
    "dict": "happiness", "word": "greatest", "stem": "greatest",
    "avg": [ 6.24, 7.26 ], "std": [ 2.59, 1.52 ], "fq": 50 
  },
  "hearts": {
    "dict": "happiness", "word": "hearts", "stem": "heart",
    "avg": [ 6.34, 7.26 ], "std": [ 2.25, 1.68 ], "fq": 50 
  },
  "luck": {
    "dict": "happiness", "word": "luck", "stem": "luck",
    "avg": [ 5.38, 7.26 ], "std": [ 2.58, 1.88 ], "fq": 50 
  },
  "play": {
    "dict": "happiness", "word": "play", "stem": "play",
    "avg": [ 6.91, 7.26 ], "std": [ 1.69, 1.23 ], "fq": 50 
  },
  "progress": {
    "dict": "happiness", "word": "progress", "stem": "progress",
    "avg": [ 6.02, 7.26 ], "std": [ 2.58, 1.16 ], "fq": 50 
  },
  "savings": {
    "dict": "happiness", "word": "savings", "stem": "save",
    "avg": [ 4.95, 7.26 ], "std": [ 2.19, 1.27 ], "fq": 50 
  },
  "appreciation": {
    "dict": "happiness", "word": "appreciation", "stem": "appreci",
    "avg": [ 6.11, 7.24 ], "std": [ 2.36, 1.47 ], "fq": 50 
  },
  "bliss": {
    "dict": "happiness", "word": "bliss", "stem": "bliss",
    "avg": [ 4.41, 7.24 ], "std": [ 2.95, 1.76 ], "fq": 50 
  },
  "bloom": {
    "dict": "happiness", "word": "bloom", "stem": "bloom",
    "avg": [ 4.00, 7.24 ], "std": [ 2.44, 1.60 ], "fq": 50 
  },
  "book": {
    "dict": "happiness", "word": "book", "stem": "book",
    "avg": [ 4.17, 7.24 ], "std": [ 2.49, 1.20 ], "fq": 50 
  },
  "child": {
    "dict": "happiness", "word": "child", "stem": "child",
    "avg": [ 5.55, 7.24 ], "std": [ 2.29, 1.56 ], "fq": 50 
  },
  "computer": {
    "dict": "happiness", "word": "computer", "stem": "comput",
    "avg": [ 4.75, 7.24 ], "std": [ 1.93, 1.39 ], "fq": 50 
  },
  "gardens": {
    "dict": "happiness", "word": "gardens", "stem": "garden",
    "avg": [ 4.39, 7.24 ], "std": [ 2.35, 1.35 ], "fq": 50 
  },
  "gentle": {
    "dict": "happiness", "word": "gentle", "stem": "gentl",
    "avg": [ 3.21, 7.24 ], "std": [ 2.57, 0.98 ], "fq": 50 
  },
  "impressed": {
    "dict": "happiness", "word": "impressed", "stem": "impress",
    "avg": [ 5.42, 7.24 ], "std": [ 2.65, 1.04 ], "fq": 50 
  },
  "kind": {
    "dict": "happiness", "word": "kind", "stem": "kind",
    "avg": [ 4.30, 7.24 ], "std": [ 2.62, 1.39 ], "fq": 50 
  },
  "knowledge": {
    "dict": "happiness", "word": "knowledge", "stem": "knowledg",
    "avg": [ 5.92, 7.24 ], "std": [ 2.32, 1.46 ], "fq": 50 
  },
  "liberty": {
    "dict": "happiness", "word": "liberty", "stem": "liberti",
    "avg": [ 5.60, 7.24 ], "std": [ 2.65, 1.27 ], "fq": 50 
  },
  "nature": {
    "dict": "happiness", "word": "nature", "stem": "natur",
    "avg": [ 4.37, 7.24 ], "std": [ 2.51, 1.80 ], "fq": 50 
  },
  "pal": {
    "dict": "happiness", "word": "pal", "stem": "pal",
    "avg": [ 4.71, 7.24 ], "std": [ 2.68, 1.27 ], "fq": 50 
  },
  "passionate": {
    "dict": "happiness", "word": "passionate", "stem": "passion",
    "avg": [ 7.26, 7.24 ], "std": [ 2.57, 1.08 ], "fq": 50 
  },
  "promoted": {
    "dict": "happiness", "word": "promoted", "stem": "promot",
    "avg": [ 6.44, 7.24 ], "std": [ 2.58, 1.49 ], "fq": 50 
  },
  "reward": {
    "dict": "happiness", "word": "reward", "stem": "reward",
    "avg": [ 4.95, 7.24 ], "std": [ 2.62, 1.89 ], "fq": 50 
  },
  "warmth": {
    "dict": "happiness", "word": "warmth", "stem": "warmth",
    "avg": [ 3.73, 7.24 ], "std": [ 2.40, 1.65 ], "fq": 50 
  },
  "amazed": {
    "dict": "happiness", "word": "amazed", "stem": "amaz",
    "avg": [ 6.58, 7.22 ], "std": [ 2.22, 1.87 ], "fq": 50 
  },
  "appreciate": {
    "dict": "happiness", "word": "appreciate", "stem": "appreci",
    "avg": [ 6.75, 7.22 ], "std": [ 2.30, 1.18 ], "fq": 50 
  },
  "brother": {
    "dict": "happiness", "word": "brother", "stem": "brother",
    "avg": [ 4.71, 7.22 ], "std": [ 2.68, 1.23 ], "fq": 50 
  },
  "confidence": {
    "dict": "happiness", "word": "confidence", "stem": "confid",
    "avg": [ 6.22, 7.22 ], "std": [ 2.41, 1.28 ], "fq": 50 
  },
  "darling": {
    "dict": "happiness", "word": "darling", "stem": "darl",
    "avg": [ 5.10, 7.22 ], "std": [ 2.59, 1.31 ], "fq": 50 
  },
  "encouraging": {
    "dict": "happiness", "word": "encouraging", "stem": "encourag",
    "avg": [ 6.44, 7.22 ], "std": [ 2.58, 1.56 ], "fq": 50 
  },
  "energy": {
    "dict": "happiness", "word": "energy", "stem": "energi",
    "avg": [ 5.90, 7.22 ], "std": [ 2.66, 1.30 ], "fq": 50 
  },
  "films": {
    "dict": "happiness", "word": "films", "stem": "film",
    "avg": [ 4.93, 7.22 ], "std": [ 2.54, 1.28 ], "fq": 50 
  },
  "garden": {
    "dict": "happiness", "word": "garden", "stem": "garden",
    "avg": [ 4.39, 7.22 ], "std": [ 2.35, 1.18 ], "fq": 50 
  },
  "graduated": {
    "dict": "happiness", "word": "graduated", "stem": "graduat",
    "avg": [ 7.25, 7.22 ], "std": [ 2.25, 1.27 ], "fq": 50 
  },
  "health": {
    "dict": "happiness", "word": "health", "stem": "health",
    "avg": [ 5.13, 7.22 ], "std": [ 2.35, 1.25 ], "fq": 50 
  },
  "heart": {
    "dict": "happiness", "word": "heart", "stem": "heart",
    "avg": [ 6.34, 7.22 ], "std": [ 2.25, 1.43 ], "fq": 50 
  },
  "honor": {
    "dict": "happiness", "word": "honor", "stem": "honor",
    "avg": [ 5.90, 7.22 ], "std": [ 1.83, 1.20 ], "fq": 50 
  },
  "like": {
    "dict": "happiness", "word": "like", "stem": "like",
    "avg": [ 5.16, 7.22 ], "std": [ 2.62, 1.22 ], "fq": 50 
  },
  "musical": {
    "dict": "happiness", "word": "musical", "stem": "music",
    "avg": [ 5.32, 7.22 ], "std": [ 3.19, 1.56 ], "fq": 50 
  },
  "pets": {
    "dict": "happiness", "word": "pets", "stem": "pet",
    "avg": [ 5.10, 7.22 ], "std": [ 2.59, 1.53 ], "fq": 50 
  },
  "relaxed": {
    "dict": "happiness", "word": "relaxed", "stem": "relax",
    "avg": [ 2.39, 7.22 ], "std": [ 2.13, 1.06 ], "fq": 50 
  },
  "star": {
    "dict": "happiness", "word": "star", "stem": "star",
    "avg": [ 5.83, 7.22 ], "std": [ 2.44, 1.58 ], "fq": 50 
  },
  "sweeter": {
    "dict": "happiness", "word": "sweeter", "stem": "sweeter",
    "avg": [ 4.83, 7.22 ], "std": [ 2.63, 1.11 ], "fq": 50 
  },
  "trust": {
    "dict": "happiness", "word": "trust", "stem": "trust",
    "avg": [ 5.30, 7.22 ], "std": [ 2.66, 1.23 ], "fq": 50 
  },
  "ecstasy": {
    "dict": "happiness", "word": "ecstasy", "stem": "ecstasi",
    "avg": [ 7.38, 7.20 ], "std": [ 1.92, 1.73 ], "fq": 50 
  },
  "benefits": {
    "dict": "happiness", "word": "benefits", "stem": "benefit",
    "avg": [ 6.68, 7.20 ], "std": [ 1.78, 1.05 ], "fq": 50 
  },
  "comforted": {
    "dict": "happiness", "word": "comforted", "stem": "comfort",
    "avg": [ 3.93, 7.20 ], "std": [ 2.85, 1.44 ], "fq": 50 
  },
  "discount": {
    "dict": "happiness", "word": "discount", "stem": "discount",
    "avg": [ 4.39, 7.20 ], "std": [ 2.49, 1.29 ], "fq": 50 
  },
  "good": {
    "dict": "happiness", "word": "good", "stem": "good",
    "avg": [ 5.43, 7.20 ], "std": [ 2.85, 1.46 ], "fq": 50 
  },
  "perfection": {
    "dict": "happiness", "word": "perfection", "stem": "perfect",
    "avg": [ 5.95, 7.20 ], "std": [ 2.73, 1.63 ], "fq": 50 
  },
  "presents": {
    "dict": "happiness", "word": "presents", "stem": "present",
    "avg": [ 5.12, 7.20 ], "std": [ 2.39, 1.46 ], "fq": 50 
  },
  "prizes": {
    "dict": "happiness", "word": "prizes", "stem": "prize",
    "avg": [ 6.75, 7.20 ], "std": [ 2.30, 2.03 ], "fq": 50 
  },
  "wishes": {
    "dict": "happiness", "word": "wishes", "stem": "wish",
    "avg": [ 5.16, 7.20 ], "std": [ 2.62, 1.21 ], "fq": 50 
  },
  "alive": {
    "dict": "happiness", "word": "alive", "stem": "aliv",
    "avg": [ 5.50, 7.18 ], "std": [ 2.74, 1.29 ], "fq": 50 
  },
  "awards": {
    "dict": "happiness", "word": "awards", "stem": "award",
    "avg": [ 5.90, 7.18 ], "std": [ 1.83, 1.21 ], "fq": 50 
  },
  "bed": {
    "dict": "happiness", "word": "bed", "stem": "bed",
    "avg": [ 3.61, 7.18 ], "std": [ 2.56, 1.29 ], "fq": 50 
  },
  "best": {
    "dict": "happiness", "word": "best", "stem": "best",
    "avg": [ 4.60, 7.18 ], "std": [ 2.67, 1.69 ], "fq": 50 
  },
  "coffee": {
    "dict": "happiness", "word": "coffee", "stem": "coffe",
    "avg": [ 5.29, 7.18 ], "std": [ 2.55, 1.48 ], "fq": 50 
  },
  "comfy": {
    "dict": "happiness", "word": "comfy", "stem": "comfi",
    "avg": [ 3.93, 7.18 ], "std": [ 2.85, 1.22 ], "fq": 50 
  },
  "imagine": {
    "dict": "happiness", "word": "imagine", "stem": "imagin",
    "avg": [ 5.98, 7.18 ], "std": [ 2.14, 1.10 ], "fq": 50 
  },
  "leisure": {
    "dict": "happiness", "word": "leisure", "stem": "leisur",
    "avg": [ 3.80, 7.18 ], "std": [ 2.38, 1.70 ], "fq": 50 
  },
  "promise": {
    "dict": "happiness", "word": "promise", "stem": "promis",
    "avg": [ 5.78, 7.18 ], "std": [ 2.09, 1.19 ], "fq": 50 
  },
  "respected": {
    "dict": "happiness", "word": "respected", "stem": "respect",
    "avg": [ 4.60, 7.18 ], "std": [ 2.67, 1.02 ], "fq": 50 
  },
  "rest": {
    "dict": "happiness", "word": "rest", "stem": "rest",
    "avg": [ 2.80, 7.18 ], "std": [ 2.66, 1.26 ], "fq": 50 
  },
  "travel": {
    "dict": "happiness", "word": "travel", "stem": "travel",
    "avg": [ 6.21, 7.18 ], "std": [ 2.51, 1.42 ], "fq": 50 
  },
  "abundant": {
    "dict": "happiness", "word": "abundant", "stem": "abund",
    "avg": [ 5.51, 7.16 ], "std": [ 2.63, 1.65 ], "fq": 50 
  },
  "devoted": {
    "dict": "happiness", "word": "devoted", "stem": "devot",
    "avg": [ 5.23, 7.16 ], "std": [ 2.21, 1.36 ], "fq": 50 
  },
  "favourite": {
    "dict": "happiness", "word": "favourite", "stem": "favourit",
    "avg": [ 5.10, 7.16 ], "std": [ 2.59, 1.36 ], "fq": 50 
  },
  "heroes": {
    "dict": "happiness", "word": "heroes", "stem": "hero",
    "avg": [ 5.85, 7.16 ], "std": [ 3.15, 1.57 ], "fq": 50 
  },
  "ideas": {
    "dict": "happiness", "word": "ideas", "stem": "idea",
    "avg": [ 5.86, 7.16 ], "std": [ 1.81, 1.28 ], "fq": 50 
  },
  "liked": {
    "dict": "happiness", "word": "liked", "stem": "like",
    "avg": [ 5.16, 7.16 ], "std": [ 2.62, 0.91 ], "fq": 50 
  },
  "oceans": {
    "dict": "happiness", "word": "oceans", "stem": "ocean",
    "avg": [ 4.95, 7.16 ], "std": [ 2.79, 1.62 ], "fq": 50 
  },
  "pizza": {
    "dict": "happiness", "word": "pizza", "stem": "pizza",
    "avg": [ 5.24, 7.16 ], "std": [ 2.09, 1.33 ], "fq": 50 
  },
  "skies": {
    "dict": "happiness", "word": "skies", "stem": "sky",
    "avg": [ 4.27, 7.16 ], "std": [ 2.17, 1.35 ], "fq": 50 
  },
  "sleep": {
    "dict": "happiness", "word": "sleep", "stem": "sleep",
    "avg": [ 2.80, 7.16 ], "std": [ 2.66, 1.71 ], "fq": 50 
  },
  "spring": {
    "dict": "happiness", "word": "spring", "stem": "spring",
    "avg": [ 5.67, 7.16 ], "std": [ 2.51, 1.43 ], "fq": 50 
  },
  "sunset": {
    "dict": "happiness", "word": "sunset", "stem": "sunset",
    "avg": [ 4.20, 7.16 ], "std": [ 2.99, 2.11 ], "fq": 50 
  },
  "adoring": {
    "dict": "happiness", "word": "adoring", "stem": "ador",
    "avg": [ 5.12, 7.14 ], "std": [ 2.71, 1.69 ], "fq": 50 
  },
  "brighter": {
    "dict": "happiness", "word": "brighter", "stem": "brighter",
    "avg": [ 5.40, 7.14 ], "std": [ 2.33, 1.32 ], "fq": 50 
  },
  "cure": {
    "dict": "happiness", "word": "cure", "stem": "cure",
    "avg": [ 4.77, 7.14 ], "std": [ 2.23, 1.51 ], "fq": 50 
  },
  "fireworks": {
    "dict": "happiness", "word": "fireworks", "stem": "firework",
    "avg": [ 6.67, 7.14 ], "std": [ 2.12, 1.48 ], "fq": 50 
  },
  "home": {
    "dict": "happiness", "word": "home", "stem": "home",
    "avg": [ 4.21, 7.14 ], "std": [ 2.94, 1.83 ], "fq": 50 
  },
  "honored": {
    "dict": "happiness", "word": "honored", "stem": "honor",
    "avg": [ 5.90, 7.14 ], "std": [ 1.83, 1.28 ], "fq": 50 
  },
  "journey": {
    "dict": "happiness", "word": "journey", "stem": "journey",
    "avg": [ 6.21, 7.14 ], "std": [ 2.51, 1.51 ], "fq": 50 
  },
  "opportunity": {
    "dict": "happiness", "word": "opportunity", "stem": "opportun",
    "avg": [ 5.38, 7.14 ], "std": [ 2.58, 1.71 ], "fq": 50 
  },
  "paid": {
    "dict": "happiness", "word": "paid", "stem": "paid",
    "avg": [ 5.23, 7.14 ], "std": [ 2.21, 1.71 ], "fq": 50 
  },
  "parks": {
    "dict": "happiness", "word": "parks", "stem": "park",
    "avg": [ 4.28, 7.14 ], "std": [ 2.46, 1.57 ], "fq": 50 
  },
  "playing": {
    "dict": "happiness", "word": "playing", "stem": "play",
    "avg": [ 5.11, 7.14 ], "std": [ 2.84, 1.47 ], "fq": 50 
  },
  "shine": {
    "dict": "happiness", "word": "shine", "stem": "shine",
    "avg": [ 4.70, 7.14 ], "std": [ 2.48, 1.71 ], "fq": 50 
  },
  "wealthy": {
    "dict": "happiness", "word": "wealthy", "stem": "wealthi",
    "avg": [ 5.80, 7.14 ], "std": [ 2.73, 1.75 ], "fq": 50 
  },
  "appreciated": {
    "dict": "happiness", "word": "appreciated", "stem": "appreci",
    "avg": [ 6.75, 7.12 ], "std": [ 2.30, 1.51 ], "fq": 50 
  },
  "children": {
    "dict": "happiness", "word": "children", "stem": "children",
    "avg": [ 5.53, 7.12 ], "std": [ 2.80, 1.35 ], "fq": 50 
  },
  "inspire": {
    "dict": "happiness", "word": "inspire", "stem": "inspir",
    "avg": [ 6.02, 7.12 ], "std": [ 2.67, 1.48 ], "fq": 50 
  },
  "partners": {
    "dict": "happiness", "word": "partners", "stem": "partner",
    "avg": [ 5.21, 7.12 ], "std": [ 2.75, 1.44 ], "fq": 50 
  },
  "son": {
    "dict": "happiness", "word": "son", "stem": "son",
    "avg": [ 4.58, 7.12 ], "std": [ 2.37, 1.81 ], "fq": 50 
  },
  "stronger": {
    "dict": "happiness", "word": "stronger", "stem": "stronger",
    "avg": [ 5.12, 7.12 ], "std": [ 2.19, 1.08 ], "fq": 50 
  },
  "tree": {
    "dict": "happiness", "word": "tree", "stem": "tree",
    "avg": [ 3.42, 7.12 ], "std": [ 2.21, 1.32 ], "fq": 50 
  },
  "women": {
    "dict": "happiness", "word": "women", "stem": "women",
    "avg": [ 5.32, 7.12 ], "std": [ 2.59, 1.47 ], "fq": 50 
  },
  "glowing": {
    "dict": "happiness", "word": "glowing", "stem": "glow",
    "avg": [ 6.22, 7.10 ], "std": [ 1.91, 1.43 ], "fq": 50 
  },
  "admiration": {
    "dict": "happiness", "word": "admiration", "stem": "admir",
    "avg": [ 6.11, 7.10 ], "std": [ 2.36, 1.46 ], "fq": 50 
  },
  "computers": {
    "dict": "happiness", "word": "computers", "stem": "comput",
    "avg": [ 4.75, 7.10 ], "std": [ 1.93, 1.28 ], "fq": 50 
  },
  "confident": {
    "dict": "happiness", "word": "confident", "stem": "confid",
    "avg": [ 6.22, 7.10 ], "std": [ 2.41, 1.18 ], "fq": 50 
  },
  "dearest": {
    "dict": "happiness", "word": "dearest", "stem": "dearest",
    "avg": [ 5.43, 7.10 ], "std": [ 2.85, 1.28 ], "fq": 50 
  },
  "dream": {
    "dict": "happiness", "word": "dream", "stem": "dream",
    "avg": [ 4.53, 7.10 ], "std": [ 2.72, 1.96 ], "fq": 50 
  },
  "plants": {
    "dict": "happiness", "word": "plants", "stem": "plant",
    "avg": [ 3.62, 7.10 ], "std": [ 2.25, 1.30 ], "fq": 50 
  },
  "quality": {
    "dict": "happiness", "word": "quality", "stem": "qualiti",
    "avg": [ 4.48, 7.10 ], "std": [ 2.12, 1.42 ], "fq": 50 
  },
  "rabbit": {
    "dict": "happiness", "word": "rabbit", "stem": "rabbit",
    "avg": [ 4.02, 7.10 ], "std": [ 2.19, 1.22 ], "fq": 50 
  },
  "shopping": {
    "dict": "happiness", "word": "shopping", "stem": "shop",
    "avg": [ 4.14, 7.10 ], "std": [ 2.11, 1.54 ], "fq": 50 
  },
  "sincere": {
    "dict": "happiness", "word": "sincere", "stem": "sincer",
    "avg": [ 3.56, 7.10 ], "std": [ 1.95, 1.04 ], "fq": 50 
  },
  "stars": {
    "dict": "happiness", "word": "stars", "stem": "star",
    "avg": [ 5.83, 7.10 ], "std": [ 2.44, 1.54 ], "fq": 50 
  },
  "toys": {
    "dict": "happiness", "word": "toys", "stem": "toy",
    "avg": [ 5.11, 7.10 ], "std": [ 2.84, 1.66 ], "fq": 50 
  },
  "useful": {
    "dict": "happiness", "word": "useful", "stem": "use",
    "avg": [ 4.26, 7.10 ], "std": [ 2.47, 1.20 ], "fq": 50 
  },
  "wise": {
    "dict": "happiness", "word": "wise", "stem": "wise",
    "avg": [ 3.91, 7.10 ], "std": [ 2.64, 1.27 ], "fq": 50 
  },
  "desirable": {
    "dict": "happiness", "word": "desirable", "stem": "desir",
    "avg": [ 7.35, 7.08 ], "std": [ 1.76, 1.66 ], "fq": 50 
  },
  "sparkle": {
    "dict": "happiness", "word": "sparkle", "stem": "sparkl",
    "avg": [ 5.26, 7.08 ], "std": [ 2.54, 1.62 ], "fq": 50 
  },
  "bless": {
    "dict": "happiness", "word": "bless", "stem": "bless",
    "avg": [ 4.05, 7.08 ], "std": [ 2.59, 1.97 ], "fq": 50 
  },
  "cooking": {
    "dict": "happiness", "word": "cooking", "stem": "cook",
    "avg": [ 4.44, 7.08 ], "std": [ 1.96, 1.29 ], "fq": 50 
  },
  "faith": {
    "dict": "happiness", "word": "faith", "stem": "faith",
    "avg": [ 5.30, 7.08 ], "std": [ 2.66, 1.44 ], "fq": 50 
  },
  "graduate": {
    "dict": "happiness", "word": "graduate", "stem": "graduat",
    "avg": [ 7.25, 7.08 ], "std": [ 2.25, 1.24 ], "fq": 50 
  },
  "improvements": {
    "dict": "happiness", "word": "improvements", "stem": "improv",
    "avg": [ 5.69, 7.08 ], "std": [ 2.15, 1.41 ], "fq": 50 
  },
  "memories": {
    "dict": "happiness", "word": "memories", "stem": "memori",
    "avg": [ 5.42, 7.08 ], "std": [ 2.25, 1.19 ], "fq": 50 
  },
  "park": {
    "dict": "happiness", "word": "park", "stem": "park",
    "avg": [ 4.28, 7.08 ], "std": [ 2.46, 1.35 ], "fq": 50 
  },
  "pet": {
    "dict": "happiness", "word": "pet", "stem": "pet",
    "avg": [ 5.10, 7.08 ], "std": [ 2.59, 1.70 ], "fq": 50 
  },
  "powerful": {
    "dict": "happiness", "word": "powerful", "stem": "power",
    "avg": [ 5.83, 7.08 ], "std": [ 2.69, 1.54 ], "fq": 50 
  },
  "qualities": {
    "dict": "happiness", "word": "qualities", "stem": "qualiti",
    "avg": [ 4.48, 7.08 ], "std": [ 2.12, 1.16 ], "fq": 50 
  },
  "thrill": {
    "dict": "happiness", "word": "thrill", "stem": "thrill",
    "avg": [ 8.02, 7.08 ], "std": [ 1.65, 1.56 ], "fq": 50 
  },
  "true": {
    "dict": "happiness", "word": "true", "stem": "true",
    "avg": [ 5.32, 7.08 ], "std": [ 1.92, 1.10 ], "fq": 50 
  },
  "wonder": {
    "dict": "happiness", "word": "wonder", "stem": "wonder",
    "avg": [ 5.00, 7.08 ], "std": [ 2.23, 1.31 ], "fq": 50 
  },
  "everlasting": {
    "dict": "happiness", "word": "everlasting", "stem": "everlast",
    "avg": [ 5.95, 7.06 ], "std": [ 2.73, 1.39 ], "fq": 50 
  },
  "caress": {
    "dict": "happiness", "word": "caress", "stem": "caress",
    "avg": [ 5.14, 7.06 ], "std": [ 3.00, 1.72 ], "fq": 50 
  },
  "charm": {
    "dict": "happiness", "word": "charm", "stem": "charm",
    "avg": [ 5.16, 7.06 ], "std": [ 2.25, 1.42 ], "fq": 50 
  },
  "father": {
    "dict": "happiness", "word": "father", "stem": "father",
    "avg": [ 5.92, 7.06 ], "std": [ 2.60, 1.74 ], "fq": 50 
  },
  "grand": {
    "dict": "happiness", "word": "grand", "stem": "grand",
    "avg": [ 5.00, 7.06 ], "std": [ 2.23, 1.36 ], "fq": 50 
  },
  "idea": {
    "dict": "happiness", "word": "idea", "stem": "idea",
    "avg": [ 5.86, 7.06 ], "std": [ 1.81, 1.28 ], "fq": 50 
  },
  "pictures": {
    "dict": "happiness", "word": "pictures", "stem": "pictur",
    "avg": [ 4.93, 7.06 ], "std": [ 2.54, 1.32 ], "fq": 50 
  },
  "restaurant": {
    "dict": "happiness", "word": "restaurant", "stem": "restaur",
    "avg": [ 5.41, 7.06 ], "std": [ 2.55, 1.25 ], "fq": 50 
  },
  "strong": {
    "dict": "happiness", "word": "strong", "stem": "strong",
    "avg": [ 5.92, 7.06 ], "std": [ 2.28, 1.52 ], "fq": 50 
  },
  "talent": {
    "dict": "happiness", "word": "talent", "stem": "talent",
    "avg": [ 6.27, 7.06 ], "std": [ 1.80, 0.98 ], "fq": 50 
  },
  "talented": {
    "dict": "happiness", "word": "talented", "stem": "talent",
    "avg": [ 6.27, 7.06 ], "std": [ 1.80, 1.53 ], "fq": 50 
  },
  "tenderness": {
    "dict": "happiness", "word": "tenderness", "stem": "tender",
    "avg": [ 4.88, 7.06 ], "std": [ 2.30, 1.27 ], "fq": 50 
  },
  "weddings": {
    "dict": "happiness", "word": "weddings", "stem": "wed",
    "avg": [ 5.97, 7.06 ], "std": [ 2.85, 1.66 ], "fq": 50 
  },
  "dove": {
    "dict": "happiness", "word": "dove", "stem": "dove",
    "avg": [ 3.79, 7.04 ], "std": [ 2.28, 1.44 ], "fq": 50 
  },
  "cherry": {
    "dict": "happiness", "word": "cherry", "stem": "cherri",
    "avg": [ 5.29, 7.04 ], "std": [ 2.04, 1.46 ], "fq": 50 
  },
  "daughter": {
    "dict": "happiness", "word": "daughter", "stem": "daughter",
    "avg": [ 4.29, 7.04 ], "std": [ 2.69, 1.81 ], "fq": 50 
  },
  "eat": {
    "dict": "happiness", "word": "eat", "stem": "eat",
    "avg": [ 5.69, 7.04 ], "std": [ 2.51, 1.46 ], "fq": 50 
  },
  "favorite": {
    "dict": "happiness", "word": "favorite", "stem": "favorit",
    "avg": [ 5.10, 7.04 ], "std": [ 2.59, 1.65 ], "fq": 50 
  },
  "girlfriend": {
    "dict": "happiness", "word": "girlfriend", "stem": "girlfriend",
    "avg": [ 4.29, 7.04 ], "std": [ 2.69, 1.63 ], "fq": 50 
  },
  "hoping": {
    "dict": "happiness", "word": "hoping", "stem": "hope",
    "avg": [ 5.78, 7.04 ], "std": [ 2.09, 1.14 ], "fq": 50 
  },
  "impressive": {
    "dict": "happiness", "word": "impressive", "stem": "impress",
    "avg": [ 5.42, 7.04 ], "std": [ 2.65, 1.03 ], "fq": 50 
  },
  "safe": {
    "dict": "happiness", "word": "safe", "stem": "safe",
    "avg": [ 3.86, 7.04 ], "std": [ 2.72, 1.62 ], "fq": 50 
  },
  "scholarship": {
    "dict": "happiness", "word": "scholarship", "stem": "scholarship",
    "avg": [ 5.39, 7.04 ], "std": [ 2.22, 1.65 ], "fq": 50 
  },
  "shining": {
    "dict": "happiness", "word": "shining", "stem": "shine",
    "avg": [ 5.40, 7.04 ], "std": [ 2.33, 1.76 ], "fq": 50 
  },
  "sunrise": {
    "dict": "happiness", "word": "sunrise", "stem": "sunris",
    "avg": [ 5.06, 7.04 ], "std": [ 3.05, 1.80 ], "fq": 50 
  },
  "respects": {
    "dict": "happiness", "word": "respects", "stem": "respect",
    "avg": [ 4.60, 7.02 ], "std": [ 2.67, 1.62 ], "fq": 50 
  },
  "fairy": {
    "dict": "happiness", "word": "fairy", "stem": "fairi",
    "avg": [ 4.76, 7.02 ], "std": [ 2.18, 1.48 ], "fq": 50 
  },
  "humanity": {
    "dict": "happiness", "word": "humanity", "stem": "human",
    "avg": [ 4.50, 7.02 ], "std": [ 1.91, 1.63 ], "fq": 50 
  },
  "brave": {
    "dict": "happiness", "word": "brave", "stem": "brave",
    "avg": [ 6.15, 7.02 ], "std": [ 2.45, 1.29 ], "fq": 50 
  },
  "colours": {
    "dict": "happiness", "word": "colours", "stem": "colour",
    "avg": [ 4.73, 7.02 ], "std": [ 2.64, 1.38 ], "fq": 50 
  },
  "dollar": {
    "dict": "happiness", "word": "dollar", "stem": "dollar",
    "avg": [ 6.07, 7.02 ], "std": [ 2.67, 1.52 ], "fq": 50 
  },
  "easily": {
    "dict": "happiness", "word": "easily", "stem": "easili",
    "avg": [ 4.48, 7.02 ], "std": [ 2.82, 1.63 ], "fq": 50 
  },
  "inspiration": {
    "dict": "happiness", "word": "inspiration", "stem": "inspir",
    "avg": [ 6.02, 7.02 ], "std": [ 2.67, 1.45 ], "fq": 50 
  },
  "saints": {
    "dict": "happiness", "word": "saints", "stem": "saint",
    "avg": [ 4.49, 7.02 ], "std": [ 1.90, 1.72 ], "fq": 50 
  },
  "sleeping": {
    "dict": "happiness", "word": "sleeping", "stem": "sleep",
    "avg": [ 2.80, 7.02 ], "std": [ 2.66, 1.67 ], "fq": 50 
  },
  "wisdom": {
    "dict": "happiness", "word": "wisdom", "stem": "wisdom",
    "avg": [ 3.91, 7.02 ], "std": [ 2.64, 1.56 ], "fq": 50 
  },
  "believed": {
    "dict": "happiness", "word": "believed", "stem": "believ",
    "avg": [ 5.30, 7.00 ], "std": [ 2.66, 1.28 ], "fq": 50 
  },
  "better": {
    "dict": "happiness", "word": "better", "stem": "better",
    "avg": [ 4.60, 7.00 ], "std": [ 2.67, 1.28 ], "fq": 50 
  },
  "color": {
    "dict": "happiness", "word": "color", "stem": "color",
    "avg": [ 4.73, 7.00 ], "std": [ 2.64, 1.37 ], "fq": 50 
  },
  "colors": {
    "dict": "happiness", "word": "colors", "stem": "color",
    "avg": [ 4.73, 7.00 ], "std": [ 2.64, 1.75 ], "fq": 50 
  },
  "discovered": {
    "dict": "happiness", "word": "discovered", "stem": "discov",
    "avg": [ 3.70, 7.00 ], "std": [ 2.18, 1.25 ], "fq": 50 
  },
  "gentlemen": {
    "dict": "happiness", "word": "gentlemen", "stem": "gentlemen",
    "avg": [ 5.24, 7.00 ], "std": [ 2.31, 1.43 ], "fq": 50 
  },
  "girl": {
    "dict": "happiness", "word": "girl", "stem": "girl",
    "avg": [ 4.29, 7.00 ], "std": [ 2.69, 1.16 ], "fq": 50 
  },
  "hopes": {
    "dict": "happiness", "word": "hopes", "stem": "hope",
    "avg": [ 5.78, 7.00 ], "std": [ 2.09, 1.55 ], "fq": 50 
  },
  "reliable": {
    "dict": "happiness", "word": "reliable", "stem": "reliabl",
    "avg": [ 5.32, 7.00 ], "std": [ 1.92, 1.48 ], "fq": 50 
  },
  "trip": {
    "dict": "happiness", "word": "trip", "stem": "trip",
    "avg": [ 6.21, 7.00 ], "std": [ 2.51, 1.55 ], "fq": 50 
  },
  "approval": {
    "dict": "happiness", "word": "approval", "stem": "approv",
    "avg": [ 4.05, 6.98 ], "std": [ 2.59, 1.20 ], "fq": 50 
  },
  "brothers": {
    "dict": "happiness", "word": "brothers", "stem": "brother",
    "avg": [ 4.71, 6.98 ], "std": [ 2.68, 1.45 ], "fq": 50 
  },
  "encouraged": {
    "dict": "happiness", "word": "encouraged", "stem": "encourag",
    "avg": [ 6.44, 6.98 ], "std": [ 2.58, 1.24 ], "fq": 50 
  },
  "giving": {
    "dict": "happiness", "word": "giving", "stem": "give",
    "avg": [ 5.23, 6.98 ], "std": [ 2.21, 1.15 ], "fq": 50 
  },
  "ideal": {
    "dict": "happiness", "word": "ideal", "stem": "ideal",
    "avg": [ 4.49, 6.98 ], "std": [ 1.90, 1.71 ], "fq": 50 
  },
  "intellectual": {
    "dict": "happiness", "word": "intellectual", "stem": "intellectu",
    "avg": [ 4.75, 6.98 ], "std": [ 2.50, 1.29 ], "fq": 50 
  },
  "marry": {
    "dict": "happiness", "word": "marry", "stem": "marri",
    "avg": [ 5.97, 6.98 ], "std": [ 2.85, 1.87 ], "fq": 50 
  },
  "outdoors": {
    "dict": "happiness", "word": "outdoors", "stem": "outdoor",
    "avg": [ 5.92, 6.98 ], "std": [ 2.55, 1.70 ], "fq": 50 
  },
  "plenty": {
    "dict": "happiness", "word": "plenty", "stem": "plenti",
    "avg": [ 5.49, 6.98 ], "std": [ 2.43, 1.22 ], "fq": 50 
  },
  "trees": {
    "dict": "happiness", "word": "trees", "stem": "tree",
    "avg": [ 3.42, 6.98 ], "std": [ 2.21, 1.60 ], "fq": 50 
  },
  "trips": {
    "dict": "happiness", "word": "trips", "stem": "trip",
    "avg": [ 6.21, 6.98 ], "std": [ 2.51, 1.32 ], "fq": 50 
  },
  "unique": {
    "dict": "happiness", "word": "unique", "stem": "uniqu",
    "avg": [ 4.83, 6.98 ], "std": [ 2.66, 1.44 ], "fq": 50 
  },
  "thrills": {
    "dict": "happiness", "word": "thrills", "stem": "thrill",
    "avg": [ 8.02, 6.98 ], "std": [ 1.65, 1.33 ], "fq": 50 
  },
  "bath": {
    "dict": "happiness", "word": "bath", "stem": "bath",
    "avg": [ 4.16, 6.96 ], "std": [ 2.31, 1.26 ], "fq": 50 
  },
  "benefit": {
    "dict": "happiness", "word": "benefit", "stem": "benefit",
    "avg": [ 6.68, 6.96 ], "std": [ 1.78, 1.31 ], "fq": 50 
  },
  "birds": {
    "dict": "happiness", "word": "birds", "stem": "bird",
    "avg": [ 3.17, 6.96 ], "std": [ 2.23, 1.43 ], "fq": 50 
  },
  "elegant": {
    "dict": "happiness", "word": "elegant", "stem": "eleg",
    "avg": [ 4.53, 6.96 ], "std": [ 2.65, 1.93 ], "fq": 50 
  },
  "fair": {
    "dict": "happiness", "word": "fair", "stem": "fair",
    "avg": [ 5.32, 6.96 ], "std": [ 1.92, 1.26 ], "fq": 50 
  },
  "fancy": {
    "dict": "happiness", "word": "fancy", "stem": "fanci",
    "avg": [ 5.14, 6.96 ], "std": [ 2.82, 1.37 ], "fq": 50 
  },
  "imagination": {
    "dict": "happiness", "word": "imagination", "stem": "imagin",
    "avg": [ 5.98, 6.96 ], "std": [ 2.14, 1.35 ], "fq": 50 
  },
  "improving": {
    "dict": "happiness", "word": "improving", "stem": "improv",
    "avg": [ 5.69, 6.96 ], "std": [ 2.15, 0.88 ], "fq": 50 
  },
  "mountains": {
    "dict": "happiness", "word": "mountains", "stem": "mountain",
    "avg": [ 5.49, 6.96 ], "std": [ 2.43, 1.19 ], "fq": 50 
  },
  "ocean": {
    "dict": "happiness", "word": "ocean", "stem": "ocean",
    "avg": [ 4.95, 6.96 ], "std": [ 2.79, 1.71 ], "fq": 50 
  },
  "pancakes": {
    "dict": "happiness", "word": "pancakes", "stem": "pancak",
    "avg": [ 4.06, 6.96 ], "std": [ 2.13, 1.21 ], "fq": 50 
  },
  "present": {
    "dict": "happiness", "word": "present", "stem": "present",
    "avg": [ 5.12, 6.96 ], "std": [ 2.39, 1.28 ], "fq": 50 
  },
  "reunion": {
    "dict": "happiness", "word": "reunion", "stem": "reunion",
    "avg": [ 6.34, 6.96 ], "std": [ 2.35, 1.63 ], "fq": 50 
  },
  "safely": {
    "dict": "happiness", "word": "safely", "stem": "safe",
    "avg": [ 3.86, 6.96 ], "std": [ 2.72, 1.46 ], "fq": 50 
  },
  "saving": {
    "dict": "happiness", "word": "saving", "stem": "save",
    "avg": [ 4.95, 6.96 ], "std": [ 2.19, 1.26 ], "fq": 50 
  },
  "singing": {
    "dict": "happiness", "word": "singing", "stem": "sing",
    "avg": [ 4.69, 6.96 ], "std": [ 1.99, 1.70 ], "fq": 50 
  },
  "songs": {
    "dict": "happiness", "word": "songs", "stem": "song",
    "avg": [ 6.07, 6.96 ], "std": [ 2.42, 1.87 ], "fq": 50 
  },
  "terrific": {
    "dict": "happiness", "word": "terrific", "stem": "terrif",
    "avg": [ 6.23, 6.96 ], "std": [ 2.73, 2.08 ], "fq": 50 
  },
  "theater": {
    "dict": "happiness", "word": "theater", "stem": "theater",
    "avg": [ 4.56, 6.96 ], "std": [ 2.41, 1.55 ], "fq": 50 
  },
  "adore": {
    "dict": "happiness", "word": "adore", "stem": "ador",
    "avg": [ 5.12, 6.96 ], "std": [ 2.71, 1.86 ], "fq": 50 
  },
  "gentleman": {
    "dict": "happiness", "word": "gentleman", "stem": "gentleman",
    "avg": [ 5.24, 6.96 ], "std": [ 2.31, 1.73 ], "fq": 50 
  },
  "autumn": {
    "dict": "happiness", "word": "autumn", "stem": "autumn",
    "avg": [ 4.51, 6.94 ], "std": [ 2.50, 1.50 ], "fq": 50 
  },
  "cozy": {
    "dict": "happiness", "word": "cozy", "stem": "cozi",
    "avg": [ 3.32, 6.94 ], "std": [ 2.28, 1.46 ], "fq": 50 
  },
  "dear": {
    "dict": "happiness", "word": "dear", "stem": "dear",
    "avg": [ 3.36, 6.94 ], "std": [ 2.18, 1.54 ], "fq": 50 
  },
  "gardening": {
    "dict": "happiness", "word": "gardening", "stem": "garden",
    "avg": [ 4.39, 6.94 ], "std": [ 2.35, 1.27 ], "fq": 50 
  },
  "girls": {
    "dict": "happiness", "word": "girls", "stem": "girl",
    "avg": [ 4.29, 6.94 ], "std": [ 2.69, 1.46 ], "fq": 50 
  },
  "outdoor": {
    "dict": "happiness", "word": "outdoor", "stem": "outdoor",
    "avg": [ 5.92, 6.94 ], "std": [ 2.55, 1.24 ], "fq": 50 
  },
  "piano": {
    "dict": "happiness", "word": "piano", "stem": "piano",
    "avg": [ 4.63, 6.94 ], "std": [ 2.61, 1.27 ], "fq": 50 
  },
  "sea": {
    "dict": "happiness", "word": "sea", "stem": "sea",
    "avg": [ 4.95, 6.94 ], "std": [ 2.79, 1.28 ], "fq": 50 
  },
  "trusted": {
    "dict": "happiness", "word": "trusted", "stem": "trust",
    "avg": [ 5.30, 6.94 ], "std": [ 2.66, 1.53 ], "fq": 50 
  },
  "favored": {
    "dict": "happiness", "word": "favored", "stem": "favor",
    "avg": [ 4.54, 6.92 ], "std": [ 1.86, 1.35 ], "fq": 50 
  },
  "game": {
    "dict": "happiness", "word": "game", "stem": "game",
    "avg": [ 5.89, 6.92 ], "std": [ 2.37, 1.60 ], "fq": 50 
  },
  "healing": {
    "dict": "happiness", "word": "healing", "stem": "heal",
    "avg": [ 4.77, 6.92 ], "std": [ 2.23, 1.40 ], "fq": 50 
  },
  "learned": {
    "dict": "happiness", "word": "learned", "stem": "learn",
    "avg": [ 5.39, 6.92 ], "std": [ 2.22, 1.52 ], "fq": 50 
  },
  "learning": {
    "dict": "happiness", "word": "learning", "stem": "learn",
    "avg": [ 5.39, 6.92 ], "std": [ 2.22, 1.35 ], "fq": 50 
  },
  "promote": {
    "dict": "happiness", "word": "promote", "stem": "promot",
    "avg": [ 6.44, 6.92 ], "std": [ 2.58, 1.07 ], "fq": 50 
  },
  "secure": {
    "dict": "happiness", "word": "secure", "stem": "secur",
    "avg": [ 3.14, 6.92 ], "std": [ 2.47, 1.29 ], "fq": 50 
  },
  "unity": {
    "dict": "happiness", "word": "unity", "stem": "uniti",
    "avg": [ 5.50, 6.92 ], "std": [ 2.66, 1.75 ], "fq": 50 
  },
  "wish": {
    "dict": "happiness", "word": "wish", "stem": "wish",
    "avg": [ 5.16, 6.92 ], "std": [ 2.62, 1.50 ], "fq": 50 
  },
  "favour": {
    "dict": "happiness", "word": "favour", "stem": "favour",
    "avg": [ 4.54, 6.92 ], "std": [ 1.86, 1.53 ], "fq": 50 
  },
  "clean": {
    "dict": "happiness", "word": "clean", "stem": "clean",
    "avg": [ 4.37, 6.90 ], "std": [ 2.14, 1.90 ], "fq": 50 
  },
  "dynamic": {
    "dict": "happiness", "word": "dynamic", "stem": "dynam",
    "avg": [ 4.86, 6.90 ], "std": [ 2.56, 1.31 ], "fq": 50 
  },
  "encourage": {
    "dict": "happiness", "word": "encourage", "stem": "encourag",
    "avg": [ 6.44, 6.90 ], "std": [ 2.58, 1.68 ], "fq": 50 
  },
  "infant": {
    "dict": "happiness", "word": "infant", "stem": "infant",
    "avg": [ 5.05, 6.90 ], "std": [ 2.66, 1.76 ], "fq": 50 
  },
  "paintings": {
    "dict": "happiness", "word": "paintings", "stem": "paint",
    "avg": [ 4.10, 6.90 ], "std": [ 2.36, 1.59 ], "fq": 50 
  },
  "voyage": {
    "dict": "happiness", "word": "voyage", "stem": "voyag",
    "avg": [ 5.55, 6.90 ], "std": [ 2.23, 1.33 ], "fq": 50 
  },
  "worthy": {
    "dict": "happiness", "word": "worthy", "stem": "worthi",
    "avg": [ 7.35, 6.90 ], "std": [ 1.76, 1.68 ], "fq": 50 
  },
  "fulfill": {
    "dict": "happiness", "word": "fulfill", "stem": "fulfil",
    "avg": [ 5.71, 6.90 ], "std": [ 2.74, 1.34 ], "fq": 50 
  },
  "accuracy": {
    "dict": "happiness", "word": "accuracy", "stem": "accuraci",
    "avg": [ 5.00, 6.88 ], "std": [ 2.77, 1.17 ], "fq": 50 
  },
  "breeze": {
    "dict": "happiness", "word": "breeze", "stem": "breez",
    "avg": [ 4.37, 6.88 ], "std": [ 2.32, 1.33 ], "fq": 50 
  },
  "bunny": {
    "dict": "happiness", "word": "bunny", "stem": "bunni",
    "avg": [ 4.06, 6.88 ], "std": [ 2.61, 1.79 ], "fq": 50 
  },
  "education": {
    "dict": "happiness", "word": "education", "stem": "educ",
    "avg": [ 5.74, 6.88 ], "std": [ 2.46, 1.61 ], "fq": 50 
  },
  "flavor": {
    "dict": "happiness", "word": "flavor", "stem": "flavor",
    "avg": [ 5.56, 6.88 ], "std": [ 2.62, 1.22 ], "fq": 50 
  },
  "pillow": {
    "dict": "happiness", "word": "pillow", "stem": "pillow",
    "avg": [ 2.97, 6.88 ], "std": [ 2.52, 1.22 ], "fq": 50 
  },
  "pure": {
    "dict": "happiness", "word": "pure", "stem": "pure",
    "avg": [ 5.51, 6.88 ], "std": [ 2.06, 1.35 ], "fq": 50 
  },
  "saved": {
    "dict": "happiness", "word": "saved", "stem": "save",
    "avg": [ 4.95, 6.88 ], "std": [ 2.19, 1.51 ], "fq": 50 
  },
  "survived": {
    "dict": "happiness", "word": "survived", "stem": "surviv",
    "avg": [ 5.53, 6.88 ], "std": [ 2.90, 1.48 ], "fq": 50 
  },
  "taste": {
    "dict": "happiness", "word": "taste", "stem": "tast",
    "avg": [ 5.22, 6.88 ], "std": [ 2.38, 1.27 ], "fq": 50 
  },
  "valued": {
    "dict": "happiness", "word": "valued", "stem": "valu",
    "avg": [ 6.75, 6.88 ], "std": [ 2.30, 1.12 ], "fq": 50 
  },
  "infants": {
    "dict": "happiness", "word": "infants", "stem": "infant",
    "avg": [ 5.05, 6.88 ], "std": [ 2.66, 1.63 ], "fq": 50 
  },
  "silk": {
    "dict": "happiness", "word": "silk", "stem": "silk",
    "avg": [ 3.71, 6.88 ], "std": [ 2.51, 1.45 ], "fq": 50 
  },
  "dreamed": {
    "dict": "happiness", "word": "dreamed", "stem": "dream",
    "avg": [ 4.53, 6.87 ], "std": [ 2.72, 1.39 ], "fq": 50 
  },
  "acceptance": {
    "dict": "happiness", "word": "acceptance", "stem": "accept",
    "avg": [ 5.40, 6.86 ], "std": [ 2.70, 1.28 ], "fq": 50 
  },
  "dancer": {
    "dict": "happiness", "word": "dancer", "stem": "dancer",
    "avg": [ 6.00, 6.86 ], "std": [ 2.20, 1.54 ], "fq": 50 
  },
  "grace": {
    "dict": "happiness", "word": "grace", "stem": "grace",
    "avg": [ 4.05, 6.86 ], "std": [ 2.59, 1.53 ], "fq": 50 
  },
  "guarantee": {
    "dict": "happiness", "word": "guarantee", "stem": "guarante",
    "avg": [ 3.14, 6.86 ], "std": [ 2.47, 1.31 ], "fq": 50 
  },
  "improved": {
    "dict": "happiness", "word": "improved", "stem": "improv",
    "avg": [ 5.69, 6.86 ], "std": [ 2.15, 1.36 ], "fq": 50 
  },
  "improvement": {
    "dict": "happiness", "word": "improvement", "stem": "improv",
    "avg": [ 5.69, 6.86 ], "std": [ 2.15, 1.26 ], "fq": 50 
  },
  "liking": {
    "dict": "happiness", "word": "liking", "stem": "like",
    "avg": [ 5.16, 6.86 ], "std": [ 2.62, 0.88 ], "fq": 50 
  },
  "pasta": {
    "dict": "happiness", "word": "pasta", "stem": "pasta",
    "avg": [ 4.94, 6.86 ], "std": [ 2.04, 1.41 ], "fq": 50 
  },
  "sailing": {
    "dict": "happiness", "word": "sailing", "stem": "sail",
    "avg": [ 5.55, 6.86 ], "std": [ 2.23, 1.48 ], "fq": 50 
  },
  "seas": {
    "dict": "happiness", "word": "seas", "stem": "sea",
    "avg": [ 4.95, 6.86 ], "std": [ 2.79, 1.63 ], "fq": 50 
  },
  "toast": {
    "dict": "happiness", "word": "toast", "stem": "toast",
    "avg": [ 5.31, 6.86 ], "std": [ 2.23, 1.41 ], "fq": 50 
  },
  "superstar": {
    "dict": "happiness", "word": "superstar", "stem": "superstar",
    "avg": [ 5.85, 6.86 ], "std": [ 3.15, 1.97 ], "fq": 50 
  },
  "advantage": {
    "dict": "happiness", "word": "advantage", "stem": "advantag",
    "avg": [ 4.76, 6.84 ], "std": [ 2.18, 1.28 ], "fq": 50 
  },
  "buddy": {
    "dict": "happiness", "word": "buddy", "stem": "buddi",
    "avg": [ 4.71, 6.84 ], "std": [ 2.68, 1.06 ], "fq": 50 
  },
  "daylight": {
    "dict": "happiness", "word": "daylight", "stem": "daylight",
    "avg": [ 4.77, 6.84 ], "std": [ 2.50, 1.40 ], "fq": 50 
  },
  "discover": {
    "dict": "happiness", "word": "discover", "stem": "discov",
    "avg": [ 3.70, 6.84 ], "std": [ 2.18, 1.40 ], "fq": 50 
  },
  "hopefully": {
    "dict": "happiness", "word": "hopefully", "stem": "hope",
    "avg": [ 5.78, 6.84 ], "std": [ 2.09, 1.52 ], "fq": 50 
  },
  "horses": {
    "dict": "happiness", "word": "horses", "stem": "hors",
    "avg": [ 3.89, 6.84 ], "std": [ 2.17, 1.48 ], "fq": 50 
  },
  "interested": {
    "dict": "happiness", "word": "interested", "stem": "interest",
    "avg": [ 5.66, 6.84 ], "std": [ 2.26, 1.09 ], "fq": 50 
  },
  "kid": {
    "dict": "happiness", "word": "kid", "stem": "kid",
    "avg": [ 5.27, 6.84 ], "std": [ 2.36, 1.48 ], "fq": 50 
  },
  "live": {
    "dict": "happiness", "word": "live", "stem": "live",
    "avg": [ 5.53, 6.84 ], "std": [ 2.90, 1.52 ], "fq": 50 
  },
  "movie": {
    "dict": "happiness", "word": "movie", "stem": "movi",
    "avg": [ 4.93, 6.84 ], "std": [ 2.54, 1.98 ], "fq": 50 
  },
  "solution": {
    "dict": "happiness", "word": "solution", "stem": "solut",
    "avg": [ 5.41, 6.84 ], "std": [ 2.43, 1.38 ], "fq": 50 
  },
  "swim": {
    "dict": "happiness", "word": "swim", "stem": "swim",
    "avg": [ 6.57, 6.84 ], "std": [ 2.33, 1.30 ], "fq": 50 
  },
  "toy": {
    "dict": "happiness", "word": "toy", "stem": "toy",
    "avg": [ 5.11, 6.84 ], "std": [ 2.84, 2.03 ], "fq": 50 
  },
  "understanding": {
    "dict": "happiness", "word": "understanding", "stem": "understand",
    "avg": [ 5.02, 6.84 ], "std": [ 2.24, 1.17 ], "fq": 50 
  },
  "universe": {
    "dict": "happiness", "word": "universe", "stem": "univers",
    "avg": [ 5.32, 6.84 ], "std": [ 2.39, 1.28 ], "fq": 50 
  },
  "woman": {
    "dict": "happiness", "word": "woman", "stem": "woman",
    "avg": [ 5.32, 6.84 ], "std": [ 2.59, 1.65 ], "fq": 50 
  },
  "rivers": {
    "dict": "happiness", "word": "rivers", "stem": "river",
    "avg": [ 4.51, 6.84 ], "std": [ 2.42, 1.53 ], "fq": 50 
  },
  "sail": {
    "dict": "happiness", "word": "sail", "stem": "sail",
    "avg": [ 5.55, 6.84 ], "std": [ 2.23, 1.56 ], "fq": 50 
  },
  "cared": {
    "dict": "happiness", "word": "cared", "stem": "care",
    "avg": [ 5.16, 6.83 ], "std": [ 2.62, 1.27 ], "fq": 50 
  },
  "active": {
    "dict": "happiness", "word": "active", "stem": "activ",
    "avg": [ 4.86, 6.82 ], "std": [ 2.56, 1.77 ], "fq": 50 
  },
  "babe": {
    "dict": "happiness", "word": "babe", "stem": "babe",
    "avg": [ 5.53, 6.82 ], "std": [ 2.80, 1.27 ], "fq": 50 
  },
  "believes": {
    "dict": "happiness", "word": "believes", "stem": "believ",
    "avg": [ 5.42, 6.82 ], "std": [ 2.65, 1.19 ], "fq": 50 
  },
  "born": {
    "dict": "happiness", "word": "born", "stem": "born",
    "avg": [ 4.37, 6.82 ], "std": [ 2.51, 1.65 ], "fq": 50 
  },
  "compassion": {
    "dict": "happiness", "word": "compassion", "stem": "compass",
    "avg": [ 3.72, 6.82 ], "std": [ 2.02, 1.90 ], "fq": 50 
  },
  "dedicated": {
    "dict": "happiness", "word": "dedicated", "stem": "dedic",
    "avg": [ 5.23, 6.82 ], "std": [ 2.21, 1.32 ], "fq": 50 
  },
  "experienced": {
    "dict": "happiness", "word": "experienced", "stem": "experienc",
    "avg": [ 5.53, 6.82 ], "std": [ 2.90, 1.17 ], "fq": 50 
  },
  "fathers": {
    "dict": "happiness", "word": "fathers", "stem": "father",
    "avg": [ 5.92, 6.82 ], "std": [ 2.60, 1.83 ], "fq": 50 
  },
  "gains": {
    "dict": "happiness", "word": "gains", "stem": "gain",
    "avg": [ 7.72, 6.82 ], "std": [ 2.16, 1.48 ], "fq": 50 
  },
  "heal": {
    "dict": "happiness", "word": "heal", "stem": "heal",
    "avg": [ 4.77, 6.82 ], "std": [ 2.23, 1.45 ], "fq": 50 
  },
  "new": {
    "dict": "happiness", "word": "new", "stem": "new",
    "avg": [ 5.64, 6.82 ], "std": [ 2.51, 1.14 ], "fq": 50 
  },
  "young": {
    "dict": "happiness", "word": "young", "stem": "young",
    "avg": [ 5.64, 6.82 ], "std": [ 2.51, 1.24 ], "fq": 50 
  },
  "mansion": {
    "dict": "happiness", "word": "mansion", "stem": "mansion",
    "avg": [ 4.56, 6.82 ], "std": [ 2.41, 1.63 ], "fq": 50 
  },
  "prevail": {
    "dict": "happiness", "word": "prevail", "stem": "prevail",
    "avg": [ 5.78, 6.82 ], "std": [ 2.60, 1.73 ], "fq": 50 
  },
  "air": {
    "dict": "happiness", "word": "air", "stem": "air",
    "avg": [ 4.12, 6.80 ], "std": [ 2.30, 1.65 ], "fq": 50 
  },
  "animal": {
    "dict": "happiness", "word": "animal", "stem": "anim",
    "avg": [ 5.57, 6.80 ], "std": [ 2.61, 1.85 ], "fq": 50 
  },
  "horse": {
    "dict": "happiness", "word": "horse", "stem": "hors",
    "avg": [ 3.89, 6.80 ], "std": [ 2.17, 1.51 ], "fq": 50 
  },
  "magic": {
    "dict": "happiness", "word": "magic", "stem": "magic",
    "avg": [ 5.95, 6.80 ], "std": [ 2.36, 1.76 ], "fq": 50 
  },
  "manners": {
    "dict": "happiness", "word": "manners", "stem": "manner",
    "avg": [ 4.56, 6.80 ], "std": [ 1.78, 1.25 ], "fq": 50 
  },
  "naturally": {
    "dict": "happiness", "word": "naturally", "stem": "natur",
    "avg": [ 4.37, 6.80 ], "std": [ 2.51, 1.60 ], "fq": 50 
  },
  "pies": {
    "dict": "happiness", "word": "pies", "stem": "pie",
    "avg": [ 4.20, 6.80 ], "std": [ 2.40, 1.37 ], "fq": 50 
  },
  "protect": {
    "dict": "happiness", "word": "protect", "stem": "protect",
    "avg": [ 4.09, 6.80 ], "std": [ 2.77, 1.41 ], "fq": 50 
  },
  "smooth": {
    "dict": "happiness", "word": "smooth", "stem": "smooth",
    "avg": [ 4.91, 6.80 ], "std": [ 2.57, 1.18 ], "fq": 50 
  },
  "elevated": {
    "dict": "happiness", "word": "elevated", "stem": "elev",
    "avg": [ 4.16, 6.80 ], "std": [ 1.99, 1.19 ], "fq": 50 
  },
  "coke": {
    "dict": "happiness", "word": "coke", "stem": "coke",
    "avg": [ 5.75, 6.78 ], "std": [ 2.47, 1.62 ], "fq": 50 
  },
  "creation": {
    "dict": "happiness", "word": "creation", "stem": "creation",
    "avg": [ 5.32, 6.78 ], "std": [ 2.39, 1.40 ], "fq": 50 
  },
  "dogs": {
    "dict": "happiness", "word": "dogs", "stem": "dog",
    "avg": [ 5.76, 6.78 ], "std": [ 2.50, 1.82 ], "fq": 50 
  },
  "esteemed": {
    "dict": "happiness", "word": "esteemed", "stem": "esteem",
    "avg": [ 4.60, 6.78 ], "std": [ 2.67, 1.40 ], "fq": 50 
  },
  "green": {
    "dict": "happiness", "word": "green", "stem": "green",
    "avg": [ 4.28, 6.78 ], "std": [ 2.46, 1.69 ], "fq": 50 
  },
  "heartbeat": {
    "dict": "happiness", "word": "heartbeat", "stem": "heartbeat",
    "avg": [ 5.44, 6.78 ], "std": [ 2.68, 1.71 ], "fq": 50 
  },
  "medal": {
    "dict": "happiness", "word": "medal", "stem": "medal",
    "avg": [ 5.14, 6.78 ], "std": [ 2.39, 1.43 ], "fq": 50 
  },
  "museums": {
    "dict": "happiness", "word": "museums", "stem": "museum",
    "avg": [ 3.60, 6.78 ], "std": [ 2.13, 1.72 ], "fq": 50 
  },
  "painting": {
    "dict": "happiness", "word": "painting", "stem": "paint",
    "avg": [ 4.10, 6.78 ], "std": [ 2.36, 1.17 ], "fq": 50 
  },
  "pie": {
    "dict": "happiness", "word": "pie", "stem": "pie",
    "avg": [ 4.20, 6.78 ], "std": [ 2.40, 1.72 ], "fq": 50 
  },
  "reading": {
    "dict": "happiness", "word": "reading", "stem": "read",
    "avg": [ 5.39, 6.78 ], "std": [ 2.22, 1.46 ], "fq": 50 
  },
  "real": {
    "dict": "happiness", "word": "real", "stem": "real",
    "avg": [ 4.36, 6.78 ], "std": [ 2.18, 1.20 ], "fq": 50 
  },
  "ruby": {
    "dict": "happiness", "word": "ruby", "stem": "rubi",
    "avg": [ 5.29, 6.78 ], "std": [ 2.04, 1.27 ], "fq": 50 
  },
  "share": {
    "dict": "happiness", "word": "share", "stem": "share",
    "avg": [ 3.82, 6.78 ], "std": [ 2.24, 1.40 ], "fq": 50 
  },
  "sons": {
    "dict": "happiness", "word": "sons", "stem": "son",
    "avg": [ 4.58, 6.78 ], "std": [ 2.37, 1.62 ], "fq": 50 
  },
  "traveling": {
    "dict": "happiness", "word": "traveling", "stem": "travel",
    "avg": [ 6.21, 6.78 ], "std": [ 2.51, 1.67 ], "fq": 50 
  },
  "variety": {
    "dict": "happiness", "word": "variety", "stem": "varieti",
    "avg": [ 4.30, 6.78 ], "std": [ 2.62, 1.31 ], "fq": 50 
  },
  "wonders": {
    "dict": "happiness", "word": "wonders", "stem": "wonder",
    "avg": [ 5.00, 6.78 ], "std": [ 2.23, 1.89 ], "fq": 50 
  },
  "guaranteed": {
    "dict": "happiness", "word": "guaranteed", "stem": "guarante",
    "avg": [ 3.14, 6.78 ], "std": [ 2.47, 1.18 ], "fq": 50 
  },
  "visions": {
    "dict": "happiness", "word": "visions", "stem": "vision",
    "avg": [ 4.66, 6.78 ], "std": [ 2.43, 1.37 ], "fq": 50 
  },
  "easy": {
    "dict": "happiness", "word": "easy", "stem": "easi",
    "avg": [ 4.48, 6.76 ], "std": [ 2.82, 1.60 ], "fq": 50 
  },
  "effective": {
    "dict": "happiness", "word": "effective", "stem": "effect",
    "avg": [ 5.43, 6.76 ], "std": [ 2.85, 1.29 ], "fq": 50 
  },
  "humans": {
    "dict": "happiness", "word": "humans", "stem": "human",
    "avg": [ 4.50, 6.76 ], "std": [ 1.91, 1.45 ], "fq": 50 
  },
  "intimate": {
    "dict": "happiness", "word": "intimate", "stem": "intim",
    "avg": [ 6.98, 6.76 ], "std": [ 2.21, 1.30 ], "fq": 50 
  },
  "married": {
    "dict": "happiness", "word": "married", "stem": "marri",
    "avg": [ 5.97, 6.76 ], "std": [ 2.85, 1.85 ], "fq": 50 
  },
  "muffin": {
    "dict": "happiness", "word": "muffin", "stem": "muffin",
    "avg": [ 4.76, 6.76 ], "std": [ 2.42, 1.24 ], "fq": 50 
  },
  "savior": {
    "dict": "happiness", "word": "savior", "stem": "savior",
    "avg": [ 5.80, 6.76 ], "std": [ 3.01, 1.62 ], "fq": 50 
  },
  "shop": {
    "dict": "happiness", "word": "shop", "stem": "shop",
    "avg": [ 4.14, 6.76 ], "std": [ 2.11, 1.04 ], "fq": 50 
  },
  "sister": {
    "dict": "happiness", "word": "sister", "stem": "sister",
    "avg": [ 5.53, 6.76 ], "std": [ 2.80, 1.65 ], "fq": 50 
  },
  "style": {
    "dict": "happiness", "word": "style", "stem": "style",
    "avg": [ 4.56, 6.76 ], "std": [ 1.78, 1.62 ], "fq": 50 
  },
  "supporter": {
    "dict": "happiness", "word": "supporter", "stem": "support",
    "avg": [ 5.85, 6.76 ], "std": [ 3.15, 1.22 ], "fq": 50 
  },
  "top": {
    "dict": "happiness", "word": "top", "stem": "top",
    "avg": [ 4.28, 6.76 ], "std": [ 2.53, 1.52 ], "fq": 50 
  },
  "capable": {
    "dict": "happiness", "word": "capable", "stem": "capabl",
    "avg": [ 5.08, 6.74 ], "std": [ 2.07, 1.68 ], "fq": 50 
  },
  "complete": {
    "dict": "happiness", "word": "complete", "stem": "complet",
    "avg": [ 5.95, 6.74 ], "std": [ 2.73, 1.24 ], "fq": 50 
  },
  "drinks": {
    "dict": "happiness", "word": "drinks", "stem": "drink",
    "avg": [ 5.21, 6.74 ], "std": [ 2.46, 1.43 ], "fq": 50 
  },
  "focused": {
    "dict": "happiness", "word": "focused", "stem": "focus",
    "avg": [ 4.65, 6.74 ], "std": [ 2.13, 1.14 ], "fq": 50 
  },
  "justice": {
    "dict": "happiness", "word": "justice", "stem": "justic",
    "avg": [ 5.47, 6.74 ], "std": [ 2.54, 1.96 ], "fq": 50 
  },
  "lake": {
    "dict": "happiness", "word": "lake", "stem": "lake",
    "avg": [ 3.95, 6.74 ], "std": [ 2.44, 1.68 ], "fq": 50 
  },
  "mankind": {
    "dict": "happiness", "word": "mankind", "stem": "mankind",
    "avg": [ 4.50, 6.74 ], "std": [ 1.91, 1.60 ], "fq": 50 
  },
  "merit": {
    "dict": "happiness", "word": "merit", "stem": "merit",
    "avg": [ 4.52, 6.74 ], "std": [ 2.52, 1.21 ], "fq": 50 
  },
  "performance": {
    "dict": "happiness", "word": "performance", "stem": "perform",
    "avg": [ 5.71, 6.74 ], "std": [ 2.74, 1.34 ], "fq": 50 
  },
  "plant": {
    "dict": "happiness", "word": "plant", "stem": "plant",
    "avg": [ 3.62, 6.74 ], "std": [ 2.25, 1.35 ], "fq": 50 
  },
  "prepared": {
    "dict": "happiness", "word": "prepared", "stem": "prepar",
    "avg": [ 3.82, 6.74 ], "std": [ 2.40, 1.07 ], "fq": 50 
  },
  "raise": {
    "dict": "happiness", "word": "raise", "stem": "rais",
    "avg": [ 7.17, 6.74 ], "std": [ 2.06, 1.21 ], "fq": 50 
  },
  "shiny": {
    "dict": "happiness", "word": "shiny", "stem": "shini",
    "avg": [ 5.40, 6.74 ], "std": [ 2.33, 1.23 ], "fq": 50 
  },
  "sugar": {
    "dict": "happiness", "word": "sugar", "stem": "sugar",
    "avg": [ 5.64, 6.74 ], "std": [ 2.18, 1.94 ], "fq": 50 
  },
  "surprising": {
    "dict": "happiness", "word": "surprising", "stem": "surpris",
    "avg": [ 7.47, 6.74 ], "std": [ 2.09, 1.29 ], "fq": 50 
  },
  "technology": {
    "dict": "happiness", "word": "technology", "stem": "technolog",
    "avg": [ 3.98, 6.74 ], "std": [ 2.33, 1.50 ], "fq": 50 
  },
  "treat": {
    "dict": "happiness", "word": "treat", "stem": "treat",
    "avg": [ 5.62, 6.74 ], "std": [ 2.25, 1.71 ], "fq": 50 
  },
  "wishing": {
    "dict": "happiness", "word": "wishing", "stem": "wish",
    "avg": [ 5.16, 6.74 ], "std": [ 2.62, 1.05 ], "fq": 50 
  },
  "desires": {
    "dict": "happiness", "word": "desires", "stem": "desir",
    "avg": [ 7.35, 6.73 ], "std": [ 1.76, 1.47 ], "fq": 50 
  },
  "wished": {
    "dict": "happiness", "word": "wished", "stem": "wish",
    "avg": [ 5.16, 6.73 ], "std": [ 2.62, 1.41 ], "fq": 50 
  },
  "car": {
    "dict": "happiness", "word": "car", "stem": "car",
    "avg": [ 6.24, 6.72 ], "std": [ 2.04, 2.10 ], "fq": 50 
  },
  "knowing": {
    "dict": "happiness", "word": "knowing", "stem": "know",
    "avg": [ 6.38, 6.72 ], "std": [ 2.68, 1.36 ], "fq": 50 
  },
  "neat": {
    "dict": "happiness", "word": "neat", "stem": "neat",
    "avg": [ 3.80, 6.72 ], "std": [ 2.18, 1.44 ], "fq": 50 
  },
  "orchestra": {
    "dict": "happiness", "word": "orchestra", "stem": "orchestra",
    "avg": [ 3.52, 6.72 ], "std": [ 2.29, 1.37 ], "fq": 50 
  },
  "plays": {
    "dict": "happiness", "word": "plays", "stem": "play",
    "avg": [ 6.91, 6.72 ], "std": [ 1.69, 1.58 ], "fq": 50 
  },
  "shower": {
    "dict": "happiness", "word": "shower", "stem": "shower",
    "avg": [ 4.93, 6.72 ], "std": [ 2.40, 1.51 ], "fq": 50 
  },
  "surprised": {
    "dict": "happiness", "word": "surprised", "stem": "surpris",
    "avg": [ 7.47, 6.72 ], "std": [ 2.09, 1.36 ], "fq": 50 
  },
  "tremendous": {
    "dict": "happiness", "word": "tremendous", "stem": "tremend",
    "avg": [ 6.23, 6.72 ], "std": [ 2.73, 1.59 ], "fq": 50 
  },
  "values": {
    "dict": "happiness", "word": "values", "stem": "valu",
    "avg": [ 6.75, 6.72 ], "std": [ 2.30, 1.57 ], "fq": 50 
  },
  "villages": {
    "dict": "happiness", "word": "villages", "stem": "villag",
    "avg": [ 4.08, 6.72 ], "std": [ 1.87, 1.37 ], "fq": 50 
  },
  "warm": {
    "dict": "happiness", "word": "warm", "stem": "warm",
    "avg": [ 6.57, 6.72 ], "std": [ 1.78, 1.80 ], "fq": 50 
  },
  "secured": {
    "dict": "happiness", "word": "secured", "stem": "secur",
    "avg": [ 3.14, 6.71 ], "std": [ 2.47, 1.15 ], "fq": 50 
  },
  "believe": {
    "dict": "happiness", "word": "believe", "stem": "believ",
    "avg": [ 5.30, 6.70 ], "std": [ 2.66, 1.59 ], "fq": 50 
  },
  "bucks": {
    "dict": "happiness", "word": "bucks", "stem": "buck",
    "avg": [ 3.89, 6.70 ], "std": [ 2.17, 1.68 ], "fq": 50 
  },
  "dancers": {
    "dict": "happiness", "word": "dancers", "stem": "dancer",
    "avg": [ 6.00, 6.70 ], "std": [ 2.20, 1.61 ], "fq": 50 
  },
  "dog": {
    "dict": "happiness", "word": "dog", "stem": "dog",
    "avg": [ 5.76, 6.70 ], "std": [ 2.50, 1.84 ], "fq": 50 
  },
  "hired": {
    "dict": "happiness", "word": "hired", "stem": "hire",
    "avg": [ 6.77, 6.70 ], "std": [ 2.07, 1.49 ], "fq": 50 
  },
  "learn": {
    "dict": "happiness", "word": "learn", "stem": "learn",
    "avg": [ 5.39, 6.70 ], "std": [ 2.22, 1.42 ], "fq": 50 
  },
  "marriage": {
    "dict": "happiness", "word": "marriage", "stem": "marriag",
    "avg": [ 5.97, 6.70 ], "std": [ 2.85, 2.27 ], "fq": 50 
  },
  "partner": {
    "dict": "happiness", "word": "partner", "stem": "partner",
    "avg": [ 5.21, 6.70 ], "std": [ 2.75, 1.25 ], "fq": 50 
  },
  "productive": {
    "dict": "happiness", "word": "productive", "stem": "product",
    "avg": [ 6.17, 6.70 ], "std": [ 2.70, 1.13 ], "fq": 50 
  },
  "teaches": {
    "dict": "happiness", "word": "teaches", "stem": "teach",
    "avg": [ 5.39, 6.70 ], "std": [ 2.22, 1.09 ], "fq": 50 
  },
  "treats": {
    "dict": "happiness", "word": "treats", "stem": "treat",
    "avg": [ 5.62, 6.70 ], "std": [ 2.25, 1.57 ], "fq": 50 
  },
  "water": {
    "dict": "happiness", "word": "water", "stem": "water",
    "avg": [ 4.97, 6.70 ], "std": [ 2.49, 1.22 ], "fq": 50 
  },
  "virtues": {
    "dict": "happiness", "word": "virtues", "stem": "virtu",
    "avg": [ 4.52, 6.69 ], "std": [ 2.52, 1.43 ], "fq": 50 
  },
  "brains": {
    "dict": "happiness", "word": "brains", "stem": "brain",
    "avg": [ 5.00, 6.69 ], "std": [ 2.68, 1.48 ], "fq": 50 
  },
  "sensation": {
    "dict": "happiness", "word": "sensation", "stem": "sensat",
    "avg": [ 5.83, 6.68 ], "std": [ 2.44, 1.40 ], "fq": 50 
  },
  "ability": {
    "dict": "happiness", "word": "ability", "stem": "abil",
    "avg": [ 5.83, 6.68 ], "std": [ 2.69, 1.00 ], "fq": 50 
  },
  "ace": {
    "dict": "happiness", "word": "ace", "stem": "ace",
    "avg": [ 5.50, 6.68 ], "std": [ 2.66, 1.68 ], "fq": 50 
  },
  "animals": {
    "dict": "happiness", "word": "animals", "stem": "anim",
    "avg": [ 5.57, 6.68 ], "std": [ 2.61, 2.02 ], "fq": 50 
  },
  "bake": {
    "dict": "happiness", "word": "bake", "stem": "bake",
    "avg": [ 5.10, 6.68 ], "std": [ 2.30, 1.41 ], "fq": 50 
  },
  "desire": {
    "dict": "happiness", "word": "desire", "stem": "desir",
    "avg": [ 7.35, 6.68 ], "std": [ 1.76, 1.36 ], "fq": 50 
  },
  "famous": {
    "dict": "happiness", "word": "famous", "stem": "famou",
    "avg": [ 6.55, 6.68 ], "std": [ 2.46, 2.00 ], "fq": 50 
  },
  "fountain": {
    "dict": "happiness", "word": "fountain", "stem": "fountain",
    "avg": [ 5.67, 6.68 ], "std": [ 2.51, 1.28 ], "fq": 50 
  },
  "greater": {
    "dict": "happiness", "word": "greater", "stem": "greater",
    "avg": [ 6.24, 6.68 ], "std": [ 2.59, 1.32 ], "fq": 50 
  },
  "grow": {
    "dict": "happiness", "word": "grow", "stem": "grow",
    "avg": [ 3.90, 6.68 ], "std": [ 1.95, 1.22 ], "fq": 50 
  },
  "liberties": {
    "dict": "happiness", "word": "liberties", "stem": "liberti",
    "avg": [ 5.60, 6.68 ], "std": [ 2.65, 1.71 ], "fq": 50 
  },
  "living": {
    "dict": "happiness", "word": "living", "stem": "live",
    "avg": [ 5.53, 6.68 ], "std": [ 2.90, 1.22 ], "fq": 50 
  },
  "museum": {
    "dict": "happiness", "word": "museum", "stem": "museum",
    "avg": [ 3.60, 6.68 ], "std": [ 2.13, 1.46 ], "fq": 50 
  },
  "novel": {
    "dict": "happiness", "word": "novel", "stem": "novel",
    "avg": [ 4.45, 6.68 ], "std": [ 2.70, 1.46 ], "fq": 50 
  },
  "palace": {
    "dict": "happiness", "word": "palace", "stem": "palac",
    "avg": [ 5.10, 6.68 ], "std": [ 2.75, 1.65 ], "fq": 50 
  },
  "power": {
    "dict": "happiness", "word": "power", "stem": "power",
    "avg": [ 5.83, 6.68 ], "std": [ 2.69, 1.49 ], "fq": 50 
  },
  "privilege": {
    "dict": "happiness", "word": "privilege", "stem": "privileg",
    "avg": [ 4.54, 6.68 ], "std": [ 1.86, 1.65 ], "fq": 50 
  },
  "river": {
    "dict": "happiness", "word": "river", "stem": "river",
    "avg": [ 4.51, 6.68 ], "std": [ 2.42, 1.33 ], "fq": 50 
  },
  "shares": {
    "dict": "happiness", "word": "shares", "stem": "share",
    "avg": [ 3.82, 6.68 ], "std": [ 2.24, 1.22 ], "fq": 50 
  },
  "theatre": {
    "dict": "happiness", "word": "theatre", "stem": "theatr",
    "avg": [ 4.56, 6.68 ], "std": [ 2.41, 1.53 ], "fq": 50 
  },
  "well": {
    "dict": "happiness", "word": "well", "stem": "well",
    "avg": [ 5.43, 6.68 ], "std": [ 2.85, 1.25 ], "fq": 50 
  },
  "acceptable": {
    "dict": "happiness", "word": "acceptable", "stem": "accept",
    "avg": [ 5.40, 6.67 ], "std": [ 2.70, 1.21 ], "fq": 50 
  },
  "possibilities": {
    "dict": "happiness", "word": "possibilities", "stem": "possibl",
    "avg": [ 4.62, 6.67 ], "std": [ 1.94, 1.48 ], "fq": 50 
  },
  "charms": {
    "dict": "happiness", "word": "charms", "stem": "charm",
    "avg": [ 5.16, 6.66 ], "std": [ 2.25, 1.38 ], "fq": 50 
  },
  "greet": {
    "dict": "happiness", "word": "greet", "stem": "greet",
    "avg": [ 5.27, 6.66 ], "std": [ 2.31, 1.56 ], "fq": 50 
  },
  "personality": {
    "dict": "happiness", "word": "personality", "stem": "person",
    "avg": [ 4.19, 6.66 ], "std": [ 2.45, 1.52 ], "fq": 50 
  },
  "powers": {
    "dict": "happiness", "word": "powers", "stem": "power",
    "avg": [ 5.83, 6.66 ], "std": [ 2.69, 1.32 ], "fq": 50 
  },
  "raises": {
    "dict": "happiness", "word": "raises", "stem": "rais",
    "avg": [ 7.17, 6.66 ], "std": [ 2.06, 1.62 ], "fq": 50 
  },
  "bird": {
    "dict": "happiness", "word": "bird", "stem": "bird",
    "avg": [ 3.17, 6.64 ], "std": [ 2.23, 1.55 ], "fq": 50 
  },
  "care": {
    "dict": "happiness", "word": "care", "stem": "care",
    "avg": [ 5.16, 6.64 ], "std": [ 2.62, 1.65 ], "fq": 50 
  },
  "cat": {
    "dict": "happiness", "word": "cat", "stem": "cat",
    "avg": [ 4.38, 6.64 ], "std": [ 2.24, 1.98 ], "fq": 50 
  },
  "cook": {
    "dict": "happiness", "word": "cook", "stem": "cook",
    "avg": [ 4.44, 6.64 ], "std": [ 1.96, 1.50 ], "fq": 50 
  },
  "expert": {
    "dict": "happiness", "word": "expert", "stem": "expert",
    "avg": [ 5.43, 6.64 ], "std": [ 2.85, 1.32 ], "fq": 50 
  },
  "high": {
    "dict": "happiness", "word": "high", "stem": "high",
    "avg": [ 4.75, 6.64 ], "std": [ 2.91, 1.21 ], "fq": 50 
  },
  "leading": {
    "dict": "happiness", "word": "leading", "stem": "lead",
    "avg": [ 5.83, 6.64 ], "std": [ 2.44, 1.51 ], "fq": 50 
  },
  "picture": {
    "dict": "happiness", "word": "picture", "stem": "pictur",
    "avg": [ 4.93, 6.64 ], "std": [ 2.54, 1.31 ], "fq": 50 
  },
  "promising": {
    "dict": "happiness", "word": "promising", "stem": "promis",
    "avg": [ 5.40, 6.64 ], "std": [ 2.33, 1.12 ], "fq": 50 
  },
  "recovered": {
    "dict": "happiness", "word": "recovered", "stem": "recov",
    "avg": [ 4.77, 6.64 ], "std": [ 2.23, 1.32 ], "fq": 50 
  },
  "salad": {
    "dict": "happiness", "word": "salad", "stem": "salad",
    "avg": [ 3.81, 6.64 ], "std": [ 2.29, 1.71 ], "fq": 50 
  },
  "shops": {
    "dict": "happiness", "word": "shops", "stem": "shop",
    "avg": [ 4.14, 6.64 ], "std": [ 2.11, 1.24 ], "fq": 50 
  },
  "solutions": {
    "dict": "happiness", "word": "solutions", "stem": "solut",
    "avg": [ 5.41, 6.64 ], "std": [ 2.43, 1.38 ], "fq": 50 
  },
  "sparks": {
    "dict": "happiness", "word": "sparks", "stem": "spark",
    "avg": [ 4.86, 6.64 ], "std": [ 2.56, 1.31 ], "fq": 50 
  },
  "sport": {
    "dict": "happiness", "word": "sport", "stem": "sport",
    "avg": [ 4.84, 6.64 ], "std": [ 2.52, 1.69 ], "fq": 50 
  },
  "theaters": {
    "dict": "happiness", "word": "theaters", "stem": "theater",
    "avg": [ 4.56, 6.64 ], "std": [ 2.41, 1.66 ], "fq": 50 
  },
  "tunes": {
    "dict": "happiness", "word": "tunes", "stem": "tune",
    "avg": [ 4.71, 6.64 ], "std": [ 2.09, 1.38 ], "fq": 50 
  },
  "unite": {
    "dict": "happiness", "word": "unite", "stem": "unit",
    "avg": [ 3.75, 6.64 ], "std": [ 2.49, 1.19 ], "fq": 50 
  },
  "simplicity": {
    "dict": "happiness", "word": "simplicity", "stem": "simplic",
    "avg": [ 4.48, 6.62 ], "std": [ 2.82, 1.52 ], "fq": 50 
  },
  "attained": {
    "dict": "happiness", "word": "attained", "stem": "attain",
    "avg": [ 5.73, 6.62 ], "std": [ 2.09, 1.40 ], "fq": 50 
  },
  "chatting": {
    "dict": "happiness", "word": "chatting", "stem": "chat",
    "avg": [ 5.74, 6.62 ], "std": [ 2.38, 1.24 ], "fq": 50 
  },
  "crown": {
    "dict": "happiness", "word": "crown", "stem": "crown",
    "avg": [ 4.28, 6.62 ], "std": [ 2.53, 1.47 ], "fq": 50 
  },
  "dresses": {
    "dict": "happiness", "word": "dresses", "stem": "dress",
    "avg": [ 4.05, 6.62 ], "std": [ 1.89, 1.71 ], "fq": 50 
  },
  "homes": {
    "dict": "happiness", "word": "homes", "stem": "home",
    "avg": [ 4.21, 6.62 ], "std": [ 2.94, 1.24 ], "fq": 50 
  },
  "immortal": {
    "dict": "happiness", "word": "immortal", "stem": "immort",
    "avg": [ 5.95, 6.62 ], "std": [ 2.84, 1.65 ], "fq": 50 
  },
  "invest": {
    "dict": "happiness", "word": "invest", "stem": "invest",
    "avg": [ 5.12, 6.62 ], "std": [ 2.42, 1.03 ], "fq": 50 
  },
  "kitty": {
    "dict": "happiness", "word": "kitty", "stem": "kitti",
    "avg": [ 5.08, 6.62 ], "std": [ 2.45, 1.86 ], "fq": 50 
  },
  "offer": {
    "dict": "happiness", "word": "offer", "stem": "offer",
    "avg": [ 4.88, 6.62 ], "std": [ 2.30, 1.03 ], "fq": 50 
  },
  "organized": {
    "dict": "happiness", "word": "organized", "stem": "organ",
    "avg": [ 3.82, 6.62 ], "std": [ 2.40, 1.24 ], "fq": 50 
  },
  "performances": {
    "dict": "happiness", "word": "performances", "stem": "perform",
    "avg": [ 5.71, 6.62 ], "std": [ 2.74, 1.37 ], "fq": 50 
  },
  "perfume": {
    "dict": "happiness", "word": "perfume", "stem": "perfum",
    "avg": [ 5.05, 6.62 ], "std": [ 2.36, 1.61 ], "fq": 50 
  },
  "rescue": {
    "dict": "happiness", "word": "rescue", "stem": "rescu",
    "avg": [ 6.53, 6.62 ], "std": [ 2.56, 1.66 ], "fq": 50 
  },
  "restaurants": {
    "dict": "happiness", "word": "restaurants", "stem": "restaur",
    "avg": [ 5.41, 6.62 ], "std": [ 2.55, 1.78 ], "fq": 50 
  },
  "sisters": {
    "dict": "happiness", "word": "sisters", "stem": "sister",
    "avg": [ 5.53, 6.62 ], "std": [ 2.80, 1.69 ], "fq": 50 
  },
  "slept": {
    "dict": "happiness", "word": "slept", "stem": "slept",
    "avg": [ 2.80, 6.62 ], "std": [ 2.66, 1.56 ], "fq": 50 
  },
  "stories": {
    "dict": "happiness", "word": "stories", "stem": "stori",
    "avg": [ 3.93, 6.62 ], "std": [ 2.29, 1.59 ], "fq": 50 
  },
  "varieties": {
    "dict": "happiness", "word": "varieties", "stem": "varieti",
    "avg": [ 4.30, 6.62 ], "std": [ 2.62, 1.31 ], "fq": 50 
  },
  "vision": {
    "dict": "happiness", "word": "vision", "stem": "vision",
    "avg": [ 4.66, 6.62 ], "std": [ 2.43, 1.21 ], "fq": 50 
  },
  "wife": {
    "dict": "happiness", "word": "wife", "stem": "wife",
    "avg": [ 4.93, 6.62 ], "std": [ 2.22, 1.81 ], "fq": 50 
  },
  "youth": {
    "dict": "happiness", "word": "youth", "stem": "youth",
    "avg": [ 5.67, 6.62 ], "std": [ 2.52, 1.88 ], "fq": 50 
  },
  "stimulation": {
    "dict": "happiness", "word": "stimulation", "stem": "stimul",
    "avg": [ 6.63, 6.61 ], "std": [ 2.70, 1.35 ], "fq": 50 
  },
  "touching": {
    "dict": "happiness", "word": "touching", "stem": "touch",
    "avg": [ 6.21, 6.61 ], "std": [ 2.75, 1.68 ], "fq": 50 
  },
  "suitable": {
    "dict": "happiness", "word": "suitable", "stem": "suitabl",
    "avg": [ 7.35, 6.60 ], "std": [ 1.76, 0.89 ], "fq": 50 
  },
  "art": {
    "dict": "happiness", "word": "art", "stem": "art",
    "avg": [ 4.86, 6.60 ], "std": [ 2.88, 1.50 ], "fq": 50 
  },
  "beam": {
    "dict": "happiness", "word": "beam", "stem": "beam",
    "avg": [ 4.02, 6.60 ], "std": [ 1.94, 1.37 ], "fq": 50 
  },
  "captain": {
    "dict": "happiness", "word": "captain", "stem": "captain",
    "avg": [ 5.20, 6.60 ], "std": [ 2.85, 1.63 ], "fq": 50 
  },
  "clothing": {
    "dict": "happiness", "word": "clothing", "stem": "cloth",
    "avg": [ 4.78, 6.60 ], "std": [ 2.88, 1.31 ], "fq": 50 
  },
  "desired": {
    "dict": "happiness", "word": "desired", "stem": "desir",
    "avg": [ 7.35, 6.60 ], "std": [ 1.76, 1.56 ], "fq": 50 
  },
  "dress": {
    "dict": "happiness", "word": "dress", "stem": "dress",
    "avg": [ 4.05, 6.60 ], "std": [ 1.89, 1.18 ], "fq": 50 
  },
  "ideals": {
    "dict": "happiness", "word": "ideals", "stem": "ideal",
    "avg": [ 4.49, 6.60 ], "std": [ 1.90, 1.62 ], "fq": 50 
  },
  "protected": {
    "dict": "happiness", "word": "protected", "stem": "protect",
    "avg": [ 4.09, 6.60 ], "std": [ 2.77, 1.18 ], "fq": 50 
  },
  "spirit": {
    "dict": "happiness", "word": "spirit", "stem": "spirit",
    "avg": [ 5.56, 6.60 ], "std": [ 2.62, 1.50 ], "fq": 50 
  },
  "supported": {
    "dict": "happiness", "word": "supported", "stem": "support",
    "avg": [ 3.93, 6.60 ], "std": [ 2.49, 1.54 ], "fq": 50 
  },
  "therapeutic": {
    "dict": "happiness", "word": "therapeutic", "stem": "therapeut",
    "avg": [ 4.77, 6.60 ], "std": [ 2.23, 1.56 ], "fq": 50 
  },
  "visiting": {
    "dict": "happiness", "word": "visiting", "stem": "visit",
    "avg": [ 5.74, 6.60 ], "std": [ 2.38, 1.21 ], "fq": 50 
  },
  "expressions": {
    "dict": "happiness", "word": "expressions", "stem": "express",
    "avg": [ 5.04, 6.60 ], "std": [ 2.18, 1.30 ], "fq": 50 
  },
  "sleeps": {
    "dict": "happiness", "word": "sleeps", "stem": "sleep",
    "avg": [ 2.80, 6.59 ], "std": [ 2.66, 1.47 ], "fq": 50 
  },
  "vocals": {
    "dict": "happiness", "word": "vocals", "stem": "vocal",
    "avg": [ 6.07, 6.59 ], "std": [ 2.42, 1.46 ], "fq": 50 
  },
  "impress": {
    "dict": "happiness", "word": "impress", "stem": "impress",
    "avg": [ 5.42, 6.58 ], "std": [ 2.65, 1.47 ], "fq": 50 
  },
  "advance": {
    "dict": "happiness", "word": "advance", "stem": "advanc",
    "avg": [ 7.72, 6.58 ], "std": [ 2.16, 1.33 ], "fq": 50 
  },
  "advanced": {
    "dict": "happiness", "word": "advanced", "stem": "advanc",
    "avg": [ 7.72, 6.58 ], "std": [ 2.16, 1.07 ], "fq": 50 
  },
  "arts": {
    "dict": "happiness", "word": "arts", "stem": "art",
    "avg": [ 4.86, 6.58 ], "std": [ 2.88, 1.94 ], "fq": 50 
  },
  "baking": {
    "dict": "happiness", "word": "baking", "stem": "bake",
    "avg": [ 5.10, 6.58 ], "std": [ 2.30, 1.57 ], "fq": 50 
  },
  "colour": {
    "dict": "happiness", "word": "colour", "stem": "colour",
    "avg": [ 4.73, 6.58 ], "std": [ 2.64, 1.53 ], "fq": 50 
  },
  "drawing": {
    "dict": "happiness", "word": "drawing", "stem": "draw",
    "avg": [ 5.36, 6.58 ], "std": [ 2.45, 1.11 ], "fq": 50 
  },
  "fish": {
    "dict": "happiness", "word": "fish", "stem": "fish",
    "avg": [ 4.00, 6.58 ], "std": [ 2.19, 1.75 ], "fq": 50 
  },
  "invented": {
    "dict": "happiness", "word": "invented", "stem": "invent",
    "avg": [ 4.14, 6.58 ], "std": [ 1.98, 1.03 ], "fq": 50 
  },
  "preferred": {
    "dict": "happiness", "word": "preferred", "stem": "prefer",
    "avg": [ 5.10, 6.58 ], "std": [ 2.59, 0.95 ], "fq": 50 
  },
  "radio": {
    "dict": "happiness", "word": "radio", "stem": "radio",
    "avg": [ 4.78, 6.58 ], "std": [ 2.82, 1.60 ], "fq": 50 
  },
  "ready": {
    "dict": "happiness", "word": "ready", "stem": "readi",
    "avg": [ 6.57, 6.58 ], "std": [ 1.78, 1.16 ], "fq": 50 
  },
  "springs": {
    "dict": "happiness", "word": "springs", "stem": "spring",
    "avg": [ 5.67, 6.58 ], "std": [ 2.51, 1.25 ], "fq": 50 
  },
  "student": {
    "dict": "happiness", "word": "student", "stem": "student",
    "avg": [ 5.12, 6.58 ], "std": [ 2.46, 1.25 ], "fq": 50 
  },
  "traditions": {
    "dict": "happiness", "word": "traditions", "stem": "tradit",
    "avg": [ 4.66, 6.58 ], "std": [ 2.12, 1.64 ], "fq": 50 
  },
  "upgrade": {
    "dict": "happiness", "word": "upgrade", "stem": "upgrad",
    "avg": [ 6.44, 6.58 ], "std": [ 2.58, 1.18 ], "fq": 50 
  },
  "saviour": {
    "dict": "happiness", "word": "saviour", "stem": "saviour",
    "avg": [ 5.80, 6.57 ], "std": [ 3.01, 1.53 ], "fq": 50 
  },
  "muscles": {
    "dict": "happiness", "word": "muscles", "stem": "muscl",
    "avg": [ 5.47, 6.56 ], "std": [ 2.20, 1.41 ], "fq": 50 
  },
  "able": {
    "dict": "happiness", "word": "able", "stem": "abl",
    "avg": [ 5.08, 6.56 ], "std": [ 2.07, 1.25 ], "fq": 50 
  },
  "butter": {
    "dict": "happiness", "word": "butter", "stem": "butter",
    "avg": [ 3.17, 6.56 ], "std": [ 1.84, 1.51 ], "fq": 50 
  },
  "diploma": {
    "dict": "happiness", "word": "diploma", "stem": "diploma",
    "avg": [ 5.67, 6.56 ], "std": [ 2.80, 1.74 ], "fq": 50 
  },
  "film": {
    "dict": "happiness", "word": "film", "stem": "film",
    "avg": [ 4.93, 6.56 ], "std": [ 2.54, 1.58 ], "fq": 50 
  },
  "morning": {
    "dict": "happiness", "word": "morning", "stem": "morn",
    "avg": [ 5.06, 6.56 ], "std": [ 3.05, 1.95 ], "fq": 50 
  },
  "natural": {
    "dict": "happiness", "word": "natural", "stem": "natur",
    "avg": [ 4.37, 6.56 ], "std": [ 2.51, 1.49 ], "fq": 50 
  },
  "preservation": {
    "dict": "happiness", "word": "preservation", "stem": "preserv",
    "avg": [ 4.95, 6.56 ], "std": [ 2.19, 1.25 ], "fq": 50 
  },
  "progressive": {
    "dict": "happiness", "word": "progressive", "stem": "progress",
    "avg": [ 6.02, 6.56 ], "std": [ 2.58, 1.33 ], "fq": 50 
  },
  "protection": {
    "dict": "happiness", "word": "protection", "stem": "protect",
    "avg": [ 4.09, 6.56 ], "std": [ 2.77, 1.33 ], "fq": 50 
  },
  "raised": {
    "dict": "happiness", "word": "raised", "stem": "rais",
    "avg": [ 7.17, 6.56 ], "std": [ 2.06, 1.23 ], "fq": 50 
  },
  "showers": {
    "dict": "happiness", "word": "showers", "stem": "shower",
    "avg": [ 4.93, 6.56 ], "std": [ 2.40, 1.05 ], "fq": 50 
  },
  "teach": {
    "dict": "happiness", "word": "teach", "stem": "teach",
    "avg": [ 5.39, 6.56 ], "std": [ 2.22, 1.55 ], "fq": 50 
  },
  "traveler": {
    "dict": "happiness", "word": "traveler", "stem": "travel",
    "avg": [ 6.21, 6.56 ], "std": [ 2.51, 1.45 ], "fq": 50 
  },
  "worldwide": {
    "dict": "happiness", "word": "worldwide", "stem": "worldwid",
    "avg": [ 5.32, 6.56 ], "std": [ 2.39, 1.26 ], "fq": 50 
  },
  "privileges": {
    "dict": "happiness", "word": "privileges", "stem": "privileg",
    "avg": [ 4.54, 6.55 ], "std": [ 1.86, 1.72 ], "fq": 50 
  },
  "accepted": {
    "dict": "happiness", "word": "accepted", "stem": "accept",
    "avg": [ 5.40, 6.54 ], "std": [ 2.70, 1.46 ], "fq": 50 
  },
  "adoption": {
    "dict": "happiness", "word": "adoption", "stem": "adopt",
    "avg": [ 5.40, 6.54 ], "std": [ 2.70, 1.46 ], "fq": 50 
  },
  "cats": {
    "dict": "happiness", "word": "cats", "stem": "cat",
    "avg": [ 4.38, 6.54 ], "std": [ 2.24, 2.02 ], "fq": 50 
  },
  "coin": {
    "dict": "happiness", "word": "coin", "stem": "coin",
    "avg": [ 4.29, 6.54 ], "std": [ 2.48, 1.18 ], "fq": 50 
  },
  "cooked": {
    "dict": "happiness", "word": "cooked", "stem": "cook",
    "avg": [ 4.44, 6.54 ], "std": [ 1.96, 1.09 ], "fq": 50 
  },
  "dawn": {
    "dict": "happiness", "word": "dawn", "stem": "dawn",
    "avg": [ 4.39, 6.54 ], "std": [ 2.81, 1.39 ], "fq": 50 
  },
  "done": {
    "dict": "happiness", "word": "done", "stem": "done",
    "avg": [ 5.71, 6.54 ], "std": [ 2.74, 1.43 ], "fq": 50 
  },
  "eager": {
    "dict": "happiness", "word": "eager", "stem": "eager",
    "avg": [ 2.83, 6.54 ], "std": [ 2.31, 1.31 ], "fq": 50 
  },
  "exercises": {
    "dict": "happiness", "word": "exercises", "stem": "exercis",
    "avg": [ 6.84, 6.54 ], "std": [ 2.06, 1.30 ], "fq": 50 
  },
  "found": {
    "dict": "happiness", "word": "found", "stem": "found",
    "avg": [ 5.42, 6.54 ], "std": [ 2.44, 1.18 ], "fq": 50 
  },
  "give": {
    "dict": "happiness", "word": "give", "stem": "give",
    "avg": [ 5.67, 6.54 ], "std": [ 2.51, 1.73 ], "fq": 50 
  },
  "groovy": {
    "dict": "happiness", "word": "groovy", "stem": "groovi",
    "avg": [ 3.80, 6.54 ], "std": [ 2.18, 1.76 ], "fq": 50 
  },
  "moral": {
    "dict": "happiness", "word": "moral", "stem": "moral",
    "avg": [ 4.49, 6.54 ], "std": [ 2.28, 1.86 ], "fq": 50 
  },
  "overcome": {
    "dict": "happiness", "word": "overcome", "stem": "overcom",
    "avg": [ 7.00, 6.54 ], "std": [ 2.37, 1.67 ], "fq": 50 
  },
  "pays": {
    "dict": "happiness", "word": "pays", "stem": "pay",
    "avg": [ 5.23, 6.54 ], "std": [ 2.21, 1.74 ], "fq": 50 
  },
  "pride": {
    "dict": "happiness", "word": "pride", "stem": "pride",
    "avg": [ 5.83, 6.54 ], "std": [ 2.48, 1.74 ], "fq": 50 
  },
  "right": {
    "dict": "happiness", "word": "right", "stem": "right",
    "avg": [ 5.61, 6.54 ], "std": [ 2.38, 1.27 ], "fq": 50 
  },
  "rising": {
    "dict": "happiness", "word": "rising", "stem": "rise",
    "avg": [ 6.56, 6.54 ], "std": [ 2.34, 1.11 ], "fq": 50 
  },
  "save": {
    "dict": "happiness", "word": "save", "stem": "save",
    "avg": [ 4.95, 6.54 ], "std": [ 2.19, 1.16 ], "fq": 50 
  },
  "scholars": {
    "dict": "happiness", "word": "scholars", "stem": "scholar",
    "avg": [ 5.12, 6.54 ], "std": [ 2.46, 1.30 ], "fq": 50 
  },
  "shelter": {
    "dict": "happiness", "word": "shelter", "stem": "shelter",
    "avg": [ 4.28, 6.54 ], "std": [ 1.77, 1.31 ], "fq": 50 
  },
  "tasting": {
    "dict": "happiness", "word": "tasting", "stem": "tast",
    "avg": [ 5.22, 6.54 ], "std": [ 2.38, 1.15 ], "fq": 50 
  },
  "visit": {
    "dict": "happiness", "word": "visit", "stem": "visit",
    "avg": [ 5.74, 6.54 ], "std": [ 2.38, 1.20 ], "fq": 50 
  },
  "advantages": {
    "dict": "happiness", "word": "advantages", "stem": "advantag",
    "avg": [ 4.76, 6.53 ], "std": [ 2.18, 1.37 ], "fq": 50 
  },
  "sailed": {
    "dict": "happiness", "word": "sailed", "stem": "sail",
    "avg": [ 5.55, 6.53 ], "std": [ 2.23, 1.53 ], "fq": 50 
  },
  "feather": {
    "dict": "happiness", "word": "feather", "stem": "feather",
    "avg": [ 3.18, 6.52 ], "std": [ 1.76, 1.32 ], "fq": 50 
  },
  "brain": {
    "dict": "happiness", "word": "brain", "stem": "brain",
    "avg": [ 5.00, 6.52 ], "std": [ 2.68, 1.53 ], "fq": 50 
  },
  "champ": {
    "dict": "happiness", "word": "champ", "stem": "champ",
    "avg": [ 6.00, 6.52 ], "std": [ 2.43, 1.87 ], "fq": 50 
  },
  "ease": {
    "dict": "happiness", "word": "ease", "stem": "eas",
    "avg": [ 4.48, 6.52 ], "std": [ 2.82, 1.59 ], "fq": 50 
  },
  "ethics": {
    "dict": "happiness", "word": "ethics", "stem": "ethic",
    "avg": [ 4.49, 6.52 ], "std": [ 2.28, 1.36 ], "fq": 50 
  },
  "fries": {
    "dict": "happiness", "word": "fries", "stem": "fri",
    "avg": [ 5.55, 6.52 ], "std": [ 2.29, 1.37 ], "fq": 50 
  },
  "growing": {
    "dict": "happiness", "word": "growing", "stem": "grow",
    "avg": [ 3.90, 6.52 ], "std": [ 1.95, 0.99 ], "fq": 50 
  },
  "nights": {
    "dict": "happiness", "word": "nights", "stem": "night",
    "avg": [ 4.28, 6.52 ], "std": [ 2.21, 1.52 ], "fq": 50 
  },
  "prefer": {
    "dict": "happiness", "word": "prefer", "stem": "prefer",
    "avg": [ 4.54, 6.52 ], "std": [ 1.86, 1.03 ], "fq": 50 
  },
  "read": {
    "dict": "happiness", "word": "read", "stem": "read",
    "avg": [ 5.39, 6.52 ], "std": [ 2.22, 1.58 ], "fq": 50 
  },
  "sang": {
    "dict": "happiness", "word": "sang", "stem": "sang",
    "avg": [ 4.69, 6.52 ], "std": [ 1.99, 1.31 ], "fq": 50 
  },
  "swimming": {
    "dict": "happiness", "word": "swimming", "stem": "swim",
    "avg": [ 6.57, 6.52 ], "std": [ 2.33, 1.22 ], "fq": 50 
  },
  "world": {
    "dict": "happiness", "word": "world", "stem": "world",
    "avg": [ 5.32, 6.52 ], "std": [ 2.39, 1.66 ], "fq": 50 
  },
  "bounce": {
    "dict": "happiness", "word": "bounce", "stem": "bounc",
    "avg": [ 5.67, 6.51 ], "std": [ 2.51, 1.50 ], "fq": 50 
  },
  "eden": {
    "dict": "happiness", "word": "eden", "stem": "eden",
    "avg": [ 5.61, 6.51 ], "std": [ 3.20, 1.56 ], "fq": 50 
  },
  "agriculture": {
    "dict": "happiness", "word": "agriculture", "stem": "agricultur",
    "avg": [ 3.90, 6.50 ], "std": [ 1.95, 1.30 ], "fq": 50 
  },
  "allies": {
    "dict": "happiness", "word": "allies", "stem": "alli",
    "avg": [ 5.11, 6.50 ], "std": [ 2.96, 1.25 ], "fq": 50 
  },
  "couples": {
    "dict": "happiness", "word": "couples", "stem": "coupl",
    "avg": [ 6.39, 6.50 ], "std": [ 2.31, 1.20 ], "fq": 50 
  },
  "deals": {
    "dict": "happiness", "word": "deals", "stem": "deal",
    "avg": [ 5.49, 6.50 ], "std": [ 2.43, 1.58 ], "fq": 50 
  },
  "determined": {
    "dict": "happiness", "word": "determined", "stem": "determin",
    "avg": [ 4.07, 6.50 ], "std": [ 1.98, 1.53 ], "fq": 50 
  },
  "eaten": {
    "dict": "happiness", "word": "eaten", "stem": "eaten",
    "avg": [ 5.69, 6.50 ], "std": [ 2.51, 1.22 ], "fq": 50 
  },
  "fame": {
    "dict": "happiness", "word": "fame", "stem": "fame",
    "avg": [ 6.55, 6.50 ], "std": [ 2.46, 1.74 ], "fq": 50 
  },
  "gives": {
    "dict": "happiness", "word": "gives", "stem": "give",
    "avg": [ 5.67, 6.50 ], "std": [ 2.51, 1.28 ], "fq": 50 
  },
  "hire": {
    "dict": "happiness", "word": "hire", "stem": "hire",
    "avg": [ 6.77, 6.50 ], "std": [ 2.07, 1.34 ], "fq": 50 
  },
  "innocence": {
    "dict": "happiness", "word": "innocence", "stem": "innoc",
    "avg": [ 4.21, 6.50 ], "std": [ 1.99, 1.73 ], "fq": 50 
  },
  "leadership": {
    "dict": "happiness", "word": "leadership", "stem": "leadership",
    "avg": [ 6.27, 6.50 ], "std": [ 2.18, 1.59 ], "fq": 50 
  },
  "legend": {
    "dict": "happiness", "word": "legend", "stem": "legend",
    "avg": [ 4.88, 6.50 ], "std": [ 1.76, 1.43 ], "fq": 50 
  },
  "newest": {
    "dict": "happiness", "word": "newest", "stem": "newest",
    "avg": [ 5.64, 6.50 ], "std": [ 2.51, 1.56 ], "fq": 50 
  },
  "performing": {
    "dict": "happiness", "word": "performing", "stem": "perform",
    "avg": [ 5.71, 6.50 ], "std": [ 2.74, 1.31 ], "fq": 50 
  },
  "roast": {
    "dict": "happiness", "word": "roast", "stem": "roast",
    "avg": [ 5.83, 6.50 ], "std": [ 2.73, 1.45 ], "fq": 50 
  },
  "starting": {
    "dict": "happiness", "word": "starting", "stem": "start",
    "avg": [ 3.82, 6.50 ], "std": [ 2.24, 1.05 ], "fq": 50 
  },
  "grows": {
    "dict": "happiness", "word": "grows", "stem": "grow",
    "avg": [ 3.90, 6.49 ], "std": [ 1.95, 1.36 ], "fq": 50 
  },
  "rays": {
    "dict": "happiness", "word": "rays", "stem": "ray",
    "avg": [ 4.02, 6.49 ], "std": [ 1.94, 1.42 ], "fq": 50 
  },
  "answers": {
    "dict": "happiness", "word": "answers", "stem": "answer",
    "avg": [ 5.41, 6.48 ], "std": [ 2.43, 1.15 ], "fq": 50 
  },
  "boost": {
    "dict": "happiness", "word": "boost", "stem": "boost",
    "avg": [ 6.44, 6.48 ], "std": [ 2.58, 1.23 ], "fq": 50 
  },
  "humble": {
    "dict": "happiness", "word": "humble", "stem": "humbl",
    "avg": [ 3.74, 6.48 ], "std": [ 2.33, 1.30 ], "fq": 50 
  },
  "mate": {
    "dict": "happiness", "word": "mate", "stem": "mate",
    "avg": [ 6.39, 6.48 ], "std": [ 2.31, 1.78 ], "fq": 50 
  },
  "offers": {
    "dict": "happiness", "word": "offers", "stem": "offer",
    "avg": [ 4.88, 6.48 ], "std": [ 2.30, 1.55 ], "fq": 50 
  },
  "perform": {
    "dict": "happiness", "word": "perform", "stem": "perform",
    "avg": [ 5.71, 6.48 ], "std": [ 2.74, 1.23 ], "fq": 50 
  },
  "restored": {
    "dict": "happiness", "word": "restored", "stem": "restor",
    "avg": [ 5.86, 6.48 ], "std": [ 2.70, 1.22 ], "fq": 50 
  },
  "scholar": {
    "dict": "happiness", "word": "scholar", "stem": "scholar",
    "avg": [ 5.12, 6.48 ], "std": [ 2.46, 1.13 ], "fq": 50 
  },
  "sings": {
    "dict": "happiness", "word": "sings", "stem": "sing",
    "avg": [ 4.69, 6.48 ], "std": [ 1.99, 1.79 ], "fq": 50 
  },
  "soft": {
    "dict": "happiness", "word": "soft", "stem": "soft",
    "avg": [ 4.63, 6.48 ], "std": [ 2.61, 1.22 ], "fq": 50 
  },
  "story": {
    "dict": "happiness", "word": "story", "stem": "stori",
    "avg": [ 3.93, 6.48 ], "std": [ 2.29, 1.34 ], "fq": 50 
  },
  "supporting": {
    "dict": "happiness", "word": "supporting", "stem": "support",
    "avg": [ 3.93, 6.48 ], "std": [ 2.49, 0.97 ], "fq": 50 
  },
  "drums": {
    "dict": "happiness", "word": "drums", "stem": "drum",
    "avg": [ 3.36, 6.47 ], "std": [ 2.28, 1.58 ], "fq": 50 
  },
  "virtue": {
    "dict": "happiness", "word": "virtue", "stem": "virtu",
    "avg": [ 4.52, 6.47 ], "std": [ 2.52, 1.77 ], "fq": 50 
  },
  "activities": {
    "dict": "happiness", "word": "activities", "stem": "activ",
    "avg": [ 4.86, 6.46 ], "std": [ 2.56, 1.22 ], "fq": 50 
  },
  "athletic": {
    "dict": "happiness", "word": "athletic", "stem": "athlet",
    "avg": [ 6.10, 6.46 ], "std": [ 2.29, 1.51 ], "fq": 50 
  },
  "clothes": {
    "dict": "happiness", "word": "clothes", "stem": "cloth",
    "avg": [ 4.78, 6.46 ], "std": [ 2.88, 1.23 ], "fq": 50 
  },
  "cultivated": {
    "dict": "happiness", "word": "cultivated", "stem": "cultiv",
    "avg": [ 4.37, 6.46 ], "std": [ 2.51, 1.36 ], "fq": 50 
  },
  "goods": {
    "dict": "happiness", "word": "goods", "stem": "good",
    "avg": [ 5.43, 6.46 ], "std": [ 2.85, 1.15 ], "fq": 50 
  },
  "grass": {
    "dict": "happiness", "word": "grass", "stem": "grass",
    "avg": [ 4.14, 6.46 ], "std": [ 2.11, 1.39 ], "fq": 50 
  },
  "memory": {
    "dict": "happiness", "word": "memory", "stem": "memori",
    "avg": [ 5.42, 6.46 ], "std": [ 2.25, 1.28 ], "fq": 50 
  },
  "mint": {
    "dict": "happiness", "word": "mint", "stem": "mint",
    "avg": [ 5.49, 6.46 ], "std": [ 2.43, 1.31 ], "fq": 50 
  },
  "prime": {
    "dict": "happiness", "word": "prime", "stem": "prime",
    "avg": [ 4.00, 6.46 ], "std": [ 2.44, 1.28 ], "fq": 50 
  },
  "prospect": {
    "dict": "happiness", "word": "prospect", "stem": "prospect",
    "avg": [ 5.38, 6.46 ], "std": [ 2.58, 1.50 ], "fq": 50 
  },
  "resource": {
    "dict": "happiness", "word": "resource", "stem": "resourc",
    "avg": [ 5.98, 6.46 ], "std": [ 2.14, 1.51 ], "fq": 50 
  },
  "resources": {
    "dict": "happiness", "word": "resources", "stem": "resourc",
    "avg": [ 5.98, 6.46 ], "std": [ 2.14, 1.15 ], "fq": 50 
  },
  "rocking": {
    "dict": "happiness", "word": "rocking", "stem": "rock",
    "avg": [ 4.52, 6.46 ], "std": [ 2.37, 1.47 ], "fq": 50 
  },
  "scored": {
    "dict": "happiness", "word": "scored", "stem": "score",
    "avg": [ 5.73, 6.46 ], "std": [ 2.09, 1.64 ], "fq": 50 
  },
  "tender": {
    "dict": "happiness", "word": "tender", "stem": "tender",
    "avg": [ 4.88, 6.45 ], "std": [ 2.30, 1.72 ], "fq": 50 
  },
  "chance": {
    "dict": "happiness", "word": "chance", "stem": "chanc",
    "avg": [ 5.38, 6.44 ], "std": [ 2.58, 1.42 ], "fq": 50 
  },
  "coast": {
    "dict": "happiness", "word": "coast", "stem": "coast",
    "avg": [ 4.59, 6.44 ], "std": [ 2.31, 1.39 ], "fq": 50 
  },
  "earth": {
    "dict": "happiness", "word": "earth", "stem": "earth",
    "avg": [ 4.24, 6.44 ], "std": [ 2.49, 1.82 ], "fq": 50 
  },
  "eats": {
    "dict": "happiness", "word": "eats", "stem": "eat",
    "avg": [ 5.69, 6.44 ], "std": [ 2.51, 1.64 ], "fq": 50 
  },
  "familiar": {
    "dict": "happiness", "word": "familiar", "stem": "familiar",
    "avg": [ 6.98, 6.44 ], "std": [ 2.21, 1.26 ], "fq": 50 
  },
  "fast": {
    "dict": "happiness", "word": "fast", "stem": "fast",
    "avg": [ 5.16, 6.44 ], "std": [ 2.42, 1.23 ], "fq": 50 
  },
  "gained": {
    "dict": "happiness", "word": "gained", "stem": "gain",
    "avg": [ 7.72, 6.44 ], "std": [ 2.16, 1.59 ], "fq": 50 
  },
  "graphics": {
    "dict": "happiness", "word": "graphics", "stem": "graphic",
    "avg": [ 4.86, 6.44 ], "std": [ 2.88, 1.25 ], "fq": 50 
  },
  "improve": {
    "dict": "happiness", "word": "improve", "stem": "improv",
    "avg": [ 5.69, 6.44 ], "std": [ 2.15, 1.50 ], "fq": 50 
  },
  "infinite": {
    "dict": "happiness", "word": "infinite", "stem": "infinit",
    "avg": [ 5.14, 6.44 ], "std": [ 2.54, 1.50 ], "fq": 50 
  },
  "nap": {
    "dict": "happiness", "word": "nap", "stem": "nap",
    "avg": [ 2.80, 6.44 ], "std": [ 2.66, 1.92 ], "fq": 50 
  },
  "professional": {
    "dict": "happiness", "word": "professional", "stem": "profession",
    "avg": [ 5.20, 6.44 ], "std": [ 2.85, 1.16 ], "fq": 50 
  },
  "rides": {
    "dict": "happiness", "word": "rides", "stem": "ride",
    "avg": [ 5.15, 6.44 ], "std": [ 3.04, 1.34 ], "fq": 50 
  },
  "satisfactory": {
    "dict": "happiness", "word": "satisfactory", "stem": "satisfactori",
    "avg": [ 5.40, 6.44 ], "std": [ 2.70, 1.61 ], "fq": 50 
  },
  "scoring": {
    "dict": "happiness", "word": "scoring", "stem": "score",
    "avg": [ 5.73, 6.44 ], "std": [ 2.09, 1.25 ], "fq": 50 
  },
  "support": {
    "dict": "happiness", "word": "support", "stem": "support",
    "avg": [ 5.53, 6.44 ], "std": [ 2.90, 1.43 ], "fq": 50 
  },
  "teachers": {
    "dict": "happiness", "word": "teachers", "stem": "teacher",
    "avg": [ 4.05, 6.44 ], "std": [ 2.61, 1.30 ], "fq": 50 
  },
  "teaching": {
    "dict": "happiness", "word": "teaching", "stem": "teach",
    "avg": [ 5.39, 6.44 ], "std": [ 2.22, 1.20 ], "fq": 50 
  },
  "wage": {
    "dict": "happiness", "word": "wage", "stem": "wage",
    "avg": [ 6.77, 6.44 ], "std": [ 2.07, 1.30 ], "fq": 50 
  },
  "wink": {
    "dict": "happiness", "word": "wink", "stem": "wink",
    "avg": [ 5.44, 6.44 ], "std": [ 2.68, 1.15 ], "fq": 50 
  },
  "wit": {
    "dict": "happiness", "word": "wit", "stem": "wit",
    "avg": [ 5.42, 6.44 ], "std": [ 2.44, 1.51 ], "fq": 50 
  },
  "accept": {
    "dict": "happiness", "word": "accept", "stem": "accept",
    "avg": [ 5.40, 6.42 ], "std": [ 2.70, 1.07 ], "fq": 50 
  },
  "band": {
    "dict": "happiness", "word": "band", "stem": "band",
    "avg": [ 3.86, 6.42 ], "std": [ 2.13, 1.55 ], "fq": 50 
  },
  "chat": {
    "dict": "happiness", "word": "chat", "stem": "chat",
    "avg": [ 5.74, 6.42 ], "std": [ 2.38, 1.18 ], "fq": 50 
  },
  "contribution": {
    "dict": "happiness", "word": "contribution", "stem": "contribut",
    "avg": [ 3.82, 6.42 ], "std": [ 2.24, 1.49 ], "fq": 50 
  },
  "curves": {
    "dict": "happiness", "word": "curves", "stem": "curv",
    "avg": [ 5.00, 6.42 ], "std": [ 2.32, 1.23 ], "fq": 50 
  },
  "dates": {
    "dict": "happiness", "word": "dates", "stem": "date",
    "avg": [ 6.77, 6.42 ], "std": [ 2.07, 1.29 ], "fq": 50 
  },
  "delivered": {
    "dict": "happiness", "word": "delivered", "stem": "deliv",
    "avg": [ 4.95, 6.42 ], "std": [ 2.19, 1.20 ], "fq": 50 
  },
  "feed": {
    "dict": "happiness", "word": "feed", "stem": "feed",
    "avg": [ 5.69, 6.42 ], "std": [ 2.51, 1.20 ], "fq": 50 
  },
  "gaming": {
    "dict": "happiness", "word": "gaming", "stem": "game",
    "avg": [ 5.89, 6.42 ], "std": [ 2.37, 1.87 ], "fq": 50 
  },
  "interests": {
    "dict": "happiness", "word": "interests", "stem": "interest",
    "avg": [ 5.66, 6.42 ], "std": [ 2.26, 1.77 ], "fq": 50 
  },
  "jazz": {
    "dict": "happiness", "word": "jazz", "stem": "jazz",
    "avg": [ 6.38, 6.42 ], "std": [ 2.68, 1.46 ], "fq": 50 
  },
  "traveled": {
    "dict": "happiness", "word": "traveled", "stem": "travel",
    "avg": [ 6.21, 6.42 ], "std": [ 2.51, 1.39 ], "fq": 50 
  },
  "wine": {
    "dict": "happiness", "word": "wine", "stem": "wine",
    "avg": [ 4.78, 6.42 ], "std": [ 2.34, 2.12 ], "fq": 50 
  },
  "wondered": {
    "dict": "happiness", "word": "wondered", "stem": "wonder",
    "avg": [ 5.00, 6.42 ], "std": [ 2.23, 1.28 ], "fq": 50 
  },
  "farming": {
    "dict": "happiness", "word": "farming", "stem": "farm",
    "avg": [ 3.90, 6.42 ], "std": [ 1.95, 1.53 ], "fq": 50 
  },
  "hats": {
    "dict": "happiness", "word": "hats", "stem": "hat",
    "avg": [ 4.10, 6.41 ], "std": [ 2.00, 1.32 ], "fq": 50 
  },
  "hearted": {
    "dict": "happiness", "word": "hearted", "stem": "heart",
    "avg": [ 6.34, 6.41 ], "std": [ 2.25, 1.38 ], "fq": 50 
  },
  "baked": {
    "dict": "happiness", "word": "baked", "stem": "bake",
    "avg": [ 5.10, 6.40 ], "std": [ 2.30, 1.88 ], "fq": 50 
  },
  "buying": {
    "dict": "happiness", "word": "buying", "stem": "buy",
    "avg": [ 4.67, 6.40 ], "std": [ 2.35, 1.29 ], "fq": 50 
  },
  "chicken": {
    "dict": "happiness", "word": "chicken", "stem": "chicken",
    "avg": [ 4.43, 6.40 ], "std": [ 2.05, 1.63 ], "fq": 50 
  },
  "drawings": {
    "dict": "happiness", "word": "drawings", "stem": "draw",
    "avg": [ 5.36, 6.40 ], "std": [ 2.45, 1.51 ], "fq": 50 
  },
  "educational": {
    "dict": "happiness", "word": "educational", "stem": "educ",
    "avg": [ 5.74, 6.40 ], "std": [ 2.46, 1.48 ], "fq": 50 
  },
  "gain": {
    "dict": "happiness", "word": "gain", "stem": "gain",
    "avg": [ 7.72, 6.40 ], "std": [ 2.16, 1.54 ], "fq": 50 
  },
  "kidding": {
    "dict": "happiness", "word": "kidding", "stem": "kid",
    "avg": [ 5.27, 6.40 ], "std": [ 2.36, 1.37 ], "fq": 50 
  },
  "light": {
    "dict": "happiness", "word": "light", "stem": "light",
    "avg": [ 5.40, 6.40 ], "std": [ 2.33, 1.51 ], "fq": 50 
  },
  "mountain": {
    "dict": "happiness", "word": "mountain", "stem": "mountain",
    "avg": [ 5.49, 6.40 ], "std": [ 2.43, 1.71 ], "fq": 50 
  },
  "pics": {
    "dict": "happiness", "word": "pics", "stem": "pic",
    "avg": [ 4.93, 6.40 ], "std": [ 2.54, 1.36 ], "fq": 50 
  },
  "poetry": {
    "dict": "happiness", "word": "poetry", "stem": "poetri",
    "avg": [ 4.00, 6.40 ], "std": [ 2.85, 1.91 ], "fq": 50 
  },
  "possibility": {
    "dict": "happiness", "word": "possibility", "stem": "possibl",
    "avg": [ 4.62, 6.40 ], "std": [ 1.94, 1.25 ], "fq": 50 
  },
  "resolved": {
    "dict": "happiness", "word": "resolved", "stem": "resolv",
    "avg": [ 5.41, 6.40 ], "std": [ 2.43, 1.47 ], "fq": 50 
  },
  "studies": {
    "dict": "happiness", "word": "studies", "stem": "studi",
    "avg": [ 4.08, 6.40 ], "std": [ 2.41, 1.37 ], "fq": 50 
  },
  "tennis": {
    "dict": "happiness", "word": "tennis", "stem": "tenni",
    "avg": [ 4.61, 6.40 ], "std": [ 2.60, 1.41 ], "fq": 50 
  },
  "touch": {
    "dict": "happiness", "word": "touch", "stem": "touch",
    "avg": [ 6.21, 6.40 ], "std": [ 2.75, 1.28 ], "fq": 50 
  },
  "touched": {
    "dict": "happiness", "word": "touched", "stem": "touch",
    "avg": [ 6.21, 6.40 ], "std": [ 2.75, 1.23 ], "fq": 50 
  },
  "tradition": {
    "dict": "happiness", "word": "tradition", "stem": "tradit",
    "avg": [ 4.66, 6.40 ], "std": [ 2.12, 1.62 ], "fq": 50 
  },
  "twins": {
    "dict": "happiness", "word": "twins", "stem": "twin",
    "avg": [ 6.39, 6.40 ], "std": [ 2.31, 1.65 ], "fq": 50 
  },
  "visits": {
    "dict": "happiness", "word": "visits", "stem": "visit",
    "avg": [ 5.74, 6.40 ], "std": [ 2.38, 1.29 ], "fq": 50 
  },
  "wages": {
    "dict": "happiness", "word": "wages", "stem": "wage",
    "avg": [ 6.77, 6.40 ], "std": [ 2.07, 1.34 ], "fq": 50 
  },
  "younger": {
    "dict": "happiness", "word": "younger", "stem": "younger",
    "avg": [ 5.64, 6.40 ], "std": [ 2.51, 1.50 ], "fq": 50 
  },
  "exercised": {
    "dict": "happiness", "word": "exercised", "stem": "exercis",
    "avg": [ 6.84, 6.39 ], "std": [ 2.06, 1.58 ], "fq": 50 
  },
  "seeds": {
    "dict": "happiness", "word": "seeds", "stem": "seed",
    "avg": [ 4.49, 6.39 ], "std": [ 2.24, 1.50 ], "fq": 50 
  },
  "bigger": {
    "dict": "happiness", "word": "bigger", "stem": "bigger",
    "avg": [ 4.76, 6.38 ], "std": [ 1.95, 1.40 ], "fq": 50 
  },
  "breath": {
    "dict": "happiness", "word": "breath", "stem": "breath",
    "avg": [ 6.98, 6.38 ], "std": [ 2.21, 1.58 ], "fq": 50 
  },
  "committed": {
    "dict": "happiness", "word": "committed", "stem": "commit",
    "avg": [ 5.12, 6.38 ], "std": [ 2.42, 1.41 ], "fq": 50 
  },
  "designers": {
    "dict": "happiness", "word": "designers", "stem": "design",
    "avg": [ 5.14, 6.38 ], "std": [ 2.39, 1.48 ], "fq": 50 
  },
  "faster": {
    "dict": "happiness", "word": "faster", "stem": "faster",
    "avg": [ 5.16, 6.38 ], "std": [ 2.42, 1.35 ], "fq": 50 
  },
  "lamb": {
    "dict": "happiness", "word": "lamb", "stem": "lamb",
    "avg": [ 3.36, 6.38 ], "std": [ 2.18, 1.26 ], "fq": 50 
  },
  "leader": {
    "dict": "happiness", "word": "leader", "stem": "leader",
    "avg": [ 6.27, 6.38 ], "std": [ 2.18, 1.34 ], "fq": 50 
  },
  "lottery": {
    "dict": "happiness", "word": "lottery", "stem": "lotteri",
    "avg": [ 5.36, 6.38 ], "std": [ 2.45, 2.13 ], "fq": 50 
  },
  "meet": {
    "dict": "happiness", "word": "meet", "stem": "meet",
    "avg": [ 4.94, 6.38 ], "std": [ 2.63, 1.26 ], "fq": 50 
  },
  "played": {
    "dict": "happiness", "word": "played", "stem": "play",
    "avg": [ 5.11, 6.38 ], "std": [ 2.84, 1.43 ], "fq": 50 
  },
  "preserve": {
    "dict": "happiness", "word": "preserve", "stem": "preserv",
    "avg": [ 4.95, 6.38 ], "std": [ 2.19, 1.50 ], "fq": 50 
  },
  "queens": {
    "dict": "happiness", "word": "queens", "stem": "queen",
    "avg": [ 4.76, 6.38 ], "std": [ 2.18, 1.66 ], "fq": 50 
  },
  "sails": {
    "dict": "happiness", "word": "sails", "stem": "sail",
    "avg": [ 5.55, 6.38 ], "std": [ 2.23, 1.38 ], "fq": 50 
  },
  "saves": {
    "dict": "happiness", "word": "saves", "stem": "save",
    "avg": [ 4.95, 6.38 ], "std": [ 2.19, 1.52 ], "fq": 50 
  },
  "score": {
    "dict": "happiness", "word": "score", "stem": "score",
    "avg": [ 5.73, 6.38 ], "std": [ 2.09, 1.09 ], "fq": 50 
  },
  "seeing": {
    "dict": "happiness", "word": "seeing", "stem": "see",
    "avg": [ 6.10, 6.38 ], "std": [ 2.19, 1.31 ], "fq": 50 
  },
  "sung": {
    "dict": "happiness", "word": "sung", "stem": "sung",
    "avg": [ 4.69, 6.38 ], "std": [ 1.99, 1.24 ], "fq": 50 
  },
  "tasted": {
    "dict": "happiness", "word": "tasted", "stem": "tast",
    "avg": [ 5.22, 6.38 ], "std": [ 2.38, 1.32 ], "fq": 50 
  },
  "tastes": {
    "dict": "happiness", "word": "tastes", "stem": "tast",
    "avg": [ 5.22, 6.38 ], "std": [ 2.38, 1.76 ], "fq": 50 
  },
  "thinks": {
    "dict": "happiness", "word": "thinks", "stem": "think",
    "avg": [ 5.98, 6.38 ], "std": [ 2.14, 1.23 ], "fq": 50 
  },
  "thought": {
    "dict": "happiness", "word": "thought", "stem": "thought",
    "avg": [ 5.72, 6.38 ], "std": [ 2.30, 1.34 ], "fq": 50 
  },
  "touches": {
    "dict": "happiness", "word": "touches", "stem": "touch",
    "avg": [ 6.21, 6.38 ], "std": [ 2.75, 1.26 ], "fq": 50 
  },
  "agricultural": {
    "dict": "happiness", "word": "agricultural", "stem": "agricultur",
    "avg": [ 3.90, 6.38 ], "std": [ 1.95, 1.45 ], "fq": 50 
  },
  "acquire": {
    "dict": "happiness", "word": "acquire", "stem": "acquir",
    "avg": [ 7.72, 6.36 ], "std": [ 2.16, 1.32 ], "fq": 50 
  },
  "calm": {
    "dict": "happiness", "word": "calm", "stem": "calm",
    "avg": [ 2.82, 6.36 ], "std": [ 2.13, 1.60 ], "fq": 50 
  },
  "curious": {
    "dict": "happiness", "word": "curious", "stem": "curiou",
    "avg": [ 4.27, 6.36 ], "std": [ 2.46, 1.27 ], "fq": 50 
  },
  "developed": {
    "dict": "happiness", "word": "developed", "stem": "develop",
    "avg": [ 5.74, 6.36 ], "std": [ 2.46, 1.48 ], "fq": 50 
  },
  "distinguished": {
    "dict": "happiness", "word": "distinguished", "stem": "distinguish",
    "avg": [ 5.26, 6.36 ], "std": [ 2.36, 1.43 ], "fq": 50 
  },
  "dressed": {
    "dict": "happiness", "word": "dressed", "stem": "dress",
    "avg": [ 4.05, 6.36 ], "std": [ 1.89, 1.12 ], "fq": 50 
  },
  "drink": {
    "dict": "happiness", "word": "drink", "stem": "drink",
    "avg": [ 5.21, 6.36 ], "std": [ 2.46, 1.77 ], "fq": 50 
  },
  "employment": {
    "dict": "happiness", "word": "employment", "stem": "employ",
    "avg": [ 5.28, 6.36 ], "std": [ 2.12, 1.78 ], "fq": 50 
  },
  "farms": {
    "dict": "happiness", "word": "farms", "stem": "farm",
    "avg": [ 3.90, 6.36 ], "std": [ 1.95, 1.51 ], "fq": 50 
  },
  "fashion": {
    "dict": "happiness", "word": "fashion", "stem": "fashion",
    "avg": [ 4.56, 6.36 ], "std": [ 1.78, 1.80 ], "fq": 50 
  },
  "imagined": {
    "dict": "happiness", "word": "imagined", "stem": "imagin",
    "avg": [ 5.98, 6.36 ], "std": [ 2.14, 1.50 ], "fq": 50 
  },
  "innocent": {
    "dict": "happiness", "word": "innocent", "stem": "innoc",
    "avg": [ 4.21, 6.36 ], "std": [ 1.99, 1.38 ], "fq": 50 
  },
  "interest": {
    "dict": "happiness", "word": "interest", "stem": "interest",
    "avg": [ 5.66, 6.36 ], "std": [ 2.26, 1.54 ], "fq": 50 
  },
  "justified": {
    "dict": "happiness", "word": "justified", "stem": "justifi",
    "avg": [ 4.48, 6.36 ], "std": [ 2.29, 1.21 ], "fq": 50 
  },
  "mail": {
    "dict": "happiness", "word": "mail", "stem": "mail",
    "avg": [ 5.63, 6.36 ], "std": [ 2.36, 1.69 ], "fq": 50 
  },
  "mobile": {
    "dict": "happiness", "word": "mobile", "stem": "mobil",
    "avg": [ 5.00, 6.36 ], "std": [ 2.18, 1.21 ], "fq": 50 
  },
  "original": {
    "dict": "happiness", "word": "original", "stem": "origin",
    "avg": [ 5.20, 6.36 ], "std": [ 2.85, 1.44 ], "fq": 50 
  },
  "performed": {
    "dict": "happiness", "word": "performed", "stem": "perform",
    "avg": [ 5.71, 6.36 ], "std": [ 2.74, 1.47 ], "fq": 50 
  },
  "please": {
    "dict": "happiness", "word": "please", "stem": "pleas",
    "avg": [ 5.44, 6.36 ], "std": [ 2.88, 1.68 ], "fq": 50 
  },
  "rain": {
    "dict": "happiness", "word": "rain", "stem": "rain",
    "avg": [ 3.65, 6.36 ], "std": [ 2.35, 1.91 ], "fq": 50 
  },
  "relation": {
    "dict": "happiness", "word": "relation", "stem": "relat",
    "avg": [ 7.00, 6.36 ], "std": [ 2.07, 1.16 ], "fq": 50 
  },
  "teacher": {
    "dict": "happiness", "word": "teacher", "stem": "teacher",
    "avg": [ 4.05, 6.36 ], "std": [ 2.61, 1.54 ], "fq": 50 
  },
  "technologies": {
    "dict": "happiness", "word": "technologies", "stem": "technolog",
    "avg": [ 3.98, 6.36 ], "std": [ 2.33, 1.69 ], "fq": 50 
  },
  "value": {
    "dict": "happiness", "word": "value", "stem": "valu",
    "avg": [ 6.75, 6.36 ], "std": [ 2.30, 1.24 ], "fq": 50 
  },
  "branches": {
    "dict": "happiness", "word": "branches", "stem": "branch",
    "avg": [ 3.96, 6.35 ], "std": [ 1.94, 1.20 ], "fq": 50 
  },
  "existed": {
    "dict": "happiness", "word": "existed", "stem": "exist",
    "avg": [ 5.53, 6.35 ], "std": [ 2.90, 1.44 ], "fq": 50 
  },
  "bread": {
    "dict": "happiness", "word": "bread", "stem": "bread",
    "avg": [ 5.64, 6.34 ], "std": [ 2.18, 1.76 ], "fq": 50 
  },
  "castle": {
    "dict": "happiness", "word": "castle", "stem": "castl",
    "avg": [ 5.10, 6.34 ], "std": [ 2.75, 1.71 ], "fq": 50 
  },
  "clouds": {
    "dict": "happiness", "word": "clouds", "stem": "cloud",
    "avg": [ 3.30, 6.34 ], "std": [ 2.08, 1.98 ], "fq": 50 
  },
  "connected": {
    "dict": "happiness", "word": "connected", "stem": "connect",
    "avg": [ 3.75, 6.34 ], "std": [ 2.49, 0.98 ], "fq": 50 
  },
  "employ": {
    "dict": "happiness", "word": "employ", "stem": "employ",
    "avg": [ 5.28, 6.34 ], "std": [ 2.12, 1.42 ], "fq": 50 
  },
  "exists": {
    "dict": "happiness", "word": "exists", "stem": "exist",
    "avg": [ 5.53, 6.34 ], "std": [ 2.90, 1.35 ], "fq": 50 
  },
  "experience": {
    "dict": "happiness", "word": "experience", "stem": "experi",
    "avg": [ 5.53, 6.34 ], "std": [ 2.90, 1.21 ], "fq": 50 
  },
  "hiring": {
    "dict": "happiness", "word": "hiring", "stem": "hire",
    "avg": [ 6.77, 6.34 ], "std": [ 2.07, 1.80 ], "fq": 50 
  },
  "house": {
    "dict": "happiness", "word": "house", "stem": "hous",
    "avg": [ 4.56, 6.34 ], "std": [ 2.41, 1.62 ], "fq": 50 
  },
  "lord": {
    "dict": "happiness", "word": "lord", "stem": "lord",
    "avg": [ 5.20, 6.34 ], "std": [ 2.85, 1.83 ], "fq": 50 
  },
  "released": {
    "dict": "happiness", "word": "released", "stem": "releas",
    "avg": [ 5.15, 6.34 ], "std": [ 3.04, 1.52 ], "fq": 50 
  },
  "saint": {
    "dict": "happiness", "word": "saint", "stem": "saint",
    "avg": [ 4.49, 6.34 ], "std": [ 1.90, 1.80 ], "fq": 50 
  },
  "soon": {
    "dict": "happiness", "word": "soon", "stem": "soon",
    "avg": [ 5.12, 6.34 ], "std": [ 2.39, 0.89 ], "fq": 50 
  },
  "soul": {
    "dict": "happiness", "word": "soul", "stem": "soul",
    "avg": [ 4.19, 6.34 ], "std": [ 2.45, 1.67 ], "fq": 50 
  },
  "activity": {
    "dict": "happiness", "word": "activity", "stem": "activ",
    "avg": [ 4.86, 6.32 ], "std": [ 2.56, 1.00 ], "fq": 50 
  },
  "agreement": {
    "dict": "happiness", "word": "agreement", "stem": "agreement",
    "avg": [ 5.02, 6.32 ], "std": [ 2.24, 1.22 ], "fq": 50 
  },
  "date": {
    "dict": "happiness", "word": "date", "stem": "date",
    "avg": [ 6.77, 6.32 ], "std": [ 2.07, 1.61 ], "fq": 50 
  },
  "deal": {
    "dict": "happiness", "word": "deal", "stem": "deal",
    "avg": [ 5.49, 6.32 ], "std": [ 2.43, 1.08 ], "fq": 50 
  },
  "designer": {
    "dict": "happiness", "word": "designer", "stem": "design",
    "avg": [ 5.14, 6.32 ], "std": [ 2.39, 1.63 ], "fq": 50 
  },
  "devotion": {
    "dict": "happiness", "word": "devotion", "stem": "devot",
    "avg": [ 5.23, 6.32 ], "std": [ 2.21, 2.09 ], "fq": 50 
  },
  "experiences": {
    "dict": "happiness", "word": "experiences", "stem": "experi",
    "avg": [ 5.53, 6.32 ], "std": [ 2.90, 1.08 ], "fq": 50 
  },
  "kin": {
    "dict": "happiness", "word": "kin", "stem": "kin",
    "avg": [ 4.80, 6.32 ], "std": [ 2.71, 1.50 ], "fq": 50 
  },
  "lights": {
    "dict": "happiness", "word": "lights", "stem": "light",
    "avg": [ 5.40, 6.32 ], "std": [ 2.33, 1.41 ], "fq": 50 
  },
  "mornings": {
    "dict": "happiness", "word": "mornings", "stem": "morn",
    "avg": [ 5.06, 6.32 ], "std": [ 3.05, 2.23 ], "fq": 50 
  },
  "newspaper": {
    "dict": "happiness", "word": "newspaper", "stem": "newspap",
    "avg": [ 2.50, 6.32 ], "std": [ 1.85, 1.35 ], "fq": 50 
  },
  "offering": {
    "dict": "happiness", "word": "offering", "stem": "offer",
    "avg": [ 4.88, 6.32 ], "std": [ 2.30, 1.65 ], "fq": 50 
  },
  "resolve": {
    "dict": "happiness", "word": "resolve", "stem": "resolv",
    "avg": [ 5.41, 6.32 ], "std": [ 2.43, 1.17 ], "fq": 50 
  },
  "snow": {
    "dict": "happiness", "word": "snow", "stem": "snow",
    "avg": [ 5.75, 6.32 ], "std": [ 2.47, 2.18 ], "fq": 50 
  },
  "sure": {
    "dict": "happiness", "word": "sure", "stem": "sure",
    "avg": [ 5.30, 6.32 ], "std": [ 2.66, 1.49 ], "fq": 50 
  },
  "waters": {
    "dict": "happiness", "word": "waters", "stem": "water",
    "avg": [ 4.97, 6.32 ], "std": [ 2.49, 1.15 ], "fq": 50 
  },
  "worship": {
    "dict": "happiness", "word": "worship", "stem": "worship",
    "avg": [ 4.00, 6.32 ], "std": [ 1.60, 1.48 ], "fq": 50 
  },
  "writers": {
    "dict": "happiness", "word": "writers", "stem": "writer",
    "avg": [ 4.33, 6.32 ], "std": [ 2.45, 1.27 ], "fq": 50 
  },
  "scent": {
    "dict": "happiness", "word": "scent", "stem": "scent",
    "avg": [ 5.05, 6.31 ], "std": [ 2.36, 1.25 ], "fq": 50 
  },
  "volumes": {
    "dict": "happiness", "word": "volumes", "stem": "volum",
    "avg": [ 4.17, 6.31 ], "std": [ 2.49, 1.29 ], "fq": 50 
  },
  "whistle": {
    "dict": "happiness", "word": "whistle", "stem": "whistl",
    "avg": [ 4.69, 6.31 ], "std": [ 1.99, 1.40 ], "fq": 50 
  },
  "absolutely": {
    "dict": "happiness", "word": "absolutely", "stem": "absolut",
    "avg": [ 5.73, 6.30 ], "std": [ 2.73, 1.42 ], "fq": 50 
  },
  "atmosphere": {
    "dict": "happiness", "word": "atmosphere", "stem": "atmospher",
    "avg": [ 4.12, 6.30 ], "std": [ 2.30, 1.20 ], "fq": 50 
  },
  "bought": {
    "dict": "happiness", "word": "bought", "stem": "bought",
    "avg": [ 4.67, 6.30 ], "std": [ 2.35, 1.23 ], "fq": 50 
  },
  "engineer": {
    "dict": "happiness", "word": "engineer", "stem": "engin",
    "avg": [ 3.98, 6.30 ], "std": [ 2.33, 1.18 ], "fq": 50 
  },
  "exercise": {
    "dict": "happiness", "word": "exercise", "stem": "exercis",
    "avg": [ 6.84, 6.30 ], "std": [ 2.06, 1.64 ], "fq": 50 
  },
  "feeding": {
    "dict": "happiness", "word": "feeding", "stem": "feed",
    "avg": [ 5.69, 6.30 ], "std": [ 2.51, 1.31 ], "fq": 50 
  },
  "flowing": {
    "dict": "happiness", "word": "flowing", "stem": "flow",
    "avg": [ 4.70, 6.30 ], "std": [ 2.48, 1.37 ], "fq": 50 
  },
  "joined": {
    "dict": "happiness", "word": "joined", "stem": "join",
    "avg": [ 6.39, 6.30 ], "std": [ 2.31, 1.09 ], "fq": 50 
  },
  "paint": {
    "dict": "happiness", "word": "paint", "stem": "paint",
    "avg": [ 4.10, 6.30 ], "std": [ 2.36, 1.07 ], "fq": 50 
  },
  "painted": {
    "dict": "happiness", "word": "painted", "stem": "paint",
    "avg": [ 4.10, 6.30 ], "std": [ 2.36, 0.99 ], "fq": 50 
  },
  "plane": {
    "dict": "happiness", "word": "plane", "stem": "plane",
    "avg": [ 6.14, 6.30 ], "std": [ 2.39, 1.63 ], "fq": 50 
  },
  "produced": {
    "dict": "happiness", "word": "produced", "stem": "produc",
    "avg": [ 3.90, 6.30 ], "std": [ 1.95, 1.20 ], "fq": 50 
  },
  "protecting": {
    "dict": "happiness", "word": "protecting", "stem": "protect",
    "avg": [ 4.09, 6.30 ], "std": [ 2.77, 1.61 ], "fq": 50 
  },
  "relations": {
    "dict": "happiness", "word": "relations", "stem": "relat",
    "avg": [ 7.00, 6.30 ], "std": [ 2.07, 1.61 ], "fq": 50 
  },
  "swing": {
    "dict": "happiness", "word": "swing", "stem": "swing",
    "avg": [ 5.00, 6.30 ], "std": [ 2.32, 1.27 ], "fq": 50 
  },
  "visited": {
    "dict": "happiness", "word": "visited", "stem": "visit",
    "avg": [ 5.74, 6.30 ], "std": [ 2.38, 1.42 ], "fq": 50 
  },
  "cheeks": {
    "dict": "happiness", "word": "cheeks", "stem": "cheek",
    "avg": [ 5.60, 6.29 ], "std": [ 2.21, 1.53 ], "fq": 50 
  },
  "observation": {
    "dict": "happiness", "word": "observation", "stem": "observ",
    "avg": [ 4.10, 6.29 ], "std": [ 2.12, 1.32 ], "fq": 50 
  },
  "rum": {
    "dict": "happiness", "word": "rum", "stem": "rum",
    "avg": [ 4.27, 6.29 ], "std": [ 2.46, 2.09 ], "fq": 50 
  },
  "babes": {
    "dict": "happiness", "word": "babes", "stem": "babe",
    "avg": [ 5.53, 6.28 ], "std": [ 2.80, 1.75 ], "fq": 50 
  },
  "buy": {
    "dict": "happiness", "word": "buy", "stem": "buy",
    "avg": [ 4.67, 6.28 ], "std": [ 2.35, 1.36 ], "fq": 50 
  },
  "cooler": {
    "dict": "happiness", "word": "cooler", "stem": "cooler",
    "avg": [ 4.88, 6.28 ], "std": [ 1.86, 1.31 ], "fq": 50 
  },
  "fairly": {
    "dict": "happiness", "word": "fairly", "stem": "fairli",
    "avg": [ 6.03, 6.28 ], "std": [ 2.22, 1.16 ], "fq": 50 
  },
  "fix": {
    "dict": "happiness", "word": "fix", "stem": "fix",
    "avg": [ 3.14, 6.28 ], "std": [ 2.47, 1.53 ], "fq": 50 
  },
  "founded": {
    "dict": "happiness", "word": "founded", "stem": "found",
    "avg": [ 3.62, 6.28 ], "std": [ 2.25, 1.25 ], "fq": 50 
  },
  "globe": {
    "dict": "happiness", "word": "globe", "stem": "globe",
    "avg": [ 4.24, 6.28 ], "std": [ 2.49, 1.43 ], "fq": 50 
  },
  "hoped": {
    "dict": "happiness", "word": "hoped", "stem": "hope",
    "avg": [ 5.78, 6.28 ], "std": [ 2.09, 1.11 ], "fq": 50 
  },
  "introduced": {
    "dict": "happiness", "word": "introduced", "stem": "introduc",
    "avg": [ 5.12, 6.28 ], "std": [ 2.39, 1.36 ], "fq": 50 
  },
  "lead": {
    "dict": "happiness", "word": "lead", "stem": "lead",
    "avg": [ 3.15, 6.28 ], "std": [ 1.77, 1.46 ], "fq": 50 
  },
  "listening": {
    "dict": "happiness", "word": "listening", "stem": "listen",
    "avg": [ 5.00, 6.28 ], "std": [ 2.68, 1.44 ], "fq": 50 
  },
  "lots": {
    "dict": "happiness", "word": "lots", "stem": "lot",
    "avg": [ 5.49, 6.28 ], "std": [ 2.43, 1.43 ], "fq": 50 
  },
  "market": {
    "dict": "happiness", "word": "market", "stem": "market",
    "avg": [ 4.12, 6.28 ], "std": [ 1.83, 1.60 ], "fq": 50 
  },
  "monkey": {
    "dict": "happiness", "word": "monkey", "stem": "monkey",
    "avg": [ 4.95, 6.28 ], "std": [ 2.01, 1.71 ], "fq": 50 
  },
  "professionals": {
    "dict": "happiness", "word": "professionals", "stem": "profession",
    "avg": [ 5.20, 6.28 ], "std": [ 2.85, 1.40 ], "fq": 50 
  },
  "remembering": {
    "dict": "happiness", "word": "remembering", "stem": "rememb",
    "avg": [ 5.42, 6.28 ], "std": [ 2.25, 1.26 ], "fq": 50 
  },
  "sentimental": {
    "dict": "happiness", "word": "sentimental", "stem": "sentiment",
    "avg": [ 4.41, 6.28 ], "std": [ 2.30, 1.67 ], "fq": 50 
  },
  "students": {
    "dict": "happiness", "word": "students", "stem": "student",
    "avg": [ 5.12, 6.28 ], "std": [ 2.46, 1.83 ], "fq": 50 
  },
  "themes": {
    "dict": "happiness", "word": "themes", "stem": "theme",
    "avg": [ 5.86, 6.28 ], "std": [ 1.81, 1.25 ], "fq": 50 
  },
  "thinking": {
    "dict": "happiness", "word": "thinking", "stem": "think",
    "avg": [ 5.72, 6.28 ], "std": [ 2.30, 1.29 ], "fq": 50 
  },
  "tips": {
    "dict": "happiness", "word": "tips", "stem": "tip",
    "avg": [ 4.28, 6.28 ], "std": [ 2.53, 1.58 ], "fq": 50 
  },
  "vehicles": {
    "dict": "happiness", "word": "vehicles", "stem": "vehicl",
    "avg": [ 4.63, 6.28 ], "std": [ 2.81, 1.50 ], "fq": 50 
  },
  "village": {
    "dict": "happiness", "word": "village", "stem": "villag",
    "avg": [ 4.08, 6.28 ], "std": [ 1.87, 1.13 ], "fq": 50 
  },
  "white": {
    "dict": "happiness", "word": "white", "stem": "white",
    "avg": [ 4.37, 6.28 ], "std": [ 2.14, 1.54 ], "fq": 50 
  },
  "wines": {
    "dict": "happiness", "word": "wines", "stem": "wine",
    "avg": [ 4.78, 6.28 ], "std": [ 2.34, 2.37 ], "fq": 50 
  },
  "reasonably": {
    "dict": "happiness", "word": "reasonably", "stem": "reason",
    "avg": [ 6.03, 6.27 ], "std": [ 2.22, 1.36 ], "fq": 50 
  },
  "observe": {
    "dict": "happiness", "word": "observe", "stem": "observ",
    "avg": [ 4.10, 6.27 ], "std": [ 2.12, 1.37 ], "fq": 50 
  },
  "regards": {
    "dict": "happiness", "word": "regards", "stem": "regard",
    "avg": [ 5.16, 6.27 ], "std": [ 2.62, 1.33 ], "fq": 50 
  },
  "allows": {
    "dict": "happiness", "word": "allows", "stem": "allow",
    "avg": [ 3.27, 6.26 ], "std": [ 2.05, 1.19 ], "fq": 50 
  },
  "appropriate": {
    "dict": "happiness", "word": "appropriate", "stem": "appropri",
    "avg": [ 3.27, 6.26 ], "std": [ 2.05, 1.24 ], "fq": 50 
  },
  "cars": {
    "dict": "happiness", "word": "cars", "stem": "car",
    "avg": [ 6.24, 6.26 ], "std": [ 2.04, 1.69 ], "fq": 50 
  },
  "develop": {
    "dict": "happiness", "word": "develop", "stem": "develop",
    "avg": [ 5.74, 6.26 ], "std": [ 2.46, 1.05 ], "fq": 50 
  },
  "events": {
    "dict": "happiness", "word": "events", "stem": "event",
    "avg": [ 5.10, 6.26 ], "std": [ 2.40, 1.47 ], "fq": 50 
  },
  "flag": {
    "dict": "happiness", "word": "flag", "stem": "flag",
    "avg": [ 4.60, 6.26 ], "std": [ 2.35, 1.31 ], "fq": 50 
  },
  "gave": {
    "dict": "happiness", "word": "gave", "stem": "gave",
    "avg": [ 5.23, 6.26 ], "std": [ 2.21, 1.29 ], "fq": 50 
  },
  "gods": {
    "dict": "happiness", "word": "gods", "stem": "god",
    "avg": [ 5.95, 6.26 ], "std": [ 2.84, 1.91 ], "fq": 50 
  },
  "hotels": {
    "dict": "happiness", "word": "hotels", "stem": "hotel",
    "avg": [ 4.80, 6.26 ], "std": [ 2.53, 1.48 ], "fq": 50 
  },
  "human": {
    "dict": "happiness", "word": "human", "stem": "human",
    "avg": [ 4.50, 6.26 ], "std": [ 1.91, 1.64 ], "fq": 50 
  },
  "leap": {
    "dict": "happiness", "word": "leap", "stem": "leap",
    "avg": [ 5.67, 6.26 ], "std": [ 2.51, 1.29 ], "fq": 50 
  },
  "lifetime": {
    "dict": "happiness", "word": "lifetime", "stem": "lifetim",
    "avg": [ 6.02, 6.26 ], "std": [ 2.62, 1.63 ], "fq": 50 
  },
  "produce": {
    "dict": "happiness", "word": "produce", "stem": "produc",
    "avg": [ 3.90, 6.26 ], "std": [ 1.95, 1.12 ], "fq": 50 
  },
  "prominent": {
    "dict": "happiness", "word": "prominent", "stem": "promin",
    "avg": [ 6.24, 6.26 ], "std": [ 2.59, 1.10 ], "fq": 50 
  },
  "promises": {
    "dict": "happiness", "word": "promises", "stem": "promis",
    "avg": [ 5.78, 6.26 ], "std": [ 2.09, 1.55 ], "fq": 50 
  },
  "raising": {
    "dict": "happiness", "word": "raising", "stem": "rais",
    "avg": [ 7.17, 6.26 ], "std": [ 2.06, 1.23 ], "fq": 50 
  },
  "school": {
    "dict": "happiness", "word": "school", "stem": "school",
    "avg": [ 5.74, 6.26 ], "std": [ 2.46, 1.88 ], "fq": 50 
  },
  "spark": {
    "dict": "happiness", "word": "spark", "stem": "spark",
    "avg": [ 4.86, 6.26 ], "std": [ 2.56, 1.66 ], "fq": 50 
  },
  "travelers": {
    "dict": "happiness", "word": "travelers", "stem": "travel",
    "avg": [ 6.21, 6.26 ], "std": [ 2.51, 1.56 ], "fq": 50 
  },
  "spirits": {
    "dict": "happiness", "word": "spirits", "stem": "spirit",
    "avg": [ 5.56, 6.24 ], "std": [ 2.62, 1.80 ], "fq": 50 
  },
  "advances": {
    "dict": "happiness", "word": "advances", "stem": "advanc",
    "avg": [ 7.72, 6.24 ], "std": [ 2.16, 1.35 ], "fq": 50 
  },
  "answer": {
    "dict": "happiness", "word": "answer", "stem": "answer",
    "avg": [ 5.41, 6.24 ], "std": [ 2.43, 1.57 ], "fq": 50 
  },
  "athletes": {
    "dict": "happiness", "word": "athletes", "stem": "athlet",
    "avg": [ 6.10, 6.24 ], "std": [ 2.29, 1.38 ], "fq": 50 
  },
  "bowling": {
    "dict": "happiness", "word": "bowling", "stem": "bowl",
    "avg": [ 3.47, 6.24 ], "std": [ 2.12, 1.51 ], "fq": 50 
  },
  "boy": {
    "dict": "happiness", "word": "boy", "stem": "boy",
    "avg": [ 4.58, 6.24 ], "std": [ 2.37, 1.29 ], "fq": 50 
  },
  "built": {
    "dict": "happiness", "word": "built", "stem": "built",
    "avg": [ 3.92, 6.24 ], "std": [ 1.94, 1.19 ], "fq": 50 
  },
  "choice": {
    "dict": "happiness", "word": "choice", "stem": "choic",
    "avg": [ 4.74, 6.24 ], "std": [ 2.23, 1.32 ], "fq": 50 
  },
  "day": {
    "dict": "happiness", "word": "day", "stem": "day",
    "avg": [ 4.77, 6.24 ], "std": [ 2.50, 1.36 ], "fq": 50 
  },
  "deliver": {
    "dict": "happiness", "word": "deliver", "stem": "deliv",
    "avg": [ 4.95, 6.24 ], "std": [ 2.19, 1.02 ], "fq": 50 
  },
  "eyes": {
    "dict": "happiness", "word": "eyes", "stem": "eye",
    "avg": [ 6.34, 6.24 ], "std": [ 2.25, 1.10 ], "fq": 50 
  },
  "flying": {
    "dict": "happiness", "word": "flying", "stem": "fli",
    "avg": [ 6.57, 6.24 ], "std": [ 1.78, 1.65 ], "fq": 50 
  },
  "grad": {
    "dict": "happiness", "word": "grad", "stem": "grad",
    "avg": [ 7.25, 6.24 ], "std": [ 2.25, 1.29 ], "fq": 50 
  },
  "jelly": {
    "dict": "happiness", "word": "jelly", "stem": "jelli",
    "avg": [ 3.70, 6.24 ], "std": [ 2.29, 1.32 ], "fq": 50 
  },
  "making": {
    "dict": "happiness", "word": "making", "stem": "make",
    "avg": [ 4.20, 6.24 ], "std": [ 2.18, 1.19 ], "fq": 50 
  },
  "options": {
    "dict": "happiness", "word": "options", "stem": "option",
    "avg": [ 4.74, 6.24 ], "std": [ 2.23, 0.94 ], "fq": 50 
  },
  "queen": {
    "dict": "happiness", "word": "queen", "stem": "queen",
    "avg": [ 4.76, 6.24 ], "std": [ 2.18, 1.79 ], "fq": 50 
  },
  "show": {
    "dict": "happiness", "word": "show", "stem": "show",
    "avg": [ 5.12, 6.24 ], "std": [ 2.39, 1.49 ], "fq": 50 
  },
  "speed": {
    "dict": "happiness", "word": "speed", "stem": "speed",
    "avg": [ 5.39, 6.24 ], "std": [ 2.53, 1.48 ], "fq": 50 
  },
  "tip": {
    "dict": "happiness", "word": "tip", "stem": "tip",
    "avg": [ 4.28, 6.24 ], "std": [ 2.53, 1.04 ], "fq": 50 
  },
  "worlds": {
    "dict": "happiness", "word": "worlds", "stem": "world",
    "avg": [ 5.32, 6.24 ], "std": [ 2.39, 1.56 ], "fq": 50 
  },
  "writing": {
    "dict": "happiness", "word": "writing", "stem": "write",
    "avg": [ 4.95, 6.24 ], "std": [ 2.19, 1.65 ], "fq": 50 
  },
  "embrace": {
    "dict": "happiness", "word": "embrace", "stem": "embrac",
    "avg": [ 5.35, 6.22 ], "std": [ 2.76, 1.90 ], "fq": 50 
  },
  "produces": {
    "dict": "happiness", "word": "produces", "stem": "produc",
    "avg": [ 3.90, 6.22 ], "std": [ 1.95, 1.34 ], "fq": 50 
  },
  "answered": {
    "dict": "happiness", "word": "answered", "stem": "answer",
    "avg": [ 5.41, 6.22 ], "std": [ 2.43, 1.34 ], "fq": 50 
  },
  "authors": {
    "dict": "happiness", "word": "authors", "stem": "author",
    "avg": [ 4.33, 6.22 ], "std": [ 2.45, 1.68 ], "fq": 50 
  },
  "big": {
    "dict": "happiness", "word": "big", "stem": "big",
    "avg": [ 4.76, 6.22 ], "std": [ 1.95, 1.50 ], "fq": 50 
  },
  "breast": {
    "dict": "happiness", "word": "breast", "stem": "breast",
    "avg": [ 5.37, 6.22 ], "std": [ 2.39, 1.45 ], "fq": 50 
  },
  "build": {
    "dict": "happiness", "word": "build", "stem": "build",
    "avg": [ 3.92, 6.22 ], "std": [ 1.94, 1.07 ], "fq": 50 
  },
  "contributions": {
    "dict": "happiness", "word": "contributions", "stem": "contribut",
    "avg": [ 3.82, 6.22 ], "std": [ 2.24, 1.56 ], "fq": 50 
  },
  "decent": {
    "dict": "happiness", "word": "decent", "stem": "decent",
    "avg": [ 5.14, 6.22 ], "std": [ 2.39, 1.71 ], "fq": 50 
  },
  "farm": {
    "dict": "happiness", "word": "farm", "stem": "farm",
    "avg": [ 3.90, 6.22 ], "std": [ 1.95, 1.58 ], "fq": 50 
  },
  "foundations": {
    "dict": "happiness", "word": "foundations", "stem": "foundat",
    "avg": [ 3.27, 6.22 ], "std": [ 1.98, 1.17 ], "fq": 50 
  },
  "full": {
    "dict": "happiness", "word": "full", "stem": "full",
    "avg": [ 5.43, 6.22 ], "std": [ 2.85, 1.22 ], "fq": 50 
  },
  "guys": {
    "dict": "happiness", "word": "guys", "stem": "guy",
    "avg": [ 5.83, 6.22 ], "std": [ 2.73, 1.42 ], "fq": 50 
  },
  "instrument": {
    "dict": "happiness", "word": "instrument", "stem": "instrument",
    "avg": [ 4.33, 6.22 ], "std": [ 1.78, 1.23 ], "fq": 50 
  },
  "join": {
    "dict": "happiness", "word": "join", "stem": "join",
    "avg": [ 3.75, 6.22 ], "std": [ 2.49, 1.56 ], "fq": 50 
  },
  "knight": {
    "dict": "happiness", "word": "knight", "stem": "knight",
    "avg": [ 3.89, 6.22 ], "std": [ 2.17, 1.46 ], "fq": 50 
  },
  "lives": {
    "dict": "happiness", "word": "lives", "stem": "live",
    "avg": [ 5.53, 6.22 ], "std": [ 2.90, 1.15 ], "fq": 50 
  },
  "milk": {
    "dict": "happiness", "word": "milk", "stem": "milk",
    "avg": [ 3.68, 6.22 ], "std": [ 2.57, 1.93 ], "fq": 50 
  },
  "night": {
    "dict": "happiness", "word": "night", "stem": "night",
    "avg": [ 4.28, 6.22 ], "std": [ 2.21, 1.30 ], "fq": 50 
  },
  "participation": {
    "dict": "happiness", "word": "participation", "stem": "particip",
    "avg": [ 6.77, 6.22 ], "std": [ 2.07, 1.15 ], "fq": 50 
  },
  "social": {
    "dict": "happiness", "word": "social", "stem": "social",
    "avg": [ 4.98, 6.22 ], "std": [ 2.59, 1.04 ], "fq": 50 
  },
  "styles": {
    "dict": "happiness", "word": "styles", "stem": "style",
    "avg": [ 4.56, 6.22 ], "std": [ 1.78, 1.02 ], "fq": 50 
  },
  "supports": {
    "dict": "happiness", "word": "supports", "stem": "support",
    "avg": [ 5.53, 6.22 ], "std": [ 2.90, 1.53 ], "fq": 50 
  },
  "thoughts": {
    "dict": "happiness", "word": "thoughts", "stem": "thought",
    "avg": [ 5.72, 6.22 ], "std": [ 2.30, 1.54 ], "fq": 50 
  },
  "tribute": {
    "dict": "happiness", "word": "tribute", "stem": "tribut",
    "avg": [ 4.09, 6.22 ], "std": [ 2.77, 1.36 ], "fq": 50 
  },
  "dough": {
    "dict": "happiness", "word": "dough", "stem": "dough",
    "avg": [ 5.64, 6.20 ], "std": [ 2.18, 1.46 ], "fq": 50 
  },
  "agreements": {
    "dict": "happiness", "word": "agreements", "stem": "agreement",
    "avg": [ 5.02, 6.20 ], "std": [ 2.24, 1.56 ], "fq": 50 
  },
  "assured": {
    "dict": "happiness", "word": "assured", "stem": "assur",
    "avg": [ 6.10, 6.20 ], "std": [ 2.19, 1.56 ], "fq": 50 
  },
  "engage": {
    "dict": "happiness", "word": "engage", "stem": "engag",
    "avg": [ 6.77, 6.20 ], "std": [ 2.07, 1.34 ], "fq": 50 
  },
  "ethical": {
    "dict": "happiness", "word": "ethical", "stem": "ethic",
    "avg": [ 5.90, 6.20 ], "std": [ 1.83, 1.37 ], "fq": 50 
  },
  "faces": {
    "dict": "happiness", "word": "faces", "stem": "face",
    "avg": [ 5.04, 6.20 ], "std": [ 2.18, 1.46 ], "fq": 50 
  },
  "feeds": {
    "dict": "happiness", "word": "feeds", "stem": "feed",
    "avg": [ 5.69, 6.20 ], "std": [ 2.51, 1.47 ], "fq": 50 
  },
  "halo": {
    "dict": "happiness", "word": "halo", "stem": "halo",
    "avg": [ 6.02, 6.20 ], "std": [ 2.71, 1.81 ], "fq": 50 
  },
  "jacket": {
    "dict": "happiness", "word": "jacket", "stem": "jacket",
    "avg": [ 4.28, 6.20 ], "std": [ 2.53, 1.12 ], "fq": 50 
  },
  "joining": {
    "dict": "happiness", "word": "joining", "stem": "join",
    "avg": [ 3.75, 6.20 ], "std": [ 2.49, 1.11 ], "fq": 50 
  },
  "lifted": {
    "dict": "happiness", "word": "lifted", "stem": "lift",
    "avg": [ 4.59, 6.20 ], "std": [ 2.10, 1.23 ], "fq": 50 
  },
  "listened": {
    "dict": "happiness", "word": "listened", "stem": "listen",
    "avg": [ 5.00, 6.20 ], "std": [ 2.68, 1.28 ], "fq": 50 
  },
  "meat": {
    "dict": "happiness", "word": "meat", "stem": "meat",
    "avg": [ 6.34, 6.20 ], "std": [ 2.25, 2.14 ], "fq": 50 
  },
  "nurse": {
    "dict": "happiness", "word": "nurse", "stem": "nurs",
    "avg": [ 4.84, 6.20 ], "std": [ 2.04, 1.26 ], "fq": 50 
  },
  "sexual": {
    "dict": "happiness", "word": "sexual", "stem": "sexual",
    "avg": [ 6.98, 6.20 ], "std": [ 2.21, 1.46 ], "fq": 50 
  },
  "succession": {
    "dict": "happiness", "word": "succession", "stem": "success",
    "avg": [ 6.11, 6.20 ], "std": [ 2.65, 1.29 ], "fq": 50 
  },
  "supporters": {
    "dict": "happiness", "word": "supporters", "stem": "support",
    "avg": [ 5.85, 6.20 ], "std": [ 3.15, 1.58 ], "fq": 50 
  },
  "think": {
    "dict": "happiness", "word": "think", "stem": "think",
    "avg": [ 5.98, 6.20 ], "std": [ 2.14, 1.29 ], "fq": 50 
  },
  "copper": {
    "dict": "happiness", "word": "copper", "stem": "copper",
    "avg": [ 4.20, 6.18 ], "std": [ 2.42, 1.60 ], "fq": 50 
  },
  "ate": {
    "dict": "happiness", "word": "ate", "stem": "ate",
    "avg": [ 5.69, 6.18 ], "std": [ 2.51, 1.45 ], "fq": 50 
  },
  "blonde": {
    "dict": "happiness", "word": "blonde", "stem": "blond",
    "avg": [ 5.07, 6.18 ], "std": [ 2.70, 1.60 ], "fq": 50 
  },
  "burger": {
    "dict": "happiness", "word": "burger", "stem": "burger",
    "avg": [ 4.55, 6.18 ], "std": [ 2.14, 2.30 ], "fq": 50 
  },
  "certificate": {
    "dict": "happiness", "word": "certificate", "stem": "certif",
    "avg": [ 3.14, 6.18 ], "std": [ 2.47, 1.14 ], "fq": 50 
  },
  "chances": {
    "dict": "happiness", "word": "chances", "stem": "chanc",
    "avg": [ 5.38, 6.18 ], "std": [ 2.58, 1.04 ], "fq": 50 
  },
  "chief": {
    "dict": "happiness", "word": "chief", "stem": "chief",
    "avg": [ 5.20, 6.18 ], "std": [ 2.85, 1.16 ], "fq": 50 
  },
  "established": {
    "dict": "happiness", "word": "established", "stem": "establish",
    "avg": [ 4.37, 6.18 ], "std": [ 2.51, 1.17 ], "fq": 50 
  },
  "expression": {
    "dict": "happiness", "word": "expression", "stem": "express",
    "avg": [ 5.04, 6.18 ], "std": [ 2.18, 1.30 ], "fq": 50 
  },
  "fishing": {
    "dict": "happiness", "word": "fishing", "stem": "fish",
    "avg": [ 4.00, 6.18 ], "std": [ 2.19, 1.83 ], "fq": 50 
  },
  "king": {
    "dict": "happiness", "word": "king", "stem": "king",
    "avg": [ 5.51, 6.18 ], "std": [ 2.77, 1.56 ], "fq": 50 
  },
  "land": {
    "dict": "happiness", "word": "land", "stem": "land",
    "avg": [ 4.24, 6.18 ], "std": [ 2.49, 1.34 ], "fq": 50 
  },
  "lion": {
    "dict": "happiness", "word": "lion", "stem": "lion",
    "avg": [ 6.20, 6.18 ], "std": [ 2.16, 1.61 ], "fq": 50 
  },
  "resolution": {
    "dict": "happiness", "word": "resolution", "stem": "resolut",
    "avg": [ 5.41, 6.18 ], "std": [ 2.43, 1.29 ], "fq": 50 
  },
  "riding": {
    "dict": "happiness", "word": "riding", "stem": "ride",
    "avg": [ 5.15, 6.18 ], "std": [ 3.04, 1.40 ], "fq": 50 
  },
  "safety": {
    "dict": "happiness", "word": "safety", "stem": "safeti",
    "avg": [ 3.86, 6.18 ], "std": [ 2.72, 1.73 ], "fq": 50 
  },
  "sight": {
    "dict": "happiness", "word": "sight", "stem": "sight",
    "avg": [ 5.49, 6.18 ], "std": [ 2.43, 0.98 ], "fq": 50 
  },
  "spice": {
    "dict": "happiness", "word": "spice", "stem": "spice",
    "avg": [ 5.59, 6.18 ], "std": [ 2.66, 1.72 ], "fq": 50 
  },
  "steady": {
    "dict": "happiness", "word": "steady", "stem": "steadi",
    "avg": [ 5.50, 6.18 ], "std": [ 2.73, 1.34 ], "fq": 50 
  },
  "trains": {
    "dict": "happiness", "word": "trains", "stem": "train",
    "avg": [ 5.74, 6.18 ], "std": [ 2.46, 1.32 ], "fq": 50 
  },
  "tune": {
    "dict": "happiness", "word": "tune", "stem": "tune",
    "avg": [ 4.71, 6.18 ], "std": [ 2.09, 1.42 ], "fq": 50 
  },
  "victor": {
    "dict": "happiness", "word": "victor", "stem": "victor",
    "avg": [ 5.20, 6.18 ], "std": [ 2.85, 1.72 ], "fq": 50 
  },
  "wireless": {
    "dict": "happiness", "word": "wireless", "stem": "wireless",
    "avg": [ 4.78, 6.18 ], "std": [ 2.82, 1.60 ], "fq": 50 
  },
  "beds": {
    "dict": "happiness", "word": "beds", "stem": "bed",
    "avg": [ 3.61, 6.17 ], "std": [ 2.56, 1.72 ], "fq": 50 
  },
  "preference": {
    "dict": "happiness", "word": "preference", "stem": "prefer",
    "avg": [ 5.22, 6.17 ], "std": [ 2.38, 1.00 ], "fq": 50 
  },
  "applying": {
    "dict": "happiness", "word": "applying", "stem": "appli",
    "avg": [ 5.28, 6.16 ], "std": [ 2.12, 1.16 ], "fq": 50 
  },
  "crop": {
    "dict": "happiness", "word": "crop", "stem": "crop",
    "avg": [ 4.05, 6.16 ], "std": [ 1.89, 1.25 ], "fq": 50 
  },
  "allowing": {
    "dict": "happiness", "word": "allowing", "stem": "allow",
    "avg": [ 3.27, 6.16 ], "std": [ 2.05, 1.09 ], "fq": 50 
  },
  "automobile": {
    "dict": "happiness", "word": "automobile", "stem": "automobil",
    "avg": [ 3.82, 6.16 ], "std": [ 2.40, 1.38 ], "fq": 50 
  },
  "bands": {
    "dict": "happiness", "word": "bands", "stem": "band",
    "avg": [ 3.86, 6.16 ], "std": [ 2.13, 1.46 ], "fq": 50 
  },
  "boys": {
    "dict": "happiness", "word": "boys", "stem": "boy",
    "avg": [ 4.58, 6.16 ], "std": [ 2.37, 1.23 ], "fq": 50 
  },
  "engaged": {
    "dict": "happiness", "word": "engaged", "stem": "engag",
    "avg": [ 6.77, 6.16 ], "std": [ 2.07, 1.96 ], "fq": 50 
  },
  "fiction": {
    "dict": "happiness", "word": "fiction", "stem": "fiction",
    "avg": [ 4.14, 6.16 ], "std": [ 1.98, 1.43 ], "fq": 50 
  },
  "grocery": {
    "dict": "happiness", "word": "grocery", "stem": "groceri",
    "avg": [ 4.12, 6.16 ], "std": [ 1.83, 1.73 ], "fq": 50 
  },
  "hotel": {
    "dict": "happiness", "word": "hotel", "stem": "hotel",
    "avg": [ 4.80, 6.16 ], "std": [ 2.53, 1.60 ], "fq": 50 
  },
  "houses": {
    "dict": "happiness", "word": "houses", "stem": "hous",
    "avg": [ 4.56, 6.16 ], "std": [ 2.41, 1.63 ], "fq": 50 
  },
  "minds": {
    "dict": "happiness", "word": "minds", "stem": "mind",
    "avg": [ 5.00, 6.16 ], "std": [ 2.68, 1.23 ], "fq": 50 
  },
  "people": {
    "dict": "happiness", "word": "people", "stem": "peopl",
    "avg": [ 5.94, 6.16 ], "std": [ 2.09, 1.58 ], "fq": 50 
  },
  "polish": {
    "dict": "happiness", "word": "polish", "stem": "polish",
    "avg": [ 4.91, 6.16 ], "std": [ 2.57, 1.39 ], "fq": 50 
  },
  "rocked": {
    "dict": "happiness", "word": "rocked", "stem": "rock",
    "avg": [ 4.52, 6.16 ], "std": [ 2.37, 1.45 ], "fq": 50 
  },
  "transportation": {
    "dict": "happiness", "word": "transportation", "stem": "transport",
    "avg": [ 4.38, 6.16 ], "std": [ 2.29, 1.68 ], "fq": 50 
  },
  "turkey": {
    "dict": "happiness", "word": "turkey", "stem": "turkey",
    "avg": [ 7.15, 6.16 ], "std": [ 2.40, 1.81 ], "fq": 50 
  },
  "wed": {
    "dict": "happiness", "word": "wed", "stem": "wed",
    "avg": [ 5.97, 6.16 ], "std": [ 2.85, 1.82 ], "fq": 50 
  },
  "yacht": {
    "dict": "happiness", "word": "yacht", "stem": "yacht",
    "avg": [ 5.61, 6.16 ], "std": [ 2.72, 1.36 ], "fq": 50 
  },
  "believing": {
    "dict": "happiness", "word": "believing", "stem": "believ",
    "avg": [ 5.30, 6.14 ], "std": [ 2.66, 1.53 ], "fq": 50 
  },
  "persons": {
    "dict": "happiness", "word": "persons", "stem": "person",
    "avg": [ 4.19, 6.14 ], "std": [ 2.45, 1.27 ], "fq": 50 
  },
  "seed": {
    "dict": "happiness", "word": "seed", "stem": "seed",
    "avg": [ 4.49, 6.14 ], "std": [ 2.24, 1.38 ], "fq": 50 
  },
  "successive": {
    "dict": "happiness", "word": "successive", "stem": "success",
    "avg": [ 6.11, 6.14 ], "std": [ 2.65, 1.41 ], "fq": 50 
  },
  "adult": {
    "dict": "happiness", "word": "adult", "stem": "adult",
    "avg": [ 4.76, 6.14 ], "std": [ 1.95, 1.34 ], "fq": 50 
  },
  "aviation": {
    "dict": "happiness", "word": "aviation", "stem": "aviat",
    "avg": [ 4.12, 6.14 ], "std": [ 2.30, 1.34 ], "fq": 50 
  },
  "cheek": {
    "dict": "happiness", "word": "cheek", "stem": "cheek",
    "avg": [ 5.60, 6.14 ], "std": [ 2.21, 1.59 ], "fq": 50 
  },
  "conscious": {
    "dict": "happiness", "word": "conscious", "stem": "consciou",
    "avg": [ 5.42, 6.14 ], "std": [ 2.44, 1.39 ], "fq": 50 
  },
  "drinking": {
    "dict": "happiness", "word": "drinking", "stem": "drink",
    "avg": [ 5.31, 6.14 ], "std": [ 2.23, 1.71 ], "fq": 50 
  },
  "eye": {
    "dict": "happiness", "word": "eye", "stem": "eye",
    "avg": [ 6.34, 6.14 ], "std": [ 2.25, 1.43 ], "fq": 50 
  },
  "generate": {
    "dict": "happiness", "word": "generate", "stem": "gener",
    "avg": [ 5.92, 6.14 ], "std": [ 2.60, 1.16 ], "fq": 50 
  },
  "jumping": {
    "dict": "happiness", "word": "jumping", "stem": "jump",
    "avg": [ 5.67, 6.14 ], "std": [ 2.51, 1.58 ], "fq": 50 
  },
  "kindle": {
    "dict": "happiness", "word": "kindle", "stem": "kindl",
    "avg": [ 7.17, 6.14 ], "std": [ 2.06, 1.25 ], "fq": 50 
  },
  "mend": {
    "dict": "happiness", "word": "mend", "stem": "mend",
    "avg": [ 5.86, 6.14 ], "std": [ 2.70, 1.21 ], "fq": 50 
  },
  "models": {
    "dict": "happiness", "word": "models", "stem": "model",
    "avg": [ 4.07, 6.14 ], "std": [ 1.98, 1.58 ], "fq": 50 
  },
  "offered": {
    "dict": "happiness", "word": "offered", "stem": "offer",
    "avg": [ 4.88, 6.14 ], "std": [ 2.30, 1.40 ], "fq": 50 
  },
  "places": {
    "dict": "happiness", "word": "places", "stem": "place",
    "avg": [ 2.95, 6.14 ], "std": [ 1.72, 1.16 ], "fq": 50 
  },
  "respectively": {
    "dict": "happiness", "word": "respectively", "stem": "respect",
    "avg": [ 4.60, 6.14 ], "std": [ 2.67, 1.21 ], "fq": 50 
  },
  "restore": {
    "dict": "happiness", "word": "restore", "stem": "restor",
    "avg": [ 5.86, 6.14 ], "std": [ 2.70, 1.16 ], "fq": 50 
  },
  "ride": {
    "dict": "happiness", "word": "ride", "stem": "ride",
    "avg": [ 5.87, 6.14 ], "std": [ 2.56, 1.39 ], "fq": 50 
  },
  "rock": {
    "dict": "happiness", "word": "rock", "stem": "rock",
    "avg": [ 4.52, 6.14 ], "std": [ 2.37, 1.29 ], "fq": 50 
  },
  "strongly": {
    "dict": "happiness", "word": "strongly", "stem": "strongli",
    "avg": [ 5.83, 6.14 ], "std": [ 2.69, 1.28 ], "fq": 50 
  },
  "trail": {
    "dict": "happiness", "word": "trail", "stem": "trail",
    "avg": [ 5.76, 6.14 ], "std": [ 2.50, 1.14 ], "fq": 50 
  },
  "twin": {
    "dict": "happiness", "word": "twin", "stem": "twin",
    "avg": [ 6.39, 6.14 ], "std": [ 2.31, 1.29 ], "fq": 50 
  },
  "vagina": {
    "dict": "happiness", "word": "vagina", "stem": "vagina",
    "avg": [ 5.55, 6.14 ], "std": [ 2.55, 1.81 ], "fq": 50 
  },
  "exclusively": {
    "dict": "happiness", "word": "exclusively", "stem": "exclus",
    "avg": [ 4.83, 6.12 ], "std": [ 2.66, 1.44 ], "fq": 50 
  },
  "writings": {
    "dict": "happiness", "word": "writings", "stem": "write",
    "avg": [ 4.95, 6.12 ], "std": [ 2.19, 1.70 ], "fq": 50 
  },
  "outcomes": {
    "dict": "happiness", "word": "outcomes", "stem": "outcom",
    "avg": [ 5.10, 6.12 ], "std": [ 2.40, 1.44 ], "fq": 50 
  },
  "quicker": {
    "dict": "happiness", "word": "quicker", "stem": "quicker",
    "avg": [ 4.85, 6.12 ], "std": [ 1.80, 1.15 ], "fq": 50 
  },
  "boulevard": {
    "dict": "happiness", "word": "boulevard", "stem": "boulevard",
    "avg": [ 4.12, 6.12 ], "std": [ 2.01, 1.26 ], "fq": 50 
  },
  "consideration": {
    "dict": "happiness", "word": "consideration", "stem": "consider",
    "avg": [ 5.72, 6.12 ], "std": [ 2.30, 1.27 ], "fq": 50 
  },
  "dish": {
    "dict": "happiness", "word": "dish", "stem": "dish",
    "avg": [ 5.50, 6.12 ], "std": [ 2.73, 1.41 ], "fq": 50 
  },
  "ensure": {
    "dict": "happiness", "word": "ensure", "stem": "ensur",
    "avg": [ 6.10, 6.12 ], "std": [ 2.19, 1.36 ], "fq": 50 
  },
  "event": {
    "dict": "happiness", "word": "event", "stem": "event",
    "avg": [ 5.10, 6.12 ], "std": [ 2.40, 1.65 ], "fq": 50 
  },
  "face": {
    "dict": "happiness", "word": "face", "stem": "face",
    "avg": [ 5.04, 6.12 ], "std": [ 2.18, 1.17 ], "fq": 50 
  },
  "focus": {
    "dict": "happiness", "word": "focus", "stem": "focu",
    "avg": [ 4.65, 6.12 ], "std": [ 2.13, 1.06 ], "fq": 50 
  },
  "investing": {
    "dict": "happiness", "word": "investing", "stem": "invest",
    "avg": [ 5.12, 6.12 ], "std": [ 2.42, 1.55 ], "fq": 50 
  },
  "knows": {
    "dict": "happiness", "word": "knows", "stem": "know",
    "avg": [ 6.38, 6.12 ], "std": [ 2.68, 0.90 ], "fq": 50 
  },
  "masters": {
    "dict": "happiness", "word": "masters", "stem": "master",
    "avg": [ 5.20, 6.12 ], "std": [ 2.85, 1.33 ], "fq": 50 
  },
  "nursing": {
    "dict": "happiness", "word": "nursing", "stem": "nurs",
    "avg": [ 4.84, 6.12 ], "std": [ 2.04, 1.47 ], "fq": 50 
  },
  "patiently": {
    "dict": "happiness", "word": "patiently", "stem": "patient",
    "avg": [ 4.21, 6.12 ], "std": [ 2.37, 1.51 ], "fq": 50 
  },
  "snowing": {
    "dict": "happiness", "word": "snowing", "stem": "snow",
    "avg": [ 5.75, 6.12 ], "std": [ 2.47, 2.16 ], "fq": 50 
  },
  "studied": {
    "dict": "happiness", "word": "studied", "stem": "studi",
    "avg": [ 5.39, 6.12 ], "std": [ 2.22, 1.30 ], "fq": 50 
  },
  "study": {
    "dict": "happiness", "word": "study", "stem": "studi",
    "avg": [ 4.08, 6.12 ], "std": [ 2.41, 1.62 ], "fq": 50 
  },
  "theme": {
    "dict": "happiness", "word": "theme", "stem": "theme",
    "avg": [ 5.86, 6.12 ], "std": [ 1.81, 1.17 ], "fq": 50 
  },
  "treasurer": {
    "dict": "happiness", "word": "treasurer", "stem": "treasur",
    "avg": [ 6.75, 6.12 ], "std": [ 2.30, 1.52 ], "fq": 50 
  },
  "nearer": {
    "dict": "happiness", "word": "nearer", "stem": "nearer",
    "avg": [ 5.43, 6.10 ], "std": [ 2.85, 1.18 ], "fq": 50 
  },
  "nurses": {
    "dict": "happiness", "word": "nurses", "stem": "nurs",
    "avg": [ 4.84, 6.10 ], "std": [ 2.04, 1.92 ], "fq": 50 
  },
  "preserved": {
    "dict": "happiness", "word": "preserved", "stem": "preserv",
    "avg": [ 4.95, 6.10 ], "std": [ 2.19, 1.40 ], "fq": 50 
  },
  "senses": {
    "dict": "happiness", "word": "senses", "stem": "sens",
    "avg": [ 4.14, 6.10 ], "std": [ 2.11, 1.49 ], "fq": 50 
  },
  "cattle": {
    "dict": "happiness", "word": "cattle", "stem": "cattl",
    "avg": [ 3.49, 6.10 ], "std": [ 2.13, 1.39 ], "fq": 50 
  },
  "check": {
    "dict": "happiness", "word": "check", "stem": "check",
    "avg": [ 6.10, 6.10 ], "std": [ 2.19, 1.53 ], "fq": 50 
  },
  "customers": {
    "dict": "happiness", "word": "customers", "stem": "custom",
    "avg": [ 4.66, 6.10 ], "std": [ 2.12, 1.09 ], "fq": 50 
  },
  "essence": {
    "dict": "happiness", "word": "essence", "stem": "essenc",
    "avg": [ 5.63, 6.10 ], "std": [ 2.07, 1.15 ], "fq": 50 
  },
  "increasingly": {
    "dict": "happiness", "word": "increasingly", "stem": "increasingli",
    "avg": [ 6.02, 6.10 ], "std": [ 2.58, 1.34 ], "fq": 50 
  },
  "investments": {
    "dict": "happiness", "word": "investments", "stem": "invest",
    "avg": [ 5.12, 6.10 ], "std": [ 2.42, 1.67 ], "fq": 50 
  },
  "keeping": {
    "dict": "happiness", "word": "keeping", "stem": "keep",
    "avg": [ 4.95, 6.10 ], "std": [ 2.19, 1.11 ], "fq": 50 
  },
  "know": {
    "dict": "happiness", "word": "know", "stem": "know",
    "avg": [ 6.38, 6.10 ], "std": [ 2.68, 1.39 ], "fq": 50 
  },
  "markets": {
    "dict": "happiness", "word": "markets", "stem": "market",
    "avg": [ 4.12, 6.10 ], "std": [ 1.83, 1.17 ], "fq": 50 
  },
  "moments": {
    "dict": "happiness", "word": "moments", "stem": "moment",
    "avg": [ 3.83, 6.10 ], "std": [ 2.29, 1.11 ], "fq": 50 
  },
  "open": {
    "dict": "happiness", "word": "open", "stem": "open",
    "avg": [ 5.92, 6.10 ], "std": [ 2.55, 1.36 ], "fq": 50 
  },
  "release": {
    "dict": "happiness", "word": "release", "stem": "releas",
    "avg": [ 7.17, 6.10 ], "std": [ 2.06, 1.23 ], "fq": 50 
  },
  "security": {
    "dict": "happiness", "word": "security", "stem": "secur",
    "avg": [ 3.14, 6.10 ], "std": [ 2.47, 1.63 ], "fq": 50 
  },
  "shade": {
    "dict": "happiness", "word": "shade", "stem": "shade",
    "avg": [ 4.30, 6.10 ], "std": [ 2.26, 1.68 ], "fq": 50 
  },
  "start": {
    "dict": "happiness", "word": "start", "stem": "start",
    "avg": [ 3.82, 6.10 ], "std": [ 2.24, 1.54 ], "fq": 50 
  },
  "window": {
    "dict": "happiness", "word": "window", "stem": "window",
    "avg": [ 3.97, 6.10 ], "std": [ 2.01, 1.45 ], "fq": 50 
  },
  "dawning": {
    "dict": "happiness", "word": "dawning", "stem": "dawn",
    "avg": [ 4.39, 6.08 ], "std": [ 2.81, 1.44 ], "fq": 50 
  },
  "crops": {
    "dict": "happiness", "word": "crops", "stem": "crop",
    "avg": [ 4.05, 6.08 ], "std": [ 1.89, 1.61 ], "fq": 50 
  },
  "throne": {
    "dict": "happiness", "word": "throne", "stem": "throne",
    "avg": [ 4.00, 6.08 ], "std": [ 2.14, 2.11 ], "fq": 50 
  },
  "acquainted": {
    "dict": "happiness", "word": "acquainted", "stem": "acquaint",
    "avg": [ 5.12, 6.08 ], "std": [ 2.39, 1.55 ], "fq": 50 
  },
  "ball": {
    "dict": "happiness", "word": "ball", "stem": "ball",
    "avg": [ 3.76, 6.08 ], "std": [ 2.39, 1.23 ], "fq": 50 
  },
  "belief": {
    "dict": "happiness", "word": "belief", "stem": "belief",
    "avg": [ 4.89, 6.08 ], "std": [ 2.46, 1.44 ], "fq": 50 
  },
  "boots": {
    "dict": "happiness", "word": "boots", "stem": "boot",
    "avg": [ 8.02, 6.08 ], "std": [ 1.65, 1.37 ], "fq": 50 
  },
  "coat": {
    "dict": "happiness", "word": "coat", "stem": "coat",
    "avg": [ 5.00, 6.08 ], "std": [ 2.37, 1.24 ], "fq": 50 
  },
  "grown": {
    "dict": "happiness", "word": "grown", "stem": "grown",
    "avg": [ 3.90, 6.08 ], "std": [ 1.95, 1.24 ], "fq": 50 
  },
  "housing": {
    "dict": "happiness", "word": "housing", "stem": "hous",
    "avg": [ 4.56, 6.08 ], "std": [ 2.41, 1.44 ], "fq": 50 
  },
  "instant": {
    "dict": "happiness", "word": "instant", "stem": "instant",
    "avg": [ 5.44, 6.08 ], "std": [ 2.68, 1.12 ], "fq": 50 
  },
  "introduction": {
    "dict": "happiness", "word": "introduction", "stem": "introduct",
    "avg": [ 5.12, 6.08 ], "std": [ 2.39, 1.01 ], "fq": 50 
  },
  "message": {
    "dict": "happiness", "word": "message", "stem": "messag",
    "avg": [ 4.32, 6.08 ], "std": [ 2.14, 1.12 ], "fq": 50 
  },
  "picked": {
    "dict": "happiness", "word": "picked", "stem": "pick",
    "avg": [ 3.27, 6.08 ], "std": [ 1.98, 1.21 ], "fq": 50 
  },
  "reached": {
    "dict": "happiness", "word": "reached", "stem": "reach",
    "avg": [ 5.73, 6.08 ], "std": [ 2.09, 1.26 ], "fq": 50 
  },
  "recognize": {
    "dict": "happiness", "word": "recognize", "stem": "recogn",
    "avg": [ 5.27, 6.08 ], "std": [ 2.31, 1.41 ], "fq": 50 
  },
  "recognized": {
    "dict": "happiness", "word": "recognized", "stem": "recogn",
    "avg": [ 5.40, 6.08 ], "std": [ 2.70, 1.31 ], "fq": 50 
  },
  "shows": {
    "dict": "happiness", "word": "shows", "stem": "show",
    "avg": [ 5.12, 6.08 ], "std": [ 2.39, 1.05 ], "fq": 50 
  },
  "superior": {
    "dict": "happiness", "word": "superior", "stem": "superior",
    "avg": [ 5.20, 6.08 ], "std": [ 2.85, 1.52 ], "fq": 50 
  },
  "vehicle": {
    "dict": "happiness", "word": "vehicle", "stem": "vehicl",
    "avg": [ 4.63, 6.08 ], "std": [ 2.81, 1.45 ], "fq": 50 
  },
  "theories": {
    "dict": "happiness", "word": "theories", "stem": "theori",
    "avg": [ 4.62, 6.06 ], "std": [ 1.94, 1.45 ], "fq": 50 
  },
  "fluid": {
    "dict": "happiness", "word": "fluid", "stem": "fluid",
    "avg": [ 4.91, 6.06 ], "std": [ 2.57, 1.23 ], "fq": 50 
  },
  "shells": {
    "dict": "happiness", "word": "shells", "stem": "shell",
    "avg": [ 5.52, 6.06 ], "std": [ 2.87, 1.51 ], "fq": 50 
  },
  "adults": {
    "dict": "happiness", "word": "adults", "stem": "adult",
    "avg": [ 4.76, 6.06 ], "std": [ 1.95, 1.30 ], "fq": 50 
  },
  "composition": {
    "dict": "happiness", "word": "composition", "stem": "composit",
    "avg": [ 2.50, 6.06 ], "std": [ 1.85, 1.19 ], "fq": 50 
  },
  "dimes": {
    "dict": "happiness", "word": "dimes", "stem": "dime",
    "avg": [ 4.39, 6.06 ], "std": [ 2.36, 1.22 ], "fq": 50 
  },
  "harbor": {
    "dict": "happiness", "word": "harbor", "stem": "harbor",
    "avg": [ 4.84, 6.06 ], "std": [ 2.04, 1.45 ], "fq": 50 
  },
  "influences": {
    "dict": "happiness", "word": "influences", "stem": "influenc",
    "avg": [ 5.16, 6.06 ], "std": [ 2.25, 1.22 ], "fq": 50 
  },
  "instruments": {
    "dict": "happiness", "word": "instruments", "stem": "instrument",
    "avg": [ 4.33, 6.06 ], "std": [ 1.78, 1.71 ], "fq": 50 
  },
  "leads": {
    "dict": "happiness", "word": "leads", "stem": "lead",
    "avg": [ 3.15, 6.06 ], "std": [ 1.77, 1.10 ], "fq": 50 
  },
  "muscle": {
    "dict": "happiness", "word": "muscle", "stem": "muscl",
    "avg": [ 5.47, 6.06 ], "std": [ 2.20, 1.33 ], "fq": 50 
  },
  "personal": {
    "dict": "happiness", "word": "personal", "stem": "person",
    "avg": [ 4.19, 6.06 ], "std": [ 2.45, 1.22 ], "fq": 50 
  },
  "preparation": {
    "dict": "happiness", "word": "preparation", "stem": "prepar",
    "avg": [ 4.44, 6.06 ], "std": [ 1.96, 1.36 ], "fq": 50 
  },
  "reflection": {
    "dict": "happiness", "word": "reflection", "stem": "reflect",
    "avg": [ 5.72, 6.06 ], "std": [ 2.30, 1.39 ], "fq": 50 
  },
  "respective": {
    "dict": "happiness", "word": "respective", "stem": "respect",
    "avg": [ 4.60, 6.06 ], "std": [ 2.67, 1.32 ], "fq": 50 
  },
  "see": {
    "dict": "happiness", "word": "see", "stem": "see",
    "avg": [ 6.10, 6.06 ], "std": [ 2.19, 1.06 ], "fq": 50 
  },
  "servings": {
    "dict": "happiness", "word": "servings", "stem": "serv",
    "avg": [ 5.41, 6.06 ], "std": [ 2.43, 1.41 ], "fq": 50 
  },
  "sports": {
    "dict": "happiness", "word": "sports", "stem": "sport",
    "avg": [ 4.84, 6.06 ], "std": [ 2.52, 2.24 ], "fq": 50 
  },
  "starring": {
    "dict": "happiness", "word": "starring", "stem": "star",
    "avg": [ 5.83, 6.06 ], "std": [ 2.44, 1.30 ], "fq": 50 
  },
  "straight": {
    "dict": "happiness", "word": "straight", "stem": "straight",
    "avg": [ 3.18, 6.06 ], "std": [ 1.76, 1.06 ], "fq": 50 
  },
  "skirt": {
    "dict": "happiness", "word": "skirt", "stem": "skirt",
    "avg": [ 4.24, 6.04 ], "std": [ 2.43, 2.07 ], "fq": 50 
  },
  "acquired": {
    "dict": "happiness", "word": "acquired", "stem": "acquir",
    "avg": [ 7.72, 6.04 ], "std": [ 2.16, 1.51 ], "fq": 50 
  },
  "alumni": {
    "dict": "happiness", "word": "alumni", "stem": "alumni",
    "avg": [ 7.25, 6.04 ], "std": [ 2.25, 1.03 ], "fq": 50 
  },
  "casino": {
    "dict": "happiness", "word": "casino", "stem": "casino",
    "avg": [ 6.51, 6.04 ], "std": [ 2.12, 2.04 ], "fq": 50 
  },
  "choices": {
    "dict": "happiness", "word": "choices", "stem": "choic",
    "avg": [ 4.74, 6.04 ], "std": [ 2.23, 1.44 ], "fq": 50 
  },
  "folks": {
    "dict": "happiness", "word": "folks", "stem": "folk",
    "avg": [ 4.80, 6.04 ], "std": [ 2.71, 1.35 ], "fq": 50 
  },
  "hint": {
    "dict": "happiness", "word": "hint", "stem": "hint",
    "avg": [ 4.59, 6.04 ], "std": [ 2.10, 1.59 ], "fq": 50 
  },
  "mind": {
    "dict": "happiness", "word": "mind", "stem": "mind",
    "avg": [ 5.00, 6.04 ], "std": [ 2.68, 1.28 ], "fq": 50 
  },
  "points": {
    "dict": "happiness", "word": "points", "stem": "point",
    "avg": [ 4.10, 6.04 ], "std": [ 2.24, 1.47 ], "fq": 50 
  },
  "prevention": {
    "dict": "happiness", "word": "prevention", "stem": "prevent",
    "avg": [ 5.00, 6.04 ], "std": [ 2.83, 1.23 ], "fq": 50 
  },
  "prospects": {
    "dict": "happiness", "word": "prospects", "stem": "prospect",
    "avg": [ 5.38, 6.04 ], "std": [ 2.58, 1.07 ], "fq": 50 
  },
  "purpose": {
    "dict": "happiness", "word": "purpose", "stem": "purpos",
    "avg": [ 4.26, 6.04 ], "std": [ 2.47, 1.16 ], "fq": 50 
  },
  "replied": {
    "dict": "happiness", "word": "replied", "stem": "repli",
    "avg": [ 5.41, 6.04 ], "std": [ 2.43, 0.97 ], "fq": 50 
  },
  "signing": {
    "dict": "happiness", "word": "signing", "stem": "sign",
    "avg": [ 4.05, 6.04 ], "std": [ 2.59, 1.48 ], "fq": 50 
  },
  "tops": {
    "dict": "happiness", "word": "tops", "stem": "top",
    "avg": [ 4.28, 6.04 ], "std": [ 2.53, 1.09 ], "fq": 50 
  },
  "transport": {
    "dict": "happiness", "word": "transport", "stem": "transport",
    "avg": [ 7.38, 6.04 ], "std": [ 1.92, 1.29 ], "fq": 50 
  },
  "union": {
    "dict": "happiness", "word": "union", "stem": "union",
    "avg": [ 3.75, 6.04 ], "std": [ 2.49, 1.40 ], "fq": 50 
  },
  "vocal": {
    "dict": "happiness", "word": "vocal", "stem": "vocal",
    "avg": [ 6.07, 6.04 ], "std": [ 2.42, 1.55 ], "fq": 50 
  },
  "words": {
    "dict": "happiness", "word": "words", "stem": "word",
    "avg": [ 5.17, 6.04 ], "std": [ 2.11, 1.19 ], "fq": 50 
  },
  "beings": {
    "dict": "happiness", "word": "beings", "stem": "be",
    "avg": [ 5.53, 6.02 ], "std": [ 2.90, 1.25 ], "fq": 50 
  },
  "colored": {
    "dict": "happiness", "word": "colored", "stem": "color",
    "avg": [ 4.73, 6.02 ], "std": [ 2.64, 1.74 ], "fq": 50 
  },
  "considerations": {
    "dict": "happiness", "word": "considerations", "stem": "consider",
    "avg": [ 5.72, 6.02 ], "std": [ 2.30, 1.41 ], "fq": 50 
  },
  "nearest": {
    "dict": "happiness", "word": "nearest", "stem": "nearest",
    "avg": [ 5.43, 6.02 ], "std": [ 2.85, 1.25 ], "fq": 50 
  },
  "basket": {
    "dict": "happiness", "word": "basket", "stem": "basket",
    "avg": [ 3.63, 6.02 ], "std": [ 2.02, 1.08 ], "fq": 50 
  },
  "cards": {
    "dict": "happiness", "word": "cards", "stem": "card",
    "avg": [ 5.42, 6.02 ], "std": [ 2.44, 1.30 ], "fq": 50 
  },
  "celebrity": {
    "dict": "happiness", "word": "celebrity", "stem": "celebr",
    "avg": [ 6.55, 6.02 ], "std": [ 2.46, 1.71 ], "fq": 50 
  },
  "content": {
    "dict": "happiness", "word": "content", "stem": "content",
    "avg": [ 4.32, 6.02 ], "std": [ 2.14, 1.62 ], "fq": 50 
  },
  "delivery": {
    "dict": "happiness", "word": "delivery", "stem": "deliveri",
    "avg": [ 6.53, 6.02 ], "std": [ 2.56, 1.44 ], "fq": 50 
  },
  "developing": {
    "dict": "happiness", "word": "developing", "stem": "develop",
    "avg": [ 5.74, 6.02 ], "std": [ 2.46, 1.10 ], "fq": 50 
  },
  "doll": {
    "dict": "happiness", "word": "doll", "stem": "doll",
    "avg": [ 4.24, 6.02 ], "std": [ 2.43, 1.94 ], "fq": 50 
  },
  "eggs": {
    "dict": "happiness", "word": "eggs", "stem": "egg",
    "avg": [ 3.76, 6.02 ], "std": [ 2.39, 1.99 ], "fq": 50 
  },
  "engineers": {
    "dict": "happiness", "word": "engineers", "stem": "engin",
    "avg": [ 3.98, 6.02 ], "std": [ 2.33, 1.13 ], "fq": 50 
  },
  "fixed": {
    "dict": "happiness", "word": "fixed", "stem": "fix",
    "avg": [ 3.14, 6.02 ], "std": [ 2.47, 1.06 ], "fq": 50 
  },
  "jam": {
    "dict": "happiness", "word": "jam", "stem": "jam",
    "avg": [ 5.52, 6.02 ], "std": [ 2.87, 2.03 ], "fq": 50 
  },
  "male": {
    "dict": "happiness", "word": "male", "stem": "male",
    "avg": [ 5.24, 6.02 ], "std": [ 2.31, 1.36 ], "fq": 50 
  },
  "newspapers": {
    "dict": "happiness", "word": "newspapers", "stem": "newspap",
    "avg": [ 2.50, 6.02 ], "std": [ 1.85, 1.46 ], "fq": 50 
  },
  "quick": {
    "dict": "happiness", "word": "quick", "stem": "quick",
    "avg": [ 6.57, 6.02 ], "std": [ 1.78, 1.63 ], "fq": 50 
  },
  "records": {
    "dict": "happiness", "word": "records", "stem": "record",
    "avg": [ 5.42, 6.02 ], "std": [ 2.25, 1.29 ], "fq": 50 
  },
  "retire": {
    "dict": "happiness", "word": "retire", "stem": "retir",
    "avg": [ 3.61, 6.02 ], "std": [ 2.56, 1.80 ], "fq": 50 
  },
  "sophisticated": {
    "dict": "happiness", "word": "sophisticated", "stem": "sophist",
    "avg": [ 6.26, 6.02 ], "std": [ 2.61, 1.76 ], "fq": 50 
  },
  "try": {
    "dict": "happiness", "word": "try", "stem": "tri",
    "avg": [ 7.45, 6.02 ], "std": [ 2.38, 0.94 ], "fq": 50 
  },
  "unwind": {
    "dict": "happiness", "word": "unwind", "stem": "unwind",
    "avg": [ 2.39, 6.02 ], "std": [ 2.13, 1.85 ], "fq": 50 
  },
  "windows": {
    "dict": "happiness", "word": "windows", "stem": "window",
    "avg": [ 3.97, 6.02 ], "std": [ 2.01, 1.39 ], "fq": 50 
  },
  "wondering": {
    "dict": "happiness", "word": "wondering", "stem": "wonder",
    "avg": [ 5.00, 6.02 ], "std": [ 2.23, 1.35 ], "fq": 50 
  },
  "writes": {
    "dict": "happiness", "word": "writes", "stem": "write",
    "avg": [ 4.95, 6.02 ], "std": [ 2.19, 1.38 ], "fq": 50 
  },
  "rains": {
    "dict": "happiness", "word": "rains", "stem": "rain",
    "avg": [ 3.65, 6.01 ], "std": [ 2.35, 1.87 ], "fq": 50 
  },
  "allow": {
    "dict": "happiness", "word": "allow", "stem": "allow",
    "avg": [ 3.27, 6.00 ], "std": [ 2.05, 1.47 ], "fq": 50 
  },
  "beliefs": {
    "dict": "happiness", "word": "beliefs", "stem": "belief",
    "avg": [ 4.89, 6.00 ], "std": [ 2.46, 1.51 ], "fq": 50 
  },
  "biggest": {
    "dict": "happiness", "word": "biggest", "stem": "biggest",
    "avg": [ 4.76, 6.00 ], "std": [ 1.95, 1.32 ], "fq": 50 
  },
  "brook": {
    "dict": "happiness", "word": "brook", "stem": "brook",
    "avg": [ 3.93, 6.00 ], "std": [ 2.49, 1.64 ], "fq": 50 
  },
  "concentrations": {
    "dict": "happiness", "word": "concentrations", "stem": "concentr",
    "avg": [ 4.65, 6.00 ], "std": [ 2.13, 1.29 ], "fq": 50 
  },
  "crimson": {
    "dict": "happiness", "word": "crimson", "stem": "crimson",
    "avg": [ 6.89, 6.00 ], "std": [ 2.47, 1.51 ], "fq": 50 
  },
  "favor": {
    "dict": "happiness", "word": "favor", "stem": "favor",
    "avg": [ 4.54, 6.00 ], "std": [ 1.86, 2.06 ], "fq": 50 
  },
  "find": {
    "dict": "happiness", "word": "find", "stem": "find",
    "avg": [ 5.42, 6.00 ], "std": [ 2.44, 1.58 ], "fq": 50 
  },
  "fixing": {
    "dict": "happiness", "word": "fixing", "stem": "fix",
    "avg": [ 5.86, 6.00 ], "std": [ 2.70, 1.07 ], "fq": 50 
  },
  "global": {
    "dict": "happiness", "word": "global", "stem": "global",
    "avg": [ 5.32, 6.00 ], "std": [ 2.39, 1.48 ], "fq": 50 
  },
  "hands": {
    "dict": "happiness", "word": "hands", "stem": "hand",
    "avg": [ 4.40, 6.00 ], "std": [ 2.07, 1.48 ], "fq": 50 
  },
  "lawn": {
    "dict": "happiness", "word": "lawn", "stem": "lawn",
    "avg": [ 4.00, 6.00 ], "std": [ 1.79, 1.23 ], "fq": 50 
  },
  "lighting": {
    "dict": "happiness", "word": "lighting", "stem": "light",
    "avg": [ 7.17, 6.00 ], "std": [ 2.06, 1.44 ], "fq": 50 
  },
  "make": {
    "dict": "happiness", "word": "make", "stem": "make",
    "avg": [ 4.20, 6.00 ], "std": [ 2.18, 0.99 ], "fq": 50 
  },
  "metals": {
    "dict": "happiness", "word": "metals", "stem": "metal",
    "avg": [ 3.79, 6.00 ], "std": [ 1.96, 1.35 ], "fq": 50 
  },
  "result": {
    "dict": "happiness", "word": "result", "stem": "result",
    "avg": [ 5.41, 6.00 ], "std": [ 2.43, 1.16 ], "fq": 50 
  },
  "sights": {
    "dict": "happiness", "word": "sights", "stem": "sight",
    "avg": [ 5.49, 6.00 ], "std": [ 2.43, 1.50 ], "fq": 50 
  },
  "sites": {
    "dict": "happiness", "word": "sites", "stem": "site",
    "avg": [ 2.95, 6.00 ], "std": [ 1.72, 1.16 ], "fq": 50 
  },
  "sponsor": {
    "dict": "happiness", "word": "sponsor", "stem": "sponsor",
    "avg": [ 5.12, 6.00 ], "std": [ 2.39, 1.41 ], "fq": 50 
  },
  "started": {
    "dict": "happiness", "word": "started", "stem": "start",
    "avg": [ 3.82, 6.00 ], "std": [ 2.24, 1.07 ], "fq": 50 
  },
  "stores": {
    "dict": "happiness", "word": "stores", "stem": "store",
    "avg": [ 5.42, 6.00 ], "std": [ 2.25, 0.97 ], "fq": 50 
  },
  "survive": {
    "dict": "happiness", "word": "survive", "stem": "surviv",
    "avg": [ 5.53, 6.00 ], "std": [ 2.90, 1.80 ], "fq": 50 
  },
  "surviving": {
    "dict": "happiness", "word": "surviving", "stem": "surviv",
    "avg": [ 5.53, 6.00 ], "std": [ 2.90, 1.75 ], "fq": 50 
  },
  "tuned": {
    "dict": "happiness", "word": "tuned", "stem": "tune",
    "avg": [ 4.71, 6.00 ], "std": [ 2.09, 0.97 ], "fq": 50 
  },
  "virgin": {
    "dict": "happiness", "word": "virgin", "stem": "virgin",
    "avg": [ 5.51, 6.00 ], "std": [ 2.06, 1.58 ], "fq": 50 
  },
  "action": {
    "dict": "happiness", "word": "action", "stem": "action",
    "avg": [ 5.71, 5.98 ], "std": [ 2.74, 1.42 ], "fq": 50 
  },
  "august": {
    "dict": "happiness", "word": "august", "stem": "august",
    "avg": [ 4.00, 5.98 ], "std": [ 1.60, 1.44 ], "fq": 50 
  },
  "author": {
    "dict": "happiness", "word": "author", "stem": "author",
    "avg": [ 4.33, 5.98 ], "std": [ 2.45, 1.39 ], "fq": 50 
  },
  "biography": {
    "dict": "happiness", "word": "biography", "stem": "biographi",
    "avg": [ 6.02, 5.98 ], "std": [ 2.62, 1.45 ], "fq": 50 
  },
  "broadcast": {
    "dict": "happiness", "word": "broadcast", "stem": "broadcast",
    "avg": [ 4.12, 5.98 ], "std": [ 2.30, 1.29 ], "fq": 50 
  },
  "creatures": {
    "dict": "happiness", "word": "creatures", "stem": "creatur",
    "avg": [ 4.33, 5.98 ], "std": [ 1.78, 1.38 ], "fq": 50 
  },
  "drum": {
    "dict": "happiness", "word": "drum", "stem": "drum",
    "avg": [ 3.36, 5.98 ], "std": [ 2.28, 1.38 ], "fq": 50 
  },
  "egg": {
    "dict": "happiness", "word": "egg", "stem": "egg",
    "avg": [ 3.76, 5.98 ], "std": [ 2.39, 1.44 ], "fq": 50 
  },
  "explained": {
    "dict": "happiness", "word": "explained", "stem": "explain",
    "avg": [ 4.48, 5.98 ], "std": [ 2.29, 1.32 ], "fq": 50 
  },
  "fabric": {
    "dict": "happiness", "word": "fabric", "stem": "fabric",
    "avg": [ 4.14, 5.98 ], "std": [ 1.98, 1.10 ], "fq": 50 
  },
  "flash": {
    "dict": "happiness", "word": "flash", "stem": "flash",
    "avg": [ 5.44, 5.98 ], "std": [ 2.68, 1.04 ], "fq": 50 
  },
  "folk": {
    "dict": "happiness", "word": "folk", "stem": "folk",
    "avg": [ 4.80, 5.98 ], "std": [ 2.71, 1.44 ], "fq": 50 
  },
  "identity": {
    "dict": "happiness", "word": "identity", "stem": "ident",
    "avg": [ 4.95, 5.98 ], "std": [ 2.24, 1.12 ], "fq": 50 
  },
  "informal": {
    "dict": "happiness", "word": "informal", "stem": "inform",
    "avg": [ 6.98, 5.98 ], "std": [ 2.21, 1.45 ], "fq": 50 
  },
  "keys": {
    "dict": "happiness", "word": "keys", "stem": "key",
    "avg": [ 3.70, 5.98 ], "std": [ 2.18, 1.20 ], "fq": 50 
  },
  "lessons": {
    "dict": "happiness", "word": "lessons", "stem": "lesson",
    "avg": [ 4.49, 5.98 ], "std": [ 2.28, 1.38 ], "fq": 50 
  },
  "looks": {
    "dict": "happiness", "word": "looks", "stem": "look",
    "avg": [ 5.56, 5.98 ], "std": [ 2.62, 1.38 ], "fq": 50 
  },
  "meets": {
    "dict": "happiness", "word": "meets", "stem": "meet",
    "avg": [ 4.94, 5.98 ], "std": [ 2.63, 1.10 ], "fq": 50 
  },
  "messages": {
    "dict": "happiness", "word": "messages", "stem": "messag",
    "avg": [ 4.32, 5.98 ], "std": [ 2.14, 0.94 ], "fq": 50 
  },
  "national": {
    "dict": "happiness", "word": "national", "stem": "nation",
    "avg": [ 4.21, 5.98 ], "std": [ 2.94, 1.15 ], "fq": 50 
  },
  "pairs": {
    "dict": "happiness", "word": "pairs", "stem": "pair",
    "avg": [ 6.39, 5.98 ], "std": [ 2.31, 1.17 ], "fq": 50 
  },
  "pic": {
    "dict": "happiness", "word": "pic", "stem": "pic",
    "avg": [ 4.93, 5.98 ], "std": [ 2.54, 1.17 ], "fq": 50 
  },
  "recordings": {
    "dict": "happiness", "word": "recordings", "stem": "record",
    "avg": [ 5.42, 5.98 ], "std": [ 2.25, 1.24 ], "fq": 50 
  },
  "represented": {
    "dict": "happiness", "word": "represented", "stem": "repres",
    "avg": [ 5.12, 5.98 ], "std": [ 2.39, 1.17 ], "fq": 50 
  },
  "schools": {
    "dict": "happiness", "word": "schools", "stem": "school",
    "avg": [ 5.74, 5.98 ], "std": [ 2.46, 1.44 ], "fq": 50 
  },
  "store": {
    "dict": "happiness", "word": "store", "stem": "store",
    "avg": [ 5.42, 5.98 ], "std": [ 2.25, 0.98 ], "fq": 50 
  },
  "train": {
    "dict": "happiness", "word": "train", "stem": "train",
    "avg": [ 5.74, 5.98 ], "std": [ 2.46, 1.49 ], "fq": 50 
  },
  "lasts": {
    "dict": "happiness", "word": "lasts", "stem": "last",
    "avg": [ 5.53, 5.98 ], "std": [ 2.90, 1.76 ], "fq": 50 
  },
  "refer": {
    "dict": "happiness", "word": "refer", "stem": "refer",
    "avg": [ 4.25, 5.98 ], "std": [ 2.47, 1.11 ], "fq": 50 
  },
  "souls": {
    "dict": "happiness", "word": "souls", "stem": "soul",
    "avg": [ 4.19, 5.98 ], "std": [ 2.45, 1.71 ], "fq": 50 
  },
  "allowed": {
    "dict": "happiness", "word": "allowed", "stem": "allow",
    "avg": [ 3.27, 5.96 ], "std": [ 2.05, 1.74 ], "fq": 50 
  },
  "body": {
    "dict": "happiness", "word": "body", "stem": "bodi",
    "avg": [ 5.52, 5.96 ], "std": [ 2.63, 1.03 ], "fq": 50 
  },
  "convinced": {
    "dict": "happiness", "word": "convinced", "stem": "convinc",
    "avg": [ 6.22, 5.96 ], "std": [ 2.41, 0.97 ], "fq": 50 
  },
  "head": {
    "dict": "happiness", "word": "head", "stem": "head",
    "avg": [ 5.00, 5.96 ], "std": [ 2.68, 1.07 ], "fq": 50 
  },
  "heels": {
    "dict": "happiness", "word": "heels", "stem": "heel",
    "avg": [ 5.76, 5.96 ], "std": [ 2.50, 1.12 ], "fq": 50 
  },
  "made": {
    "dict": "happiness", "word": "made", "stem": "made",
    "avg": [ 4.20, 5.96 ], "std": [ 2.18, 1.07 ], "fq": 50 
  },
  "match": {
    "dict": "happiness", "word": "match", "stem": "match",
    "avg": [ 6.39, 5.96 ], "std": [ 2.31, 0.99 ], "fq": 50 
  },
  "mighty": {
    "dict": "happiness", "word": "mighty", "stem": "mighti",
    "avg": [ 5.61, 5.96 ], "std": [ 2.38, 1.31 ], "fq": 50 
  },
  "net": {
    "dict": "happiness", "word": "net", "stem": "net",
    "avg": [ 6.68, 5.96 ], "std": [ 1.78, 1.03 ], "fq": 50 
  },
  "presently": {
    "dict": "happiness", "word": "presently", "stem": "present",
    "avg": [ 5.12, 5.96 ], "std": [ 2.39, 1.26 ], "fq": 50 
  },
  "reaches": {
    "dict": "happiness", "word": "reaches", "stem": "reach",
    "avg": [ 5.61, 5.96 ], "std": [ 2.92, 1.37 ], "fq": 50 
  },
  "releases": {
    "dict": "happiness", "word": "releases", "stem": "releas",
    "avg": [ 7.17, 5.96 ], "std": [ 2.06, 1.47 ], "fq": 50 
  },
  "rocks": {
    "dict": "happiness", "word": "rocks", "stem": "rock",
    "avg": [ 4.52, 5.96 ], "std": [ 2.37, 1.48 ], "fq": 50 
  },
  "selection": {
    "dict": "happiness", "word": "selection", "stem": "select",
    "avg": [ 4.74, 5.96 ], "std": [ 2.23, 1.29 ], "fq": 50 
  },
  "ship": {
    "dict": "happiness", "word": "ship", "stem": "ship",
    "avg": [ 4.38, 5.96 ], "std": [ 2.29, 1.23 ], "fq": 50 
  },
  "ships": {
    "dict": "happiness", "word": "ships", "stem": "ship",
    "avg": [ 4.38, 5.96 ], "std": [ 2.29, 1.01 ], "fq": 50 
  },
  "space": {
    "dict": "happiness", "word": "space", "stem": "space",
    "avg": [ 5.14, 5.96 ], "std": [ 2.54, 1.01 ], "fq": 50 
  },
  "stadium": {
    "dict": "happiness", "word": "stadium", "stem": "stadium",
    "avg": [ 3.47, 5.96 ], "std": [ 2.12, 1.58 ], "fq": 50 
  },
  "starts": {
    "dict": "happiness", "word": "starts", "stem": "start",
    "avg": [ 3.82, 5.96 ], "std": [ 2.24, 1.19 ], "fq": 50 
  },
  "taught": {
    "dict": "happiness", "word": "taught", "stem": "taught",
    "avg": [ 5.39, 5.96 ], "std": [ 2.22, 1.46 ], "fq": 50 
  },
  "writer": {
    "dict": "happiness", "word": "writer", "stem": "writer",
    "avg": [ 4.33, 5.96 ], "std": [ 2.45, 1.54 ], "fq": 50 
  },
  "justify": {
    "dict": "happiness", "word": "justify", "stem": "justifi",
    "avg": [ 4.48, 5.96 ], "std": [ 2.29, 1.34 ], "fq": 50 
  },
  "spreading": {
    "dict": "happiness", "word": "spreading", "stem": "spread",
    "avg": [ 4.12, 5.96 ], "std": [ 2.30, 1.31 ], "fq": 50 
  },
  "exhibit": {
    "dict": "happiness", "word": "exhibit", "stem": "exhibit",
    "avg": [ 5.12, 5.96 ], "std": [ 2.39, 1.25 ], "fq": 50 
  },
  "fiddle": {
    "dict": "happiness", "word": "fiddle", "stem": "fiddl",
    "avg": [ 5.11, 5.96 ], "std": [ 2.84, 1.73 ], "fq": 50 
  },
  "alternative": {
    "dict": "happiness", "word": "alternative", "stem": "altern",
    "avg": [ 4.74, 5.94 ], "std": [ 2.23, 1.39 ], "fq": 50 
  },
  "awe": {
    "dict": "happiness", "word": "awe", "stem": "awe",
    "avg": [ 5.74, 5.94 ], "std": [ 2.31, 2.09 ], "fq": 50 
  },
  "building": {
    "dict": "happiness", "word": "building", "stem": "build",
    "avg": [ 3.92, 5.94 ], "std": [ 1.94, 1.11 ], "fq": 50 
  },
  "chick": {
    "dict": "happiness", "word": "chick", "stem": "chick",
    "avg": [ 4.24, 5.94 ], "std": [ 2.43, 1.65 ], "fq": 50 
  },
  "consent": {
    "dict": "happiness", "word": "consent", "stem": "consent",
    "avg": [ 5.40, 5.94 ], "std": [ 2.70, 1.22 ], "fq": 50 
  },
  "correspondence": {
    "dict": "happiness", "word": "correspondence", "stem": "correspond",
    "avg": [ 5.02, 5.94 ], "std": [ 2.24, 1.32 ], "fq": 50 
  },
  "custom": {
    "dict": "happiness", "word": "custom", "stem": "custom",
    "avg": [ 4.66, 5.94 ], "std": [ 2.12, 0.91 ], "fq": 50 
  },
  "diary": {
    "dict": "happiness", "word": "diary", "stem": "diari",
    "avg": [ 4.05, 5.94 ], "std": [ 1.96, 1.15 ], "fq": 50 
  },
  "elevation": {
    "dict": "happiness", "word": "elevation", "stem": "elev",
    "avg": [ 4.16, 5.94 ], "std": [ 1.99, 1.52 ], "fq": 50 
  },
  "finds": {
    "dict": "happiness", "word": "finds", "stem": "find",
    "avg": [ 5.42, 5.94 ], "std": [ 2.44, 1.25 ], "fq": 50 
  },
  "framework": {
    "dict": "happiness", "word": "framework", "stem": "framework",
    "avg": [ 4.14, 5.94 ], "std": [ 1.98, 1.06 ], "fq": 50 
  },
  "frank": {
    "dict": "happiness", "word": "frank", "stem": "frank",
    "avg": [ 5.76, 5.94 ], "std": [ 2.50, 1.30 ], "fq": 50 
  },
  "impression": {
    "dict": "happiness", "word": "impression", "stem": "impress",
    "avg": [ 5.42, 5.94 ], "std": [ 2.65, 1.08 ], "fq": 50 
  },
  "jet": {
    "dict": "happiness", "word": "jet", "stem": "jet",
    "avg": [ 4.28, 5.94 ], "std": [ 2.46, 1.63 ], "fq": 50 
  },
  "kings": {
    "dict": "happiness", "word": "kings", "stem": "king",
    "avg": [ 5.51, 5.94 ], "std": [ 2.77, 1.53 ], "fq": 50 
  },
  "knew": {
    "dict": "happiness", "word": "knew", "stem": "knew",
    "avg": [ 6.38, 5.94 ], "std": [ 2.68, 1.30 ], "fq": 50 
  },
  "letter": {
    "dict": "happiness", "word": "letter", "stem": "letter",
    "avg": [ 4.90, 5.94 ], "std": [ 2.37, 1.10 ], "fq": 50 
  },
  "listen": {
    "dict": "happiness", "word": "listen", "stem": "listen",
    "avg": [ 5.00, 5.94 ], "std": [ 2.68, 1.43 ], "fq": 50 
  },
  "looking": {
    "dict": "happiness", "word": "looking", "stem": "look",
    "avg": [ 5.04, 5.94 ], "std": [ 2.18, 0.98 ], "fq": 50 
  },
  "member": {
    "dict": "happiness", "word": "member", "stem": "member",
    "avg": [ 5.54, 5.94 ], "std": [ 2.63, 1.11 ], "fq": 50 
  },
  "men": {
    "dict": "happiness", "word": "men", "stem": "men",
    "avg": [ 4.50, 5.94 ], "std": [ 1.91, 1.39 ], "fq": 50 
  },
  "option": {
    "dict": "happiness", "word": "option", "stem": "option",
    "avg": [ 4.74, 5.94 ], "std": [ 2.23, 1.39 ], "fq": 50 
  },
  "preparations": {
    "dict": "happiness", "word": "preparations", "stem": "prepar",
    "avg": [ 4.44, 5.94 ], "std": [ 1.96, 1.41 ], "fq": 50 
  },
  "reality": {
    "dict": "happiness", "word": "reality", "stem": "realiti",
    "avg": [ 5.32, 5.94 ], "std": [ 2.39, 1.65 ], "fq": 50 
  },
  "reservations": {
    "dict": "happiness", "word": "reservations", "stem": "reserv",
    "avg": [ 3.27, 5.94 ], "std": [ 2.05, 1.46 ], "fq": 50 
  },
  "submitted": {
    "dict": "happiness", "word": "submitted", "stem": "submit",
    "avg": [ 5.12, 5.94 ], "std": [ 2.39, 1.30 ], "fq": 50 
  },
  "substantial": {
    "dict": "happiness", "word": "substantial", "stem": "substanti",
    "avg": [ 3.18, 5.94 ], "std": [ 1.76, 1.10 ], "fq": 50 
  },
  "swift": {
    "dict": "happiness", "word": "swift", "stem": "swift",
    "avg": [ 5.39, 5.94 ], "std": [ 2.53, 1.27 ], "fq": 50 
  },
  "trends": {
    "dict": "happiness", "word": "trends", "stem": "trend",
    "avg": [ 5.00, 5.94 ], "std": [ 2.32, 1.28 ], "fq": 50 
  },
  "wear": {
    "dict": "happiness", "word": "wear", "stem": "wear",
    "avg": [ 2.64, 5.94 ], "std": [ 2.19, 1.39 ], "fq": 50 
  },
  "cloth": {
    "dict": "happiness", "word": "cloth", "stem": "cloth",
    "avg": [ 4.78, 5.94 ], "std": [ 2.88, 1.13 ], "fq": 50 
  },
  "delicate": {
    "dict": "happiness", "word": "delicate", "stem": "delic",
    "avg": [ 4.63, 5.94 ], "std": [ 2.61, 1.53 ], "fq": 50 
  },
  "processing": {
    "dict": "happiness", "word": "processing", "stem": "process",
    "avg": [ 5.62, 5.94 ], "std": [ 2.25, 1.41 ], "fq": 50 
  },
  "bank": {
    "dict": "happiness", "word": "bank", "stem": "bank",
    "avg": [ 5.30, 5.92 ], "std": [ 2.66, 1.63 ], "fq": 50 
  },
  "banks": {
    "dict": "happiness", "word": "banks", "stem": "bank",
    "avg": [ 5.30, 5.92 ], "std": [ 2.66, 1.24 ], "fq": 50 
  },
  "boobs": {
    "dict": "happiness", "word": "boobs", "stem": "boob",
    "avg": [ 4.35, 5.92 ], "std": [ 2.25, 2.14 ], "fq": 50 
  },
  "chicks": {
    "dict": "happiness", "word": "chicks", "stem": "chick",
    "avg": [ 4.24, 5.92 ], "std": [ 2.43, 1.85 ], "fq": 50 
  },
  "covered": {
    "dict": "happiness", "word": "covered", "stem": "cover",
    "avg": [ 5.28, 5.92 ], "std": [ 2.51, 1.01 ], "fq": 50 
  },
  "fields": {
    "dict": "happiness", "word": "fields", "stem": "field",
    "avg": [ 4.08, 5.92 ], "std": [ 2.41, 1.24 ], "fq": 50 
  },
  "get": {
    "dict": "happiness", "word": "get", "stem": "get",
    "avg": [ 5.92, 5.92 ], "std": [ 2.60, 1.08 ], "fq": 50 
  },
  "guy": {
    "dict": "happiness", "word": "guy", "stem": "guy",
    "avg": [ 5.83, 5.92 ], "std": [ 2.73, 1.34 ], "fq": 50 
  },
  "opens": {
    "dict": "happiness", "word": "opens", "stem": "open",
    "avg": [ 5.92, 5.92 ], "std": [ 2.55, 1.28 ], "fq": 50 
  },
  "raining": {
    "dict": "happiness", "word": "raining", "stem": "rain",
    "avg": [ 3.65, 5.92 ], "std": [ 2.35, 2.17 ], "fq": 50 
  },
  "sends": {
    "dict": "happiness", "word": "sends", "stem": "send",
    "avg": [ 5.63, 5.92 ], "std": [ 2.36, 0.92 ], "fq": 50 
  },
  "shorts": {
    "dict": "happiness", "word": "shorts", "stem": "short",
    "avg": [ 5.12, 5.92 ], "std": [ 2.26, 1.26 ], "fq": 50 
  },
  "shown": {
    "dict": "happiness", "word": "shown", "stem": "shown",
    "avg": [ 5.12, 5.92 ], "std": [ 2.39, 1.07 ], "fq": 50 
  },
  "solid": {
    "dict": "happiness", "word": "solid", "stem": "solid",
    "avg": [ 3.18, 5.92 ], "std": [ 1.76, 1.12 ], "fq": 50 
  },
  "umbrella": {
    "dict": "happiness", "word": "umbrella", "stem": "umbrella",
    "avg": [ 3.68, 5.92 ], "std": [ 1.99, 1.29 ], "fq": 50 
  },
  "views": {
    "dict": "happiness", "word": "views", "stem": "view",
    "avg": [ 4.41, 5.92 ], "std": [ 2.30, 1.01 ], "fq": 50 
  },
  "alternatives": {
    "dict": "happiness", "word": "alternatives", "stem": "altern",
    "avg": [ 4.74, 5.92 ], "std": [ 2.23, 1.47 ], "fq": 50 
  },
  "applies": {
    "dict": "happiness", "word": "applies", "stem": "appli",
    "avg": [ 5.28, 5.92 ], "std": [ 2.12, 1.34 ], "fq": 50 
  },
  "generated": {
    "dict": "happiness", "word": "generated", "stem": "gener",
    "avg": [ 5.92, 5.92 ], "std": [ 2.60, 1.29 ], "fq": 50 
  },
  "addition": {
    "dict": "happiness", "word": "addition", "stem": "addit",
    "avg": [ 5.69, 5.90 ], "std": [ 2.15, 1.30 ], "fq": 50 
  },
  "diaries": {
    "dict": "happiness", "word": "diaries", "stem": "diari",
    "avg": [ 4.05, 5.90 ], "std": [ 1.96, 1.39 ], "fq": 50 
  },
  "establish": {
    "dict": "happiness", "word": "establish", "stem": "establish",
    "avg": [ 3.62, 5.90 ], "std": [ 2.25, 1.52 ], "fq": 50 
  },
  "exist": {
    "dict": "happiness", "word": "exist", "stem": "exist",
    "avg": [ 5.53, 5.90 ], "std": [ 2.90, 1.68 ], "fq": 50 
  },
  "existence": {
    "dict": "happiness", "word": "existence", "stem": "exist",
    "avg": [ 5.32, 5.90 ], "std": [ 2.39, 1.25 ], "fq": 50 
  },
  "feel": {
    "dict": "happiness", "word": "feel", "stem": "feel",
    "avg": [ 3.78, 5.90 ], "std": [ 2.42, 1.13 ], "fq": 50 
  },
  "gin": {
    "dict": "happiness", "word": "gin", "stem": "gin",
    "avg": [ 4.39, 5.90 ], "std": [ 2.08, 1.81 ], "fq": 50 
  },
  "grew": {
    "dict": "happiness", "word": "grew", "stem": "grew",
    "avg": [ 3.90, 5.90 ], "std": [ 1.95, 1.33 ], "fq": 50 
  },
  "hand": {
    "dict": "happiness", "word": "hand", "stem": "hand",
    "avg": [ 4.40, 5.90 ], "std": [ 2.07, 1.07 ], "fq": 50 
  },
  "letters": {
    "dict": "happiness", "word": "letters", "stem": "letter",
    "avg": [ 4.90, 5.90 ], "std": [ 2.37, 1.42 ], "fq": 50 
  },
  "man": {
    "dict": "happiness", "word": "man", "stem": "man",
    "avg": [ 5.24, 5.90 ], "std": [ 2.31, 1.40 ], "fq": 50 
  },
  "modest": {
    "dict": "happiness", "word": "modest", "stem": "modest",
    "avg": [ 3.98, 5.90 ], "std": [ 2.24, 1.42 ], "fq": 50 
  },
  "naked": {
    "dict": "happiness", "word": "naked", "stem": "nake",
    "avg": [ 5.80, 5.90 ], "std": [ 2.80, 2.29 ], "fq": 50 
  },
  "pass": {
    "dict": "happiness", "word": "pass", "stem": "pass",
    "avg": [ 4.70, 5.90 ], "std": [ 2.48, 1.43 ], "fq": 50 
  },
  "peak": {
    "dict": "happiness", "word": "peak", "stem": "peak",
    "avg": [ 4.28, 5.90 ], "std": [ 2.53, 1.59 ], "fq": 50 
  },
  "personally": {
    "dict": "happiness", "word": "personally", "stem": "person",
    "avg": [ 4.19, 5.90 ], "std": [ 2.45, 1.07 ], "fq": 50 
  },
  "planes": {
    "dict": "happiness", "word": "planes", "stem": "plane",
    "avg": [ 6.14, 5.90 ], "std": [ 2.39, 1.68 ], "fq": 50 
  },
  "ratings": {
    "dict": "happiness", "word": "ratings", "stem": "rate",
    "avg": [ 7.24, 5.90 ], "std": [ 2.06, 1.27 ], "fq": 50 
  },
  "recording": {
    "dict": "happiness", "word": "recording", "stem": "record",
    "avg": [ 5.42, 5.90 ], "std": [ 2.25, 1.15 ], "fq": 50 
  },
  "replies": {
    "dict": "happiness", "word": "replies", "stem": "repli",
    "avg": [ 5.41, 5.90 ], "std": [ 2.43, 0.95 ], "fq": 50 
  },
  "results": {
    "dict": "happiness", "word": "results", "stem": "result",
    "avg": [ 5.41, 5.90 ], "std": [ 2.43, 1.37 ], "fq": 50 
  },
  "scores": {
    "dict": "happiness", "word": "scores", "stem": "score",
    "avg": [ 5.73, 5.90 ], "std": [ 2.09, 1.13 ], "fq": 50 
  },
  "settlement": {
    "dict": "happiness", "word": "settlement", "stem": "settlement",
    "avg": [ 4.08, 5.90 ], "std": [ 1.87, 1.50 ], "fq": 50 
  },
  "angle": {
    "dict": "happiness", "word": "angle", "stem": "angl",
    "avg": [ 4.00, 5.90 ], "std": [ 2.19, 1.36 ], "fq": 50 
  },
  "dolly": {
    "dict": "happiness", "word": "dolly", "stem": "dolli",
    "avg": [ 4.24, 5.90 ], "std": [ 2.43, 1.34 ], "fq": 50 
  },
  "puppet": {
    "dict": "happiness", "word": "puppet", "stem": "puppet",
    "avg": [ 4.33, 5.90 ], "std": [ 1.78, 1.76 ], "fq": 50 
  },
  "admiral": {
    "dict": "happiness", "word": "admiral", "stem": "admir",
    "avg": [ 6.11, 5.89 ], "std": [ 2.36, 1.40 ], "fq": 50 
  },
  "distinguish": {
    "dict": "happiness", "word": "distinguish", "stem": "distinguish",
    "avg": [ 5.26, 5.88 ], "std": [ 2.36, 1.41 ], "fq": 50 
  },
  "evidently": {
    "dict": "happiness", "word": "evidently", "stem": "evid",
    "avg": [ 3.52, 5.88 ], "std": [ 2.05, 1.35 ], "fq": 50 
  },
  "field": {
    "dict": "happiness", "word": "field", "stem": "field",
    "avg": [ 4.08, 5.88 ], "std": [ 2.41, 1.19 ], "fq": 50 
  },
  "founder": {
    "dict": "happiness", "word": "founder", "stem": "founder",
    "avg": [ 5.92, 5.88 ], "std": [ 2.60, 1.12 ], "fq": 50 
  },
  "keeps": {
    "dict": "happiness", "word": "keeps", "stem": "keep",
    "avg": [ 5.53, 5.88 ], "std": [ 2.90, 1.32 ], "fq": 50 
  },
  "leaders": {
    "dict": "happiness", "word": "leaders", "stem": "leader",
    "avg": [ 6.27, 5.88 ], "std": [ 2.18, 1.32 ], "fq": 50 
  },
  "mood": {
    "dict": "happiness", "word": "mood", "stem": "mood",
    "avg": [ 5.50, 5.88 ], "std": [ 2.91, 1.64 ], "fq": 50 
  },
  "primary": {
    "dict": "happiness", "word": "primary", "stem": "primari",
    "avg": [ 5.20, 5.88 ], "std": [ 2.85, 1.12 ], "fq": 50 
  },
  "printed": {
    "dict": "happiness", "word": "printed", "stem": "print",
    "avg": [ 5.42, 5.88 ], "std": [ 2.65, 0.96 ], "fq": 50 
  },
  "privacy": {
    "dict": "happiness", "word": "privacy", "stem": "privaci",
    "avg": [ 4.12, 5.88 ], "std": [ 1.83, 2.15 ], "fq": 50 
  },
  "scout": {
    "dict": "happiness", "word": "scout", "stem": "scout",
    "avg": [ 4.10, 5.88 ], "std": [ 2.12, 1.10 ], "fq": 50 
  },
  "sequence": {
    "dict": "happiness", "word": "sequence", "stem": "sequenc",
    "avg": [ 6.11, 5.88 ], "std": [ 2.65, 1.32 ], "fq": 50 
  },
  "sustained": {
    "dict": "happiness", "word": "sustained", "stem": "sustain",
    "avg": [ 4.29, 5.88 ], "std": [ 2.51, 1.41 ], "fq": 50 
  },
  "twilight": {
    "dict": "happiness", "word": "twilight", "stem": "twilight",
    "avg": [ 4.70, 5.88 ], "std": [ 2.41, 1.91 ], "fq": 50 
  },
  "weather": {
    "dict": "happiness", "word": "weather", "stem": "weather",
    "avg": [ 6.15, 5.88 ], "std": [ 2.45, 1.52 ], "fq": 50 
  },
  "whole": {
    "dict": "happiness", "word": "whole", "stem": "whole",
    "avg": [ 3.75, 5.88 ], "std": [ 2.49, 1.33 ], "fq": 50 
  },
  "demonstration": {
    "dict": "happiness", "word": "demonstration", "stem": "demonstr",
    "avg": [ 5.12, 5.88 ], "std": [ 2.39, 1.22 ], "fq": 50 
  },
  "flex": {
    "dict": "happiness", "word": "flex", "stem": "flex",
    "avg": [ 4.07, 5.87 ], "std": [ 2.34, 1.16 ], "fq": 50 
  },
  "applied": {
    "dict": "happiness", "word": "applied", "stem": "appli",
    "avg": [ 5.28, 5.86 ], "std": [ 2.12, 1.29 ], "fq": 50 
  },
  "arrangement": {
    "dict": "happiness", "word": "arrangement", "stem": "arrang",
    "avg": [ 5.02, 5.86 ], "std": [ 2.24, 1.12 ], "fq": 50 
  },
  "balls": {
    "dict": "happiness", "word": "balls", "stem": "ball",
    "avg": [ 3.76, 5.86 ], "std": [ 2.39, 1.21 ], "fq": 50 
  },
  "bear": {
    "dict": "happiness", "word": "bear", "stem": "bear",
    "avg": [ 5.40, 5.86 ], "std": [ 2.70, 1.85 ], "fq": 50 
  },
  "brooks": {
    "dict": "happiness", "word": "brooks", "stem": "brook",
    "avg": [ 3.93, 5.86 ], "std": [ 2.49, 1.37 ], "fq": 50 
  },
  "connect": {
    "dict": "happiness", "word": "connect", "stem": "connect",
    "avg": [ 3.75, 5.86 ], "std": [ 2.49, 1.48 ], "fq": 50 
  },
  "curve": {
    "dict": "happiness", "word": "curve", "stem": "curv",
    "avg": [ 5.00, 5.86 ], "std": [ 2.32, 1.48 ], "fq": 50 
  },
  "diverse": {
    "dict": "happiness", "word": "diverse", "stem": "divers",
    "avg": [ 5.04, 5.86 ], "std": [ 2.10, 1.54 ], "fq": 50 
  },
  "engineering": {
    "dict": "happiness", "word": "engineering", "stem": "engin",
    "avg": [ 3.98, 5.86 ], "std": [ 2.33, 1.48 ], "fq": 50 
  },
  "figures": {
    "dict": "happiness", "word": "figures", "stem": "figur",
    "avg": [ 4.75, 5.86 ], "std": [ 1.93, 1.18 ], "fq": 50 
  },
  "hotter": {
    "dict": "happiness", "word": "hotter", "stem": "hotter",
    "avg": [ 4.10, 5.86 ], "std": [ 2.34, 1.54 ], "fq": 50 
  },
  "household": {
    "dict": "happiness", "word": "household", "stem": "household",
    "avg": [ 4.21, 5.86 ], "std": [ 2.94, 1.65 ], "fq": 50 
  },
  "introduce": {
    "dict": "happiness", "word": "introduce", "stem": "introduc",
    "avg": [ 5.12, 5.86 ], "std": [ 2.39, 0.97 ], "fq": 50 
  },
  "keep": {
    "dict": "happiness", "word": "keep", "stem": "keep",
    "avg": [ 5.53, 5.86 ], "std": [ 2.90, 1.07 ], "fq": 50 
  },
  "nut": {
    "dict": "happiness", "word": "nut", "stem": "nut",
    "avg": [ 4.81, 5.86 ], "std": [ 2.46, 1.50 ], "fq": 50 
  },
  "nuts": {
    "dict": "happiness", "word": "nuts", "stem": "nut",
    "avg": [ 4.81, 5.86 ], "std": [ 2.46, 1.63 ], "fq": 50 
  },
  "observations": {
    "dict": "happiness", "word": "observations", "stem": "observ",
    "avg": [ 4.10, 5.86 ], "std": [ 2.12, 1.07 ], "fq": 50 
  },
  "position": {
    "dict": "happiness", "word": "position", "stem": "posit",
    "avg": [ 3.46, 5.86 ], "std": [ 1.72, 1.12 ], "fq": 50 
  },
  "president": {
    "dict": "happiness", "word": "president", "stem": "presid",
    "avg": [ 3.15, 5.86 ], "std": [ 1.77, 2.11 ], "fq": 50 
  },
  "seat": {
    "dict": "happiness", "word": "seat", "stem": "seat",
    "avg": [ 2.95, 5.86 ], "std": [ 1.72, 1.05 ], "fq": 50 
  },
  "sound": {
    "dict": "happiness", "word": "sound", "stem": "sound",
    "avg": [ 5.43, 5.86 ], "std": [ 2.85, 1.28 ], "fq": 50 
  },
  "trained": {
    "dict": "happiness", "word": "trained", "stem": "train",
    "avg": [ 5.74, 5.86 ], "std": [ 2.46, 1.50 ], "fq": 50 
  },
  "variations": {
    "dict": "happiness", "word": "variations", "stem": "variat",
    "avg": [ 4.84, 5.86 ], "std": [ 2.52, 1.20 ], "fq": 50 
  },
  "viewers": {
    "dict": "happiness", "word": "viewers", "stem": "viewer",
    "avg": [ 5.42, 5.86 ], "std": [ 2.44, 1.28 ], "fq": 50 
  },
  "wrapped": {
    "dict": "happiness", "word": "wrapped", "stem": "wrap",
    "avg": [ 4.78, 5.86 ], "std": [ 2.88, 1.31 ], "fq": 50 
  },
  "autonomy": {
    "dict": "happiness", "word": "autonomy", "stem": "autonomi",
    "avg": [ 5.60, 5.86 ], "std": [ 2.65, 1.59 ], "fq": 50 
  },
  "concentrated": {
    "dict": "happiness", "word": "concentrated", "stem": "concentr",
    "avg": [ 4.65, 5.86 ], "std": [ 2.13, 1.29 ], "fq": 50 
  },
  "deeper": {
    "dict": "happiness", "word": "deeper", "stem": "deeper",
    "avg": [ 6.17, 5.86 ], "std": [ 2.70, 1.34 ], "fq": 50 
  },
  "liquid": {
    "dict": "happiness", "word": "liquid", "stem": "liquid",
    "avg": [ 4.91, 5.86 ], "std": [ 2.57, 1.17 ], "fq": 50 
  },
  "concentration": {
    "dict": "happiness", "word": "concentration", "stem": "concentr",
    "avg": [ 4.65, 5.85 ], "std": [ 2.13, 1.56 ], "fq": 50 
  },
  "construct": {
    "dict": "happiness", "word": "construct", "stem": "construct",
    "avg": [ 4.14, 5.85 ], "std": [ 1.98, 1.52 ], "fq": 50 
  },
  "angeles": {
    "dict": "happiness", "word": "angeles", "stem": "angel",
    "avg": [ 4.83, 5.84 ], "std": [ 2.63, 1.56 ], "fq": 50 
  },
  "arena": {
    "dict": "happiness", "word": "arena", "stem": "arena",
    "avg": [ 3.88, 5.84 ], "std": [ 1.99, 1.02 ], "fq": 50 
  },
  "banking": {
    "dict": "happiness", "word": "banking", "stem": "bank",
    "avg": [ 5.30, 5.84 ], "std": [ 2.66, 1.65 ], "fq": 50 
  },
  "buck": {
    "dict": "happiness", "word": "buck", "stem": "buck",
    "avg": [ 3.89, 5.84 ], "std": [ 2.17, 1.78 ], "fq": 50 
  },
  "checks": {
    "dict": "happiness", "word": "checks", "stem": "check",
    "avg": [ 6.10, 5.84 ], "std": [ 2.19, 1.54 ], "fq": 50 
  },
  "circles": {
    "dict": "happiness", "word": "circles", "stem": "circl",
    "avg": [ 3.86, 5.84 ], "std": [ 2.13, 1.18 ], "fq": 50 
  },
  "classes": {
    "dict": "happiness", "word": "classes", "stem": "class",
    "avg": [ 4.80, 5.84 ], "std": [ 2.71, 1.33 ], "fq": 50 
  },
  "coming": {
    "dict": "happiness", "word": "coming", "stem": "come",
    "avg": [ 8.10, 5.84 ], "std": [ 1.45, 1.20 ], "fq": 50 
  },
  "curry": {
    "dict": "happiness", "word": "curry", "stem": "curri",
    "avg": [ 4.05, 5.84 ], "std": [ 1.89, 1.82 ], "fq": 50 
  },
  "feelings": {
    "dict": "happiness", "word": "feelings", "stem": "feel",
    "avg": [ 3.78, 5.84 ], "std": [ 2.42, 1.72 ], "fq": 50 
  },
  "gets": {
    "dict": "happiness", "word": "gets", "stem": "get",
    "avg": [ 5.92, 5.84 ], "std": [ 2.60, 1.30 ], "fq": 50 
  },
  "gravity": {
    "dict": "happiness", "word": "gravity", "stem": "graviti",
    "avg": [ 3.56, 5.84 ], "std": [ 1.95, 1.58 ], "fq": 50 
  },
  "hear": {
    "dict": "happiness", "word": "hear", "stem": "hear",
    "avg": [ 5.39, 5.84 ], "std": [ 2.22, 1.20 ], "fq": 50 
  },
  "history": {
    "dict": "happiness", "word": "history", "stem": "histori",
    "avg": [ 3.93, 5.84 ], "std": [ 2.29, 1.50 ], "fq": 50 
  },
  "individuals": {
    "dict": "happiness", "word": "individuals", "stem": "individu",
    "avg": [ 4.19, 5.84 ], "std": [ 2.45, 1.00 ], "fq": 50 
  },
  "lands": {
    "dict": "happiness", "word": "lands", "stem": "land",
    "avg": [ 4.24, 5.84 ], "std": [ 2.49, 1.33 ], "fq": 50 
  },
  "patents": {
    "dict": "happiness", "word": "patents", "stem": "patent",
    "avg": [ 3.50, 5.84 ], "std": [ 1.84, 1.06 ], "fq": 50 
  },
  "poster": {
    "dict": "happiness", "word": "poster", "stem": "poster",
    "avg": [ 3.93, 5.84 ], "std": [ 2.56, 1.13 ], "fq": 50 
  },
  "producing": {
    "dict": "happiness", "word": "producing", "stem": "produc",
    "avg": [ 3.90, 5.84 ], "std": [ 1.95, 1.33 ], "fq": 50 
  },
  "puff": {
    "dict": "happiness", "word": "puff", "stem": "puff",
    "avg": [ 3.93, 5.84 ], "std": [ 2.85, 1.48 ], "fq": 50 
  },
  "really": {
    "dict": "happiness", "word": "really", "stem": "realli",
    "avg": [ 4.36, 5.84 ], "std": [ 2.18, 1.49 ], "fq": 50 
  },
  "responses": {
    "dict": "happiness", "word": "responses", "stem": "respons",
    "avg": [ 5.41, 5.84 ], "std": [ 2.43, 1.15 ], "fq": 50 
  },
  "sample": {
    "dict": "happiness", "word": "sample", "stem": "sampl",
    "avg": [ 5.22, 5.84 ], "std": [ 2.38, 0.93 ], "fq": 50 
  },
  "showing": {
    "dict": "happiness", "word": "showing", "stem": "show",
    "avg": [ 5.12, 5.84 ], "std": [ 2.39, 0.84 ], "fq": 50 
  },
  "stages": {
    "dict": "happiness", "word": "stages", "stem": "stage",
    "avg": [ 4.95, 5.84 ], "std": [ 2.36, 1.54 ], "fq": 50 
  },
  "watching": {
    "dict": "happiness", "word": "watching", "stem": "watch",
    "avg": [ 4.10, 5.84 ], "std": [ 2.12, 1.22 ], "fq": 50 
  },
  "absorption": {
    "dict": "happiness", "word": "absorption", "stem": "absorpt",
    "avg": [ 4.65, 5.84 ], "std": [ 2.13, 1.36 ], "fq": 50 
  },
  "constructed": {
    "dict": "happiness", "word": "constructed", "stem": "construct",
    "avg": [ 4.14, 5.84 ], "std": [ 1.98, 1.40 ], "fq": 50 
  },
  "examples": {
    "dict": "happiness", "word": "examples", "stem": "exampl",
    "avg": [ 6.84, 5.84 ], "std": [ 2.06, 1.46 ], "fq": 50 
  },
  "shades": {
    "dict": "happiness", "word": "shades", "stem": "shade",
    "avg": [ 4.30, 5.84 ], "std": [ 2.26, 1.40 ], "fq": 50 
  },
  "instruction": {
    "dict": "happiness", "word": "instruction", "stem": "instruct",
    "avg": [ 5.74, 5.83 ], "std": [ 2.46, 1.26 ], "fq": 50 
  },
  "wagon": {
    "dict": "happiness", "word": "wagon", "stem": "wagon",
    "avg": [ 3.98, 5.83 ], "std": [ 2.04, 1.32 ], "fq": 50 
  },
  "apply": {
    "dict": "happiness", "word": "apply", "stem": "appli",
    "avg": [ 5.28, 5.82 ], "std": [ 2.12, 0.80 ], "fq": 50 
  },
  "bar": {
    "dict": "happiness", "word": "bar", "stem": "bar",
    "avg": [ 5.00, 5.82 ], "std": [ 2.83, 1.80 ], "fq": 50 
  },
  "becoming": {
    "dict": "happiness", "word": "becoming", "stem": "becom",
    "avg": [ 5.14, 5.82 ], "std": [ 2.39, 0.92 ], "fq": 50 
  },
  "come": {
    "dict": "happiness", "word": "come", "stem": "come",
    "avg": [ 4.70, 5.82 ], "std": [ 2.48, 1.00 ], "fq": 50 
  },
  "cow": {
    "dict": "happiness", "word": "cow", "stem": "cow",
    "avg": [ 3.49, 5.82 ], "std": [ 2.13, 1.47 ], "fq": 50 
  },
  "detail": {
    "dict": "happiness", "word": "detail", "stem": "detail",
    "avg": [ 4.10, 5.82 ], "std": [ 2.24, 1.14 ], "fq": 50 
  },
  "emphasized": {
    "dict": "happiness", "word": "emphasized", "stem": "emphas",
    "avg": [ 7.45, 5.82 ], "std": [ 2.38, 1.44 ], "fq": 50 
  },
  "endowment": {
    "dict": "happiness", "word": "endowment", "stem": "endow",
    "avg": [ 6.27, 5.82 ], "std": [ 1.80, 1.51 ], "fq": 50 
  },
  "hearing": {
    "dict": "happiness", "word": "hearing", "stem": "hear",
    "avg": [ 5.39, 5.82 ], "std": [ 2.22, 1.48 ], "fq": 50 
  },
  "homey": {
    "dict": "happiness", "word": "homey", "stem": "homey",
    "avg": [ 4.21, 5.82 ], "std": [ 2.94, 2.06 ], "fq": 50 
  },
  "investment": {
    "dict": "happiness", "word": "investment", "stem": "invest",
    "avg": [ 5.12, 5.82 ], "std": [ 2.42, 1.81 ], "fq": 50 
  },
  "involved": {
    "dict": "happiness", "word": "involved", "stem": "involv",
    "avg": [ 6.21, 5.82 ], "std": [ 2.75, 1.34 ], "fq": 50 
  },
  "key": {
    "dict": "happiness", "word": "key", "stem": "key",
    "avg": [ 3.70, 5.82 ], "std": [ 2.18, 1.06 ], "fq": 50 
  },
  "lived": {
    "dict": "happiness", "word": "lived", "stem": "live",
    "avg": [ 5.53, 5.82 ], "std": [ 2.90, 1.60 ], "fq": 50 
  },
  "met": {
    "dict": "happiness", "word": "met", "stem": "met",
    "avg": [ 4.94, 5.82 ], "std": [ 2.63, 0.92 ], "fq": 50 
  },
  "opinion": {
    "dict": "happiness", "word": "opinion", "stem": "opinion",
    "avg": [ 4.89, 5.82 ], "std": [ 2.46, 1.34 ], "fq": 50 
  },
  "owl": {
    "dict": "happiness", "word": "owl", "stem": "owl",
    "avg": [ 3.98, 5.82 ], "std": [ 1.87, 1.86 ], "fq": 50 
  },
  "pair": {
    "dict": "happiness", "word": "pair", "stem": "pair",
    "avg": [ 6.39, 5.82 ], "std": [ 2.31, 1.19 ], "fq": 50 
  },
  "peoples": {
    "dict": "happiness", "word": "peoples", "stem": "peopl",
    "avg": [ 5.94, 5.82 ], "std": [ 2.09, 1.37 ], "fq": 50 
  },
  "quickly": {
    "dict": "happiness", "word": "quickly", "stem": "quickli",
    "avg": [ 6.57, 5.82 ], "std": [ 1.78, 1.45 ], "fq": 50 
  },
  "regarded": {
    "dict": "happiness", "word": "regarded", "stem": "regard",
    "avg": [ 6.21, 5.82 ], "std": [ 2.75, 1.17 ], "fq": 50 
  },
  "sum": {
    "dict": "happiness", "word": "sum", "stem": "sum",
    "avg": [ 6.34, 5.82 ], "std": [ 2.25, 1.14 ], "fq": 50 
  },
  "mist": {
    "dict": "happiness", "word": "mist", "stem": "mist",
    "avg": [ 3.30, 5.82 ], "std": [ 2.08, 1.58 ], "fq": 50 
  },
  "acquisition": {
    "dict": "happiness", "word": "acquisition", "stem": "acquisit",
    "avg": [ 5.39, 5.80 ], "std": [ 2.22, 1.53 ], "fq": 50 
  },
  "addressed": {
    "dict": "happiness", "word": "addressed", "stem": "address",
    "avg": [ 5.62, 5.80 ], "std": [ 2.25, 1.21 ], "fq": 50 
  },
  "determine": {
    "dict": "happiness", "word": "determine", "stem": "determin",
    "avg": [ 4.07, 5.80 ], "std": [ 1.98, 1.34 ], "fq": 50 
  },
  "double": {
    "dict": "happiness", "word": "double", "stem": "doubl",
    "avg": [ 3.96, 5.80 ], "std": [ 1.94, 1.37 ], "fq": 50 
  },
  "establishing": {
    "dict": "happiness", "word": "establishing", "stem": "establish",
    "avg": [ 3.62, 5.80 ], "std": [ 2.25, 1.40 ], "fq": 50 
  },
  "finding": {
    "dict": "happiness", "word": "finding", "stem": "find",
    "avg": [ 5.42, 5.80 ], "std": [ 2.44, 1.21 ], "fq": 50 
  },
  "ice": {
    "dict": "happiness", "word": "ice", "stem": "ice",
    "avg": [ 4.16, 5.80 ], "std": [ 2.16, 1.48 ], "fq": 50 
  },
  "interior": {
    "dict": "happiness", "word": "interior", "stem": "interior",
    "avg": [ 4.21, 5.80 ], "std": [ 2.94, 0.88 ], "fq": 50 
  },
  "known": {
    "dict": "happiness", "word": "known", "stem": "known",
    "avg": [ 6.38, 5.80 ], "std": [ 2.68, 1.39 ], "fq": 50 
  },
  "liberal": {
    "dict": "happiness", "word": "liberal", "stem": "liber",
    "avg": [ 5.95, 5.80 ], "std": [ 2.73, 2.17 ], "fq": 50 
  },
  "model": {
    "dict": "happiness", "word": "model", "stem": "model",
    "avg": [ 4.07, 5.80 ], "std": [ 1.98, 1.09 ], "fq": 50 
  },
  "outside": {
    "dict": "happiness", "word": "outside", "stem": "outsid",
    "avg": [ 5.92, 5.80 ], "std": [ 2.55, 1.68 ], "fq": 50 
  },
  "paper": {
    "dict": "happiness", "word": "paper", "stem": "paper",
    "avg": [ 2.50, 5.80 ], "std": [ 1.85, 1.20 ], "fq": 50 
  },
  "pardon": {
    "dict": "happiness", "word": "pardon", "stem": "pardon",
    "avg": [ 4.48, 5.80 ], "std": [ 2.29, 1.63 ], "fq": 50 
  },
  "practice": {
    "dict": "happiness", "word": "practice", "stem": "practic",
    "avg": [ 4.26, 5.80 ], "std": [ 2.47, 1.34 ], "fq": 50 
  },
  "rubber": {
    "dict": "happiness", "word": "rubber", "stem": "rubber",
    "avg": [ 3.86, 5.80 ], "std": [ 2.72, 1.36 ], "fq": 50 
  },
  "sending": {
    "dict": "happiness", "word": "sending", "stem": "send",
    "avg": [ 5.63, 5.80 ], "std": [ 2.36, 0.93 ], "fq": 50 
  },
  "shaped": {
    "dict": "happiness", "word": "shaped", "stem": "shape",
    "avg": [ 4.07, 5.80 ], "std": [ 1.98, 1.21 ], "fq": 50 
  },
  "write": {
    "dict": "happiness", "word": "write", "stem": "write",
    "avg": [ 4.95, 5.80 ], "std": [ 2.19, 1.47 ], "fq": 50 
  },
  "yellow": {
    "dict": "happiness", "word": "yellow", "stem": "yellow",
    "avg": [ 4.43, 5.80 ], "std": [ 2.05, 1.46 ], "fq": 50 
  },
  "seated": {
    "dict": "happiness", "word": "seated", "stem": "seat",
    "avg": [ 2.95, 5.80 ], "std": [ 1.72, 1.22 ], "fq": 50 
  },
  "gender": {
    "dict": "happiness", "word": "gender", "stem": "gender",
    "avg": [ 4.38, 5.80 ], "std": [ 2.13, 1.24 ], "fq": 50 
  },
  "involve": {
    "dict": "happiness", "word": "involve", "stem": "involv",
    "avg": [ 6.21, 5.80 ], "std": [ 2.75, 1.34 ], "fq": 50 
  },
  "manufacture": {
    "dict": "happiness", "word": "manufacture", "stem": "manufactur",
    "avg": [ 4.14, 5.80 ], "std": [ 1.98, 1.43 ], "fq": 50 
  },
  "sentiment": {
    "dict": "happiness", "word": "sentiment", "stem": "sentiment",
    "avg": [ 4.41, 5.80 ], "std": [ 2.30, 1.90 ], "fq": 50 
  },
  "arch": {
    "dict": "happiness", "word": "arch", "stem": "arch",
    "avg": [ 6.09, 5.79 ], "std": [ 2.44, 1.31 ], "fq": 50 
  },
  "actions": {
    "dict": "happiness", "word": "actions", "stem": "action",
    "avg": [ 5.71, 5.78 ], "std": [ 2.74, 0.89 ], "fq": 50 
  },
  "amber": {
    "dict": "happiness", "word": "amber", "stem": "amber",
    "avg": [ 5.76, 5.78 ], "std": [ 2.79, 1.50 ], "fq": 50 
  },
  "aware": {
    "dict": "happiness", "word": "aware", "stem": "awar",
    "avg": [ 5.00, 5.78 ], "std": [ 2.68, 1.47 ], "fq": 50 
  },
  "characters": {
    "dict": "happiness", "word": "characters", "stem": "charact",
    "avg": [ 4.48, 5.78 ], "std": [ 2.12, 1.40 ], "fq": 50 
  },
  "containing": {
    "dict": "happiness", "word": "containing", "stem": "contain",
    "avg": [ 6.10, 5.78 ], "std": [ 2.19, 1.00 ], "fq": 50 
  },
  "fed": {
    "dict": "happiness", "word": "fed", "stem": "fed",
    "avg": [ 5.69, 5.78 ], "std": [ 2.51, 1.49 ], "fq": 50 
  },
  "flows": {
    "dict": "happiness", "word": "flows", "stem": "flow",
    "avg": [ 4.70, 5.78 ], "std": [ 2.48, 1.36 ], "fq": 50 
  },
  "founding": {
    "dict": "happiness", "word": "founding", "stem": "found",
    "avg": [ 3.62, 5.78 ], "std": [ 2.25, 1.46 ], "fq": 50 
  },
  "hottest": {
    "dict": "happiness", "word": "hottest", "stem": "hottest",
    "avg": [ 4.10, 5.78 ], "std": [ 2.34, 2.19 ], "fq": 50 
  },
  "lift": {
    "dict": "happiness", "word": "lift", "stem": "lift",
    "avg": [ 5.64, 5.78 ], "std": [ 2.99, 1.04 ], "fq": 50 
  },
  "link": {
    "dict": "happiness", "word": "link", "stem": "link",
    "avg": [ 3.75, 5.78 ], "std": [ 2.49, 1.11 ], "fq": 50 
  },
  "lot": {
    "dict": "happiness", "word": "lot", "stem": "lot",
    "avg": [ 5.49, 5.78 ], "std": [ 2.43, 1.37 ], "fq": 50 
  },
  "morality": {
    "dict": "happiness", "word": "morality", "stem": "moral",
    "avg": [ 4.49, 5.78 ], "std": [ 2.28, 1.80 ], "fq": 50 
  },
  "passages": {
    "dict": "happiness", "word": "passages", "stem": "passag",
    "avg": [ 4.36, 5.78 ], "std": [ 2.13, 1.23 ], "fq": 50 
  },
  "plates": {
    "dict": "happiness", "word": "plates", "stem": "plate",
    "avg": [ 4.21, 5.78 ], "std": [ 2.94, 1.33 ], "fq": 50 
  },
  "record": {
    "dict": "happiness", "word": "record", "stem": "record",
    "avg": [ 5.42, 5.78 ], "std": [ 2.25, 1.40 ], "fq": 50 
  },
  "respond": {
    "dict": "happiness", "word": "respond", "stem": "respond",
    "avg": [ 5.41, 5.78 ], "std": [ 2.43, 1.06 ], "fq": 50 
  },
  "shuttle": {
    "dict": "happiness", "word": "shuttle", "stem": "shuttl",
    "avg": [ 3.17, 5.78 ], "std": [ 2.23, 0.93 ], "fq": 50 
  },
  "trying": {
    "dict": "happiness", "word": "trying", "stem": "tri",
    "avg": [ 7.45, 5.78 ], "std": [ 2.38, 1.17 ], "fq": 50 
  },
  "various": {
    "dict": "happiness", "word": "various", "stem": "variou",
    "avg": [ 4.60, 5.78 ], "std": [ 2.67, 0.86 ], "fq": 50 
  },
  "volume": {
    "dict": "happiness", "word": "volume", "stem": "volum",
    "avg": [ 4.17, 5.78 ], "std": [ 2.49, 1.50 ], "fq": 50 
  },
  "workout": {
    "dict": "happiness", "word": "workout", "stem": "workout",
    "avg": [ 6.84, 5.78 ], "std": [ 2.06, 2.08 ], "fq": 50 
  },
  "sober": {
    "dict": "happiness", "word": "sober", "stem": "sober",
    "avg": [ 3.56, 5.78 ], "std": [ 1.95, 1.98 ], "fq": 50 
  },
  "components": {
    "dict": "happiness", "word": "components", "stem": "compon",
    "avg": [ 3.82, 5.78 ], "std": [ 2.24, 1.37 ], "fq": 50 
  },
  "flashing": {
    "dict": "happiness", "word": "flashing", "stem": "flash",
    "avg": [ 5.44, 5.78 ], "std": [ 2.68, 1.65 ], "fq": 50 
  },
  "printing": {
    "dict": "happiness", "word": "printing", "stem": "print",
    "avg": [ 5.42, 5.77 ], "std": [ 2.65, 1.36 ], "fq": 50 
  },
  "accord": {
    "dict": "happiness", "word": "accord", "stem": "accord",
    "avg": [ 5.02, 5.76 ], "std": [ 2.24, 1.24 ], "fq": 50 
  },
  "city": {
    "dict": "happiness", "word": "city", "stem": "citi",
    "avg": [ 5.24, 5.76 ], "std": [ 2.53, 1.55 ], "fq": 50 
  },
  "days": {
    "dict": "happiness", "word": "days", "stem": "day",
    "avg": [ 4.77, 5.76 ], "std": [ 2.50, 1.24 ], "fq": 50 
  },
  "describes": {
    "dict": "happiness", "word": "describes", "stem": "describ",
    "avg": [ 3.70, 5.76 ], "std": [ 2.18, 1.08 ], "fq": 50 
  },
  "facilities": {
    "dict": "happiness", "word": "facilities", "stem": "facil",
    "avg": [ 6.57, 5.76 ], "std": [ 1.78, 1.45 ], "fq": 50 
  },
  "functions": {
    "dict": "happiness", "word": "functions", "stem": "function",
    "avg": [ 4.26, 5.76 ], "std": [ 2.47, 1.24 ], "fq": 50 
  },
  "glass": {
    "dict": "happiness", "word": "glass", "stem": "glass",
    "avg": [ 4.27, 5.76 ], "std": [ 2.07, 1.22 ], "fq": 50 
  },
  "horny": {
    "dict": "happiness", "word": "horny", "stem": "horni",
    "avg": [ 6.63, 5.76 ], "std": [ 2.70, 2.02 ], "fq": 50 
  },
  "lamp": {
    "dict": "happiness", "word": "lamp", "stem": "lamp",
    "avg": [ 3.80, 5.76 ], "std": [ 2.12, 0.98 ], "fq": 50 
  },
  "preparing": {
    "dict": "happiness", "word": "preparing", "stem": "prepar",
    "avg": [ 3.82, 5.76 ], "std": [ 2.40, 1.41 ], "fq": 50 
  },
  "probability": {
    "dict": "happiness", "word": "probability", "stem": "probabl",
    "avg": [ 5.38, 5.76 ], "std": [ 2.58, 1.25 ], "fq": 50 
  },
  "referring": {
    "dict": "happiness", "word": "referring", "stem": "refer",
    "avg": [ 4.25, 5.76 ], "std": [ 2.47, 1.17 ], "fq": 50 
  },
  "representing": {
    "dict": "happiness", "word": "representing", "stem": "repres",
    "avg": [ 5.12, 5.76 ], "std": [ 2.39, 1.10 ], "fq": 50 
  },
  "sees": {
    "dict": "happiness", "word": "sees", "stem": "see",
    "avg": [ 6.10, 5.76 ], "std": [ 2.19, 1.41 ], "fq": 50 
  },
  "selling": {
    "dict": "happiness", "word": "selling", "stem": "sell",
    "avg": [ 7.24, 5.76 ], "std": [ 2.06, 1.59 ], "fq": 50 
  },
  "slide": {
    "dict": "happiness", "word": "slide", "stem": "slide",
    "avg": [ 4.59, 5.76 ], "std": [ 2.31, 1.22 ], "fq": 50 
  },
  "staying": {
    "dict": "happiness", "word": "staying", "stem": "stay",
    "avg": [ 5.62, 5.76 ], "std": [ 2.39, 1.35 ], "fq": 50 
  },
  "viewing": {
    "dict": "happiness", "word": "viewing", "stem": "view",
    "avg": [ 4.10, 5.76 ], "std": [ 2.12, 1.42 ], "fq": 50 
  },
  "vital": {
    "dict": "happiness", "word": "vital", "stem": "vital",
    "avg": [ 5.53, 5.76 ], "std": [ 2.90, 1.56 ], "fq": 50 
  },
  "voice": {
    "dict": "happiness", "word": "voice", "stem": "voic",
    "avg": [ 3.82, 5.76 ], "std": [ 2.24, 1.06 ], "fq": 50 
  },
  "handed": {
    "dict": "happiness", "word": "handed", "stem": "hand",
    "avg": [ 4.40, 5.76 ], "std": [ 2.07, 1.38 ], "fq": 50 
  },
  "thoroughly": {
    "dict": "happiness", "word": "thoroughly", "stem": "thoroughli",
    "avg": [ 5.43, 5.76 ], "std": [ 2.85, 1.44 ], "fq": 50 
  },
  "awake": {
    "dict": "happiness", "word": "awake", "stem": "awak",
    "avg": [ 6.85, 5.74 ], "std": [ 2.53, 1.47 ], "fq": 50 
  },
  "call": {
    "dict": "happiness", "word": "call", "stem": "call",
    "avg": [ 6.07, 5.74 ], "std": [ 2.42, 1.44 ], "fq": 50 
  },
  "calling": {
    "dict": "happiness", "word": "calling", "stem": "call",
    "avg": [ 4.25, 5.74 ], "std": [ 2.47, 1.26 ], "fq": 50 
  },
  "catch": {
    "dict": "happiness", "word": "catch", "stem": "catch",
    "avg": [ 5.83, 5.74 ], "std": [ 2.73, 1.38 ], "fq": 50 
  },
  "concentrate": {
    "dict": "happiness", "word": "concentrate", "stem": "concentr",
    "avg": [ 4.65, 5.74 ], "std": [ 2.13, 1.59 ], "fq": 50 
  },
  "deep": {
    "dict": "happiness", "word": "deep", "stem": "deep",
    "avg": [ 6.17, 5.74 ], "std": [ 2.70, 1.40 ], "fq": 50 
  },
  "details": {
    "dict": "happiness", "word": "details", "stem": "detail",
    "avg": [ 4.10, 5.74 ], "std": [ 2.24, 1.23 ], "fq": 50 
  },
  "fundamental": {
    "dict": "happiness", "word": "fundamental", "stem": "fundament",
    "avg": [ 3.70, 5.74 ], "std": [ 2.18, 0.96 ], "fq": 50 
  },
  "given": {
    "dict": "happiness", "word": "given", "stem": "given",
    "avg": [ 5.00, 5.74 ], "std": [ 2.68, 1.44 ], "fq": 50 
  },
  "kept": {
    "dict": "happiness", "word": "kept", "stem": "kept",
    "avg": [ 4.95, 5.74 ], "std": [ 2.19, 1.10 ], "fq": 50 
  },
  "kinds": {
    "dict": "happiness", "word": "kinds", "stem": "kind",
    "avg": [ 4.30, 5.74 ], "std": [ 2.62, 1.05 ], "fq": 50 
  },
  "name": {
    "dict": "happiness", "word": "name", "stem": "name",
    "avg": [ 4.25, 5.74 ], "std": [ 2.47, 1.17 ], "fq": 50 
  },
  "observed": {
    "dict": "happiness", "word": "observed", "stem": "observ",
    "avg": [ 4.10, 5.74 ], "std": [ 2.12, 1.03 ], "fq": 50 
  },
  "presented": {
    "dict": "happiness", "word": "presented", "stem": "present",
    "avg": [ 5.12, 5.74 ], "std": [ 2.39, 0.99 ], "fq": 50 
  },
  "reach": {
    "dict": "happiness", "word": "reach", "stem": "reach",
    "avg": [ 5.61, 5.74 ], "std": [ 2.92, 1.40 ], "fq": 50 
  },
  "responded": {
    "dict": "happiness", "word": "responded", "stem": "respond",
    "avg": [ 5.41, 5.74 ], "std": [ 2.43, 1.29 ], "fq": 50 
  },
  "screen": {
    "dict": "happiness", "word": "screen", "stem": "screen",
    "avg": [ 4.39, 5.74 ], "std": [ 2.36, 1.26 ], "fq": 50 
  },
  "serves": {
    "dict": "happiness", "word": "serves", "stem": "serv",
    "avg": [ 5.41, 5.74 ], "std": [ 2.43, 1.65 ], "fq": 50 
  },
  "settled": {
    "dict": "happiness", "word": "settled", "stem": "settl",
    "avg": [ 4.70, 5.74 ], "std": [ 2.48, 1.55 ], "fq": 50 
  },
  "showed": {
    "dict": "happiness", "word": "showed", "stem": "show",
    "avg": [ 5.12, 5.74 ], "std": [ 2.39, 1.01 ], "fq": 50 
  },
  "spare": {
    "dict": "happiness", "word": "spare", "stem": "spare",
    "avg": [ 3.52, 5.74 ], "std": [ 2.05, 1.51 ], "fq": 50 
  },
  "suits": {
    "dict": "happiness", "word": "suits", "stem": "suit",
    "avg": [ 4.93, 5.74 ], "std": [ 2.44, 1.01 ], "fq": 50 
  },
  "swag": {
    "dict": "happiness", "word": "swag", "stem": "swag",
    "avg": [ 4.60, 5.74 ], "std": [ 2.35, 1.19 ], "fq": 50 
  },
  "thin": {
    "dict": "happiness", "word": "thin", "stem": "thin",
    "avg": [ 5.00, 5.74 ], "std": [ 2.32, 1.38 ], "fq": 50 
  },
  "time": {
    "dict": "happiness", "word": "time", "stem": "time",
    "avg": [ 4.64, 5.74 ], "std": [ 2.75, 1.21 ], "fq": 50 
  },
  "training": {
    "dict": "happiness", "word": "training", "stem": "train",
    "avg": [ 5.74, 5.74 ], "std": [ 2.46, 1.40 ], "fq": 50 
  },
  "wives": {
    "dict": "happiness", "word": "wives", "stem": "wive",
    "avg": [ 4.93, 5.74 ], "std": [ 2.22, 1.95 ], "fq": 50 
  },
  "involves": {
    "dict": "happiness", "word": "involves", "stem": "involv",
    "avg": [ 6.21, 5.73 ], "std": [ 2.75, 1.04 ], "fq": 50 
  },
  "sphere": {
    "dict": "happiness", "word": "sphere", "stem": "sphere",
    "avg": [ 3.88, 5.73 ], "std": [ 1.99, 1.08 ], "fq": 50 
  },
  "shell": {
    "dict": "happiness", "word": "shell", "stem": "shell",
    "avg": [ 5.52, 5.73 ], "std": [ 2.87, 1.36 ], "fq": 50 
  },
  "pose": {
    "dict": "happiness", "word": "pose", "stem": "pose",
    "avg": [ 4.56, 5.72 ], "std": [ 1.78, 1.19 ], "fq": 50 
  },
  "apt": {
    "dict": "happiness", "word": "apt", "stem": "apt",
    "avg": [ 5.00, 5.72 ], "std": [ 2.68, 1.18 ], "fq": 50 
  },
  "card": {
    "dict": "happiness", "word": "card", "stem": "card",
    "avg": [ 5.42, 5.72 ], "std": [ 2.44, 1.13 ], "fq": 50 
  },
  "click": {
    "dict": "happiness", "word": "click", "stem": "click",
    "avg": [ 4.39, 5.72 ], "std": [ 2.81, 1.03 ], "fq": 50 
  },
  "detailed": {
    "dict": "happiness", "word": "detailed", "stem": "detail",
    "avg": [ 4.10, 5.72 ], "std": [ 2.24, 1.50 ], "fq": 50 
  },
  "funky": {
    "dict": "happiness", "word": "funky", "stem": "funki",
    "avg": [ 4.26, 5.72 ], "std": [ 2.10, 1.68 ], "fq": 50 
  },
  "happening": {
    "dict": "happiness", "word": "happening", "stem": "happen",
    "avg": [ 4.05, 5.72 ], "std": [ 2.34, 1.01 ], "fq": 50 
  },
  "hypothesis": {
    "dict": "happiness", "word": "hypothesis", "stem": "hypothesi",
    "avg": [ 4.62, 5.72 ], "std": [ 1.94, 1.54 ], "fq": 50 
  },
  "implementation": {
    "dict": "happiness", "word": "implementation", "stem": "implement",
    "avg": [ 5.71, 5.72 ], "std": [ 2.74, 1.28 ], "fq": 50 
  },
  "import": {
    "dict": "happiness", "word": "import", "stem": "import",
    "avg": [ 3.83, 5.72 ], "std": [ 2.29, 1.34 ], "fq": 50 
  },
  "individual": {
    "dict": "happiness", "word": "individual", "stem": "individu",
    "avg": [ 4.19, 5.72 ], "std": [ 2.45, 1.37 ], "fq": 50 
  },
  "move": {
    "dict": "happiness", "word": "move", "stem": "move",
    "avg": [ 6.21, 5.72 ], "std": [ 2.51, 1.36 ], "fq": 50 
  },
  "near": {
    "dict": "happiness", "word": "near", "stem": "near",
    "avg": [ 5.43, 5.72 ], "std": [ 2.85, 1.60 ], "fq": 50 
  },
  "plate": {
    "dict": "happiness", "word": "plate", "stem": "plate",
    "avg": [ 4.21, 5.72 ], "std": [ 2.94, 1.07 ], "fq": 50 
  },
  "quietly": {
    "dict": "happiness", "word": "quietly", "stem": "quietli",
    "avg": [ 2.82, 5.72 ], "std": [ 2.13, 1.40 ], "fq": 50 
  },
  "roles": {
    "dict": "happiness", "word": "roles", "stem": "role",
    "avg": [ 4.26, 5.72 ], "std": [ 2.47, 1.40 ], "fq": 50 
  },
  "script": {
    "dict": "happiness", "word": "script", "stem": "script",
    "avg": [ 4.17, 5.72 ], "std": [ 2.49, 1.74 ], "fq": 50 
  },
  "signed": {
    "dict": "happiness", "word": "signed", "stem": "sign",
    "avg": [ 4.05, 5.72 ], "std": [ 2.59, 1.09 ], "fq": 50 
  },
  "source": {
    "dict": "happiness", "word": "source", "stem": "sourc",
    "avg": [ 4.49, 5.72 ], "std": [ 2.24, 1.21 ], "fq": 50 
  },
  "stage": {
    "dict": "happiness", "word": "stage", "stem": "stage",
    "avg": [ 5.12, 5.72 ], "std": [ 2.39, 1.44 ], "fq": 50 
  },
  "taxi": {
    "dict": "happiness", "word": "taxi", "stem": "taxi",
    "avg": [ 3.41, 5.72 ], "std": [ 2.14, 1.26 ], "fq": 50 
  },
  "uses": {
    "dict": "happiness", "word": "uses", "stem": "use",
    "avg": [ 4.26, 5.72 ], "std": [ 2.47, 1.16 ], "fq": 50 
  },
  "view": {
    "dict": "happiness", "word": "view", "stem": "view",
    "avg": [ 4.41, 5.72 ], "std": [ 2.30, 1.13 ], "fq": 50 
  },
  "waking": {
    "dict": "happiness", "word": "waking", "stem": "wake",
    "avg": [ 6.63, 5.72 ], "std": [ 2.70, 1.46 ], "fq": 50 
  },
  "contains": {
    "dict": "happiness", "word": "contains", "stem": "contain",
    "avg": [ 6.10, 5.71 ], "std": [ 2.19, 1.21 ], "fq": 50 
  },
  "employer": {
    "dict": "happiness", "word": "employer", "stem": "employ",
    "avg": [ 5.28, 5.71 ], "std": [ 2.12, 1.72 ], "fq": 50 
  },
  "opinions": {
    "dict": "happiness", "word": "opinions", "stem": "opinion",
    "avg": [ 4.89, 5.71 ], "std": [ 2.46, 1.54 ], "fq": 50 
  },
  "hears": {
    "dict": "happiness", "word": "hears", "stem": "hear",
    "avg": [ 5.39, 5.71 ], "std": [ 2.22, 1.38 ], "fq": 50 
  },
  "scope": {
    "dict": "happiness", "word": "scope", "stem": "scope",
    "avg": [ 5.61, 5.71 ], "std": [ 2.92, 1.41 ], "fq": 50 
  },
  "soil": {
    "dict": "happiness", "word": "soil", "stem": "soil",
    "avg": [ 5.12, 5.71 ], "std": [ 2.32, 1.65 ], "fq": 50 
  },
  "timber": {
    "dict": "happiness", "word": "timber", "stem": "timber",
    "avg": [ 4.48, 5.71 ], "std": [ 2.12, 1.50 ], "fq": 50 
  },
  "appointed": {
    "dict": "happiness", "word": "appointed", "stem": "appoint",
    "avg": [ 4.25, 5.70 ], "std": [ 2.47, 1.42 ], "fq": 50 
  },
  "arrangements": {
    "dict": "happiness", "word": "arrangements", "stem": "arrang",
    "avg": [ 5.02, 5.70 ], "std": [ 2.24, 1.23 ], "fq": 50 
  },
  "banner": {
    "dict": "happiness", "word": "banner", "stem": "banner",
    "avg": [ 3.83, 5.70 ], "std": [ 1.95, 1.04 ], "fq": 50 
  },
  "churches": {
    "dict": "happiness", "word": "churches", "stem": "church",
    "avg": [ 4.34, 5.70 ], "std": [ 2.45, 2.46 ], "fq": 50 
  },
  "contain": {
    "dict": "happiness", "word": "contain", "stem": "contain",
    "avg": [ 6.10, 5.70 ], "std": [ 2.19, 1.18 ], "fq": 50 
  },
  "demonstrated": {
    "dict": "happiness", "word": "demonstrated", "stem": "demonstr",
    "avg": [ 5.12, 5.70 ], "std": [ 2.39, 1.15 ], "fq": 50 
  },
  "engine": {
    "dict": "happiness", "word": "engine", "stem": "engin",
    "avg": [ 3.98, 5.70 ], "std": [ 2.33, 1.23 ], "fq": 50 
  },
  "feeling": {
    "dict": "happiness", "word": "feeling", "stem": "feel",
    "avg": [ 3.78, 5.70 ], "std": [ 2.42, 1.52 ], "fq": 50 
  },
  "fill": {
    "dict": "happiness", "word": "fill", "stem": "fill",
    "avg": [ 4.94, 5.70 ], "std": [ 2.63, 1.23 ], "fq": 50 
  },
  "hat": {
    "dict": "happiness", "word": "hat", "stem": "hat",
    "avg": [ 4.10, 5.70 ], "std": [ 2.00, 1.30 ], "fq": 50 
  },
  "hold": {
    "dict": "happiness", "word": "hold", "stem": "hold",
    "avg": [ 6.10, 5.70 ], "std": [ 2.19, 1.22 ], "fq": 50 
  },
  "identical": {
    "dict": "happiness", "word": "identical", "stem": "ident",
    "avg": [ 4.95, 5.70 ], "std": [ 2.24, 1.47 ], "fq": 50 
  },
  "journal": {
    "dict": "happiness", "word": "journal", "stem": "journal",
    "avg": [ 4.05, 5.70 ], "std": [ 1.96, 1.31 ], "fq": 50 
  },
  "master": {
    "dict": "happiness", "word": "master", "stem": "master",
    "avg": [ 5.20, 5.70 ], "std": [ 2.85, 1.52 ], "fq": 50 
  },
  "mild": {
    "dict": "happiness", "word": "mild", "stem": "mild",
    "avg": [ 4.63, 5.70 ], "std": [ 2.61, 1.50 ], "fq": 50 
  },
  "placing": {
    "dict": "happiness", "word": "placing", "stem": "place",
    "avg": [ 5.12, 5.70 ], "std": [ 2.42, 1.13 ], "fq": 50 
  },
  "rally": {
    "dict": "happiness", "word": "rally", "stem": "ralli",
    "avg": [ 5.00, 5.70 ], "std": [ 2.18, 1.25 ], "fq": 50 
  },
  "rolling": {
    "dict": "happiness", "word": "rolling", "stem": "roll",
    "avg": [ 5.55, 5.70 ], "std": [ 2.39, 1.25 ], "fq": 50 
  },
  "running": {
    "dict": "happiness", "word": "running", "stem": "run",
    "avg": [ 5.71, 5.70 ], "std": [ 2.74, 1.50 ], "fq": 50 
  },
  "thumb": {
    "dict": "happiness", "word": "thumb", "stem": "thumb",
    "avg": [ 3.78, 5.70 ], "std": [ 2.42, 1.36 ], "fq": 50 
  },
  "want": {
    "dict": "happiness", "word": "want", "stem": "want",
    "avg": [ 5.16, 5.70 ], "std": [ 2.62, 1.34 ], "fq": 50 
  },
  "watch": {
    "dict": "happiness", "word": "watch", "stem": "watch",
    "avg": [ 4.10, 5.70 ], "std": [ 2.12, 1.25 ], "fq": 50 
  },
  "whites": {
    "dict": "happiness", "word": "whites", "stem": "white",
    "avg": [ 4.37, 5.70 ], "std": [ 2.14, 1.22 ], "fq": 50 
  },
  "written": {
    "dict": "happiness", "word": "written", "stem": "written",
    "avg": [ 4.95, 5.70 ], "std": [ 2.19, 1.27 ], "fq": 50 
  },
  "determining": {
    "dict": "happiness", "word": "determining", "stem": "determin",
    "avg": [ 4.07, 5.69 ], "std": [ 1.98, 1.34 ], "fq": 50 
  },
  "dusk": {
    "dict": "happiness", "word": "dusk", "stem": "dusk",
    "avg": [ 4.70, 5.69 ], "std": [ 2.48, 1.63 ], "fq": 50 
  },
  "angles": {
    "dict": "happiness", "word": "angles", "stem": "angl",
    "avg": [ 4.00, 5.68 ], "std": [ 2.19, 1.35 ], "fq": 50 
  },
  "avenue": {
    "dict": "happiness", "word": "avenue", "stem": "avenu",
    "avg": [ 4.12, 5.68 ], "std": [ 2.01, 1.17 ], "fq": 50 
  },
  "bars": {
    "dict": "happiness", "word": "bars", "stem": "bar",
    "avg": [ 5.00, 5.68 ], "std": [ 2.83, 1.58 ], "fq": 50 
  },
  "broadcasting": {
    "dict": "happiness", "word": "broadcasting", "stem": "broadcast",
    "avg": [ 4.12, 5.68 ], "std": [ 2.30, 1.32 ], "fq": 50 
  },
  "cabinet": {
    "dict": "happiness", "word": "cabinet", "stem": "cabinet",
    "avg": [ 3.43, 5.68 ], "std": [ 1.85, 1.13 ], "fq": 50 
  },
  "character": {
    "dict": "happiness", "word": "character", "stem": "charact",
    "avg": [ 4.48, 5.68 ], "std": [ 2.12, 1.49 ], "fq": 50 
  },
  "direct": {
    "dict": "happiness", "word": "direct", "stem": "direct",
    "avg": [ 3.98, 5.68 ], "std": [ 2.33, 1.33 ], "fq": 50 
  },
  "emphasis": {
    "dict": "happiness", "word": "emphasis", "stem": "emphasi",
    "avg": [ 7.45, 5.68 ], "std": [ 2.38, 1.00 ], "fq": 50 
  },
  "foreign": {
    "dict": "happiness", "word": "foreign", "stem": "foreign",
    "avg": [ 5.45, 5.68 ], "std": [ 2.15, 1.70 ], "fq": 50 
  },
  "getting": {
    "dict": "happiness", "word": "getting", "stem": "get",
    "avg": [ 5.92, 5.68 ], "std": [ 2.60, 1.19 ], "fq": 50 
  },
  "grounds": {
    "dict": "happiness", "word": "grounds", "stem": "ground",
    "avg": [ 4.24, 5.68 ], "std": [ 2.49, 1.24 ], "fq": 50 
  },
  "machines": {
    "dict": "happiness", "word": "machines", "stem": "machin",
    "avg": [ 3.82, 5.68 ], "std": [ 2.40, 1.30 ], "fq": 50 
  },
  "mars": {
    "dict": "happiness", "word": "mars", "stem": "mar",
    "avg": [ 4.04, 5.68 ], "std": [ 2.14, 0.96 ], "fq": 50 
  },
  "moment": {
    "dict": "happiness", "word": "moment", "stem": "moment",
    "avg": [ 3.83, 5.68 ], "std": [ 2.29, 1.11 ], "fq": 50 
  },
  "moves": {
    "dict": "happiness", "word": "moves", "stem": "move",
    "avg": [ 6.21, 5.68 ], "std": [ 2.51, 0.96 ], "fq": 50 
  },
  "publicity": {
    "dict": "happiness", "word": "publicity", "stem": "public",
    "avg": [ 6.44, 5.68 ], "std": [ 2.58, 1.38 ], "fq": 50 
  },
  "pursue": {
    "dict": "happiness", "word": "pursue", "stem": "pursu",
    "avg": [ 6.77, 5.68 ], "std": [ 2.07, 1.48 ], "fq": 50 
  },
  "response": {
    "dict": "happiness", "word": "response", "stem": "respons",
    "avg": [ 5.41, 5.68 ], "std": [ 2.43, 1.27 ], "fq": 50 
  },
  "role": {
    "dict": "happiness", "word": "role", "stem": "role",
    "avg": [ 4.26, 5.68 ], "std": [ 2.47, 0.89 ], "fq": 50 
  },
  "sitting": {
    "dict": "happiness", "word": "sitting", "stem": "sit",
    "avg": [ 2.95, 5.68 ], "std": [ 1.72, 1.10 ], "fq": 50 
  },
  "suggests": {
    "dict": "happiness", "word": "suggests", "stem": "suggest",
    "avg": [ 6.98, 5.68 ], "std": [ 2.21, 0.94 ], "fq": 50 
  },
  "saddle": {
    "dict": "happiness", "word": "saddle", "stem": "saddl",
    "avg": [ 5.63, 5.67 ], "std": [ 2.07, 1.45 ], "fq": 50 
  },
  "samples": {
    "dict": "happiness", "word": "samples", "stem": "sampl",
    "avg": [ 5.22, 5.67 ], "std": [ 2.38, 1.20 ], "fq": 50 
  },
  "tail": {
    "dict": "happiness", "word": "tail", "stem": "tail",
    "avg": [ 4.30, 5.67 ], "std": [ 2.26, 1.51 ], "fq": 50 
  },
  "evident": {
    "dict": "happiness", "word": "evident", "stem": "evid",
    "avg": [ 3.50, 5.67 ], "std": [ 1.84, 1.32 ], "fq": 50 
  },
  "absorbed": {
    "dict": "happiness", "word": "absorbed", "stem": "absorb",
    "avg": [ 6.77, 5.66 ], "std": [ 2.07, 1.48 ], "fq": 50 
  },
  "aspect": {
    "dict": "happiness", "word": "aspect", "stem": "aspect",
    "avg": [ 5.04, 5.66 ], "std": [ 2.18, 1.06 ], "fq": 50 
  },
  "auto": {
    "dict": "happiness", "word": "auto", "stem": "auto",
    "avg": [ 3.82, 5.66 ], "std": [ 2.40, 1.59 ], "fq": 50 
  },
  "blue": {
    "dict": "happiness", "word": "blue", "stem": "blue",
    "avg": [ 4.31, 5.66 ], "std": [ 2.20, 1.93 ], "fq": 50 
  },
  "bold": {
    "dict": "happiness", "word": "bold", "stem": "bold",
    "avg": [ 5.60, 5.66 ], "std": [ 2.21, 1.79 ], "fq": 50 
  },
  "customer": {
    "dict": "happiness", "word": "customer", "stem": "custom",
    "avg": [ 4.66, 5.66 ], "std": [ 2.12, 1.69 ], "fq": 50 
  },
  "describe": {
    "dict": "happiness", "word": "describe", "stem": "describ",
    "avg": [ 3.70, 5.66 ], "std": [ 2.18, 1.08 ], "fq": 50 
  },
  "digest": {
    "dict": "happiness", "word": "digest", "stem": "digest",
    "avg": [ 4.65, 5.66 ], "std": [ 2.13, 1.49 ], "fq": 50 
  },
  "entrance": {
    "dict": "happiness", "word": "entrance", "stem": "entranc",
    "avg": [ 5.83, 5.66 ], "std": [ 2.73, 0.80 ], "fq": 50 
  },
  "follow": {
    "dict": "happiness", "word": "follow", "stem": "follow",
    "avg": [ 4.10, 5.66 ], "std": [ 2.12, 1.17 ], "fq": 50 
  },
  "foundation": {
    "dict": "happiness", "word": "foundation", "stem": "foundat",
    "avg": [ 3.27, 5.66 ], "std": [ 1.98, 1.36 ], "fq": 50 
  },
  "manufacturing": {
    "dict": "happiness", "word": "manufacturing", "stem": "manufactur",
    "avg": [ 4.14, 5.66 ], "std": [ 1.98, 1.35 ], "fq": 50 
  },
  "members": {
    "dict": "happiness", "word": "members", "stem": "member",
    "avg": [ 5.54, 5.66 ], "std": [ 2.63, 1.22 ], "fq": 50 
  },
  "occupy": {
    "dict": "happiness", "word": "occupy", "stem": "occupi",
    "avg": [ 6.77, 5.66 ], "std": [ 2.07, 1.56 ], "fq": 50 
  },
  "passed": {
    "dict": "happiness", "word": "passed", "stem": "pass",
    "avg": [ 4.40, 5.66 ], "std": [ 2.07, 2.06 ], "fq": 50 
  },
  "practices": {
    "dict": "happiness", "word": "practices", "stem": "practic",
    "avg": [ 4.26, 5.66 ], "std": [ 2.47, 1.32 ], "fq": 50 
  },
  "prepare": {
    "dict": "happiness", "word": "prepare", "stem": "prepar",
    "avg": [ 3.82, 5.66 ], "std": [ 2.40, 1.48 ], "fq": 50 
  },
  "regard": {
    "dict": "happiness", "word": "regard", "stem": "regard",
    "avg": [ 5.16, 5.66 ], "std": [ 2.62, 1.02 ], "fq": 50 
  },
  "rode": {
    "dict": "happiness", "word": "rode", "stem": "rode",
    "avg": [ 5.87, 5.66 ], "std": [ 2.56, 1.12 ], "fq": 50 
  },
  "roll": {
    "dict": "happiness", "word": "roll", "stem": "roll",
    "avg": [ 3.47, 5.66 ], "std": [ 2.12, 1.06 ], "fq": 50 
  },
  "rugged": {
    "dict": "happiness", "word": "rugged", "stem": "rug",
    "avg": [ 5.43, 5.66 ], "std": [ 2.42, 1.67 ], "fq": 50 
  },
  "sake": {
    "dict": "happiness", "word": "sake", "stem": "sake",
    "avg": [ 5.66, 5.66 ], "std": [ 2.26, 1.47 ], "fq": 50 
  },
  "served": {
    "dict": "happiness", "word": "served", "stem": "serv",
    "avg": [ 5.41, 5.66 ], "std": [ 2.43, 1.24 ], "fq": 50 
  },
  "several": {
    "dict": "happiness", "word": "several", "stem": "sever",
    "avg": [ 5.26, 5.66 ], "std": [ 2.36, 0.92 ], "fq": 50 
  },
  "sign": {
    "dict": "happiness", "word": "sign", "stem": "sign",
    "avg": [ 4.56, 5.66 ], "std": [ 2.41, 1.29 ], "fq": 50 
  },
  "timing": {
    "dict": "happiness", "word": "timing", "stem": "time",
    "avg": [ 4.64, 5.66 ], "std": [ 2.75, 1.15 ], "fq": 50 
  },
  "tongues": {
    "dict": "happiness", "word": "tongues", "stem": "tongu",
    "avg": [ 5.80, 5.66 ], "std": [ 2.00, 1.35 ], "fq": 50 
  },
  "tower": {
    "dict": "happiness", "word": "tower", "stem": "tower",
    "avg": [ 3.95, 5.66 ], "std": [ 2.28, 1.41 ], "fq": 50 
  },
  "verse": {
    "dict": "happiness", "word": "verse", "stem": "vers",
    "avg": [ 4.00, 5.66 ], "std": [ 2.85, 1.36 ], "fq": 50 
  },
  "explains": {
    "dict": "happiness", "word": "explains", "stem": "explain",
    "avg": [ 4.48, 5.66 ], "std": [ 2.29, 1.52 ], "fq": 50 
  },
  "doorway": {
    "dict": "happiness", "word": "doorway", "stem": "doorway",
    "avg": [ 3.80, 5.65 ], "std": [ 2.29, 1.15 ], "fq": 50 
  },
  "height": {
    "dict": "happiness", "word": "height", "stem": "height",
    "avg": [ 4.16, 5.65 ], "std": [ 1.99, 1.41 ], "fq": 50 
  },
  "influenced": {
    "dict": "happiness", "word": "influenced", "stem": "influenc",
    "avg": [ 5.16, 5.65 ], "std": [ 2.25, 1.47 ], "fq": 50 
  },
  "phases": {
    "dict": "happiness", "word": "phases", "stem": "phase",
    "avg": [ 3.98, 5.65 ], "std": [ 1.82, 1.09 ], "fq": 50 
  },
  "consisting": {
    "dict": "happiness", "word": "consisting", "stem": "consist",
    "avg": [ 5.96, 5.65 ], "std": [ 2.63, 1.18 ], "fq": 50 
  },
  "asterisk": {
    "dict": "happiness", "word": "asterisk", "stem": "asterisk",
    "avg": [ 5.83, 5.64 ], "std": [ 2.44, 1.21 ], "fq": 50 
  },
  "closely": {
    "dict": "happiness", "word": "closely", "stem": "close",
    "avg": [ 6.98, 5.64 ], "std": [ 2.21, 1.52 ], "fq": 50 
  },
  "commons": {
    "dict": "happiness", "word": "commons", "stem": "common",
    "avg": [ 4.28, 5.64 ], "std": [ 2.46, 1.35 ], "fq": 50 
  },
  "competition": {
    "dict": "happiness", "word": "competition", "stem": "competit",
    "avg": [ 4.32, 5.64 ], "std": [ 2.14, 1.70 ], "fq": 50 
  },
  "construction": {
    "dict": "happiness", "word": "construction", "stem": "construct",
    "avg": [ 3.92, 5.64 ], "std": [ 1.94, 1.54 ], "fq": 50 
  },
  "entitled": {
    "dict": "happiness", "word": "entitled", "stem": "entitl",
    "avg": [ 3.21, 5.64 ], "std": [ 2.57, 1.51 ], "fq": 50 
  },
  "guess": {
    "dict": "happiness", "word": "guess", "stem": "guess",
    "avg": [ 5.98, 5.64 ], "std": [ 2.14, 1.08 ], "fq": 50 
  },
  "handful": {
    "dict": "happiness", "word": "handful", "stem": "hand",
    "avg": [ 4.40, 5.64 ], "std": [ 2.07, 1.26 ], "fq": 50 
  },
  "heads": {
    "dict": "happiness", "word": "heads", "stem": "head",
    "avg": [ 5.00, 5.64 ], "std": [ 2.68, 1.05 ], "fq": 50 
  },
  "heights": {
    "dict": "happiness", "word": "heights", "stem": "height",
    "avg": [ 4.16, 5.64 ], "std": [ 1.99, 1.64 ], "fq": 50 
  },
  "holding": {
    "dict": "happiness", "word": "holding", "stem": "hold",
    "avg": [ 6.10, 5.64 ], "std": [ 2.19, 1.12 ], "fq": 50 
  },
  "influence": {
    "dict": "happiness", "word": "influence", "stem": "influenc",
    "avg": [ 5.16, 5.64 ], "std": [ 2.25, 1.24 ], "fq": 50 
  },
  "involvement": {
    "dict": "happiness", "word": "involvement", "stem": "involv",
    "avg": [ 6.77, 5.64 ], "std": [ 2.07, 1.37 ], "fq": 50 
  },
  "layer": {
    "dict": "happiness", "word": "layer", "stem": "layer",
    "avg": [ 3.61, 5.64 ], "std": [ 2.56, 1.16 ], "fq": 50 
  },
  "lit": {
    "dict": "happiness", "word": "lit", "stem": "lit",
    "avg": [ 4.70, 5.64 ], "std": [ 2.48, 1.31 ], "fq": 50 
  },
  "portions": {
    "dict": "happiness", "word": "portions", "stem": "portion",
    "avg": [ 3.82, 5.64 ], "std": [ 2.24, 1.26 ], "fq": 50 
  },
  "presidents": {
    "dict": "happiness", "word": "presidents", "stem": "presid",
    "avg": [ 3.15, 5.64 ], "std": [ 1.77, 1.57 ], "fq": 50 
  },
  "purposes": {
    "dict": "happiness", "word": "purposes", "stem": "purpos",
    "avg": [ 4.26, 5.64 ], "std": [ 2.47, 1.45 ], "fq": 50 
  },
  "serving": {
    "dict": "happiness", "word": "serving", "stem": "serv",
    "avg": [ 5.41, 5.64 ], "std": [ 2.43, 1.35 ], "fq": 50 
  },
  "sheets": {
    "dict": "happiness", "word": "sheets", "stem": "sheet",
    "avg": [ 6.14, 5.64 ], "std": [ 2.39, 1.06 ], "fq": 50 
  },
  "streets": {
    "dict": "happiness", "word": "streets", "stem": "street",
    "avg": [ 3.39, 5.64 ], "std": [ 1.87, 1.24 ], "fq": 50 
  },
  "trend": {
    "dict": "happiness", "word": "trend", "stem": "trend",
    "avg": [ 5.00, 5.64 ], "std": [ 2.32, 1.17 ], "fq": 50 
  },
  "use": {
    "dict": "happiness", "word": "use", "stem": "use",
    "avg": [ 4.26, 5.64 ], "std": [ 2.47, 1.16 ], "fq": 50 
  },
  "venture": {
    "dict": "happiness", "word": "venture", "stem": "ventur",
    "avg": [ 6.98, 5.64 ], "std": [ 2.15, 1.32 ], "fq": 50 
  },
  "wrote": {
    "dict": "happiness", "word": "wrote", "stem": "wrote",
    "avg": [ 4.95, 5.64 ], "std": [ 2.19, 1.34 ], "fq": 50 
  },
  "spaces": {
    "dict": "happiness", "word": "spaces", "stem": "space",
    "avg": [ 5.14, 5.62 ], "std": [ 2.54, 1.02 ], "fq": 50 
  },
  "accent": {
    "dict": "happiness", "word": "accent", "stem": "accent",
    "avg": [ 7.45, 5.62 ], "std": [ 2.38, 1.03 ], "fq": 50 
  },
  "appeal": {
    "dict": "happiness", "word": "appeal", "stem": "appeal",
    "avg": [ 5.16, 5.62 ], "std": [ 2.25, 1.51 ], "fq": 50 
  },
  "bottle": {
    "dict": "happiness", "word": "bottle", "stem": "bottl",
    "avg": [ 4.79, 5.62 ], "std": [ 2.44, 1.34 ], "fq": 50 
  },
  "buildings": {
    "dict": "happiness", "word": "buildings", "stem": "build",
    "avg": [ 3.92, 5.62 ], "std": [ 1.94, 1.40 ], "fq": 50 
  },
  "catching": {
    "dict": "happiness", "word": "catching", "stem": "catch",
    "avg": [ 5.83, 5.62 ], "std": [ 2.73, 1.23 ], "fq": 50 
  },
  "clock": {
    "dict": "happiness", "word": "clock", "stem": "clock",
    "avg": [ 4.02, 5.62 ], "std": [ 2.54, 0.99 ], "fq": 50 
  },
  "cloud": {
    "dict": "happiness", "word": "cloud", "stem": "cloud",
    "avg": [ 3.30, 5.62 ], "std": [ 2.08, 1.85 ], "fq": 50 
  },
  "comments": {
    "dict": "happiness", "word": "comments", "stem": "comment",
    "avg": [ 5.74, 5.62 ], "std": [ 2.38, 1.05 ], "fq": 50 
  },
  "describing": {
    "dict": "happiness", "word": "describing", "stem": "describ",
    "avg": [ 3.70, 5.62 ], "std": [ 2.18, 1.32 ], "fq": 50 
  },
  "display": {
    "dict": "happiness", "word": "display", "stem": "display",
    "avg": [ 5.12, 5.62 ], "std": [ 2.39, 0.92 ], "fq": 50 
  },
  "fry": {
    "dict": "happiness", "word": "fry", "stem": "fri",
    "avg": [ 5.55, 5.62 ], "std": [ 2.29, 1.83 ], "fq": 50 
  },
  "leaves": {
    "dict": "happiness", "word": "leaves", "stem": "leav",
    "avg": [ 3.82, 5.62 ], "std": [ 2.24, 1.79 ], "fq": 50 
  },
  "material": {
    "dict": "happiness", "word": "material", "stem": "materi",
    "avg": [ 4.05, 5.62 ], "std": [ 2.34, 0.92 ], "fq": 50 
  },
  "pitch": {
    "dict": "happiness", "word": "pitch", "stem": "pitch",
    "avg": [ 4.27, 5.62 ], "std": [ 2.17, 1.35 ], "fq": 50 
  },
  "poll": {
    "dict": "happiness", "word": "poll", "stem": "poll",
    "avg": [ 4.28, 5.62 ], "std": [ 2.53, 1.34 ], "fq": 50 
  },
  "referred": {
    "dict": "happiness", "word": "referred", "stem": "refer",
    "avg": [ 4.25, 5.62 ], "std": [ 2.47, 0.99 ], "fq": 50 
  },
  "reply": {
    "dict": "happiness", "word": "reply", "stem": "repli",
    "avg": [ 5.41, 5.62 ], "std": [ 2.43, 1.32 ], "fq": 50 
  },
  "runs": {
    "dict": "happiness", "word": "runs", "stem": "run",
    "avg": [ 5.71, 5.62 ], "std": [ 2.74, 1.28 ], "fq": 50 
  },
  "sells": {
    "dict": "happiness", "word": "sells", "stem": "sell",
    "avg": [ 7.24, 5.62 ], "std": [ 2.06, 1.32 ], "fq": 50 
  },
  "snowed": {
    "dict": "happiness", "word": "snowed", "stem": "snow",
    "avg": [ 5.75, 5.62 ], "std": [ 2.47, 2.03 ], "fq": 50 
  },
  "status": {
    "dict": "happiness", "word": "status", "stem": "statu",
    "avg": [ 3.46, 5.62 ], "std": [ 1.72, 1.18 ], "fq": 50 
  },
  "tub": {
    "dict": "happiness", "word": "tub", "stem": "tub",
    "avg": [ 4.36, 5.62 ], "std": [ 2.59, 1.64 ], "fq": 50 
  },
  "watches": {
    "dict": "happiness", "word": "watches", "stem": "watch",
    "avg": [ 4.10, 5.62 ], "std": [ 2.12, 1.51 ], "fq": 50 
  },
  "address": {
    "dict": "happiness", "word": "address", "stem": "address",
    "avg": [ 5.62, 5.60 ], "std": [ 2.25, 1.05 ], "fq": 50 
  },
  "apparent": {
    "dict": "happiness", "word": "apparent", "stem": "appar",
    "avg": [ 3.50, 5.60 ], "std": [ 1.84, 1.07 ], "fq": 50 
  },
  "arranged": {
    "dict": "happiness", "word": "arranged", "stem": "arrang",
    "avg": [ 4.05, 5.60 ], "std": [ 1.89, 1.34 ], "fq": 50 
  },
  "assembly": {
    "dict": "happiness", "word": "assembly", "stem": "assembl",
    "avg": [ 4.14, 5.60 ], "std": [ 1.98, 1.09 ], "fq": 50 
  },
  "bathroom": {
    "dict": "happiness", "word": "bathroom", "stem": "bathroom",
    "avg": [ 3.88, 5.60 ], "std": [ 1.72, 1.32 ], "fq": 50 
  },
  "bees": {
    "dict": "happiness", "word": "bees", "stem": "bee",
    "avg": [ 6.51, 5.60 ], "std": [ 2.14, 2.14 ], "fq": 50 
  },
  "called": {
    "dict": "happiness", "word": "called", "stem": "call",
    "avg": [ 4.25, 5.60 ], "std": [ 2.47, 1.11 ], "fq": 50 
  },
  "centers": {
    "dict": "happiness", "word": "centers", "stem": "center",
    "avg": [ 6.34, 5.60 ], "std": [ 2.25, 0.90 ], "fq": 50 
  },
  "central": {
    "dict": "happiness", "word": "central", "stem": "central",
    "avg": [ 3.70, 5.60 ], "std": [ 2.18, 0.88 ], "fq": 50 
  },
  "columns": {
    "dict": "happiness", "word": "columns", "stem": "column",
    "avg": [ 3.62, 5.60 ], "std": [ 1.91, 1.20 ], "fq": 50 
  },
  "combined": {
    "dict": "happiness", "word": "combined", "stem": "combin",
    "avg": [ 3.75, 5.60 ], "std": [ 2.49, 1.11 ], "fq": 50 
  },
  "covers": {
    "dict": "happiness", "word": "covers", "stem": "cover",
    "avg": [ 5.28, 5.60 ], "std": [ 2.51, 0.99 ], "fq": 50 
  },
  "entirely": {
    "dict": "happiness", "word": "entirely", "stem": "entir",
    "avg": [ 4.83, 5.60 ], "std": [ 2.66, 1.14 ], "fq": 50 
  },
  "function": {
    "dict": "happiness", "word": "function", "stem": "function",
    "avg": [ 4.26, 5.60 ], "std": [ 2.47, 1.46 ], "fq": 50 
  },
  "got": {
    "dict": "happiness", "word": "got", "stem": "got",
    "avg": [ 5.92, 5.60 ], "std": [ 2.60, 1.46 ], "fq": 50 
  },
  "idol": {
    "dict": "happiness", "word": "idol", "stem": "idol",
    "avg": [ 4.95, 5.60 ], "std": [ 2.14, 1.47 ], "fq": 50 
  },
  "immediate": {
    "dict": "happiness", "word": "immediate", "stem": "immedi",
    "avg": [ 6.57, 5.60 ], "std": [ 1.78, 1.67 ], "fq": 50 
  },
  "involving": {
    "dict": "happiness", "word": "involving", "stem": "involv",
    "avg": [ 6.21, 5.60 ], "std": [ 2.75, 1.34 ], "fq": 50 
  },
  "layers": {
    "dict": "happiness", "word": "layers", "stem": "layer",
    "avg": [ 3.61, 5.60 ], "std": [ 2.56, 1.31 ], "fq": 50 
  },
  "level": {
    "dict": "happiness", "word": "level", "stem": "level",
    "avg": [ 6.14, 5.60 ], "std": [ 2.39, 0.99 ], "fq": 50 
  },
  "links": {
    "dict": "happiness", "word": "links", "stem": "link",
    "avg": [ 3.75, 5.60 ], "std": [ 2.49, 1.16 ], "fq": 50 
  },
  "news": {
    "dict": "happiness", "word": "news", "stem": "news",
    "avg": [ 5.17, 5.60 ], "std": [ 2.11, 1.55 ], "fq": 50 
  },
  "outcome": {
    "dict": "happiness", "word": "outcome", "stem": "outcom",
    "avg": [ 5.10, 5.60 ], "std": [ 2.40, 1.14 ], "fq": 50 
  },
  "patent": {
    "dict": "happiness", "word": "patent", "stem": "patent",
    "avg": [ 3.50, 5.60 ], "std": [ 1.84, 1.62 ], "fq": 50 
  },
  "pick": {
    "dict": "happiness", "word": "pick", "stem": "pick",
    "avg": [ 4.74, 5.60 ], "std": [ 2.23, 0.97 ], "fq": 50 
  },
  "priest": {
    "dict": "happiness", "word": "priest", "stem": "priest",
    "avg": [ 4.41, 5.60 ], "std": [ 2.71, 1.70 ], "fq": 50 
  },
  "reaching": {
    "dict": "happiness", "word": "reaching", "stem": "reach",
    "avg": [ 5.73, 5.60 ], "std": [ 2.09, 1.11 ], "fq": 50 
  },
  "runner": {
    "dict": "happiness", "word": "runner", "stem": "runner",
    "avg": [ 4.76, 5.60 ], "std": [ 2.40, 1.63 ], "fq": 50 
  },
  "spell": {
    "dict": "happiness", "word": "spell", "stem": "spell",
    "avg": [ 5.16, 5.60 ], "std": [ 2.25, 1.41 ], "fq": 50 
  },
  "stand": {
    "dict": "happiness", "word": "stand", "stem": "stand",
    "avg": [ 3.93, 5.60 ], "std": [ 2.49, 1.11 ], "fq": 50 
  },
  "suggested": {
    "dict": "happiness", "word": "suggested", "stem": "suggest",
    "avg": [ 6.98, 5.60 ], "std": [ 2.21, 1.25 ], "fq": 50 
  },
  "utilities": {
    "dict": "happiness", "word": "utilities", "stem": "util",
    "avg": [ 4.26, 5.60 ], "std": [ 2.47, 1.70 ], "fq": 50 
  },
  "viewed": {
    "dict": "happiness", "word": "viewed", "stem": "view",
    "avg": [ 4.10, 5.60 ], "std": [ 2.12, 1.21 ], "fq": 50 
  },
  "constituted": {
    "dict": "happiness", "word": "constituted", "stem": "constitut",
    "avg": [ 3.62, 5.59 ], "std": [ 2.25, 1.14 ], "fq": 50 
  },
  "sentences": {
    "dict": "happiness", "word": "sentences", "stem": "sentenc",
    "avg": [ 4.64, 5.59 ], "std": [ 2.75, 1.63 ], "fq": 50 
  },
  "habits": {
    "dict": "happiness", "word": "habits", "stem": "habit",
    "avg": [ 3.95, 5.58 ], "std": [ 2.11, 1.49 ], "fq": 50 
  },
  "appeals": {
    "dict": "happiness", "word": "appeals", "stem": "appeal",
    "avg": [ 5.16, 5.58 ], "std": [ 2.25, 1.73 ], "fq": 50 
  },
  "bears": {
    "dict": "happiness", "word": "bears", "stem": "bear",
    "avg": [ 5.40, 5.58 ], "std": [ 2.70, 1.82 ], "fq": 50 
  },
  "circle": {
    "dict": "happiness", "word": "circle", "stem": "circl",
    "avg": [ 3.86, 5.58 ], "std": [ 2.13, 1.21 ], "fq": 50 
  },
  "cities": {
    "dict": "happiness", "word": "cities", "stem": "citi",
    "avg": [ 5.24, 5.58 ], "std": [ 2.53, 1.50 ], "fq": 50 
  },
  "client": {
    "dict": "happiness", "word": "client", "stem": "client",
    "avg": [ 4.66, 5.58 ], "std": [ 2.12, 1.18 ], "fq": 50 
  },
  "comes": {
    "dict": "happiness", "word": "comes", "stem": "come",
    "avg": [ 4.70, 5.58 ], "std": [ 2.48, 0.76 ], "fq": 50 
  },
  "comment": {
    "dict": "happiness", "word": "comment", "stem": "comment",
    "avg": [ 5.74, 5.58 ], "std": [ 2.38, 1.28 ], "fq": 50 
  },
  "consists": {
    "dict": "happiness", "word": "consists", "stem": "consist",
    "avg": [ 5.96, 5.58 ], "std": [ 2.63, 1.36 ], "fq": 50 
  },
  "described": {
    "dict": "happiness", "word": "described", "stem": "describ",
    "avg": [ 3.70, 5.58 ], "std": [ 2.18, 1.14 ], "fq": 50 
  },
  "example": {
    "dict": "happiness", "word": "example", "stem": "exampl",
    "avg": [ 6.84, 5.58 ], "std": [ 2.06, 1.07 ], "fq": 50 
  },
  "executive": {
    "dict": "happiness", "word": "executive", "stem": "execut",
    "avg": [ 5.71, 5.58 ], "std": [ 2.74, 1.67 ], "fq": 50 
  },
  "feet": {
    "dict": "happiness", "word": "feet", "stem": "feet",
    "avg": [ 3.27, 5.58 ], "std": [ 1.98, 1.26 ], "fq": 50 
  },
  "filling": {
    "dict": "happiness", "word": "filling", "stem": "fill",
    "avg": [ 4.94, 5.58 ], "std": [ 2.63, 1.36 ], "fq": 50 
  },
  "fingers": {
    "dict": "happiness", "word": "fingers", "stem": "finger",
    "avg": [ 3.78, 5.58 ], "std": [ 2.42, 1.14 ], "fq": 50 
  },
  "formed": {
    "dict": "happiness", "word": "formed", "stem": "form",
    "avg": [ 5.67, 5.58 ], "std": [ 2.51, 1.16 ], "fq": 50 
  },
  "front": {
    "dict": "happiness", "word": "front", "stem": "front",
    "avg": [ 5.04, 5.58 ], "std": [ 2.18, 1.07 ], "fq": 50 
  },
  "identify": {
    "dict": "happiness", "word": "identify", "stem": "identifi",
    "avg": [ 4.25, 5.58 ], "std": [ 2.47, 1.36 ], "fq": 50 
  },
  "intro": {
    "dict": "happiness", "word": "intro", "stem": "intro",
    "avg": [ 5.12, 5.58 ], "std": [ 2.39, 0.95 ], "fq": 50 
  },
  "lay": {
    "dict": "happiness", "word": "lay", "stem": "lay",
    "avg": [ 5.96, 5.58 ], "std": [ 2.63, 1.28 ], "fq": 50 
  },
  "looked": {
    "dict": "happiness", "word": "looked", "stem": "look",
    "avg": [ 5.04, 5.58 ], "std": [ 2.18, 1.36 ], "fq": 50 
  },
  "lords": {
    "dict": "happiness", "word": "lords", "stem": "lord",
    "avg": [ 5.20, 5.58 ], "std": [ 2.85, 2.14 ], "fq": 50 
  },
  "named": {
    "dict": "happiness", "word": "named", "stem": "name",
    "avg": [ 4.25, 5.58 ], "std": [ 2.47, 0.86 ], "fq": 50 
  },
  "pot": {
    "dict": "happiness", "word": "pot", "stem": "pot",
    "avg": [ 4.00, 5.58 ], "std": [ 2.14, 1.53 ], "fq": 50 
  },
  "pursuit": {
    "dict": "happiness", "word": "pursuit", "stem": "pursuit",
    "avg": [ 5.66, 5.58 ], "std": [ 2.26, 1.79 ], "fq": 50 
  },
  "recorded": {
    "dict": "happiness", "word": "recorded", "stem": "record",
    "avg": [ 5.42, 5.58 ], "std": [ 2.25, 1.20 ], "fq": 50 
  },
  "returning": {
    "dict": "happiness", "word": "returning", "stem": "return",
    "avg": [ 4.70, 5.58 ], "std": [ 2.48, 1.47 ], "fq": 50 
  },
  "rooms": {
    "dict": "happiness", "word": "rooms", "stem": "room",
    "avg": [ 3.36, 5.58 ], "std": [ 2.12, 0.91 ], "fq": 50 
  },
  "seats": {
    "dict": "happiness", "word": "seats", "stem": "seat",
    "avg": [ 2.95, 5.58 ], "std": [ 1.72, 1.34 ], "fq": 50 
  },
  "set": {
    "dict": "happiness", "word": "set", "stem": "set",
    "avg": [ 4.05, 5.58 ], "std": [ 1.89, 1.20 ], "fq": 50 
  },
  "shortly": {
    "dict": "happiness", "word": "shortly", "stem": "shortli",
    "avg": [ 5.12, 5.58 ], "std": [ 2.39, 1.31 ], "fq": 50 
  },
  "solely": {
    "dict": "happiness", "word": "solely", "stem": "sole",
    "avg": [ 4.83, 5.58 ], "std": [ 2.66, 1.34 ], "fq": 50 
  },
  "stuff": {
    "dict": "happiness", "word": "stuff", "stem": "stuff",
    "avg": [ 4.05, 5.58 ], "std": [ 2.34, 1.50 ], "fq": 50 
  },
  "times": {
    "dict": "happiness", "word": "times", "stem": "time",
    "avg": [ 4.64, 5.58 ], "std": [ 2.75, 1.20 ], "fq": 50 
  },
  "trending": {
    "dict": "happiness", "word": "trending", "stem": "trend",
    "avg": [ 5.00, 5.58 ], "std": [ 2.32, 1.44 ], "fq": 50 
  },
  "tries": {
    "dict": "happiness", "word": "tries", "stem": "tri",
    "avg": [ 7.45, 5.58 ], "std": [ 2.38, 1.26 ], "fq": 50 
  },
  "density": {
    "dict": "happiness", "word": "density", "stem": "densiti",
    "avg": [ 4.65, 5.57 ], "std": [ 2.13, 1.20 ], "fq": 50 
  },
  "component": {
    "dict": "happiness", "word": "component", "stem": "compon",
    "avg": [ 3.82, 5.56 ], "std": [ 2.24, 1.11 ], "fq": 50 
  },
  "illusion": {
    "dict": "happiness", "word": "illusion", "stem": "illus",
    "avg": [ 5.14, 5.56 ], "std": [ 2.82, 1.50 ], "fq": 50 
  },
  "aspects": {
    "dict": "happiness", "word": "aspects", "stem": "aspect",
    "avg": [ 5.04, 5.56 ], "std": [ 2.18, 1.40 ], "fq": 50 
  },
  "cap": {
    "dict": "happiness", "word": "cap", "stem": "cap",
    "avg": [ 4.28, 5.56 ], "std": [ 2.53, 0.93 ], "fq": 50 
  },
  "civil": {
    "dict": "happiness", "word": "civil", "stem": "civil",
    "avg": [ 3.74, 5.56 ], "std": [ 2.37, 1.15 ], "fq": 50 
  },
  "clients": {
    "dict": "happiness", "word": "clients", "stem": "client",
    "avg": [ 4.66, 5.56 ], "std": [ 2.12, 1.20 ], "fq": 50 
  },
  "contents": {
    "dict": "happiness", "word": "contents", "stem": "content",
    "avg": [ 4.32, 5.56 ], "std": [ 2.14, 0.95 ], "fq": 50 
  },
  "forming": {
    "dict": "happiness", "word": "forming", "stem": "form",
    "avg": [ 5.67, 5.56 ], "std": [ 2.51, 0.99 ], "fq": 50 
  },
  "ink": {
    "dict": "happiness", "word": "ink", "stem": "ink",
    "avg": [ 3.84, 5.56 ], "std": [ 1.88, 1.28 ], "fq": 50 
  },
  "jumped": {
    "dict": "happiness", "word": "jumped", "stem": "jump",
    "avg": [ 5.67, 5.56 ], "std": [ 2.51, 1.34 ], "fq": 50 
  },
  "makes": {
    "dict": "happiness", "word": "makes", "stem": "make",
    "avg": [ 4.20, 5.56 ], "std": [ 2.18, 1.25 ], "fq": 50 
  },
  "matches": {
    "dict": "happiness", "word": "matches", "stem": "match",
    "avg": [ 6.39, 5.56 ], "std": [ 2.31, 1.21 ], "fq": 50 
  },
  "method": {
    "dict": "happiness", "word": "method", "stem": "method",
    "avg": [ 3.85, 5.56 ], "std": [ 2.58, 0.91 ], "fq": 50 
  },
  "pan": {
    "dict": "happiness", "word": "pan", "stem": "pan",
    "avg": [ 4.16, 5.56 ], "std": [ 2.16, 0.84 ], "fq": 50 
  },
  "passage": {
    "dict": "happiness", "word": "passage", "stem": "passag",
    "avg": [ 4.36, 5.56 ], "std": [ 2.13, 1.15 ], "fq": 50 
  },
  "place": {
    "dict": "happiness", "word": "place", "stem": "place",
    "avg": [ 2.95, 5.56 ], "std": [ 1.72, 1.20 ], "fq": 50 
  },
  "range": {
    "dict": "happiness", "word": "range", "stem": "rang",
    "avg": [ 4.51, 5.56 ], "std": [ 2.14, 1.01 ], "fq": 50 
  },
  "red": {
    "dict": "happiness", "word": "red", "stem": "red",
    "avg": [ 5.29, 5.56 ], "std": [ 2.04, 1.62 ], "fq": 50 
  },
  "regarding": {
    "dict": "happiness", "word": "regarding", "stem": "regard",
    "avg": [ 6.21, 5.56 ], "std": [ 2.75, 1.13 ], "fq": 50 
  },
  "rolls": {
    "dict": "happiness", "word": "rolls", "stem": "roll",
    "avg": [ 3.47, 5.56 ], "std": [ 2.12, 1.31 ], "fq": 50 
  },
  "solo": {
    "dict": "happiness", "word": "solo", "stem": "solo",
    "avg": [ 4.83, 5.56 ], "std": [ 2.66, 1.37 ], "fq": 50 
  },
  "stay": {
    "dict": "happiness", "word": "stay", "stem": "stay",
    "avg": [ 5.62, 5.56 ], "std": [ 2.39, 1.16 ], "fq": 50 
  },
  "stepping": {
    "dict": "happiness", "word": "stepping", "stem": "step",
    "avg": [ 6.83, 5.56 ], "std": [ 2.70, 0.99 ], "fq": 50 
  },
  "studying": {
    "dict": "happiness", "word": "studying", "stem": "studi",
    "avg": [ 5.39, 5.56 ], "std": [ 2.22, 2.00 ], "fq": 50 
  },
  "substance": {
    "dict": "happiness", "word": "substance", "stem": "substanc",
    "avg": [ 6.34, 5.56 ], "std": [ 2.25, 1.11 ], "fq": 50 
  },
  "treated": {
    "dict": "happiness", "word": "treated", "stem": "treat",
    "avg": [ 5.62, 5.56 ], "std": [ 2.25, 1.64 ], "fq": 50 
  },
  "voices": {
    "dict": "happiness", "word": "voices", "stem": "voic",
    "avg": [ 3.82, 5.56 ], "std": [ 2.24, 1.50 ], "fq": 50 
  },
  "woke": {
    "dict": "happiness", "word": "woke", "stem": "woke",
    "avg": [ 6.63, 5.56 ], "std": [ 2.70, 1.42 ], "fq": 50 
  },
  "word": {
    "dict": "happiness", "word": "word", "stem": "word",
    "avg": [ 5.17, 5.56 ], "std": [ 2.11, 1.15 ], "fq": 50 
  },
  "working": {
    "dict": "happiness", "word": "working", "stem": "work",
    "avg": [ 4.07, 5.56 ], "std": [ 1.98, 1.76 ], "fq": 50 
  },
  "calculations": {
    "dict": "happiness", "word": "calculations", "stem": "calcul",
    "avg": [ 4.75, 5.55 ], "std": [ 1.93, 1.60 ], "fq": 50 
  },
  "tame": {
    "dict": "happiness", "word": "tame", "stem": "tame",
    "avg": [ 3.80, 5.55 ], "std": [ 2.13, 1.42 ], "fq": 50 
  },
  "acquisitions": {
    "dict": "happiness", "word": "acquisitions", "stem": "acquisit",
    "avg": [ 5.39, 5.54 ], "std": [ 2.22, 1.72 ], "fq": 50 
  },
  "adam": {
    "dict": "happiness", "word": "adam", "stem": "adam",
    "avg": [ 7.38, 5.54 ], "std": [ 1.92, 1.27 ], "fq": 50 
  },
  "apparently": {
    "dict": "happiness", "word": "apparently", "stem": "appar",
    "avg": [ 3.52, 5.54 ], "std": [ 2.05, 1.11 ], "fq": 50 
  },
  "box": {
    "dict": "happiness", "word": "box", "stem": "box",
    "avg": [ 3.91, 5.54 ], "std": [ 1.92, 0.89 ], "fq": 50 
  },
  "cardinal": {
    "dict": "happiness", "word": "cardinal", "stem": "cardin",
    "avg": [ 3.70, 5.54 ], "std": [ 2.18, 1.61 ], "fq": 50 
  },
  "chest": {
    "dict": "happiness", "word": "chest", "stem": "chest",
    "avg": [ 5.37, 5.54 ], "std": [ 2.39, 0.97 ], "fq": 50 
  },
  "dame": {
    "dict": "happiness", "word": "dame", "stem": "dame",
    "avg": [ 4.24, 5.54 ], "std": [ 2.43, 1.37 ], "fq": 50 
  },
  "dealing": {
    "dict": "happiness", "word": "dealing", "stem": "deal",
    "avg": [ 5.62, 5.54 ], "std": [ 2.25, 1.16 ], "fq": 50 
  },
  "doctors": {
    "dict": "happiness", "word": "doctors", "stem": "doctor",
    "avg": [ 5.86, 5.54 ], "std": [ 2.70, 1.66 ], "fq": 50 
  },
  "domain": {
    "dict": "happiness", "word": "domain", "stem": "domain",
    "avg": [ 3.88, 5.54 ], "std": [ 1.99, 1.11 ], "fq": 50 
  },
  "firmly": {
    "dict": "happiness", "word": "firmly", "stem": "firmli",
    "avg": [ 3.14, 5.54 ], "std": [ 2.47, 1.23 ], "fq": 50 
  },
  "frame": {
    "dict": "happiness", "word": "frame", "stem": "frame",
    "avg": [ 3.92, 5.54 ], "std": [ 1.94, 1.54 ], "fq": 50 
  },
  "go": {
    "dict": "happiness", "word": "go", "stem": "go",
    "avg": [ 7.38, 5.54 ], "std": [ 1.92, 1.18 ], "fq": 50 
  },
  "handle": {
    "dict": "happiness", "word": "handle", "stem": "handl",
    "avg": [ 5.62, 5.54 ], "std": [ 2.25, 1.05 ], "fq": 50 
  },
  "holdings": {
    "dict": "happiness", "word": "holdings", "stem": "hold",
    "avg": [ 6.10, 5.54 ], "std": [ 2.19, 1.40 ], "fq": 50 
  },
  "lap": {
    "dict": "happiness", "word": "lap", "stem": "lap",
    "avg": [ 3.86, 5.54 ], "std": [ 2.13, 1.28 ], "fq": 50 
  },
  "look": {
    "dict": "happiness", "word": "look", "stem": "look",
    "avg": [ 5.56, 5.54 ], "std": [ 2.62, 1.13 ], "fq": 50 
  },
  "materials": {
    "dict": "happiness", "word": "materials", "stem": "materi",
    "avg": [ 4.05, 5.54 ], "std": [ 2.34, 1.07 ], "fq": 50 
  },
  "mount": {
    "dict": "happiness", "word": "mount", "stem": "mount",
    "avg": [ 5.49, 5.54 ], "std": [ 2.43, 1.27 ], "fq": 50 
  },
  "mysterious": {
    "dict": "happiness", "word": "mysterious", "stem": "mysteri",
    "avg": [ 4.84, 5.54 ], "std": [ 2.57, 1.67 ], "fq": 50 
  },
  "obviously": {
    "dict": "happiness", "word": "obviously", "stem": "obvious",
    "avg": [ 3.52, 5.54 ], "std": [ 2.05, 1.27 ], "fq": 50 
  },
  "panel": {
    "dict": "happiness", "word": "panel", "stem": "panel",
    "avg": [ 3.36, 5.54 ], "std": [ 2.12, 1.28 ], "fq": 50 
  },
  "particular": {
    "dict": "happiness", "word": "particular", "stem": "particular",
    "avg": [ 4.10, 5.54 ], "std": [ 2.24, 1.13 ], "fq": 50 
  },
  "person": {
    "dict": "happiness", "word": "person", "stem": "person",
    "avg": [ 4.19, 5.54 ], "std": [ 2.45, 1.15 ], "fq": 50 
  },
  "posted": {
    "dict": "happiness", "word": "posted", "stem": "post",
    "avg": [ 5.63, 5.54 ], "std": [ 2.36, 1.13 ], "fq": 50 
  },
  "prompted": {
    "dict": "happiness", "word": "prompted", "stem": "prompt",
    "avg": [ 6.02, 5.54 ], "std": [ 2.67, 1.03 ], "fq": 50 
  },
  "rating": {
    "dict": "happiness", "word": "rating", "stem": "rate",
    "avg": [ 7.24, 5.54 ], "std": [ 2.06, 1.09 ], "fq": 50 
  },
  "reason": {
    "dict": "happiness", "word": "reason", "stem": "reason",
    "avg": [ 4.75, 5.54 ], "std": [ 2.50, 1.47 ], "fq": 50 
  },
  "regions": {
    "dict": "happiness", "word": "regions", "stem": "region",
    "avg": [ 3.82, 5.54 ], "std": [ 2.24, 1.11 ], "fq": 50 
  },
  "round": {
    "dict": "happiness", "word": "round", "stem": "round",
    "avg": [ 3.86, 5.54 ], "std": [ 2.13, 0.95 ], "fq": 50 
  },
  "signs": {
    "dict": "happiness", "word": "signs", "stem": "sign",
    "avg": [ 4.56, 5.54 ], "std": [ 2.41, 0.86 ], "fq": 50 
  },
  "sources": {
    "dict": "happiness", "word": "sources", "stem": "sourc",
    "avg": [ 4.49, 5.54 ], "std": [ 2.24, 1.23 ], "fq": 50 
  },
  "suggesting": {
    "dict": "happiness", "word": "suggesting", "stem": "suggest",
    "avg": [ 6.98, 5.54 ], "std": [ 2.21, 1.20 ], "fq": 50 
  },
  "tools": {
    "dict": "happiness", "word": "tools", "stem": "tool",
    "avg": [ 4.33, 5.54 ], "std": [ 1.78, 1.42 ], "fq": 50 
  },
  "abstract": {
    "dict": "happiness", "word": "abstract", "stem": "abstract",
    "avg": [ 4.59, 5.53 ], "std": [ 2.10, 1.44 ], "fq": 50 
  },
  "pipe": {
    "dict": "happiness", "word": "pipe", "stem": "pipe",
    "avg": [ 5.36, 5.53 ], "std": [ 2.91, 1.39 ], "fq": 50 
  },
  "rely": {
    "dict": "happiness", "word": "rely", "stem": "reli",
    "avg": [ 5.30, 5.53 ], "std": [ 2.66, 1.46 ], "fq": 50 
  },
  "sheet": {
    "dict": "happiness", "word": "sheet", "stem": "sheet",
    "avg": [ 6.14, 5.53 ], "std": [ 2.39, 1.23 ], "fq": 50 
  },
  "sole": {
    "dict": "happiness", "word": "sole", "stem": "sole",
    "avg": [ 4.51, 5.53 ], "std": [ 2.68, 1.29 ], "fq": 50 
  },
  "blazing": {
    "dict": "happiness", "word": "blazing", "stem": "blaze",
    "avg": [ 4.39, 5.52 ], "std": [ 2.36, 2.06 ], "fq": 50 
  },
  "appointment": {
    "dict": "happiness", "word": "appointment", "stem": "appoint",
    "avg": [ 6.77, 5.52 ], "std": [ 2.07, 1.84 ], "fq": 50 
  },
  "bottles": {
    "dict": "happiness", "word": "bottles", "stem": "bottl",
    "avg": [ 4.79, 5.52 ], "std": [ 2.44, 1.09 ], "fq": 50 
  },
  "boxes": {
    "dict": "happiness", "word": "boxes", "stem": "box",
    "avg": [ 3.91, 5.52 ], "std": [ 1.92, 1.22 ], "fq": 50 
  },
  "branch": {
    "dict": "happiness", "word": "branch", "stem": "branch",
    "avg": [ 3.96, 5.52 ], "std": [ 1.94, 1.15 ], "fq": 50 
  },
  "categories": {
    "dict": "happiness", "word": "categories", "stem": "categori",
    "avg": [ 4.80, 5.52 ], "std": [ 2.71, 1.23 ], "fq": 50 
  },
  "class": {
    "dict": "happiness", "word": "class", "stem": "class",
    "avg": [ 4.80, 5.52 ], "std": [ 2.71, 1.78 ], "fq": 50 
  },
  "demonstrate": {
    "dict": "happiness", "word": "demonstrate", "stem": "demonstr",
    "avg": [ 5.12, 5.52 ], "std": [ 2.39, 1.18 ], "fq": 50 
  },
  "employers": {
    "dict": "happiness", "word": "employers", "stem": "employ",
    "avg": [ 5.28, 5.52 ], "std": [ 2.12, 1.37 ], "fq": 50 
  },
  "filled": {
    "dict": "happiness", "word": "filled", "stem": "fill",
    "avg": [ 4.94, 5.52 ], "std": [ 2.63, 1.27 ], "fq": 50 
  },
  "findings": {
    "dict": "happiness", "word": "findings", "stem": "find",
    "avg": [ 5.42, 5.52 ], "std": [ 2.44, 1.47 ], "fq": 50 
  },
  "jets": {
    "dict": "happiness", "word": "jets", "stem": "jet",
    "avg": [ 4.28, 5.52 ], "std": [ 2.46, 1.36 ], "fq": 50 
  },
  "josh": {
    "dict": "happiness", "word": "josh", "stem": "josh",
    "avg": [ 5.57, 5.52 ], "std": [ 2.80, 1.37 ], "fq": 50 
  },
  "journalism": {
    "dict": "happiness", "word": "journalism", "stem": "journal",
    "avg": [ 4.05, 5.52 ], "std": [ 1.96, 1.62 ], "fq": 50 
  },
  "plains": {
    "dict": "happiness", "word": "plains", "stem": "plain",
    "avg": [ 3.52, 5.52 ], "std": [ 2.05, 1.43 ], "fq": 50 
  },
  "positions": {
    "dict": "happiness", "word": "positions", "stem": "posit",
    "avg": [ 3.46, 5.52 ], "std": [ 1.72, 1.28 ], "fq": 50 
  },
  "posting": {
    "dict": "happiness", "word": "posting", "stem": "post",
    "avg": [ 3.93, 5.52 ], "std": [ 2.56, 1.09 ], "fq": 50 
  },
  "ray": {
    "dict": "happiness", "word": "ray", "stem": "ray",
    "avg": [ 4.02, 5.52 ], "std": [ 1.94, 1.46 ], "fq": 50 
  },
  "reserves": {
    "dict": "happiness", "word": "reserves", "stem": "reserv",
    "avg": [ 3.27, 5.52 ], "std": [ 2.05, 1.28 ], "fq": 50 
  },
  "room": {
    "dict": "happiness", "word": "room", "stem": "room",
    "avg": [ 3.36, 5.52 ], "std": [ 2.12, 1.15 ], "fq": 50 
  },
  "suggest": {
    "dict": "happiness", "word": "suggest", "stem": "suggest",
    "avg": [ 6.98, 5.52 ], "std": [ 2.21, 1.23 ], "fq": 50 
  },
  "summit": {
    "dict": "happiness", "word": "summit", "stem": "summit",
    "avg": [ 4.28, 5.52 ], "std": [ 2.53, 1.62 ], "fq": 50 
  },
  "usage": {
    "dict": "happiness", "word": "usage", "stem": "usag",
    "avg": [ 5.28, 5.52 ], "std": [ 2.12, 1.50 ], "fq": 50 
  },
  "fills": {
    "dict": "happiness", "word": "fills", "stem": "fill",
    "avg": [ 4.94, 5.51 ], "std": [ 2.63, 1.20 ], "fq": 50 
  },
  "priests": {
    "dict": "happiness", "word": "priests", "stem": "priest",
    "avg": [ 4.41, 5.51 ], "std": [ 2.71, 2.01 ], "fq": 50 
  },
  "account": {
    "dict": "happiness", "word": "account", "stem": "account",
    "avg": [ 3.93, 5.50 ], "std": [ 2.29, 0.95 ], "fq": 50 
  },
  "arm": {
    "dict": "happiness", "word": "arm", "stem": "arm",
    "avg": [ 3.59, 5.50 ], "std": [ 2.40, 1.02 ], "fq": 50 
  },
  "capacity": {
    "dict": "happiness", "word": "capacity", "stem": "capac",
    "avg": [ 4.32, 5.50 ], "std": [ 2.14, 1.42 ], "fq": 50 
  },
  "chairwoman": {
    "dict": "happiness", "word": "chairwoman", "stem": "chairwoman",
    "avg": [ 3.15, 5.50 ], "std": [ 1.77, 1.18 ], "fq": 50 
  },
  "clay": {
    "dict": "happiness", "word": "clay", "stem": "clay",
    "avg": [ 4.74, 5.50 ], "std": [ 2.94, 1.33 ], "fq": 50 
  },
  "effects": {
    "dict": "happiness", "word": "effects", "stem": "effect",
    "avg": [ 5.42, 5.50 ], "std": [ 2.65, 1.47 ], "fq": 50 
  },
  "feels": {
    "dict": "happiness", "word": "feels", "stem": "feel",
    "avg": [ 3.78, 5.50 ], "std": [ 2.42, 1.74 ], "fq": 50 
  },
  "figure": {
    "dict": "happiness", "word": "figure", "stem": "figur",
    "avg": [ 4.75, 5.50 ], "std": [ 1.93, 1.15 ], "fq": 50 
  },
  "genetic": {
    "dict": "happiness", "word": "genetic", "stem": "genet",
    "avg": [ 4.80, 5.50 ], "std": [ 2.71, 1.25 ], "fq": 50 
  },
  "glasses": {
    "dict": "happiness", "word": "glasses", "stem": "glass",
    "avg": [ 4.27, 5.50 ], "std": [ 2.07, 1.30 ], "fq": 50 
  },
  "handled": {
    "dict": "happiness", "word": "handled", "stem": "handl",
    "avg": [ 5.62, 5.50 ], "std": [ 2.25, 0.93 ], "fq": 50 
  },
  "insure": {
    "dict": "happiness", "word": "insure", "stem": "insur",
    "avg": [ 6.10, 5.50 ], "std": [ 2.19, 1.43 ], "fq": 50 
  },
  "item": {
    "dict": "happiness", "word": "item", "stem": "item",
    "avg": [ 3.24, 5.50 ], "std": [ 2.08, 0.93 ], "fq": 50 
  },
  "manifest": {
    "dict": "happiness", "word": "manifest", "stem": "manifest",
    "avg": [ 3.50, 5.50 ], "std": [ 1.84, 1.36 ], "fq": 50 
  },
  "minute": {
    "dict": "happiness", "word": "minute", "stem": "minut",
    "avg": [ 3.83, 5.50 ], "std": [ 2.29, 0.93 ], "fq": 50 
  },
  "quiet": {
    "dict": "happiness", "word": "quiet", "stem": "quiet",
    "avg": [ 2.82, 5.50 ], "std": [ 2.13, 1.81 ], "fq": 50 
  },
  "ran": {
    "dict": "happiness", "word": "ran", "stem": "ran",
    "avg": [ 5.71, 5.50 ], "std": [ 2.74, 1.46 ], "fq": 50 
  },
  "rated": {
    "dict": "happiness", "word": "rated", "stem": "rate",
    "avg": [ 4.95, 5.50 ], "std": [ 2.36, 1.43 ], "fq": 50 
  },
  "settings": {
    "dict": "happiness", "word": "settings", "stem": "set",
    "avg": [ 4.22, 5.50 ], "std": [ 2.24, 1.25 ], "fq": 50 
  },
  "skin": {
    "dict": "happiness", "word": "skin", "stem": "skin",
    "avg": [ 5.28, 5.50 ], "std": [ 2.51, 1.56 ], "fq": 50 
  },
  "tie": {
    "dict": "happiness", "word": "tie", "stem": "tie",
    "avg": [ 5.97, 5.50 ], "std": [ 2.85, 1.18 ], "fq": 50 
  },
  "transmission": {
    "dict": "happiness", "word": "transmission", "stem": "transmiss",
    "avg": [ 5.03, 5.50 ], "std": [ 2.77, 1.33 ], "fq": 50 
  },
  "unit": {
    "dict": "happiness", "word": "unit", "stem": "unit",
    "avg": [ 3.75, 5.50 ], "std": [ 2.49, 0.97 ], "fq": 50 
  },
  "variation": {
    "dict": "happiness", "word": "variation", "stem": "variat",
    "avg": [ 4.84, 5.50 ], "std": [ 2.52, 1.18 ], "fq": 50 
  },
  "wearing": {
    "dict": "happiness", "word": "wearing", "stem": "wear",
    "avg": [ 2.64, 5.50 ], "std": [ 2.19, 1.18 ], "fq": 50 
  },
  "wild": {
    "dict": "happiness", "word": "wild", "stem": "wild",
    "avg": [ 4.14, 5.50 ], "std": [ 2.30, 1.81 ], "fq": 50 
  },
  "works": {
    "dict": "happiness", "word": "works", "stem": "work",
    "avg": [ 4.07, 5.50 ], "std": [ 1.98, 1.45 ], "fq": 50 
  },
  "flame": {
    "dict": "happiness", "word": "flame", "stem": "flame",
    "avg": [ 7.17, 5.49 ], "std": [ 2.06, 1.73 ], "fq": 50 
  },
  "church": {
    "dict": "happiness", "word": "church", "stem": "church",
    "avg": [ 4.34, 5.48 ], "std": [ 2.45, 1.85 ], "fq": 50 
  },
  "column": {
    "dict": "happiness", "word": "column", "stem": "column",
    "avg": [ 3.62, 5.48 ], "std": [ 1.91, 0.91 ], "fq": 50 
  },
  "demo": {
    "dict": "happiness", "word": "demo", "stem": "demo",
    "avg": [ 5.12, 5.48 ], "std": [ 2.39, 1.31 ], "fq": 50 
  },
  "encountered": {
    "dict": "happiness", "word": "encountered", "stem": "encount",
    "avg": [ 5.38, 5.48 ], "std": [ 2.58, 1.33 ], "fq": 50 
  },
  "felt": {
    "dict": "happiness", "word": "felt", "stem": "felt",
    "avg": [ 3.78, 5.48 ], "std": [ 2.42, 1.37 ], "fq": 50 
  },
  "habit": {
    "dict": "happiness", "word": "habit", "stem": "habit",
    "avg": [ 3.95, 5.48 ], "std": [ 2.11, 1.61 ], "fq": 50 
  },
  "highway": {
    "dict": "happiness", "word": "highway", "stem": "highway",
    "avg": [ 5.16, 5.48 ], "std": [ 2.44, 1.27 ], "fq": 50 
  },
  "jump": {
    "dict": "happiness", "word": "jump", "stem": "jump",
    "avg": [ 5.67, 5.48 ], "std": [ 2.51, 1.74 ], "fq": 50 
  },
  "led": {
    "dict": "happiness", "word": "led", "stem": "led",
    "avg": [ 3.15, 5.48 ], "std": [ 1.77, 1.13 ], "fq": 50 
  },
  "mark": {
    "dict": "happiness", "word": "mark", "stem": "mark",
    "avg": [ 4.79, 5.48 ], "std": [ 2.11, 1.30 ], "fq": 50 
  },
  "methods": {
    "dict": "happiness", "word": "methods", "stem": "method",
    "avg": [ 3.85, 5.48 ], "std": [ 2.58, 0.99 ], "fq": 50 
  },
  "nose": {
    "dict": "happiness", "word": "nose", "stem": "nose",
    "avg": [ 6.86, 5.48 ], "std": [ 2.41, 1.23 ], "fq": 50 
  },
  "operates": {
    "dict": "happiness", "word": "operates", "stem": "oper",
    "avg": [ 6.77, 5.48 ], "std": [ 2.07, 1.23 ], "fq": 50 
  },
  "palm": {
    "dict": "happiness", "word": "palm", "stem": "palm",
    "avg": [ 5.14, 5.48 ], "std": [ 2.39, 1.33 ], "fq": 50 
  },
  "picking": {
    "dict": "happiness", "word": "picking", "stem": "pick",
    "avg": [ 3.27, 5.48 ], "std": [ 1.98, 0.95 ], "fq": 50 
  },
  "portion": {
    "dict": "happiness", "word": "portion", "stem": "portion",
    "avg": [ 3.82, 5.48 ], "std": [ 2.24, 1.52 ], "fq": 50 
  },
  "post": {
    "dict": "happiness", "word": "post", "stem": "post",
    "avg": [ 4.08, 5.48 ], "std": [ 1.92, 1.09 ], "fq": 50 
  },
  "run": {
    "dict": "happiness", "word": "run", "stem": "run",
    "avg": [ 5.71, 5.48 ], "std": [ 2.74, 1.43 ], "fq": 50 
  },
  "sell": {
    "dict": "happiness", "word": "sell", "stem": "sell",
    "avg": [ 7.24, 5.48 ], "std": [ 2.06, 1.13 ], "fq": 50 
  },
  "shape": {
    "dict": "happiness", "word": "shape", "stem": "shape",
    "avg": [ 4.07, 5.48 ], "std": [ 1.98, 0.86 ], "fq": 50 
  },
  "square": {
    "dict": "happiness", "word": "square", "stem": "squar",
    "avg": [ 3.18, 5.48 ], "std": [ 1.76, 0.99 ], "fq": 50 
  },
  "tried": {
    "dict": "happiness", "word": "tried", "stem": "tri",
    "avg": [ 7.45, 5.48 ], "std": [ 2.38, 1.64 ], "fq": 50 
  },
  "truck": {
    "dict": "happiness", "word": "truck", "stem": "truck",
    "avg": [ 4.84, 5.48 ], "std": [ 2.17, 1.55 ], "fq": 50 
  },
  "tweet": {
    "dict": "happiness", "word": "tweet", "stem": "tweet",
    "avg": [ 4.59, 5.48 ], "std": [ 2.10, 1.59 ], "fq": 50 
  },
  "utility": {
    "dict": "happiness", "word": "utility", "stem": "util",
    "avg": [ 4.26, 5.48 ], "std": [ 2.47, 1.22 ], "fq": 50 
  },
  "dwell": {
    "dict": "happiness", "word": "dwell", "stem": "dwell",
    "avg": [ 5.96, 5.47 ], "std": [ 2.63, 1.66 ], "fq": 50 
  },
  "elaborate": {
    "dict": "happiness", "word": "elaborate", "stem": "elabor",
    "avg": [ 4.10, 5.47 ], "std": [ 2.24, 1.66 ], "fq": 50 
  },
  "grip": {
    "dict": "happiness", "word": "grip", "stem": "grip",
    "avg": [ 5.83, 5.47 ], "std": [ 2.73, 1.71 ], "fq": 50 
  },
  "loaded": {
    "dict": "happiness", "word": "loaded", "stem": "load",
    "avg": [ 5.70, 5.47 ], "std": [ 2.66, 1.84 ], "fq": 50 
  },
  "caption": {
    "dict": "happiness", "word": "caption", "stem": "caption",
    "avg": [ 4.88, 5.46 ], "std": [ 1.76, 0.84 ], "fq": 50 
  },
  "cavalry": {
    "dict": "happiness", "word": "cavalry", "stem": "cavalri",
    "avg": [ 3.89, 5.46 ], "std": [ 2.17, 1.73 ], "fq": 50 
  },
  "chronicle": {
    "dict": "happiness", "word": "chronicle", "stem": "chronicl",
    "avg": [ 3.93, 5.46 ], "std": [ 2.29, 1.53 ], "fq": 50 
  },
  "consisted": {
    "dict": "happiness", "word": "consisted", "stem": "consist",
    "avg": [ 5.96, 5.46 ], "std": [ 2.63, 1.33 ], "fq": 50 
  },
  "contract": {
    "dict": "happiness", "word": "contract", "stem": "contract",
    "avg": [ 5.00, 5.46 ], "std": [ 2.32, 1.11 ], "fq": 50 
  },
  "directed": {
    "dict": "happiness", "word": "directed", "stem": "direct",
    "avg": [ 3.98, 5.46 ], "std": [ 2.33, 1.07 ], "fq": 50 
  },
  "explain": {
    "dict": "happiness", "word": "explain", "stem": "explain",
    "avg": [ 4.48, 5.46 ], "std": [ 2.29, 1.34 ], "fq": 50 
  },
  "followed": {
    "dict": "happiness", "word": "followed", "stem": "follow",
    "avg": [ 4.10, 5.46 ], "std": [ 2.12, 1.22 ], "fq": 50 
  },
  "fox": {
    "dict": "happiness", "word": "fox", "stem": "fox",
    "avg": [ 6.03, 5.46 ], "std": [ 1.88, 1.72 ], "fq": 50 
  },
  "index": {
    "dict": "happiness", "word": "index", "stem": "index",
    "avg": [ 5.83, 5.46 ], "std": [ 2.69, 1.23 ], "fq": 50 
  },
  "instructions": {
    "dict": "happiness", "word": "instructions", "stem": "instruct",
    "avg": [ 5.74, 5.46 ], "std": [ 2.46, 1.45 ], "fq": 50 
  },
  "linked": {
    "dict": "happiness", "word": "linked", "stem": "link",
    "avg": [ 6.39, 5.46 ], "std": [ 2.31, 1.40 ], "fq": 50 
  },
  "list": {
    "dict": "happiness", "word": "list", "stem": "list",
    "avg": [ 4.25, 5.46 ], "std": [ 2.47, 0.86 ], "fq": 50 
  },
  "meeting": {
    "dict": "happiness", "word": "meeting", "stem": "meet",
    "avg": [ 4.94, 5.46 ], "std": [ 2.63, 1.34 ], "fq": 50 
  },
  "process": {
    "dict": "happiness", "word": "process", "stem": "process",
    "avg": [ 5.62, 5.46 ], "std": [ 2.25, 1.11 ], "fq": 50 
  },
  "sent": {
    "dict": "happiness", "word": "sent", "stem": "sent",
    "avg": [ 5.63, 5.46 ], "std": [ 2.36, 0.91 ], "fq": 50 
  },
  "serve": {
    "dict": "happiness", "word": "serve", "stem": "serv",
    "avg": [ 5.41, 5.46 ], "std": [ 2.43, 1.31 ], "fq": 50 
  },
  "shipping": {
    "dict": "happiness", "word": "shipping", "stem": "ship",
    "avg": [ 4.38, 5.46 ], "std": [ 2.29, 1.31 ], "fq": 50 
  },
  "stacks": {
    "dict": "happiness", "word": "stacks", "stem": "stack",
    "avg": [ 5.49, 5.46 ], "std": [ 2.43, 1.33 ], "fq": 50 
  },
  "watched": {
    "dict": "happiness", "word": "watched", "stem": "watch",
    "avg": [ 4.10, 5.46 ], "std": [ 2.12, 1.27 ], "fq": 50 
  },
  "notions": {
    "dict": "happiness", "word": "notions", "stem": "notion",
    "avg": [ 5.42, 5.46 ], "std": [ 2.65, 1.13 ], "fq": 50 
  },
  "unfold": {
    "dict": "happiness", "word": "unfold", "stem": "unfold",
    "avg": [ 5.03, 5.46 ], "std": [ 2.65, 1.32 ], "fq": 50 
  },
  "situations": {
    "dict": "happiness", "word": "situations", "stem": "situat",
    "avg": [ 4.08, 5.45 ], "std": [ 1.92, 1.14 ], "fq": 50 
  },
  "sway": {
    "dict": "happiness", "word": "sway", "stem": "sway",
    "avg": [ 4.52, 5.45 ], "std": [ 2.37, 1.21 ], "fq": 50 
  },
  "drawers": {
    "dict": "happiness", "word": "drawers", "stem": "drawer",
    "avg": [ 5.12, 5.45 ], "std": [ 2.26, 1.32 ], "fq": 50 
  },
  "area": {
    "dict": "happiness", "word": "area", "stem": "area",
    "avg": [ 4.08, 5.44 ], "std": [ 2.41, 0.88 ], "fq": 50 
  },
  "assigned": {
    "dict": "happiness", "word": "assigned", "stem": "assign",
    "avg": [ 5.65, 5.44 ], "std": [ 2.23, 1.23 ], "fq": 50 
  },
  "bob": {
    "dict": "happiness", "word": "bob", "stem": "bob",
    "avg": [ 3.80, 5.44 ], "std": [ 2.18, 1.16 ], "fq": 50 
  },
  "calculation": {
    "dict": "happiness", "word": "calculation", "stem": "calcul",
    "avg": [ 4.75, 5.44 ], "std": [ 1.93, 1.20 ], "fq": 50 
  },
  "centres": {
    "dict": "happiness", "word": "centres", "stem": "centr",
    "avg": [ 6.34, 5.44 ], "std": [ 2.25, 1.23 ], "fq": 50 
  },
  "chair": {
    "dict": "happiness", "word": "chair", "stem": "chair",
    "avg": [ 3.15, 5.44 ], "std": [ 1.77, 1.25 ], "fq": 50 
  },
  "charter": {
    "dict": "happiness", "word": "charter", "stem": "charter",
    "avg": [ 6.77, 5.44 ], "std": [ 2.07, 0.93 ], "fq": 50 
  },
  "company": {
    "dict": "happiness", "word": "company", "stem": "compani",
    "avg": [ 6.69, 5.44 ], "std": [ 2.84, 1.58 ], "fq": 50 
  },
  "consist": {
    "dict": "happiness", "word": "consist", "stem": "consist",
    "avg": [ 5.96, 5.44 ], "std": [ 2.63, 1.28 ], "fq": 50 
  },
  "curtains": {
    "dict": "happiness", "word": "curtains", "stem": "curtain",
    "avg": [ 3.67, 5.44 ], "std": [ 1.83, 1.37 ], "fq": 50 
  },
  "deck": {
    "dict": "happiness", "word": "deck", "stem": "deck",
    "avg": [ 5.14, 5.44 ], "std": [ 2.39, 1.39 ], "fq": 50 
  },
  "doors": {
    "dict": "happiness", "word": "doors", "stem": "door",
    "avg": [ 3.80, 5.44 ], "std": [ 2.29, 1.07 ], "fq": 50 
  },
  "flow": {
    "dict": "happiness", "word": "flow", "stem": "flow",
    "avg": [ 4.70, 5.44 ], "std": [ 2.48, 1.59 ], "fq": 50 
  },
  "imports": {
    "dict": "happiness", "word": "imports", "stem": "import",
    "avg": [ 3.83, 5.44 ], "std": [ 2.29, 1.49 ], "fq": 50 
  },
  "mass": {
    "dict": "happiness", "word": "mass", "stem": "mass",
    "avg": [ 5.49, 5.44 ], "std": [ 2.43, 1.11 ], "fq": 50 
  },
  "metal": {
    "dict": "happiness", "word": "metal", "stem": "metal",
    "avg": [ 3.79, 5.44 ], "std": [ 1.96, 1.28 ], "fq": 50 
  },
  "operating": {
    "dict": "happiness", "word": "operating", "stem": "oper",
    "avg": [ 6.77, 5.44 ], "std": [ 2.07, 1.42 ], "fq": 50 
  },
  "passes": {
    "dict": "happiness", "word": "passes", "stem": "pass",
    "avg": [ 4.70, 5.44 ], "std": [ 2.48, 1.49 ], "fq": 50 
  },
  "passing": {
    "dict": "happiness", "word": "passing", "stem": "pass",
    "avg": [ 4.36, 5.44 ], "std": [ 2.13, 1.74 ], "fq": 50 
  },
  "refers": {
    "dict": "happiness", "word": "refers", "stem": "refer",
    "avg": [ 4.25, 5.44 ], "std": [ 2.47, 1.16 ], "fq": 50 
  },
  "represent": {
    "dict": "happiness", "word": "represent", "stem": "repres",
    "avg": [ 5.12, 5.44 ], "std": [ 2.39, 1.05 ], "fq": 50 
  },
  "saw": {
    "dict": "happiness", "word": "saw", "stem": "saw",
    "avg": [ 6.10, 5.44 ], "std": [ 2.19, 0.81 ], "fq": 50 
  },
  "sept": {
    "dict": "happiness", "word": "sept", "stem": "sept",
    "avg": [ 4.80, 5.44 ], "std": [ 2.71, 1.03 ], "fq": 50 
  },
  "storage": {
    "dict": "happiness", "word": "storage", "stem": "storag",
    "avg": [ 5.42, 5.44 ], "std": [ 2.25, 1.07 ], "fq": 50 
  },
  "street": {
    "dict": "happiness", "word": "street", "stem": "street",
    "avg": [ 3.39, 5.44 ], "std": [ 1.87, 0.84 ], "fq": 50 
  },
  "subject": {
    "dict": "happiness", "word": "subject", "stem": "subject",
    "avg": [ 4.32, 5.44 ], "std": [ 2.14, 1.03 ], "fq": 50 
  },
  "submit": {
    "dict": "happiness", "word": "submit", "stem": "submit",
    "avg": [ 5.12, 5.44 ], "std": [ 2.39, 1.50 ], "fq": 50 
  },
  "tone": {
    "dict": "happiness", "word": "tone", "stem": "tone",
    "avg": [ 4.48, 5.44 ], "std": [ 2.12, 0.86 ], "fq": 50 
  },
  "tongue": {
    "dict": "happiness", "word": "tongue", "stem": "tongu",
    "avg": [ 5.80, 5.44 ], "std": [ 2.00, 1.09 ], "fq": 50 
  },
  "trunk": {
    "dict": "happiness", "word": "trunk", "stem": "trunk",
    "avg": [ 4.18, 5.44 ], "std": [ 2.19, 0.97 ], "fq": 50 
  },
  "tweeted": {
    "dict": "happiness", "word": "tweeted", "stem": "tweet",
    "avg": [ 4.59, 5.44 ], "std": [ 2.10, 1.69 ], "fq": 50 
  },
  "worked": {
    "dict": "happiness", "word": "worked", "stem": "work",
    "avg": [ 4.07, 5.44 ], "std": [ 1.98, 1.58 ], "fq": 50 
  },
  "yen": {
    "dict": "happiness", "word": "yen", "stem": "yen",
    "avg": [ 5.00, 5.44 ], "std": [ 2.45, 1.43 ], "fq": 50 
  },
  "modes": {
    "dict": "happiness", "word": "modes", "stem": "mode",
    "avg": [ 4.56, 5.43 ], "std": [ 1.78, 1.21 ], "fq": 50 
  },
  "barrel": {
    "dict": "happiness", "word": "barrel", "stem": "barrel",
    "avg": [ 3.36, 5.42 ], "std": [ 2.28, 1.29 ], "fq": 50 
  },
  "bowl": {
    "dict": "happiness", "word": "bowl", "stem": "bowl",
    "avg": [ 3.47, 5.42 ], "std": [ 2.12, 1.26 ], "fq": 50 
  },
  "calls": {
    "dict": "happiness", "word": "calls", "stem": "call",
    "avg": [ 6.07, 5.42 ], "std": [ 2.42, 1.03 ], "fq": 50 
  },
  "came": {
    "dict": "happiness", "word": "came", "stem": "came",
    "avg": [ 4.70, 5.42 ], "std": [ 2.48, 1.42 ], "fq": 50 
  },
  "category": {
    "dict": "happiness", "word": "category", "stem": "categori",
    "avg": [ 4.80, 5.42 ], "std": [ 2.71, 1.50 ], "fq": 50 
  },
  "centre": {
    "dict": "happiness", "word": "centre", "stem": "centr",
    "avg": [ 6.34, 5.42 ], "std": [ 2.25, 0.84 ], "fq": 50 
  },
  "course": {
    "dict": "happiness", "word": "course", "stem": "cours",
    "avg": [ 4.37, 5.42 ], "std": [ 2.51, 1.37 ], "fq": 50 
  },
  "crow": {
    "dict": "happiness", "word": "crow", "stem": "crow",
    "avg": [ 5.78, 5.42 ], "std": [ 2.60, 1.68 ], "fq": 50 
  },
  "derived": {
    "dict": "happiness", "word": "derived", "stem": "deriv",
    "avg": [ 5.74, 5.42 ], "std": [ 2.46, 1.21 ], "fq": 50 
  },
  "floors": {
    "dict": "happiness", "word": "floors", "stem": "floor",
    "avg": [ 4.12, 5.42 ], "std": [ 2.36, 0.84 ], "fq": 50 
  },
  "going": {
    "dict": "happiness", "word": "going", "stem": "go",
    "avg": [ 6.21, 5.42 ], "std": [ 2.51, 1.16 ], "fq": 50 
  },
  "gotten": {
    "dict": "happiness", "word": "gotten", "stem": "gotten",
    "avg": [ 5.92, 5.42 ], "std": [ 2.60, 1.39 ], "fq": 50 
  },
  "inner": {
    "dict": "happiness", "word": "inner", "stem": "inner",
    "avg": [ 6.98, 5.42 ], "std": [ 2.21, 1.03 ], "fq": 50 
  },
  "mentioned": {
    "dict": "happiness", "word": "mentioned", "stem": "mention",
    "avg": [ 4.25, 5.42 ], "std": [ 2.47, 1.11 ], "fq": 50 
  },
  "nowadays": {
    "dict": "happiness", "word": "nowadays", "stem": "nowaday",
    "avg": [ 5.12, 5.42 ], "std": [ 2.39, 1.46 ], "fq": 50 
  },
  "peter": {
    "dict": "happiness", "word": "peter", "stem": "peter",
    "avg": [ 4.70, 5.42 ], "std": [ 2.59, 1.05 ], "fq": 50 
  },
  "point": {
    "dict": "happiness", "word": "point", "stem": "point",
    "avg": [ 4.10, 5.42 ], "std": [ 2.24, 0.91 ], "fq": 50 
  },
  "polls": {
    "dict": "happiness", "word": "polls", "stem": "poll",
    "avg": [ 4.28, 5.42 ], "std": [ 2.53, 1.28 ], "fq": 50 
  },
  "presentation": {
    "dict": "happiness", "word": "presentation", "stem": "present",
    "avg": [ 5.12, 5.42 ], "std": [ 2.39, 1.58 ], "fq": 50 
  },
  "rolled": {
    "dict": "happiness", "word": "rolled", "stem": "roll",
    "avg": [ 5.55, 5.42 ], "std": [ 2.39, 1.36 ], "fq": 50 
  },
  "select": {
    "dict": "happiness", "word": "select", "stem": "select",
    "avg": [ 4.48, 5.42 ], "std": [ 2.12, 1.25 ], "fq": 50 
  },
  "subjects": {
    "dict": "happiness", "word": "subjects", "stem": "subject",
    "avg": [ 4.32, 5.42 ], "std": [ 2.14, 1.01 ], "fq": 50 
  },
  "tables": {
    "dict": "happiness", "word": "tables", "stem": "tabl",
    "avg": [ 2.92, 5.42 ], "std": [ 2.16, 0.84 ], "fq": 50 
  },
  "tell": {
    "dict": "happiness", "word": "tell", "stem": "tell",
    "avg": [ 5.26, 5.42 ], "std": [ 2.36, 1.03 ], "fq": 50 
  },
  "theory": {
    "dict": "happiness", "word": "theory", "stem": "theori",
    "avg": [ 4.62, 5.42 ], "std": [ 1.94, 1.49 ], "fq": 50 
  },
  "toss": {
    "dict": "happiness", "word": "toss", "stem": "toss",
    "avg": [ 4.27, 5.42 ], "std": [ 2.17, 1.37 ], "fq": 50 
  },
  "tweets": {
    "dict": "happiness", "word": "tweets", "stem": "tweet",
    "avg": [ 4.59, 5.42 ], "std": [ 2.10, 1.97 ], "fq": 50 
  },
  "calculated": {
    "dict": "happiness", "word": "calculated", "stem": "calcul",
    "avg": [ 4.75, 5.42 ], "std": [ 1.93, 1.40 ], "fq": 50 
  },
  "inhabitants": {
    "dict": "happiness", "word": "inhabitants", "stem": "inhabit",
    "avg": [ 3.95, 5.42 ], "std": [ 1.97, 1.44 ], "fq": 50 
  },
  "constitutes": {
    "dict": "happiness", "word": "constitutes", "stem": "constitut",
    "avg": [ 3.62, 5.41 ], "std": [ 2.25, 1.37 ], "fq": 50 
  },
  "boldface": {
    "dict": "happiness", "word": "boldface", "stem": "boldfac",
    "avg": [ 5.60, 5.40 ], "std": [ 2.21, 1.09 ], "fq": 50 
  },
  "cast": {
    "dict": "happiness", "word": "cast", "stem": "cast",
    "avg": [ 4.07, 5.40 ], "std": [ 1.98, 1.37 ], "fq": 50 
  },
  "claimed": {
    "dict": "happiness", "word": "claimed", "stem": "claim",
    "avg": [ 5.65, 5.40 ], "std": [ 2.23, 1.18 ], "fq": 50 
  },
  "consecutive": {
    "dict": "happiness", "word": "consecutive", "stem": "consecut",
    "avg": [ 6.11, 5.40 ], "std": [ 2.65, 1.16 ], "fq": 50 
  },
  "document": {
    "dict": "happiness", "word": "document", "stem": "document",
    "avg": [ 2.50, 5.40 ], "std": [ 1.85, 1.23 ], "fq": 50 
  },
  "estimate": {
    "dict": "happiness", "word": "estimate", "stem": "estim",
    "avg": [ 5.86, 5.40 ], "std": [ 1.81, 0.99 ], "fq": 50 
  },
  "figured": {
    "dict": "happiness", "word": "figured", "stem": "figur",
    "avg": [ 4.75, 5.40 ], "std": [ 1.93, 1.18 ], "fq": 50 
  },
  "fuel": {
    "dict": "happiness", "word": "fuel", "stem": "fuel",
    "avg": [ 7.17, 5.40 ], "std": [ 2.06, 1.18 ], "fq": 50 
  },
  "holds": {
    "dict": "happiness", "word": "holds", "stem": "hold",
    "avg": [ 6.10, 5.40 ], "std": [ 2.19, 1.07 ], "fq": 50 
  },
  "intent": {
    "dict": "happiness", "word": "intent", "stem": "intent",
    "avg": [ 5.56, 5.40 ], "std": [ 2.62, 1.46 ], "fq": 50 
  },
  "main": {
    "dict": "happiness", "word": "main", "stem": "main",
    "avg": [ 5.20, 5.40 ], "std": [ 2.85, 1.21 ], "fq": 50 
  },
  "obedience": {
    "dict": "happiness", "word": "obedience", "stem": "obedi",
    "avg": [ 4.60, 5.40 ], "std": [ 2.67, 1.62 ], "fq": 50 
  },
  "one": {
    "dict": "happiness", "word": "one", "stem": "one",
    "avg": [ 5.50, 5.40 ], "std": [ 2.66, 1.59 ], "fq": 50 
  },
  "picks": {
    "dict": "happiness", "word": "picks", "stem": "pick",
    "avg": [ 4.74, 5.40 ], "std": [ 2.23, 1.36 ], "fq": 50 
  },
  "processes": {
    "dict": "happiness", "word": "processes", "stem": "process",
    "avg": [ 5.62, 5.40 ], "std": [ 2.25, 1.48 ], "fq": 50 
  },
  "putting": {
    "dict": "happiness", "word": "putting", "stem": "put",
    "avg": [ 5.12, 5.40 ], "std": [ 2.42, 1.09 ], "fq": 50 
  },
  "represents": {
    "dict": "happiness", "word": "represents", "stem": "repres",
    "avg": [ 5.12, 5.40 ], "std": [ 2.39, 0.88 ], "fq": 50 
  },
  "seen": {
    "dict": "happiness", "word": "seen", "stem": "seen",
    "avg": [ 6.10, 5.40 ], "std": [ 2.19, 1.20 ], "fq": 50 
  },
  "stayed": {
    "dict": "happiness", "word": "stayed", "stem": "stay",
    "avg": [ 5.62, 5.40 ], "std": [ 2.39, 1.25 ], "fq": 50 
  },
  "stomach": {
    "dict": "happiness", "word": "stomach", "stem": "stomach",
    "avg": [ 3.93, 5.40 ], "std": [ 2.49, 1.07 ], "fq": 50 
  },
  "tap": {
    "dict": "happiness", "word": "tap", "stem": "tap",
    "avg": [ 3.71, 5.40 ], "std": [ 1.75, 1.23 ], "fq": 50 
  },
  "arms": {
    "dict": "happiness", "word": "arms", "stem": "arm",
    "avg": [ 3.59, 5.38 ], "std": [ 2.40, 0.99 ], "fq": 50 
  },
  "basis": {
    "dict": "happiness", "word": "basis", "stem": "basi",
    "avg": [ 3.27, 5.38 ], "std": [ 1.98, 1.01 ], "fq": 50 
  },
  "control": {
    "dict": "happiness", "word": "control", "stem": "control",
    "avg": [ 6.10, 5.38 ], "std": [ 2.19, 1.48 ], "fq": 50 
  },
  "core": {
    "dict": "happiness", "word": "core", "stem": "core",
    "avg": [ 6.34, 5.38 ], "std": [ 2.25, 1.09 ], "fq": 50 
  },
  "door": {
    "dict": "happiness", "word": "door", "stem": "door",
    "avg": [ 3.80, 5.38 ], "std": [ 2.29, 1.21 ], "fq": 50 
  },
  "following": {
    "dict": "happiness", "word": "following", "stem": "follow",
    "avg": [ 4.10, 5.38 ], "std": [ 2.12, 1.64 ], "fq": 50 
  },
  "industry": {
    "dict": "happiness", "word": "industry", "stem": "industri",
    "avg": [ 4.47, 5.38 ], "std": [ 2.43, 1.31 ], "fq": 50 
  },
  "items": {
    "dict": "happiness", "word": "items", "stem": "item",
    "avg": [ 3.24, 5.38 ], "std": [ 2.08, 1.54 ], "fq": 50 
  },
  "machine": {
    "dict": "happiness", "word": "machine", "stem": "machin",
    "avg": [ 3.82, 5.38 ], "std": [ 2.40, 1.26 ], "fq": 50 
  },
  "manner": {
    "dict": "happiness", "word": "manner", "stem": "manner",
    "avg": [ 4.56, 5.38 ], "std": [ 1.78, 1.35 ], "fq": 50 
  },
  "pitching": {
    "dict": "happiness", "word": "pitching", "stem": "pitch",
    "avg": [ 4.27, 5.38 ], "std": [ 2.17, 1.43 ], "fq": 50 
  },
  "rope": {
    "dict": "happiness", "word": "rope", "stem": "rope",
    "avg": [ 3.86, 5.38 ], "std": [ 2.13, 1.26 ], "fq": 50 
  },
  "second": {
    "dict": "happiness", "word": "second", "stem": "second",
    "avg": [ 3.83, 5.38 ], "std": [ 2.29, 1.19 ], "fq": 50 
  },
  "securities": {
    "dict": "happiness", "word": "securities", "stem": "secur",
    "avg": [ 3.14, 5.38 ], "std": [ 2.47, 2.05 ], "fq": 50 
  },
  "send": {
    "dict": "happiness", "word": "send", "stem": "send",
    "avg": [ 5.63, 5.38 ], "std": [ 2.36, 1.35 ], "fq": 50 
  },
  "standards": {
    "dict": "happiness", "word": "standards", "stem": "standard",
    "avg": [ 3.83, 5.38 ], "std": [ 1.95, 1.09 ], "fq": 50 
  },
  "steps": {
    "dict": "happiness", "word": "steps", "stem": "step",
    "avg": [ 6.83, 5.38 ], "std": [ 2.70, 1.12 ], "fq": 50 
  },
  "tan": {
    "dict": "happiness", "word": "tan", "stem": "tan",
    "avg": [ 6.22, 5.38 ], "std": [ 1.91, 1.71 ], "fq": 50 
  },
  "tricks": {
    "dict": "happiness", "word": "tricks", "stem": "trick",
    "avg": [ 5.95, 5.38 ], "std": [ 2.36, 1.52 ], "fq": 50 
  },
  "wants": {
    "dict": "happiness", "word": "wants", "stem": "want",
    "avg": [ 5.16, 5.38 ], "std": [ 2.62, 1.32 ], "fq": 50 
  },
  "sits": {
    "dict": "happiness", "word": "sits", "stem": "sit",
    "avg": [ 2.95, 5.37 ], "std": [ 1.72, 1.09 ], "fq": 50 
  },
  "illusions": {
    "dict": "happiness", "word": "illusions", "stem": "illus",
    "avg": [ 5.14, 5.36 ], "std": [ 2.82, 1.81 ], "fq": 50 
  },
  "bee": {
    "dict": "happiness", "word": "bee", "stem": "bee",
    "avg": [ 6.51, 5.36 ], "std": [ 2.14, 1.65 ], "fq": 50 
  },
  "caps": {
    "dict": "happiness", "word": "caps", "stem": "cap",
    "avg": [ 4.28, 5.36 ], "std": [ 2.53, 1.03 ], "fq": 50 
  },
  "clip": {
    "dict": "happiness", "word": "clip", "stem": "clip",
    "avg": [ 4.05, 5.36 ], "std": [ 1.89, 1.26 ], "fq": 50 
  },
  "clips": {
    "dict": "happiness", "word": "clips", "stem": "clip",
    "avg": [ 4.05, 5.36 ], "std": [ 1.89, 1.17 ], "fq": 50 
  },
  "constitute": {
    "dict": "happiness", "word": "constitute", "stem": "constitut",
    "avg": [ 3.62, 5.36 ], "std": [ 2.25, 1.14 ], "fq": 50 
  },
  "contracts": {
    "dict": "happiness", "word": "contracts", "stem": "contract",
    "avg": [ 5.00, 5.36 ], "std": [ 2.32, 1.24 ], "fq": 50 
  },
  "covering": {
    "dict": "happiness", "word": "covering", "stem": "cover",
    "avg": [ 5.28, 5.36 ], "std": [ 2.51, 0.88 ], "fq": 50 
  },
  "customs": {
    "dict": "happiness", "word": "customs", "stem": "custom",
    "avg": [ 4.66, 5.36 ], "std": [ 2.12, 1.64 ], "fq": 50 
  },
  "dash": {
    "dict": "happiness", "word": "dash", "stem": "dash",
    "avg": [ 6.95, 5.36 ], "std": [ 2.44, 1.48 ], "fq": 50 
  },
  "dishes": {
    "dict": "happiness", "word": "dishes", "stem": "dish",
    "avg": [ 5.50, 5.36 ], "std": [ 2.73, 1.82 ], "fq": 50 
  },
  "edit": {
    "dict": "happiness", "word": "edit", "stem": "edit",
    "avg": [ 5.00, 5.36 ], "std": [ 2.32, 1.17 ], "fq": 50 
  },
  "finger": {
    "dict": "happiness", "word": "finger", "stem": "finger",
    "avg": [ 3.78, 5.36 ], "std": [ 2.42, 1.17 ], "fq": 50 
  },
  "greene": {
    "dict": "happiness", "word": "greene", "stem": "green",
    "avg": [ 4.28, 5.36 ], "std": [ 2.46, 1.05 ], "fq": 50 
  },
  "hay": {
    "dict": "happiness", "word": "hay", "stem": "hay",
    "avg": [ 3.95, 5.36 ], "std": [ 2.58, 1.48 ], "fq": 50 
  },
  "heard": {
    "dict": "happiness", "word": "heard", "stem": "heard",
    "avg": [ 5.39, 5.36 ], "std": [ 2.22, 0.80 ], "fq": 50 
  },
  "liquor": {
    "dict": "happiness", "word": "liquor", "stem": "liquor",
    "avg": [ 5.56, 5.36 ], "std": [ 2.62, 2.28 ], "fq": 50 
  },
  "listing": {
    "dict": "happiness", "word": "listing", "stem": "list",
    "avg": [ 4.25, 5.36 ], "std": [ 2.47, 1.01 ], "fq": 50 
  },
  "moving": {
    "dict": "happiness", "word": "moving", "stem": "move",
    "avg": [ 5.42, 5.36 ], "std": [ 2.65, 1.50 ], "fq": 50 
  },
  "nude": {
    "dict": "happiness", "word": "nude", "stem": "nude",
    "avg": [ 6.41, 5.36 ], "std": [ 2.09, 1.97 ], "fq": 50 
  },
  "press": {
    "dict": "happiness", "word": "press", "stem": "press",
    "avg": [ 6.07, 5.36 ], "std": [ 2.26, 1.22 ], "fq": 50 
  },
  "principal": {
    "dict": "happiness", "word": "principal", "stem": "princip",
    "avg": [ 5.83, 5.36 ], "std": [ 2.44, 1.40 ], "fq": 50 
  },
  "sit": {
    "dict": "happiness", "word": "sit", "stem": "sit",
    "avg": [ 2.95, 5.36 ], "std": [ 1.72, 1.22 ], "fq": 50 
  },
  "sold": {
    "dict": "happiness", "word": "sold", "stem": "sold",
    "avg": [ 7.24, 5.36 ], "std": [ 2.06, 1.29 ], "fq": 50 
  },
  "standing": {
    "dict": "happiness", "word": "standing", "stem": "stand",
    "avg": [ 3.93, 5.36 ], "std": [ 2.49, 0.85 ], "fq": 50 
  },
  "trucks": {
    "dict": "happiness", "word": "trucks", "stem": "truck",
    "avg": [ 4.84, 5.36 ], "std": [ 2.17, 1.66 ], "fq": 50 
  },
  "tummy": {
    "dict": "happiness", "word": "tummy", "stem": "tummi",
    "avg": [ 3.93, 5.36 ], "std": [ 2.49, 1.38 ], "fq": 50 
  },
  "tweeting": {
    "dict": "happiness", "word": "tweeting", "stem": "tweet",
    "avg": [ 4.59, 5.36 ], "std": [ 2.10, 1.97 ], "fq": 50 
  },
  "vest": {
    "dict": "happiness", "word": "vest", "stem": "vest",
    "avg": [ 3.95, 5.36 ], "std": [ 2.09, 1.14 ], "fq": 50 
  },
  "wakes": {
    "dict": "happiness", "word": "wakes", "stem": "wake",
    "avg": [ 6.63, 5.36 ], "std": [ 2.70, 1.68 ], "fq": 50 
  },
  "loot": {
    "dict": "happiness", "word": "loot", "stem": "loot",
    "avg": [ 5.64, 5.35 ], "std": [ 2.18, 2.09 ], "fq": 50 
  },
  "adams": {
    "dict": "happiness", "word": "adams", "stem": "adam",
    "avg": [ 7.38, 5.34 ], "std": [ 1.92, 1.08 ], "fq": 50 
  },
  "areas": {
    "dict": "happiness", "word": "areas", "stem": "area",
    "avg": [ 4.08, 5.34 ], "std": [ 2.41, 1.02 ], "fq": 50 
  },
  "backs": {
    "dict": "happiness", "word": "backs", "stem": "back",
    "avg": [ 5.89, 5.34 ], "std": [ 2.37, 1.44 ], "fq": 50 
  },
  "campaign": {
    "dict": "happiness", "word": "campaign", "stem": "campaign",
    "avg": [ 7.15, 5.34 ], "std": [ 2.19, 1.55 ], "fq": 50 
  },
  "checked": {
    "dict": "happiness", "word": "checked", "stem": "check",
    "avg": [ 6.10, 5.34 ], "std": [ 2.19, 1.14 ], "fq": 50 
  },
  "crossing": {
    "dict": "happiness", "word": "crossing", "stem": "cross",
    "avg": [ 5.61, 5.34 ], "std": [ 2.76, 1.33 ], "fq": 50 
  },
  "currently": {
    "dict": "happiness", "word": "currently", "stem": "current",
    "avg": [ 5.12, 5.34 ], "std": [ 2.39, 0.82 ], "fq": 50 
  },
  "doctor": {
    "dict": "happiness", "word": "doctor", "stem": "doctor",
    "avg": [ 5.86, 5.34 ], "std": [ 2.70, 1.62 ], "fq": 50 
  },
  "drank": {
    "dict": "happiness", "word": "drank", "stem": "drank",
    "avg": [ 5.31, 5.34 ], "std": [ 2.23, 1.47 ], "fq": 50 
  },
  "editorial": {
    "dict": "happiness", "word": "editorial", "stem": "editori",
    "avg": [ 3.62, 5.34 ], "std": [ 1.91, 1.36 ], "fq": 50 
  },
  "flick": {
    "dict": "happiness", "word": "flick", "stem": "flick",
    "avg": [ 4.93, 5.34 ], "std": [ 2.54, 1.36 ], "fq": 50 
  },
  "fur": {
    "dict": "happiness", "word": "fur", "stem": "fur",
    "avg": [ 4.18, 5.34 ], "std": [ 2.44, 1.73 ], "fq": 50 
  },
  "iron": {
    "dict": "happiness", "word": "iron", "stem": "iron",
    "avg": [ 3.76, 5.34 ], "std": [ 2.06, 1.35 ], "fq": 50 
  },
  "middle": {
    "dict": "happiness", "word": "middle", "stem": "middl",
    "avg": [ 6.34, 5.34 ], "std": [ 2.25, 0.72 ], "fq": 50 
  },
  "moderate": {
    "dict": "happiness", "word": "moderate", "stem": "moder",
    "avg": [ 6.10, 5.34 ], "std": [ 2.19, 1.27 ], "fq": 50 
  },
  "physician": {
    "dict": "happiness", "word": "physician", "stem": "physician",
    "avg": [ 5.86, 5.34 ], "std": [ 2.70, 1.84 ], "fq": 50 
  },
  "transmitted": {
    "dict": "happiness", "word": "transmitted", "stem": "transmit",
    "avg": [ 4.80, 5.34 ], "std": [ 2.71, 1.57 ], "fq": 50 
  },
  "blink": {
    "dict": "happiness", "word": "blink", "stem": "blink",
    "avg": [ 5.44, 5.33 ], "std": [ 2.68, 1.43 ], "fq": 50 
  },
  "threshold": {
    "dict": "happiness", "word": "threshold", "stem": "threshold",
    "avg": [ 3.80, 5.33 ], "std": [ 2.29, 1.48 ], "fq": 50 
  },
  "bench": {
    "dict": "happiness", "word": "bench", "stem": "bench",
    "avg": [ 3.59, 5.32 ], "std": [ 2.07, 1.04 ], "fq": 50 
  },
  "chin": {
    "dict": "happiness", "word": "chin", "stem": "chin",
    "avg": [ 3.31, 5.32 ], "std": [ 1.98, 0.98 ], "fq": 50 
  },
  "cover": {
    "dict": "happiness", "word": "cover", "stem": "cover",
    "avg": [ 5.28, 5.32 ], "std": [ 2.51, 1.27 ], "fq": 50 
  },
  "deepest": {
    "dict": "happiness", "word": "deepest", "stem": "deepest",
    "avg": [ 6.17, 5.32 ], "std": [ 2.70, 1.45 ], "fq": 50 
  },
  "editorials": {
    "dict": "happiness", "word": "editorials", "stem": "editori",
    "avg": [ 3.62, 5.32 ], "std": [ 1.91, 1.10 ], "fq": 50 
  },
  "estimates": {
    "dict": "happiness", "word": "estimates", "stem": "estim",
    "avg": [ 5.86, 5.32 ], "std": [ 1.81, 1.11 ], "fq": 50 
  },
  "firm": {
    "dict": "happiness", "word": "firm", "stem": "firm",
    "avg": [ 4.56, 5.32 ], "std": [ 2.41, 1.17 ], "fq": 50 
  },
  "identified": {
    "dict": "happiness", "word": "identified", "stem": "identifi",
    "avg": [ 4.25, 5.32 ], "std": [ 2.47, 1.27 ], "fq": 50 
  },
  "measure": {
    "dict": "happiness", "word": "measure", "stem": "measur",
    "avg": [ 5.00, 5.32 ], "std": [ 2.83, 1.10 ], "fq": 50 
  },
  "mention": {
    "dict": "happiness", "word": "mention", "stem": "mention",
    "avg": [ 4.25, 5.32 ], "std": [ 2.47, 0.74 ], "fq": 50 
  },
  "names": {
    "dict": "happiness", "word": "names", "stem": "name",
    "avg": [ 4.25, 5.32 ], "std": [ 2.47, 1.00 ], "fq": 50 
  },
  "partly": {
    "dict": "happiness", "word": "partly", "stem": "partli",
    "avg": [ 3.82, 5.32 ], "std": [ 2.24, 1.17 ], "fq": 50 
  },
  "posts": {
    "dict": "happiness", "word": "posts", "stem": "post",
    "avg": [ 4.08, 5.32 ], "std": [ 1.92, 1.11 ], "fq": 50 
  },
  "rebounds": {
    "dict": "happiness", "word": "rebounds", "stem": "rebound",
    "avg": [ 5.67, 5.32 ], "std": [ 2.51, 1.32 ], "fq": 50 
  },
  "reserve": {
    "dict": "happiness", "word": "reserve", "stem": "reserv",
    "avg": [ 3.27, 5.32 ], "std": [ 2.05, 1.11 ], "fq": 50 
  },
  "review": {
    "dict": "happiness", "word": "review", "stem": "review",
    "avg": [ 4.45, 5.32 ], "std": [ 2.70, 1.02 ], "fq": 50 
  },
  "skip": {
    "dict": "happiness", "word": "skip", "stem": "skip",
    "avg": [ 5.00, 5.32 ], "std": [ 2.32, 1.46 ], "fq": 50 
  },
  "step": {
    "dict": "happiness", "word": "step", "stem": "step",
    "avg": [ 6.83, 5.32 ], "std": [ 2.70, 0.87 ], "fq": 50 
  },
  "table": {
    "dict": "happiness", "word": "table", "stem": "tabl",
    "avg": [ 2.92, 5.32 ], "std": [ 2.16, 0.68 ], "fq": 50 
  },
  "taking": {
    "dict": "happiness", "word": "taking", "stem": "take",
    "avg": [ 5.39, 5.32 ], "std": [ 2.22, 1.30 ], "fq": 50 
  },
  "tells": {
    "dict": "happiness", "word": "tells", "stem": "tell",
    "avg": [ 5.26, 5.32 ], "std": [ 2.36, 1.27 ], "fq": 50 
  },
  "turning": {
    "dict": "happiness", "word": "turning", "stem": "turn",
    "avg": [ 4.07, 5.32 ], "std": [ 2.34, 1.02 ], "fq": 50 
  },
  "affecting": {
    "dict": "happiness", "word": "affecting", "stem": "affect",
    "avg": [ 6.21, 5.31 ], "std": [ 2.75, 1.33 ], "fq": 50 
  },
  "consume": {
    "dict": "happiness", "word": "consume", "stem": "consum",
    "avg": [ 4.14, 5.31 ], "std": [ 2.30, 1.88 ], "fq": 50 
  },
  "discipline": {
    "dict": "happiness", "word": "discipline", "stem": "disciplin",
    "avg": [ 4.08, 5.31 ], "std": [ 2.41, 1.81 ], "fq": 50 
  },
  "heed": {
    "dict": "happiness", "word": "heed", "stem": "heed",
    "avg": [ 5.00, 5.31 ], "std": [ 2.68, 1.21 ], "fq": 50 
  },
  "aire": {
    "dict": "happiness", "word": "aire", "stem": "air",
    "avg": [ 4.12, 5.30 ], "std": [ 2.30, 1.42 ], "fq": 50 
  },
  "center": {
    "dict": "happiness", "word": "center", "stem": "center",
    "avg": [ 6.34, 5.30 ], "std": [ 2.25, 0.99 ], "fq": 50 
  },
  "chairman": {
    "dict": "happiness", "word": "chairman", "stem": "chairman",
    "avg": [ 3.15, 5.30 ], "std": [ 1.77, 1.47 ], "fq": 50 
  },
  "circuits": {
    "dict": "happiness", "word": "circuits", "stem": "circuit",
    "avg": [ 3.86, 5.30 ], "std": [ 2.13, 0.76 ], "fq": 50 
  },
  "creature": {
    "dict": "happiness", "word": "creature", "stem": "creatur",
    "avg": [ 4.33, 5.30 ], "std": [ 1.78, 1.64 ], "fq": 50 
  },
  "editing": {
    "dict": "happiness", "word": "editing", "stem": "edit",
    "avg": [ 5.00, 5.30 ], "std": [ 2.32, 1.23 ], "fq": 50 
  },
  "elevator": {
    "dict": "happiness", "word": "elevator", "stem": "elev",
    "avg": [ 4.16, 5.30 ], "std": [ 1.99, 1.39 ], "fq": 50 
  },
  "lesson": {
    "dict": "happiness", "word": "lesson", "stem": "lesson",
    "avg": [ 4.49, 5.30 ], "std": [ 2.28, 1.49 ], "fq": 50 
  },
  "md": {
    "dict": "happiness", "word": "md", "stem": "md",
    "avg": [ 5.86, 5.30 ], "std": [ 2.70, 1.13 ], "fq": 50 
  },
  "miles": {
    "dict": "happiness", "word": "miles", "stem": "mile",
    "avg": [ 4.07, 5.30 ], "std": [ 2.15, 1.17 ], "fq": 50 
  },
  "patch": {
    "dict": "happiness", "word": "patch", "stem": "patch",
    "avg": [ 3.90, 5.30 ], "std": [ 2.07, 1.04 ], "fq": 50 
  },
  "pay": {
    "dict": "happiness", "word": "pay", "stem": "pay",
    "avg": [ 5.23, 5.30 ], "std": [ 2.21, 2.32 ], "fq": 50 
  },
  "placed": {
    "dict": "happiness", "word": "placed", "stem": "place",
    "avg": [ 5.12, 5.30 ], "std": [ 2.42, 1.56 ], "fq": 50 
  },
  "pounds": {
    "dict": "happiness", "word": "pounds", "stem": "pound",
    "avg": [ 4.58, 5.30 ], "std": [ 2.02, 1.82 ], "fq": 50 
  },
  "randy": {
    "dict": "happiness", "word": "randy", "stem": "randi",
    "avg": [ 6.63, 5.30 ], "std": [ 2.70, 1.36 ], "fq": 50 
  },
  "reviews": {
    "dict": "happiness", "word": "reviews", "stem": "review",
    "avg": [ 4.45, 5.30 ], "std": [ 2.70, 1.22 ], "fq": 50 
  },
  "silly": {
    "dict": "happiness", "word": "silly", "stem": "silli",
    "avg": [ 5.88, 5.30 ], "std": [ 2.38, 1.98 ], "fq": 50 
  },
  "singular": {
    "dict": "happiness", "word": "singular", "stem": "singular",
    "avg": [ 4.27, 5.30 ], "std": [ 2.46, 1.45 ], "fq": 50 
  },
  "somebody": {
    "dict": "happiness", "word": "somebody", "stem": "somebodi",
    "avg": [ 4.19, 5.30 ], "std": [ 2.45, 1.13 ], "fq": 50 
  },
  "someone": {
    "dict": "happiness", "word": "someone", "stem": "someon",
    "avg": [ 4.19, 5.30 ], "std": [ 2.45, 1.17 ], "fq": 50 
  },
  "spray": {
    "dict": "happiness", "word": "spray", "stem": "spray",
    "avg": [ 4.14, 5.30 ], "std": [ 2.28, 1.45 ], "fq": 50 
  },
  "suit": {
    "dict": "happiness", "word": "suit", "stem": "suit",
    "avg": [ 4.93, 5.30 ], "std": [ 2.44, 1.58 ], "fq": 50 
  },
  "telling": {
    "dict": "happiness", "word": "telling", "stem": "tell",
    "avg": [ 5.26, 5.30 ], "std": [ 2.36, 1.05 ], "fq": 50 
  },
  "transition": {
    "dict": "happiness", "word": "transition", "stem": "transit",
    "avg": [ 4.36, 5.30 ], "std": [ 2.13, 1.36 ], "fq": 50 
  },
  "trump": {
    "dict": "happiness", "word": "trump", "stem": "trump",
    "avg": [ 4.97, 5.30 ], "std": [ 2.13, 1.71 ], "fq": 50 
  },
  "ways": {
    "dict": "happiness", "word": "ways", "stem": "way",
    "avg": [ 4.56, 5.30 ], "std": [ 1.78, 1.17 ], "fq": 50 
  },
  "heel": {
    "dict": "happiness", "word": "heel", "stem": "heel",
    "avg": [ 5.76, 5.29 ], "std": [ 2.50, 1.35 ], "fq": 50 
  },
  "alert": {
    "dict": "happiness", "word": "alert", "stem": "alert",
    "avg": [ 6.85, 5.28 ], "std": [ 2.53, 1.81 ], "fq": 50 
  },
  "beef": {
    "dict": "happiness", "word": "beef", "stem": "beef",
    "avg": [ 5.00, 5.28 ], "std": [ 2.19, 2.18 ], "fq": 50 
  },
  "defended": {
    "dict": "happiness", "word": "defended", "stem": "defend",
    "avg": [ 5.85, 5.28 ], "std": [ 3.15, 1.76 ], "fq": 50 
  },
  "extract": {
    "dict": "happiness", "word": "extract", "stem": "extract",
    "avg": [ 5.74, 5.28 ], "std": [ 2.46, 1.46 ], "fq": 50 
  },
  "form": {
    "dict": "happiness", "word": "form", "stem": "form",
    "avg": [ 5.67, 5.28 ], "std": [ 2.51, 1.11 ], "fq": 50 
  },
  "handling": {
    "dict": "happiness", "word": "handling", "stem": "handl",
    "avg": [ 5.62, 5.28 ], "std": [ 2.25, 1.09 ], "fq": 50 
  },
  "happen": {
    "dict": "happiness", "word": "happen", "stem": "happen",
    "avg": [ 4.05, 5.28 ], "std": [ 2.34, 1.05 ], "fq": 50 
  },
  "held": {
    "dict": "happiness", "word": "held", "stem": "held",
    "avg": [ 6.10, 5.28 ], "std": [ 2.19, 1.28 ], "fq": 50 
  },
  "institute": {
    "dict": "happiness", "word": "institute", "stem": "institut",
    "avg": [ 3.62, 5.28 ], "std": [ 2.25, 1.41 ], "fq": 50 
  },
  "james": {
    "dict": "happiness", "word": "james", "stem": "jame",
    "avg": [ 5.52, 5.28 ], "std": [ 2.87, 1.07 ], "fq": 50 
  },
  "minutes": {
    "dict": "happiness", "word": "minutes", "stem": "minut",
    "avg": [ 3.83, 5.28 ], "std": [ 2.29, 0.90 ], "fq": 50 
  },
  "mode": {
    "dict": "happiness", "word": "mode", "stem": "mode",
    "avg": [ 4.56, 5.28 ], "std": [ 1.78, 1.18 ], "fq": 50 
  },
  "section": {
    "dict": "happiness", "word": "section", "stem": "section",
    "avg": [ 3.82, 5.28 ], "std": [ 2.24, 0.83 ], "fq": 50 
  },
  "sort": {
    "dict": "happiness", "word": "sort", "stem": "sort",
    "avg": [ 4.30, 5.28 ], "std": [ 2.62, 0.83 ], "fq": 50 
  },
  "stands": {
    "dict": "happiness", "word": "stands", "stem": "stand",
    "avg": [ 3.93, 5.28 ], "std": [ 2.49, 0.88 ], "fq": 50 
  },
  "stays": {
    "dict": "happiness", "word": "stays", "stem": "stay",
    "avg": [ 5.62, 5.28 ], "std": [ 2.39, 1.31 ], "fq": 50 
  },
  "tracks": {
    "dict": "happiness", "word": "tracks", "stem": "track",
    "avg": [ 5.76, 5.28 ], "std": [ 2.50, 1.11 ], "fq": 50 
  },
  "unions": {
    "dict": "happiness", "word": "unions", "stem": "union",
    "avg": [ 3.75, 5.28 ], "std": [ 2.49, 1.65 ], "fq": 50 
  },
  "wandering": {
    "dict": "happiness", "word": "wandering", "stem": "wander",
    "avg": [ 5.00, 5.28 ], "std": [ 2.18, 1.73 ], "fq": 50 
  },
  "agency": {
    "dict": "happiness", "word": "agency", "stem": "agenc",
    "avg": [ 4.08, 5.26 ], "std": [ 1.92, 0.92 ], "fq": 50 
  },
  "bid": {
    "dict": "happiness", "word": "bid", "stem": "bid",
    "avg": [ 5.16, 5.26 ], "std": [ 2.62, 1.19 ], "fq": 50 
  },
  "companies": {
    "dict": "happiness", "word": "companies", "stem": "compani",
    "avg": [ 6.69, 5.26 ], "std": [ 2.84, 1.03 ], "fq": 50 
  },
  "facility": {
    "dict": "happiness", "word": "facility", "stem": "facil",
    "avg": [ 6.57, 5.26 ], "std": [ 1.78, 1.59 ], "fq": 50 
  },
  "facing": {
    "dict": "happiness", "word": "facing", "stem": "face",
    "avg": [ 5.04, 5.26 ], "std": [ 2.18, 1.10 ], "fq": 50 
  },
  "frog": {
    "dict": "happiness", "word": "frog", "stem": "frog",
    "avg": [ 4.54, 5.26 ], "std": [ 2.03, 1.80 ], "fq": 50 
  },
  "goes": {
    "dict": "happiness", "word": "goes", "stem": "goe",
    "avg": [ 7.38, 5.26 ], "std": [ 1.92, 1.12 ], "fq": 50 
  },
  "ground": {
    "dict": "happiness", "word": "ground", "stem": "ground",
    "avg": [ 4.58, 5.26 ], "std": [ 2.14, 1.29 ], "fq": 50 
  },
  "lines": {
    "dict": "happiness", "word": "lines", "stem": "line",
    "avg": [ 4.98, 5.26 ], "std": [ 2.52, 1.01 ], "fq": 50 
  },
  "nearly": {
    "dict": "happiness", "word": "nearly", "stem": "nearli",
    "avg": [ 6.98, 5.26 ], "std": [ 2.21, 1.24 ], "fq": 50 
  },
  "papers": {
    "dict": "happiness", "word": "papers", "stem": "paper",
    "avg": [ 2.50, 5.26 ], "std": [ 1.85, 1.31 ], "fq": 50 
  },
  "piece": {
    "dict": "happiness", "word": "piece", "stem": "piec",
    "avg": [ 3.82, 5.26 ], "std": [ 2.24, 1.07 ], "fq": 50 
  },
  "plot": {
    "dict": "happiness", "word": "plot", "stem": "plot",
    "avg": [ 5.89, 5.26 ], "std": [ 2.37, 1.38 ], "fq": 50 
  },
  "print": {
    "dict": "happiness", "word": "print", "stem": "print",
    "avg": [ 5.42, 5.26 ], "std": [ 2.65, 1.21 ], "fq": 50 
  },
  "reasons": {
    "dict": "happiness", "word": "reasons", "stem": "reason",
    "avg": [ 4.75, 5.26 ], "std": [ 2.50, 1.01 ], "fq": 50 
  },
  "shift": {
    "dict": "happiness", "word": "shift", "stem": "shift",
    "avg": [ 4.07, 5.26 ], "std": [ 1.69, 1.05 ], "fq": 50 
  },
  "spot": {
    "dict": "happiness", "word": "spot", "stem": "spot",
    "avg": [ 4.08, 5.26 ], "std": [ 1.92, 1.47 ], "fq": 50 
  },
  "tool": {
    "dict": "happiness", "word": "tool", "stem": "tool",
    "avg": [ 4.33, 5.26 ], "std": [ 1.78, 1.54 ], "fq": 50 
  },
  "units": {
    "dict": "happiness", "word": "units", "stem": "unit",
    "avg": [ 3.75, 5.26 ], "std": [ 2.49, 1.03 ], "fq": 50 
  },
  "borne": {
    "dict": "happiness", "word": "borne", "stem": "born",
    "avg": [ 5.40, 5.24 ], "std": [ 2.70, 1.38 ], "fq": 50 
  },
  "edited": {
    "dict": "happiness", "word": "edited", "stem": "edit",
    "avg": [ 5.00, 5.24 ], "std": [ 2.32, 1.14 ], "fq": 50 
  },
  "encounter": {
    "dict": "happiness", "word": "encounter", "stem": "encount",
    "avg": [ 5.38, 5.24 ], "std": [ 2.58, 1.78 ], "fq": 50 
  },
  "faced": {
    "dict": "happiness", "word": "faced", "stem": "face",
    "avg": [ 5.04, 5.24 ], "std": [ 2.18, 1.24 ], "fq": 50 
  },
  "industries": {
    "dict": "happiness", "word": "industries", "stem": "industri",
    "avg": [ 4.47, 5.24 ], "std": [ 2.43, 1.10 ], "fq": 50 
  },
  "namely": {
    "dict": "happiness", "word": "namely", "stem": "name",
    "avg": [ 4.25, 5.24 ], "std": [ 2.47, 1.27 ], "fq": 50 
  },
  "partially": {
    "dict": "happiness", "word": "partially", "stem": "partial",
    "avg": [ 3.82, 5.24 ], "std": [ 2.24, 1.30 ], "fq": 50 
  },
  "parts": {
    "dict": "happiness", "word": "parts", "stem": "part",
    "avg": [ 3.82, 5.24 ], "std": [ 2.24, 1.12 ], "fq": 50 
  },
  "returns": {
    "dict": "happiness", "word": "returns", "stem": "return",
    "avg": [ 4.70, 5.24 ], "std": [ 2.48, 1.51 ], "fq": 50 
  },
  "sat": {
    "dict": "happiness", "word": "sat", "stem": "sat",
    "avg": [ 2.95, 5.24 ], "std": [ 1.72, 1.33 ], "fq": 50 
  },
  "sorts": {
    "dict": "happiness", "word": "sorts", "stem": "sort",
    "avg": [ 4.30, 5.24 ], "std": [ 2.62, 0.94 ], "fq": 50 
  },
  "substances": {
    "dict": "happiness", "word": "substances", "stem": "substanc",
    "avg": [ 6.34, 5.24 ], "std": [ 2.25, 1.30 ], "fq": 50 
  },
  "ties": {
    "dict": "happiness", "word": "ties", "stem": "tie",
    "avg": [ 5.97, 5.24 ], "std": [ 2.85, 1.45 ], "fq": 50 
  },
  "turned": {
    "dict": "happiness", "word": "turned", "stem": "turn",
    "avg": [ 4.07, 5.24 ], "std": [ 2.34, 0.85 ], "fq": 50 
  },
  "way": {
    "dict": "happiness", "word": "way", "stem": "way",
    "avg": [ 4.56, 5.24 ], "std": [ 1.78, 1.42 ], "fq": 50 
  },
  "wee": {
    "dict": "happiness", "word": "wee", "stem": "wee",
    "avg": [ 4.20, 5.24 ], "std": [ 2.18, 1.52 ], "fq": 50 
  },
  "work": {
    "dict": "happiness", "word": "work", "stem": "work",
    "avg": [ 4.07, 5.24 ], "std": [ 1.98, 2.10 ], "fq": 50 
  },
  "bits": {
    "dict": "happiness", "word": "bits", "stem": "bit",
    "avg": [ 3.83, 5.22 ], "std": [ 2.29, 0.86 ], "fq": 50 
  },
  "cause": {
    "dict": "happiness", "word": "cause", "stem": "caus",
    "avg": [ 4.93, 5.22 ], "std": [ 2.44, 1.06 ], "fq": 50 
  },
  "defend": {
    "dict": "happiness", "word": "defend", "stem": "defend",
    "avg": [ 5.85, 5.22 ], "std": [ 3.15, 1.72 ], "fq": 50 
  },
  "defending": {
    "dict": "happiness", "word": "defending", "stem": "defend",
    "avg": [ 5.85, 5.22 ], "std": [ 3.15, 1.50 ], "fq": 50 
  },
  "nets": {
    "dict": "happiness", "word": "nets", "stem": "net",
    "avg": [ 6.68, 5.22 ], "std": [ 1.78, 0.93 ], "fq": 50 
  },
  "officer": {
    "dict": "happiness", "word": "officer", "stem": "offic",
    "avg": [ 4.08, 5.22 ], "std": [ 1.92, 1.64 ], "fq": 50 
  },
  "pump": {
    "dict": "happiness", "word": "pump", "stem": "pump",
    "avg": [ 6.34, 5.22 ], "std": [ 2.25, 1.07 ], "fq": 50 
  },
  "sentence": {
    "dict": "happiness", "word": "sentence", "stem": "sentenc",
    "avg": [ 4.64, 5.22 ], "std": [ 2.75, 1.45 ], "fq": 50 
  },
  "swallow": {
    "dict": "happiness", "word": "swallow", "stem": "swallow",
    "avg": [ 5.40, 5.22 ], "std": [ 2.70, 1.58 ], "fq": 50 
  },
  "trance": {
    "dict": "happiness", "word": "trance", "stem": "tranc",
    "avg": [ 5.83, 5.22 ], "std": [ 2.73, 1.72 ], "fq": 50 
  },
  "trick": {
    "dict": "happiness", "word": "trick", "stem": "trick",
    "avg": [ 5.95, 5.22 ], "std": [ 2.36, 1.67 ], "fq": 50 
  },
  "masses": {
    "dict": "happiness", "word": "masses", "stem": "mass",
    "avg": [ 5.49, 5.21 ], "std": [ 2.43, 1.32 ], "fq": 50 
  },
  "twist": {
    "dict": "happiness", "word": "twist", "stem": "twist",
    "avg": [ 6.26, 5.21 ], "std": [ 2.61, 1.38 ], "fq": 50 
  },
  "alcohol": {
    "dict": "happiness", "word": "alcohol", "stem": "alcohol",
    "avg": [ 5.69, 5.20 ], "std": [ 2.36, 2.32 ], "fq": 50 
  },
  "cab": {
    "dict": "happiness", "word": "cab", "stem": "cab",
    "avg": [ 3.41, 5.20 ], "std": [ 2.14, 1.53 ], "fq": 50 
  },
  "checking": {
    "dict": "happiness", "word": "checking", "stem": "check",
    "avg": [ 6.10, 5.20 ], "std": [ 2.19, 1.37 ], "fq": 50 
  },
  "happens": {
    "dict": "happiness", "word": "happens", "stem": "happen",
    "avg": [ 4.05, 5.20 ], "std": [ 2.34, 1.21 ], "fq": 50 
  },
  "internal": {
    "dict": "happiness", "word": "internal", "stem": "intern",
    "avg": [ 6.98, 5.20 ], "std": [ 2.21, 1.31 ], "fq": 50 
  },
  "jaw": {
    "dict": "happiness", "word": "jaw", "stem": "jaw",
    "avg": [ 5.74, 5.20 ], "std": [ 2.38, 1.34 ], "fq": 50 
  },
  "lightning": {
    "dict": "happiness", "word": "lightning", "stem": "lightn",
    "avg": [ 6.61, 5.20 ], "std": [ 1.77, 1.88 ], "fq": 50 
  },
  "loads": {
    "dict": "happiness", "word": "loads", "stem": "load",
    "avg": [ 5.63, 5.20 ], "std": [ 2.07, 1.21 ], "fq": 50 
  },
  "marketing": {
    "dict": "happiness", "word": "marketing", "stem": "market",
    "avg": [ 4.12, 5.20 ], "std": [ 1.83, 1.95 ], "fq": 50 
  },
  "percentage": {
    "dict": "happiness", "word": "percentage", "stem": "percentag",
    "avg": [ 3.82, 5.20 ], "std": [ 2.24, 0.81 ], "fq": 50 
  },
  "physicians": {
    "dict": "happiness", "word": "physicians", "stem": "physician",
    "avg": [ 5.86, 5.20 ], "std": [ 2.70, 1.65 ], "fq": 50 
  },
  "retiring": {
    "dict": "happiness", "word": "retiring", "stem": "retir",
    "avg": [ 3.61, 5.20 ], "std": [ 2.56, 2.16 ], "fq": 50 
  },
  "return": {
    "dict": "happiness", "word": "return", "stem": "return",
    "avg": [ 4.70, 5.20 ], "std": [ 2.48, 1.47 ], "fq": 50 
  },
  "sections": {
    "dict": "happiness", "word": "sections", "stem": "section",
    "avg": [ 3.82, 5.20 ], "std": [ 2.24, 1.17 ], "fq": 50 
  },
  "snap": {
    "dict": "happiness", "word": "snap", "stem": "snap",
    "avg": [ 4.37, 5.20 ], "std": [ 2.32, 1.63 ], "fq": 50 
  },
  "tighter": {
    "dict": "happiness", "word": "tighter", "stem": "tighter",
    "avg": [ 4.89, 5.20 ], "std": [ 2.50, 1.44 ], "fq": 50 
  },
  "tires": {
    "dict": "happiness", "word": "tires", "stem": "tire",
    "avg": [ 2.83, 5.20 ], "std": [ 2.31, 1.37 ], "fq": 50 
  },
  "turn": {
    "dict": "happiness", "word": "turn", "stem": "turn",
    "avg": [ 4.07, 5.20 ], "std": [ 2.34, 1.25 ], "fq": 50 
  },
  "turns": {
    "dict": "happiness", "word": "turns", "stem": "turn",
    "avg": [ 4.07, 5.20 ], "std": [ 2.34, 0.90 ], "fq": 50 
  },
  "back": {
    "dict": "happiness", "word": "back", "stem": "back",
    "avg": [ 4.12, 5.18 ], "std": [ 2.01, 1.24 ], "fq": 50 
  },
  "basement": {
    "dict": "happiness", "word": "basement", "stem": "basement",
    "avg": [ 4.39, 5.18 ], "std": [ 2.33, 1.02 ], "fq": 50 
  },
  "blowing": {
    "dict": "happiness", "word": "blowing", "stem": "blow",
    "avg": [ 4.14, 5.18 ], "std": [ 2.30, 1.59 ], "fq": 50 
  },
  "boards": {
    "dict": "happiness", "word": "boards", "stem": "board",
    "avg": [ 3.36, 5.18 ], "std": [ 2.12, 1.08 ], "fq": 50 
  },
  "claim": {
    "dict": "happiness", "word": "claim", "stem": "claim",
    "avg": [ 5.65, 5.18 ], "std": [ 2.23, 1.49 ], "fq": 50 
  },
  "collar": {
    "dict": "happiness", "word": "collar", "stem": "collar",
    "avg": [ 4.59, 5.18 ], "std": [ 2.10, 1.32 ], "fq": 50 
  },
  "context": {
    "dict": "happiness", "word": "context", "stem": "context",
    "avg": [ 4.22, 5.18 ], "std": [ 2.24, 0.96 ], "fq": 50 
  },
  "existing": {
    "dict": "happiness", "word": "existing", "stem": "exist",
    "avg": [ 5.53, 5.18 ], "std": [ 2.90, 1.67 ], "fq": 50 
  },
  "horn": {
    "dict": "happiness", "word": "horn", "stem": "horn",
    "avg": [ 4.97, 5.18 ], "std": [ 2.13, 1.42 ], "fq": 50 
  },
  "month": {
    "dict": "happiness", "word": "month", "stem": "month",
    "avg": [ 4.03, 5.18 ], "std": [ 1.77, 1.34 ], "fq": 50 
  },
  "notion": {
    "dict": "happiness", "word": "notion", "stem": "notion",
    "avg": [ 5.42, 5.18 ], "std": [ 2.65, 1.32 ], "fq": 50 
  },
  "penis": {
    "dict": "happiness", "word": "penis", "stem": "peni",
    "avg": [ 5.54, 5.18 ], "std": [ 2.63, 1.96 ], "fq": 50 
  },
  "plug": {
    "dict": "happiness", "word": "plug", "stem": "plug",
    "avg": [ 3.14, 5.18 ], "std": [ 2.47, 1.02 ], "fq": 50 
  },
  "public": {
    "dict": "happiness", "word": "public", "stem": "public",
    "avg": [ 5.32, 5.18 ], "std": [ 2.39, 1.37 ], "fq": 50 
  },
  "returned": {
    "dict": "happiness", "word": "returned", "stem": "return",
    "avg": [ 4.70, 5.18 ], "std": [ 2.48, 1.44 ], "fq": 50 
  },
  "stepped": {
    "dict": "happiness", "word": "stepped", "stem": "step",
    "avg": [ 6.83, 5.18 ], "std": [ 2.70, 1.27 ], "fq": 50 
  },
  "take": {
    "dict": "happiness", "word": "take", "stem": "take",
    "avg": [ 5.39, 5.18 ], "std": [ 2.22, 1.51 ], "fq": 50 
  },
  "urge": {
    "dict": "happiness", "word": "urge", "stem": "urg",
    "avg": [ 6.02, 5.18 ], "std": [ 2.67, 1.30 ], "fq": 50 
  },
  "spine": {
    "dict": "happiness", "word": "spine", "stem": "spine",
    "avg": [ 5.14, 5.16 ], "std": [ 2.14, 1.28 ], "fq": 50 
  },
  "dos": {
    "dict": "happiness", "word": "dos", "stem": "do",
    "avg": [ 5.71, 5.16 ], "std": [ 2.74, 1.33 ], "fq": 50 
  },
  "effect": {
    "dict": "happiness", "word": "effect", "stem": "effect",
    "avg": [ 5.42, 5.16 ], "std": [ 2.65, 1.09 ], "fq": 50 
  },
  "floor": {
    "dict": "happiness", "word": "floor", "stem": "floor",
    "avg": [ 4.12, 5.16 ], "std": [ 2.36, 1.25 ], "fq": 50 
  },
  "locker": {
    "dict": "happiness", "word": "locker", "stem": "locker",
    "avg": [ 3.38, 5.16 ], "std": [ 2.13, 0.96 ], "fq": 50 
  },
  "months": {
    "dict": "happiness", "word": "months", "stem": "month",
    "avg": [ 4.03, 5.16 ], "std": [ 1.77, 0.87 ], "fq": 50 
  },
  "notice": {
    "dict": "happiness", "word": "notice", "stem": "notic",
    "avg": [ 3.93, 5.16 ], "std": [ 2.56, 1.50 ], "fq": 50 
  },
  "ones": {
    "dict": "happiness", "word": "ones", "stem": "one",
    "avg": [ 5.50, 5.16 ], "std": [ 2.66, 0.82 ], "fq": 50 
  },
  "remaining": {
    "dict": "happiness", "word": "remaining", "stem": "remain",
    "avg": [ 4.27, 5.16 ], "std": [ 2.46, 1.28 ], "fq": 50 
  },
  "wears": {
    "dict": "happiness", "word": "wears", "stem": "wear",
    "avg": [ 2.64, 5.16 ], "std": [ 2.19, 0.98 ], "fq": 50 
  },
  "posterior": {
    "dict": "happiness", "word": "posterior", "stem": "posterior",
    "avg": [ 2.95, 5.15 ], "std": [ 1.72, 1.44 ], "fq": 50 
  },
  "bearing": {
    "dict": "happiness", "word": "bearing", "stem": "bear",
    "avg": [ 5.40, 5.14 ], "std": [ 2.70, 1.53 ], "fq": 50 
  },
  "firms": {
    "dict": "happiness", "word": "firms", "stem": "firm",
    "avg": [ 4.56, 5.14 ], "std": [ 2.41, 1.18 ], "fq": 50 
  },
  "hypnotized": {
    "dict": "happiness", "word": "hypnotized", "stem": "hypnot",
    "avg": [ 5.83, 5.14 ], "std": [ 2.73, 1.46 ], "fq": 50 
  },
  "lesbian": {
    "dict": "happiness", "word": "lesbian", "stem": "lesbian",
    "avg": [ 5.12, 5.14 ], "std": [ 2.27, 2.11 ], "fq": 50 
  },
  "operated": {
    "dict": "happiness", "word": "operated", "stem": "oper",
    "avg": [ 6.77, 5.14 ], "std": [ 2.07, 1.31 ], "fq": 50 
  },
  "region": {
    "dict": "happiness", "word": "region", "stem": "region",
    "avg": [ 3.82, 5.14 ], "std": [ 2.24, 1.14 ], "fq": 50 
  },
  "retired": {
    "dict": "happiness", "word": "retired", "stem": "retir",
    "avg": [ 3.61, 5.14 ], "std": [ 2.56, 1.95 ], "fq": 50 
  },
  "shake": {
    "dict": "happiness", "word": "shake", "stem": "shake",
    "avg": [ 7.67, 5.14 ], "std": [ 1.91, 1.20 ], "fq": 50 
  },
  "silence": {
    "dict": "happiness", "word": "silence", "stem": "silenc",
    "avg": [ 2.82, 5.14 ], "std": [ 2.13, 1.74 ], "fq": 50 
  },
  "still": {
    "dict": "happiness", "word": "still", "stem": "still",
    "avg": [ 4.91, 5.14 ], "std": [ 2.57, 1.12 ], "fq": 50 
  },
  "supposed": {
    "dict": "happiness", "word": "supposed", "stem": "suppos",
    "avg": [ 5.98, 5.14 ], "std": [ 2.14, 1.12 ], "fq": 50 
  },
  "track": {
    "dict": "happiness", "word": "track", "stem": "track",
    "avg": [ 5.76, 5.14 ], "std": [ 2.50, 1.14 ], "fq": 50 
  },
  "wet": {
    "dict": "happiness", "word": "wet", "stem": "wet",
    "avg": [ 4.02, 5.14 ], "std": [ 2.41, 1.41 ], "fq": 50 
  },
  "yearning": {
    "dict": "happiness", "word": "yearning", "stem": "yearn",
    "avg": [ 5.00, 5.14 ], "std": [ 2.45, 1.57 ], "fq": 50 
  },
  "ankle": {
    "dict": "happiness", "word": "ankle", "stem": "ankl",
    "avg": [ 4.16, 5.12 ], "std": [ 2.03, 0.82 ], "fq": 50 
  },
  "backed": {
    "dict": "happiness", "word": "backed", "stem": "back",
    "avg": [ 5.89, 5.12 ], "std": [ 2.37, 1.38 ], "fq": 50 
  },
  "bare": {
    "dict": "happiness", "word": "bare", "stem": "bare",
    "avg": [ 5.80, 5.12 ], "std": [ 2.80, 1.72 ], "fq": 50 
  },
  "cell": {
    "dict": "happiness", "word": "cell", "stem": "cell",
    "avg": [ 4.08, 5.12 ], "std": [ 2.19, 1.41 ], "fq": 50 
  },
  "contained": {
    "dict": "happiness", "word": "contained", "stem": "contain",
    "avg": [ 6.10, 5.12 ], "std": [ 2.19, 1.36 ], "fq": 50 
  },
  "cops": {
    "dict": "happiness", "word": "cops", "stem": "cop",
    "avg": [ 4.20, 5.12 ], "std": [ 2.42, 1.85 ], "fq": 50 
  },
  "crush": {
    "dict": "happiness", "word": "crush", "stem": "crush",
    "avg": [ 5.52, 5.12 ], "std": [ 2.87, 1.75 ], "fq": 50 
  },
  "office": {
    "dict": "happiness", "word": "office", "stem": "offic",
    "avg": [ 4.08, 5.12 ], "std": [ 1.92, 1.62 ], "fq": 50 
  },
  "rear": {
    "dict": "happiness", "word": "rear", "stem": "rear",
    "avg": [ 2.95, 5.12 ], "std": [ 1.72, 1.47 ], "fq": 50 
  },
  "rounds": {
    "dict": "happiness", "word": "rounds", "stem": "round",
    "avg": [ 3.86, 5.12 ], "std": [ 2.13, 1.02 ], "fq": 50 
  },
  "shadows": {
    "dict": "happiness", "word": "shadows", "stem": "shadow",
    "avg": [ 4.30, 5.12 ], "std": [ 2.26, 1.73 ], "fq": 50 
  },
  "side": {
    "dict": "happiness", "word": "side", "stem": "side",
    "avg": [ 5.04, 5.12 ], "std": [ 2.18, 0.72 ], "fq": 50 
  },
  "single": {
    "dict": "happiness", "word": "single", "stem": "singl",
    "avg": [ 5.50, 5.12 ], "std": [ 2.66, 1.52 ], "fq": 50 
  },
  "wander": {
    "dict": "happiness", "word": "wander", "stem": "wander",
    "avg": [ 7.24, 5.12 ], "std": [ 2.06, 1.64 ], "fq": 50 
  },
  "bases": {
    "dict": "happiness", "word": "bases", "stem": "base",
    "avg": [ 3.27, 5.10 ], "std": [ 1.98, 1.04 ], "fq": 50 
  },
  "butt": {
    "dict": "happiness", "word": "butt", "stem": "butt",
    "avg": [ 2.95, 5.10 ], "std": [ 1.72, 1.85 ], "fq": 50 
  },
  "cells": {
    "dict": "happiness", "word": "cells", "stem": "cell",
    "avg": [ 4.08, 5.10 ], "std": [ 2.19, 1.40 ], "fq": 50 
  },
  "circuit": {
    "dict": "happiness", "word": "circuit", "stem": "circuit",
    "avg": [ 3.86, 5.10 ], "std": [ 2.13, 1.25 ], "fq": 50 
  },
  "cliff": {
    "dict": "happiness", "word": "cliff", "stem": "cliff",
    "avg": [ 6.25, 5.10 ], "std": [ 2.15, 1.53 ], "fq": 50 
  },
  "consumption": {
    "dict": "happiness", "word": "consumption", "stem": "consumpt",
    "avg": [ 4.26, 5.10 ], "std": [ 2.47, 1.80 ], "fq": 50 
  },
  "dealt": {
    "dict": "happiness", "word": "dealt", "stem": "dealt",
    "avg": [ 5.62, 5.10 ], "std": [ 2.25, 1.25 ], "fq": 50 
  },
  "lists": {
    "dict": "happiness", "word": "lists", "stem": "list",
    "avg": [ 4.25, 5.10 ], "std": [ 2.47, 1.37 ], "fq": 50 
  },
  "mans": {
    "dict": "happiness", "word": "mans", "stem": "man",
    "avg": [ 5.24, 5.10 ], "std": [ 2.31, 1.39 ], "fq": 50 
  },
  "marks": {
    "dict": "happiness", "word": "marks", "stem": "mark",
    "avg": [ 4.79, 5.10 ], "std": [ 2.11, 1.43 ], "fq": 50 
  },
  "merger": {
    "dict": "happiness", "word": "merger", "stem": "merger",
    "avg": [ 3.75, 5.10 ], "std": [ 2.49, 1.02 ], "fq": 50 
  },
  "obey": {
    "dict": "happiness", "word": "obey", "stem": "obey",
    "avg": [ 4.23, 5.10 ], "std": [ 1.72, 1.88 ], "fq": 50 
  },
  "pin": {
    "dict": "happiness", "word": "pin", "stem": "pin",
    "avg": [ 4.60, 5.10 ], "std": [ 2.35, 0.89 ], "fq": 50 
  },
  "puts": {
    "dict": "happiness", "word": "puts", "stem": "put",
    "avg": [ 5.12, 5.10 ], "std": [ 2.42, 0.65 ], "fq": 50 
  },
  "stack": {
    "dict": "happiness", "word": "stack", "stem": "stack",
    "avg": [ 5.49, 5.10 ], "std": [ 2.43, 1.13 ], "fq": 50 
  },
  "wolf": {
    "dict": "happiness", "word": "wolf", "stem": "wolf",
    "avg": [ 5.57, 5.10 ], "std": [ 2.61, 1.81 ], "fq": 50 
  },
  "hump": {
    "dict": "happiness", "word": "hump", "stem": "hump",
    "avg": [ 6.38, 5.08 ], "std": [ 2.68, 1.74 ], "fq": 50 
  },
  "trace": {
    "dict": "happiness", "word": "trace", "stem": "trace",
    "avg": [ 4.30, 5.08 ], "std": [ 2.26, 1.22 ], "fq": 50 
  },
  "assuming": {
    "dict": "happiness", "word": "assuming", "stem": "assum",
    "avg": [ 5.40, 5.08 ], "std": [ 2.70, 1.41 ], "fq": 50 
  },
  "neutral": {
    "dict": "happiness", "word": "neutral", "stem": "neutral",
    "avg": [ 3.18, 5.08 ], "std": [ 1.85, 1.11 ], "fq": 50 
  },
  "admitted": {
    "dict": "happiness", "word": "admitted", "stem": "admit",
    "avg": [ 5.40, 5.08 ], "std": [ 2.70, 1.35 ], "fq": 50 
  },
  "base": {
    "dict": "happiness", "word": "base", "stem": "base",
    "avg": [ 3.27, 5.08 ], "std": [ 1.98, 1.05 ], "fq": 50 
  },
  "booked": {
    "dict": "happiness", "word": "booked", "stem": "book",
    "avg": [ 4.17, 5.08 ], "std": [ 2.49, 1.55 ], "fq": 50 
  },
  "buss": {
    "dict": "happiness", "word": "buss", "stem": "buss",
    "avg": [ 7.32, 5.08 ], "std": [ 2.03, 1.37 ], "fq": 50 
  },
  "cord": {
    "dict": "happiness", "word": "cord", "stem": "cord",
    "avg": [ 3.54, 5.08 ], "std": [ 2.09, 1.10 ], "fq": 50 
  },
  "john": {
    "dict": "happiness", "word": "john", "stem": "john",
    "avg": [ 3.88, 5.08 ], "std": [ 1.72, 1.16 ], "fq": 50 
  },
  "listed": {
    "dict": "happiness", "word": "listed", "stem": "list",
    "avg": [ 4.25, 5.08 ], "std": [ 2.47, 1.16 ], "fq": 50 
  },
  "medicine": {
    "dict": "happiness", "word": "medicine", "stem": "medicin",
    "avg": [ 4.40, 5.08 ], "std": [ 2.36, 1.69 ], "fq": 50 
  },
  "might": {
    "dict": "happiness", "word": "might", "stem": "might",
    "avg": [ 5.61, 5.08 ], "std": [ 2.38, 1.23 ], "fq": 50 
  },
  "noted": {
    "dict": "happiness", "word": "noted", "stem": "note",
    "avg": [ 6.55, 5.08 ], "std": [ 2.46, 1.01 ], "fq": 50 
  },
  "seconds": {
    "dict": "happiness", "word": "seconds", "stem": "second",
    "avg": [ 3.83, 5.08 ], "std": [ 2.29, 0.97 ], "fq": 50 
  },
  "sets": {
    "dict": "happiness", "word": "sets", "stem": "set",
    "avg": [ 4.05, 5.08 ], "std": [ 1.89, 1.34 ], "fq": 50 
  },
  "settle": {
    "dict": "happiness", "word": "settle", "stem": "settl",
    "avg": [ 4.70, 5.08 ], "std": [ 2.48, 1.44 ], "fq": 50 
  },
  "squeeze": {
    "dict": "happiness", "word": "squeeze", "stem": "squeez",
    "avg": [ 6.07, 5.08 ], "std": [ 2.26, 1.70 ], "fq": 50 
  },
  "tag": {
    "dict": "happiness", "word": "tag", "stem": "tag",
    "avg": [ 5.76, 5.08 ], "std": [ 2.50, 1.28 ], "fq": 50 
  },
  "told": {
    "dict": "happiness", "word": "told", "stem": "told",
    "avg": [ 5.26, 5.08 ], "std": [ 2.36, 1.38 ], "fq": 50 
  },
  "transit": {
    "dict": "happiness", "word": "transit", "stem": "transit",
    "avg": [ 4.36, 5.08 ], "std": [ 2.13, 1.21 ], "fq": 50 
  },
  "wanted": {
    "dict": "happiness", "word": "wanted", "stem": "want",
    "avg": [ 7.35, 5.08 ], "std": [ 1.76, 1.78 ], "fq": 50 
  },
  "swallowed": {
    "dict": "happiness", "word": "swallowed", "stem": "swallow",
    "avg": [ 5.40, 5.06 ], "std": [ 2.70, 1.48 ], "fq": 50 
  },
  "aus": {
    "dict": "happiness", "word": "aus", "stem": "au",
    "avg": [ 5.76, 5.06 ], "std": [ 2.79, 1.00 ], "fq": 50 
  },
  "bend": {
    "dict": "happiness", "word": "bend", "stem": "bend",
    "avg": [ 4.07, 5.06 ], "std": [ 2.34, 1.32 ], "fq": 50 
  },
  "chill": {
    "dict": "happiness", "word": "chill", "stem": "chill",
    "avg": [ 8.02, 5.06 ], "std": [ 1.65, 2.10 ], "fq": 50 
  },
  "follows": {
    "dict": "happiness", "word": "follows", "stem": "follow",
    "avg": [ 4.10, 5.06 ], "std": [ 2.12, 1.61 ], "fq": 50 
  },
  "moved": {
    "dict": "happiness", "word": "moved", "stem": "move",
    "avg": [ 5.42, 5.06 ], "std": [ 2.65, 1.24 ], "fq": 50 
  },
  "phase": {
    "dict": "happiness", "word": "phase", "stem": "phase",
    "avg": [ 3.98, 5.06 ], "std": [ 1.82, 0.98 ], "fq": 50 
  },
  "primitive": {
    "dict": "happiness", "word": "primitive", "stem": "primit",
    "avg": [ 6.31, 5.06 ], "std": [ 2.47, 1.54 ], "fq": 50 
  },
  "rattle": {
    "dict": "happiness", "word": "rattle", "stem": "rattl",
    "avg": [ 4.36, 5.06 ], "std": [ 2.18, 1.54 ], "fq": 50 
  },
  "ruth": {
    "dict": "happiness", "word": "ruth", "stem": "ruth",
    "avg": [ 3.72, 5.06 ], "std": [ 2.02, 1.28 ], "fq": 50 
  },
  "stones": {
    "dict": "happiness", "word": "stones", "stem": "stone",
    "avg": [ 4.52, 5.06 ], "std": [ 2.37, 1.25 ], "fq": 50 
  },
  "streak": {
    "dict": "happiness", "word": "streak", "stem": "streak",
    "avg": [ 5.00, 5.06 ], "std": [ 2.83, 1.41 ], "fq": 50 
  },
  "judgement": {
    "dict": "happiness", "word": "judgement", "stem": "judgement",
    "avg": [ 5.00, 5.04 ], "std": [ 2.68, 1.57 ], "fq": 50 
  },
  "conquer": {
    "dict": "happiness", "word": "conquer", "stem": "conquer",
    "avg": [ 2.90, 5.04 ], "std": [ 1.81, 2.22 ], "fq": 50 
  },
  "advertising": {
    "dict": "happiness", "word": "advertising", "stem": "advertis",
    "avg": [ 6.44, 5.04 ], "std": [ 2.58, 1.58 ], "fq": 50 
  },
  "biz": {
    "dict": "happiness", "word": "biz", "stem": "biz",
    "avg": [ 5.89, 5.04 ], "std": [ 2.37, 1.37 ], "fq": 50 
  },
  "blaze": {
    "dict": "happiness", "word": "blaze", "stem": "blaze",
    "avg": [ 5.38, 5.04 ], "std": [ 2.62, 1.52 ], "fq": 50 
  },
  "break": {
    "dict": "happiness", "word": "break", "stem": "break",
    "avg": [ 4.07, 5.04 ], "std": [ 1.69, 1.82 ], "fq": 50 
  },
  "charged": {
    "dict": "happiness", "word": "charged", "stem": "charg",
    "avg": [ 7.67, 5.04 ], "std": [ 1.91, 1.59 ], "fq": 50 
  },
  "doc": {
    "dict": "happiness", "word": "doc", "stem": "doc",
    "avg": [ 5.86, 5.04 ], "std": [ 2.70, 1.48 ], "fq": 50 
  },
  "fleet": {
    "dict": "happiness", "word": "fleet", "stem": "fleet",
    "avg": [ 5.39, 5.04 ], "std": [ 2.53, 1.37 ], "fq": 50 
  },
  "hombre": {
    "dict": "happiness", "word": "hombre", "stem": "hombr",
    "avg": [ 4.38, 5.04 ], "std": [ 2.24, 1.35 ], "fq": 50 
  },
  "measures": {
    "dict": "happiness", "word": "measures", "stem": "measur",
    "avg": [ 5.00, 5.04 ], "std": [ 2.83, 1.24 ], "fq": 50 
  },
  "mile": {
    "dict": "happiness", "word": "mile", "stem": "mile",
    "avg": [ 4.07, 5.04 ], "std": [ 2.15, 1.05 ], "fq": 50 
  },
  "nun": {
    "dict": "happiness", "word": "nun", "stem": "nun",
    "avg": [ 2.93, 5.04 ], "std": [ 1.80, 1.54 ], "fq": 50 
  },
  "occupied": {
    "dict": "happiness", "word": "occupied", "stem": "occupi",
    "avg": [ 6.77, 5.04 ], "std": [ 2.07, 1.34 ], "fq": 50 
  },
  "patient": {
    "dict": "happiness", "word": "patient", "stem": "patient",
    "avg": [ 4.21, 5.04 ], "std": [ 2.37, 2.01 ], "fq": 50 
  },
  "put": {
    "dict": "happiness", "word": "put", "stem": "put",
    "avg": [ 5.12, 5.04 ], "std": [ 2.42, 0.97 ], "fq": 50 
  },
  "sides": {
    "dict": "happiness", "word": "sides", "stem": "side",
    "avg": [ 5.04, 5.04 ], "std": [ 2.18, 1.18 ], "fq": 50 
  },
  "stone": {
    "dict": "happiness", "word": "stone", "stem": "stone",
    "avg": [ 4.52, 5.04 ], "std": [ 2.37, 1.47 ], "fq": 50 
  },
  "takes": {
    "dict": "happiness", "word": "takes", "stem": "take",
    "avg": [ 5.39, 5.04 ], "std": [ 2.22, 1.14 ], "fq": 50 
  },
  "corners": {
    "dict": "happiness", "word": "corners", "stem": "corner",
    "avg": [ 3.91, 5.02 ], "std": [ 1.92, 1.45 ], "fq": 50 
  },
  "curtain": {
    "dict": "happiness", "word": "curtain", "stem": "curtain",
    "avg": [ 3.67, 5.02 ], "std": [ 1.83, 1.41 ], "fq": 50 
  },
  "mash": {
    "dict": "happiness", "word": "mash", "stem": "mash",
    "avg": [ 6.91, 5.02 ], "std": [ 1.69, 1.73 ], "fq": 50 
  },
  "administrator": {
    "dict": "happiness", "word": "administrator", "stem": "administr",
    "avg": [ 5.71, 5.02 ], "std": [ 2.74, 1.33 ], "fq": 50 
  },
  "apologize": {
    "dict": "happiness", "word": "apologize", "stem": "apolog",
    "avg": [ 4.48, 5.02 ], "std": [ 2.29, 1.81 ], "fq": 50 
  },
  "blacks": {
    "dict": "happiness", "word": "blacks", "stem": "black",
    "avg": [ 4.61, 5.02 ], "std": [ 2.24, 1.65 ], "fq": 50 
  },
  "case": {
    "dict": "happiness", "word": "case", "stem": "case",
    "avg": [ 5.04, 5.02 ], "std": [ 2.18, 1.30 ], "fq": 50 
  },
  "controls": {
    "dict": "happiness", "word": "controls", "stem": "control",
    "avg": [ 6.10, 5.02 ], "std": [ 2.19, 1.33 ], "fq": 50 
  },
  "documents": {
    "dict": "happiness", "word": "documents", "stem": "document",
    "avg": [ 2.50, 5.02 ], "std": [ 1.85, 1.32 ], "fq": 50 
  },
  "flat": {
    "dict": "happiness", "word": "flat", "stem": "flat",
    "avg": [ 3.29, 5.02 ], "std": [ 1.89, 1.24 ], "fq": 50 
  },
  "flip": {
    "dict": "happiness", "word": "flip", "stem": "flip",
    "avg": [ 4.27, 5.02 ], "std": [ 2.17, 1.30 ], "fq": 50 
  },
  "foot": {
    "dict": "happiness", "word": "foot", "stem": "foot",
    "avg": [ 3.27, 5.02 ], "std": [ 1.98, 1.29 ], "fq": 50 
  },
  "happened": {
    "dict": "happiness", "word": "happened", "stem": "happen",
    "avg": [ 4.05, 5.02 ], "std": [ 2.34, 1.19 ], "fq": 50 
  },
  "hot": {
    "dict": "happiness", "word": "hot", "stem": "hot",
    "avg": [ 4.10, 5.02 ], "std": [ 2.34, 1.92 ], "fq": 50 
  },
  "industrial": {
    "dict": "happiness", "word": "industrial", "stem": "industri",
    "avg": [ 4.47, 5.02 ], "std": [ 2.43, 1.38 ], "fq": 50 
  },
  "mi": {
    "dict": "happiness", "word": "mi", "stem": "mi",
    "avg": [ 4.07, 5.02 ], "std": [ 2.15, 0.91 ], "fq": 50 
  },
  "phantom": {
    "dict": "happiness", "word": "phantom", "stem": "phantom",
    "avg": [ 4.30, 5.02 ], "std": [ 2.26, 1.61 ], "fq": 50 
  },
  "setting": {
    "dict": "happiness", "word": "setting", "stem": "set",
    "avg": [ 4.05, 5.02 ], "std": [ 1.89, 1.30 ], "fq": 50 
  },
  "sleeve": {
    "dict": "happiness", "word": "sleeve", "stem": "sleev",
    "avg": [ 3.59, 5.02 ], "std": [ 2.40, 1.36 ], "fq": 50 
  },
  "slice": {
    "dict": "happiness", "word": "slice", "stem": "slice",
    "avg": [ 5.00, 5.02 ], "std": [ 2.32, 1.49 ], "fq": 50 
  },
  "stake": {
    "dict": "happiness", "word": "stake", "stem": "stake",
    "avg": [ 6.98, 5.02 ], "std": [ 2.15, 1.19 ], "fq": 50 
  },
  "veil": {
    "dict": "happiness", "word": "veil", "stem": "veil",
    "avg": [ 5.28, 5.02 ], "std": [ 2.51, 1.44 ], "fq": 50 
  },
  "binding": {
    "dict": "happiness", "word": "binding", "stem": "bind",
    "avg": [ 3.90, 5.01 ], "std": [ 2.07, 1.60 ], "fq": 50 
  },
  "assess": {
    "dict": "happiness", "word": "assess", "stem": "assess",
    "avg": [ 2.95, 5.00 ], "std": [ 1.72, 1.37 ], "fq": 50 
  },
  "boot": {
    "dict": "happiness", "word": "boot", "stem": "boot",
    "avg": [ 8.02, 5.00 ], "std": [ 1.65, 1.03 ], "fq": 50 
  },
  "commands": {
    "dict": "happiness", "word": "commands", "stem": "command",
    "avg": [ 6.10, 5.00 ], "std": [ 2.19, 1.57 ], "fq": 50 
  },
  "executives": {
    "dict": "happiness", "word": "executives", "stem": "execut",
    "avg": [ 5.71, 5.00 ], "std": [ 2.74, 1.44 ], "fq": 50 
  },
  "hush": {
    "dict": "happiness", "word": "hush", "stem": "hush",
    "avg": [ 2.82, 5.00 ], "std": [ 2.13, 1.50 ], "fq": 50 
  },
  "listings": {
    "dict": "happiness", "word": "listings", "stem": "list",
    "avg": [ 4.25, 5.00 ], "std": [ 2.47, 1.23 ], "fq": 50 
  },
  "odds": {
    "dict": "happiness", "word": "odds", "stem": "odd",
    "avg": [ 4.27, 5.00 ], "std": [ 2.46, 1.12 ], "fq": 50 
  },
  "offices": {
    "dict": "happiness", "word": "offices", "stem": "offic",
    "avg": [ 4.08, 5.00 ], "std": [ 1.92, 1.44 ], "fq": 50 
  },
  "paying": {
    "dict": "happiness", "word": "paying", "stem": "pay",
    "avg": [ 5.23, 5.00 ], "std": [ 2.21, 1.88 ], "fq": 50 
  },
  "peculiar": {
    "dict": "happiness", "word": "peculiar", "stem": "peculiar",
    "avg": [ 4.27, 5.00 ], "std": [ 2.46, 1.71 ], "fq": 50 
  },
  "plain": {
    "dict": "happiness", "word": "plain", "stem": "plain",
    "avg": [ 3.52, 5.00 ], "std": [ 2.05, 1.44 ], "fq": 50 
  },
  "price": {
    "dict": "happiness", "word": "price", "stem": "price",
    "avg": [ 5.57, 5.00 ], "std": [ 2.26, 1.40 ], "fq": 50 
  },
  "pursued": {
    "dict": "happiness", "word": "pursued", "stem": "pursu",
    "avg": [ 6.77, 5.00 ], "std": [ 2.07, 1.82 ], "fq": 50 
  },
  "questions": {
    "dict": "happiness", "word": "questions", "stem": "question",
    "avg": [ 5.00, 5.00 ], "std": [ 2.23, 1.05 ], "fq": 50 
  },
  "reports": {
    "dict": "happiness", "word": "reports", "stem": "report",
    "avg": [ 2.50, 5.00 ], "std": [ 1.85, 1.51 ], "fq": 50 
  },
  "situation": {
    "dict": "happiness", "word": "situation", "stem": "situat",
    "avg": [ 4.08, 5.00 ], "std": [ 1.92, 1.31 ], "fq": 50 
  },
  "standard": {
    "dict": "happiness", "word": "standard", "stem": "standard",
    "avg": [ 3.83, 5.00 ], "std": [ 1.95, 1.47 ], "fq": 50 
  },
  "stir": {
    "dict": "happiness", "word": "stir", "stem": "stir",
    "avg": [ 7.67, 5.00 ], "std": [ 1.91, 1.29 ], "fq": 50 
  },
  "throw": {
    "dict": "happiness", "word": "throw", "stem": "throw",
    "avg": [ 6.03, 5.00 ], "std": [ 1.88, 1.55 ], "fq": 50 
  },
  "using": {
    "dict": "happiness", "word": "using", "stem": "use",
    "avg": [ 4.26, 5.00 ], "std": [ 2.47, 1.05 ], "fq": 50 
  },
  "weighted": {
    "dict": "happiness", "word": "weighted", "stem": "weight",
    "avg": [ 5.63, 5.00 ], "std": [ 2.07, 1.14 ], "fq": 50 
  },
  "cloudy": {
    "dict": "happiness", "word": "cloudy", "stem": "cloudi",
    "avg": [ 4.13, 4.98 ], "std": [ 2.13, 1.86 ], "fq": 50 
  },
  "hits": {
    "dict": "happiness", "word": "hits", "stem": "hit",
    "avg": [ 5.73, 4.98 ], "std": [ 2.09, 2.19 ], "fq": 50 
  },
  "knot": {
    "dict": "happiness", "word": "knot", "stem": "knot",
    "avg": [ 4.07, 4.98 ], "std": [ 2.15, 1.41 ], "fq": 50 
  },
  "line": {
    "dict": "happiness", "word": "line", "stem": "line",
    "avg": [ 4.98, 4.98 ], "std": [ 2.52, 1.20 ], "fq": 50 
  },
  "nails": {
    "dict": "happiness", "word": "nails", "stem": "nail",
    "avg": [ 5.50, 4.98 ], "std": [ 2.66, 1.48 ], "fq": 50 
  },
  "officers": {
    "dict": "happiness", "word": "officers", "stem": "offic",
    "avg": [ 4.08, 4.98 ], "std": [ 1.92, 1.67 ], "fq": 50 
  },
  "part": {
    "dict": "happiness", "word": "part", "stem": "part",
    "avg": [ 3.82, 4.98 ], "std": [ 2.24, 1.13 ], "fq": 50 
  },
  "pound": {
    "dict": "happiness", "word": "pound", "stem": "pound",
    "avg": [ 4.58, 4.98 ], "std": [ 2.02, 1.71 ], "fq": 50 
  },
  "question": {
    "dict": "happiness", "word": "question", "stem": "question",
    "avg": [ 5.00, 4.98 ], "std": [ 2.23, 1.73 ], "fq": 50 
  },
  "stared": {
    "dict": "happiness", "word": "stared", "stem": "stare",
    "avg": [ 5.83, 4.98 ], "std": [ 2.44, 1.44 ], "fq": 50 
  },
  "throws": {
    "dict": "happiness", "word": "throws", "stem": "throw",
    "avg": [ 6.03, 4.98 ], "std": [ 1.88, 1.06 ], "fq": 50 
  },
  "shi": {
    "dict": "happiness", "word": "shi", "stem": "shi",
    "avg": [ 3.77, 4.97 ], "std": [ 2.29, 1.36 ], "fq": 50 
  },
  "accounts": {
    "dict": "happiness", "word": "accounts", "stem": "account",
    "avg": [ 3.93, 4.96 ], "std": [ 2.29, 1.50 ], "fq": 50 
  },
  "assumed": {
    "dict": "happiness", "word": "assumed", "stem": "assum",
    "avg": [ 5.40, 4.96 ], "std": [ 2.70, 1.44 ], "fq": 50 
  },
  "borders": {
    "dict": "happiness", "word": "borders", "stem": "border",
    "avg": [ 4.07, 4.96 ], "std": [ 1.98, 1.52 ], "fq": 50 
  },
  "drops": {
    "dict": "happiness", "word": "drops", "stem": "drop",
    "avg": [ 4.70, 4.96 ], "std": [ 2.48, 1.55 ], "fq": 50 
  },
  "fe": {
    "dict": "happiness", "word": "fe", "stem": "fe",
    "avg": [ 3.76, 4.96 ], "std": [ 2.06, 1.32 ], "fq": 50 
  },
  "memorial": {
    "dict": "happiness", "word": "memorial", "stem": "memori",
    "avg": [ 5.42, 4.96 ], "std": [ 2.25, 1.75 ], "fq": 50 
  },
  "socialism": {
    "dict": "happiness", "word": "socialism", "stem": "social",
    "avg": [ 4.98, 4.96 ], "std": [ 2.59, 2.27 ], "fq": 50 
  },
  "alibi": {
    "dict": "happiness", "word": "alibi", "stem": "alibi",
    "avg": [ 4.48, 4.94 ], "std": [ 2.29, 1.74 ], "fq": 50 
  },
  "banging": {
    "dict": "happiness", "word": "banging", "stem": "bang",
    "avg": [ 6.38, 4.94 ], "std": [ 2.68, 2.14 ], "fq": 50 
  },
  "chase": {
    "dict": "happiness", "word": "chase", "stem": "chase",
    "avg": [ 5.76, 4.94 ], "std": [ 2.50, 1.72 ], "fq": 50 
  },
  "dip": {
    "dict": "happiness", "word": "dip", "stem": "dip",
    "avg": [ 4.70, 4.94 ], "std": [ 2.48, 1.28 ], "fq": 50 
  },
  "hooked": {
    "dict": "happiness", "word": "hooked", "stem": "hook",
    "avg": [ 4.81, 4.94 ], "std": [ 2.46, 1.20 ], "fq": 50 
  },
  "mo": {
    "dict": "happiness", "word": "mo", "stem": "mo",
    "avg": [ 3.83, 4.94 ], "std": [ 2.29, 1.32 ], "fq": 50 
  },
  "naughty": {
    "dict": "happiness", "word": "naughty", "stem": "naughti",
    "avg": [ 4.31, 4.94 ], "std": [ 2.20, 1.98 ], "fq": 50 
  },
  "razor": {
    "dict": "happiness", "word": "razor", "stem": "razor",
    "avg": [ 5.36, 4.94 ], "std": [ 2.44, 1.41 ], "fq": 50 
  },
  "row": {
    "dict": "happiness", "word": "row", "stem": "row",
    "avg": [ 6.29, 4.94 ], "std": [ 2.56, 1.20 ], "fq": 50 
  },
  "stood": {
    "dict": "happiness", "word": "stood", "stem": "stood",
    "avg": [ 3.93, 4.94 ], "std": [ 2.49, 1.08 ], "fq": 50 
  },
  "swell": {
    "dict": "happiness", "word": "swell", "stem": "swell",
    "avg": [ 3.80, 4.94 ], "std": [ 2.18, 2.01 ], "fq": 50 
  },
  "affect": {
    "dict": "happiness", "word": "affect", "stem": "affect",
    "avg": [ 6.21, 4.92 ], "std": [ 2.75, 1.44 ], "fq": 50 
  },
  "agencies": {
    "dict": "happiness", "word": "agencies", "stem": "agenc",
    "avg": [ 4.08, 4.92 ], "std": [ 1.92, 1.34 ], "fq": 50 
  },
  "armies": {
    "dict": "happiness", "word": "armies", "stem": "armi",
    "avg": [ 5.03, 4.92 ], "std": [ 2.03, 1.89 ], "fq": 50 
  },
  "au": {
    "dict": "happiness", "word": "au", "stem": "au",
    "avg": [ 5.76, 4.92 ], "std": [ 2.79, 1.05 ], "fq": 50 
  },
  "common": {
    "dict": "happiness", "word": "common", "stem": "common",
    "avg": [ 4.28, 4.92 ], "std": [ 2.46, 1.26 ], "fq": 50 
  },
  "crave": {
    "dict": "happiness", "word": "crave", "stem": "crave",
    "avg": [ 6.88, 4.92 ], "std": [ 1.85, 1.60 ], "fq": 50 
  },
  "judge": {
    "dict": "happiness", "word": "judge", "stem": "judg",
    "avg": [ 5.47, 4.92 ], "std": [ 2.54, 1.60 ], "fq": 50 
  },
  "marked": {
    "dict": "happiness", "word": "marked", "stem": "mark",
    "avg": [ 4.79, 4.92 ], "std": [ 2.11, 1.29 ], "fq": 50 
  },
  "shadow": {
    "dict": "happiness", "word": "shadow", "stem": "shadow",
    "avg": [ 4.30, 4.92 ], "std": [ 2.26, 1.44 ], "fq": 50 
  },
  "strip": {
    "dict": "happiness", "word": "strip", "stem": "strip",
    "avg": [ 6.35, 4.92 ], "std": [ 2.04, 1.66 ], "fq": 50 
  },
  "suppose": {
    "dict": "happiness", "word": "suppose", "stem": "suppos",
    "avg": [ 5.98, 4.92 ], "std": [ 2.14, 1.12 ], "fq": 50 
  },
  "pretending": {
    "dict": "happiness", "word": "pretending", "stem": "pretend",
    "avg": [ 6.21, 4.92 ], "std": [ 2.75, 1.57 ], "fq": 50 
  },
  "border": {
    "dict": "happiness", "word": "border", "stem": "border",
    "avg": [ 4.07, 4.90 ], "std": [ 1.98, 1.49 ], "fq": 50 
  },
  "campaigns": {
    "dict": "happiness", "word": "campaigns", "stem": "campaign",
    "avg": [ 7.15, 4.90 ], "std": [ 2.19, 1.93 ], "fq": 50 
  },
  "charge": {
    "dict": "happiness", "word": "charge", "stem": "charg",
    "avg": [ 7.67, 4.90 ], "std": [ 1.91, 1.31 ], "fq": 50 
  },
  "fog": {
    "dict": "happiness", "word": "fog", "stem": "fog",
    "avg": [ 3.30, 4.90 ], "std": [ 2.08, 1.89 ], "fq": 50 
  },
  "sector": {
    "dict": "happiness", "word": "sector", "stem": "sector",
    "avg": [ 3.88, 4.90 ], "std": [ 1.99, 1.23 ], "fq": 50 
  },
  "black": {
    "dict": "happiness", "word": "black", "stem": "black",
    "avg": [ 4.61, 4.88 ], "std": [ 2.24, 1.84 ], "fq": 50 
  },
  "causes": {
    "dict": "happiness", "word": "causes", "stem": "caus",
    "avg": [ 4.93, 4.88 ], "std": [ 2.44, 1.27 ], "fq": 50 
  },
  "chuck": {
    "dict": "happiness", "word": "chuck", "stem": "chuck",
    "avg": [ 5.61, 4.88 ], "std": [ 2.67, 1.39 ], "fq": 50 
  },
  "cited": {
    "dict": "happiness", "word": "cited", "stem": "cite",
    "avg": [ 4.25, 4.88 ], "std": [ 2.47, 1.41 ], "fq": 50 
  },
  "issued": {
    "dict": "happiness", "word": "issued", "stem": "issu",
    "avg": [ 5.00, 4.88 ], "std": [ 2.32, 1.14 ], "fq": 50 
  },
  "judges": {
    "dict": "happiness", "word": "judges", "stem": "judg",
    "avg": [ 5.47, 4.88 ], "std": [ 2.54, 1.33 ], "fq": 50 
  },
  "mis": {
    "dict": "happiness", "word": "mis", "stem": "mi",
    "avg": [ 4.07, 4.88 ], "std": [ 2.15, 1.10 ], "fq": 50 
  },
  "oil": {
    "dict": "happiness", "word": "oil", "stem": "oil",
    "avg": [ 5.07, 4.88 ], "std": [ 2.37, 1.64 ], "fq": 50 
  },
  "toilet": {
    "dict": "happiness", "word": "toilet", "stem": "toilet",
    "avg": [ 4.00, 4.88 ], "std": [ 2.14, 1.49 ], "fq": 50 
  },
  "went": {
    "dict": "happiness", "word": "went", "stem": "went",
    "avg": [ 6.21, 4.88 ], "std": [ 2.51, 1.45 ], "fq": 50 
  },
  "substitute": {
    "dict": "happiness", "word": "substitute", "stem": "substitut",
    "avg": [ 3.27, 4.88 ], "std": [ 2.05, 1.47 ], "fq": 50 
  },
  "nous": {
    "dict": "happiness", "word": "nous", "stem": "nou",
    "avg": [ 5.00, 4.88 ], "std": [ 2.68, 1.16 ], "fq": 50 
  },
  "circumstances": {
    "dict": "happiness", "word": "circumstances", "stem": "circumst",
    "avg": [ 4.22, 4.86 ], "std": [ 2.24, 1.11 ], "fq": 50 
  },
  "divisions": {
    "dict": "happiness", "word": "divisions", "stem": "divis",
    "avg": [ 3.82, 4.86 ], "std": [ 2.24, 1.48 ], "fq": 50 
  },
  "ft": {
    "dict": "happiness", "word": "ft", "stem": "ft",
    "avg": [ 3.27, 4.86 ], "std": [ 1.98, 0.78 ], "fq": 50 
  },
  "ira": {
    "dict": "happiness", "word": "ira", "stem": "ira",
    "avg": [ 7.63, 4.86 ], "std": [ 1.91, 1.40 ], "fq": 50 
  },
  "missy": {
    "dict": "happiness", "word": "missy", "stem": "missi",
    "avg": [ 4.29, 4.86 ], "std": [ 2.69, 1.55 ], "fq": 50 
  },
  "sensitive": {
    "dict": "happiness", "word": "sensitive", "stem": "sensit",
    "avg": [ 4.88, 4.86 ], "std": [ 2.30, 1.41 ], "fq": 50 
  },
  "staring": {
    "dict": "happiness", "word": "staring", "stem": "stare",
    "avg": [ 5.83, 4.86 ], "std": [ 2.44, 1.28 ], "fq": 50 
  },
  "tempted": {
    "dict": "happiness", "word": "tempted", "stem": "tempt",
    "avg": [ 5.16, 4.86 ], "std": [ 2.25, 1.73 ], "fq": 50 
  },
  "tract": {
    "dict": "happiness", "word": "tract", "stem": "tract",
    "avg": [ 3.62, 4.86 ], "std": [ 2.02, 1.25 ], "fq": 50 
  },
  "geld": {
    "dict": "happiness", "word": "geld", "stem": "geld",
    "avg": [ 5.00, 4.86 ], "std": [ 2.32, 1.59 ], "fq": 50 
  },
  "maintenance": {
    "dict": "happiness", "word": "maintenance", "stem": "mainten",
    "avg": [ 4.30, 4.84 ], "std": [ 2.29, 1.60 ], "fq": 50 
  },
  "mar": {
    "dict": "happiness", "word": "mar", "stem": "mar",
    "avg": [ 4.04, 4.84 ], "std": [ 2.14, 1.23 ], "fq": 50 
  },
  "rates": {
    "dict": "happiness", "word": "rates", "stem": "rate",
    "avg": [ 7.24, 4.84 ], "std": [ 2.06, 1.15 ], "fq": 50 
  },
  "secret": {
    "dict": "happiness", "word": "secret", "stem": "secret",
    "avg": [ 4.84, 4.84 ], "std": [ 2.57, 1.61 ], "fq": 50 
  },
  "horns": {
    "dict": "happiness", "word": "horns", "stem": "horn",
    "avg": [ 4.97, 4.84 ], "std": [ 2.13, 1.93 ], "fq": 50 
  },
  "cane": {
    "dict": "happiness", "word": "cane", "stem": "cane",
    "avg": [ 4.20, 4.82 ], "std": [ 1.93, 1.79 ], "fq": 50 
  },
  "cases": {
    "dict": "happiness", "word": "cases", "stem": "case",
    "avg": [ 5.04, 4.82 ], "std": [ 2.18, 0.92 ], "fq": 50 
  },
  "flipped": {
    "dict": "happiness", "word": "flipped", "stem": "flip",
    "avg": [ 4.27, 4.82 ], "std": [ 2.17, 1.34 ], "fq": 50 
  },
  "hid": {
    "dict": "happiness", "word": "hid", "stem": "hid",
    "avg": [ 5.28, 4.82 ], "std": [ 2.51, 1.12 ], "fq": 50 
  },
  "impact": {
    "dict": "happiness", "word": "impact", "stem": "impact",
    "avg": [ 6.21, 4.82 ], "std": [ 2.75, 1.32 ], "fq": 50 
  },
  "smell": {
    "dict": "happiness", "word": "smell", "stem": "smell",
    "avg": [ 5.56, 4.82 ], "std": [ 2.62, 1.55 ], "fq": 50 
  },
  "witness": {
    "dict": "happiness", "word": "witness", "stem": "wit",
    "avg": [ 5.42, 4.82 ], "std": [ 2.44, 1.37 ], "fq": 50 
  },
  "nerve": {
    "dict": "happiness", "word": "nerve", "stem": "nerv",
    "avg": [ 6.34, 4.82 ], "std": [ 2.25, 1.48 ], "fq": 50 
  },
  "cock": {
    "dict": "happiness", "word": "cock", "stem": "cock",
    "avg": [ 4.70, 4.80 ], "std": [ 2.59, 2.00 ], "fq": 50 
  },
  "el": {
    "dict": "happiness", "word": "el", "stem": "el",
    "avg": [ 4.16, 4.80 ], "std": [ 1.99, 1.12 ], "fq": 50 
  },
  "johns": {
    "dict": "happiness", "word": "johns", "stem": "john",
    "avg": [ 3.88, 4.80 ], "std": [ 1.72, 1.39 ], "fq": 50 
  },
  "meetings": {
    "dict": "happiness", "word": "meetings", "stem": "meet",
    "avg": [ 4.94, 4.80 ], "std": [ 2.63, 1.54 ], "fq": 50 
  },
  "passive": {
    "dict": "happiness", "word": "passive", "stem": "passiv",
    "avg": [ 2.95, 4.80 ], "std": [ 2.55, 1.77 ], "fq": 50 
  },
  "belly": {
    "dict": "happiness", "word": "belly", "stem": "belli",
    "avg": [ 3.93, 4.78 ], "std": [ 2.49, 1.46 ], "fq": 50 
  },
  "conditions": {
    "dict": "happiness", "word": "conditions", "stem": "condit",
    "avg": [ 3.46, 4.78 ], "std": [ 1.72, 1.47 ], "fq": 50 
  },
  "reserved": {
    "dict": "happiness", "word": "reserved", "stem": "reserv",
    "avg": [ 3.27, 4.78 ], "std": [ 2.05, 1.40 ], "fq": 50 
  },
  "reversed": {
    "dict": "happiness", "word": "reversed", "stem": "revers",
    "avg": [ 5.64, 4.78 ], "std": [ 2.99, 1.43 ], "fq": 50 
  },
  "stakes": {
    "dict": "happiness", "word": "stakes", "stem": "stake",
    "avg": [ 6.98, 4.78 ], "std": [ 2.15, 0.95 ], "fq": 50 
  },
  "suddenly": {
    "dict": "happiness", "word": "suddenly", "stem": "suddenli",
    "avg": [ 5.73, 4.78 ], "std": [ 2.73, 1.31 ], "fq": 50 
  },
  "throwing": {
    "dict": "happiness", "word": "throwing", "stem": "throw",
    "avg": [ 6.03, 4.78 ], "std": [ 1.88, 1.23 ], "fq": 50 
  },
  "witnesses": {
    "dict": "happiness", "word": "witnesses", "stem": "wit",
    "avg": [ 5.42, 4.78 ], "std": [ 2.44, 1.46 ], "fq": 50 
  },
  "board": {
    "dict": "happiness", "word": "board", "stem": "board",
    "avg": [ 3.36, 4.76 ], "std": [ 2.12, 1.52 ], "fq": 50 
  },
  "gas": {
    "dict": "happiness", "word": "gas", "stem": "ga",
    "avg": [ 7.02, 4.76 ], "std": [ 1.84, 1.65 ], "fq": 50 
  },
  "pieces": {
    "dict": "happiness", "word": "pieces", "stem": "piec",
    "avg": [ 3.82, 4.76 ], "std": [ 2.24, 1.27 ], "fq": 50 
  },
  "pig": {
    "dict": "happiness", "word": "pig", "stem": "pig",
    "avg": [ 4.20, 4.76 ], "std": [ 2.42, 2.10 ], "fq": 50 
  },
  "repair": {
    "dict": "happiness", "word": "repair", "stem": "repair",
    "avg": [ 5.86, 4.76 ], "std": [ 2.70, 1.82 ], "fq": 50 
  },
  "report": {
    "dict": "happiness", "word": "report", "stem": "report",
    "avg": [ 2.50, 4.76 ], "std": [ 1.85, 1.33 ], "fq": 50 
  },
  "somewhat": {
    "dict": "happiness", "word": "somewhat", "stem": "somewhat",
    "avg": [ 6.03, 4.76 ], "std": [ 2.22, 1.33 ], "fq": 50 
  },
  "spent": {
    "dict": "happiness", "word": "spent", "stem": "spent",
    "avg": [ 2.64, 4.76 ], "std": [ 2.19, 1.55 ], "fq": 50 
  },
  "took": {
    "dict": "happiness", "word": "took", "stem": "took",
    "avg": [ 5.39, 4.76 ], "std": [ 2.22, 1.02 ], "fq": 50 
  },
  "wore": {
    "dict": "happiness", "word": "wore", "stem": "wore",
    "avg": [ 2.64, 4.76 ], "std": [ 2.19, 1.36 ], "fq": 50 
  },
  "goed": {
    "dict": "happiness", "word": "goed", "stem": "go",
    "avg": [ 6.21, 4.76 ], "std": [ 2.51, 1.01 ], "fq": 50 
  },
  "admit": {
    "dict": "happiness", "word": "admit", "stem": "admit",
    "avg": [ 5.40, 4.74 ], "std": [ 2.70, 1.27 ], "fq": 50 
  },
  "alley": {
    "dict": "happiness", "word": "alley", "stem": "alley",
    "avg": [ 4.91, 4.74 ], "std": [ 2.42, 1.19 ], "fq": 50 
  },
  "authority": {
    "dict": "happiness", "word": "authority", "stem": "author",
    "avg": [ 4.08, 4.74 ], "std": [ 1.92, 1.59 ], "fq": 50 
  },
  "corner": {
    "dict": "happiness", "word": "corner", "stem": "corner",
    "avg": [ 3.91, 4.74 ], "std": [ 1.92, 1.35 ], "fq": 50 
  },
  "heavily": {
    "dict": "happiness", "word": "heavily", "stem": "heavili",
    "avg": [ 5.12, 4.74 ], "std": [ 2.19, 1.12 ], "fq": 50 
  },
  "hook": {
    "dict": "happiness", "word": "hook", "stem": "hook",
    "avg": [ 4.81, 4.74 ], "std": [ 2.46, 1.14 ], "fq": 50 
  },
  "judgment": {
    "dict": "happiness", "word": "judgment", "stem": "judgment",
    "avg": [ 5.00, 4.74 ], "std": [ 2.68, 1.84 ], "fq": 50 
  },
  "load": {
    "dict": "happiness", "word": "load", "stem": "load",
    "avg": [ 5.63, 4.74 ], "std": [ 2.07, 1.07 ], "fq": 50 
  },
  "operate": {
    "dict": "happiness", "word": "operate", "stem": "oper",
    "avg": [ 6.77, 4.74 ], "std": [ 2.07, 1.70 ], "fq": 50 
  },
  "resist": {
    "dict": "happiness", "word": "resist", "stem": "resist",
    "avg": [ 6.37, 4.74 ], "std": [ 2.56, 1.60 ], "fq": 50 
  },
  "smaller": {
    "dict": "happiness", "word": "smaller", "stem": "smaller",
    "avg": [ 3.98, 4.74 ], "std": [ 2.24, 1.48 ], "fq": 50 
  },
  "possessed": {
    "dict": "happiness", "word": "possessed", "stem": "possess",
    "avg": [ 6.41, 4.73 ], "std": [ 2.13, 1.91 ], "fq": 50 
  },
  "alien": {
    "dict": "happiness", "word": "alien", "stem": "alien",
    "avg": [ 5.45, 4.72 ], "std": [ 2.15, 1.63 ], "fq": 50 
  },
  "assume": {
    "dict": "happiness", "word": "assume", "stem": "assum",
    "avg": [ 5.40, 4.72 ], "std": [ 2.70, 1.18 ], "fq": 50 
  },
  "bent": {
    "dict": "happiness", "word": "bent", "stem": "bent",
    "avg": [ 4.07, 4.72 ], "std": [ 2.34, 1.57 ], "fq": 50 
  },
  "citing": {
    "dict": "happiness", "word": "citing", "stem": "cite",
    "avg": [ 4.25, 4.72 ], "std": [ 2.47, 1.44 ], "fq": 50 
  },
  "claims": {
    "dict": "happiness", "word": "claims", "stem": "claim",
    "avg": [ 5.65, 4.72 ], "std": [ 2.23, 1.44 ], "fq": 50 
  },
  "condition": {
    "dict": "happiness", "word": "condition", "stem": "condit",
    "avg": [ 3.46, 4.72 ], "std": [ 1.72, 1.34 ], "fq": 50 
  },
  "guessing": {
    "dict": "happiness", "word": "guessing", "stem": "guess",
    "avg": [ 5.98, 4.72 ], "std": [ 2.14, 1.63 ], "fq": 50 
  },
  "offset": {
    "dict": "happiness", "word": "offset", "stem": "offset",
    "avg": [ 4.76, 4.72 ], "std": [ 2.40, 1.20 ], "fq": 50 
  },
  "wake": {
    "dict": "happiness", "word": "wake", "stem": "wake",
    "avg": [ 6.63, 4.72 ], "std": [ 2.70, 1.65 ], "fq": 50 
  },
  "interference": {
    "dict": "happiness", "word": "interference", "stem": "interfer",
    "avg": [ 4.12, 4.71 ], "std": [ 2.01, 1.73 ], "fq": 50 
  },
  "chasing": {
    "dict": "happiness", "word": "chasing", "stem": "chase",
    "avg": [ 5.76, 4.70 ], "std": [ 2.50, 1.37 ], "fq": 50 
  },
  "corporate": {
    "dict": "happiness", "word": "corporate", "stem": "corpor",
    "avg": [ 5.52, 4.70 ], "std": [ 2.63, 1.53 ], "fq": 50 
  },
  "crossed": {
    "dict": "happiness", "word": "crossed", "stem": "cross",
    "avg": [ 5.61, 4.70 ], "std": [ 2.76, 1.37 ], "fq": 50 
  },
  "hound": {
    "dict": "happiness", "word": "hound", "stem": "hound",
    "avg": [ 5.76, 4.70 ], "std": [ 2.50, 1.58 ], "fq": 50 
  },
  "nail": {
    "dict": "happiness", "word": "nail", "stem": "nail",
    "avg": [ 5.50, 4.70 ], "std": [ 2.66, 1.43 ], "fq": 50 
  },
  "rocky": {
    "dict": "happiness", "word": "rocky", "stem": "rocki",
    "avg": [ 5.33, 4.70 ], "std": [ 2.04, 1.73 ], "fq": 50 
  },
  "seriously": {
    "dict": "happiness", "word": "seriously", "stem": "serious",
    "avg": [ 4.00, 4.70 ], "std": [ 1.87, 1.56 ], "fq": 50 
  },
  "striking": {
    "dict": "happiness", "word": "striking", "stem": "strike",
    "avg": [ 6.24, 4.70 ], "std": [ 2.59, 1.88 ], "fq": 50 
  },
  "shakes": {
    "dict": "happiness", "word": "shakes", "stem": "shake",
    "avg": [ 7.67, 4.69 ], "std": [ 1.91, 1.82 ], "fq": 50 
  },
  "bodies": {
    "dict": "happiness", "word": "bodies", "stem": "bodi",
    "avg": [ 5.52, 4.68 ], "std": [ 2.63, 1.62 ], "fq": 50 
  },
  "cross": {
    "dict": "happiness", "word": "cross", "stem": "cross",
    "avg": [ 5.61, 4.68 ], "std": [ 2.76, 1.71 ], "fq": 50 
  },
  "curb": {
    "dict": "happiness", "word": "curb", "stem": "curb",
    "avg": [ 6.10, 4.68 ], "std": [ 2.19, 1.28 ], "fq": 50 
  },
  "dun": {
    "dict": "happiness", "word": "dun", "stem": "dun",
    "avg": [ 5.61, 4.68 ], "std": [ 2.76, 1.39 ], "fq": 50 
  },
  "knives": {
    "dict": "happiness", "word": "knives", "stem": "knive",
    "avg": [ 5.80, 4.68 ], "std": [ 2.00, 2.09 ], "fq": 50 
  },
  "overcast": {
    "dict": "happiness", "word": "overcast", "stem": "overcast",
    "avg": [ 3.46, 4.68 ], "std": [ 1.92, 1.66 ], "fq": 50 
  },
  "ruling": {
    "dict": "happiness", "word": "ruling", "stem": "rule",
    "avg": [ 4.89, 4.68 ], "std": [ 2.46, 1.45 ], "fq": 50 
  },
  "shady": {
    "dict": "happiness", "word": "shady", "stem": "shadi",
    "avg": [ 6.25, 4.68 ], "std": [ 1.59, 1.71 ], "fq": 50 
  },
  "spots": {
    "dict": "happiness", "word": "spots", "stem": "spot",
    "avg": [ 4.08, 4.68 ], "std": [ 1.92, 1.41 ], "fq": 50 
  },
  "threw": {
    "dict": "happiness", "word": "threw", "stem": "threw",
    "avg": [ 6.03, 4.68 ], "std": [ 1.88, 1.06 ], "fq": 50 
  },
  "bump": {
    "dict": "happiness", "word": "bump", "stem": "bump",
    "avg": [ 5.38, 4.67 ], "std": [ 2.58, 1.42 ], "fq": 50 
  },
  "dependence": {
    "dict": "happiness", "word": "dependence", "stem": "depend",
    "avg": [ 4.81, 4.67 ], "std": [ 2.46, 1.96 ], "fq": 50 
  },
  "flesh": {
    "dict": "happiness", "word": "flesh", "stem": "flesh",
    "avg": [ 3.92, 4.67 ], "std": [ 1.94, 1.56 ], "fq": 50 
  },
  "tumble": {
    "dict": "happiness", "word": "tumble", "stem": "tumbl",
    "avg": [ 4.70, 4.67 ], "std": [ 2.48, 1.70 ], "fq": 50 
  },
  "forms": {
    "dict": "happiness", "word": "forms", "stem": "form",
    "avg": [ 5.67, 4.66 ], "std": [ 2.51, 1.33 ], "fq": 50 
  },
  "minor": {
    "dict": "happiness", "word": "minor", "stem": "minor",
    "avg": [ 3.98, 4.66 ], "std": [ 2.24, 1.26 ], "fq": 50 
  },
  "odd": {
    "dict": "happiness", "word": "odd", "stem": "odd",
    "avg": [ 4.27, 4.66 ], "std": [ 2.46, 1.65 ], "fq": 50 
  },
  "pile": {
    "dict": "happiness", "word": "pile", "stem": "pile",
    "avg": [ 5.49, 4.66 ], "std": [ 2.43, 0.89 ], "fq": 50 
  },
  "wanting": {
    "dict": "happiness", "word": "wanting", "stem": "want",
    "avg": [ 7.35, 4.66 ], "std": [ 1.76, 1.48 ], "fq": 50 
  },
  "stripped": {
    "dict": "happiness", "word": "stripped", "stem": "strip",
    "avg": [ 6.35, 4.65 ], "std": [ 2.04, 1.93 ], "fq": 50 
  },
  "tire": {
    "dict": "happiness", "word": "tire", "stem": "tire",
    "avg": [ 2.83, 4.65 ], "std": [ 2.31, 1.49 ], "fq": 50 
  },
  "wolves": {
    "dict": "happiness", "word": "wolves", "stem": "wolv",
    "avg": [ 5.57, 4.65 ], "std": [ 2.61, 2.28 ], "fq": 50 
  },
  "crazy": {
    "dict": "happiness", "word": "crazy", "stem": "crazi",
    "avg": [ 5.80, 4.64 ], "std": [ 2.39, 2.26 ], "fq": 50 
  },
  "dry": {
    "dict": "happiness", "word": "dry", "stem": "dri",
    "avg": [ 3.76, 4.64 ], "std": [ 2.06, 1.26 ], "fq": 50 
  },
  "freak": {
    "dict": "happiness", "word": "freak", "stem": "freak",
    "avg": [ 4.81, 4.64 ], "std": [ 2.46, 1.92 ], "fq": 50 
  },
  "fucking": {
    "dict": "happiness", "word": "fucking", "stem": "fuck",
    "avg": [ 6.38, 4.64 ], "std": [ 2.68, 2.93 ], "fq": 50 
  },
  "government": {
    "dict": "happiness", "word": "government", "stem": "govern",
    "avg": [ 3.74, 4.64 ], "std": [ 2.37, 1.64 ], "fq": 50 
  },
  "left": {
    "dict": "happiness", "word": "left", "stem": "left",
    "avg": [ 4.27, 4.64 ], "std": [ 2.46, 1.44 ], "fq": 50 
  },
  "lust": {
    "dict": "happiness", "word": "lust", "stem": "lust",
    "avg": [ 6.88, 4.64 ], "std": [ 1.85, 2.04 ], "fq": 50 
  },
  "pretend": {
    "dict": "happiness", "word": "pretend", "stem": "pretend",
    "avg": [ 6.21, 4.64 ], "std": [ 2.75, 1.27 ], "fq": 50 
  },
  "slit": {
    "dict": "happiness", "word": "slit", "stem": "slit",
    "avg": [ 4.70, 4.64 ], "std": [ 2.59, 1.51 ], "fq": 50 
  },
  "stares": {
    "dict": "happiness", "word": "stares", "stem": "stare",
    "avg": [ 5.83, 4.63 ], "std": [ 2.44, 1.50 ], "fq": 50 
  },
  "stiff": {
    "dict": "happiness", "word": "stiff", "stem": "stiff",
    "avg": [ 4.02, 4.63 ], "std": [ 2.41, 1.68 ], "fq": 50 
  },
  "bull": {
    "dict": "happiness", "word": "bull", "stem": "bull",
    "avg": [ 4.20, 4.62 ], "std": [ 2.42, 1.31 ], "fq": 50 
  },
  "bureau": {
    "dict": "happiness", "word": "bureau", "stem": "bureau",
    "avg": [ 4.08, 4.62 ], "std": [ 1.92, 1.29 ], "fq": 50 
  },
  "dick": {
    "dict": "happiness", "word": "dick", "stem": "dick",
    "avg": [ 4.70, 4.62 ], "std": [ 2.59, 1.78 ], "fq": 50 
  },
  "governments": {
    "dict": "happiness", "word": "governments", "stem": "govern",
    "avg": [ 3.74, 4.62 ], "std": [ 2.37, 1.70 ], "fq": 50 
  },
  "holler": {
    "dict": "happiness", "word": "holler", "stem": "holler",
    "avg": [ 5.00, 4.62 ], "std": [ 2.19, 1.43 ], "fq": 50 
  },
  "lease": {
    "dict": "happiness", "word": "lease", "stem": "leas",
    "avg": [ 6.77, 4.62 ], "std": [ 2.07, 1.26 ], "fq": 50 
  },
  "pigs": {
    "dict": "happiness", "word": "pigs", "stem": "pig",
    "avg": [ 4.20, 4.62 ], "std": [ 2.42, 2.03 ], "fq": 50 
  },
  "pressed": {
    "dict": "happiness", "word": "pressed", "stem": "press",
    "avg": [ 7.15, 4.62 ], "std": [ 2.19, 1.31 ], "fq": 50 
  },
  "daze": {
    "dict": "happiness", "word": "daze", "stem": "daze",
    "avg": [ 6.33, 4.61 ], "std": [ 2.02, 1.44 ], "fq": 50 
  },
  "bind": {
    "dict": "happiness", "word": "bind", "stem": "bind",
    "avg": [ 3.90, 4.60 ], "std": [ 2.07, 1.78 ], "fq": 50 
  },
  "bound": {
    "dict": "happiness", "word": "bound", "stem": "bound",
    "avg": [ 5.67, 4.60 ], "std": [ 2.51, 1.36 ], "fq": 50 
  },
  "flames": {
    "dict": "happiness", "word": "flames", "stem": "flame",
    "avg": [ 7.17, 4.60 ], "std": [ 2.06, 1.87 ], "fq": 50 
  },
  "sack": {
    "dict": "happiness", "word": "sack", "stem": "sack",
    "avg": [ 7.17, 4.60 ], "std": [ 2.06, 1.50 ], "fq": 50 
  },
  "sticky": {
    "dict": "happiness", "word": "sticky", "stem": "sticki",
    "avg": [ 5.87, 4.60 ], "std": [ 2.55, 1.32 ], "fq": 50 
  },
  "tight": {
    "dict": "happiness", "word": "tight", "stem": "tight",
    "avg": [ 4.89, 4.60 ], "std": [ 2.50, 1.25 ], "fq": 50 
  },
  "trigger": {
    "dict": "happiness", "word": "trigger", "stem": "trigger",
    "avg": [ 4.86, 4.60 ], "std": [ 2.56, 1.95 ], "fq": 50 
  },
  "used": {
    "dict": "happiness", "word": "used", "stem": "use",
    "avg": [ 4.26, 4.60 ], "std": [ 2.47, 1.48 ], "fq": 50 
  },
  "busy": {
    "dict": "happiness", "word": "busy", "stem": "busi",
    "avg": [ 6.77, 4.58 ], "std": [ 2.07, 1.83 ], "fq": 50 
  },
  "excuse": {
    "dict": "happiness", "word": "excuse", "stem": "excus",
    "avg": [ 4.48, 4.58 ], "std": [ 2.29, 1.53 ], "fq": 50 
  },
  "fighter": {
    "dict": "happiness", "word": "fighter", "stem": "fighter",
    "avg": [ 5.85, 4.58 ], "std": [ 3.15, 1.65 ], "fq": 50 
  },
  "hit": {
    "dict": "happiness", "word": "hit", "stem": "hit",
    "avg": [ 5.73, 4.58 ], "std": [ 2.09, 1.81 ], "fq": 50 
  },
  "lock": {
    "dict": "happiness", "word": "lock", "stem": "lock",
    "avg": [ 6.77, 4.58 ], "std": [ 2.07, 1.01 ], "fq": 50 
  },
  "stops": {
    "dict": "happiness", "word": "stops", "stem": "stop",
    "avg": [ 5.00, 4.58 ], "std": [ 2.83, 1.21 ], "fq": 50 
  },
  "blues": {
    "dict": "happiness", "word": "blues", "stem": "blue",
    "avg": [ 4.31, 4.56 ], "std": [ 2.20, 1.98 ], "fq": 50 
  },
  "separately": {
    "dict": "happiness", "word": "separately", "stem": "separ",
    "avg": [ 5.26, 4.55 ], "std": [ 2.36, 1.51 ], "fq": 50 
  },
  "bit": {
    "dict": "happiness", "word": "bit", "stem": "bit",
    "avg": [ 4.70, 4.54 ], "std": [ 2.59, 1.13 ], "fq": 50 
  },
  "blocks": {
    "dict": "happiness", "word": "blocks", "stem": "block",
    "avg": [ 4.12, 4.54 ], "std": [ 2.01, 1.42 ], "fq": 50 
  },
  "command": {
    "dict": "happiness", "word": "command", "stem": "command",
    "avg": [ 6.10, 4.54 ], "std": [ 2.19, 1.58 ], "fq": 50 
  },
  "terms": {
    "dict": "happiness", "word": "terms", "stem": "term",
    "avg": [ 3.27, 4.54 ], "std": [ 1.98, 1.05 ], "fq": 50 
  },
  "twisting": {
    "dict": "happiness", "word": "twisting", "stem": "twist",
    "avg": [ 6.26, 4.54 ], "std": [ 2.61, 1.40 ], "fq": 50 
  },
  "urged": {
    "dict": "happiness", "word": "urged", "stem": "urg",
    "avg": [ 6.02, 4.54 ], "std": [ 2.67, 1.30 ], "fq": 50 
  },
  "chains": {
    "dict": "happiness", "word": "chains", "stem": "chain",
    "avg": [ 3.76, 4.53 ], "std": [ 2.06, 1.77 ], "fq": 50 
  },
  "waits": {
    "dict": "happiness", "word": "waits", "stem": "wait",
    "avg": [ 5.62, 4.53 ], "std": [ 2.39, 1.24 ], "fq": 50 
  },
  "blew": {
    "dict": "happiness", "word": "blew", "stem": "blew",
    "avg": [ 4.14, 4.52 ], "std": [ 2.30, 1.47 ], "fq": 50 
  },
  "leave": {
    "dict": "happiness", "word": "leave", "stem": "leav",
    "avg": [ 3.82, 4.52 ], "std": [ 2.24, 1.33 ], "fq": 50 
  },
  "muss": {
    "dict": "happiness", "word": "muss", "stem": "muss",
    "avg": [ 3.34, 4.52 ], "std": [ 2.37, 1.07 ], "fq": 50 
  },
  "small": {
    "dict": "happiness", "word": "small", "stem": "small",
    "avg": [ 3.98, 4.52 ], "std": [ 2.24, 1.36 ], "fq": 50 
  },
  "utterly": {
    "dict": "happiness", "word": "utterly", "stem": "utterli",
    "avg": [ 5.73, 4.52 ], "std": [ 2.73, 1.71 ], "fq": 50 
  },
  "weight": {
    "dict": "happiness", "word": "weight", "stem": "weight",
    "avg": [ 5.63, 4.52 ], "std": [ 2.07, 1.55 ], "fq": 50 
  },
  "disposed": {
    "dict": "happiness", "word": "disposed", "stem": "dispos",
    "avg": [ 5.00, 4.50 ], "std": [ 2.68, 1.73 ], "fq": 50 
  },
  "distance": {
    "dict": "happiness", "word": "distance", "stem": "distanc",
    "avg": [ 5.14, 4.50 ], "std": [ 2.54, 1.31 ], "fq": 50 
  },
  "reverse": {
    "dict": "happiness", "word": "reverse", "stem": "revers",
    "avg": [ 5.64, 4.50 ], "std": [ 2.99, 1.11 ], "fq": 50 
  },
  "goo": {
    "dict": "happiness", "word": "goo", "stem": "goo",
    "avg": [ 5.36, 4.49 ], "std": [ 2.63, 1.59 ], "fq": 50 
  },
  "army": {
    "dict": "happiness", "word": "army", "stem": "armi",
    "avg": [ 5.03, 4.48 ], "std": [ 2.03, 2.01 ], "fq": 50 
  },
  "blow": {
    "dict": "happiness", "word": "blow", "stem": "blow",
    "avg": [ 4.14, 4.48 ], "std": [ 2.30, 1.74 ], "fq": 50 
  },
  "despite": {
    "dict": "happiness", "word": "despite", "stem": "despit",
    "avg": [ 5.04, 4.48 ], "std": [ 2.56, 1.34 ], "fq": 50 
  },
  "hidden": {
    "dict": "happiness", "word": "hidden", "stem": "hidden",
    "avg": [ 5.28, 4.48 ], "std": [ 2.51, 1.43 ], "fq": 50 
  },
  "issue": {
    "dict": "happiness", "word": "issue", "stem": "issu",
    "avg": [ 5.10, 4.48 ], "std": [ 2.40, 1.40 ], "fq": 50 
  },
  "commanded": {
    "dict": "happiness", "word": "commanded", "stem": "command",
    "avg": [ 6.10, 4.47 ], "std": [ 2.19, 1.60 ], "fq": 50 
  },
  "nerves": {
    "dict": "happiness", "word": "nerves", "stem": "nerv",
    "avg": [ 6.34, 4.47 ], "std": [ 2.25, 1.70 ], "fq": 50 
  },
  "spill": {
    "dict": "happiness", "word": "spill", "stem": "spill",
    "avg": [ 4.70, 4.47 ], "std": [ 2.48, 1.68 ], "fq": 50 
  },
  "craving": {
    "dict": "happiness", "word": "craving", "stem": "crave",
    "avg": [ 6.88, 4.46 ], "std": [ 1.85, 1.46 ], "fq": 50 
  },
  "hammer": {
    "dict": "happiness", "word": "hammer", "stem": "hammer",
    "avg": [ 4.58, 4.46 ], "std": [ 2.02, 1.54 ], "fq": 50 
  },
  "kicks": {
    "dict": "happiness", "word": "kicks", "stem": "kick",
    "avg": [ 4.90, 4.46 ], "std": [ 2.35, 1.57 ], "fq": 50 
  },
  "politics": {
    "dict": "happiness", "word": "politics", "stem": "polit",
    "avg": [ 3.74, 4.46 ], "std": [ 2.37, 1.76 ], "fq": 50 
  },
  "rigid": {
    "dict": "happiness", "word": "rigid", "stem": "rigid",
    "avg": [ 4.66, 4.46 ], "std": [ 2.47, 1.61 ], "fq": 50 
  },
  "short": {
    "dict": "happiness", "word": "short", "stem": "short",
    "avg": [ 5.73, 4.46 ], "std": [ 2.73, 1.15 ], "fq": 50 
  },
  "shy": {
    "dict": "happiness", "word": "shy", "stem": "shi",
    "avg": [ 3.77, 4.46 ], "std": [ 2.29, 1.74 ], "fq": 50 
  },
  "thrown": {
    "dict": "happiness", "word": "thrown", "stem": "thrown",
    "avg": [ 6.03, 4.46 ], "std": [ 1.88, 1.16 ], "fq": 50 
  },
  "tossed": {
    "dict": "happiness", "word": "tossed", "stem": "toss",
    "avg": [ 4.27, 4.46 ], "std": [ 2.17, 1.49 ], "fq": 50 
  },
  "infantry": {
    "dict": "happiness", "word": "infantry", "stem": "infantri",
    "avg": [ 3.27, 4.45 ], "std": [ 1.98, 2.08 ], "fq": 50 
  },
  "blank": {
    "dict": "happiness", "word": "blank", "stem": "blank",
    "avg": [ 5.14, 4.44 ], "std": [ 2.54, 0.84 ], "fq": 50 
  },
  "bottom": {
    "dict": "happiness", "word": "bottom", "stem": "bottom",
    "avg": [ 2.95, 4.44 ], "std": [ 1.72, 1.33 ], "fq": 50 
  },
  "cop": {
    "dict": "happiness", "word": "cop", "stem": "cop",
    "avg": [ 4.20, 4.44 ], "std": [ 2.42, 1.69 ], "fq": 50 
  },
  "errands": {
    "dict": "happiness", "word": "errands", "stem": "errand",
    "avg": [ 3.85, 4.44 ], "std": [ 1.92, 1.54 ], "fq": 50 
  },
  "gay": {
    "dict": "happiness", "word": "gay", "stem": "gay",
    "avg": [ 6.15, 4.44 ], "std": [ 2.45, 2.18 ], "fq": 50 
  },
  "harder": {
    "dict": "happiness", "word": "harder", "stem": "harder",
    "avg": [ 5.12, 4.44 ], "std": [ 2.19, 1.47 ], "fq": 50 
  },
  "push": {
    "dict": "happiness", "word": "push", "stem": "push",
    "avg": [ 6.44, 4.44 ], "std": [ 2.58, 1.47 ], "fq": 50 
  },
  "rag": {
    "dict": "happiness", "word": "rag", "stem": "rag",
    "avg": [ 5.76, 4.44 ], "std": [ 2.15, 1.26 ], "fq": 50 
  },
  "tank": {
    "dict": "happiness", "word": "tank", "stem": "tank",
    "avg": [ 4.88, 4.44 ], "std": [ 1.86, 1.61 ], "fq": 50 
  },
  "weed": {
    "dict": "happiness", "word": "weed", "stem": "weed",
    "avg": [ 4.14, 4.44 ], "std": [ 2.11, 2.10 ], "fq": 50 
  },
  "longing": {
    "dict": "happiness", "word": "longing", "stem": "long",
    "avg": [ 5.13, 4.43 ], "std": [ 2.44, 1.70 ], "fq": 50 
  },
  "behind": {
    "dict": "happiness", "word": "behind", "stem": "behind",
    "avg": [ 3.39, 4.42 ], "std": [ 2.22, 1.21 ], "fq": 50 
  },
  "breaks": {
    "dict": "happiness", "word": "breaks", "stem": "break",
    "avg": [ 4.07, 4.42 ], "std": [ 1.69, 1.83 ], "fq": 50 
  },
  "controlling": {
    "dict": "happiness", "word": "controlling", "stem": "control",
    "avg": [ 6.10, 4.42 ], "std": [ 2.19, 2.05 ], "fq": 50 
  },
  "emotional": {
    "dict": "happiness", "word": "emotional", "stem": "emot",
    "avg": [ 7.67, 4.42 ], "std": [ 1.91, 1.76 ], "fq": 50 
  },
  "hides": {
    "dict": "happiness", "word": "hides", "stem": "hide",
    "avg": [ 5.28, 4.42 ], "std": [ 2.51, 1.11 ], "fq": 50 
  },
  "remains": {
    "dict": "happiness", "word": "remains", "stem": "remain",
    "avg": [ 4.74, 4.42 ], "std": [ 2.94, 1.44 ], "fq": 50 
  },
  "serious": {
    "dict": "happiness", "word": "serious", "stem": "seriou",
    "avg": [ 5.43, 4.42 ], "std": [ 2.85, 1.46 ], "fq": 50 
  },
  "stumble": {
    "dict": "happiness", "word": "stumble", "stem": "stumbl",
    "avg": [ 5.73, 4.42 ], "std": [ 2.09, 1.58 ], "fq": 50 
  },
  "beats": {
    "dict": "happiness", "word": "beats", "stem": "beat",
    "avg": [ 5.52, 4.40 ], "std": [ 2.87, 1.93 ], "fq": 50 
  },
  "controlled": {
    "dict": "happiness", "word": "controlled", "stem": "control",
    "avg": [ 6.10, 4.40 ], "std": [ 2.19, 1.76 ], "fq": 50 
  },
  "desert": {
    "dict": "happiness", "word": "desert", "stem": "desert",
    "avg": [ 5.50, 4.40 ], "std": [ 2.55, 1.83 ], "fq": 50 
  },
  "hearings": {
    "dict": "happiness", "word": "hearings", "stem": "hear",
    "avg": [ 5.39, 4.40 ], "std": [ 2.22, 1.65 ], "fq": 50 
  },
  "tied": {
    "dict": "happiness", "word": "tied", "stem": "tie",
    "avg": [ 5.97, 4.40 ], "std": [ 2.85, 1.36 ], "fq": 50 
  },
  "authorities": {
    "dict": "happiness", "word": "authorities", "stem": "author",
    "avg": [ 4.08, 4.38 ], "std": [ 1.92, 1.16 ], "fq": 50 
  },
  "chills": {
    "dict": "happiness", "word": "chills", "stem": "chill",
    "avg": [ 8.02, 4.38 ], "std": [ 1.65, 1.76 ], "fq": 50 
  },
  "economy": {
    "dict": "happiness", "word": "economy", "stem": "economi",
    "avg": [ 4.95, 4.38 ], "std": [ 2.19, 1.66 ], "fq": 50 
  },
  "effing": {
    "dict": "happiness", "word": "effing", "stem": "ef",
    "avg": [ 6.38, 4.38 ], "std": [ 2.68, 1.40 ], "fq": 50 
  },
  "frozen": {
    "dict": "happiness", "word": "frozen", "stem": "frozen",
    "avg": [ 4.75, 4.38 ], "std": [ 2.56, 1.54 ], "fq": 50 
  },
  "prices": {
    "dict": "happiness", "word": "prices", "stem": "price",
    "avg": [ 5.57, 4.38 ], "std": [ 2.26, 1.60 ], "fq": 50 
  },
  "slips": {
    "dict": "happiness", "word": "slips", "stem": "slip",
    "avg": [ 5.18, 4.38 ], "std": [ 2.42, 1.47 ], "fq": 50 
  },
  "tangled": {
    "dict": "happiness", "word": "tangled", "stem": "tangl",
    "avg": [ 4.07, 4.38 ], "std": [ 2.15, 1.60 ], "fq": 50 
  },
  "consequence": {
    "dict": "happiness", "word": "consequence", "stem": "consequ",
    "avg": [ 3.83, 4.36 ], "std": [ 2.29, 1.32 ], "fq": 50 
  },
  "custody": {
    "dict": "happiness", "word": "custody", "stem": "custodi",
    "avg": [ 4.40, 4.36 ], "std": [ 2.07, 1.70 ], "fq": 50 
  },
  "divided": {
    "dict": "happiness", "word": "divided", "stem": "divid",
    "avg": [ 3.82, 4.36 ], "std": [ 2.24, 1.27 ], "fq": 50 
  },
  "division": {
    "dict": "happiness", "word": "division", "stem": "divis",
    "avg": [ 3.82, 4.36 ], "std": [ 2.24, 1.29 ], "fq": 50 
  },
  "end": {
    "dict": "happiness", "word": "end", "stem": "end",
    "avg": [ 4.59, 4.36 ], "std": [ 3.07, 1.74 ], "fq": 50 
  },
  "grease": {
    "dict": "happiness", "word": "grease", "stem": "greas",
    "avg": [ 5.12, 4.36 ], "std": [ 2.32, 1.34 ], "fq": 50 
  },
  "hide": {
    "dict": "happiness", "word": "hide", "stem": "hide",
    "avg": [ 5.28, 4.36 ], "std": [ 2.51, 1.41 ], "fq": 50 
  },
  "needle": {
    "dict": "happiness", "word": "needle", "stem": "needl",
    "avg": [ 5.36, 4.36 ], "std": [ 2.89, 1.83 ], "fq": 50 
  },
  "operations": {
    "dict": "happiness", "word": "operations", "stem": "oper",
    "avg": [ 6.35, 4.36 ], "std": [ 2.32, 1.77 ], "fq": 50 
  },
  "reducing": {
    "dict": "happiness", "word": "reducing", "stem": "reduc",
    "avg": [ 4.65, 4.36 ], "std": [ 2.13, 1.48 ], "fq": 50 
  },
  "sharply": {
    "dict": "happiness", "word": "sharply", "stem": "sharpli",
    "avg": [ 5.83, 4.36 ], "std": [ 2.33, 1.64 ], "fq": 50 
  },
  "tease": {
    "dict": "happiness", "word": "tease", "stem": "teas",
    "avg": [ 5.87, 4.36 ], "std": [ 2.56, 2.09 ], "fq": 50 
  },
  "storms": {
    "dict": "happiness", "word": "storms", "stem": "storm",
    "avg": [ 5.71, 4.34 ], "std": [ 2.34, 1.98 ], "fq": 50 
  },
  "blown": {
    "dict": "happiness", "word": "blown", "stem": "blown",
    "avg": [ 4.14, 4.34 ], "std": [ 2.30, 1.39 ], "fq": 50 
  },
  "congress": {
    "dict": "happiness", "word": "congress", "stem": "congress",
    "avg": [ 7.00, 4.34 ], "std": [ 2.07, 1.76 ], "fq": 50 
  },
  "ditch": {
    "dict": "happiness", "word": "ditch", "stem": "ditch",
    "avg": [ 4.12, 4.34 ], "std": [ 2.36, 1.55 ], "fq": 50 
  },
  "hiding": {
    "dict": "happiness", "word": "hiding", "stem": "hide",
    "avg": [ 5.28, 4.34 ], "std": [ 2.51, 1.29 ], "fq": 50 
  },
  "icy": {
    "dict": "happiness", "word": "icy", "stem": "ici",
    "avg": [ 4.75, 4.34 ], "std": [ 2.56, 1.85 ], "fq": 50 
  },
  "shook": {
    "dict": "happiness", "word": "shook", "stem": "shook",
    "avg": [ 7.67, 4.34 ], "std": [ 1.91, 1.42 ], "fq": 50 
  },
  "vampire": {
    "dict": "happiness", "word": "vampire", "stem": "vampir",
    "avg": [ 6.37, 4.34 ], "std": [ 2.35, 2.12 ], "fq": 50 
  },
  "eff": {
    "dict": "happiness", "word": "eff", "stem": "eff",
    "avg": [ 6.38, 4.32 ], "std": [ 2.68, 1.57 ], "fq": 50 
  },
  "howling": {
    "dict": "happiness", "word": "howling", "stem": "howl",
    "avg": [ 6.23, 4.32 ], "std": [ 2.73, 1.83 ], "fq": 50 
  },
  "reduced": {
    "dict": "happiness", "word": "reduced", "stem": "reduc",
    "avg": [ 4.65, 4.32 ], "std": [ 2.13, 1.58 ], "fq": 50 
  },
  "scattered": {
    "dict": "happiness", "word": "scattered", "stem": "scatter",
    "avg": [ 6.03, 4.32 ], "std": [ 1.88, 1.35 ], "fq": 50 
  },
  "separate": {
    "dict": "happiness", "word": "separate", "stem": "separ",
    "avg": [ 3.96, 4.32 ], "std": [ 1.94, 1.56 ], "fq": 50 
  },
  "slowly": {
    "dict": "happiness", "word": "slowly", "stem": "slowli",
    "avg": [ 3.39, 4.32 ], "std": [ 2.22, 1.43 ], "fq": 50 
  },
  "tripping": {
    "dict": "happiness", "word": "tripping", "stem": "trip",
    "avg": [ 6.21, 4.32 ], "std": [ 2.51, 1.87 ], "fq": 50 
  },
  "blunt": {
    "dict": "happiness", "word": "blunt", "stem": "blunt",
    "avg": [ 5.07, 4.31 ], "std": [ 2.37, 1.52 ], "fq": 50 
  },
  "shaking": {
    "dict": "happiness", "word": "shaking", "stem": "shake",
    "avg": [ 7.67, 4.31 ], "std": [ 1.91, 1.75 ], "fq": 50 
  },
  "smack": {
    "dict": "happiness", "word": "smack", "stem": "smack",
    "avg": [ 6.46, 4.31 ], "std": [ 2.58, 2.00 ], "fq": 50 
  },
  "affected": {
    "dict": "happiness", "word": "affected", "stem": "affect",
    "avg": [ 6.21, 4.30 ], "std": [ 2.75, 1.39 ], "fq": 50 
  },
  "drop": {
    "dict": "happiness", "word": "drop", "stem": "drop",
    "avg": [ 4.70, 4.30 ], "std": [ 2.48, 1.20 ], "fq": 50 
  },
  "pit": {
    "dict": "happiness", "word": "pit", "stem": "pit",
    "avg": [ 4.79, 4.30 ], "std": [ 2.11, 1.02 ], "fq": 50 
  },
  "sneak": {
    "dict": "happiness", "word": "sneak", "stem": "sneak",
    "avg": [ 4.59, 4.30 ], "std": [ 2.10, 1.54 ], "fq": 50 
  },
  "chased": {
    "dict": "happiness", "word": "chased", "stem": "chase",
    "avg": [ 5.76, 4.29 ], "std": [ 2.50, 1.63 ], "fq": 50 
  },
  "divide": {
    "dict": "happiness", "word": "divide", "stem": "divid",
    "avg": [ 3.82, 4.29 ], "std": [ 2.24, 1.46 ], "fq": 50 
  },
  "mortal": {
    "dict": "happiness", "word": "mortal", "stem": "mortal",
    "avg": [ 4.19, 4.29 ], "std": [ 2.45, 2.03 ], "fq": 50 
  },
  "rebellion": {
    "dict": "happiness", "word": "rebellion", "stem": "rebellion",
    "avg": [ 6.56, 4.29 ], "std": [ 2.34, 1.68 ], "fq": 50 
  },
  "petroleum": {
    "dict": "happiness", "word": "petroleum", "stem": "petroleum",
    "avg": [ 5.07, 4.28 ], "std": [ 2.37, 1.63 ], "fq": 50 
  },
  "spider": {
    "dict": "happiness", "word": "spider", "stem": "spider",
    "avg": [ 5.71, 4.28 ], "std": [ 2.21, 2.00 ], "fq": 50 
  },
  "swore": {
    "dict": "happiness", "word": "swore", "stem": "swore",
    "avg": [ 5.30, 4.28 ], "std": [ 2.66, 1.58 ], "fq": 50 
  },
  "taken": {
    "dict": "happiness", "word": "taken", "stem": "taken",
    "avg": [ 5.39, 4.28 ], "std": [ 2.22, 1.47 ], "fq": 50 
  },
  "warn": {
    "dict": "happiness", "word": "warn", "stem": "warn",
    "avg": [ 4.53, 4.27 ], "std": [ 2.11, 1.72 ], "fq": 50 
  },
  "blows": {
    "dict": "happiness", "word": "blows", "stem": "blow",
    "avg": [ 4.14, 4.26 ], "std": [ 2.30, 1.76 ], "fq": 50 
  },
  "fires": {
    "dict": "happiness", "word": "fires", "stem": "fire",
    "avg": [ 7.17, 4.26 ], "std": [ 2.06, 1.74 ], "fq": 50 
  },
  "outlaw": {
    "dict": "happiness", "word": "outlaw", "stem": "outlaw",
    "avg": [ 4.79, 4.26 ], "std": [ 2.51, 1.70 ], "fq": 50 
  },
  "owing": {
    "dict": "happiness", "word": "owing", "stem": "owe",
    "avg": [ 6.24, 4.26 ], "std": [ 2.59, 1.95 ], "fq": 50 
  },
  "split": {
    "dict": "happiness", "word": "split", "stem": "split",
    "avg": [ 3.82, 4.26 ], "std": [ 2.24, 1.50 ], "fq": 50 
  },
  "storm": {
    "dict": "happiness", "word": "storm", "stem": "storm",
    "avg": [ 5.71, 4.26 ], "std": [ 2.34, 2.01 ], "fq": 50 
  },
  "concerning": {
    "dict": "happiness", "word": "concerning", "stem": "concern",
    "avg": [ 5.66, 4.24 ], "std": [ 2.26, 1.69 ], "fq": 50 
  },
  "lower": {
    "dict": "happiness", "word": "lower", "stem": "lower",
    "avg": [ 4.31, 4.24 ], "std": [ 2.20, 1.08 ], "fq": 50 
  },
  "pounding": {
    "dict": "happiness", "word": "pounding", "stem": "pound",
    "avg": [ 4.58, 4.24 ], "std": [ 2.02, 2.03 ], "fq": 50 
  },
  "questioned": {
    "dict": "happiness", "word": "questioned", "stem": "question",
    "avg": [ 5.00, 4.24 ], "std": [ 2.23, 1.27 ], "fq": 50 
  },
  "raw": {
    "dict": "happiness", "word": "raw", "stem": "raw",
    "avg": [ 5.00, 4.24 ], "std": [ 2.32, 1.29 ], "fq": 50 
  },
  "sag": {
    "dict": "happiness", "word": "sag", "stem": "sag",
    "avg": [ 4.60, 4.24 ], "std": [ 2.35, 1.32 ], "fq": 50 
  },
  "smash": {
    "dict": "happiness", "word": "smash", "stem": "smash",
    "avg": [ 5.73, 4.24 ], "std": [ 2.09, 1.57 ], "fq": 50 
  },
  "stern": {
    "dict": "happiness", "word": "stern", "stem": "stern",
    "avg": [ 5.26, 4.24 ], "std": [ 2.36, 1.36 ], "fq": 50 
  },
  "swear": {
    "dict": "happiness", "word": "swear", "stem": "swear",
    "avg": [ 5.30, 4.24 ], "std": [ 2.66, 1.62 ], "fq": 50 
  },
  "worn": {
    "dict": "happiness", "word": "worn", "stem": "worn",
    "avg": [ 2.64, 4.23 ], "std": [ 2.19, 1.10 ], "fq": 50 
  },
  "freaks": {
    "dict": "happiness", "word": "freaks", "stem": "freak",
    "avg": [ 4.81, 4.22 ], "std": [ 2.46, 2.00 ], "fq": 50 
  },
  "beware": {
    "dict": "happiness", "word": "beware", "stem": "bewar",
    "avg": [ 5.00, 4.22 ], "std": [ 2.68, 1.67 ], "fq": 50 
  },
  "blast": {
    "dict": "happiness", "word": "blast", "stem": "blast",
    "avg": [ 6.47, 4.22 ], "std": [ 2.47, 2.12 ], "fq": 50 
  },
  "cold": {
    "dict": "happiness", "word": "cold", "stem": "cold",
    "avg": [ 5.19, 4.22 ], "std": [ 2.23, 1.78 ], "fq": 50 
  },
  "concerned": {
    "dict": "happiness", "word": "concerned", "stem": "concern",
    "avg": [ 5.66, 4.22 ], "std": [ 2.26, 1.66 ], "fq": 50 
  },
  "grind": {
    "dict": "happiness", "word": "grind", "stem": "grind",
    "avg": [ 4.58, 4.22 ], "std": [ 2.14, 1.37 ], "fq": 50 
  },
  "python": {
    "dict": "happiness", "word": "python", "stem": "python",
    "avg": [ 6.18, 4.22 ], "std": [ 2.25, 1.80 ], "fq": 50 
  },
  "scratch": {
    "dict": "happiness", "word": "scratch", "stem": "scratch",
    "avg": [ 4.79, 4.22 ], "std": [ 2.11, 1.37 ], "fq": 50 
  },
  "beat": {
    "dict": "happiness", "word": "beat", "stem": "beat",
    "avg": [ 5.52, 4.20 ], "std": [ 2.87, 1.98 ], "fq": 50 
  },
  "lone": {
    "dict": "happiness", "word": "lone", "stem": "lone",
    "avg": [ 4.51, 4.20 ], "std": [ 2.68, 1.56 ], "fq": 50 
  },
  "politically": {
    "dict": "happiness", "word": "politically", "stem": "polit",
    "avg": [ 3.74, 4.20 ], "std": [ 2.37, 1.37 ], "fq": 50 
  },
  "screw": {
    "dict": "happiness", "word": "screw", "stem": "screw",
    "avg": [ 6.38, 4.20 ], "std": [ 2.68, 1.85 ], "fq": 50 
  },
  "whips": {
    "dict": "happiness", "word": "whips", "stem": "whip",
    "avg": [ 4.10, 4.20 ], "std": [ 2.34, 1.91 ], "fq": 50 
  },
  "capture": {
    "dict": "happiness", "word": "capture", "stem": "captur",
    "avg": [ 5.83, 4.18 ], "std": [ 2.73, 1.70 ], "fq": 50 
  },
  "forces": {
    "dict": "happiness", "word": "forces", "stem": "forc",
    "avg": [ 6.07, 4.18 ], "std": [ 2.26, 1.59 ], "fq": 50 
  },
  "reduce": {
    "dict": "happiness", "word": "reduce", "stem": "reduc",
    "avg": [ 4.65, 4.18 ], "std": [ 2.13, 1.26 ], "fq": 50 
  },
  "smells": {
    "dict": "happiness", "word": "smells", "stem": "smell",
    "avg": [ 5.56, 4.18 ], "std": [ 2.62, 1.59 ], "fq": 50 
  },
  "gambling": {
    "dict": "happiness", "word": "gambling", "stem": "gambl",
    "avg": [ 5.89, 4.16 ], "std": [ 2.37, 1.99 ], "fq": 50 
  },
  "heat": {
    "dict": "happiness", "word": "heat", "stem": "heat",
    "avg": [ 7.26, 4.16 ], "std": [ 2.57, 1.82 ], "fq": 50 
  },
  "stranger": {
    "dict": "happiness", "word": "stranger", "stem": "stranger",
    "avg": [ 5.45, 4.16 ], "std": [ 2.15, 0.96 ], "fq": 50 
  },
  "strangers": {
    "dict": "happiness", "word": "strangers", "stem": "stranger",
    "avg": [ 5.45, 4.16 ], "std": [ 2.15, 1.75 ], "fq": 50 
  },
  "sucking": {
    "dict": "happiness", "word": "sucking", "stem": "suck",
    "avg": [ 4.84, 4.16 ], "std": [ 2.04, 1.73 ], "fq": 50 
  },
  "fuck": {
    "dict": "happiness", "word": "fuck", "stem": "fuck",
    "avg": [ 6.38, 4.14 ], "std": [ 2.68, 2.58 ], "fq": 50 
  },
  "pee": {
    "dict": "happiness", "word": "pee", "stem": "pee",
    "avg": [ 4.20, 4.14 ], "std": [ 2.18, 1.53 ], "fq": 50 
  },
  "pushing": {
    "dict": "happiness", "word": "pushing", "stem": "push",
    "avg": [ 6.44, 4.14 ], "std": [ 2.58, 1.32 ], "fq": 50 
  },
  "shark": {
    "dict": "happiness", "word": "shark", "stem": "shark",
    "avg": [ 7.16, 4.14 ], "std": [ 1.96, 1.92 ], "fq": 50 
  },
  "strict": {
    "dict": "happiness", "word": "strict", "stem": "strict",
    "avg": [ 4.66, 4.13 ], "std": [ 2.47, 1.76 ], "fq": 50 
  },
  "decrease": {
    "dict": "happiness", "word": "decrease", "stem": "decreas",
    "avg": [ 4.70, 4.12 ], "std": [ 2.48, 1.55 ], "fq": 50 
  },
  "bother": {
    "dict": "happiness", "word": "bother", "stem": "bother",
    "avg": [ 5.76, 4.12 ], "std": [ 2.15, 1.62 ], "fq": 50 
  },
  "fuss": {
    "dict": "happiness", "word": "fuss", "stem": "fuss",
    "avg": [ 5.94, 4.12 ], "std": [ 2.36, 1.78 ], "fq": 50 
  },
  "nonsense": {
    "dict": "happiness", "word": "nonsense", "stem": "nonsens",
    "avg": [ 4.17, 4.12 ], "std": [ 2.02, 1.60 ], "fq": 50 
  },
  "political": {
    "dict": "happiness", "word": "political", "stem": "polit",
    "avg": [ 3.74, 4.12 ], "std": [ 2.37, 1.52 ], "fq": 50 
  },
  "rush": {
    "dict": "happiness", "word": "rush", "stem": "rush",
    "avg": [ 4.90, 4.12 ], "std": [ 2.35, 1.36 ], "fq": 50 
  },
  "twisted": {
    "dict": "happiness", "word": "twisted", "stem": "twist",
    "avg": [ 6.26, 4.12 ], "std": [ 2.61, 1.67 ], "fq": 50 
  },
  "hard": {
    "dict": "happiness", "word": "hard", "stem": "hard",
    "avg": [ 5.12, 4.10 ], "std": [ 2.19, 1.39 ], "fq": 50 
  },
  "heavy": {
    "dict": "happiness", "word": "heavy", "stem": "heavi",
    "avg": [ 5.12, 4.10 ], "std": [ 2.19, 1.42 ], "fq": 50 
  },
  "numb": {
    "dict": "happiness", "word": "numb", "stem": "numb",
    "avg": [ 5.73, 4.10 ], "std": [ 2.73, 1.63 ], "fq": 50 
  },
  "pushed": {
    "dict": "happiness", "word": "pushed", "stem": "push",
    "avg": [ 6.44, 4.10 ], "std": [ 2.58, 1.47 ], "fq": 50 
  },
  "rid": {
    "dict": "happiness", "word": "rid", "stem": "rid",
    "avg": [ 5.15, 4.10 ], "std": [ 3.04, 1.42 ], "fq": 50 
  },
  "weary": {
    "dict": "happiness", "word": "weary", "stem": "weari",
    "avg": [ 3.81, 4.08 ], "std": [ 2.29, 1.62 ], "fq": 50 
  },
  "cutting": {
    "dict": "happiness", "word": "cutting", "stem": "cut",
    "avg": [ 5.00, 4.08 ], "std": [ 2.32, 1.40 ], "fq": 50 
  },
  "hung": {
    "dict": "happiness", "word": "hung", "stem": "hung",
    "avg": [ 4.70, 4.08 ], "std": [ 2.48, 1.63 ], "fq": 50 
  },
  "knife": {
    "dict": "happiness", "word": "knife", "stem": "knife",
    "avg": [ 5.80, 4.08 ], "std": [ 2.00, 1.40 ], "fq": 50 
  },
  "stopping": {
    "dict": "happiness", "word": "stopping", "stem": "stop",
    "avg": [ 5.00, 4.08 ], "std": [ 2.83, 1.40 ], "fq": 50 
  },
  "surrender": {
    "dict": "happiness", "word": "surrender", "stem": "surrend",
    "avg": [ 4.70, 4.08 ], "std": [ 2.48, 1.68 ], "fq": 50 
  },
  "temper": {
    "dict": "happiness", "word": "temper", "stem": "temper",
    "avg": [ 5.50, 4.08 ], "std": [ 2.91, 1.79 ], "fq": 50 
  },
  "wont": {
    "dict": "happiness", "word": "wont", "stem": "wont",
    "avg": [ 3.95, 4.08 ], "std": [ 2.11, 1.05 ], "fq": 50 
  },
  "blinding": {
    "dict": "happiness", "word": "blinding", "stem": "blind",
    "avg": [ 4.39, 4.06 ], "std": [ 2.36, 1.67 ], "fq": 50 
  },
  "concerns": {
    "dict": "happiness", "word": "concerns", "stem": "concern",
    "avg": [ 5.07, 4.06 ], "std": [ 2.74, 1.56 ], "fq": 50 
  },
  "sour": {
    "dict": "happiness", "word": "sour", "stem": "sour",
    "avg": [ 5.10, 4.06 ], "std": [ 1.95, 1.50 ], "fq": 50 
  },
  "needles": {
    "dict": "happiness", "word": "needles", "stem": "needl",
    "avg": [ 5.36, 4.04 ], "std": [ 2.89, 1.99 ], "fq": 50 
  },
  "colder": {
    "dict": "happiness", "word": "colder", "stem": "colder",
    "avg": [ 4.75, 4.04 ], "std": [ 2.56, 1.96 ], "fq": 50 
  },
  "concern": {
    "dict": "happiness", "word": "concern", "stem": "concern",
    "avg": [ 5.07, 4.04 ], "std": [ 2.74, 1.62 ], "fq": 50 
  },
  "discharge": {
    "dict": "happiness", "word": "discharge", "stem": "discharg",
    "avg": [ 7.17, 4.04 ], "std": [ 2.06, 1.78 ], "fq": 50 
  },
  "dominated": {
    "dict": "happiness", "word": "dominated", "stem": "domin",
    "avg": [ 5.20, 4.04 ], "std": [ 2.85, 1.52 ], "fq": 50 
  },
  "fall": {
    "dict": "happiness", "word": "fall", "stem": "fall",
    "avg": [ 4.70, 4.04 ], "std": [ 2.48, 1.97 ], "fq": 50 
  },
  "unknown": {
    "dict": "happiness", "word": "unknown", "stem": "unknown",
    "avg": [ 5.45, 4.04 ], "std": [ 2.15, 1.51 ], "fq": 50 
  },
  "worm": {
    "dict": "happiness", "word": "worm", "stem": "worm",
    "avg": [ 4.98, 4.04 ], "std": [ 2.03, 1.67 ], "fq": 50 
  },
  "rust": {
    "dict": "happiness", "word": "rust", "stem": "rust",
    "avg": [ 3.77, 4.02 ], "std": [ 2.16, 1.63 ], "fq": 50 
  },
  "distant": {
    "dict": "happiness", "word": "distant", "stem": "distant",
    "avg": [ 4.28, 4.02 ], "std": [ 2.10, 1.53 ], "fq": 50 
  },
  "block": {
    "dict": "happiness", "word": "block", "stem": "block",
    "avg": [ 4.12, 4.02 ], "std": [ 2.01, 1.42 ], "fq": 50 
  },
  "consequences": {
    "dict": "happiness", "word": "consequences", "stem": "consequ",
    "avg": [ 3.83, 4.02 ], "std": [ 2.29, 1.32 ], "fq": 50 
  },
  "dropping": {
    "dict": "happiness", "word": "dropping", "stem": "drop",
    "avg": [ 4.70, 4.02 ], "std": [ 2.48, 1.10 ], "fq": 50 
  },
  "strikes": {
    "dict": "happiness", "word": "strikes", "stem": "strike",
    "avg": [ 5.73, 4.02 ], "std": [ 2.09, 1.36 ], "fq": 50 
  },
  "bum": {
    "dict": "happiness", "word": "bum", "stem": "bum",
    "avg": [ 4.95, 4.00 ], "std": [ 2.36, 1.73 ], "fq": 50 
  },
  "cracks": {
    "dict": "happiness", "word": "cracks", "stem": "crack",
    "avg": [ 6.83, 4.00 ], "std": [ 2.49, 1.36 ], "fq": 50 
  },
  "force": {
    "dict": "happiness", "word": "force", "stem": "forc",
    "avg": [ 6.07, 4.00 ], "std": [ 2.26, 1.69 ], "fq": 50 
  },
  "ridiculous": {
    "dict": "happiness", "word": "ridiculous", "stem": "ridicul",
    "avg": [ 5.83, 4.00 ], "std": [ 2.73, 1.80 ], "fq": 50 
  },
  "roughly": {
    "dict": "happiness", "word": "roughly", "stem": "roughli",
    "avg": [ 5.33, 4.00 ], "std": [ 2.04, 1.21 ], "fq": 50 
  },
  "twit": {
    "dict": "happiness", "word": "twit", "stem": "twit",
    "avg": [ 5.87, 4.00 ], "std": [ 2.56, 1.76 ], "fq": 50 
  },
  "bite": {
    "dict": "happiness", "word": "bite", "stem": "bite",
    "avg": [ 4.70, 3.98 ], "std": [ 2.59, 1.72 ], "fq": 50 
  },
  "breaking": {
    "dict": "happiness", "word": "breaking", "stem": "break",
    "avg": [ 6.21, 3.98 ], "std": [ 2.79, 1.49 ], "fq": 50 
  },
  "ruins": {
    "dict": "happiness", "word": "ruins", "stem": "ruin",
    "avg": [ 6.21, 3.98 ], "std": [ 2.79, 1.76 ], "fq": 50 
  },
  "bang": {
    "dict": "happiness", "word": "bang", "stem": "bang",
    "avg": [ 6.38, 3.96 ], "std": [ 2.68, 1.48 ], "fq": 50 
  },
  "dagger": {
    "dict": "happiness", "word": "dagger", "stem": "dagger",
    "avg": [ 6.14, 3.96 ], "std": [ 2.64, 1.32 ], "fq": 50 
  },
  "loose": {
    "dict": "happiness", "word": "loose", "stem": "loos",
    "avg": [ 4.48, 3.96 ], "std": [ 2.82, 1.65 ], "fq": 50 
  },
  "slugs": {
    "dict": "happiness", "word": "slugs", "stem": "slug",
    "avg": [ 5.33, 3.96 ], "std": [ 2.48, 1.64 ], "fq": 50 
  },
  "strike": {
    "dict": "happiness", "word": "strike", "stem": "strike",
    "avg": [ 5.73, 3.96 ], "std": [ 2.09, 1.35 ], "fq": 50 
  },
  "tough": {
    "dict": "happiness", "word": "tough", "stem": "tough",
    "avg": [ 5.12, 3.96 ], "std": [ 2.19, 1.41 ], "fq": 50 
  },
  "skull": {
    "dict": "happiness", "word": "skull", "stem": "skull",
    "avg": [ 4.75, 3.96 ], "std": [ 1.85, 1.63 ], "fq": 50 
  },
  "charges": {
    "dict": "happiness", "word": "charges", "stem": "charg",
    "avg": [ 7.67, 3.94 ], "std": [ 1.91, 1.53 ], "fq": 50 
  },
  "darker": {
    "dict": "happiness", "word": "darker", "stem": "darker",
    "avg": [ 4.73, 3.94 ], "std": [ 2.64, 1.90 ], "fq": 50 
  },
  "mess": {
    "dict": "happiness", "word": "mess", "stem": "mess",
    "avg": [ 3.34, 3.94 ], "std": [ 2.37, 1.57 ], "fq": 50 
  },
  "dizzy": {
    "dict": "happiness", "word": "dizzy", "stem": "dizzi",
    "avg": [ 5.88, 3.94 ], "std": [ 2.38, 1.72 ], "fq": 50 
  },
  "executed": {
    "dict": "happiness", "word": "executed", "stem": "execut",
    "avg": [ 5.71, 3.94 ], "std": [ 2.74, 2.20 ], "fq": 50 
  },
  "omitted": {
    "dict": "happiness", "word": "omitted", "stem": "omit",
    "avg": [ 4.83, 3.92 ], "std": [ 2.31, 1.21 ], "fq": 50 
  },
  "jaded": {
    "dict": "happiness", "word": "jaded", "stem": "jade",
    "avg": [ 2.64, 3.92 ], "std": [ 2.19, 1.66 ], "fq": 50 
  },
  "dusty": {
    "dict": "happiness", "word": "dusty", "stem": "dusti",
    "avg": [ 5.19, 3.92 ], "std": [ 2.23, 1.70 ], "fq": 50 
  },
  "alarm": {
    "dict": "happiness", "word": "alarm", "stem": "alarm",
    "avg": [ 6.85, 3.90 ], "std": [ 2.53, 1.66 ], "fq": 50 
  },
  "dim": {
    "dict": "happiness", "word": "dim", "stem": "dim",
    "avg": [ 4.39, 3.90 ], "std": [ 2.36, 1.34 ], "fq": 50 
  },
  "issues": {
    "dict": "happiness", "word": "issues", "stem": "issu",
    "avg": [ 5.10, 3.90 ], "std": [ 2.40, 1.37 ], "fq": 50 
  },
  "misses": {
    "dict": "happiness", "word": "misses", "stem": "miss",
    "avg": [ 4.29, 3.90 ], "std": [ 2.69, 1.37 ], "fq": 50 
  },
  "slipping": {
    "dict": "happiness", "word": "slipping", "stem": "slip",
    "avg": [ 5.18, 3.90 ], "std": [ 2.42, 1.45 ], "fq": 50 
  },
  "stop": {
    "dict": "happiness", "word": "stop", "stem": "stop",
    "avg": [ 5.00, 3.90 ], "std": [ 2.83, 1.34 ], "fq": 50 
  },
  "dropped": {
    "dict": "happiness", "word": "dropped", "stem": "drop",
    "avg": [ 4.83, 3.88 ], "std": [ 2.31, 1.00 ], "fq": 50 
  },
  "drunk": {
    "dict": "happiness", "word": "drunk", "stem": "drunk",
    "avg": [ 5.31, 3.88 ], "std": [ 2.23, 2.25 ], "fq": 50 
  },
  "shout": {
    "dict": "happiness", "word": "shout", "stem": "shout",
    "avg": [ 6.83, 3.88 ], "std": [ 2.70, 1.38 ], "fq": 50 
  },
  "artillery": {
    "dict": "happiness", "word": "artillery", "stem": "artilleri",
    "avg": [ 6.03, 3.88 ], "std": [ 1.89, 1.54 ], "fq": 50 
  },
  "goddamn": {
    "dict": "happiness", "word": "goddamn", "stem": "goddamn",
    "avg": [ 4.05, 3.88 ], "std": [ 2.59, 2.18 ], "fq": 50 
  },
  "rags": {
    "dict": "happiness", "word": "rags", "stem": "rag",
    "avg": [ 5.76, 3.88 ], "std": [ 2.15, 1.54 ], "fq": 50 
  },
  "fiends": {
    "dict": "happiness", "word": "fiends", "stem": "fiend",
    "avg": [ 6.07, 3.88 ], "std": [ 2.61, 1.92 ], "fq": 50 
  },
  "ass": {
    "dict": "happiness", "word": "ass", "stem": "ass",
    "avg": [ 2.95, 3.86 ], "std": [ 1.72, 1.86 ], "fq": 50 
  },
  "farewell": {
    "dict": "happiness", "word": "farewell", "stem": "farewel",
    "avg": [ 3.82, 3.86 ], "std": [ 2.24, 2.13 ], "fq": 50 
  },
  "hang": {
    "dict": "happiness", "word": "hang", "stem": "hang",
    "avg": [ 4.70, 3.86 ], "std": [ 2.48, 1.32 ], "fq": 50 
  },
  "stopped": {
    "dict": "happiness", "word": "stopped", "stem": "stop",
    "avg": [ 5.00, 3.86 ], "std": [ 2.83, 1.23 ], "fq": 50 
  },
  "slipped": {
    "dict": "happiness", "word": "slipped", "stem": "slip",
    "avg": [ 5.18, 3.86 ], "std": [ 2.42, 1.58 ], "fq": 50 
  },
  "mold": {
    "dict": "happiness", "word": "mold", "stem": "mold",
    "avg": [ 4.07, 3.85 ], "std": [ 1.98, 1.80 ], "fq": 50 
  },
  "shiver": {
    "dict": "happiness", "word": "shiver", "stem": "shiver",
    "avg": [ 8.02, 3.85 ], "std": [ 1.65, 1.49 ], "fq": 50 
  },
  "armed": {
    "dict": "happiness", "word": "armed", "stem": "arm",
    "avg": [ 3.59, 3.84 ], "std": [ 2.40, 1.86 ], "fq": 50 
  },
  "excuses": {
    "dict": "happiness", "word": "excuses", "stem": "excus",
    "avg": [ 4.48, 3.84 ], "std": [ 2.29, 1.52 ], "fq": 50 
  },
  "gripe": {
    "dict": "happiness", "word": "gripe", "stem": "gripe",
    "avg": [ 5.00, 3.84 ], "std": [ 2.19, 1.87 ], "fq": 50 
  },
  "rent": {
    "dict": "happiness", "word": "rent", "stem": "rent",
    "avg": [ 6.77, 3.84 ], "std": [ 2.07, 1.48 ], "fq": 50 
  },
  "snatch": {
    "dict": "happiness", "word": "snatch", "stem": "snatch",
    "avg": [ 5.53, 3.84 ], "std": [ 2.43, 1.63 ], "fq": 50 
  },
  "ghosts": {
    "dict": "happiness", "word": "ghosts", "stem": "ghost",
    "avg": [ 6.41, 3.84 ], "std": [ 2.13, 1.98 ], "fq": 50 
  },
  "dark": {
    "dict": "happiness", "word": "dark", "stem": "dark",
    "avg": [ 4.28, 3.82 ], "std": [ 2.21, 1.41 ], "fq": 50 
  },
  "darkness": {
    "dict": "happiness", "word": "darkness", "stem": "dark",
    "avg": [ 4.28, 3.82 ], "std": [ 2.21, 1.87 ], "fq": 50 
  },
  "eliminate": {
    "dict": "happiness", "word": "eliminate", "stem": "elimin",
    "avg": [ 6.37, 3.82 ], "std": [ 2.56, 1.75 ], "fq": 50 
  },
  "hanging": {
    "dict": "happiness", "word": "hanging", "stem": "hang",
    "avg": [ 4.70, 3.82 ], "std": [ 2.48, 1.72 ], "fq": 50 
  },
  "hardest": {
    "dict": "happiness", "word": "hardest", "stem": "hardest",
    "avg": [ 5.12, 3.82 ], "std": [ 2.19, 1.62 ], "fq": 50 
  },
  "junk": {
    "dict": "happiness", "word": "junk", "stem": "junk",
    "avg": [ 4.16, 3.82 ], "std": [ 2.16, 1.34 ], "fq": 50 
  },
  "oppose": {
    "dict": "happiness", "word": "oppose", "stem": "oppos",
    "avg": [ 7.15, 3.82 ], "std": [ 2.19, 1.44 ], "fq": 50 
  },
  "slip": {
    "dict": "happiness", "word": "slip", "stem": "slip",
    "avg": [ 5.18, 3.82 ], "std": [ 2.42, 1.29 ], "fq": 50 
  },
  "thirst": {
    "dict": "happiness", "word": "thirst", "stem": "thirst",
    "avg": [ 6.88, 3.82 ], "std": [ 1.85, 1.72 ], "fq": 50 
  },
  "aggressive": {
    "dict": "happiness", "word": "aggressive", "stem": "aggress",
    "avg": [ 5.83, 3.80 ], "std": [ 2.33, 1.58 ], "fq": 50 
  },
  "fire": {
    "dict": "happiness", "word": "fire", "stem": "fire",
    "avg": [ 7.17, 3.80 ], "std": [ 2.06, 1.58 ], "fq": 50 
  },
  "interment": {
    "dict": "happiness", "word": "interment", "stem": "inter",
    "avg": [ 5.08, 3.80 ], "std": [ 2.40, 1.83 ], "fq": 50 
  },
  "pale": {
    "dict": "happiness", "word": "pale", "stem": "pale",
    "avg": [ 5.61, 3.80 ], "std": [ 2.67, 1.09 ], "fq": 50 
  },
  "witch": {
    "dict": "happiness", "word": "witch", "stem": "witch",
    "avg": [ 4.68, 3.80 ], "std": [ 2.23, 2.09 ], "fq": 50 
  },
  "thirsty": {
    "dict": "happiness", "word": "thirsty", "stem": "thirsti",
    "avg": [ 5.13, 3.79 ], "std": [ 2.44, 1.46 ], "fq": 50 
  },
  "thorns": {
    "dict": "happiness", "word": "thorns", "stem": "thorn",
    "avg": [ 5.14, 3.79 ], "std": [ 2.14, 1.68 ], "fq": 50 
  },
  "battles": {
    "dict": "happiness", "word": "battles", "stem": "battl",
    "avg": [ 6.77, 3.78 ], "std": [ 2.07, 2.00 ], "fq": 50 
  },
  "bugs": {
    "dict": "happiness", "word": "bugs", "stem": "bug",
    "avg": [ 5.87, 3.78 ], "std": [ 2.56, 1.52 ], "fq": 50 
  },
  "ends": {
    "dict": "happiness", "word": "ends", "stem": "end",
    "avg": [ 4.59, 3.78 ], "std": [ 3.07, 1.49 ], "fq": 50 
  },
  "risks": {
    "dict": "happiness", "word": "risks", "stem": "risk",
    "avg": [ 7.32, 3.78 ], "std": [ 2.07, 1.76 ], "fq": 50 
  },
  "rusty": {
    "dict": "happiness", "word": "rusty", "stem": "rusti",
    "avg": [ 3.77, 3.78 ], "std": [ 2.16, 1.46 ], "fq": 50 
  },
  "slow": {
    "dict": "happiness", "word": "slow", "stem": "slow",
    "avg": [ 3.39, 3.78 ], "std": [ 2.22, 1.11 ], "fq": 50 
  },
  "bothered": {
    "dict": "happiness", "word": "bothered", "stem": "bother",
    "avg": [ 5.76, 3.78 ], "std": [ 2.15, 1.53 ], "fq": 50 
  },
  "resigned": {
    "dict": "happiness", "word": "resigned", "stem": "resign",
    "avg": [ 5.64, 3.76 ], "std": [ 2.99, 1.59 ], "fq": 50 
  },
  "yell": {
    "dict": "happiness", "word": "yell", "stem": "yell",
    "avg": [ 7.04, 3.76 ], "std": [ 1.96, 1.72 ], "fq": 50 
  },
  "hangs": {
    "dict": "happiness", "word": "hangs", "stem": "hang",
    "avg": [ 4.70, 3.76 ], "std": [ 2.48, 1.68 ], "fq": 50 
  },
  "boo": {
    "dict": "happiness", "word": "boo", "stem": "boo",
    "avg": [ 3.17, 3.74 ], "std": [ 2.23, 1.76 ], "fq": 50 
  },
  "last": {
    "dict": "happiness", "word": "last", "stem": "last",
    "avg": [ 4.59, 3.74 ], "std": [ 3.07, 1.26 ], "fq": 50 
  },
  "noise": {
    "dict": "happiness", "word": "noise", "stem": "nois",
    "avg": [ 5.80, 3.74 ], "std": [ 2.39, 1.31 ], "fq": 50 
  },
  "obsession": {
    "dict": "happiness", "word": "obsession", "stem": "obsess",
    "avg": [ 6.41, 3.74 ], "std": [ 2.13, 1.12 ], "fq": 50 
  },
  "wait": {
    "dict": "happiness", "word": "wait", "stem": "wait",
    "avg": [ 5.62, 3.74 ], "std": [ 2.39, 1.21 ], "fq": 50 
  },
  "tearing": {
    "dict": "happiness", "word": "tearing", "stem": "tear",
    "avg": [ 4.97, 3.73 ], "std": [ 2.49, 1.38 ], "fq": 50 
  },
  "strain": {
    "dict": "happiness", "word": "strain", "stem": "strain",
    "avg": [ 4.07, 3.73 ], "std": [ 2.34, 1.81 ], "fq": 50 
  },
  "crack": {
    "dict": "happiness", "word": "crack", "stem": "crack",
    "avg": [ 6.83, 3.72 ], "std": [ 2.49, 1.44 ], "fq": 50 
  },
  "gross": {
    "dict": "happiness", "word": "gross", "stem": "gross",
    "avg": [ 5.07, 3.72 ], "std": [ 2.37, 1.49 ], "fq": 50 
  },
  "kick": {
    "dict": "happiness", "word": "kick", "stem": "kick",
    "avg": [ 4.90, 3.72 ], "std": [ 2.35, 1.55 ], "fq": 50 
  },
  "operation": {
    "dict": "happiness", "word": "operation", "stem": "oper",
    "avg": [ 6.35, 3.72 ], "std": [ 2.32, 1.60 ], "fq": 50 
  },
  "removed": {
    "dict": "happiness", "word": "removed", "stem": "remov",
    "avg": [ 7.47, 3.72 ], "std": [ 2.18, 1.39 ], "fq": 50 
  },
  "withdrawal": {
    "dict": "happiness", "word": "withdrawal", "stem": "withdraw",
    "avg": [ 4.26, 3.72 ], "std": [ 2.57, 1.84 ], "fq": 50 
  },
  "con": {
    "dict": "happiness", "word": "con", "stem": "con",
    "avg": [ 6.06, 3.70 ], "std": [ 2.32, 1.15 ], "fq": 50 
  },
  "crooked": {
    "dict": "happiness", "word": "crooked", "stem": "crook",
    "avg": [ 4.67, 3.70 ], "std": [ 2.35, 1.61 ], "fq": 50 
  },
  "dirt": {
    "dict": "happiness", "word": "dirt", "stem": "dirt",
    "avg": [ 3.76, 3.70 ], "std": [ 2.26, 1.53 ], "fq": 50 
  },
  "locked": {
    "dict": "happiness", "word": "locked", "stem": "lock",
    "avg": [ 6.77, 3.70 ], "std": [ 2.07, 1.27 ], "fq": 50 
  },
  "remove": {
    "dict": "happiness", "word": "remove", "stem": "remov",
    "avg": [ 7.47, 3.70 ], "std": [ 2.18, 1.20 ], "fq": 50 
  },
  "hustler": {
    "dict": "happiness", "word": "hustler", "stem": "hustler",
    "avg": [ 4.93, 3.69 ], "std": [ 2.82, 1.76 ], "fq": 50 
  },
  "controversy": {
    "dict": "happiness", "word": "controversy", "stem": "controversi",
    "avg": [ 4.32, 3.68 ], "std": [ 2.14, 1.74 ], "fq": 50 
  },
  "hitting": {
    "dict": "happiness", "word": "hitting", "stem": "hit",
    "avg": [ 5.73, 3.68 ], "std": [ 2.09, 1.74 ], "fq": 50 
  },
  "kicking": {
    "dict": "happiness", "word": "kicking", "stem": "kick",
    "avg": [ 4.90, 3.68 ], "std": [ 2.35, 1.62 ], "fq": 50 
  },
  "mean": {
    "dict": "happiness", "word": "mean", "stem": "mean",
    "avg": [ 6.95, 3.68 ], "std": [ 2.56, 1.92 ], "fq": 50 
  },
  "missed": {
    "dict": "happiness", "word": "missed", "stem": "miss",
    "avg": [ 5.82, 3.68 ], "std": [ 2.62, 1.24 ], "fq": 50 
  },
  "wrath": {
    "dict": "happiness", "word": "wrath", "stem": "wrath",
    "avg": [ 7.63, 3.68 ], "std": [ 1.91, 1.97 ], "fq": 50 
  },
  "low": {
    "dict": "happiness", "word": "low", "stem": "low",
    "avg": [ 4.54, 3.66 ], "std": [ 3.19, 1.12 ], "fq": 50 
  },
  "messy": {
    "dict": "happiness", "word": "messy", "stem": "messi",
    "avg": [ 3.34, 3.66 ], "std": [ 2.37, 1.19 ], "fq": 50 
  },
  "patients": {
    "dict": "happiness", "word": "patients", "stem": "patient",
    "avg": [ 4.21, 3.66 ], "std": [ 2.37, 1.41 ], "fq": 50 
  },
  "pressure": {
    "dict": "happiness", "word": "pressure", "stem": "pressur",
    "avg": [ 6.07, 3.66 ], "std": [ 2.26, 1.55 ], "fq": 50 
  },
  "snitch": {
    "dict": "happiness", "word": "snitch", "stem": "snitch",
    "avg": [ 7.24, 3.66 ], "std": [ 2.06, 1.65 ], "fq": 50 
  },
  "sorry": {
    "dict": "happiness", "word": "sorry", "stem": "sorri",
    "avg": [ 5.74, 3.66 ], "std": [ 2.32, 1.76 ], "fq": 50 
  },
  "snakes": {
    "dict": "happiness", "word": "snakes", "stem": "snake",
    "avg": [ 6.82, 3.65 ], "std": [ 2.10, 2.09 ], "fq": 50 
  },
  "lesions": {
    "dict": "happiness", "word": "lesions", "stem": "lesion",
    "avg": [ 5.82, 3.65 ], "std": [ 2.01, 1.90 ], "fq": 50 
  },
  "bill": {
    "dict": "happiness", "word": "bill", "stem": "bill",
    "avg": [ 3.93, 3.64 ], "std": [ 2.56, 1.77 ], "fq": 50 
  },
  "blocked": {
    "dict": "happiness", "word": "blocked", "stem": "block",
    "avg": [ 4.12, 3.64 ], "std": [ 2.01, 1.45 ], "fq": 50 
  },
  "bore": {
    "dict": "happiness", "word": "bore", "stem": "bore",
    "avg": [ 2.83, 3.64 ], "std": [ 2.31, 1.59 ], "fq": 50 
  },
  "cuts": {
    "dict": "happiness", "word": "cuts", "stem": "cut",
    "avg": [ 5.00, 3.64 ], "std": [ 2.32, 1.40 ], "fq": 50 
  },
  "darkest": {
    "dict": "happiness", "word": "darkest", "stem": "darkest",
    "avg": [ 4.73, 3.64 ], "std": [ 2.64, 2.12 ], "fq": 50 
  },
  "ghost": {
    "dict": "happiness", "word": "ghost", "stem": "ghost",
    "avg": [ 6.41, 3.64 ], "std": [ 2.13, 2.08 ], "fq": 50 
  },
  "miss": {
    "dict": "happiness", "word": "miss", "stem": "miss",
    "avg": [ 4.29, 3.64 ], "std": [ 2.69, 1.63 ], "fq": 50 
  },
  "shocked": {
    "dict": "happiness", "word": "shocked", "stem": "shock",
    "avg": [ 6.83, 3.64 ], "std": [ 2.26, 1.32 ], "fq": 50 
  },
  "awkward": {
    "dict": "happiness", "word": "awkward", "stem": "awkward",
    "avg": [ 5.18, 3.62 ], "std": [ 2.40, 1.40 ], "fq": 50 
  },
  "haunt": {
    "dict": "happiness", "word": "haunt", "stem": "haunt",
    "avg": [ 6.41, 3.62 ], "std": [ 2.13, 1.64 ], "fq": 50 
  },
  "risk": {
    "dict": "happiness", "word": "risk", "stem": "risk",
    "avg": [ 7.32, 3.62 ], "std": [ 2.07, 1.64 ], "fq": 50 
  },
  "crude": {
    "dict": "happiness", "word": "crude", "stem": "crude",
    "avg": [ 5.07, 3.60 ], "std": [ 2.37, 1.44 ], "fq": 50 
  },
  "falls": {
    "dict": "happiness", "word": "falls", "stem": "fall",
    "avg": [ 4.70, 3.60 ], "std": [ 2.48, 1.90 ], "fq": 50 
  },
  "madness": {
    "dict": "happiness", "word": "madness", "stem": "mad",
    "avg": [ 6.76, 3.60 ], "std": [ 2.26, 1.82 ], "fq": 50 
  },
  "mistaken": {
    "dict": "happiness", "word": "mistaken", "stem": "mistaken",
    "avg": [ 3.43, 3.60 ], "std": [ 2.09, 1.43 ], "fq": 50 
  },
  "acid": {
    "dict": "happiness", "word": "acid", "stem": "acid",
    "avg": [ 4.10, 3.59 ], "std": [ 2.34, 1.55 ], "fq": 50 
  },
  "pistol": {
    "dict": "happiness", "word": "pistol", "stem": "pistol",
    "avg": [ 6.15, 3.59 ], "std": [ 2.19, 1.90 ], "fq": 50 
  },
  "decreased": {
    "dict": "happiness", "word": "decreased", "stem": "decreas",
    "avg": [ 4.70, 3.58 ], "std": [ 2.48, 1.40 ], "fq": 50 
  },
  "excluded": {
    "dict": "happiness", "word": "excluded", "stem": "exclud",
    "avg": [ 5.00, 3.58 ], "std": [ 2.83, 1.54 ], "fq": 50 
  },
  "gossip": {
    "dict": "happiness", "word": "gossip", "stem": "gossip",
    "avg": [ 5.74, 3.58 ], "std": [ 2.38, 1.93 ], "fq": 50 
  },
  "shotgun": {
    "dict": "happiness", "word": "shotgun", "stem": "shotgun",
    "avg": [ 6.27, 3.58 ], "std": [ 1.94, 1.87 ], "fq": 50 
  },
  "confusing": {
    "dict": "happiness", "word": "confusing", "stem": "confus",
    "avg": [ 6.03, 3.56 ], "std": [ 1.88, 0.97 ], "fq": 50 
  },
  "empty": {
    "dict": "happiness", "word": "empty", "stem": "empti",
    "avg": [ 5.64, 3.56 ], "std": [ 2.99, 1.63 ], "fq": 50 
  },
  "fucked": {
    "dict": "happiness", "word": "fucked", "stem": "fuck",
    "avg": [ 6.38, 3.56 ], "std": [ 2.68, 2.71 ], "fq": 50 
  },
  "gloom": {
    "dict": "happiness", "word": "gloom", "stem": "gloom",
    "avg": [ 3.83, 3.56 ], "std": [ 2.33, 2.12 ], "fq": 50 
  },
  "mob": {
    "dict": "happiness", "word": "mob", "stem": "mob",
    "avg": [ 4.80, 3.56 ], "std": [ 2.71, 1.86 ], "fq": 50 
  },
  "offense": {
    "dict": "happiness", "word": "offense", "stem": "offens",
    "avg": [ 5.41, 3.56 ], "std": [ 2.69, 1.53 ], "fq": 50 
  },
  "piss": {
    "dict": "happiness", "word": "piss", "stem": "piss",
    "avg": [ 4.20, 3.56 ], "std": [ 2.18, 1.73 ], "fq": 50 
  },
  "sorely": {
    "dict": "happiness", "word": "sorely", "stem": "sore",
    "avg": [ 6.50, 3.56 ], "std": [ 2.49, 1.28 ], "fq": 50 
  },
  "dire": {
    "dict": "happiness", "word": "dire", "stem": "dire",
    "avg": [ 6.27, 3.55 ], "std": [ 2.44, 1.99 ], "fq": 50 
  },
  "stains": {
    "dict": "happiness", "word": "stains", "stem": "stain",
    "avg": [ 5.12, 3.55 ], "std": [ 2.32, 1.47 ], "fq": 50 
  },
  "haunted": {
    "dict": "happiness", "word": "haunted", "stem": "haunt",
    "avg": [ 6.41, 3.54 ], "std": [ 2.13, 1.64 ], "fq": 50 
  },
  "bug": {
    "dict": "happiness", "word": "bug", "stem": "bug",
    "avg": [ 5.87, 3.54 ], "std": [ 2.56, 1.37 ], "fq": 50 
  },
  "caught": {
    "dict": "happiness", "word": "caught", "stem": "caught",
    "avg": [ 5.83, 3.54 ], "std": [ 2.73, 1.79 ], "fq": 50 
  },
  "crushed": {
    "dict": "happiness", "word": "crushed", "stem": "crush",
    "avg": [ 5.52, 3.54 ], "std": [ 2.87, 1.67 ], "fq": 50 
  },
  "despise": {
    "dict": "happiness", "word": "despise", "stem": "despis",
    "avg": [ 6.28, 3.54 ], "std": [ 2.43, 2.03 ], "fq": 50 
  },
  "dispute": {
    "dict": "happiness", "word": "dispute", "stem": "disput",
    "avg": [ 6.29, 3.54 ], "std": [ 2.56, 1.73 ], "fq": 50 
  },
  "forsaken": {
    "dict": "happiness", "word": "forsaken", "stem": "forsaken",
    "avg": [ 5.50, 3.54 ], "std": [ 2.55, 1.94 ], "fq": 50 
  },
  "hospitals": {
    "dict": "happiness", "word": "hospitals", "stem": "hospit",
    "avg": [ 5.98, 3.54 ], "std": [ 2.54, 1.57 ], "fq": 50 
  },
  "rough": {
    "dict": "happiness", "word": "rough", "stem": "rough",
    "avg": [ 5.33, 3.54 ], "std": [ 2.04, 1.45 ], "fq": 50 
  },
  "shock": {
    "dict": "happiness", "word": "shock", "stem": "shock",
    "avg": [ 6.83, 3.54 ], "std": [ 2.26, 1.62 ], "fq": 50 
  },
  "slug": {
    "dict": "happiness", "word": "slug", "stem": "slug",
    "avg": [ 5.33, 3.54 ], "std": [ 2.48, 1.37 ], "fq": 50 
  },
  "separation": {
    "dict": "happiness", "word": "separation", "stem": "separ",
    "avg": [ 4.26, 3.53 ], "std": [ 2.57, 1.82 ], "fq": 50 
  },
  "spite": {
    "dict": "happiness", "word": "spite", "stem": "spite",
    "avg": [ 4.89, 3.53 ], "std": [ 2.50, 1.83 ], "fq": 50 
  },
  "addicted": {
    "dict": "happiness", "word": "addicted", "stem": "addict",
    "avg": [ 4.81, 3.52 ], "std": [ 2.46, 2.10 ], "fq": 50 
  },
  "fallen": {
    "dict": "happiness", "word": "fallen", "stem": "fallen",
    "avg": [ 4.70, 3.52 ], "std": [ 2.48, 1.42 ], "fq": 50 
  },
  "suspicion": {
    "dict": "happiness", "word": "suspicion", "stem": "suspicion",
    "avg": [ 6.25, 3.52 ], "std": [ 1.59, 1.50 ], "fq": 50 
  },
  "tomb": {
    "dict": "happiness", "word": "tomb", "stem": "tomb",
    "avg": [ 4.73, 3.52 ], "std": [ 2.72, 2.04 ], "fq": 50 
  },
  "warned": {
    "dict": "happiness", "word": "warned", "stem": "warn",
    "avg": [ 4.53, 3.52 ], "std": [ 2.11, 1.31 ], "fq": 50 
  },
  "untrue": {
    "dict": "happiness", "word": "untrue", "stem": "untru",
    "avg": [ 3.43, 3.51 ], "std": [ 2.09, 1.31 ], "fq": 50 
  },
  "casket": {
    "dict": "happiness", "word": "casket", "stem": "casket",
    "avg": [ 5.03, 3.50 ], "std": [ 2.79, 2.10 ], "fq": 50 
  },
  "dope": {
    "dict": "happiness", "word": "dope", "stem": "dope",
    "avg": [ 4.14, 3.50 ], "std": [ 2.11, 1.71 ], "fq": 50 
  },
  "hospital": {
    "dict": "happiness", "word": "hospital", "stem": "hospit",
    "avg": [ 5.98, 3.50 ], "std": [ 2.54, 1.62 ], "fq": 50 
  },
  "snake": {
    "dict": "happiness", "word": "snake", "stem": "snake",
    "avg": [ 6.82, 3.50 ], "std": [ 2.10, 1.67 ], "fq": 50 
  },
  "struck": {
    "dict": "happiness", "word": "struck", "stem": "struck",
    "avg": [ 4.70, 3.50 ], "std": [ 2.48, 1.40 ], "fq": 50 
  },
  "pressures": {
    "dict": "happiness", "word": "pressures", "stem": "pressur",
    "avg": [ 6.07, 3.49 ], "std": [ 2.26, 1.76 ], "fq": 50 
  },
  "sucked": {
    "dict": "happiness", "word": "sucked", "stem": "suck",
    "avg": [ 4.84, 3.48 ], "std": [ 2.04, 1.85 ], "fq": 50 
  },
  "tobacco": {
    "dict": "happiness", "word": "tobacco", "stem": "tobacco",
    "avg": [ 4.83, 3.48 ], "std": [ 2.90, 2.18 ], "fq": 50 
  },
  "screams": {
    "dict": "happiness", "word": "screams", "stem": "scream",
    "avg": [ 7.04, 3.48 ], "std": [ 1.96, 2.04 ], "fq": 50 
  },
  "deceive": {
    "dict": "happiness", "word": "deceive", "stem": "deceiv",
    "avg": [ 7.24, 3.47 ], "std": [ 2.06, 2.01 ], "fq": 50 
  },
  "monsters": {
    "dict": "happiness", "word": "monsters", "stem": "monster",
    "avg": [ 6.07, 3.47 ], "std": [ 2.61, 1.68 ], "fq": 50 
  },
  "urine": {
    "dict": "happiness", "word": "urine", "stem": "urin",
    "avg": [ 4.20, 3.47 ], "std": [ 2.18, 1.67 ], "fq": 50 
  },
  "chaos": {
    "dict": "happiness", "word": "chaos", "stem": "chao",
    "avg": [ 6.67, 3.46 ], "std": [ 2.06, 1.79 ], "fq": 50 
  },
  "insanity": {
    "dict": "happiness", "word": "insanity", "stem": "insan",
    "avg": [ 5.83, 3.46 ], "std": [ 2.45, 2.18 ], "fq": 50 
  },
  "isolated": {
    "dict": "happiness", "word": "isolated", "stem": "isol",
    "avg": [ 4.26, 3.46 ], "std": [ 2.57, 1.82 ], "fq": 50 
  },
  "monster": {
    "dict": "happiness", "word": "monster", "stem": "monster",
    "avg": [ 6.07, 3.46 ], "std": [ 2.61, 1.92 ], "fq": 50 
  },
  "refuse": {
    "dict": "happiness", "word": "refuse", "stem": "refus",
    "avg": [ 5.04, 3.46 ], "std": [ 2.50, 0.93 ], "fq": 50 
  },
  "shoot": {
    "dict": "happiness", "word": "shoot", "stem": "shoot",
    "avg": [ 5.73, 3.46 ], "std": [ 2.09, 1.67 ], "fq": 50 
  },
  "sting": {
    "dict": "happiness", "word": "sting", "stem": "sting",
    "avg": [ 4.70, 3.46 ], "std": [ 2.59, 1.74 ], "fq": 50 
  },
  "thorn": {
    "dict": "happiness", "word": "thorn", "stem": "thorn",
    "avg": [ 5.14, 3.46 ], "std": [ 2.14, 1.57 ], "fq": 50 
  },
  "wreck": {
    "dict": "happiness", "word": "wreck", "stem": "wreck",
    "avg": [ 6.95, 3.46 ], "std": [ 2.44, 1.80 ], "fq": 50 
  },
  "fright": {
    "dict": "happiness", "word": "fright", "stem": "fright",
    "avg": [ 6.33, 3.45 ], "std": [ 2.28, 1.84 ], "fq": 50 
  },
  "radiation": {
    "dict": "happiness", "word": "radiation", "stem": "radiat",
    "avg": [ 4.02, 3.45 ], "std": [ 1.94, 2.28 ], "fq": 50 
  },
  "stab": {
    "dict": "happiness", "word": "stab", "stem": "stab",
    "avg": [ 5.80, 3.45 ], "std": [ 2.00, 2.13 ], "fq": 50 
  },
  "confined": {
    "dict": "happiness", "word": "confined", "stem": "confin",
    "avg": [ 5.49, 3.44 ], "std": [ 2.67, 1.74 ], "fq": 50 
  },
  "delays": {
    "dict": "happiness", "word": "delays", "stem": "delay",
    "avg": [ 5.62, 3.44 ], "std": [ 2.39, 1.15 ], "fq": 50 
  },
  "fault": {
    "dict": "happiness", "word": "fault", "stem": "fault",
    "avg": [ 4.07, 3.44 ], "std": [ 1.69, 1.30 ], "fq": 50 
  },
  "poop": {
    "dict": "happiness", "word": "poop", "stem": "poop",
    "avg": [ 3.76, 3.44 ], "std": [ 2.26, 1.72 ], "fq": 50 
  },
  "seized": {
    "dict": "happiness", "word": "seized", "stem": "seiz",
    "avg": [ 5.65, 3.44 ], "std": [ 2.23, 1.46 ], "fq": 50 
  },
  "diss": {
    "dict": "happiness", "word": "diss", "stem": "diss",
    "avg": [ 6.00, 3.43 ], "std": [ 2.46, 1.88 ], "fq": 50 
  },
  "smashed": {
    "dict": "happiness", "word": "smashed", "stem": "smash",
    "avg": [ 6.21, 3.42 ], "std": [ 2.79, 1.74 ], "fq": 50 
  },
  "cut": {
    "dict": "happiness", "word": "cut", "stem": "cut",
    "avg": [ 5.00, 3.42 ], "std": [ 2.32, 1.29 ], "fq": 50 
  },
  "gone": {
    "dict": "happiness", "word": "gone", "stem": "gone",
    "avg": [ 6.21, 3.42 ], "std": [ 2.51, 1.74 ], "fq": 50 
  },
  "ignorant": {
    "dict": "happiness", "word": "ignorant", "stem": "ignor",
    "avg": [ 4.39, 3.42 ], "std": [ 2.49, 1.87 ], "fq": 50 
  },
  "lame": {
    "dict": "happiness", "word": "lame", "stem": "lame",
    "avg": [ 3.18, 3.42 ], "std": [ 1.76, 1.43 ], "fq": 50 
  },
  "obsessed": {
    "dict": "happiness", "word": "obsessed", "stem": "obsess",
    "avg": [ 6.41, 3.42 ], "std": [ 2.13, 1.47 ], "fq": 50 
  },
  "raging": {
    "dict": "happiness", "word": "raging", "stem": "rage",
    "avg": [ 8.17, 3.42 ], "std": [ 1.40, 1.64 ], "fq": 50 
  },
  "shouting": {
    "dict": "happiness", "word": "shouting", "stem": "shout",
    "avg": [ 6.12, 3.42 ], "std": [ 2.45, 1.60 ], "fq": 50 
  },
  "troubles": {
    "dict": "happiness", "word": "troubles", "stem": "troubl",
    "avg": [ 5.94, 3.42 ], "std": [ 2.36, 2.15 ], "fq": 50 
  },
  "disturbed": {
    "dict": "happiness", "word": "disturbed", "stem": "disturb",
    "avg": [ 5.80, 3.41 ], "std": [ 2.39, 1.59 ], "fq": 50 
  },
  "separated": {
    "dict": "happiness", "word": "separated", "stem": "separ",
    "avg": [ 3.96, 3.40 ], "std": [ 1.94, 1.32 ], "fq": 50 
  },
  "struggle": {
    "dict": "happiness", "word": "struggle", "stem": "struggl",
    "avg": [ 7.15, 3.40 ], "std": [ 2.19, 1.75 ], "fq": 50 
  },
  "whores": {
    "dict": "happiness", "word": "whores", "stem": "whore",
    "avg": [ 5.85, 3.40 ], "std": [ 2.93, 2.29 ], "fq": 50 
  },
  "deception": {
    "dict": "happiness", "word": "deception", "stem": "decept",
    "avg": [ 5.95, 3.39 ], "std": [ 2.36, 1.80 ], "fq": 50 
  },
  "stain": {
    "dict": "happiness", "word": "stain", "stem": "stain",
    "avg": [ 5.12, 3.39 ], "std": [ 2.32, 1.34 ], "fq": 50 
  },
  "delay": {
    "dict": "happiness", "word": "delay", "stem": "delay",
    "avg": [ 5.62, 3.38 ], "std": [ 2.39, 1.32 ], "fq": 50 
  },
  "difficulty": {
    "dict": "happiness", "word": "difficulty", "stem": "difficulti",
    "avg": [ 5.94, 3.38 ], "std": [ 2.36, 1.23 ], "fq": 50 
  },
  "eliminated": {
    "dict": "happiness", "word": "eliminated", "stem": "elimin",
    "avg": [ 6.37, 3.38 ], "std": [ 2.56, 1.69 ], "fq": 50 
  },
  "haunting": {
    "dict": "happiness", "word": "haunting", "stem": "haunt",
    "avg": [ 6.41, 3.38 ], "std": [ 2.13, 1.74 ], "fq": 50 
  },
  "hungry": {
    "dict": "happiness", "word": "hungry", "stem": "hungri",
    "avg": [ 5.13, 3.38 ], "std": [ 2.44, 1.93 ], "fq": 50 
  },
  "refused": {
    "dict": "happiness", "word": "refused", "stem": "refus",
    "avg": [ 6.37, 3.38 ], "std": [ 2.56, 1.46 ], "fq": 50 
  },
  "wicked": {
    "dict": "happiness", "word": "wicked", "stem": "wick",
    "avg": [ 6.09, 3.38 ], "std": [ 2.44, 1.95 ], "fq": 50 
  },
  "blinded": {
    "dict": "happiness", "word": "blinded", "stem": "blind",
    "avg": [ 4.39, 3.37 ], "std": [ 2.36, 1.58 ], "fq": 50 
  },
  "hunger": {
    "dict": "happiness", "word": "hunger", "stem": "hunger",
    "avg": [ 6.88, 3.37 ], "std": [ 1.85, 2.00 ], "fq": 50 
  },
  "torn": {
    "dict": "happiness", "word": "torn", "stem": "torn",
    "avg": [ 5.44, 3.37 ], "std": [ 2.10, 1.47 ], "fq": 50 
  },
  "phony": {
    "dict": "happiness", "word": "phony", "stem": "phoni",
    "avg": [ 6.07, 3.36 ], "std": [ 2.15, 1.91 ], "fq": 50 
  },
  "beast": {
    "dict": "happiness", "word": "beast", "stem": "beast",
    "avg": [ 5.57, 3.36 ], "std": [ 2.61, 1.52 ], "fq": 50 
  },
  "bullet": {
    "dict": "happiness", "word": "bullet", "stem": "bullet",
    "avg": [ 5.33, 3.36 ], "std": [ 2.48, 1.80 ], "fq": 50 
  },
  "busted": {
    "dict": "happiness", "word": "busted", "stem": "bust",
    "avg": [ 5.43, 3.36 ], "std": [ 2.42, 1.31 ], "fq": 50 
  },
  "dentist": {
    "dict": "happiness", "word": "dentist", "stem": "dentist",
    "avg": [ 5.73, 3.36 ], "std": [ 2.13, 1.69 ], "fq": 50 
  },
  "tornado": {
    "dict": "happiness", "word": "tornado", "stem": "tornado",
    "avg": [ 6.83, 3.36 ], "std": [ 2.49, 1.83 ], "fq": 50 
  },
  "weapon": {
    "dict": "happiness", "word": "weapon", "stem": "weapon",
    "avg": [ 6.03, 3.36 ], "std": [ 1.89, 1.66 ], "fq": 50 
  },
  "emptiness": {
    "dict": "happiness", "word": "emptiness", "stem": "empti",
    "avg": [ 4.98, 3.35 ], "std": [ 2.31, 1.97 ], "fq": 50 
  },
  "burnt": {
    "dict": "happiness", "word": "burnt", "stem": "burnt",
    "avg": [ 5.00, 3.34 ], "std": [ 2.32, 1.93 ], "fq": 50 
  },
  "crap": {
    "dict": "happiness", "word": "crap", "stem": "crap",
    "avg": [ 3.76, 3.34 ], "std": [ 2.26, 1.65 ], "fq": 50 
  },
  "tired": {
    "dict": "happiness", "word": "tired", "stem": "tire",
    "avg": [ 2.64, 3.34 ], "std": [ 2.19, 1.12 ], "fq": 50 
  },
  "warning": {
    "dict": "happiness", "word": "warning", "stem": "warn",
    "avg": [ 4.53, 3.34 ], "std": [ 2.11, 1.42 ], "fq": 50 
  },
  "alone": {
    "dict": "happiness", "word": "alone", "stem": "alon",
    "avg": [ 4.83, 3.32 ], "std": [ 2.66, 1.73 ], "fq": 50 
  },
  "confusion": {
    "dict": "happiness", "word": "confusion", "stem": "confus",
    "avg": [ 6.03, 3.32 ], "std": [ 1.88, 1.36 ], "fq": 50 
  },
  "ignored": {
    "dict": "happiness", "word": "ignored", "stem": "ignor",
    "avg": [ 4.39, 3.32 ], "std": [ 2.49, 1.50 ], "fq": 50 
  },
  "noose": {
    "dict": "happiness", "word": "noose", "stem": "noos",
    "avg": [ 4.39, 3.32 ], "std": [ 2.08, 2.22 ], "fq": 50 
  },
  "opposed": {
    "dict": "happiness", "word": "opposed", "stem": "oppos",
    "avg": [ 7.15, 3.32 ], "std": [ 2.19, 1.41 ], "fq": 50 
  },
  "scars": {
    "dict": "happiness", "word": "scars", "stem": "scar",
    "avg": [ 4.79, 3.32 ], "std": [ 2.11, 1.73 ], "fq": 50 
  },
  "savage": {
    "dict": "happiness", "word": "savage", "stem": "savag",
    "avg": [ 6.47, 3.31 ], "std": [ 2.47, 1.95 ], "fq": 50 
  },
  "choke": {
    "dict": "happiness", "word": "choke", "stem": "choke",
    "avg": [ 4.93, 3.31 ], "std": [ 2.23, 1.69 ], "fq": 50 
  },
  "fury": {
    "dict": "happiness", "word": "fury", "stem": "furi",
    "avg": [ 8.17, 3.30 ], "std": [ 1.40, 1.78 ], "fq": 50 
  },
  "lowest": {
    "dict": "happiness", "word": "lowest", "stem": "lowest",
    "avg": [ 4.31, 3.30 ], "std": [ 2.20, 1.17 ], "fq": 50 
  },
  "whip": {
    "dict": "happiness", "word": "whip", "stem": "whip",
    "avg": [ 4.10, 3.30 ], "std": [ 2.34, 1.74 ], "fq": 50 
  },
  "helpless": {
    "dict": "happiness", "word": "helpless", "stem": "helpless",
    "avg": [ 5.34, 3.29 ], "std": [ 2.52, 2.02 ], "fq": 50 
  },
  "rats": {
    "dict": "happiness", "word": "rats", "stem": "rat",
    "avg": [ 4.95, 3.29 ], "std": [ 2.36, 1.89 ], "fq": 50 
  },
  "crashing": {
    "dict": "happiness", "word": "crashing", "stem": "crash",
    "avg": [ 6.95, 3.28 ], "std": [ 2.44, 1.88 ], "fq": 50 
  },
  "falling": {
    "dict": "happiness", "word": "falling", "stem": "fall",
    "avg": [ 4.70, 3.28 ], "std": [ 2.48, 1.54 ], "fq": 50 
  },
  "lazy": {
    "dict": "happiness", "word": "lazy", "stem": "lazi",
    "avg": [ 2.65, 3.28 ], "std": [ 2.06, 1.46 ], "fq": 50 
  },
  "scar": {
    "dict": "happiness", "word": "scar", "stem": "scar",
    "avg": [ 4.79, 3.28 ], "std": [ 2.11, 1.46 ], "fq": 50 
  },
  "suspicious": {
    "dict": "happiness", "word": "suspicious", "stem": "suspici",
    "avg": [ 6.25, 3.28 ], "std": [ 1.59, 1.37 ], "fq": 50 
  },
  "scarred": {
    "dict": "happiness", "word": "scarred", "stem": "scar",
    "avg": [ 4.79, 3.27 ], "std": [ 2.11, 2.03 ], "fq": 50 
  },
  "screamed": {
    "dict": "happiness", "word": "screamed", "stem": "scream",
    "avg": [ 7.04, 3.27 ], "std": [ 1.96, 1.64 ], "fq": 50 
  },
  "damned": {
    "dict": "happiness", "word": "damned", "stem": "damn",
    "avg": [ 4.05, 3.26 ], "std": [ 2.59, 1.97 ], "fq": 50 
  },
  "delayed": {
    "dict": "happiness", "word": "delayed", "stem": "delay",
    "avg": [ 5.62, 3.24 ], "std": [ 2.39, 1.19 ], "fq": 50 
  },
  "dull": {
    "dict": "happiness", "word": "dull", "stem": "dull",
    "avg": [ 2.83, 3.24 ], "std": [ 2.31, 1.22 ], "fq": 50 
  },
  "fat": {
    "dict": "happiness", "word": "fat", "stem": "fat",
    "avg": [ 4.81, 3.24 ], "std": [ 2.80, 1.82 ], "fq": 50 
  },
  "rot": {
    "dict": "happiness", "word": "rot", "stem": "rot",
    "avg": [ 4.14, 3.24 ], "std": [ 2.30, 1.61 ], "fq": 50 
  },
  "screwed": {
    "dict": "happiness", "word": "screwed", "stem": "screw",
    "avg": [ 6.38, 3.24 ], "std": [ 2.68, 1.61 ], "fq": 50 
  },
  "captured": {
    "dict": "happiness", "word": "captured", "stem": "captur",
    "avg": [ 5.83, 3.22 ], "std": [ 2.73, 1.61 ], "fq": 50 
  },
  "fell": {
    "dict": "happiness", "word": "fell", "stem": "fell",
    "avg": [ 5.28, 3.22 ], "std": [ 2.51, 1.47 ], "fq": 50 
  },
  "ignore": {
    "dict": "happiness", "word": "ignore", "stem": "ignor",
    "avg": [ 4.39, 3.22 ], "std": [ 2.49, 1.37 ], "fq": 50 
  },
  "losers": {
    "dict": "happiness", "word": "losers", "stem": "loser",
    "avg": [ 4.95, 3.22 ], "std": [ 2.57, 1.88 ], "fq": 50 
  },
  "wasting": {
    "dict": "happiness", "word": "wasting", "stem": "wast",
    "avg": [ 4.14, 3.22 ], "std": [ 2.30, 1.42 ], "fq": 50 
  },
  "defect": {
    "dict": "happiness", "word": "defect", "stem": "defect",
    "avg": [ 4.07, 3.21 ], "std": [ 1.69, 1.70 ], "fq": 50 
  },
  "frightened": {
    "dict": "happiness", "word": "frightened", "stem": "frighten",
    "avg": [ 7.86, 3.20 ], "std": [ 2.27, 1.86 ], "fq": 50 
  },
  "combat": {
    "dict": "happiness", "word": "combat", "stem": "combat",
    "avg": [ 7.15, 3.20 ], "std": [ 2.19, 1.68 ], "fq": 50 
  },
  "defeat": {
    "dict": "happiness", "word": "defeat", "stem": "defeat",
    "avg": [ 5.09, 3.20 ], "std": [ 3.00, 1.95 ], "fq": 50 
  },
  "dirty": {
    "dict": "happiness", "word": "dirty", "stem": "dirti",
    "avg": [ 4.88, 3.20 ], "std": [ 2.29, 1.51 ], "fq": 50 
  },
  "dread": {
    "dict": "happiness", "word": "dread", "stem": "dread",
    "avg": [ 5.84, 3.20 ], "std": [ 2.62, 1.95 ], "fq": 50 
  },
  "inferior": {
    "dict": "happiness", "word": "inferior", "stem": "inferior",
    "avg": [ 3.83, 3.20 ], "std": [ 2.05, 1.47 ], "fq": 50 
  },
  "aching": {
    "dict": "happiness", "word": "aching", "stem": "ach",
    "avg": [ 5.00, 3.18 ], "std": [ 2.45, 1.49 ], "fq": 50 
  },
  "difficult": {
    "dict": "happiness", "word": "difficult", "stem": "difficult",
    "avg": [ 5.12, 3.18 ], "std": [ 2.19, 0.90 ], "fq": 50 
  },
  "faggot": {
    "dict": "happiness", "word": "faggot", "stem": "faggot",
    "avg": [ 4.76, 3.18 ], "std": [ 2.18, 1.98 ], "fq": 50 
  },
  "false": {
    "dict": "happiness", "word": "false", "stem": "fals",
    "avg": [ 3.43, 3.18 ], "std": [ 2.09, 1.35 ], "fq": 50 
  },
  "garbage": {
    "dict": "happiness", "word": "garbage", "stem": "garbag",
    "avg": [ 5.04, 3.18 ], "std": [ 2.50, 1.62 ], "fq": 50 
  },
  "kicked": {
    "dict": "happiness", "word": "kicked", "stem": "kick",
    "avg": [ 4.90, 3.18 ], "std": [ 2.35, 1.40 ], "fq": 50 
  },
  "scandal": {
    "dict": "happiness", "word": "scandal", "stem": "scandal",
    "avg": [ 5.12, 3.18 ], "std": [ 2.22, 1.56 ], "fq": 50 
  },
  "complain": {
    "dict": "happiness", "word": "complain", "stem": "complain",
    "avg": [ 3.52, 3.16 ], "std": [ 2.05, 1.56 ], "fq": 50 
  },
  "declined": {
    "dict": "happiness", "word": "declined", "stem": "declin",
    "avg": [ 6.37, 3.16 ], "std": [ 2.56, 1.54 ], "fq": 50 
  },
  "disorders": {
    "dict": "happiness", "word": "disorders", "stem": "disord",
    "avg": [ 5.86, 3.16 ], "std": [ 2.40, 1.43 ], "fq": 50 
  },
  "forced": {
    "dict": "happiness", "word": "forced", "stem": "forc",
    "avg": [ 6.07, 3.16 ], "std": [ 2.26, 1.27 ], "fq": 50 
  },
  "severe": {
    "dict": "happiness", "word": "severe", "stem": "sever",
    "avg": [ 5.26, 3.16 ], "std": [ 2.36, 1.72 ], "fq": 50 
  },
  "smoke": {
    "dict": "happiness", "word": "smoke", "stem": "smoke",
    "avg": [ 5.33, 3.16 ], "std": [ 2.48, 1.94 ], "fq": 50 
  },
  "feared": {
    "dict": "happiness", "word": "feared", "stem": "fear",
    "avg": [ 6.33, 3.14 ], "std": [ 2.28, 1.93 ], "fq": 50 
  },
  "argument": {
    "dict": "happiness", "word": "argument", "stem": "argument",
    "avg": [ 4.32, 3.14 ], "std": [ 2.14, 1.55 ], "fq": 50 
  },
  "bitch": {
    "dict": "happiness", "word": "bitch", "stem": "bitch",
    "avg": [ 5.00, 3.14 ], "std": [ 2.19, 1.81 ], "fq": 50 
  },
  "bruise": {
    "dict": "happiness", "word": "bruise", "stem": "bruis",
    "avg": [ 5.82, 3.14 ], "std": [ 2.01, 1.21 ], "fq": 50 
  },
  "dismissed": {
    "dict": "happiness", "word": "dismissed", "stem": "dismiss",
    "avg": [ 7.17, 3.14 ], "std": [ 2.06, 1.11 ], "fq": 50 
  },
  "disorder": {
    "dict": "happiness", "word": "disorder", "stem": "disord",
    "avg": [ 5.86, 3.14 ], "std": [ 2.40, 1.40 ], "fq": 50 
  },
  "exhausted": {
    "dict": "happiness", "word": "exhausted", "stem": "exhaust",
    "avg": [ 2.64, 3.14 ], "std": [ 2.19, 1.71 ], "fq": 50 
  },
  "incorrectly": {
    "dict": "happiness", "word": "incorrectly", "stem": "incorrectli",
    "avg": [ 3.43, 3.14 ], "std": [ 2.09, 1.03 ], "fq": 50 
  },
  "scream": {
    "dict": "happiness", "word": "scream", "stem": "scream",
    "avg": [ 7.04, 3.14 ], "std": [ 1.96, 1.41 ], "fq": 50 
  },
  "slapped": {
    "dict": "happiness", "word": "slapped", "stem": "slap",
    "avg": [ 6.46, 3.14 ], "std": [ 2.58, 1.55 ], "fq": 50 
  },
  "suck": {
    "dict": "happiness", "word": "suck", "stem": "suck",
    "avg": [ 4.84, 3.14 ], "std": [ 2.04, 1.82 ], "fq": 50 
  },
  "sucks": {
    "dict": "happiness", "word": "sucks", "stem": "suck",
    "avg": [ 4.84, 3.14 ], "std": [ 2.04, 1.48 ], "fq": 50 
  },
  "suspect": {
    "dict": "happiness", "word": "suspect", "stem": "suspect",
    "avg": [ 6.25, 3.14 ], "std": [ 1.59, 1.31 ], "fq": 50 
  },
  "whore": {
    "dict": "happiness", "word": "whore", "stem": "whore",
    "avg": [ 5.85, 3.14 ], "std": [ 2.93, 2.11 ], "fq": 50 
  },
  "wrong": {
    "dict": "happiness", "word": "wrong", "stem": "wrong",
    "avg": [ 5.57, 3.14 ], "std": [ 2.26, 0.97 ], "fq": 50 
  },
  "desperate": {
    "dict": "happiness", "word": "desperate", "stem": "desper",
    "avg": [ 5.68, 3.12 ], "std": [ 2.37, 1.62 ], "fq": 50 
  },
  "lonesome": {
    "dict": "happiness", "word": "lonesome", "stem": "lonesom",
    "avg": [ 4.51, 3.12 ], "std": [ 2.68, 1.62 ], "fq": 50 
  },
  "regret": {
    "dict": "happiness", "word": "regret", "stem": "regret",
    "avg": [ 5.74, 3.12 ], "std": [ 2.32, 1.51 ], "fq": 50 
  },
  "defects": {
    "dict": "happiness", "word": "defects", "stem": "defect",
    "avg": [ 4.07, 3.10 ], "std": [ 1.69, 1.56 ], "fq": 50 
  },
  "ambulance": {
    "dict": "happiness", "word": "ambulance", "stem": "ambul",
    "avg": [ 7.33, 3.10 ], "std": [ 1.96, 1.61 ], "fq": 50 
  },
  "annoy": {
    "dict": "happiness", "word": "annoy", "stem": "annoy",
    "avg": [ 6.49, 3.10 ], "std": [ 2.17, 1.39 ], "fq": 50 
  },
  "conflict": {
    "dict": "happiness", "word": "conflict", "stem": "conflict",
    "avg": [ 6.77, 3.10 ], "std": [ 2.07, 1.53 ], "fq": 50 
  },
  "execution": {
    "dict": "happiness", "word": "execution", "stem": "execut",
    "avg": [ 5.71, 3.10 ], "std": [ 2.74, 2.39 ], "fq": 50 
  },
  "fought": {
    "dict": "happiness", "word": "fought", "stem": "fought",
    "avg": [ 7.15, 3.10 ], "std": [ 2.19, 1.39 ], "fq": 50 
  },
  "pity": {
    "dict": "happiness", "word": "pity", "stem": "piti",
    "avg": [ 3.72, 3.10 ], "std": [ 2.02, 1.31 ], "fq": 50 
  },
  "stink": {
    "dict": "happiness", "word": "stink", "stem": "stink",
    "avg": [ 4.26, 3.10 ], "std": [ 2.10, 1.22 ], "fq": 50 
  },
  "decay": {
    "dict": "happiness", "word": "decay", "stem": "decay",
    "avg": [ 4.65, 3.08 ], "std": [ 2.39, 1.41 ], "fq": 50 
  },
  "decline": {
    "dict": "happiness", "word": "decline", "stem": "declin",
    "avg": [ 6.37, 3.08 ], "std": [ 2.56, 1.23 ], "fq": 50 
  },
  "difficulties": {
    "dict": "happiness", "word": "difficulties", "stem": "difficulti",
    "avg": [ 5.94, 3.08 ], "std": [ 2.36, 1.28 ], "fq": 50 
  },
  "graves": {
    "dict": "happiness", "word": "graves", "stem": "grave",
    "avg": [ 4.73, 3.08 ], "std": [ 2.72, 1.85 ], "fq": 50 
  },
  "regrets": {
    "dict": "happiness", "word": "regrets", "stem": "regret",
    "avg": [ 5.74, 3.08 ], "std": [ 2.32, 1.52 ], "fq": 50 
  },
  "trapped": {
    "dict": "happiness", "word": "trapped", "stem": "trap",
    "avg": [ 3.91, 3.08 ], "std": [ 1.92, 1.52 ], "fq": 50 
  },
  "yelling": {
    "dict": "happiness", "word": "yelling", "stem": "yell",
    "avg": [ 7.04, 3.08 ], "std": [ 1.96, 1.56 ], "fq": 50 
  },
  "arguing": {
    "dict": "happiness", "word": "arguing", "stem": "argu",
    "avg": [ 4.32, 3.06 ], "std": [ 2.14, 1.36 ], "fq": 50 
  },
  "bullets": {
    "dict": "happiness", "word": "bullets", "stem": "bullet",
    "avg": [ 5.33, 3.06 ], "std": [ 2.48, 1.96 ], "fq": 50 
  },
  "dumb": {
    "dict": "happiness", "word": "dumb", "stem": "dumb",
    "avg": [ 3.39, 3.06 ], "std": [ 2.22, 0.96 ], "fq": 50 
  },
  "emergency": {
    "dict": "happiness", "word": "emergency", "stem": "emerg",
    "avg": [ 4.59, 3.06 ], "std": [ 2.10, 1.78 ], "fq": 50 
  },
  "greed": {
    "dict": "happiness", "word": "greed", "stem": "greed",
    "avg": [ 4.71, 3.06 ], "std": [ 2.26, 1.92 ], "fq": 50 
  },
  "idiot": {
    "dict": "happiness", "word": "idiot", "stem": "idiot",
    "avg": [ 4.21, 3.06 ], "std": [ 2.47, 1.53 ], "fq": 50 
  },
  "idiots": {
    "dict": "happiness", "word": "idiots", "stem": "idiot",
    "avg": [ 4.21, 3.06 ], "std": [ 2.47, 1.61 ], "fq": 50 
  },
  "turmoil": {
    "dict": "happiness", "word": "turmoil", "stem": "turmoil",
    "avg": [ 7.67, 3.06 ], "std": [ 1.91, 1.63 ], "fq": 50 
  },
  "rotting": {
    "dict": "happiness", "word": "rotting", "stem": "rot",
    "avg": [ 4.14, 3.04 ], "std": [ 2.30, 1.53 ], "fq": 50 
  },
  "arguments": {
    "dict": "happiness", "word": "arguments", "stem": "argument",
    "avg": [ 4.32, 3.04 ], "std": [ 2.14, 1.52 ], "fq": 50 
  },
  "bored": {
    "dict": "happiness", "word": "bored", "stem": "bore",
    "avg": [ 2.83, 3.04 ], "std": [ 2.31, 1.19 ], "fq": 50 
  },
  "complaints": {
    "dict": "happiness", "word": "complaints", "stem": "complaint",
    "avg": [ 4.71, 3.04 ], "std": [ 2.24, 1.32 ], "fq": 50 
  },
  "horror": {
    "dict": "happiness", "word": "horror", "stem": "horror",
    "avg": [ 7.21, 3.04 ], "std": [ 2.14, 2.00 ], "fq": 50 
  },
  "insane": {
    "dict": "happiness", "word": "insane", "stem": "insan",
    "avg": [ 5.83, 3.04 ], "std": [ 2.45, 1.73 ], "fq": 50 
  },
  "jealousy": {
    "dict": "happiness", "word": "jealousy", "stem": "jealousi",
    "avg": [ 6.36, 3.04 ], "std": [ 2.66, 1.55 ], "fq": 50 
  },
  "lawsuits": {
    "dict": "happiness", "word": "lawsuits", "stem": "lawsuit",
    "avg": [ 4.93, 3.04 ], "std": [ 2.44, 1.70 ], "fq": 50 
  },
  "rat": {
    "dict": "happiness", "word": "rat", "stem": "rat",
    "avg": [ 4.95, 3.04 ], "std": [ 2.36, 1.86 ], "fq": 50 
  },
  "scare": {
    "dict": "happiness", "word": "scare", "stem": "scare",
    "avg": [ 6.82, 3.04 ], "std": [ 2.03, 1.56 ], "fq": 50 
  },
  "anxiety": {
    "dict": "happiness", "word": "anxiety", "stem": "anxieti",
    "avg": [ 6.92, 3.03 ], "std": [ 1.81, 1.89 ], "fq": 50 
  },
  "fiend": {
    "dict": "happiness", "word": "fiend", "stem": "fiend",
    "avg": [ 6.07, 3.02 ], "std": [ 2.61, 1.55 ], "fq": 50 
  },
  "hostile": {
    "dict": "happiness", "word": "hostile", "stem": "hostil",
    "avg": [ 6.44, 3.02 ], "std": [ 2.28, 1.97 ], "fq": 50 
  },
  "broken": {
    "dict": "happiness", "word": "broken", "stem": "broken",
    "avg": [ 5.43, 3.02 ], "std": [ 2.42, 1.41 ], "fq": 50 
  },
  "bitter": {
    "dict": "happiness", "word": "bitter", "stem": "bitter",
    "avg": [ 4.10, 3.00 ], "std": [ 2.34, 1.25 ], "fq": 50 
  },
  "fights": {
    "dict": "happiness", "word": "fights", "stem": "fight",
    "avg": [ 7.15, 3.00 ], "std": [ 2.19, 1.37 ], "fq": 50 
  },
  "vicious": {
    "dict": "happiness", "word": "vicious", "stem": "viciou",
    "avg": [ 6.39, 3.00 ], "std": [ 2.44, 1.93 ], "fq": 50 
  },
  "battle": {
    "dict": "happiness", "word": "battle", "stem": "battl",
    "avg": [ 6.77, 2.98 ], "std": [ 2.07, 1.73 ], "fq": 50 
  },
  "confused": {
    "dict": "happiness", "word": "confused", "stem": "confus",
    "avg": [ 6.03, 2.98 ], "std": [ 1.88, 1.29 ], "fq": 50 
  },
  "crappy": {
    "dict": "happiness", "word": "crappy", "stem": "crappi",
    "avg": [ 4.26, 2.98 ], "std": [ 2.10, 1.66 ], "fq": 50 
  },
  "damn": {
    "dict": "happiness", "word": "damn", "stem": "damn",
    "avg": [ 6.41, 2.98 ], "std": [ 2.00, 1.62 ], "fq": 50 
  },
  "guns": {
    "dict": "happiness", "word": "guns", "stem": "gun",
    "avg": [ 7.02, 2.98 ], "std": [ 1.84, 2.02 ], "fq": 50 
  },
  "ignorance": {
    "dict": "happiness", "word": "ignorance", "stem": "ignor",
    "avg": [ 4.39, 2.98 ], "std": [ 2.49, 1.36 ], "fq": 50 
  },
  "missing": {
    "dict": "happiness", "word": "missing", "stem": "miss",
    "avg": [ 4.83, 2.98 ], "std": [ 2.31, 1.38 ], "fq": 50 
  },
  "problem": {
    "dict": "happiness", "word": "problem", "stem": "problem",
    "avg": [ 5.94, 2.98 ], "std": [ 2.36, 1.41 ], "fq": 50 
  },
  "worthless": {
    "dict": "happiness", "word": "worthless", "stem": "worthless",
    "avg": [ 5.38, 2.98 ], "std": [ 2.23, 1.91 ], "fq": 50 
  },
  "insecure": {
    "dict": "happiness", "word": "insecure", "stem": "insecur",
    "avg": [ 5.56, 2.98 ], "std": [ 2.34, 1.13 ], "fq": 50 
  },
  "coffin": {
    "dict": "happiness", "word": "coffin", "stem": "coffin",
    "avg": [ 5.03, 2.96 ], "std": [ 2.79, 1.99 ], "fq": 50 
  },
  "conflicts": {
    "dict": "happiness", "word": "conflicts", "stem": "conflict",
    "avg": [ 6.77, 2.96 ], "std": [ 2.07, 1.46 ], "fq": 50 
  },
  "damages": {
    "dict": "happiness", "word": "damages", "stem": "damag",
    "avg": [ 5.57, 2.96 ], "std": [ 2.26, 1.37 ], "fq": 50 
  },
  "lawsuit": {
    "dict": "happiness", "word": "lawsuit", "stem": "lawsuit",
    "avg": [ 4.93, 2.96 ], "std": [ 2.44, 1.62 ], "fq": 50 
  },
  "screaming": {
    "dict": "happiness", "word": "screaming", "stem": "scream",
    "avg": [ 7.04, 2.96 ], "std": [ 1.96, 1.52 ], "fq": 50 
  },
  "wound": {
    "dict": "happiness", "word": "wound", "stem": "wound",
    "avg": [ 5.82, 2.96 ], "std": [ 2.01, 1.68 ], "fq": 50 
  },
  "bloody": {
    "dict": "happiness", "word": "bloody", "stem": "bloodi",
    "avg": [ 6.41, 2.94 ], "std": [ 2.00, 1.70 ], "fq": 50 
  },
  "cemetery": {
    "dict": "happiness", "word": "cemetery", "stem": "cemeteri",
    "avg": [ 4.82, 2.94 ], "std": [ 2.66, 1.71 ], "fq": 50 
  },
  "choking": {
    "dict": "happiness", "word": "choking", "stem": "choke",
    "avg": [ 4.93, 2.94 ], "std": [ 2.23, 1.88 ], "fq": 50 
  },
  "foul": {
    "dict": "happiness", "word": "foul", "stem": "foul",
    "avg": [ 4.93, 2.94 ], "std": [ 2.23, 1.33 ], "fq": 50 
  },
  "sore": {
    "dict": "happiness", "word": "sore", "stem": "sore",
    "avg": [ 6.50, 2.94 ], "std": [ 2.49, 1.33 ], "fq": 50 
  },
  "tension": {
    "dict": "happiness", "word": "tension", "stem": "tension",
    "avg": [ 7.45, 2.94 ], "std": [ 2.38, 1.58 ], "fq": 50 
  },
  "thief": {
    "dict": "happiness", "word": "thief", "stem": "thief",
    "avg": [ 6.89, 2.94 ], "std": [ 2.13, 2.21 ], "fq": 50 
  },
  "weakness": {
    "dict": "happiness", "word": "weakness", "stem": "weak",
    "avg": [ 5.34, 2.94 ], "std": [ 2.52, 1.53 ], "fq": 50 
  },
  "accused": {
    "dict": "happiness", "word": "accused", "stem": "accus",
    "avg": [ 4.79, 2.92 ], "std": [ 2.51, 1.55 ], "fq": 50 
  },
  "awful": {
    "dict": "happiness", "word": "awful", "stem": "aw",
    "avg": [ 6.50, 2.92 ], "std": [ 2.49, 1.94 ], "fq": 50 
  },
  "burn": {
    "dict": "happiness", "word": "burn", "stem": "burn",
    "avg": [ 6.22, 2.92 ], "std": [ 1.91, 1.34 ], "fq": 50 
  },
  "cries": {
    "dict": "happiness", "word": "cries", "stem": "cri",
    "avg": [ 7.04, 2.92 ], "std": [ 1.96, 1.59 ], "fq": 50 
  },
  "mistakes": {
    "dict": "happiness", "word": "mistakes", "stem": "mistak",
    "avg": [ 5.18, 2.92 ], "std": [ 2.42, 1.45 ], "fq": 50 
  },
  "problems": {
    "dict": "happiness", "word": "problems", "stem": "problem",
    "avg": [ 5.94, 2.92 ], "std": [ 2.36, 1.56 ], "fq": 50 
  },
  "riot": {
    "dict": "happiness", "word": "riot", "stem": "riot",
    "avg": [ 6.39, 2.92 ], "std": [ 2.63, 1.76 ], "fq": 50 
  },
  "sleepless": {
    "dict": "happiness", "word": "sleepless", "stem": "sleepless",
    "avg": [ 4.10, 2.92 ], "std": [ 2.12, 1.55 ], "fq": 50 
  },
  "demon": {
    "dict": "happiness", "word": "demon", "stem": "demon",
    "avg": [ 6.76, 2.92 ], "std": [ 2.68, 1.96 ], "fq": 50 
  },
  "boring": {
    "dict": "happiness", "word": "boring", "stem": "bore",
    "avg": [ 2.83, 2.90 ], "std": [ 2.31, 1.15 ], "fq": 50 
  },
  "bruised": {
    "dict": "happiness", "word": "bruised", "stem": "bruis",
    "avg": [ 5.82, 2.90 ], "std": [ 2.01, 1.75 ], "fq": 50 
  },
  "burned": {
    "dict": "happiness", "word": "burned", "stem": "burn",
    "avg": [ 6.22, 2.90 ], "std": [ 1.91, 1.42 ], "fq": 50 
  },
  "collapse": {
    "dict": "happiness", "word": "collapse", "stem": "collaps",
    "avg": [ 6.95, 2.90 ], "std": [ 2.44, 1.45 ], "fq": 50 
  },
  "complained": {
    "dict": "happiness", "word": "complained", "stem": "complain",
    "avg": [ 3.52, 2.90 ], "std": [ 2.05, 0.99 ], "fq": 50 
  },
  "debt": {
    "dict": "happiness", "word": "debt", "stem": "debt",
    "avg": [ 5.68, 2.90 ], "std": [ 2.74, 1.66 ], "fq": 50 
  },
  "fake": {
    "dict": "happiness", "word": "fake", "stem": "fake",
    "avg": [ 6.07, 2.90 ], "std": [ 2.15, 1.25 ], "fq": 50 
  },
  "frustrated": {
    "dict": "happiness", "word": "frustrated", "stem": "frustrat",
    "avg": [ 5.61, 2.90 ], "std": [ 2.76, 1.61 ], "fq": 50 
  },
  "deadly": {
    "dict": "happiness", "word": "deadly", "stem": "deadli",
    "avg": [ 5.83, 2.90 ], "std": [ 2.45, 1.82 ], "fq": 50 
  },
  "disrespect": {
    "dict": "happiness", "word": "disrespect", "stem": "disrespect",
    "avg": [ 5.28, 2.90 ], "std": [ 2.04, 1.78 ], "fq": 50 
  },
  "drown": {
    "dict": "happiness", "word": "drown", "stem": "drown",
    "avg": [ 6.57, 2.90 ], "std": [ 2.33, 2.09 ], "fq": 50 
  },
  "badly": {
    "dict": "happiness", "word": "badly", "stem": "badli",
    "avg": [ 4.71, 2.88 ], "std": [ 2.24, 1.61 ], "fq": 50 
  },
  "burning": {
    "dict": "happiness", "word": "burning", "stem": "burn",
    "avg": [ 6.22, 2.88 ], "std": [ 1.91, 1.49 ], "fq": 50 
  },
  "threats": {
    "dict": "happiness", "word": "threats", "stem": "threat",
    "avg": [ 5.52, 2.88 ], "std": [ 2.45, 1.77 ], "fq": 50 
  },
  "sins": {
    "dict": "happiness", "word": "sins", "stem": "sin",
    "avg": [ 6.29, 2.88 ], "std": [ 2.43, 1.32 ], "fq": 50 
  },
  "bombs": {
    "dict": "happiness", "word": "bombs", "stem": "bomb",
    "avg": [ 7.15, 2.86 ], "std": [ 2.40, 2.27 ], "fq": 50 
  },
  "complaint": {
    "dict": "happiness", "word": "complaint", "stem": "complaint",
    "avg": [ 4.71, 2.86 ], "std": [ 2.24, 1.01 ], "fq": 50 
  },
  "errors": {
    "dict": "happiness", "word": "errors", "stem": "error",
    "avg": [ 4.07, 2.86 ], "std": [ 1.69, 0.97 ], "fq": 50 
  },
  "lonely": {
    "dict": "happiness", "word": "lonely", "stem": "lone",
    "avg": [ 4.51, 2.86 ], "std": [ 2.68, 1.51 ], "fq": 50 
  },
  "prisoner": {
    "dict": "happiness", "word": "prisoner", "stem": "prison",
    "avg": [ 5.70, 2.86 ], "std": [ 2.56, 1.85 ], "fq": 50 
  },
  "stress": {
    "dict": "happiness", "word": "stress", "stem": "stress",
    "avg": [ 7.45, 2.86 ], "std": [ 2.38, 1.60 ], "fq": 50 
  },
  "violations": {
    "dict": "happiness", "word": "violations", "stem": "violat",
    "avg": [ 7.51, 2.86 ], "std": [ 2.28, 1.43 ], "fq": 50 
  },
  "addict": {
    "dict": "happiness", "word": "addict", "stem": "addict",
    "avg": [ 4.81, 2.84 ], "std": [ 2.46, 1.31 ], "fq": 50 
  },
  "devils": {
    "dict": "happiness", "word": "devils", "stem": "devil",
    "avg": [ 6.07, 2.84 ], "std": [ 2.61, 1.71 ], "fq": 50 
  },
  "dump": {
    "dict": "happiness", "word": "dump", "stem": "dump",
    "avg": [ 4.12, 2.84 ], "std": [ 2.36, 1.33 ], "fq": 50 
  },
  "infection": {
    "dict": "happiness", "word": "infection", "stem": "infect",
    "avg": [ 5.03, 2.84 ], "std": [ 2.77, 1.65 ], "fq": 50 
  },
  "neglected": {
    "dict": "happiness", "word": "neglected", "stem": "neglect",
    "avg": [ 4.83, 2.84 ], "std": [ 2.31, 1.75 ], "fq": 50 
  },
  "penalty": {
    "dict": "happiness", "word": "penalty", "stem": "penalti",
    "avg": [ 5.10, 2.84 ], "std": [ 2.31, 1.31 ], "fq": 50 
  },
  "terrible": {
    "dict": "happiness", "word": "terrible", "stem": "terribl",
    "avg": [ 6.27, 2.84 ], "std": [ 2.44, 1.81 ], "fq": 50 
  },
  "weak": {
    "dict": "happiness", "word": "weak", "stem": "weak",
    "avg": [ 4.10, 2.84 ], "std": [ 2.07, 1.25 ], "fq": 50 
  },
  "annoying": {
    "dict": "happiness", "word": "annoying", "stem": "annoy",
    "avg": [ 6.49, 2.82 ], "std": [ 2.17, 1.32 ], "fq": 50 
  },
  "bills": {
    "dict": "happiness", "word": "bills", "stem": "bill",
    "avg": [ 3.93, 2.82 ], "std": [ 2.56, 1.64 ], "fq": 50 
  },
  "blame": {
    "dict": "happiness", "word": "blame", "stem": "blame",
    "avg": [ 4.05, 2.82 ], "std": [ 2.59, 1.53 ], "fq": 50 
  },
  "burden": {
    "dict": "happiness", "word": "burden", "stem": "burden",
    "avg": [ 5.63, 2.82 ], "std": [ 2.07, 1.53 ], "fq": 50 
  },
  "complaining": {
    "dict": "happiness", "word": "complaining", "stem": "complain",
    "avg": [ 3.52, 2.82 ], "std": [ 2.05, 1.14 ], "fq": 50 
  },
  "danger": {
    "dict": "happiness", "word": "danger", "stem": "danger",
    "avg": [ 7.32, 2.82 ], "std": [ 2.07, 1.64 ], "fq": 50 
  },
  "demise": {
    "dict": "happiness", "word": "demise", "stem": "demis",
    "avg": [ 4.59, 2.82 ], "std": [ 3.07, 1.73 ], "fq": 50 
  },
  "despair": {
    "dict": "happiness", "word": "despair", "stem": "despair",
    "avg": [ 5.68, 2.82 ], "std": [ 2.37, 2.01 ], "fq": 50 
  },
  "disabled": {
    "dict": "happiness", "word": "disabled", "stem": "disabl",
    "avg": [ 3.81, 2.82 ], "std": [ 2.27, 1.19 ], "fq": 50 
  },
  "filthy": {
    "dict": "happiness", "word": "filthy", "stem": "filthi",
    "avg": [ 4.88, 2.82 ], "std": [ 2.29, 1.83 ], "fq": 50 
  },
  "gun": {
    "dict": "happiness", "word": "gun", "stem": "gun",
    "avg": [ 7.02, 2.82 ], "std": [ 1.84, 1.41 ], "fq": 50 
  },
  "lied": {
    "dict": "happiness", "word": "lied", "stem": "lie",
    "avg": [ 5.96, 2.82 ], "std": [ 2.63, 1.21 ], "fq": 50 
  },
  "worry": {
    "dict": "happiness", "word": "worry", "stem": "worri",
    "avg": [ 5.07, 2.82 ], "std": [ 2.74, 1.71 ], "fq": 50 
  },
  "wounds": {
    "dict": "happiness", "word": "wounds", "stem": "wound",
    "avg": [ 5.82, 2.80 ], "std": [ 2.01, 2.02 ], "fq": 50 
  },
  "burns": {
    "dict": "happiness", "word": "burns", "stem": "burn",
    "avg": [ 6.22, 2.78 ], "std": [ 1.91, 1.45 ], "fq": 50 
  },
  "cowards": {
    "dict": "happiness", "word": "cowards", "stem": "coward",
    "avg": [ 4.07, 2.78 ], "std": [ 2.19, 1.36 ], "fq": 50 
  },
  "fever": {
    "dict": "happiness", "word": "fever", "stem": "fever",
    "avg": [ 4.29, 2.78 ], "std": [ 2.31, 1.56 ], "fq": 50 
  },
  "mistake": {
    "dict": "happiness", "word": "mistake", "stem": "mistak",
    "avg": [ 5.18, 2.78 ], "std": [ 2.42, 1.20 ], "fq": 50 
  },
  "trouble": {
    "dict": "happiness", "word": "trouble", "stem": "troubl",
    "avg": [ 5.94, 2.78 ], "std": [ 2.36, 1.47 ], "fq": 50 
  },
  "troubled": {
    "dict": "happiness", "word": "troubled", "stem": "troubl",
    "avg": [ 5.94, 2.78 ], "std": [ 2.36, 1.43 ], "fq": 50 
  },
  "wasted": {
    "dict": "happiness", "word": "wasted", "stem": "wast",
    "avg": [ 4.14, 2.78 ], "std": [ 2.30, 1.17 ], "fq": 50 
  },
  "bitches": {
    "dict": "happiness", "word": "bitches", "stem": "bitch",
    "avg": [ 5.00, 2.76 ], "std": [ 2.19, 1.92 ], "fq": 50 
  },
  "fighting": {
    "dict": "happiness", "word": "fighting", "stem": "fight",
    "avg": [ 7.15, 2.76 ], "std": [ 2.19, 1.57 ], "fq": 50 
  },
  "lost": {
    "dict": "happiness", "word": "lost", "stem": "lost",
    "avg": [ 5.82, 2.76 ], "std": [ 2.62, 1.39 ], "fq": 50 
  },
  "pathetic": {
    "dict": "happiness", "word": "pathetic", "stem": "pathet",
    "avg": [ 3.72, 2.76 ], "std": [ 2.02, 1.29 ], "fq": 50 
  },
  "neglect": {
    "dict": "happiness", "word": "neglect", "stem": "neglect",
    "avg": [ 4.83, 2.76 ], "std": [ 2.31, 2.17 ], "fq": 50 
  },
  "defeated": {
    "dict": "happiness", "word": "defeated", "stem": "defeat",
    "avg": [ 5.09, 2.74 ], "std": [ 3.00, 1.61 ], "fq": 50 
  },
  "stressed": {
    "dict": "happiness", "word": "stressed", "stem": "stress",
    "avg": [ 7.45, 2.74 ], "std": [ 2.38, 1.12 ], "fq": 50 
  },
  "ugly": {
    "dict": "happiness", "word": "ugly", "stem": "ugli",
    "avg": [ 5.38, 2.74 ], "std": [ 2.23, 1.44 ], "fq": 50 
  },
  "violation": {
    "dict": "happiness", "word": "violation", "stem": "violat",
    "avg": [ 7.51, 2.74 ], "std": [ 2.28, 1.08 ], "fq": 50 
  },
  "unholy": {
    "dict": "happiness", "word": "unholy", "stem": "unholi",
    "avg": [ 6.76, 2.73 ], "std": [ 2.68, 1.40 ], "fq": 50 
  },
  "addiction": {
    "dict": "happiness", "word": "addiction", "stem": "addict",
    "avg": [ 4.81, 2.72 ], "std": [ 2.46, 1.46 ], "fq": 50 
  },
  "arrests": {
    "dict": "happiness", "word": "arrests", "stem": "arrest",
    "avg": [ 4.59, 2.72 ], "std": [ 2.10, 1.59 ], "fq": 50 
  },
  "disgrace": {
    "dict": "happiness", "word": "disgrace", "stem": "disgrac",
    "avg": [ 4.88, 2.72 ], "std": [ 2.27, 1.41 ], "fq": 50 
  },
  "struggling": {
    "dict": "happiness", "word": "struggling", "stem": "struggl",
    "avg": [ 7.15, 2.72 ], "std": [ 2.19, 1.21 ], "fq": 50 
  },
  "desperation": {
    "dict": "happiness", "word": "desperation", "stem": "desper",
    "avg": [ 5.68, 2.70 ], "std": [ 2.37, 1.91 ], "fq": 50 
  },
  "distress": {
    "dict": "happiness", "word": "distress", "stem": "distress",
    "avg": [ 6.40, 2.70 ], "std": [ 2.38, 1.42 ], "fq": 50 
  },
  "fight": {
    "dict": "happiness", "word": "fight", "stem": "fight",
    "avg": [ 7.15, 2.70 ], "std": [ 2.19, 1.74 ], "fq": 50 
  },
  "taxes": {
    "dict": "happiness", "word": "taxes", "stem": "tax",
    "avg": [ 3.41, 2.70 ], "std": [ 2.14, 1.53 ], "fq": 50 
  },
  "waste": {
    "dict": "happiness", "word": "waste", "stem": "wast",
    "avg": [ 4.14, 2.70 ], "std": [ 2.30, 1.05 ], "fq": 50 
  },
  "worse": {
    "dict": "happiness", "word": "worse", "stem": "wors",
    "avg": [ 5.74, 2.70 ], "std": [ 2.32, 1.42 ], "fq": 50 
  },
  "sorrows": {
    "dict": "happiness", "word": "sorrows", "stem": "sorrow",
    "avg": [ 5.74, 2.69 ], "std": [ 2.32, 1.78 ], "fq": 50 
  },
  "ache": {
    "dict": "happiness", "word": "ache", "stem": "ach",
    "avg": [ 5.00, 2.68 ], "std": [ 2.45, 1.20 ], "fq": 50 
  },
  "bastards": {
    "dict": "happiness", "word": "bastards", "stem": "bastard",
    "avg": [ 6.07, 2.68 ], "std": [ 2.15, 1.52 ], "fq": 50 
  },
  "fears": {
    "dict": "happiness", "word": "fears", "stem": "fear",
    "avg": [ 6.33, 2.68 ], "std": [ 2.28, 1.27 ], "fq": 50 
  },
  "injuries": {
    "dict": "happiness", "word": "injuries", "stem": "injuri",
    "avg": [ 5.69, 2.68 ], "std": [ 2.06, 1.50 ], "fq": 50 
  },
  "misery": {
    "dict": "happiness", "word": "misery", "stem": "miseri",
    "avg": [ 5.17, 2.68 ], "std": [ 2.69, 2.04 ], "fq": 50 
  },
  "ruin": {
    "dict": "happiness", "word": "ruin", "stem": "ruin",
    "avg": [ 6.21, 2.68 ], "std": [ 2.79, 1.57 ], "fq": 50 
  },
  "shame": {
    "dict": "happiness", "word": "shame", "stem": "shame",
    "avg": [ 4.88, 2.68 ], "std": [ 2.27, 1.30 ], "fq": 50 
  },
  "stupid": {
    "dict": "happiness", "word": "stupid", "stem": "stupid",
    "avg": [ 4.72, 2.68 ], "std": [ 2.71, 1.22 ], "fq": 50 
  },
  "trash": {
    "dict": "happiness", "word": "trash", "stem": "trash",
    "avg": [ 4.16, 2.68 ], "std": [ 2.16, 1.22 ], "fq": 50 
  },
  "deaf": {
    "dict": "happiness", "word": "deaf", "stem": "deaf",
    "avg": [ 3.18, 2.67 ], "std": [ 1.85, 1.33 ], "fq": 50 
  },
  "afraid": {
    "dict": "happiness", "word": "afraid", "stem": "afraid",
    "avg": [ 6.67, 2.66 ], "std": [ 2.54, 1.51 ], "fq": 50 
  },
  "loneliness": {
    "dict": "happiness", "word": "loneliness", "stem": "loneli",
    "avg": [ 4.56, 2.66 ], "std": [ 2.97, 1.81 ], "fq": 50 
  },
  "penalties": {
    "dict": "happiness", "word": "penalties", "stem": "penalti",
    "avg": [ 5.10, 2.66 ], "std": [ 2.31, 1.08 ], "fq": 50 
  },
  "surgery": {
    "dict": "happiness", "word": "surgery", "stem": "surgeri",
    "avg": [ 6.35, 2.66 ], "std": [ 2.32, 1.75 ], "fq": 50 
  },
  "tensions": {
    "dict": "happiness", "word": "tensions", "stem": "tension",
    "avg": [ 7.45, 2.66 ], "std": [ 2.38, 1.26 ], "fq": 50 
  },
  "bad": {
    "dict": "happiness", "word": "bad", "stem": "bad",
    "avg": [ 5.74, 2.64 ], "std": [ 2.32, 1.47 ], "fq": 50 
  },
  "demons": {
    "dict": "happiness", "word": "demons", "stem": "demon",
    "avg": [ 6.76, 2.64 ], "std": [ 2.68, 2.07 ], "fq": 50 
  },
  "guilty": {
    "dict": "happiness", "word": "guilty", "stem": "guilti",
    "avg": [ 6.04, 2.64 ], "std": [ 2.76, 1.59 ], "fq": 50 
  },
  "sin": {
    "dict": "happiness", "word": "sin", "stem": "sin",
    "avg": [ 6.29, 2.64 ], "std": [ 2.43, 1.70 ], "fq": 50 
  },
  "heartaches": {
    "dict": "happiness", "word": "heartaches", "stem": "heartach",
    "avg": [ 4.78, 2.63 ], "std": [ 2.84, 2.02 ], "fq": 50 
  },
  "beaten": {
    "dict": "happiness", "word": "beaten", "stem": "beaten",
    "avg": [ 5.52, 2.62 ], "std": [ 2.87, 1.59 ], "fq": 50 
  },
  "lies": {
    "dict": "happiness", "word": "lies", "stem": "lie",
    "avg": [ 5.96, 2.62 ], "std": [ 2.63, 1.38 ], "fq": 50 
  },
  "nasty": {
    "dict": "happiness", "word": "nasty", "stem": "nasti",
    "avg": [ 4.89, 2.62 ], "std": [ 2.50, 1.23 ], "fq": 50 
  },
  "retarded": {
    "dict": "happiness", "word": "retarded", "stem": "retard",
    "avg": [ 3.39, 2.62 ], "std": [ 2.22, 1.54 ], "fq": 50 
  },
  "rude": {
    "dict": "happiness", "word": "rude", "stem": "rude",
    "avg": [ 6.31, 2.62 ], "std": [ 2.47, 1.64 ], "fq": 50 
  },
  "threatened": {
    "dict": "happiness", "word": "threatened", "stem": "threaten",
    "avg": [ 5.52, 2.62 ], "std": [ 2.45, 1.47 ], "fq": 50 
  },
  "violated": {
    "dict": "happiness", "word": "violated", "stem": "violat",
    "avg": [ 6.83, 2.62 ], "std": [ 2.26, 1.38 ], "fq": 50 
  },
  "abortion": {
    "dict": "happiness", "word": "abortion", "stem": "abort",
    "avg": [ 5.39, 2.60 ], "std": [ 2.80, 1.53 ], "fq": 50 
  },
  "brutal": {
    "dict": "happiness", "word": "brutal", "stem": "brutal",
    "avg": [ 6.60, 2.60 ], "std": [ 2.36, 2.08 ], "fq": 50 
  },
  "crash": {
    "dict": "happiness", "word": "crash", "stem": "crash",
    "avg": [ 6.95, 2.60 ], "std": [ 2.44, 1.37 ], "fq": 50 
  },
  "error": {
    "dict": "happiness", "word": "error", "stem": "error",
    "avg": [ 4.07, 2.60 ], "std": [ 1.69, 0.81 ], "fq": 50 
  },
  "lie": {
    "dict": "happiness", "word": "lie", "stem": "lie",
    "avg": [ 5.96, 2.60 ], "std": [ 2.63, 1.62 ], "fq": 50 
  },
  "mad": {
    "dict": "happiness", "word": "mad", "stem": "mad",
    "avg": [ 6.76, 2.60 ], "std": [ 2.26, 1.32 ], "fq": 50 
  },
  "selfish": {
    "dict": "happiness", "word": "selfish", "stem": "selfish",
    "avg": [ 5.50, 2.60 ], "std": [ 2.62, 1.05 ], "fq": 50 
  },
  "worries": {
    "dict": "happiness", "word": "worries", "stem": "worri",
    "avg": [ 5.07, 2.60 ], "std": [ 2.74, 1.32 ], "fq": 50 
  },
  "infections": {
    "dict": "happiness", "word": "infections", "stem": "infect",
    "avg": [ 5.03, 2.59 ], "std": [ 2.77, 1.91 ], "fq": 50 
  },
  "annoyed": {
    "dict": "happiness", "word": "annoyed", "stem": "annoy",
    "avg": [ 6.49, 2.58 ], "std": [ 2.17, 1.64 ], "fq": 50 
  },
  "blind": {
    "dict": "happiness", "word": "blind", "stem": "blind",
    "avg": [ 4.39, 2.58 ], "std": [ 2.36, 1.23 ], "fq": 50 
  },
  "cheated": {
    "dict": "happiness", "word": "cheated", "stem": "cheat",
    "avg": [ 7.24, 2.58 ], "std": [ 2.06, 1.59 ], "fq": 50 
  },
  "damage": {
    "dict": "happiness", "word": "damage", "stem": "damag",
    "avg": [ 5.57, 2.58 ], "std": [ 2.26, 1.50 ], "fq": 50 
  },
  "disgusting": {
    "dict": "happiness", "word": "disgusting", "stem": "disgust",
    "avg": [ 5.42, 2.58 ], "std": [ 2.59, 1.47 ], "fq": 50 
  },
  "guilt": {
    "dict": "happiness", "word": "guilt", "stem": "guilt",
    "avg": [ 6.04, 2.58 ], "std": [ 2.76, 1.46 ], "fq": 50 
  },
  "lying": {
    "dict": "happiness", "word": "lying", "stem": "lie",
    "avg": [ 5.96, 2.58 ], "std": [ 2.63, 1.70 ], "fq": 50 
  },
  "rotten": {
    "dict": "happiness", "word": "rotten", "stem": "rotten",
    "avg": [ 4.53, 2.58 ], "std": [ 2.38, 1.60 ], "fq": 50 
  },
  "scared": {
    "dict": "happiness", "word": "scared", "stem": "scare",
    "avg": [ 6.82, 2.58 ], "std": [ 2.03, 1.43 ], "fq": 50 
  },
  "shitty": {
    "dict": "happiness", "word": "shitty", "stem": "shitti",
    "avg": [ 4.26, 2.58 ], "std": [ 2.10, 1.57 ], "fq": 50 
  },
  "starving": {
    "dict": "happiness", "word": "starving", "stem": "starv",
    "avg": [ 5.61, 2.58 ], "std": [ 2.53, 1.47 ], "fq": 50 
  },
  "stroke": {
    "dict": "happiness", "word": "stroke", "stem": "stroke",
    "avg": [ 6.26, 2.58 ], "std": [ 2.87, 1.60 ], "fq": 50 
  },
  "betrayed": {
    "dict": "happiness", "word": "betrayed", "stem": "betray",
    "avg": [ 7.24, 2.57 ], "std": [ 2.06, 1.83 ], "fq": 50 
  },
  "nightmares": {
    "dict": "happiness", "word": "nightmares", "stem": "nightmar",
    "avg": [ 7.59, 2.56 ], "std": [ 2.23, 1.65 ], "fq": 50 
  },
  "assault": {
    "dict": "happiness", "word": "assault", "stem": "assault",
    "avg": [ 7.51, 2.56 ], "std": [ 2.28, 1.66 ], "fq": 50 
  },
  "beating": {
    "dict": "happiness", "word": "beating", "stem": "beat",
    "avg": [ 5.52, 2.56 ], "std": [ 2.87, 1.90 ], "fq": 50 
  },
  "grave": {
    "dict": "happiness", "word": "grave", "stem": "grave",
    "avg": [ 3.56, 2.56 ], "std": [ 1.95, 1.85 ], "fq": 50 
  },
  "loss": {
    "dict": "happiness", "word": "loss", "stem": "loss",
    "avg": [ 5.29, 2.56 ], "std": [ 2.04, 1.50 ], "fq": 50 
  },
  "rage": {
    "dict": "happiness", "word": "rage", "stem": "rage",
    "avg": [ 8.17, 2.56 ], "std": [ 1.40, 1.51 ], "fq": 50 
  },
  "upset": {
    "dict": "happiness", "word": "upset", "stem": "upset",
    "avg": [ 5.86, 2.56 ], "std": [ 2.40, 1.43 ], "fq": 50 
  },
  "corpse": {
    "dict": "happiness", "word": "corpse", "stem": "corps",
    "avg": [ 4.74, 2.55 ], "std": [ 2.94, 1.96 ], "fq": 50 
  },
  "abandoned": {
    "dict": "happiness", "word": "abandoned", "stem": "abandon",
    "avg": [ 5.64, 2.54 ], "std": [ 2.99, 1.37 ], "fq": 50 
  },
  "broke": {
    "dict": "happiness", "word": "broke", "stem": "broke",
    "avg": [ 6.21, 2.54 ], "std": [ 2.79, 1.28 ], "fq": 50 
  },
  "harm": {
    "dict": "happiness", "word": "harm", "stem": "harm",
    "avg": [ 5.69, 2.54 ], "std": [ 2.06, 1.45 ], "fq": 50 
  },
  "hurricane": {
    "dict": "happiness", "word": "hurricane", "stem": "hurrican",
    "avg": [ 6.83, 2.54 ], "std": [ 2.06, 1.57 ], "fq": 50 
  },
  "miserable": {
    "dict": "happiness", "word": "miserable", "stem": "miser",
    "avg": [ 3.72, 2.54 ], "std": [ 2.02, 1.67 ], "fq": 50 
  },
  "pissed": {
    "dict": "happiness", "word": "pissed", "stem": "piss",
    "avg": [ 5.76, 2.54 ], "std": [ 2.15, 1.33 ], "fq": 50 
  },
  "ruined": {
    "dict": "happiness", "word": "ruined", "stem": "ruin",
    "avg": [ 6.21, 2.54 ], "std": [ 2.79, 1.62 ], "fq": 50 
  },
  "tumor": {
    "dict": "happiness", "word": "tumor", "stem": "tumor",
    "avg": [ 6.51, 2.53 ], "std": [ 2.85, 2.00 ], "fq": 50 
  },
  "attacked": {
    "dict": "happiness", "word": "attacked", "stem": "attack",
    "avg": [ 5.83, 2.52 ], "std": [ 2.33, 1.55 ], "fq": 50 
  },
  "bastard": {
    "dict": "happiness", "word": "bastard", "stem": "bastard",
    "avg": [ 6.07, 2.52 ], "std": [ 2.15, 1.30 ], "fq": 50 
  },
  "destroy": {
    "dict": "happiness", "word": "destroy", "stem": "destroy",
    "avg": [ 6.83, 2.52 ], "std": [ 2.38, 1.81 ], "fq": 50 
  },
  "failing": {
    "dict": "happiness", "word": "failing", "stem": "fail",
    "avg": [ 7.15, 2.52 ], "std": [ 2.40, 1.27 ], "fq": 50 
  },
  "shooting": {
    "dict": "happiness", "word": "shooting", "stem": "shoot",
    "avg": [ 5.73, 2.52 ], "std": [ 2.09, 1.74 ], "fq": 50 
  },
  "useless": {
    "dict": "happiness", "word": "useless", "stem": "useless",
    "avg": [ 4.87, 2.52 ], "std": [ 2.58, 1.42 ], "fq": 50 
  },
  "motherfuckers": {
    "dict": "happiness", "word": "motherfuckers", "stem": "motherfuck",
    "avg": [ 6.07, 2.51 ], "std": [ 2.15, 2.47 ], "fq": 50 
  },
  "betray": {
    "dict": "happiness", "word": "betray", "stem": "betray",
    "avg": [ 7.24, 2.50 ], "std": [ 2.06, 1.63 ], "fq": 50 
  },
  "shit": {
    "dict": "happiness", "word": "shit", "stem": "shit",
    "avg": [ 4.12, 2.50 ], "std": [ 2.36, 1.52 ], "fq": 50 
  },
  "shot": {
    "dict": "happiness", "word": "shot", "stem": "shot",
    "avg": [ 5.73, 2.50 ], "std": [ 2.09, 1.66 ], "fq": 50 
  },
  "crisis": {
    "dict": "happiness", "word": "crisis", "stem": "crisi",
    "avg": [ 5.44, 2.48 ], "std": [ 3.07, 1.67 ], "fq": 50 
  },
  "damaged": {
    "dict": "happiness", "word": "damaged", "stem": "damag",
    "avg": [ 5.57, 2.48 ], "std": [ 2.26, 1.03 ], "fq": 50 
  },
  "recession": {
    "dict": "happiness", "word": "recession", "stem": "recess",
    "avg": [ 3.91, 2.48 ], "std": [ 1.92, 1.50 ], "fq": 50 
  },
  "slap": {
    "dict": "happiness", "word": "slap", "stem": "slap",
    "avg": [ 6.46, 2.48 ], "std": [ 2.58, 1.53 ], "fq": 50 
  },
  "attacks": {
    "dict": "happiness", "word": "attacks", "stem": "attack",
    "avg": [ 7.17, 2.46 ], "std": [ 2.06, 1.46 ], "fq": 50 
  },
  "crashed": {
    "dict": "happiness", "word": "crashed", "stem": "crash",
    "avg": [ 6.95, 2.46 ], "std": [ 2.44, 1.40 ], "fq": 50 
  },
  "losses": {
    "dict": "happiness", "word": "losses", "stem": "loss",
    "avg": [ 5.29, 2.46 ], "std": [ 2.04, 1.45 ], "fq": 50 
  },
  "panic": {
    "dict": "happiness", "word": "panic", "stem": "panic",
    "avg": [ 7.02, 2.46 ], "std": [ 2.02, 1.34 ], "fq": 50 
  },
  "burial": {
    "dict": "happiness", "word": "burial", "stem": "burial",
    "avg": [ 5.08, 2.44 ], "std": [ 2.40, 1.92 ], "fq": 50 
  },
  "cheat": {
    "dict": "happiness", "word": "cheat", "stem": "cheat",
    "avg": [ 7.24, 2.44 ], "std": [ 2.06, 1.23 ], "fq": 50 
  },
  "dangerous": {
    "dict": "happiness", "word": "dangerous", "stem": "danger",
    "avg": [ 7.32, 2.44 ], "std": [ 2.07, 1.46 ], "fq": 50 
  },
  "drowning": {
    "dict": "happiness", "word": "drowning", "stem": "drown",
    "avg": [ 6.57, 2.44 ], "std": [ 2.33, 1.59 ], "fq": 50 
  },
  "hating": {
    "dict": "happiness", "word": "hating", "stem": "hate",
    "avg": [ 6.95, 2.44 ], "std": [ 2.56, 1.45 ], "fq": 50 
  },
  "prisoners": {
    "dict": "happiness", "word": "prisoners", "stem": "prison",
    "avg": [ 5.70, 2.44 ], "std": [ 2.56, 1.46 ], "fq": 50 
  },
  "arrest": {
    "dict": "happiness", "word": "arrest", "stem": "arrest",
    "avg": [ 4.59, 2.42 ], "std": [ 2.10, 1.49 ], "fq": 50 
  },
  "attack": {
    "dict": "happiness", "word": "attack", "stem": "attack",
    "avg": [ 7.17, 2.42 ], "std": [ 2.06, 1.43 ], "fq": 50 
  },
  "flood": {
    "dict": "happiness", "word": "flood", "stem": "flood",
    "avg": [ 6.00, 2.42 ], "std": [ 2.02, 1.37 ], "fq": 50 
  },
  "ill": {
    "dict": "happiness", "word": "ill", "stem": "ill",
    "avg": [ 4.71, 2.42 ], "std": [ 2.24, 1.23 ], "fq": 50 
  },
  "killer": {
    "dict": "happiness", "word": "killer", "stem": "killer",
    "avg": [ 7.86, 2.42 ], "std": [ 1.89, 1.93 ], "fq": 50 
  },
  "negative": {
    "dict": "happiness", "word": "negative", "stem": "neg",
    "avg": [ 5.57, 2.42 ], "std": [ 2.26, 1.05 ], "fq": 50 
  },
  "worried": {
    "dict": "happiness", "word": "worried", "stem": "worri",
    "avg": [ 5.80, 2.42 ], "std": [ 2.39, 1.18 ], "fq": 50 
  },
  "wounded": {
    "dict": "happiness", "word": "wounded", "stem": "wound",
    "avg": [ 5.82, 2.42 ], "std": [ 2.01, 1.55 ], "fq": 50 
  },
  "slaughter": {
    "dict": "happiness", "word": "slaughter", "stem": "slaughter",
    "avg": [ 6.77, 2.41 ], "std": [ 2.42, 1.84 ], "fq": 50 
  },
  "asshole": {
    "dict": "happiness", "word": "asshole", "stem": "asshol",
    "avg": [ 6.07, 2.40 ], "std": [ 2.15, 1.60 ], "fq": 50 
  },
  "weapons": {
    "dict": "happiness", "word": "weapons", "stem": "weapon",
    "avg": [ 6.03, 2.40 ], "std": [ 1.89, 1.69 ], "fq": 50 
  },
  "sad": {
    "dict": "happiness", "word": "sad", "stem": "sad",
    "avg": [ 4.13, 2.38 ], "std": [ 2.38, 1.61 ], "fq": 50 
  },
  "victim": {
    "dict": "happiness", "word": "victim", "stem": "victim",
    "avg": [ 6.06, 2.38 ], "std": [ 2.32, 1.41 ], "fq": 50 
  },
  "hurting": {
    "dict": "happiness", "word": "hurting", "stem": "hurt",
    "avg": [ 5.85, 2.36 ], "std": [ 2.49, 1.12 ], "fq": 50 
  },
  "threat": {
    "dict": "happiness", "word": "threat", "stem": "threat",
    "avg": [ 5.52, 2.36 ], "std": [ 2.45, 1.31 ], "fq": 50 
  },
  "frustration": {
    "dict": "happiness", "word": "frustration", "stem": "frustrat",
    "avg": [ 5.61, 2.34 ], "std": [ 2.76, 1.19 ], "fq": 50 
  },
  "hate": {
    "dict": "happiness", "word": "hate", "stem": "hate",
    "avg": [ 6.95, 2.34 ], "std": [ 2.56, 1.88 ], "fq": 50 
  },
  "grief": {
    "dict": "happiness", "word": "grief", "stem": "grief",
    "avg": [ 4.78, 2.33 ], "std": [ 2.84, 1.78 ], "fq": 50 
  },
  "accident": {
    "dict": "happiness", "word": "accident", "stem": "accid",
    "avg": [ 6.26, 2.32 ], "std": [ 2.87, 1.52 ], "fq": 50 
  },
  "angry": {
    "dict": "happiness", "word": "angry", "stem": "angri",
    "avg": [ 7.17, 2.32 ], "std": [ 2.07, 1.24 ], "fq": 50 
  },
  "fear": {
    "dict": "happiness", "word": "fear", "stem": "fear",
    "avg": [ 6.33, 2.32 ], "std": [ 2.28, 1.30 ], "fq": 50 
  },
  "nightmare": {
    "dict": "happiness", "word": "nightmare", "stem": "nightmar",
    "avg": [ 7.59, 2.32 ], "std": [ 2.23, 1.87 ], "fq": 50 
  },
  "poor": {
    "dict": "happiness", "word": "poor", "stem": "poor",
    "avg": [ 3.72, 2.32 ], "std": [ 2.02, 1.28 ], "fq": 50 
  },
  "victims": {
    "dict": "happiness", "word": "victims", "stem": "victim",
    "avg": [ 6.06, 2.32 ], "std": [ 2.32, 1.50 ], "fq": 50 
  },
  "anger": {
    "dict": "happiness", "word": "anger", "stem": "anger",
    "avg": [ 7.63, 2.30 ], "std": [ 1.91, 1.42 ], "fq": 50 
  },
  "fired": {
    "dict": "happiness", "word": "fired", "stem": "fire",
    "avg": [ 7.17, 2.30 ], "std": [ 2.06, 1.57 ], "fq": 50 
  },
  "fraud": {
    "dict": "happiness", "word": "fraud", "stem": "fraud",
    "avg": [ 5.75, 2.30 ], "std": [ 2.45, 1.18 ], "fq": 50 
  },
  "thieves": {
    "dict": "happiness", "word": "thieves", "stem": "thiev",
    "avg": [ 6.89, 2.29 ], "std": [ 2.13, 1.31 ], "fq": 50 
  },
  "heartache": {
    "dict": "happiness", "word": "heartache", "stem": "heartach",
    "avg": [ 4.78, 2.28 ], "std": [ 2.84, 1.50 ], "fq": 50 
  },
  "cheating": {
    "dict": "happiness", "word": "cheating", "stem": "cheat",
    "avg": [ 4.93, 2.26 ], "std": [ 2.23, 1.19 ], "fq": 50 
  },
  "destruction": {
    "dict": "happiness", "word": "destruction", "stem": "destruct",
    "avg": [ 5.82, 2.26 ], "std": [ 2.71, 1.51 ], "fq": 50 
  },
  "disappointed": {
    "dict": "happiness", "word": "disappointed", "stem": "disappoint",
    "avg": [ 4.92, 2.26 ], "std": [ 2.64, 1.03 ], "fq": 50 
  },
  "bombing": {
    "dict": "happiness", "word": "bombing", "stem": "bomb",
    "avg": [ 7.15, 2.24 ], "std": [ 2.40, 1.48 ], "fq": 50 
  },
  "devil": {
    "dict": "happiness", "word": "devil", "stem": "devil",
    "avg": [ 6.07, 2.24 ], "std": [ 2.61, 1.55 ], "fq": 50 
  },
  "horrible": {
    "dict": "happiness", "word": "horrible", "stem": "horribl",
    "avg": [ 5.38, 2.24 ], "std": [ 2.23, 1.48 ], "fq": 50 
  },
  "suffered": {
    "dict": "happiness", "word": "suffered", "stem": "suffer",
    "avg": [ 5.00, 2.24 ], "std": [ 2.45, 1.60 ], "fq": 50 
  },
  "hatred": {
    "dict": "happiness", "word": "hatred", "stem": "hatr",
    "avg": [ 6.66, 2.22 ], "std": [ 2.56, 1.86 ], "fq": 50 
  },
  "hell": {
    "dict": "happiness", "word": "hell", "stem": "hell",
    "avg": [ 5.38, 2.22 ], "std": [ 2.62, 1.47 ], "fq": 50 
  },
  "injured": {
    "dict": "happiness", "word": "injured", "stem": "injur",
    "avg": [ 5.82, 2.22 ], "std": [ 2.01, 1.11 ], "fq": 50 
  },
  "suffering": {
    "dict": "happiness", "word": "suffering", "stem": "suffer",
    "avg": [ 6.40, 2.22 ], "std": [ 2.38, 1.71 ], "fq": 50 
  },
  "cried": {
    "dict": "happiness", "word": "cried", "stem": "cri",
    "avg": [ 7.04, 2.20 ], "std": [ 1.96, 1.29 ], "fq": 50 
  },
  "crime": {
    "dict": "happiness", "word": "crime", "stem": "crime",
    "avg": [ 5.41, 2.20 ], "std": [ 2.69, 1.26 ], "fq": 50 
  },
  "loser": {
    "dict": "happiness", "word": "loser", "stem": "loser",
    "avg": [ 4.95, 2.20 ], "std": [ 2.57, 1.11 ], "fq": 50 
  },
  "depressed": {
    "dict": "happiness", "word": "depressed", "stem": "depress",
    "avg": [ 4.54, 2.18 ], "std": [ 3.19, 1.79 ], "fq": 50 
  },
  "divorce": {
    "dict": "happiness", "word": "divorce", "stem": "divorc",
    "avg": [ 6.33, 2.18 ], "std": [ 2.71, 1.32 ], "fq": 50 
  },
  "hurt": {
    "dict": "happiness", "word": "hurt", "stem": "hurt",
    "avg": [ 5.85, 2.18 ], "std": [ 2.49, 1.37 ], "fq": 50 
  },
  "agony": {
    "dict": "happiness", "word": "agony", "stem": "agoni",
    "avg": [ 6.06, 2.16 ], "std": [ 2.67, 1.88 ], "fq": 50 
  },
  "drowned": {
    "dict": "happiness", "word": "drowned", "stem": "drown",
    "avg": [ 6.57, 2.16 ], "std": [ 2.33, 1.60 ], "fq": 50 
  },
  "pollution": {
    "dict": "happiness", "word": "pollution", "stem": "pollut",
    "avg": [ 6.08, 2.16 ], "std": [ 2.42, 1.18 ], "fq": 50 
  },
  "corruption": {
    "dict": "happiness", "word": "corruption", "stem": "corrupt",
    "avg": [ 4.67, 2.14 ], "std": [ 2.35, 1.31 ], "fq": 50 
  },
  "crimes": {
    "dict": "happiness", "word": "crimes", "stem": "crime",
    "avg": [ 5.41, 2.14 ], "std": [ 2.69, 1.37 ], "fq": 50 
  },
  "hated": {
    "dict": "happiness", "word": "hated", "stem": "hate",
    "avg": [ 6.95, 2.14 ], "std": [ 2.56, 1.29 ], "fq": 50 
  },
  "hurts": {
    "dict": "happiness", "word": "hurts", "stem": "hurt",
    "avg": [ 5.85, 2.14 ], "std": [ 2.49, 1.20 ], "fq": 50 
  },
  "painful": {
    "dict": "happiness", "word": "painful", "stem": "pain",
    "avg": [ 6.50, 2.12 ], "std": [ 2.49, 1.45 ], "fq": 50 
  },
  "sorrow": {
    "dict": "happiness", "word": "sorrow", "stem": "sorrow",
    "avg": [ 5.74, 2.12 ], "std": [ 2.32, 1.56 ], "fq": 50 
  },
  "unhappy": {
    "dict": "happiness", "word": "unhappy", "stem": "unhappi",
    "avg": [ 4.18, 2.12 ], "std": [ 2.50, 1.36 ], "fq": 50 
  },
  "heartbreak": {
    "dict": "happiness", "word": "heartbreak", "stem": "heartbreak",
    "avg": [ 4.78, 2.11 ], "std": [ 2.84, 1.31 ], "fq": 50 
  },
  "dying": {
    "dict": "happiness", "word": "dying", "stem": "die",
    "avg": [ 4.59, 2.10 ], "std": [ 3.07, 1.47 ], "fq": 50 
  },
  "funeral": {
    "dict": "happiness", "word": "funeral", "stem": "funer",
    "avg": [ 4.94, 2.10 ], "std": [ 3.21, 1.56 ], "fq": 50 
  },
  "pain": {
    "dict": "happiness", "word": "pain", "stem": "pain",
    "avg": [ 6.50, 2.10 ], "std": [ 2.49, 1.28 ], "fq": 50 
  },
  "worst": {
    "dict": "happiness", "word": "worst", "stem": "worst",
    "avg": [ 5.74, 2.10 ], "std": [ 2.32, 1.34 ], "fq": 50 
  },
  "rejected": {
    "dict": "happiness", "word": "rejected", "stem": "reject",
    "avg": [ 6.37, 2.08 ], "std": [ 2.56, 1.12 ], "fq": 50 
  },
  "suffer": {
    "dict": "happiness", "word": "suffer", "stem": "suffer",
    "avg": [ 5.00, 2.08 ], "std": [ 2.45, 1.38 ], "fq": 50 
  },
  "bankruptcy": {
    "dict": "happiness", "word": "bankruptcy", "stem": "bankruptci",
    "avg": [ 4.95, 2.06 ], "std": [ 2.81, 1.60 ], "fq": 50 
  },
  "fails": {
    "dict": "happiness", "word": "fails", "stem": "fail",
    "avg": [ 7.15, 2.06 ], "std": [ 2.40, 1.20 ], "fq": 50 
  },
  "failure": {
    "dict": "happiness", "word": "failure", "stem": "failur",
    "avg": [ 4.95, 2.06 ], "std": [ 2.81, 1.22 ], "fq": 50 
  },
  "hates": {
    "dict": "happiness", "word": "hates", "stem": "hate",
    "avg": [ 6.95, 2.06 ], "std": [ 2.56, 1.33 ], "fq": 50 
  },
  "prison": {
    "dict": "happiness", "word": "prison", "stem": "prison",
    "avg": [ 5.70, 2.06 ], "std": [ 2.56, 1.48 ], "fq": 50 
  },
  "slave": {
    "dict": "happiness", "word": "slave", "stem": "slave",
    "avg": [ 6.21, 2.06 ], "std": [ 2.93, 1.46 ], "fq": 50 
  },
  "slaves": {
    "dict": "happiness", "word": "slaves", "stem": "slave",
    "avg": [ 6.21, 2.06 ], "std": [ 2.93, 1.37 ], "fq": 50 
  },
  "tragedy": {
    "dict": "happiness", "word": "tragedy", "stem": "tragedi",
    "avg": [ 6.24, 2.06 ], "std": [ 2.64, 1.38 ], "fq": 50 
  },
  "violent": {
    "dict": "happiness", "word": "violent", "stem": "violent",
    "avg": [ 6.89, 2.06 ], "std": [ 2.47, 1.35 ], "fq": 50 
  },
  "crying": {
    "dict": "happiness", "word": "crying", "stem": "cri",
    "avg": [ 7.04, 2.04 ], "std": [ 1.96, 1.24 ], "fq": 50 
  },
  "destroyed": {
    "dict": "happiness", "word": "destroyed", "stem": "destroy",
    "avg": [ 6.83, 2.04 ], "std": [ 2.38, 1.34 ], "fq": 50 
  },
  "injury": {
    "dict": "happiness", "word": "injury", "stem": "injuri",
    "avg": [ 5.69, 2.04 ], "std": [ 2.06, 1.24 ], "fq": 50 
  },
  "rejection": {
    "dict": "happiness", "word": "rejection", "stem": "reject",
    "avg": [ 6.37, 2.02 ], "std": [ 2.56, 1.33 ], "fq": 50 
  },
  "motherfucker": {
    "dict": "happiness", "word": "motherfucker", "stem": "motherfuck",
    "avg": [ 6.07, 2.02 ], "std": [ 2.15, 1.66 ], "fq": 50 
  },
  "sick": {
    "dict": "happiness", "word": "sick", "stem": "sick",
    "avg": [ 5.61, 2.02 ], "std": [ 2.67, 1.08 ], "fq": 50 
  },
  "dead": {
    "dict": "happiness", "word": "dead", "stem": "dead",
    "avg": [ 5.73, 2.00 ], "std": [ 2.73, 1.32 ], "fq": 50 
  },
  "illness": {
    "dict": "happiness", "word": "illness", "stem": "ill",
    "avg": [ 4.71, 2.00 ], "std": [ 2.24, 1.18 ], "fq": 50 
  },
  "killers": {
    "dict": "happiness", "word": "killers", "stem": "killer",
    "avg": [ 7.86, 2.00 ], "std": [ 1.89, 1.53 ], "fq": 50 
  },
  "punishment": {
    "dict": "happiness", "word": "punishment", "stem": "punish",
    "avg": [ 5.93, 2.00 ], "std": [ 2.40, 1.34 ], "fq": 50 
  },
  "criminal": {
    "dict": "happiness", "word": "criminal", "stem": "crimin",
    "avg": [ 4.79, 1.98 ], "std": [ 2.51, 1.27 ], "fq": 50 
  },
  "depression": {
    "dict": "happiness", "word": "depression", "stem": "depress",
    "avg": [ 4.54, 1.98 ], "std": [ 3.19, 1.56 ], "fq": 50 
  },
  "headache": {
    "dict": "happiness", "word": "headache", "stem": "headach",
    "avg": [ 5.07, 1.98 ], "std": [ 2.74, 1.12 ], "fq": 50 
  },
  "poverty": {
    "dict": "happiness", "word": "poverty", "stem": "poverti",
    "avg": [ 4.87, 1.98 ], "std": [ 2.66, 1.12 ], "fq": 50 
  },
  "tumors": {
    "dict": "happiness", "word": "tumors", "stem": "tumor",
    "avg": [ 6.51, 1.98 ], "std": [ 2.85, 1.35 ], "fq": 50 
  },
  "bomb": {
    "dict": "happiness", "word": "bomb", "stem": "bomb",
    "avg": [ 7.15, 1.96 ], "std": [ 2.40, 1.28 ], "fq": 50 
  },
  "disaster": {
    "dict": "happiness", "word": "disaster", "stem": "disast",
    "avg": [ 6.33, 1.96 ], "std": [ 2.70, 1.43 ], "fq": 50 
  },
  "fail": {
    "dict": "happiness", "word": "fail", "stem": "fail",
    "avg": [ 7.15, 1.96 ], "std": [ 2.40, 1.03 ], "fq": 50 
  },
  "poison": {
    "dict": "happiness", "word": "poison", "stem": "poison",
    "avg": [ 6.05, 1.94 ], "std": [ 2.82, 1.15 ], "fq": 50 
  },
  "depressing": {
    "dict": "happiness", "word": "depressing", "stem": "depress",
    "avg": [ 4.54, 1.90 ], "std": [ 3.19, 1.22 ], "fq": 50 
  },
  "evil": {
    "dict": "happiness", "word": "evil", "stem": "evil",
    "avg": [ 6.39, 1.90 ], "std": [ 2.44, 1.28 ], "fq": 50 
  },
  "wars": {
    "dict": "happiness", "word": "wars", "stem": "war",
    "avg": [ 7.49, 1.90 ], "std": [ 2.16, 1.33 ], "fq": 50 
  },
  "abuse": {
    "dict": "happiness", "word": "abuse", "stem": "abus",
    "avg": [ 6.83, 1.88 ], "std": [ 2.70, 1.24 ], "fq": 50 
  },
  "sadness": {
    "dict": "happiness", "word": "sadness", "stem": "sad",
    "avg": [ 4.13, 1.88 ], "std": [ 2.38, 1.19 ], "fq": 50 
  },
  "cruel": {
    "dict": "happiness", "word": "cruel", "stem": "cruel",
    "avg": [ 5.68, 1.84 ], "std": [ 2.65, 1.15 ], "fq": 50 
  },
  "cry": {
    "dict": "happiness", "word": "cry", "stem": "cri",
    "avg": [ 7.04, 1.84 ], "std": [ 1.96, 1.28 ], "fq": 50 
  },
  "failed": {
    "dict": "happiness", "word": "failed", "stem": "fail",
    "avg": [ 7.15, 1.84 ], "std": [ 2.40, 1.00 ], "fq": 50 
  },
  "sickness": {
    "dict": "happiness", "word": "sickness", "stem": "sick",
    "avg": [ 5.61, 1.84 ], "std": [ 2.67, 1.18 ], "fq": 50 
  },
  "abused": {
    "dict": "happiness", "word": "abused", "stem": "abus",
    "avg": [ 6.83, 1.83 ], "std": [ 2.70, 1.31 ], "fq": 50 
  },
  "tortured": {
    "dict": "happiness", "word": "tortured", "stem": "tortur",
    "avg": [ 6.10, 1.82 ], "std": [ 2.77, 1.42 ], "fq": 50 
  },
  "fatal": {
    "dict": "happiness", "word": "fatal", "stem": "fatal",
    "avg": [ 4.61, 1.80 ], "std": [ 2.24, 1.53 ], "fq": 50 
  },
  "killings": {
    "dict": "happiness", "word": "killings", "stem": "kill",
    "avg": [ 5.09, 1.80 ], "std": [ 3.00, 1.54 ], "fq": 50 
  },
  "murdered": {
    "dict": "happiness", "word": "murdered", "stem": "murder",
    "avg": [ 7.47, 1.80 ], "std": [ 2.18, 1.63 ], "fq": 50 
  },
  "war": {
    "dict": "happiness", "word": "war", "stem": "war",
    "avg": [ 7.49, 1.80 ], "std": [ 2.16, 1.41 ], "fq": 50 
  },
  "kills": {
    "dict": "happiness", "word": "kills", "stem": "kill",
    "avg": [ 5.09, 1.78 ], "std": [ 3.00, 1.23 ], "fq": 50 
  },
  "jail": {
    "dict": "happiness", "word": "jail", "stem": "jail",
    "avg": [ 5.49, 1.76 ], "std": [ 2.67, 1.02 ], "fq": 50 
  },
  "terror": {
    "dict": "happiness", "word": "terror", "stem": "terror",
    "avg": [ 7.02, 1.76 ], "std": [ 2.02, 1.00 ], "fq": 50 
  },
  "killing": {
    "dict": "happiness", "word": "killing", "stem": "kill",
    "avg": [ 5.09, 1.70 ], "std": [ 3.00, 1.36 ], "fq": 50 
  },
  "deaths": {
    "dict": "happiness", "word": "deaths", "stem": "death",
    "avg": [ 4.59, 1.64 ], "std": [ 3.07, 1.14 ], "fq": 50 
  },
  "raped": {
    "dict": "happiness", "word": "raped", "stem": "rape",
    "avg": [ 6.81, 1.64 ], "std": [ 3.17, 1.43 ], "fq": 50 
  },
  "torture": {
    "dict": "happiness", "word": "torture", "stem": "tortur",
    "avg": [ 6.10, 1.58 ], "std": [ 2.77, 1.05 ], "fq": 50 
  },
  "kill": {
    "dict": "happiness", "word": "kill", "stem": "kill",
    "avg": [ 5.09, 1.56 ], "std": [ 3.00, 1.05 ], "fq": 50 
  },
  "killed": {
    "dict": "happiness", "word": "killed", "stem": "kill",
    "avg": [ 5.09, 1.56 ], "std": [ 3.00, 1.23 ], "fq": 50 
  },
  "cancer": {
    "dict": "happiness", "word": "cancer", "stem": "cancer",
    "avg": [ 6.42, 1.54 ], "std": [ 2.83, 1.07 ], "fq": 50 
  },
  "death": {
    "dict": "happiness", "word": "death", "stem": "death",
    "avg": [ 4.59, 1.54 ], "std": [ 3.07, 1.28 ], "fq": 50 
  },
  "murder": {
    "dict": "happiness", "word": "murder", "stem": "murder",
    "avg": [ 7.47, 1.48 ], "std": [ 2.18, 1.01 ], "fq": 50 
  },
  "rape": {
    "dict": "happiness", "word": "rape", "stem": "rape",
    "avg": [ 6.81, 1.44 ], "std": [ 3.17, 0.79 ], "fq": 50 
  },
  "suicide": {
    "dict": "happiness", "word": "suicide", "stem": "suicid",
    "avg": [ 5.73, 1.30 ], "std": [ 3.14, 0.84 ], "fq": 50 
  },
  "terrorist": {
    "dict": "happiness", "word": "terrorist", "stem": "terrorist",
    "avg": [ 7.27, 1.30 ], "std": [ 2.38, 0.91 ], "fq": 50 
  },
}
