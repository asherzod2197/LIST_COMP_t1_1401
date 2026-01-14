sozlar = ["olma", "banan", "anor"]
uzunliklar = [len(s) for s in sozlar]
print(uzunliklar)

sonlar = [1, 3, 5, 6, 9, 10, 12]
uchga_bolinadiganlar = [x for x in sonlar if x % 3 == 0]
print(uchga_bolinadiganlar)
