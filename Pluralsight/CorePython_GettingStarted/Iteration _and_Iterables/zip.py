sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]

for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print("average =", (sun + mon) / 2)

tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for temps in zip(sunday, monday, tuesday):
    print(f"min = {min(temps):4.1f}, max={max(temps):4.1f}, average={sum(temps) / len(temps):4.1f}")