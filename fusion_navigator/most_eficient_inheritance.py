#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

import json

with open('/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/personae.json', 'r') as fp:
    personae = json.load(fp)

# open json file and read contenta as a list of dictionaries
with open('/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/combos2.json', 'r') as fp:
    arcana2Combos = json.load(fp)

with open('/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/combos3.json', 'r') as fp:
    arcana3Combos = json.load(fp)

with open('/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/specialCombos.json', 'r') as fp:
    specialCombos = json.load(fp)


# In[3]:


class PersonaCompendiumExtracted:
    def __init__(self, name, level, skills):
        self.name = name
        self.level = level
        self.skills = skills

import json

# Load the JSON file
with open('/home/eduardo/Documents/Persona3/AutoTelos/fusion_navigator/persona_compendium_save_file.json', 'r', encoding='utf-8') as f:
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

# In[5]:


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

#calc_ctrl = CalcCtrl('chi you', is_intermediate_fusion=False)
#calc_ctrl = CalcCtrl('orpheus telos', is_intermediate_fusion=True)
#print(calc_ctrl.all_recipes)


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


# In[17]:


# open dataframe located in "/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv"
import pandas as pd
df = pd.read_csv("/home/eduardo/Documents/Persona3/AutoTelos/skills_list/skills.csv")


#print(df)

skill_type_dict = df.set_index('skill')['type'].to_dict()

skill_rank_dict = df.set_index('skill')['rank'].to_dict()


# given a skill name return the skill type
def get_skill_type(skill_name):
    return skill_type_dict[skill_name]

def get_skill_rank(skill_name):
    return skill_rank_dict[skill_name]

#print(get_skill_type('Agidyne'))

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


#print(get_inheritance_probability('Almighty', persona_inherit_type))


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


#chi_you_base = CalcCtrl(persona_name, is_intermediate_fusion=False).all_recipes



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

#best_ratio, best_recipe, best_set, best_desired_skills_prob_dict, biggest_ammount_of_inherited_skills, best_ratio_max, best_recipe_max, best_set_max, best_skills_max, best_desired_skills_prob_dict_max, running_ratio, running_recipe, running_set = get_best_recipe(desired_skills=desired_skills, recipes_list=chi_you_base)


# In[2]:


import pandas as pd

# Read the CSV file
persona_inheritance_df = pd.read_csv('/home/eduardo/Documents/Persona3/AutoTelos/inheritance_calculator/personas_inheritance.csv')

# Convert the dataframe to a dictionary
persona_inheritance_dict = persona_inheritance_df.set_index('Persona')['Type'].to_dict()

def get_persona_inheritance_type(persona_name):
    # Use the dictionary for fast lookups
    return persona_inheritance_dict.get(persona_name)

# Example usage
#persona_inheritance_type = get_persona_inheritance_type("chi you")


# In[3]:


''' 
from itertools import product

class Persona:
    def __init__(self, data):
        self.name = data.get('name', 'Unknown')
        self.level = data.get('level', 0)
        self.arcana = data.get('arcana', 'Unknown')
        self.special = data.get('special', False)
        self.base_level = data.get('base_level', 0)
        self.base_level_plus_5 = data.get('base_level+5', self.base_level + 5)
        self.skills = data.get('skills', [])
        self.all_recipes = CalcCtrl(self.name, is_intermediate_fusion=False).all_recipes

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Level: {self.level}\n"
                f"Arcana: {self.arcana}\n"
                f"Special: {self.special}\n"
                f"Base Level: {self.base_level}\n"
                f"Base Level + 5: {self.base_level_plus_5}\n"
                f"Skills: {', '.join(self.skills)}")

all_personas = {}

# make a list with all integer numbers from 1 to 9 inclusive
# Create a list with all integer numbers from 1 to 9 inclusive
all_ranks = [i for i in range(1, 10)]

all_ratio_skill = [0.2, 1.0, 3.8, 8.0]

# beging search

def are_all_values_true(dictionary):
    return all(dictionary.values())

minimal_ammout_of_recipes = 0


total_dict = {(rank, ratio): False for rank, ratio in product(all_ranks, all_ratio_skill)}

print(total_dict)

total_dict[(6, 3.8)] = True


from tqdm import tqdm


list_of_best_recipes = []
list_of_highest_recipe_skills = []
list_of_best_skills_pair_dict = []
highest_count = 0

while not are_all_values_true(total_dict):
    minimal_ammout_of_recipes += 1
    print('raised to', minimal_ammout_of_recipes)
    for persona in tqdm(personae):
        persona_name = persona['name']

        persona_inherit_type = get_persona_inheritance_type(persona_name)

        if persona_name not in all_personas:
            # Convert JSON string to dictionary
            # Create Persona object
            current_p = Persona(persona)
            all_personas[persona_name] = current_p
        else:
            current_p = all_personas[persona_name]
        
        all_recipes = current_p.all_recipes

        for recipe in all_recipes:
            # make all values in the dictionary be the last iteration
            combinations_dict = total_dict.copy()
            personas = []
            recipe_skills = []
            for parent in recipe['sources']:
                name = parent.get('name', 'Unknown')
                if name not in all_personas:
                    # Convert JSON string to dictionary
                    # Create Persona object
                    current_p = Persona(parent)
                    all_personas[name] = current_p
                else:
                    current_p = all_personas[name]
                
                for s in current_p.skills:
                    recipe_skills.append(s)
                    
            recipe_skills_set_list = list(set(recipe_skills))
            
            #find all probability ratios for each skill in the recipe
            skills_pair_dict = {}
            for s in recipe_skills_set_list:
                skill_type = get_skill_type(s)
                ratio_skill = get_inheritance_probability(skill_type, persona_inherit_type)
                if ratio_skill == 0:
                    continue
                skill_rank = get_skill_rank(s)
                pair_ratio_skill_rank = (skill_rank, ratio_skill)
                skills_pair_dict[s] = pair_ratio_skill_rank

                if combinations_dict[pair_ratio_skill_rank] == False:
                    combinations_dict[pair_ratio_skill_rank] = True
                
            
            # count the ammount of True values in the dictionary
            count = sum(combinations_dict.values())
            
            if count > highest_count:
                highest_count = count
                best_recipe_of_the_round = recipe
                best_recipe_skills_set_list_of_the_round = recipe_skills_set_list
                best_skills_pair_dict_of_the_round = skills_pair_dict
                best_combinations_dict_of_the_round = combinations_dict.copy()
    total_dict = best_combinations_dict_of_the_round
    #print the ammount of true values in the dictionary
    true_count = sum(total_dict.values())
    print(true_count)
    list_of_best_recipes.append(best_recipe_of_the_round)
    list_of_highest_recipe_skills.append(best_recipe_skills_set_list_of_the_round)
    list_of_best_skills_pair_dict.append(best_skills_pair_dict_of_the_round)
    

print(minimal_ammout_of_recipes)
print(highest_count)
print(list_of_best_recipes)
print(list_of_highest_recipe_skills)
print(list_of_best_skills_pair_dict)    
'''


# In[4]:


''' 
print(list_of_best_recipes)
print(list_of_best_skills_pair_dict)



# for each recipe in the list of best recipes print the names of the personas
for recipe in list_of_best_recipes:
    for persona in recipe['sources']:
        print(persona['name'])
    print('---')
'''


# In[5]:


''' 
# print all values in total dict that are false
for k, v in total_dict.items():
    if v == False:
        print(k)
'''


# In[6]:


''' 
# accumulate all skils in a list and make a set out of it
for recipe in list_of_best_recipes[:1]:
    all_skills = []
    for persona in recipe['sources']:
        skills = persona['skills']
        for s in skills:
            all_skills.append(s)
    all_skills_set = list(set(all_skills))

    print(all_skills_set)

print(list(list_of_best_skills_pair_dict[0].keys()))
'''


# In[7]:


from itertools import product
from tqdm import tqdm


class Persona:
    def __init__(self, data):
        self.name = data.get('name', 'Unknown')
        self.level = data.get('level', 0)
        self.arcana = data.get('arcana', 'Unknown')
        self.special = data.get('special', False)
        self.base_level = data.get('base_level', 0)
        self.base_level_plus_5 = data.get('base_level+5', self.base_level + 5)
        self.skills = data.get('skills', [])
        self.all_recipes = CalcCtrl(self.name, is_intermediate_fusion=False).all_recipes

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Level: {self.level}\n"
                f"Arcana: {self.arcana}\n"
                f"Special: {self.special}\n"
                f"Base Level: {self.base_level}\n"
                f"Base Level + 5: {self.base_level_plus_5}\n"
                f"Skills: {', '.join(self.skills)}")

all_personas = {}

# make a list with all integer numbers from 1 to 9 inclusive
# Create a list with all integer numbers from 1 to 9 inclusive
all_ranks = [i for i in range(1, 10)]

all_ratio_skill = [0.2, 1.0, 3.8, 8.0]

total_dict = {(rank, ratio): False for rank, ratio in product(all_ranks, all_ratio_skill)}


total_dict[(6, 3.8)] = True

# beging search

def are_all_values_true(dictionary):
    return all(dictionary.values())

minimal_ammout_of_recipes = 0

class Recipe():
    def __init__(self, personas, skills_set, resulting_persona_name=None, coverage_dict=None):
        self.personas = personas
        self.skills_set = skills_set
        self.resulting_persona_name = resulting_persona_name
        self.coverage_dict = coverage_dict

    def __str__(self):
        # count ammount of true values in the dictionary
        count = sum(self.coverage_dict.values())

        persona_names = [persona.name for persona in self.personas]

        return (f"Personas: {persona_names}\n"
                f"Skills: {self.skills_set}\n"
                f"Resulting Persona: {self.resulting_persona_name}\n"
                f"Coverage: {self.coverage_dict}\n"
                f"Coverage Ammount: {count}\n")
    
    def __repr__(self):

        count = sum(self.coverage_dict.values())

        persona_names = [persona.name for persona in self.personas]

        return (f"Personas: {persona_names}\n"
                f"Skills: {self.skills_set}\n"
                f"Resulting Persona: {self.resulting_persona_name}\n"
                f"Coverage: {self.coverage_dict}\n"
                f"Coverage Ammount: {count}\n"
                "------------------------\n")

all_fucking_recipes = []

# giant list of recipes
for persona in tqdm(personae):
    persona_name = persona['name']

    persona_inherit_type = get_persona_inheritance_type(persona_name)

    if persona_name not in all_personas:
        # Convert JSON string to dictionary
        # Create Persona object
        current_p = Persona(persona)
        all_personas[persona_name] = current_p
    else:
        current_p = all_personas[persona_name]
    
    all_recipes = current_p.all_recipes

    for recipe in all_recipes:
        # make all values in the dictionary be the last iteration
        personas = []
        recipe_skills = []

        coverage_dict = total_dict.copy()
        for parent in recipe['sources']:
            name = parent.get('name', 'Unknown')
            if name not in all_personas:
                # Convert JSON string to dictionary
                # Create Persona object
                current_p = Persona(parent)
                all_personas[name] = current_p
            else:
                current_p = all_personas[name]
            personas.append(current_p)
            
            for s in current_p.skills:
                recipe_skills.append(s)

            for s in current_p.skills:
                skill_type = get_skill_type(s)
                ratio_skill = get_inheritance_probability(skill_type, persona_inherit_type)
                if ratio_skill == 0:
                    continue
                skill_rank = get_skill_rank(s)
                pair_ratio_skill_rank = (skill_rank, ratio_skill)
                coverage_dict[pair_ratio_skill_rank] = True
                
        recipe_skills_set_list = list(set(recipe_skills))

        all_fucking_recipes.append(Recipe(personas, recipe_skills_set_list,resulting_persona_name=persona_name,coverage_dict=coverage_dict))


print(len(all_fucking_recipes))


# In[8]:


import itertools


def coverage_of_list_of_recipes(list_of_recipes):
    total_dict = {(rank, ratio): False for rank, ratio in product(all_ranks, all_ratio_skill)}
    #print(total_dict)

    total_dict[(6, 3.8)] = True

    for recipe in list_of_recipes:
        
        recipe_skills_set_list = recipe.skills_set

        persona_inherit_type = get_persona_inheritance_type(recipe.resulting_persona_name)
        
        #find all probability ratios for each skill in the recipe
        skills_pair_dict = {}
        for s in recipe_skills_set_list:
            skill_type = get_skill_type(s)
            ratio_skill = get_inheritance_probability(skill_type, persona_inherit_type)
            if ratio_skill == 0:
                continue
            skill_rank = get_skill_rank(s)
            
            pair_ratio_skill_rank = (skill_rank, ratio_skill)
            skills_pair_dict[s] = pair_ratio_skill_rank

            
            total_dict[pair_ratio_skill_rank] = True
    
            
    # count the ammount of True values in the dictionary
    count = sum(total_dict.values())
    return count

recipe = all_fucking_recipes[:1]
print(recipe[0].coverage_dict)
coverage_of_list_of_recipes(recipe)




        


# In[9]:


# NEVER RUN THIS
''' 
# make a all possible permutations of 'all_fucking_recipes' and put them all in a list
permutations_list = []
print("Generating all permutations for different lengths")
for r in range(1, 4):
    for permutation in itertools.permutations(all_fucking_recipes[:2], r):
        permutations_list.append(permutation)
        None

print("Finished creating all permutations for different lengths")
print("Creating list")


max_coverage = 0
for permutation in tqdm(permutations_list):
    # if permutation is of type 'Recipe'
    if isinstance(permutation, Recipe):
        permutation = [permutation]
    cvg = coverage_of_list_of_recipes(permutation)
    if cvg > max_coverage:
        max_coverage = cvg
        max_perm = permutation

for recipe in max_perm:
    for persona in recipe.personas:
        print(persona.name)
    print('--')
print(max_coverage)
'''


# In[10]:


def remove_duplicate_recipes(recipe_list):
    unique_recipes = {}

    for recipe in recipe_list:
        coverage = tuple(sorted(recipe.coverage_dict.items()))  # Convert dict to tuple for hashability

        if coverage in unique_recipes:
            # Compare the length of 'personas' and keep the one with fewer elements
            if len(recipe.personas) < len(unique_recipes[coverage].personas):
                unique_recipes[coverage] = recipe
        else:
            unique_recipes[coverage] = recipe

    return list(unique_recipes.values())


def remove_recipes_with_zero_coverage(recipe_list):
    return [recipe for recipe in recipe_list if sum(recipe.coverage_dict.values()) > 0]

filtered_recipes = remove_duplicate_recipes(all_fucking_recipes)
filtered_recipes = remove_recipes_with_zero_coverage(filtered_recipes)
print(len(filtered_recipes))


# In[11]:


from tqdm import tqdm


list_of_best_recipes = []
list_of_highest_recipe_skills = []
highest_count = 0

total_dict = {(rank, ratio): False for rank, ratio in product(all_ranks, all_ratio_skill)}

total_dict[(6, 3.8)] = True

minimal_ammout_of_recipes = 0

while not are_all_values_true(total_dict):
    minimal_ammout_of_recipes += 1
    print('raised to', minimal_ammout_of_recipes)
    for recipe in filtered_recipes:
        persona_inherit_type = get_persona_inheritance_type(recipe.resulting_persona_name)
        combinations_dict = total_dict.copy()

        coverage_dict = recipe.coverage_dict

        # merge two dictionaries making 'True' prevail over 'False'

        merged_dict = {key: combinations_dict.get(key, False) or coverage_dict.get(key, False) for key in set(combinations_dict) | set(coverage_dict)}
            
        
        # count the ammount of True values in the dictionary
        count = sum(merged_dict.values())
        
        if count > highest_count:
            highest_count = count
            best_recipe_of_the_round = recipe
            best_recipe_skills_set_list_of_the_round = recipe_skills_set_list
            best_combinations_dict_of_the_round = merged_dict.copy()
    total_dict = best_combinations_dict_of_the_round
    #print the ammount of true values in the dictionary
    true_count = sum(total_dict.values())
    print(true_count)
    list_of_best_recipes.append(best_recipe_of_the_round)
    list_of_highest_recipe_skills.append(best_recipe_skills_set_list_of_the_round)
    

print(minimal_ammout_of_recipes)
print(highest_count)
print(list_of_best_recipes)
print(list_of_highest_recipe_skills)


# In[12]:


list_of_best_recipes


# In[13]:


dict_constraints = {}

for i in range(len(filtered_recipes)):
    recipe = filtered_recipes[i]
    coverage_dict = recipe.coverage_dict
    for key, value, in coverage_dict.items():
        if value == True:
            # add empty list if key does not exist
            if key not in dict_constraints:
                dict_constraints[key] = []
            dict_constraints[key].append(i)
            
dict_constraints_keys = list(dict_constraints.keys())
dict_constraints_keys.sort()
#print(dict_constraints_keys)
#print(len(dict_constraints_keys))
''' 
for key in dict_constraints_keys:
    list_of_indexes = dict_constraints[key]
    string = ''
    for index in list_of_indexes:
        string += 'x' + str(index)
        # if not the last index print "+"
        if index != list_of_indexes[-1]:
            string += ' + '
    string += ' >= 1'
    
    # Open the file and append the string
    with open('contraints_output.txt', 'a') as f:
        f.write(string + '\n')
'''



# In[14]:



a = []
list_of_row = []
index = 0
for key in dict_constraints_keys:
    coverage_index_list = dict_constraints[key]
    list_of_row = []
    print(key, index)
    for i in range(len(filtered_recipes)):
        if i == 0:
            g = 0
        if i in coverage_index_list:
            list_of_row.append(1)
        else:
            list_of_row.append(0)
    a.append(list_of_row)
    list_of_row = []
    index += 1


# In[15]:


import numpy as np

# Assuming 'a' is your matrix
a = np.array(a)

# erase all contents of 'matrix_a.txt'
open('matrix_a.txt', 'w').close()

# Save the matrix to a text file
np.savetxt('matrix_a.txt', a, fmt='%s')


# In[16]:


# Step 1: Read the matrix 'a' from the file
with open('matrix_a.txt', 'r') as file:
    matrix_a = np.loadtxt(file)

# Number of recipes (n) and tags (m)
n, m = matrix_a.shape

print(n, m)


# In[17]:


import pulp
import numpy as np
from tqdm import tqdm

# Step 1: Read the matrix 'a' from the file
with open('matrix_a.txt', 'r') as file:
    matrix_a = np.loadtxt(file)


# Number of recipes (n) and tags (m)
m, n = matrix_a.shape  # Note that m is the number of tags, n is the number of recipes

# Create the problem variable
prob = pulp.LpProblem("Recipe_Selection", pulp.LpMinimize)

# Decision variables
x = [pulp.LpVariable(f'x{j}', cat='Binary') for j in range(n)]

# Objective function
prob += pulp.lpSum(x)

# Constraints
for i in tqdm(range(m)):  # for each tag
    prob += pulp.lpSum(matrix_a[i][j] * x[j] for j in range(n)) >= 1, f"TagCoverage{i}"

# Solve the problem
prob.solve()

# Print the results
print("Status:", pulp.LpStatus[prob.status])
print("Minimum number of recipes:", pulp.value(prob.objective))
selected_recipes = [j for j in range(n) if x[j].varValue == 1]
print("Selected recipes (indexed at j):", selected_recipes)



# In[18]:


list_of_index_of_best_solutions = [61087, 61984, 67801, 74459, 76794]

list_of_best_solutions = []

for i in list_of_index_of_best_solutions:
    list_of_best_solutions.append(filtered_recipes[i])
    print(filtered_recipes[i])

list_of_best_solutions

coverage_of_list_of_recipes(list_of_best_solutions)


# In[19]:


import matplotlib.pyplot as plt

# Extracting counts from each recipe
counts = [sum(recipe.coverage_dict.values()) for recipe in filtered_recipes]

# Finding the range of count values
min_count = min(counts)
max_count = max(counts)

# Plotting the histogram with one bin for each integer value
plt.hist(counts, bins=range(min_count, max_count + 1), edgecolor='black')
plt.xticks(range(min_count, max_count + 1))  # Set x-ticks to show each integer
plt.title('Histogram of Coverage Counts')
plt.xlabel('Count')
plt.ylabel('Frequency')
plt.show()


# In[20]:


import matplotlib.pyplot as plt

# Initialize a dictionary to hold counts of True values for each key
true_counts = {}

# Count True occurrences for each key
for recipe in filtered_recipes:
    for key, value in recipe.coverage_dict.items():
        if value:  # Check if the value is True
            true_counts[key] = true_counts.get(key, 0) + 1

# Converting tuple keys to string representations for better plotting
keys = [str(key) for key in true_counts.keys()]
counts = list(true_counts.values())

# Checking the lengths of keys and counts
if len(keys) != len(counts):
    raise ValueError(f"Length mismatch: keys length is {len(keys)}, counts length is {len(counts)}")

# Plotting the histogram
plt.figure(figsize=(10, 6))  # Adjust figure size for better visibility
plt.bar(keys, counts, edgecolor='black')
plt.title('Histogram of True Counts for Each Key')
plt.xlabel('Key')
plt.ylabel('True Count Frequency')
plt.xticks(rotation=90)  # Rotate x-ticks if there are many keys
plt.tight_layout()  # Adjust layout for better fit
plt.show()




# Next code refers to a failed attempt at a genetic algorithm

# In[21]:


''' 
import random
from itertools import product

# Assume `filtered_recipes` is your list of Recipe objects
# Assume `all_ranks` and `all_ratio_skill` are defined and used to create `total_dict`

population_size = 100  # Number of individuals in each generation
max_generations = 1000   # Maximum number of generations
mutation_rate = 0.0001   # Probability of mutation
greedy_solution_best_amount = len(list_of_best_recipes)
PENALTY_FACTOR = 1000  # Penalty factor for each recipe used above the greedy solution

# Calculate the coverage for each recipe
recipe_coverages = [sum(recipe.coverage_dict.values()) for recipe in filtered_recipes]

# Normalize these values to use in mutation probabilities
max_coverage = max(recipe_coverages)
normalized_coverages = [coverage / max_coverage for coverage in recipe_coverages]

# Find the maximum true count to normalize
max_true_count = max(true_counts.values())

# Normalize true counts (inverse because we want rarer keys to have more weight)
normalized_true_counts = {key: (max_true_count / count) for key, count in true_counts.items()}


def greedy_solution_to_ga_format(list_of_best_recipes, filtered_recipes):
    return [recipe in list_of_best_recipes for recipe in filtered_recipes]



def create_individual():
    return [random.choice([True, False]) for _ in filtered_recipes]


def create_skewed_individual():
    individual = [False] * len(filtered_recipes)
    desired_amount = random.randint(1, greedy_solution_best_amount)
    
    # Choose recipes based on their coverage weights
    weighted_recipes = random.choices(range(len(filtered_recipes)), weights=normalized_coverages, k=desired_amount)
    
    for i in weighted_recipes:
        individual[i] = True
    return individual


def create_population_with_greedy(population_size, list_of_best_recipes, filtered_recipes):
    population = [create_skewed_individual() for _ in range(population_size - 1)]
    greedy_individual = greedy_solution_to_ga_format(list_of_best_recipes, filtered_recipes)
    population.append(greedy_individual)  # Add the greedy solution to the population
    return population

# Create initial population
population = create_population_with_greedy(population_size, list_of_best_recipes, filtered_recipes)

def create_initial_population(population_size, true_counts, filtered_recipes):
    population = []
    average_count = sum(true_counts.values()) / len(true_counts)
    
    for _ in range(population_size):
        individual = [False] * len(filtered_recipes)
        
        # Sort the recipes by their rarity based on the coverage dictionary
        recipes_sorted_by_rarity = sorted(filtered_recipes, key=lambda r: sum(r.coverage_dict.values()))
        
        # Ensure that rare keys have a higher chance of being covered
        for i, recipe in enumerate(recipes_sorted_by_rarity):
            coverage_true_count = sum(recipe.coverage_dict.values())
            if coverage_true_count < average_count:
                # Random chance to include the recipe based on rarity
                if random.random() < (average_count / coverage_true_count):
                    individual[i] = True
        
        population.append(individual)
    
    return population


population = create_initial_population(population_size, true_counts, filtered_recipes)

def calculate_fitness(individual):
    coverage_dict = {(rank, ratio): False for rank, ratio in product(all_ranks, all_ratio_skill)}
    num_recipes_used = sum(individual)
    
    for recipe, included in zip(filtered_recipes, individual):
        if included:
            for key in coverage_dict:
                coverage_dict[key] = coverage_dict[key] or recipe.coverage_dict.get(key, False)

    true_count = sum(coverage_dict.values())
    
    # Apply penalty only if the amount of recipes used is higher than greedy_solution_best_amount
    recipe_penalty = max(0, num_recipes_used - greedy_solution_best_amount) * 1000

    return true_count - recipe_penalty

def calculate_fitness(individual, normalized_true_counts):
    fitness = 0
    
    for recipe, included in zip(filtered_recipes, individual):
        if included:
            for key in recipe.coverage_dict:
                if recipe.coverage_dict[key]:
                    # The weight is inversely proportional to the frequency count
                    fitness += normalized_true_counts[key]
    
    # Penalize the number of recipes used
    fitness -= sum(individual) * PENALTY_FACTOR  # Define PENALTY_FACTOR appropriately

    return fitness





def tournament_selection(population, tournament_size, fitness_args):
    selected = random.sample(population, tournament_size)
    # Pass additional arguments to calculate_fitness
    selected.sort(key=lambda ind: calculate_fitness(ind, *fitness_args), reverse=True)
    return selected[0]


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]

# Define the heuristic_crossover function using the normalized coverages
def heuristic_crossover(parent1, parent2, normalized_coverages):
    # Initialize offspring with None to indicate undecided genes
    offspring = [None] * len(parent1)

    # Loop over each gene position
    for i in range(len(parent1)):
        # If both parents have the same gene, inherit it
        if parent1[i] == parent2[i]:
            offspring[i] = parent1[i]
        else:
            # Use normalized coverages to weigh the probability of inheriting the gene
            # The higher the coverage, the more likely to inherit the gene from the parent where it's True
            if random.random() < normalized_coverages[i]:
                offspring[i] = parent1[i] if parent1[i] else parent2[i]
            else:
                offspring[i] = parent2[i] if parent2[i] else parent1[i]

    # Resolve any undecided genes (if they exist)
    for i in range(len(offspring)):
        if offspring[i] is None:
            offspring[i] = random.choice([parent1[i], parent2[i]])

    return offspring


def mutate(individual):
    mutated_individual = []
    for gene, coverage in zip(individual, normalized_coverages):
        if gene:
            # Lower chance to flip if the recipe has higher coverage
            mutation_chance = mutation_rate * (1 - coverage)
        else:
            # Higher chance to flip if the recipe has higher coverage
            mutation_chance = mutation_rate * coverage

        mutated_gene = not gene if random.random() < mutation_chance else gene
        mutated_individual.append(mutated_gene)

    return mutated_individual

def mutate(individual, true_counts, filtered_recipes):
    # Determine average count to set a threshold for rarity
    average_count = sum(true_counts.values()) / len(true_counts)

    for i, included in enumerate(individual):
        recipe = filtered_recipes[i]
        recipe_true_count = sum(recipe.coverage_dict.values())

        if included and recipe_true_count > average_count:
            # Flip the gene with higher frequency more readily
            if random.random() < mutation_rate:
                individual[i] = not individual[i]
        elif not included and recipe_true_count < average_count:
            # Flip the gene with lower frequency less readily
            if random.random() < mutation_rate / 2:
                individual[i] = not individual[i]
    return individual



'''

''' 
for generation in range(max_generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        offspring1 = heuristic_crossover(parent1, parent2,normalized_coverages)
        offspring2 = heuristic_crossover(parent1, parent2,normalized_coverages)
        offspring1 = mutate(offspring1)
        offspring2 = mutate(offspring2)
        new_population.extend([offspring1, offspring2])
    population = new_population

    # Optional: Print the best fitness in this generation
    best_fitness = max(calculate_fitness(individual) for individual in population)
    print(f"Generation {generation}: Best Fitness = {best_fitness}")
'''

'''
# Assuming the rest of your GA setup is already in place

#population = create_initial_population(population_size, true_counts)

# Assuming calculate_fitness requires normalized_true_counts, which is a list or dict
fitness_args = (normalized_true_counts,)

for generation in range(max_generations):
    new_population = []
    
    for _ in range(population_size // 2):
        parent1 = tournament_selection(population, 10, fitness_args)
        parent2 = tournament_selection(population, 10, fitness_args)
        
        offspring1 = heuristic_crossover(parent1, parent2, true_counts)
        offspring2 = heuristic_crossover(parent1, parent2, true_counts)
        
        offspring1 = mutate(offspring1, true_counts, filtered_recipes)
        offspring2 = mutate(offspring2, true_counts, filtered_recipes)
        
        new_population.extend([offspring1, offspring2])
    
    population = new_population

    # Evaluate fitness
    best_fitness = max(calculate_fitness(individual, normalized_true_counts) for individual in population)
    print(f"Generation {generation}: Best Fitness = {best_fitness}")



best_individual = max(population, key=calculate_fitness)
best_recipe_indices = [i for i, included in enumerate(best_individual) if included]
best_recipes = [filtered_recipes[i] for i in best_recipe_indices]

print("Best Recipes:", best_recipes)
'''

