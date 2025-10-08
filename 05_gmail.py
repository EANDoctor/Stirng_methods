"""
5️⃣ Szó elejének/végének ellenőrzése – email ellenőrzés
Feladat: Kérj be egy email címet a regisztrációhoz, majd ellenőrizd, hogy Gmail-es-e.
"""

user = input("Add meg az email címed!: ")
if "@gmail" in user:
    print("Sikeres regisztráció!")
else:
    print("Az email nem érvényes!")