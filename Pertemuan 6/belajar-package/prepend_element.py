names = [    
        'Mikasa Akcerman'
        'Armin Arlert'
        'Eren Yeager'
        'Zeke Yeager'
        'Reiner Braun'
        'Annie Leonhart'
]

names = ('Jean Kirstein',*names)
print(names)

names = ('Jean Kirstein',*names)
print(f"type:{type(names).__name__}")

names2 = ['Jean Kirstein',*names]
print(f"type:{type(names2).__name__}")

names3 = {'Jean Kirstein',*names}
print(f"type:{type(names3).__name__}")

