
for i in range(100):
    print(f"{i:02d}", end=", " if i < 99 else "\n")
for i in range(99):
    print("Decimal: {}, Hexadecimal: {}".format(i, hex(i)))
