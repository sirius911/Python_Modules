t = (19, 42, 21)
string = f"The {len(t)} numbers are: {t[0]}, {t[1]}, {t[2]}"
print(f"The {len(t)} numbers are: ", end = "")
for i in range(0, len(t)):
    print(f"{t[i]}", end = "")
    if i + 1 < len(t):
        print(", ", end = "")
print("")