#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Personae
personae = [
    {'name': 'Orpheus', 'level': 1, 'arcana': 'Fool', 'special': True},
    {'name': 'Slime', 'level': 12, 'arcana': 'Fool'},
    {'name': 'Legion', 'level': 22, 'arcana': 'Fool'},
     {'name': 'Black Frost',     'level': 34, 'arcana': 'Fool', 'special': True},
    {'name': 'Ose',             'level': 44, 'arcana': 'Fool'},
    {'name': 'Decarabia',       'level': 50, 'arcana': 'Fool'},
    {'name': 'Loki',            'level': 58, 'arcana': 'Fool'},
    {'name': 'Susano-o',        'level': 76, 'arcana': 'Fool', 'max': True, 'special': True},
    {'name': 'Orpheus Telos',   'level': 90, 'arcana': 'Fool', 'special': True},
    {'name': 'Nekomata',        'level':  5, 'arcana': 'Magician'},
    {'name': 'Jack Frost',      'level':  8, 'arcana': 'Magician'},
    {'name': 'Pyro Jack',       'level': 14, 'arcana': 'Magician'},
    {'name': 'Hua Po',          'level': 20, 'arcana': 'Magician', 'item': True},
    {'name': 'Sati',            'level': 28, 'arcana': 'Magician'},
    {'name': 'Orobas',          'level': 34, 'arcana': 'Magician'},
    {'name': 'Rangda',          'level': 40, 'arcana': 'Magician'},
    {'name': 'Surt',            'level': 52, 'arcana': 'Magician', 'max': True},
    {'name': 'Apsaras',         'level':  3, 'arcana': 'Priestess'},
    {'name': 'Unicorn',         'level': 11, 'arcana': 'Priestess'},
    {'name': 'High Pixie',      'level': 21, 'arcana': 'Priestess'},
    {'name': 'Sarasvati',       'level': 27, 'arcana': 'Priestess'},
    {'name': 'Ganga',           'level': 35, 'arcana': 'Priestess'},
    {'name': 'Parvati',         'level': 47, 'arcana': 'Priestess'},
    {'name': 'Kikuri-hime',     'level': 53, 'arcana': 'Priestess'},
    {'name': 'Scathach',        'level': 64, 'arcana': 'Priestess', 'max': True},
    {'name': 'Leanan Sidhe',    'level': 33, 'arcana': 'Empress'},
    {'name': 'Yaksini',         'level': 50, 'arcana': 'Empress'},
    {'name': 'Laksmi',          'level': 57, 'arcana': 'Empress'},
    {'name': 'Hariti',          'level': 62, 'arcana': 'Empress'},
    {'name': 'Gabriel',         'level': 69, 'arcana': 'Empress'},
    {'name': 'Mother Harlot',   'level': 74, 'arcana': 'Empress'},
    {'name': 'Skadi',           'level': 80, 'arcana': 'Empress'},
    {'name': 'Alilat',          'level': 84, 'arcana': 'Empress', 'max': True},
    {'name': 'Forneus',         'level':  7, 'arcana': 'Emperor'},
    {'name': 'Oberon',          'level': 15, 'arcana': 'Emperor'},
    {'name': 'Take-mikazuchi',  'level': 24, 'arcana': 'Emperor'},
    {'name': 'King Frost',      'level': 30, 'arcana': 'Emperor', 'item': True},
    {'name': 'Raja Naga',       'level': 36, 'arcana': 'Emperor'},
    {'name': 'Kingu',           'level': 46, 'arcana': 'Emperor'},
    {'name': 'Barong',          'level': 52, 'arcana': 'Emperor'},
    {'name': 'Odin',            'level': 57, 'arcana': 'Emperor', 'max': True},
    {'name': 'Omoikane',        'level':  7, 'arcana': 'Hierophant'},
    {'name': 'Berith',          'level': 13, 'arcana': 'Hierophant'},
    {'name': 'Shiisaa',         'level': 26, 'arcana': 'Hierophant'},
    {'name': 'Flauros',         'level': 33, 'arcana': 'Hierophant'},
    {'name': 'Thoth',           'level': 41, 'arcana': 'Hierophant', 'item': True},
    {'name': 'Hokuto Seikun',   'level': 47, 'arcana': 'Hierophant'},
    {'name': 'Daisoujou',       'level': 53, 'arcana': 'Hierophant', 'special': True},
    {'name': 'Kohryu',          'level': 66, 'arcana': 'Hierophant', 'max': True, 'special': True},
    {'name': 'Pixie',           'level':  2, 'arcana': 'Lovers'},
    {'name': 'Alp',             'level':  6, 'arcana': 'Lovers'},
    {'name': 'Narcissus',       'level': 20, 'arcana': 'Lovers'},
    {'name': 'Queen Mab',       'level': 27, 'arcana': 'Lovers'},
    {'name': 'Saki Mitama',     'level': 39, 'arcana': 'Lovers'},
    {'name': 'Titania',         'level': 48, 'arcana': 'Lovers'},
    {'name': 'Raphael',         'level': 61, 'arcana': 'Lovers'},
    {'name': 'Cybele',          'level': 68, 'arcana': 'Lovers', 'max': True},
    {'name': 'Ara Mitama',      'level':  6, 'arcana': 'Chariot'},
    {'name': 'Chimera',         'level':  9, 'arcana': 'Chariot'},
    {'name': 'Zouchouten',      'level': 14, 'arcana': 'Chariot'},
    {'name': 'Ares',            'level': 19, 'arcana': 'Chariot'},
    {'name': 'Oumitsunu',       'level': 30, 'arcana': 'Chariot'},
    {'name': 'Nata Taishi',     'level': 37, 'arcana': 'Chariot', 'item': True},
    {'name': 'Koumokuten',      'level': 43, 'arcana': 'Chariot'},
    {'name': 'Thor',            'level': 53, 'arcana': 'Chariot', 'max': True},
    {'name': 'Angel',           'level':  4, 'arcana': 'Justice'},
    {'name': 'Archangel',       'level': 10, 'arcana': 'Justice'},
    {'name': 'Principality',    'level': 16, 'arcana': 'Justice'},
    {'name': 'Power',           'level': 25, 'arcana': 'Justice'},
    {'name': 'Virtue',          'level': 32, 'arcana': 'Justice'},
    {'name': 'Dominion',        'level': 42, 'arcana': 'Justice'},
    {'name': 'Throne',          'level': 51, 'arcana': 'Justice'},
    {'name': 'Melchizedek',     'level': 59, 'arcana': 'Justice', 'max': True},
    {'name': 'Yomotsu Shikome', 'level':  9, 'arcana': 'Hermit'},
    {'name': 'Naga',            'level': 17, 'arcana': 'Hermit'},
    {'name': 'Lamia',           'level': 25, 'arcana': 'Hermit'},
    {'name': 'Mothman',         'level': 32, 'arcana': 'Hermit'},
    {'name': 'Taraka',          'level': 38, 'arcana': 'Hermit'},
    {'name': 'Kurama Tengu',    'level': 44, 'arcana': 'Hermit'},
    {'name': 'Nebiros',         'level': 50, 'arcana': 'Hermit', 'item': True},
    {'name': 'Kumbhanda',       'level': 56, 'arcana': 'Hermit'},
    {'name': 'Arahabaki',       'level': 60, 'arcana': 'Hermit', 'max': True, 'special': True},
    {'name': 'Fortuna',         'level': 17, 'arcana': 'Fortune'},
    {'name': 'Empusa',          'level': 23, 'arcana': 'Fortune', 'item': True},
    {'name': 'Kusi Mitama',     'level': 29, 'arcana': 'Fortune'},
    {'name': 'Clotho',          'level': 38, 'arcana': 'Fortune'},
    {'name': 'Lachesis',        'level': 45, 'arcana': 'Fortune'},
    {'name': 'Atropos',         'level': 54, 'arcana': 'Fortune'},
    {'name': 'Norn',            'level': 62, 'arcana': 'Fortune', 'max': True, 'special': True},
    {'name': 'Valkyrie',        'level': 11, 'arcana': 'Strength'},
    {'name': 'Rakshasa',        'level': 16, 'arcana': 'Strength'},
    {'name': 'Titan',           'level': 23, 'arcana': 'Strength'},
    {'name': 'Jikokuten',       'level': 29, 'arcana': 'Strength'},
    {'name': 'Hanuman',         'level': 37, 'arcana': 'Strength'},
    {'name': 'Narasimha',       'level': 46, 'arcana': 'Strength'},
    {'name': 'Kali',            'level': 55, 'arcana': 'Strength'},
    {'name': 'Siegfried',       'level': 59, 'arcana': 'Strength', 'max': True},
    {'name': 'Inugami',         'level': 10, 'arcana': 'Hanged Man'},
    {'name': 'Take-minakata',   'level': 21, 'arcana': 'Hanged Man'},
    {'name': 'Orthrus',         'level': 28, 'arcana': 'Hanged Man'},
    {'name': 'Vasuki',          'level': 38, 'arcana': 'Hanged Man'},
    {'name': 'Ubelluris',       'level': 48, 'arcana': 'Hanged Man'},
    {'name': 'Hecatoncheires',  'level': 54, 'arcana': 'Hanged Man'},
    {'name': 'Hell Biker',      'level': 60, 'arcana': 'Hanged Man', 'item': True},
    {'name': 'Attis',           'level': 67, 'arcana': 'Hanged Man', 'max': True, 'special': True},
    {'name': 'Ghoul',           'level': 18, 'arcana': 'Death'},
    {'name': 'Pale Rider',      'level': 24, 'arcana': 'Death', 'item': True},
    {'name': 'Loa',             'level': 31, 'arcana': 'Death'},
    {'name': 'Samael',          'level': 37, 'arcana': 'Death'},
    {'name': 'Mot',             'level': 45, 'arcana': 'Death'},
    {'name': 'Alice',           'level': 56, 'arcana': 'Death', 'special': True},
    {'name': 'Thanatos',        'level': 64, 'arcana': 'Death', 'max': True, 'special': True},
    {'name': 'Nigi Mitama',     'level': 12, 'arcana': 'Temperance'},
    {'name': 'Mithra',          'level': 22, 'arcana': 'Temperance'},
    {'name': 'Genbu',           'level': 29, 'arcana': 'Temperance'},
    {'name': 'Seiryuu',         'level': 36, 'arcana': 'Temperance'},
    {'name': 'Okuninushi',      'level': 44, 'arcana': 'Temperance'},
    {'name': 'Suzaku',          'level': 51, 'arcana': 'Temperance'},
    {'name': 'Byakko',          'level': 57, 'arcana': 'Temperance'},
    {'name': 'Yurlungur',       'level': 64, 'arcana': 'Temperance', 'max': True},
    {'name': 'Lilim',           'level':  8, 'arcana': 'Devil'},
    {'name': 'Vetala',          'level': 24, 'arcana': 'Devil'},
    {'name': 'Incubus',         'level': 34, 'arcana': 'Devil'},
    {'name': 'Succubus',        'level': 43, 'arcana': 'Devil'},
    {'name': 'Pazuzu',          'level': 52, 'arcana': 'Devil'},
    {'name': 'Lilith',          'level': 61, 'arcana': 'Devil', 'item': True, 'special': True},
    {'name': 'Abaddon',         'level': 68, 'arcana': 'Devil'},
    {'name': 'Beelzebub',       'level': 81, 'arcana': 'Devil', 'max': True, 'special': True},
    {'name': 'Eligor',          'level': 31, 'arcana': 'Tower'},
    {'name': 'Cu Chulainn',     'level': 40, 'arcana': 'Tower'},
    {'name': 'Bishamonten',     'level': 60, 'arcana': 'Tower'},
    {'name': 'Seiten Taisei',   'level': 67, 'arcana': 'Tower'},
    {'name': 'Masakado',        'level': 73, 'arcana': 'Tower', 'item': True, 'special': True},
    {'name': 'Mara',            'level': 77, 'arcana': 'Tower', 'special': True},
    {'name': 'Shiva',           'level': 82, 'arcana': 'Tower', 'special': True},
    {'name': 'Chi You',         'level': 86, 'arcana': 'Tower', 'max': True},
    {'name': 'Nandi',           'level': 39, 'arcana': 'Star'},
    {'name': 'Kaiwan',          'level': 49, 'arcana': 'Star'},
    {'name': 'Ganesha',         'level': 58, 'arcana': 'Star'},
    {'name': 'Garuda',          'level': 65, 'arcana': 'Star'},
    {'name': 'Kartikeya',       'level': 70, 'arcana': 'Star', 'item': True},
    {'name': 'Saturnus',        'level': 78, 'arcana': 'Star'},
    {'name': 'Helel',           'level': 88, 'arcana': 'Star', 'max': True},
    {'name': 'Gurr',            'level': 15, 'arcana': 'Moon'},
    {'name': 'Yamatano-orochi', 'level': 26, 'arcana': 'Moon'},
    {'name': 'Girimehkala',     'level': 42, 'arcana': 'Moon', 'special': True},
    {'name': 'Dionysus',        'level': 48, 'arcana': 'Moon'},
    {'name': 'Chernobog',       'level': 58, 'arcana': 'Moon'},
    {'name': 'Seth',            'level': 66, 'arcana': 'Moon'},
    {'name': 'Baal Zebul',      'level': 71, 'arcana': 'Moon'},
    {'name': 'Sandalphon',      'level': 74, 'arcana': 'Moon', 'max': True, 'special': True},
    {'name': 'Yatagarasu',      'level': 30, 'arcana': 'Sun'},
    {'name': 'Quetzalcoatl',    'level': 43, 'arcana': 'Sun'},
    {'name': 'Jatayu',          'level': 55, 'arcana': 'Sun'},
    {'name': 'Horus',           'level': 63, 'arcana': 'Sun'},
    {'name': 'Suparna',         'level': 70, 'arcana': 'Sun'},
    {'name': 'Vishnu',          'level': 78, 'arcana': 'Sun'},
    {'name': 'Asura',           'level': 85, 'arcana': 'Sun', 'max': True, 'special': True},
    {'name': 'Anubis',          'level': 59, 'arcana': 'Judgment'},
    {'name': 'Trumpeter',       'level': 65, 'arcana': 'Judgment'},
    {'name': 'Michael',         'level': 72, 'arcana': 'Judgment'},
    {'name': 'Satan',           'level': 79, 'arcana': 'Judgment'},
    {'name': 'Lucifer',         'level': 89, 'arcana': 'Judgment', 'special': True},
    {'name': 'Messiah',         'level': 90, 'arcana': 'Judgment', 'max': True, 'special': True},
    {'name': 'Uriel',           'level': 63, 'arcana': 'Aeon'},
    {'name': 'Nidhoggr',        'level': 69, 'arcana': 'Aeon'},
    {'name': 'Ananta',          'level': 75, 'arcana': 'Aeon'},
    {'name': 'Atavaka',         'level': 80, 'arcana': 'Aeon'},
    {'name': 'Metatron',        'level': 87, 'arcana': 'Aeon', 'max': True, 'special': True},
]

# for each entry in 'personae' make the value in the key 'name' be lower

for persona in personae:
    # Update the 'name' value to be lower case
    persona['name'] = persona['name'].lower()


# Arcana 2 Combos
arcana2Combos = [
    {'source': ['Fool', 'Fool'], 'result': 'Fool'},
    {'source': ['Fool', 'Magician'], 'result': 'Hierophant'},
    {'source': ['Fool',       'Priestess'   ], 'result': 'Justice'     },
    {'source': ['Fool',       'Empress'     ], 'result': 'Fortune'     },
    {'source': ['Fool',       'Emperor'     ], 'result': 'Chariot'     },
    {'source': ['Fool',       'Hierophant'  ], 'result': 'Hermit'      },
    {'source': ['Fool',       'Lovers'      ], 'result': 'Priestess'   },
    {'source': ['Fool',       'Chariot'     ], 'result': 'Emperor'     },
    {'source': ['Fool',       'Justice'     ], 'result': 'Lovers'      },
    {'source': ['Fool',       'Hermit'      ], 'result': 'Priestess'   },
    {'source': ['Fool',       'Fortune'     ], 'result': 'Justice'     },
    {'source': ['Fool',       'Strength'    ], 'result': 'Hanged Man'  },
    {'source': ['Fool',       'Hanged Man'  ], 'result': 'Magician'    },
    {'source': ['Fool',       'Death'       ], 'result': 'Strength'    },
    {'source': ['Fool',       'Temperance'  ], 'result': 'Hierophant'  },
    {'source': ['Fool',       'Devil'       ], 'result': 'Hermit'      },
    {'source': ['Fool',       'Tower'       ], 'result': 'Moon'        },
    {'source': ['Fool',       'Star'        ], 'result': 'Aeon'        },
    {'source': ['Fool',       'Moon'        ], 'result': 'Fortune'     },
    {'source': ['Fool',       'Sun'         ], 'result': 'Empress'     },
    {'source': ['Fool',       'Judgment'    ], 'result': 'Star'        },
    {'source': ['Fool',       'Aeon'        ], 'result': 'Death'       },
    {'source': ['Magician',   'Magician'    ], 'result': 'Magician'    },
    {'source': ['Magician',   'Priestess'   ], 'result': 'Lovers'      },
    {'source': ['Magician',   'Empress'     ], 'result': 'Hanged Man'  },
    {'source': ['Magician',   'Emperor'     ], 'result': 'Temperance'  },
    {'source': ['Magician',   'Hierophant'  ], 'result': 'Hermit'      },
    {'source': ['Magician',   'Lovers'      ], 'result': 'Emperor'     },
    {'source': ['Magician',   'Chariot'     ], 'result': 'Devil'       },
    {'source': ['Magician',   'Justice'     ], 'result': 'Hierophant'  },
    {'source': ['Magician',   'Hermit'      ], 'result': 'Chariot'     },
    {'source': ['Magician',   'Fortune'     ], 'result': 'Emperor'     },
    {'source': ['Magician',   'Hanged Man'  ], 'result': 'Devil'       },
    {'source': ['Magician',   'Temperance'  ], 'result': 'Death'       },
    {'source': ['Magician',   'Devil'       ], 'result': 'Temperance'  },
    {'source': ['Magician',   'Tower'       ], 'result': 'Empress'     },
    {'source': ['Magician',   'Star'        ], 'result': 'Empress'     },
    {'source': ['Magician',   'Moon'        ], 'result': 'Priestess'   },
    {'source': ['Magician',   'Sun'         ], 'result': 'Lovers'      },
    {'source': ['Priestess',  'Priestess'   ], 'result': 'Priestess'   },
    {'source': ['Priestess',  'Empress'     ], 'result': 'Lovers'      },
    {'source': ['Priestess',  'Emperor'     ], 'result': 'Justice'     },
    {'source': ['Priestess',  'Hierophant'  ], 'result': 'Chariot'     },
    {'source': ['Priestess',  'Lovers'      ], 'result': 'Magician'    },
    {'source': ['Priestess',  'Chariot'     ], 'result': 'Magician'    },
    {'source': ['Priestess',  'Justice'     ], 'result': 'Lovers'      },
    {'source': ['Priestess',  'Hermit'      ], 'result': 'Strength'    },
    {'source': ['Priestess',  'Fortune'     ], 'result': 'Magician'    },
    {'source': ['Priestess',  'Strength'    ], 'result': 'Hermit'      },
    {'source': ['Priestess',  'Hanged Man'  ], 'result': 'Strength'    },
    {'source': ['Priestess',  'Death'       ], 'result': 'Emperor'     },
    {'source': ['Priestess',  'Temperance'  ], 'result': 'Empress'     },
    {'source': ['Priestess',  'Star'        ], 'result': 'Justice'     },
    {'source': ['Priestess',  'Moon'        ], 'result': 'Star'        },
    {'source': ['Priestess',  'Sun'         ], 'result': 'Star'        },
    {'source': ['Priestess',  'Judgment'    ], 'result': 'Empress'     },
    {'source': ['Priestess',  'Aeon'        ], 'result': 'Empress'     },
    {'source': ['Empress',    'Empress'     ], 'result': 'Empress'     },
    {'source': ['Empress',    'Emperor'     ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Hierophant'  ], 'result': 'Priestess'   },
    {'source': ['Empress',    'Lovers'      ], 'result': 'Fortune'     },
    {'source': ['Empress',    'Chariot'     ], 'result': 'Devil'       },
    {'source': ['Empress',    'Justice'     ], 'result': 'Emperor'     },
    {'source': ['Empress',    'Hermit'      ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Fortune'     ], 'result': 'Strength'    },
    {'source': ['Empress',    'Strength'    ], 'result': 'Chariot'     },
    {'source': ['Empress',    'Hanged Man'  ], 'result': 'Chariot'     },
    {'source': ['Empress',    'Death'       ], 'result': 'Devil'       },
    {'source': ['Empress',    'Temperance'  ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Devil'       ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Tower'       ], 'result': 'Chariot'     },
    {'source': ['Empress',    'Star'        ], 'result': 'Temperance'  },
    {'source': ['Empress',    'Moon'        ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Sun'         ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Aeon'        ], 'result': 'Moon'        },
    {'source': ['Emperor',    'Emperor'     ], 'result': 'Emperor'     },
    {'source': ['Emperor',    'Hierophant'  ], 'result': 'Chariot'     },
    {'source': ['Emperor',    'Lovers'      ], 'result': 'Chariot'     },
    {'source': ['Emperor',    'Chariot'     ], 'result': 'Hermit'      },
    {'source': ['Emperor',    'Justice'     ], 'result': 'Devil'       },
    {'source': ['Emperor',    'Hermit'      ], 'result': 'Strength'    },
    {'source': ['Emperor',    'Strength'    ], 'result': 'Hanged Man'  },
    {'source': ['Emperor',    'Hanged Man'  ], 'result': 'Hermit'      },
    {'source': ['Emperor',    'Death'       ], 'result': 'Moon'        },
    {'source': ['Emperor',    'Temperance'  ], 'result': 'Hanged Man'  },
    {'source': ['Emperor',    'Star'        ], 'result': 'Justice'     },
    {'source': ['Emperor',    'Sun'         ], 'result': 'Empress'     },
    {'source': ['Emperor',    'Judgment'    ], 'result': 'Hierophant'  },
    {'source': ['Hierophant', 'Hierophant'  ], 'result': 'Hierophant'  },
    {'source': ['Hierophant', 'Lovers'      ], 'result': 'Magician'    },
    {'source': ['Hierophant', 'Chariot'     ], 'result': 'Justice'     },
    {'source': ['Hierophant', 'Justice'     ], 'result': 'Chariot'     },
    {'source': ['Hierophant', 'Hermit'      ], 'result': 'Chariot'     },
    {'source': ['Hierophant', 'Fortune'     ], 'result': 'Emperor'     },
    {'source': ['Hierophant', 'Strength'    ], 'result': 'Priestess'   },
    {'source': ['Hierophant', 'Hanged Man'  ], 'result': 'Lovers'      },
    {'source': ['Hierophant', 'Death'       ], 'result': 'Empress'     },
    {'source': ['Hierophant', 'Temperance'  ], 'result': 'Strength'    },
    {'source': ['Hierophant', 'Tower'       ], 'result': 'Temperance'  },
    {'source': ['Hierophant', 'Star'        ], 'result': 'Priestess'   },
    {'source': ['Hierophant', 'Moon'        ], 'result': 'Temperance'  },
    {'source': ['Hierophant', 'Sun'         ], 'result': 'Temperance'  },
    {'source': ['Hierophant', 'Judgment'    ], 'result': 'Lovers'      },
    {'source': ['Lovers',     'Lovers'      ], 'result': 'Lovers'      },
    {'source': ['Lovers',     'Chariot'     ], 'result': 'Emperor'     },
    {'source': ['Lovers',     'Justice'     ], 'result': 'Chariot'     },
    {'source': ['Lovers',     'Hermit'      ], 'result': 'Justice'     },
    {'source': ['Lovers',     'Fortune'     ], 'result': 'Magician'    },
    {'source': ['Lovers',     'Strength'    ], 'result': 'Hierophant'  },
    {'source': ['Lovers',     'Hanged Man'  ], 'result': 'Hermit'      },
    {'source': ['Lovers',     'Death'       ], 'result': 'Devil'       },
    {'source': ['Lovers',     'Temperance'  ], 'result': 'Priestess'   },
    {'source': ['Lovers',     'Devil'       ], 'result': 'Strength'    },
    {'source': ['Lovers',     'Tower'       ], 'result': 'Star'        },
    {'source': ['Lovers',     'Star'        ], 'result': 'Hierophant'  },
    {'source': ['Lovers',     'Moon'        ], 'result': 'Empress'     },
    {'source': ['Lovers',     'Sun'         ], 'result': 'Hierophant'  },
    {'source': ['Lovers',     'Aeon'        ], 'result': 'Hanged Man'  },
    {'source': ['Chariot',    'Chariot'     ], 'result': 'Chariot'     },
    {'source': ['Chariot',    'Justice'     ], 'result': 'Magician'    },
    {'source': ['Chariot',    'Hermit'      ], 'result': 'Temperance'  },
    {'source': ['Chariot',    'Fortune'     ], 'result': 'Strength'    },
    {'source': ['Chariot',    'Strength'    ], 'result': 'Justice'     },
    {'source': ['Chariot',    'Hanged Man'  ], 'result': 'Fortune'     },
    {'source': ['Chariot',    'Temperance'  ], 'result': 'Death'       },
    {'source': ['Chariot',    'Devil'       ], 'result': 'Hanged Man'  },
    {'source': ['Chariot',    'Tower'       ], 'result': 'Moon'        },
    {'source': ['Chariot',    'Moon'        ], 'result': 'Fortune'     },
    {'source': ['Chariot',    'Aeon'        ], 'result': 'Death'       },
    {'source': ['Justice',    'Justice'     ], 'result': 'Justice'     },
    {'source': ['Justice',    'Hermit'      ], 'result': 'Priestess'   },
    {'source': ['Justice',    'Fortune'     ], 'result': 'Chariot'     },
    {'source': ['Justice',    'Strength'    ], 'result': 'Temperance'  },
    {'source': ['Justice',    'Hanged Man'  ], 'result': 'Priestess'   },
    {'source': ['Justice',    'Death'       ], 'result': 'Moon'        },
    {'source': ['Justice',    'Temperance'  ], 'result': 'Moon'        },
    {'source': ['Justice',    'Tower'       ], 'result': 'Star'        },
    {'source': ['Justice',    'Star'        ], 'result': 'Emperor'     },
    {'source': ['Justice',    'Sun'         ], 'result': 'Emperor'     },
    {'source': ['Justice',    'Judgment'    ], 'result': 'Aeon'        },
    {'source': ['Hermit',     'Hermit'      ], 'result': 'Hermit'      },
    {'source': ['Hermit',     'Fortune'     ], 'result': 'Emperor'     },
    {'source': ['Hermit',     'Strength'    ], 'result': 'Fortune'     },
    {'source': ['Hermit',     'Hanged Man'  ], 'result': 'Fortune'     },
    {'source': ['Hermit',     'Temperance'  ], 'result': 'Hanged Man'  },
    {'source': ['Hermit',     'Devil'       ], 'result': 'Death'       },
    {'source': ['Hermit',     'Star'        ], 'result': 'Chariot'     },
    {'source': ['Hermit',     'Moon'        ], 'result': 'Magician'    },
    {'source': ['Hermit',     'Aeon'        ], 'result': 'Star'        },
    {'source': ['Fortune',    'Fortune'     ], 'result': 'Fortune'     },
    {'source': ['Fortune',    'Hanged Man'  ], 'result': 'Strength'    },
    {'source': ['Fortune',    'Temperance'  ], 'result': 'Lovers'      },
    {'source': ['Fortune',    'Devil'       ], 'result': 'Moon'        },
    {'source': ['Fortune',    'Tower'       ], 'result': 'Moon'        },
    {'source': ['Fortune',    'Star'        ], 'result': 'Moon'        },
    {'source': ['Fortune',    'Moon'        ], 'result': 'Chariot'     },
    {'source': ['Fortune',    'Sun'         ], 'result': 'Temperance'  },
    {'source': ['Fortune',    'Aeon'        ], 'result': 'Devil'       },
    {'source': ['Strength',   'Strength'    ], 'result': 'Strength'    },
    {'source': ['Strength',   'Hanged Man'  ], 'result': 'Hermit'      },
    {'source': ['Strength',   'Death'       ], 'result': 'Hanged Man'  },
    {'source': ['Strength',   'Temperance'  ], 'result': 'Moon'        },
    {'source': ['Strength',   'Devil'       ], 'result': 'Fortune'     },
    {'source': ['Strength',   'Tower'       ], 'result': 'Devil'       },
    {'source': ['Strength',   'Star'        ], 'result': 'Priestess'   },
    {'source': ['Strength',   'Moon'        ], 'result': 'Hanged Man'  },
    {'source': ['Strength',   'Sun'         ], 'result': 'Priestess'   },
    {'source': ['Strength',   'Judgment'    ], 'result': 'Hanged Man'  },
    {'source': ['Hanged Man', 'Hanged Man'  ], 'result': 'Hanged Man'  },
    {'source': ['Hanged Man', 'Death'       ], 'result': 'Devil'       },
    {'source': ['Hanged Man', 'Temperance'  ], 'result': 'Hierophant'  },
    {'source': ['Hanged Man', 'Devil'       ], 'result': 'Moon'        },
    {'source': ['Hanged Man', 'Tower'       ], 'result': 'Death'       },
    {'source': ['Hanged Man', 'Star'        ], 'result': 'Strength'    },
    {'source': ['Hanged Man', 'Moon'        ], 'result': 'Empress'     },
    {'source': ['Hanged Man', 'Aeon'        ], 'result': 'Temperance'  },
    {'source': ['Death',      'Death'       ], 'result': 'Death'       },
    {'source': ['Death',      'Moon'        ], 'result': 'Star'        },
    {'source': ['Temperance', 'Temperance'  ], 'result': 'Temperance'  },
    {'source': ['Temperance', 'Devil'       ], 'result': 'Death'       },
    {'source': ['Temperance', 'Tower'       ], 'result': 'Devil'       },
    {'source': ['Temperance', 'Star'        ], 'result': 'Moon'        },
    {'source': ['Temperance', 'Moon'        ], 'result': 'Empress'     },
    {'source': ['Temperance', 'Sun'         ], 'result': 'Star'        },
    {'source': ['Temperance', 'Judgment'    ], 'result': 'Moon'        },
    {'source': ['Temperance', 'Aeon'        ], 'result': 'Star'        },
    {'source': ['Devil',      'Devil'       ], 'result': 'Devil'       },
    {'source': ['Devil',      'Aeon'        ], 'result': 'Lovers'      },
    {'source': ['Tower',      'Tower'       ], 'result': 'Tower'       },
    {'source': ['Tower',      'Moon'        ], 'result': 'Fortune'     },
    {'source': ['Tower',      'Judgment'    ], 'result': 'Aeon'        },
    {'source': ['Tower',      'Aeon'        ], 'result': 'Moon'        },
    {'source': ['Star',       'Star'        ], 'result': 'Star'        },
    {'source': ['Star',       'Moon'        ], 'result': 'Death'       },
    {'source': ['Star',       'Sun'         ], 'result': 'Justice'     },
    {'source': ['Star',       'Judgment'    ], 'result': 'Temperance'  },
    {'source': ['Star',       'Aeon'        ], 'result': 'Devil'       },
    {'source': ['Moon',       'Moon'        ], 'result': 'Moon'        },
    {'source': ['Moon',       'Sun'         ], 'result': 'Temperance'  },
    {'source': ['Sun',        'Sun'         ], 'result': 'Sun'         },
    {'source': ['Sun',        'Judgment'    ], 'result': 'Star'        },
    {'source': ['Sun',        'Aeon'        ], 'result': 'Empress'     },
    {'source': ['Judgment',   'Judgment'    ], 'result': 'Judgment'    },
    {'source': ['Judgment',   'Aeon'        ], 'result': 'Star'        },
    {'source': ['Aeon',       'Aeon'        ], 'result': 'Aeon'        },
]

# Arcana 3 Combos
arcana3Combos = [
    {'source': ['Fool', 'Fool'], 'result': 'Fool'},
    {'source': ['Fool', 'Magician'], 'result': 'Emperor'},
    {'source': ['Fool',       'Priestess'   ], 'result': 'Magician'    },
    {'source': ['Fool',       'Empress'     ], 'result': 'Fortune'     },
    {'source': ['Fool',       'Emperor'     ], 'result': 'Lovers'      },
    {'source': ['Fool',       'Hierophant'  ], 'result': 'Hermit'      },
    {'source': ['Fool',       'Lovers'      ], 'result': 'Temperance'  },
    {'source': ['Fool',       'Chariot'     ], 'result': 'Devil'       },
    {'source': ['Fool',       'Justice'     ], 'result': 'Chariot'     },
    {'source': ['Fool',       'Hermit'      ], 'result': 'Priestess'   },
    {'source': ['Fool',       'Fortune'     ], 'result': 'Justice'     },
    {'source': ['Fool',       'Strength'    ], 'result': 'Hanged Man'  },
    {'source': ['Fool',       'Hanged Man'  ], 'result': 'Magician'    },
    {'source': ['Fool',       'Death'       ], 'result': 'Strength'    },
    {'source': ['Fool',       'Temperance'  ], 'result': 'Hierophant'  },
    {'source': ['Fool',       'Devil'       ], 'result': 'Justice'     },
    {'source': ['Fool',       'Tower'       ], 'result': 'Moon'        },
    {'source': ['Fool',       'Star'        ], 'result': 'Aeon'        },
    {'source': ['Fool',       'Moon'        ], 'result': 'Fortune'     },
    {'source': ['Fool',       'Sun'         ], 'result': 'Empress'     },
    {'source': ['Fool',       'Judgment'    ], 'result': 'Star'        },
    {'source': ['Fool',       'Aeon'        ], 'result': 'Death'       },
    {'source': ['Magician',   'Magician'    ], 'result': 'Magician'    },
    {'source': ['Magician',   'Priestess'   ], 'result': 'Devil'       },
    {'source': ['Magician',   'Empress'     ], 'result': 'Hanged Man'  },
    {'source': ['Magician',   'Emperor'     ], 'result': 'Lovers'      },
    {'source': ['Magician',   'Hierophant'  ], 'result': 'Hermit'      },
    {'source': ['Magician',   'Lovers'      ], 'result': 'Devil'       },
    {'source': ['Magician',   'Chariot'     ], 'result': 'Moon'        },
    {'source': ['Magician',   'Justice'     ], 'result': 'Fool'        },
    {'source': ['Magician',   'Hermit'      ], 'result': 'Hanged Man'  },
    {'source': ['Magician',   'Fortune'     ], 'result': 'Emperor'     },
    {'source': ['Magician',   'Strength'    ], 'result': 'Star'        },
    {'source': ['Magician',   'Hanged Man'  ], 'result': 'Devil'       },
    {'source': ['Magician',   'Death'       ], 'result': 'Tower'       },
    {'source': ['Magician',   'Temperance'  ], 'result': 'Death'       },
    {'source': ['Magician',   'Devil'       ], 'result': 'Temperance'  },
    {'source': ['Magician',   'Tower'       ], 'result': 'Empress'     },
    {'source': ['Magician',   'Star'        ], 'result': 'Empress'     },
    {'source': ['Magician',   'Moon'        ], 'result': 'Fortune'     },
    {'source': ['Magician',   'Sun'         ], 'result': 'Lovers'      },
    {'source': ['Magician',   'Judgment'    ], 'result': 'Tower'       },
    {'source': ['Magician',   'Aeon'        ], 'result': 'Sun'         },
    {'source': ['Priestess',  'Priestess'   ], 'result': 'Priestess'   },
    {'source': ['Priestess',  'Empress'     ], 'result': 'Lovers'      },
    {'source': ['Priestess',  'Emperor'     ], 'result': 'Hierophant'  },
    {'source': ['Priestess',  'Hierophant'  ], 'result': 'Chariot'     },
    {'source': ['Priestess',  'Lovers'      ], 'result': 'Hermit'      },
    {'source': ['Priestess',  'Chariot'     ], 'result': 'Emperor'     },
    {'source': ['Priestess',  'Justice'     ], 'result': 'Hierophant'  },
    {'source': ['Priestess',  'Hermit'      ], 'result': 'Fool'        },
    {'source': ['Priestess',  'Fortune'     ], 'result': 'Magician'    },
    {'source': ['Priestess',  'Strength'    ], 'result': 'Chariot'     },
    {'source': ['Priestess',  'Hanged Man'  ], 'result': 'Strength'    },
    {'source': ['Priestess',  'Death'       ], 'result': 'Emperor'     },
    {'source': ['Priestess',  'Temperance'  ], 'result': 'Empress'     },
    {'source': ['Priestess',  'Devil'       ], 'result': 'Tower'       },
    {'source': ['Priestess',  'Tower'       ], 'result': 'Death'       },
    {'source': ['Priestess',  'Star'        ], 'result': 'Justice'     },
    {'source': ['Priestess',  'Moon'        ], 'result': 'Star'        },
    {'source': ['Priestess',  'Sun'         ], 'result': 'Star'        },
    {'source': ['Priestess',  'Judgment'    ], 'result': 'Justice'     },
    {'source': ['Priestess',  'Aeon'        ], 'result': 'Empress'     },
    {'source': ['Empress',    'Empress'     ], 'result': 'Empress'     },
    {'source': ['Empress',    'Emperor'     ], 'result': 'Fool'        },
    {'source': ['Empress',    'Hierophant'  ], 'result': 'Priestess'   },
    {'source': ['Empress',    'Lovers'      ], 'result': 'Fortune'     },
    {'source': ['Empress',    'Chariot'     ], 'result': 'Devil'       },
    {'source': ['Empress',    'Justice'     ], 'result': 'Emperor'     },
    {'source': ['Empress',    'Hermit'      ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Fortune'     ], 'result': 'Strength'    },
    {'source': ['Empress',    'Strength'    ], 'result': 'Chariot'     },
    {'source': ['Empress',    'Hanged Man'  ], 'result': 'Chariot'     },
    {'source': ['Empress',    'Death'       ], 'result': 'Devil'       },
    {'source': ['Empress',    'Temperance'  ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Devil'       ], 'result': 'Magician'    },
    {'source': ['Empress',    'Tower'       ], 'result': 'Chariot'     },
    {'source': ['Empress',    'Star'        ], 'result': 'Temperance'  },
    {'source': ['Empress',    'Moon'        ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Sun'         ], 'result': 'Lovers'      },
    {'source': ['Empress',    'Judgment'    ], 'result': 'Devil'       },
    {'source': ['Empress',    'Aeon'        ], 'result': 'Moon'        },
    {'source': ['Emperor',    'Emperor'     ], 'result': 'Emperor'     },
    {'source': ['Emperor',    'Hierophant'  ], 'result': 'Chariot'     },
    {'source': ['Emperor',    'Lovers'      ], 'result': 'Strength'    },
    {'source': ['Emperor',    'Chariot'     ], 'result': 'Justice'     },
    {'source': ['Emperor',    'Justice'     ], 'result': 'Chariot'     },
    {'source': ['Emperor',    'Hermit'      ], 'result': 'Lovers'      },
    {'source': ['Emperor',    'Fortune'     ], 'result': 'Sun'         },
    {'source': ['Emperor',    'Strength'    ], 'result': 'Hanged Man'  },
    {'source': ['Emperor',    'Hanged Man'  ], 'result': 'Temperance'  },
    {'source': ['Emperor',    'Death'       ], 'result': 'Moon'        },
    {'source': ['Emperor',    'Temperance'  ], 'result': 'Hanged Man'  },
    {'source': ['Emperor',    'Devil'       ], 'result': 'Tower'       },
    {'source': ['Emperor',    'Tower'       ], 'result': 'Death'       },
    {'source': ['Emperor',    'Star'        ], 'result': 'Hermit'      },
    {'source': ['Emperor',    'Moon'        ], 'result': 'Tower'       },
    {'source': ['Emperor',    'Sun'         ], 'result': 'Empress'     },
    {'source': ['Emperor',    'Judgment'    ], 'result': 'Hierophant'  },
    {'source': ['Emperor',    'Aeon'        ], 'result': 'Sun'         },
    {'source': ['Hierophant', 'Hierophant'  ], 'result': 'Hierophant'  },
    {'source': ['Hierophant', 'Lovers'      ], 'result': 'Temperance'  },
    {'source': ['Hierophant', 'Chariot'     ], 'result': 'Sun'         },
    {'source': ['Hierophant', 'Justice'     ], 'result': 'Magician'    },
    {'source': ['Hierophant', 'Hermit'      ], 'result': 'Chariot'     },
    {'source': ['Hierophant', 'Fortune'     ], 'result': 'Emperor'     },
    {'source': ['Hierophant', 'Strength'    ], 'result': 'Emperor'     },
    {'source': ['Hierophant', 'Hanged Man'  ], 'result': 'Fortune'     },
    {'source': ['Hierophant', 'Death'       ], 'result': 'Empress'     },
    {'source': ['Hierophant', 'Temperance'  ], 'result': 'Strength'    },
    {'source': ['Hierophant', 'Devil'       ], 'result': 'Fool'        },
    {'source': ['Hierophant', 'Tower'       ], 'result': 'Temperance'  },
    {'source': ['Hierophant', 'Star'        ], 'result': 'Priestess'   },
    {'source': ['Hierophant', 'Moon'        ], 'result': 'Temperance'  },
    {'source': ['Hierophant', 'Sun'         ], 'result': 'Temperance'  },
    {'source': ['Hierophant', 'Judgment'    ], 'result': 'Lovers'      },
    {'source': ['Hierophant', 'Aeon'        ], 'result': 'Tower'       },
    {'source': ['Lovers',     'Lovers'      ], 'result': 'Lovers'      },
    {'source': ['Lovers',     'Chariot'     ], 'result': 'Strength'    },
    {'source': ['Lovers',     'Justice'     ], 'result': 'Hanged Man'  },
    {'source': ['Lovers',     'Hermit'      ], 'result': 'Hierophant'  },
    {'source': ['Lovers',     'Fortune'     ], 'result': 'Fool'        },
    {'source': ['Lovers',     'Strength'    ], 'result': 'Hierophant'  },
    {'source': ['Lovers',     'Hanged Man'  ], 'result': 'Hermit'      },
    {'source': ['Lovers',     'Death'       ], 'result': 'Devil'       },
    {'source': ['Lovers',     'Temperance'  ], 'result': 'Priestess'   },
    {'source': ['Lovers',     'Devil'       ], 'result': 'Death'       },
    {'source': ['Lovers',     'Tower'       ], 'result': 'Star'        },
    {'source': ['Lovers',     'Star'        ], 'result': 'Hierophant'  },
    {'source': ['Lovers',     'Moon'        ], 'result': 'Empress'     },
    {'source': ['Lovers',     'Sun'         ], 'result': 'Hierophant'  },
    {'source': ['Lovers',     'Judgment'    ], 'result': 'Sun'         },
    {'source': ['Lovers',     'Aeon'        ], 'result': 'Hanged Man'  },
    {'source': ['Chariot',    'Chariot'     ], 'result': 'Chariot'     },
    {'source': ['Chariot',    'Justice'     ], 'result': 'Magician'    },
    {'source': ['Chariot',    'Hermit'      ], 'result': 'Hanged Man'  },
    {'source': ['Chariot',    'Fortune'     ], 'result': 'Hermit'      },
    {'source': ['Chariot',    'Strength'    ], 'result': 'Justice'     },
    {'source': ['Chariot',    'Hanged Man'  ], 'result': 'Fortune'     },
    {'source': ['Chariot',    'Death'       ], 'result': 'Fool'        },
    {'source': ['Chariot',    'Temperance'  ], 'result': 'Death'       },
    {'source': ['Chariot',    'Devil'       ], 'result': 'Star'        },
    {'source': ['Chariot',    'Tower'       ], 'result': 'Moon'        },
    {'source': ['Chariot',    'Star'        ], 'result': 'Sun'         },
    {'source': ['Chariot',    'Moon'        ], 'result': 'Fortune'     },
    {'source': ['Chariot',    'Sun'         ], 'result': 'Justice'     },
    {'source': ['Chariot',    'Judgment'    ], 'result': 'Tower'       },
    {'source': ['Chariot',    'Aeon'        ], 'result': 'Death'       },
    {'source': ['Justice',    'Justice'     ], 'result': 'Justice'     },
    {'source': ['Justice',    'Hermit'      ], 'result': 'Strength'    },
    {'source': ['Justice',    'Fortune'     ], 'result': 'Chariot'     },
    {'source': ['Justice',    'Strength'    ], 'result': 'Temperance'  },
    {'source': ['Justice',    'Hanged Man'  ], 'result': 'Priestess'   },
    {'source': ['Justice',    'Death'       ], 'result': 'Moon'        },
    {'source': ['Justice',    'Temperance'  ], 'result': 'Moon'        },
    {'source': ['Justice',    'Devil'       ], 'result': 'Tower'       },
    {'source': ['Justice',    'Tower'       ], 'result': 'Sun'         },
    {'source': ['Justice',    'Star'        ], 'result': 'Emperor'     },
    {'source': ['Justice',    'Moon'        ], 'result': 'Tower'       },
    {'source': ['Justice',    'Sun'         ], 'result': 'Emperor'     },
    {'source': ['Justice',    'Judgment'    ], 'result': 'Aeon'        },
    {'source': ['Justice',    'Aeon'        ], 'result': 'Judgment'    },
    {'source': ['Hermit',     'Hermit'      ], 'result': 'Hermit'      },
    {'source': ['Hermit',     'Fortune'     ], 'result': 'Emperor'     },
    {'source': ['Hermit',     'Strength'    ], 'result': 'Fortune'     },
    {'source': ['Hermit',     'Hanged Man'  ], 'result': 'Fortune'     },
    {'source': ['Hermit',     'Death'       ], 'result': 'Tower'       },
    {'source': ['Hermit',     'Temperance'  ], 'result': 'Hanged Man'  },
    {'source': ['Hermit',     'Devil'       ], 'result': 'Death'       },
    {'source': ['Hermit',     'Tower'       ], 'result': 'Death'       },
    {'source': ['Hermit',     'Star'        ], 'result': 'Chariot'     },
    {'source': ['Hermit',     'Moon'        ], 'result': 'Magician'    },
    {'source': ['Hermit',     'Sun'         ], 'result': 'Star'        },
    {'source': ['Hermit',     'Judgment'    ], 'result': 'Tower'       },
    {'source': ['Hermit',     'Aeon'        ], 'result': 'Star'        },
    {'source': ['Fortune',    'Fortune'     ], 'result': 'Fortune'     },
    {'source': ['Fortune',    'Strength'    ], 'result': 'Sun'         },
    {'source': ['Fortune',    'Hanged Man'  ], 'result': 'Strength'    },
    {'source': ['Fortune',    'Death'       ], 'result': 'Judgment'    },
    {'source': ['Fortune',    'Temperance'  ], 'result': 'Lovers'      },
    {'source': ['Fortune',    'Devil'       ], 'result': 'Hermit'      },
    {'source': ['Fortune',    'Tower'       ], 'result': 'Aeon'        },
    {'source': ['Fortune',    'Star'        ], 'result': 'Moon'        },
    {'source': ['Fortune',    'Moon'        ], 'result': 'Chariot'     },
    {'source': ['Fortune',    'Sun'         ], 'result': 'Temperance'  },
    {'source': ['Fortune',    'Judgment'    ], 'result': 'Star'        },
    {'source': ['Fortune',    'Aeon'        ], 'result': 'Devil'       },
    {'source': ['Strength',   'Hermit'      ], 'result': 'Emperor'     },
    {'source': ['Strength',   'Strength'    ], 'result': 'Strength'    },
    {'source': ['Strength',   'Hanged Man'  ], 'result': 'Fortune'     },
    {'source': ['Strength',   'Death'       ], 'result': 'Hanged Man'  },
    {'source': ['Strength',   'Temperance'  ], 'result': 'Moon'        },
    {'source': ['Strength',   'Devil'       ], 'result': 'Empress'     },
    {'source': ['Strength',   'Tower'       ], 'result': 'Judgment'    },
    {'source': ['Strength',   'Star'        ], 'result': 'Priestess'   },
    {'source': ['Strength',   'Moon'        ], 'result': 'Aeon'        },
    {'source': ['Strength',   'Sun'         ], 'result': 'Priestess'   },
    {'source': ['Strength',   'Judgment'    ], 'result': 'Hanged Man'  },
    {'source': ['Strength',   'Aeon'        ], 'result': 'Tower'       },
    {'source': ['Hanged Man', 'Hanged Man'  ], 'result': 'Hanged Man'  },
    {'source': ['Hanged Man', 'Death'       ], 'result': 'Devil'       },
    {'source': ['Hanged Man', 'Temperance'  ], 'result': 'Hierophant'  },
    {'source': ['Hanged Man', 'Devil'       ], 'result': 'Death'       },
    {'source': ['Hanged Man', 'Tower'       ], 'result': 'Death'       },
    {'source': ['Hanged Man', 'Star'        ], 'result': 'Strength'    },
    {'source': ['Hanged Man', 'Moon'        ], 'result': 'Empress'     },
    {'source': ['Hanged Man', 'Sun'         ], 'result': 'Judgment'    },
    {'source': ['Hanged Man', 'Judgment'    ], 'result': 'Aeon'        },
    {'source': ['Hanged Man', 'Aeon'        ], 'result': 'Temperance'  },
    {'source': ['Death',      'Chariot'     ], 'result': 'Fool'        },
    {'source': ['Death',      'Death'       ], 'result': 'Death'       },
    {'source': ['Death',      'Temperance'  ], 'result': 'Tower'       },
    {'source': ['Death',      'Devil'       ], 'result': 'Judgment'    },
    {'source': ['Death',      'Tower'       ], 'result': 'Sun'         },
    {'source': ['Death',      'Star'        ], 'result': 'Tower'       },
    {'source': ['Death',      'Moon'        ], 'result': 'Star'        },
    {'source': ['Death',      'Sun'         ], 'result': 'Moon'        },
    {'source': ['Death',      'Judgment'    ], 'result': 'Fool'        },
    {'source': ['Death',      'Aeon'        ], 'result': 'Sun'         },
    {'source': ['Temperance', 'Temperance'  ], 'result': 'Temperance'  },
    {'source': ['Temperance', 'Devil'       ], 'result': 'Moon'        },
    {'source': ['Temperance', 'Tower'       ], 'result': 'Devil'       },
    {'source': ['Temperance', 'Star'        ], 'result': 'Hermit'      },
    {'source': ['Temperance', 'Moon'        ], 'result': 'Empress'     },
    {'source': ['Temperance', 'Sun'         ], 'result': 'Judgment'    },
    {'source': ['Temperance', 'Judgment'    ], 'result': 'Justice'     },
    {'source': ['Temperance', 'Aeon'        ], 'result': 'Star'        },
    {'source': ['Devil',      'Devil'       ], 'result': 'Devil'       },
    {'source': ['Devil',      'Tower'       ], 'result': 'Judgment'    },
    {'source': ['Devil',      'Star'        ], 'result': 'Magician'    },
    {'source': ['Devil',      'Moon'        ], 'result': 'Judgment'    },
    {'source': ['Devil',      'Sun'         ], 'result': 'Death'       },
    {'source': ['Devil',      'Judgment'    ], 'result': 'Moon'        },
    {'source': ['Devil',      'Aeon'        ], 'result': 'Lovers'      },
    {'source': ['Tower',      'Tower'       ], 'result': 'Tower'       },
    {'source': ['Tower',      'Star'        ], 'result': 'Judgment'    },
    {'source': ['Tower',      'Moon'        ], 'result': 'Fortune'     },
    {'source': ['Tower',      'Sun'         ], 'result': 'Moon'        },
    {'source': ['Tower',      'Judgment'    ], 'result': 'Aeon'        },
    {'source': ['Tower',      'Aeon'        ], 'result': 'Fool'        },
    {'source': ['Star',       'Star'        ], 'result': 'Star'        },
    {'source': ['Star',       'Moon'        ], 'result': 'Sun'         },
    {'source': ['Star',       'Sun'         ], 'result': 'Aeon'        },
    {'source': ['Star',       'Judgment'    ], 'result': 'Temperance'  },
    {'source': ['Star',       'Aeon'        ], 'result': 'Devil'       },
    {'source': ['Moon',       'Moon'        ], 'result': 'Moon'        },
    {'source': ['Moon',       'Sun'         ], 'result': 'Temperance'  },
    {'source': ['Moon',       'Judgment'    ], 'result': 'Priestess'   },
    {'source': ['Moon',       'Aeon'        ], 'result': 'Judgment'    },
    {'source': ['Sun',        'Sun'         ], 'result': 'Sun'         },
    {'source': ['Sun',        'Judgment'    ], 'result': 'Star'        },
    {'source': ['Sun',        'Aeon'        ], 'result': 'Empress'     },
    {'source': ['Judgment',   'Judgment'    ], 'result': 'Judgment'    },
    {'source': ['Judgment',   'Aeon'        ], 'result': 'Fool'        },
    {'source': ['Aeon',       'Aeon'        ], 'result': 'Aeon'        },
]

# Special Combos
specialCombos = [
    {'result': 'Alice', 'sources': ['Pixie', 'Lilim', 'Narcissus', 'Nata Taishi']},
     {'result': 'Arahabaki', 'sources': ['Omoikane', 'Take-minakata', 'Okuninushi', 'Kikuri-hime']},
    {'result': 'Asura', 'sources': ['Yatagarasu', 'Quetzalcoatl', 'Jatayu', 'Horus', 'Suparna', 'Vishnu']},
    {'result': 'Attis', 'sources': ['Inugami', 'Take-minakata', 'Orthrus', 'Vasuki', 'Ubelluris']},
    {'result': 'Beelzebub', 'sources': ['Incubus', 'Succubus', 'Pazuzu', 'Lilith', 'Abaddon', 'Baal Zebul']},
    {'result': 'Black Frost', 'sources': ['Jack Frost', 'Pyro Jack', 'King Frost', 'Queen Mab']},
    {'result': 'Daisoujou', 'sources': ['Mithra', 'Ara Mitama', 'Nigi Mitama', 'Kusi Mitama', 'Saki Mitama']},
    {'result': 'Girimehkala', 'sources': ['Gurr', 'Vetala', 'Taraka', 'Rangda']},
    {'result': 'Kohryu', 'sources': ['Genbu', 'Seiryuu', 'Suzaku', 'Byakko']},
    {'result': 'Lilith', 'sources': ['Lilim', 'Vetala', 'Incubus', 'Succubus']},
    {'result': 'Lucifer', 'sources': ['Samael', 'Abaddon', 'Beelzebub', 'Satan', 'Helel']},
    {'result': 'Mara', 'sources': ['Incubus', 'Pazuzu', 'Mot', 'Kumbhanda', 'Attis']},
    {'result': 'Masakado', 'sources': ['Zouchouten', 'Jikokuten', 'Koumokuten', 'Bishamonten']},
    {'result': 'Messiah', 'sources': ['Orpheus', 'Thanatos']},
    {'result': 'Metatron', 'sources': ['Uriel', 'Raphael', 'Gabriel', 'Michael']},
    {'result': 'Norn', 'sources': ['Clotho', 'Lachesis', 'Atropos']},
    {'result': 'Orpheus', 'sources': ['Slime', 'Legion']},
    {'result': 'Orpheus Telos', 'sources': ['Thanatos', 'Chi You', 'Helel', 'Asura', 'Messiah', 'Metatron']},
    {'result': 'Sandalphon', 'sources': ['Gurr', 'Suzaku', 'Yatagarasu', 'Horus', 'Garuda']},
    {'result': 'Shiva', 'sources': ['Barong', 'Rangda']},
    {'result': 'Susano-o', 'sources': ['Orpheus', 'Legion', 'Black Frost', 'Ose', 'Decarabia', 'Loki']},
    {'result': 'Thanatos', 'sources': ['Ghoul', 'Pale Rider', 'Loa', 'Samael', 'Mot', 'Alice']},
]

for combo in specialCombos:
    # Update the 'name' value to be lower case
    combo['result'] = combo['result'].lower()
    combo['sources'] = [source.lower() for source in combo['sources']]








# In[ ]:


# export a dictionary to a json file
import json
with open('arcana2Combos.json', 'w') as fp:
    json.dump(arcana2Combos, fp)

with open('arcana3Combos.json', 'w') as fp:
    json.dump(arcana3Combos, fp)

with open('specialCombos.json', 'w') as fp:
    json.dump(specialCombos, fp)


# In[ ]:


# open json file and read contenta as a list of dictionaries
with open('combos2.json', 'r') as fp:
    arcana2Combos = json.load(fp)

with open('combos3.json', 'r') as fp:
    arcana3Combos = json.load(fp)

with open('specialCombos.json', 'r') as fp:
    specialCombos = json.load(fp)


# In[3]:


class PersonaCompendiumExtracted:
    def __init__(self, name, level, skills):
        self.name = name
        self.level = level
        self.skills = skills

import json

# Load the JSON file
with open('persona_compendium_save_file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# Create Persona objects
personas_compendium_extracted = [PersonaCompendiumExtracted(item['name'], item['level'], item['skills']) for item in data]

for persona in personae:
    persona['base_level+5'] = persona['level'] + 5 # max social links lead to a +5 bonus
    persona['base_level'] = persona['level']

# overwrite 'personae' with the new list
for persona_compendium_extracted in personas_compendium_extracted:
    for persona in personae:
        if persona_compendium_extracted.name.lower() == persona['name'].lower():
            persona['level'] = persona_compendium_extracted.level
            persona['skills'] = persona_compendium_extracted.skills
            break


print(personae)


# In[4]:


for persona in personae:
    # if persona does not have 'skills' key print the name
    if 'skills' not in persona:
        print(persona['name'])


# In[12]:


import math


def generate_arcana_rank(personae):
    arcana_rank = {}
    rank = 0
    last_arcana = None
    for persona in personae:
        if persona['arcana'] == last_arcana:
            continue
        last_arcana = persona['arcana']
        arcana_rank[persona['arcana']] = rank
        rank += 1
    return arcana_rank

# Assuming 'personae' is a list of dictionaries with an 'arcana' key.
# You need to define or import this list from your data.
arcana_rank = generate_arcana_rank(personae)

def generate_personae_by_name(personae):
    personae_by_name = {}
    for persona in personae:
        personae_by_name[persona['name']] = persona
    return personae_by_name

personae_by_name = generate_personae_by_name(personae)

def generate_personae_by_arcana(personae):
    personae_by_arcana = {}
    for persona in personae:
        arcana = persona['arcana']
        if arcana not in personae_by_arcana:
            personae_by_arcana[arcana] = []
        personae_by_arcana[arcana].append(persona)
    return personae_by_arcana

# Assuming 'personae' is a list of dictionaries with at least an 'arcana' key.
# You need to define or import this list from your data.
personae_by_arcana = generate_personae_by_arcana(personae)




class CalcCtrl:
    def __init__(self, persona_name, is_intermediate_fusion=False):
        self.ceil = math.ceil
        
        self.level_key = 'base_level'

        if is_intermediate_fusion:
            self.current_level_key = 'base_level+5'
        else:
            self.current_level_key = 'level'

        self.persona = personae_by_name.get(persona_name)

        self.all_recipes = []  # Consider renaming this to just 'recipes' for consistency with other methods
        if self.persona:
            self.get_recipes()
            self.all_recipes.sort(key=lambda x: x['cost'])
            self.max_cost = max(recipe['cost'] for recipe in self.all_recipes) if self.all_recipes else 0

    @staticmethod
    def get_rank(persona):
        return arcana_rank[persona['arcana']]

    def add_recipe(self, recipe):
        recipe['cost'] = sum((27 * source[self.level_key]**2 + 126 * source[self.level_key] + 2147) for source in recipe['sources'])
        recipe['sources'].sort(key=lambda x: (-x[self.level_key], self.get_rank(x)))
        self.all_recipes.append(recipe)

    def fuse2(self, arcana, persona1, persona2):
        level = 1 + (persona1[self.level_key] + persona2[self.level_key]) // 2
        personae = personae_by_arcana[arcana]

        for i, persona in enumerate(personae):
            if persona[self.level_key] >= level:
                if persona.get('special'):
                    continue
                break

        if persona1['arcana'] == persona2['arcana']:
            i -= 1
        if i < len(personae) and (personae[i] == persona1 or personae[i] == persona2):
            i -= 1

        return personae[max(i, 0)]  # Ensure i doesn't go below 0

    def fuse3(self, arcana, persona1, persona2, persona3):
        level = 5 + (persona1[self.level_key] + persona2[self.level_key] + persona3[self.level_key]) // 3
        personae = personae_by_arcana[arcana]

        found = False
        for i, persona in enumerate(personae):
            if persona[self.level_key] >= level:
                if persona.get('special'):
                    continue
                found = True
                break

        if not found:
            return None

        # In same arcana fusion, skip over the ingredients.
        if persona1['arcana'] == arcana and persona2['arcana'] == arcana and persona3['arcana'] == arcana:
            while (i < len(personae) and (persona1['name'] == personae[i]['name'] or
                                          persona2['name'] == personae[i]['name'] or
                                          persona3['name'] == personae[i]['name'])):
                i += 1
                if i >= len(personae):
                    return None

        return personae[i] if i < len(personae) else None
    
    def persona3_is_valid(self, persona1, persona2, persona3):
        if persona3 == persona1 or persona3 == persona2:
            return False
        
        if persona1['name'] == 'siegfried' and persona2['name'] == 'kali' and persona3['name'] == 'orthrus':
            print('here')

        if persona1['name'] == 'kali' and persona2['name'] == 'siegfried' and persona3['name'] == 'orthrus':
            print('here')
        
        if persona1['name'] == 'siegfried' and persona2['name'] == 'orthrus' and persona3['name'] == 'kali':
            print('here')
        
        if persona1['name'] == 'orthrus' and persona2['name'] == 'siegfried' and persona3['name'] == 'kali':
            print('here')
        
        if persona1['name'] == 'orthrus' and persona2['name'] == 'kali' and persona3['name'] == 'siegfried':
            print('here')
        
        if persona1['name'] == 'kali' and persona2['name'] == 'orthrus' and persona3['name'] == 'siegfried':
            print('here')


        if persona3[self.current_level_key] < persona1[self.current_level_key] or persona3[self.current_level_key] < persona2[self.current_level_key]:
            return False

        if persona3[self.current_level_key] == persona1[self.current_level_key]:
            return arcana_rank[persona3['arcana']] < arcana_rank[persona1['arcana']]

        if persona3[self.current_level_key] == persona2[self.current_level_key]:
            return arcana_rank[persona3['arcana']] < arcana_rank[persona2['arcana']]

        return True

    def find_3way_recipes(self, arcana1, arcana2):
        step1_recipes = self.get_arcana_recipes(arcana1)
        for step1_recipe in step1_recipes:
            persona1 = step1_recipe['sources'][0]
            persona2 = step1_recipe['sources'][1]
            personae = personae_by_arcana[arcana2]

            for persona3 in personae:
                if self.persona3_is_valid(persona1, persona2, persona3):
                    result = self.fuse3(self.persona['arcana'], persona1, persona2, persona3)
                    if not result or result['name'] != self.persona['name']:
                        continue

                    # filter if persona1,persona2 or persona3 name are equal to result
                    if persona1['name'] == result['name'] or persona2['name'] == result['name'] or persona3['name'] == result['name']:
                        continue

                    self.add_recipe({'sources': [persona1, persona2, persona3]})

    def get_recipes(self):
        # if persona is the target of a special combo, add the recipe
        if self.persona.get('special'):
            for combo in specialCombos:
                if self.persona['name'] == combo['result']:
                    recipe = {'sources': [personae_by_name[source] for source in combo['sources']]}
                    self.add_recipe(recipe)
                    return
        
        # Define filter_2way inside get_recipes
        def filter_2way(persona1, persona2, result):
            # Note: 'self' is accessible here because this is an inner function
            if persona1['name'] ==  self.persona['name']:
                return True
            if persona2['name'] ==  self.persona['name']:
                return True
            if result['name'] ==  self.persona['name']:
                return False
            return True
        

        # first get all normal spread (2 way fusions)
        recipes = self.get_arcana_recipes(self.persona['arcana'], filter_2way)
        for recipe in recipes:
            self.add_recipe(recipe)

        # Consider triangle fusion
        combos = [combo for combo in arcana3Combos if combo['result'] == self.persona['arcana']]
        for combo in combos:
            self.find_3way_recipes(combo['source'][0], combo['source'][1])
            if combo['source'][1] != combo['source'][0]:
                self.find_3way_recipes(combo['source'][1], combo['source'][0])
    
    def get_arcana_recipes(self, arcana_name, filter_callback=None):
        recipes = []
        combos = [x for x in arcana2Combos if x['result'] == arcana_name]

        for combo in combos:
            personae1 = personae_by_arcana[combo['source'][0]]
            personae2 = personae_by_arcana[combo['source'][1]]

            for i, persona1 in enumerate(personae1):
                for j, persona2 in enumerate(personae2):
                    if persona1['arcana'] == persona2['arcana'] and j <= i:
                        continue
                    result = self.fuse2(combo['result'], persona1, persona2)
                    if not result:
                        continue
                    if filter_callback and filter_callback(persona1, persona2, result):
                        continue

                    recipes.append({'sources': [persona1, persona2]})

        return recipes

calc_ctrl = CalcCtrl('chi you', is_intermediate_fusion=False)
#calc_ctrl = CalcCtrl('orpheus telos', is_intermediate_fusion=True)
print(calc_ctrl.all_recipes)


def print_sources(recipes, file):
    for recipe in recipes:
        print("Recipe:", file=file)
        for source in recipe['sources']:
            name = source.get('name', 'Unknown')
            level = source.get('level', 'Unknown')
            arcana = source.get('arcana', 'Unknown')
            special = ' (special)' if source.get('special') else ''
            print(f"  - {name}, Level: {level}, Arcana: {arcana}{special}", file=file)
        cost = recipe.get('cost', 'Unknown')
        print(f"Total Cost: {cost}\n", file=file)



# In[15]:


barong_test = CalcCtrl('barong', is_intermediate_fusion=False)
#['siegfried', 'kali', 'orthrus']
for recipe in barong_test.all_recipes:
    siegfried = False
    kali = False
    orthrus = False
    for source in recipe['sources']:
        if source['name'] == 'siegfried':
            siegfried = True
        if source['name'] == 'kali':
            kali = True
        if source['name'] == 'orthrus':
            orthrus = True
        if siegfried and kali and orthrus:
            print(recipe['cost'])


# In[16]:





# In[17]:


# open dataframe located in "/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv"
import pandas as pd
df = pd.read_csv("/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv")


print(df)

skill_type_dict = df.set_index('skill')['type'].to_dict()


# given a skill name return the skill type
def get_skill_type(skill_name):
    return skill_type_dict[skill_name]

print(get_skill_type('Agidyne'))

persona_name = 'chi you'

# load '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/inheritance.csv' into a dataframe
inheritance_df = pd.read_csv('/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/inheritance.csv')
# load '/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/personas_inheritance.csv' into a dataframe
persona_inheritance_df = pd.read_csv('/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/personas_inheritance.csv')

# get the type of the persona 'chi you' in the persona_inheritance_df
persona_inherit_type = persona_inheritance_df.loc[persona_inheritance_df['Persona'] == persona_name, 'Type'].iloc[0]


# Convert the DataFrame to a dictionary where each key is an inheritance type
# and its value is another dictionary of skill types and their probabilities.
inheritance_dict = inheritance_df.set_index('Inheritance Type').T.to_dict('dict')



# given a skill type return the skill inheritance probability for a given persona type
def get_inheritance_probability(skill_type, persona_inheritance_type):
    # Access the nested dictionary directly for the value
    # Check if the persona_inheritance_type exists to avoid KeyErrors
    if persona_inheritance_type in inheritance_dict:
        # Return the probability value for the given skill_type and persona_inheritance_type
        return inheritance_dict[persona_inheritance_type].get(skill_type, 0)  # Returns 0 if skill_type is not found


print(get_inheritance_probability('Almighty', persona_inherit_type))

#https://web.archive.org/web/20131213184851/http://www.gamefaqs.com/ps2/937269-shin-megami-tensei-persona-3-fes/faqs/52531
''' 
 ============================
 |   Pre-Fusion | Post-Fusion |
 | Total Skills |   Inherited |
  -----------------------------
 |         < 6  |           1 |
 |         6-8  |           2 |
 |        9-11  |           3 |
 |       12-23  |           4 |
 |       24-31  |           5 |
 |   32-39 (?)  |           6 |
 |   40-47 (?)  |           7 |
 |      48 (?)  |           8 |
  ----------------------------
'''

def get_ammount_of_inherited_skills(skills):
    if len(skills) < 6:
        return 1
    elif len(skills) < 9:
        return 2
    elif len(skills) < 12:
        return 3
    elif len(skills) < 24:
        return 4
    elif len(skills) < 32:
        return 5
    elif len(skills) < 40:
        return 6
    elif len(skills) < 48:
        return 7
    else:
        return 8
    
def create_desired_skills_probability_dict(desired_skills):
    desired_skills_probability_dict = {}
    for s in desired_skills:
        skill_type = get_skill_type(s)
        desired_skills_probability_dict[s] = get_inheritance_probability(skill_type, persona_inherit_type)
    return desired_skills_probability_dict
    
def get_best_recipe(desired_skills, recipes_list):

    best_ratio = 0
    best_ratio_max = 0
    best_recipe = recipes_list[0]
    best_set = None

    best_ratio_max = 0
    best_recipe_max = best_recipe
    best_set_max = best_set
    best_skills_max = best_set

    biggest_ammount_of_inherited_skills = 0

    for i in range(len(recipes_list)):
        current_skills = []
        dont_have = False

        lucifer = False
        norn = False
        baal_zebul = False

        for j in range(len(recipes_list[i]['sources'])):
            # if 'skills' key does not exist continue
            if 'skills' not in recipes_list[i]['sources'][j]:
                dont_have = True
                continue
            for s in recipes_list[i]['sources'][j]['skills']:
                current_skills.append(s)
            if recipes_list[i]['sources'][j]['name'] == 'lucifer':
                lucifer = True
            if recipes_list[i]['sources'][j]['name'] == 'norn':
                norn = True
            if recipes_list[i]['sources'][j]['name'] == 'baal zebul':
                baal_zebul = True
            if lucifer and baal_zebul and norn:
                #print('hello')
                None
            
        
        if dont_have:
            continue

        ammount_of_inherited_skills = get_ammount_of_inherited_skills(current_skills)

        

        if ammount_of_inherited_skills > biggest_ammount_of_inherited_skills:
            best_ratio_max = 0
            best_recipe_max = None
            best_set_max = None
            biggest_ammount_of_inherited_skills = ammount_of_inherited_skills
            

        set_current_skills = list(set(current_skills))
        
        #count how many skills of the desired skills are in the current skills
        desired_count = 0
        
        # while 'ammount_of_inherited_skills' is not reached count as many 'desired_skills' as possible. If space still remais count 'noise_skills'
        for s in set_current_skills:
            skill_type = get_skill_type(s)
            if s in desired_skills:
                ratio_skill = get_inheritance_probability(skill_type, persona_inherit_type)
                if ratio_skill > 0:
                    desired_count += 1
        
        
        current_desired_skills = []

        #count how many skills of the desired skills are in the current skills
        desired_count_ratio = 0
        noise_count_ratio = 0
        for s in set_current_skills:
            # get the skill type from the dataframe
            skill_type = get_skill_type(s)

            ratio_skill = get_inheritance_probability(skill_type, persona_inherit_type)
            if s in desired_skills:
                current_desired_skills.append(s)
                desired_count_ratio += ratio_skill
            else:
                noise_count_ratio += ratio_skill

        # should it be 1 or something between? should i switch nominator and denominator?   
        ratio = desired_count_ratio / max(noise_count_ratio,1)

        # the bigger the ratio the better
        if ratio > best_ratio:
            best_ratio = ratio
            best_recipe = recipes_list[i]
            best_set = set_current_skills
            best_desired_skills_prob_dict = create_desired_skills_probability_dict(current_desired_skills)
        
        if desired_count >= biggest_ammount_of_inherited_skills and ammount_of_inherited_skills == biggest_ammount_of_inherited_skills and ratio > best_ratio_max:
            best_ratio_max = ratio
            best_recipe_max = recipes_list[i]
            best_set_max = set_current_skills
            best_skills_max = current_skills
            best_desired_skills_prob_dict_max = create_desired_skills_probability_dict(current_desired_skills)

        if 2185 == i:
            running_ratio = ratio
            running_recipe = recipes_list[i]
            running_set = set_current_skills

    return best_ratio, best_recipe, best_set, best_desired_skills_prob_dict, biggest_ammount_of_inherited_skills, best_ratio_max, best_recipe_max, best_set_max, best_skills_max, best_desired_skills_prob_dict_max, running_ratio, running_recipe, running_set


chi_you_base = CalcCtrl(persona_name, is_intermediate_fusion=False).all_recipes



mandatory_skills = [
'High Counter',
'Unshaken Will',
'Panta Rhei',
]

optional_skills = [
'Wind Boost',
'Wind Amp',
'Spell Master',
'Mind Charge',
'Salvation',
]

desired_skills = mandatory_skills + optional_skills

best_ratio, best_recipe, best_set, best_desired_skills_prob_dict, biggest_ammount_of_inherited_skills, best_ratio_max, best_recipe_max, best_set_max, best_skills_max, best_desired_skills_prob_dict_max, running_ratio, running_recipe, running_set = get_best_recipe(desired_skills=desired_skills, recipes_list=chi_you_base)

print('best')
print(best_ratio)
print(best_recipe)
print(len(best_set))
print(best_set)
print(best_desired_skills_prob_dict)

#print(running_ratio)
#print(running_recipe)
#print(len(running_set))
#print(running_set)

print('bigest')
print(biggest_ammount_of_inherited_skills)
print(best_ratio_max)
print(best_recipe_max)
print(len(best_set_max))
print(best_set_max)
print(len(best_skills_max))
print(best_desired_skills_prob_dict_max)



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)





# In[2]:


get_ipython().system('jupyter nbconvert --to script fusion_calculator.ipynb')


# In[ ]:





# In[16]:


import pandas as pd
# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\\Users\\Eduardo\\Documents\\Projects\\AutoTelos\\inheritable_skills_with_levels.csv')

#print all lines of the dataframe
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)


# In[19]:


import ast

class UnlockableSkill:
    def __init__(self, name, level=None):
        self.name = name
        self.level = level

    def __repr__(self):
        if self.level:
            return f"('{self.name}', lv{self.level})"
        else:
            return f"('{self.name}')"

# Sample data with skills as a string representation of a list
data = {
    'persona': ['abaddon', 'alice'],
    'skill': [
        "['Weary Thrust', 'Evil Smile', 'High Counter']",
        "['Die for Me!(59)', 'Spirit Drain']"
    ]
}

def extract_skills(data):
    skill_dict = {}
    for persona, skills_str in zip(data['persona'], data['skill']):
        # Safely evaluate the string as a list
        skills = ast.literal_eval(skills_str)
        skill_list = []
        for skill in skills:
            # Check if there's a level specified in the skill string
            if '(' in skill and ')' in skill:
                name, level_str = skill.rsplit('(', 1)
                level = int(level_str[:-1])  # Remove the closing parenthesis and convert to int
            else:
                name, level = skill, None

            skill_list.append(UnlockableSkill(name.strip(), level))
        
        skill_dict[persona] = skill_list

    return skill_dict

skill_dict = extract_skills(df)
for persona, skills in skill_dict.items():
    None
    #print(f"{persona}: {skills}")


# verify if for any persona in the dictionary, if it's skills have level numbers that repeat
for persona, skills in skill_dict.items():
    levels = [skill.level for skill in skills]
    # remove 'None' values from the list
    levels = [level for level in levels if level is not None]
    if len(levels) != len(set(levels)):
        print(f"Persona {persona} has repeated levels: {levels}")



# In[22]:


mandatory_skills = [
'High Counter',
'Unshaken Will',
'Panta Rhei',
]

optional_skills = [
'Wind Boost',
'Wind Amp',
'Spell Master',
'Mind Charge',
'Salvation',
]

def separate_keys(previous_skills):
    # Initialize the dictionaries
    accumulated_mandatory_skills = {}
    accumulated_optional_skills = {}
    accumulated_noise_skills = {}

    # Separate the keys into the three dictionaries
    for key, value in previous_skills.items():
        if key in mandatory_skills:
            accumulated_mandatory_skills[key] = value
        elif key in optional_skills:
            accumulated_optional_skills[key] = value
        else:
            accumulated_noise_skills[key] = value
    
    return accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills




class Persona:
    
    def __init__(self, name) -> None:
        self.name = name.lower()
        self.calc_ctrl = CalcCtrl(self.name, personae_by_name, personae_by_arcana, specialCombos, arcana_rank)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, o: object) -> bool:
        return self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)
    
class Recipe:

    def __init__(self, personas,accumulated_mandatory_skills, accumulated_optional_skills,accumulated_noise_skills , previous_recipe = None) -> None:
        self.personas = personas # list of personas
        self.accumulated_mandatory_skills =  accumulated_mandatory_skills # dict of accumulated mandatory skills
        self.accumulated_optional_skills = accumulated_optional_skills # dict of accumulated optional skills
        self.accumulated_noise_skills = accumulated_noise_skills # dict of accumulated noise skills
        self.previous_recipe = previous_recipe # previous recipe
        self.next_recipes = [] # list of next recipes

    
    def __str__(self) -> str:
        return str(self.personas)


def count_true_values(dictionary):
    return list(dictionary.values()).count(True)

class BFS:

    def __init__(self,initial_persona, mandatory_skills, optional_skills ) -> None:
        self.mandatory_skills = mandatory_skills
        self.optional_skills = optional_skills
        self.initial_persona = initial_persona
        self.all_personas = {initial_persona.name : initial_persona}
        self.current_level_list_of_recipies = None
        self.first_recipie = None
    
    def get_persona_skills(self,persona,accumulated_mandatory_skills,accumulated_optional_skills, accumulated_noise_skills):
        
        persona_skills = persona_skills_dict.get(persona.name, None)
        for skill in persona_skills:
            # check if its in the keys of accumulated_mandatory_skills
            if skill in accumulated_mandatory_skills:
                # increment `accumulated_mandatory_skills[skill]``
                accumulated_mandatory_skills[skill] += 1
            # do the same for accumulated_optional_skills
            elif skill in accumulated_optional_skills:
                accumulated_optional_skills[skill] += 1
            #skill not part of mandatory or optional skills
            else:
                noise_skill_count = accumulated_noise_skills.get(skill, 0)
                accumulated_noise_skills[skill] = noise_skill_count + 1
            
        # return all dictionaries
        return accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills

    def convert_all_recepies_list_to_recipe_object_list(self,all_recepies,accumulated_mandatory_skills,accumulated_optional_skills,accumulated_noise_skills, previous_recipe = None):
        recipes = []
        for recipe in all_recepies:
            personas = []
            current_recipe_accumulated_mandatory_skills = accumulated_mandatory_skills.copy()
            current_recipe_accumulated_optional_skills = accumulated_optional_skills.copy()
            current_recipe_accumulated_noise_skills = accumulated_noise_skills.copy()
            for parent in recipe['sources']:
                name = parent.get('name', 'Unknown')
                if name not in self.all_personas:
                    persona = Persona(name)
                    self.all_personas[name] = persona
                else:
                    persona = self.all_personas[name]
                current_recipe_accumulated_mandatory_skills, current_recipe_accumulated_optional_skills , current_recipe_accumulated_noise_skills = self.get_persona_skills(persona,current_recipe_accumulated_mandatory_skills,current_recipe_accumulated_optional_skills, current_recipe_accumulated_noise_skills)

                personas.append(persona)

            recipes.append(Recipe(personas, current_recipe_accumulated_mandatory_skills, current_recipe_accumulated_optional_skills,current_recipe_accumulated_noise_skills, previous_recipe = previous_recipe))
        return recipes
    
    def compare_dictionary_of_skills(self, previous_accumulated_mandatory_skills,previous_accumulated_optional_skills, previous_accumulated_noise_skills,
                                     current_accumulated_mandatory_skills, current_accumulated_optional_skills, current_accumulated_noise_skills,
                                        best_accumulated_mandatory_skills, best_accumulated_optional_skills, best_accumulated_noise_skills):
        # get the key of 'previous_dict' that has the lowest value
        min_key = min(previous_accumulated_mandatory_skills, key=previous_accumulated_mandatory_skills.get)

        # return 'True' if 'new_dict_1_no_desired_skills' has the least ammount of unique keys than 'new_dict2_no_desired_skills'
        if current_accumulated_mandatory_skills[min_key] > best_accumulated_mandatory_skills[min_key]:
            return True
        return False
            
    
    
    def select_best_recipes(self, list_of_lists_of_recipes, previous_accumulated_mandatory_skills, previous_accumulated_optional_skills, previous_accumulated_noise_skills, next_recipes = []):
        #TODO solve the combination of recipies that maximizes the number of skills
        #TODO update acummulated_optional_skills and acummulated_mandatory_skills
        #TODO leave only recipies part of the optmiized solution

        # merge dictionaries 'accumulated_mandatory_skills' and 'accumulated_optional_skills' into one dictionary
        # Merge the dictionaries
        merged_previous_skills = {**previous_accumulated_mandatory_skills, **previous_accumulated_optional_skills, **previous_accumulated_noise_skills}

        previous_skills = merged_previous_skills

        maximal_combination = []
        for list_of_recipes in list_of_lists_of_recipes:
            maximal_combination.append(list_of_recipes[0])

        index_list_of_lists_of_recipes = 0
        for list_of_recipes in list_of_lists_of_recipes:
            for recipe in list_of_recipes:

                merged_current_skills = {**(recipe.accumulated_mandatory_skills), **(recipe.accumulated_optional_skills), **(recipe.accumulated_noise_skills)}
                merged_best_skills = {**(maximal_combination[index_list_of_lists_of_recipes].accumulated_mandatory_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_optional_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_noise_skills)}
                
                if self.compare_dictionary_of_skills(previous_accumulated_mandatory_skills,previous_accumulated_optional_skills, previous_accumulated_noise_skills,
                recipe.accumulated_mandatory_skills,recipe.accumulated_optional_skills, recipe.accumulated_noise_skills,
                maximal_combination[index_list_of_lists_of_recipes].accumulated_mandatory_skills,maximal_combination[index_list_of_lists_of_recipes].accumulated_optional_skills, maximal_combination[index_list_of_lists_of_recipes].accumulated_noise_skills):
                    maximal_combination[index_list_of_lists_of_recipes] = recipe

            
            # finalizing 'for' loop
            ## update previous skills for next list of recipe
            previous_skills = {**(maximal_combination[index_list_of_lists_of_recipes].accumulated_mandatory_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_optional_skills), **(maximal_combination[index_list_of_lists_of_recipes].accumulated_noise_skills)}
            
            ## updating reference for next recipes
            if maximal_combination[index_list_of_lists_of_recipes].previous_recipe is not None:
                maximal_combination[index_list_of_lists_of_recipes].previous_recipe.next_recipes.append(maximal_combination[index_list_of_lists_of_recipes])
            
            index_list_of_lists_of_recipes += 1
        
        # finalizing 'for' loop
        
        accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills = separate_keys(previous_skills)

        return maximal_combination, accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills

    
    def find_personas_with_skills(self, max_layer = 4):
        accumulated_mandatory_skills = {}
        for skill in self.mandatory_skills:
            accumulated_mandatory_skills[skill] = 0

        accumulated_optional_skills = {}
        for skill in self.optional_skills:
            accumulated_optional_skills[skill] = 0
        
        accumulated_noise_skills = {}

        self.accumulated_mandatory_skills, self.accumulated_optional_skills, self.accumulated_noise_skills = self.get_persona_skills(self.initial_persona,accumulated_mandatory_skills,accumulated_optional_skills, accumulated_noise_skills)

        initial_recipies = self.initial_persona.calc_ctrl.all_recipes

        # make a list of recipies for each recipie in initial_recipies
        initial_recipies_list = self.convert_all_recepies_list_to_recipe_object_list(initial_recipies, accumulated_mandatory_skills,accumulated_optional_skills, accumulated_noise_skills, previous_recipe = None)

        current_level_list_of_lists_of_recipies = [initial_recipies_list]
        next_level_list_of_lists_of_recipies = []

        self.current_level_list_of_recipies, self.accumulated_mandatory_skills, self.accumulated_optional_skills, self.accumulated_noise_skills  = self.select_best_recipes(current_level_list_of_lists_of_recipies, accumulated_mandatory_skills, accumulated_optional_skills, accumulated_noise_skills, next_recipes = [])


        self.first_recipie = self.current_level_list_of_recipies[0]
        bfs_layer = 0

        while bfs_layer < max_layer: #major BFS Loop. made on a fixed number of iterations
            print('layer ', bfs_layer)        
            # loop while current_level_queue is not empty
            while self.current_level_list_of_recipies:
                current_recipe = self.current_level_list_of_recipies.pop(0)

                for current_persona in current_recipe.personas:
                    new_persona_recipes_list = []
                    current_persona_recipies = current_persona.calc_ctrl.all_recipes
                    current_persona_recipies_list = self.convert_all_recepies_list_to_recipe_object_list(current_persona_recipies,current_recipe.accumulated_mandatory_skills,current_recipe.accumulated_optional_skills, current_recipe.accumulated_noise_skills, previous_recipe=current_recipe)

                    for recipe in current_persona_recipies_list:
                        new_persona_recipes_list.append(recipe)
                    next_level_list_of_lists_of_recipies.append(new_persona_recipes_list)

            #TODO solve the combination of recipies that maximizes the number of skills
            #TODO update acummulated_optional_skills and acummulated_mandatory_skills
            #TODO leave only recipies part of the optmiized solution
            # pass all elements from next_level_queue to current_level_queue
            next_level_list_of_recipies, self.accumulated_mandatory_skills, self.accumulated_optional_skills, self.accumulated_noise_skills = self.select_best_recipes(next_level_list_of_lists_of_recipies, accumulated_mandatory_skills, accumulated_optional_skills,accumulated_noise_skills)
            

            #finalizing 'while' loop
            self.current_level_list_of_recipies = next_level_list_of_recipies
            bfs_layer += 1

        return None



# In[23]:


initial_persona = Persona('Orpheus Telos')
bfs = BFS(initial_persona, mandatory_skills, optional_skills)

bfs.find_personas_with_skills(max_layer = 4)


#  # abre persona
#  ## checa as skills que ela tem e adiciona as acumuladas daquela receita
#  ## para essa persona gere todas as receitas possiveis, mande para as receitas as skills acumuladas da receita daquela persona
#  ## para cada receita repete acima
# 
#  ## repita ate que todas as skills sejam encontradas

# In[21]:


bfs.accumulated_noise_skills


# In[41]:


import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Source

def build_graph(node, graph=None, parent=None):
    if graph is None:
        graph = nx.DiGraph()
    if parent:
        graph.add_edge(parent, node)
    for child in node.next_recipes:
        build_graph(child, graph, node)
    return graph

def visualize_tree(root, fig_size=(20, 20), dpi=300):
    graph = build_graph(root)
    plt.figure(figsize=fig_size)
    pos = nx.spring_layout(graph, k=0.5)  # Adjust the spacing between nodes with k

    # Set default color for nodes and then update the root node color
    node_colors = ['skyblue' if node != root else 'red' for node in graph.nodes()]

    # Draw the graph
    nx.draw(graph, pos, with_labels=False, node_size=5000, font_size=12, node_color=node_colors, edge_color='gray')
    #labels = {n: f"{n.attribute1}\n{n.attribute2}" for n in graph.nodes()}  # Customize as needed
    nx.draw_networkx_labels(graph, pos, None, font_size=8)

    # Save and show the graph
    plt.savefig("graph.png", format='PNG', dpi=dpi)
    plt.show()

# Example usage
# Build your tree by setting previous_recipe and next_recipes
visualize_tree(bfs.first_recipie, fig_size=(40, 40), dpi=300)


# In[28]:


import networkx as nx
import matplotlib.pyplot as plt

def build_graph(node, graph=None, parent=None, depth=0, levels=None):
    if graph is None:
        graph = nx.DiGraph()
    if levels is None:
        levels = {}
    
    # Assign the node to its level in the tree
    levels[node] = depth
    
    if parent:
        graph.add_edge(parent, node)
    for child in node.next_recipes:
        build_graph(child, graph, node, depth+1, levels)
    return graph, levels

def visualize_tree(root, fig_size=(20, 20), dpi=300):
    graph, levels = build_graph(root)
    plt.figure(figsize=fig_size)
    
    # Position nodes layer by layer
    pos = {node: (depth, -i) for i, (node, depth) in enumerate(sorted(levels.items(), key=lambda x: x[1]))}
    
    # Set colors layer by layer, root node will be red
    node_colors = ['skyblue' if node != root else 'red' for node in graph.nodes()]

    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_size=3000, font_size=12, node_color=node_colors, edge_color='gray')
    #labels = {n: f"{n.attribute1}\n{n.attribute2}" for n in graph.nodes()}  # Customize as needed
    nx.draw_networkx_labels(graph, pos, None, font_size=8)

    # Save and show the graph
    plt.savefig("/mnt/data/layered_tree_visualization.png", format='PNG', dpi=dpi)
    plt.show()

# Build your tree by setting previous_recipe and next_recipes
visualize_tree(bfs.first_recipie, fig_size=(120, 40), dpi=300)

