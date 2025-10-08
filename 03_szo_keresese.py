"""
3️⃣ Szó keresése a szövegben – tartalom ellenőrzés
Feladat: Kérj be egy bejegyzést a közösségi oldalra, majd ellenőrizd, hogy szerepel-e benne a „Python” szó.
"""

user = input("Írj egy bejegyzést amiben szerepel a python szó: ")
output = user.count("python")

print(output)
