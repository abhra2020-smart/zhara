import pygame as pg
vec = pg.math.Vector2

BULLET_SIZES = ['sm', 'md', 'lg', 'xl']
ENCHANTED_BULLETS = ['2', '3', '5', '6', '7', '8', '9']
FIRE_BULLETS = ['3', '5', '6', '9']
SHOCK_BULLETS = ['2', '7', '8', '9']
EXPLOSIVE_BULLETS = ['4', '5', '8', '10']

# Weapon settings
WEAPON_SOUNDS = {'pistol': ['pistol.wav'], 'laser': ['laser.wav'], 'grenades': ['shotgun.wav'], 'pickaxe': ['mace_swipe.wav'], 'axe': ['mace_swipe.wav'],
                 'shotgun': ['shotgun.wav'], 'rifle': ['assault rifle.wav'], 'turret': ['turret.wav'], 'sword': ['sword_swipe.wav'], 'mace': ['mace_swipe.wav'], 'dagger': ['sword_swipe.wav'], 'shield': ['mace_swipe.wav']}
WEAPON_HIT_SOUNDS = {'pistol': ['gun_hit1.wav'], 'laser': ['gun_hit1.wav'], 'grenades': ['shotgun.wav'], 'pickaxe': ['pickaxe.wav'], 'axe': ['axe.wav'],
                 'shotgun': ['gun_hit1.wav'], 'rifle': ['gun_hit1.wav'], 'turret': ['turret_hit1.wav'], 'sword': ['sword_hit1.wav'], 'mace': ['mace_hit1.wav', 'mace_hit2.wav'], 'dagger': ['sword_hit1.wav'], 'shield': ['punch1.wav', 'punch2.wav']}

WEAPONS = {}
WEAPONS['harmless bullet source'] = {'type': 'turret',
                     'gun': True,
                     'bullet_speed': 10,
                     'bullet_lifetime': 300,
                     'magazine size': 1,
                     'reload speed': 1,
                     'rate': 1,
                     'auto': False,
                     'kickback': 0,
                     'knockback': 0,
                     'spread': 365,
                     'damage': 0,
                     'bullet_size': 'lg3',
                     'bullet_count': 10,
                     'grip': 'CP_PISTOL0',
                     'melee animation': 'WALK',
                     'melee damage': 0,
                     'walk': 'PISTOL_WALK',
                     'image': 0,
                     'offset': vec(0, 0),
                     'armor': 0,
                     'weight': 0}

WEAPONS['tank turret'] = {'type': 'turret',
                     'gun': True,
                     'bullet_speed': 1000,
                     'bullet_lifetime': 2000,
                     'melee damage': 0,
                     'magazine size': 1000,
                     'reload speed': 1,
                     'rate': 1000,
                     'auto': False,
                     'kickback': 0,
                     'knockback': 25,
                     'spread': 1,
                     'damage': 200,
                     'bullet_size': 'lg1',
                     'bullet_count': 1,
                     'grip': 'CP_PISTOL0',
                     'melee animation': 'WALK',
                     'walk': 'PISTOL_WALK',
                     'image': 27,
                     'offset': vec(275, 0),
                     'armor': 0,
                     'weight': 0}
WEAPONS['ship cannon'] = {'type': 'turret',
                     'gun': True,
                     'bullet_speed': 700,
                     'melee damage': 0,
                     'bullet_lifetime': 2000,
                     'magazine size': 100,
                     'reload speed': 1,
                     'rate': 1000,
                     'auto': False,
                     'kickback': 0,
                     'knockback': 25,
                     'spread': 1,
                     'damage': 300,
                     'bullet_size': 'xl1',
                     'bullet_count': 1,
                     'grip': 'CP_PISTOL0',
                     'melee animation': 'WALK',
                     'walk': 'PISTOL_WALK',
                     'image': 27,
                     'offset': vec(408, -28),
                     'armor': 0,
                     'weight': 0}
WEAPONS['fire bombs'] = {'type': 'turret',
                     'gun': True,
                     'bullet_speed': 300,
                     'bullet_lifetime': 1150,
                     'magazine size': 100,
                     'melee damage': 0,
                     'reload speed': 1,
                     'rate': 1000,
                     'auto': False,
                     'kickback': 0,
                     'knockback': 25,
                     'spread': 200,
                     'damage': 200,
                     'bullet_size': 'xl3',
                     'bullet_count': 20,
                     'grip': 'CP_PISTOL0',
                     'melee animation': 'WALK',
                     'walk': 'PISTOL_WALK',
                     'image': 27,
                     'offset': vec(0, 0),
                     'armor': 0,
                     'weight': 0}
WEAPONS['tank mini gun'] = {'type': 'rifle',
                      'gun': True,
                      'bullet_speed': 700,
                      'bullet_lifetime': 600,
                      'magazine size': 1000,
                      'reload speed': 1,
                      'rate': 80,
                      'auto': True,
                      'kickback': 0,
                      'knockback': 5,
                      'spread': 7,
                      'damage': 12,
                      'melee damage': 0,
                      'bullet_size': 'sm1',
                      'bullet_count': 1,
                      'walk': 'SHOTGUN_WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SHOTGUN0',
                      'image': 20,
                      'offset': vec(175, 65),
                      'armor': 0,
                      'weight': 0}

WEAPONS['mini gun'] = {'type': 'rifle', 'value': 2500,
                      'gun': True,
                      'bullet_speed': 700,
                      'bullet_lifetime': 600,
                      'magazine size': 500,
                      'reload speed': 300,
                      'rate': 80,
                      'auto': True,
                      'kickback': 25,
                      'knockback': 5,
                      'spread': 7,
                      'damage': 12,
                      'melee damage': 2,
                      'bullet_size': 'sm1',
                      'bullet_count': 1,
                      'walk': 'SHOTGUN_WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SHOTGUN0',
                      'image': 20,
                      'offset': vec(58, 0),
                      'armor': 0,
                      'weight': 15}

WEAPONS['mechanima blaster'] = {'type': 'laser', 'gun': True, 'value': 300,
                     'bullet_speed': 700,
                     'bullet_lifetime': 1200,
                     'magazine size': 50,
                     'reload speed': 100,
                     'rate': 100,
                     'auto': False,
                     'kickback': 3,
                     'knockback': 0.5,
                     'spread': 6,
                     'damage': 10,
                     'melee damage': 1,
                     'bullet_size': 'md2',
                     'bullet_count': 3,
                     'grip': 'CP_PISTOL0',
                     'melee animation': 'PUNCH',
                     'walk': 'PISTOL_WALK',
                     'image': 14,
                     'offset': vec(38, 0),
                     'armor': 0,
                     'materials': {'machine screws': 2, 'aluminum ingot': 2, 'steel pipe': 1, 'aluminum rod':1, 'steel wire':1, 'springs': 1, 'blue crystal':2},
                     'weight': 2}

WEAPONS['pistol'] = {'type': 'pistol','gun': True, 'value': 250,
                     'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'magazine size': 6,
                     'reload speed': 100,
                     'rate': 250,
                     'auto': False,
                     'kickback': 5,
                     'knockback': 0.2,
                     'spread': 5,
                     'damage': 10,
                     'melee damage': 1,
                     'bullet_size': 'md1',
                     'bullet_count': 1,
                     'grip': 'CP_PISTOL0',
                     'melee animation': 'PUNCH',
                     'walk': 'PISTOL_WALK',
                     'image': 1,
                     'offset': vec(28, 0),
                     'armor': 0,
                     'materials': {'machine screws': 1, 'aluminum ingot': 1, 'steel pipe': 1, 'springs': 1},
                     'weight': 1.4}

WEAPONS['grenade launcher'] = {'type': 'grenades','gun': True, 'value': 2000,
                     'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'magazine size': 1,
                     'reload speed': 150,
                     'rate': 500,
                     'auto': False,
                     'kickback': 55,
                     'knockback': 0,
                     'spread': 2,
                     'damage': 1,
                     'melee damage': 5,
                     'bullet_size': 'md4',
                     'bullet_count': 1,
                     'grip': 'CP_SHOTGUN0',
                     'melee animation': 'SWIPE',
                     'walk': 'SHOTGUN_WALK',
                     'image': 21,
                     'offset': vec(56, 0),
                     'armor': 0,
                     'weight': 10}

WEAPONS['auto grenade launcher'] = {'type': 'grenades','gun': True, 'value': 3000,
                     'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'magazine size': 12,
                     'reload speed': 300,
                     'rate': 500,
                     'auto': True,
                     'kickback': 55,
                     'knockback': 0,
                     'spread': 2,
                     'damage': 1,
                     'melee damage': 5,
                     'bullet_size': 'md4',
                     'bullet_count': 1,
                     'grip': 'CP_SHOTGUN0',
                     'melee animation': 'SWIPE',
                     'walk': 'SHOTGUN_WALK',
                     'image': 23,
                     'offset': vec(56, 0),
                     'armor': 0,
                     'weight': 10}

WEAPONS['grenade'] = {'type': 'grenades','gun': False,
                     'bullet_speed': 300,
                     'bullet_lifetime': 600,
                     'magazine size': 0,
                     'reload speed': 0,
                      'rate': 500,
                     'auto': False,
                     'kickback': 0,
                     'knockback': 0,
                     'spread': 20,
                     'damage': 1,
                     'melee damage': 2,
                     'bullet_size': 'md4',
                     'bullet_count': 0,
                     'grip': 'CP_PISTOL0',
                     'melee animation': 'SWIPE',
                     'walk': 'SHOTGUN_WALK',
                     'image': 22,
                     'offset': vec(0, 0),
                     'armor': 0,
                     'weight': 0.4}

WEAPONS['shotgun'] = {'type': 'shotgun','gun': True, 'value': 450,
                      'bullet_speed': 400,
                      'bullet_lifetime': 600,
                      'magazine size': 2,
                      'reload speed': 150,
                      'rate': 900,
                      'auto': False,
                      'kickback': 50,
                      'knockback': 0.5,
                      'spread': 20,
                      'damage': 6,
                      'melee damage': 2,
                      'bullet_size': 'sm1',
                      'bullet_count': 12,
                      'walk': 'SHOTGUN_WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SHOTGUN0',
                      'image': 2,
                      'offset': vec(58, 0),
                       'armor': 0,
                       'materials': {'machine screws': 1, 'wood block': 2, 'steel pipe': 2, 'springs': 1, 'steel ingot':1},
                      'weight': 2.7}
WEAPONS['assault rifle'] = {'type': 'rifle','gun': True, 'value': 700,
                      'bullet_speed': 700,
                      'bullet_lifetime': 800,
                      'magazine size': 30,
                      'reload speed': 160,
                      'rate': 100,
                      'auto': True,
                      'kickback': 0.4,
                      'knockback': 5,
                      'spread': 7,
                      'damage': 12,
                      'melee damage': 2,
                      'bullet_size': 'sm1',
                      'bullet_count': 1,
                      'walk': 'SHOTGUN_WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SHOTGUN0',
                      'image': 3,
                      'offset': vec(58, 0),
                      'armor': 0,
                      'weight': 2.9}
WEAPONS['steel sword'] = {'type': 'sword','gun': False, 'value': 200,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 0,
                      'rate': 200,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 12,
                      'spread': 0,
                      'damage': 5,
                      'melee damage': 20,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 4,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'steel ingot': 2}, 'upgrade': {'steel ingot': 1},
                      'weight': 4}
WEAPONS['Yaizhang'] = {'type': 'sword','gun': False,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 0,
                      'rate': 200,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 12,
                      'spread': 0,
                      'damage': 50,
                      'melee damage': 200,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 24,
                      'offset': vec(0, 0),
                      'armor': 25,
                      'weight': 4}
WEAPONS['karang'] = {'type': 'sword','gun': False,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 0,
                      'rate': 200,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 12,
                      'spread': 0,
                      'damage': 50,
                      'melee damage': 200,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 32,
                      'offset': vec(0, 0),
                      'armor': 25,
                      'weight': 4}
WEAPONS['live rabbit'] = {'type': 'sword','gun': False,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 0,
                      'rate': 200,
                      'auto': False,
                      'kickback': 10,
                      'knockback': 5,
                      'spread': 0,
                      'damage': 0.7,
                      'melee damage': 0.5,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'PISTOL_WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_PISTOL0',
                      'image': 5,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'weight': 5}
WEAPONS['live chicken'] = {'type': 'sword','gun': False,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 0,
                      'rate': 200,
                      'auto': False,
                      'kickback': 10,
                      'knockback': 20,
                      'spread': 0,
                      'damage': 1,
                      'melee damage': 0.5,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'SHOTGUN_WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SHOTGUN0',
                      'image': 6,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'weight': 6}
WEAPONS['live goldfish'] = {'type': 'mace','gun': False,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 0,
                      'rate': 200,
                      'auto': False,
                      'kickback': 10,
                      'knockback': 2,
                      'spread': 0,
                      'damage': 0.5,
                      'melee damage': 0.5,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'PISTOL_WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_PISTOL0',
                      'image': 7,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'weight': 1}
WEAPONS['live bluefish'] = {'type': 'mace','gun': False,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 0,
                      'rate': 200,
                      'auto': False,
                      'kickback': 10,
                      'knockback': 2,
                      'spread': 0,
                      'damage': 0.5,
                      'melee damage': 0.5,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'PISTOL_WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_PISTOL0',
                      'image': 18,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'weight': 1.2}

WEAPONS['garbage can lid'] = {'type': 'shield','gun': False, 'value': 10,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 200,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 25,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 5,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 8,
                      'offset': vec(0, 0),
                      'armor': 5,
                      'weight': 4}
WEAPONS['steel shield'] = {'type': 'shield','gun': False, 'value': 200,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 50,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 90,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 5,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 25,
                      'offset': vec(0, 0),
                      'armor': 16,
                      'materials': {'steel ingot': 5, 'leather strips': 1}, 'upgrade': {'steel ingot': 2, 'leather strips': 1},
                      'weight': 6}
WEAPONS['steel mace'] = {'type': 'mace','gun': False, 'value': 350,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 25,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 12,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 9,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'steel ingot': 3}, 'upgrade': {'steel ingot': 2},
                      'weight': 7}
WEAPONS['steel dagger'] = {'type': 'dagger','gun': False, 'value': 100,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 50,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 5,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 6,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 10,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'steel ingot': 1}, 'upgrade': {'steel ingot': 1},
                      'weight': 0.5}
WEAPONS['iron dagger'] = {'type': 'dagger','gun': False, 'value': 75,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 50,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 5,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 4,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 11,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'iron ingot': 1}, 'upgrade': {'iron ingot': 1},
                      'weight': 1.5}
WEAPONS['bronze dagger'] = {'type': 'dagger','gun': False, 'value': 75,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 50,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 5,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 4,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 0,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'bronze ingot': 1}, 'upgrade': {'bronze ingot': 1},
                      'weight': 0.8}
WEAPONS['enchanted elven dagger'] = {'type': 'dagger','gun': False, 'value': 100,
                      'bullet_speed': 450,
                      'bullet_lifetime': 300,
                      'magazine size': 20,
                      'reload speed': 1,
                      'rate': 50,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 5,
                      'spread': 1,
                      'damage': 10,
                      'melee damage': 6,
                      'bullet_size': 'lg2',
                      'bullet_count': 1,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 0,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'upgrade': {'bronze ingot': 1, 'tin ingot':1},
                      'weight': 0.8}
WEAPONS['bronze mace'] = {'type': 'mace','gun': False, 'value': 200,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 20,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 8,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 12,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'bronze ingot': 3}, 'upgrade': {'bronze ingot': 1, 'leather strips': 1},
                      'weight': 5}

WEAPONS['miewdra blade'] = {'type': 'sword','gun': False, 'value': 150,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 200,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 15,
                      'spread': 0,
                      'damage': 5,
                      'melee damage': 18,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 13,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'steel ingot': 2, 'ebony block': 1}, 'upgrade': {'steel ingot': 1, 'ebony block': 1, 'leather strips': 1},
                      'weight': 4}

WEAPONS['bone club'] = {'type': 'mace','gun': False, 'value': 12,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 25,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 8,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 15,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'weight': 3}
WEAPONS['queen ant leg'] = {'type': 'sword','gun': False, 'value': 100,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 200,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 15,
                      'spread': 0,
                      'damage': 4,
                      'melee damage': 15,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 16,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'weight': 1}
WEAPONS['ancient viking sword'] = {'type': 'sword','gun': False, 'value': 120,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 200,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 12,
                      'spread': 0,
                      'damage': 4,
                      'melee damage': 14,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'PUNCH',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 17,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'upgrade': {'steel ingot': 3},
                      'weight': 6}
WEAPONS['oar'] = {'type': 'mace','gun': False,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 25,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 2,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 19,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'weight': 20}
WEAPONS['pickaxe'] = {'type': 'pickaxe','gun': False, 'value': 75,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 20,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 12,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 26,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'iron ingot': 2, 'wood block': 1}, 'upgrade': {'iron ingot': 1, 'wood block': 1},
                      'weight': 10}

WEAPONS['wood cutting axe'] = {'type': 'axe','gun': False, 'value': 70,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 20,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 13,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 31,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'iron ingot': 2, 'wood block': 1}, 'upgrade': {'iron ingot': 1, 'wood block': 1},
                      'weight': 8}

WEAPONS['iron battle axe'] = {'type': 'axe','gun': False, 'value': 120,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 30,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 18,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 28,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'iron ingot': 3}, 'upgrade': {'iron ingot': 1, 'leather strips': 1},
                      'weight': 7}

WEAPONS['steel battle axe'] = {'type': 'axe','gun': False, 'value': 175,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 30,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 18,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 30,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'steel ingot': 3, 'leather strips': 1}, 'upgrade': {'steel ingot': 1, 'leather strips': 1},
                      'weight': 5}

WEAPONS['long battle axe'] = {'type': 'axe','gun': False, 'value': 220,
                      'bullet_speed': 0,
                      'bullet_lifetime': 0,
                      'magazine size': 0,
                      'reload speed': 1,
                      'rate': 300,
                      'auto': False,
                      'kickback': 0,
                      'knockback': 30,
                      'spread': 0,
                      'damage': 0,
                      'melee damage': 45,
                      'bullet_size': 'sm1',
                      'bullet_count': 0,
                      'walk': 'WALK',
                      'melee animation': 'SWIPE',
                      'grip': 'CP_SWORD_GRIP',
                      'image': 30,
                      'offset': vec(0, 0),
                      'armor': 0,
                      'materials': {'steel ingot': 3, 'iron ingot': 2, 'leather strips': 2}, 'upgrade': {'steel ingot': 2, 'leather strips': 1},
                      'weight': 9}

UPGRADED_WEAPONS = {}


