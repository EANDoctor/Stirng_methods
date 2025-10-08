"""
2️⃣ Szóhossz meghatározása – tweet vagy SMS ellenőrzés
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll. Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez.
"""

user = input("Írj be egy üzenetet ")

uzenet = len(user)

print(f"Az üzenetet hossza: {uzenet} karakter")