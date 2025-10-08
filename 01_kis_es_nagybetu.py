"""
1 Kis- és nagybetűssé alakítás - névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),
kisbetűs (pl. email összehasonlításhoz),
csak az első betű nagy (személyes üdvözlésnél).
"""

username = input("Kérek egy nevet a regisztrációhoz:")

nagybetus_szo = username.upper()
kisbetus_szo = username.lower()
kezdobetus_szo = username.capitalize()

print(f"Csupa nagybetűs: {nagybetus_szo}")
print(f"Csupa kicsi betű: {kisbetus_szo}")
print(f"Nagy kezdőbetű: {kezdobetus_szo}")
