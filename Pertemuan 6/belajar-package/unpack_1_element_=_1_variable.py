names = (
    'Mikasa Ackerman',
    'Armin Arlert',
    'Eren Yeager',
    'Zeke Yeager'
    'Reiner Braun'
    'Annie Leonhart'
)

soldier1,soldier2,deceiver1,*warriors=names
print(soldier1)
print(soldier2)
print(deceiver1)
print(warriors)

soldier1,soldier2,deceiver1,*_=names
print(soldier1)
print(soldier2)
print(deceiver1)
