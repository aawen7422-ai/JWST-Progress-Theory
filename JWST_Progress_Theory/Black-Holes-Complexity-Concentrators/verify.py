# verify.py
c = 299792458
hbar = 1.054571817e-34
t_pl = 5.391247e-44
M_pl = 2.176434e-8

M = 1.989e30  # масса Солнца

# Расчёт
E = M * c**2
dCdt = E / hbar
P = dCdt * t_pl
mu = P / (M / M_pl)

# Запись в файл
with open("verify_result.txt", "w") as f:
    f.write(f"Масса: {M} кг\n")
    f.write(f"dC/dt = {dCdt:.3e} с⁻¹\n")
    f.write(f"μ = {mu:.3f}")

print("Результат сохранён в verify_result.txt")