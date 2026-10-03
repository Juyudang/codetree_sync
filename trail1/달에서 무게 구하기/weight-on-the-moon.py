choo = 13
moon_gra = 0.165

# print(choo * moon_gra)
def my_compute(choo, moon_gra):
    res = choo * moon_gra
    print(f"{choo} * {moon_gra:.6f} = {res:.6f}")

my_compute(choo, moon_gra)