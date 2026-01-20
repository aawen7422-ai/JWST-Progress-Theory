import os

# Константы
hbar = 1.054571817e-34
c = 3e8
rho_crit = 9.0e-27
rho_DE = 6.9e-27
Mpc3_to_m3 = 2.938e73

def calculate_dCdt(V_Mpc3, name, f_b=0.1, f_dm=0.15):
    """
    Рассчитывает dC/dt для войда.
    V_Mpc3 - объём в Мпк³
    f_b - доля барионов от критической плотности
    f_dm - доля тёмной материи от критической плотности
    """
    V = V_Mpc3 * Mpc3_to_m3
    rho_total = rho_DE + (f_b + f_dm) * rho_crit
    E = rho_total * V * c**2
    dCdt = E / hbar
    return f"{name}: {dCdt:.2e} с⁻¹"

# Создаём папку, если её нет
os.makedirs("Voids_DarkEnergy", exist_ok=True)

# Рассчитываем для трёх войдов
results = []
results.append(calculate_dCdt(2.36e5, "Войд Волопаса", 0.1, 0.15))
results.append(calculate_dCdt(2.24e7, "Гигантский войд", 0.05, 0.10))
results.append(calculate_dCdt(8.7e7, "Сверхпустота Эридана", 0.3, 0.20))

# Сохраняем в файл
with open("Voids_DarkEnergy/results.txt", "w", encoding="utf-8") as f:
    f.write("РЕЗУЛЬТАТЫ РАСЧЁТА dC/dt ДЛЯ ВОЙДОВ\n")
    f.write("=" * 50 + "\n")
    for line in results:
        f.write(line + "\n")
    f.write("\nМетод: dC/dt = E / ħ, где E = (ρ_DE + ρ_b + ρ_DM) * V * c²")

# Выводим результат в консоль
print("✅ Результаты сохранены в папке 'Voids_DarkEnergy/results.txt'")
print("\n" + "=" * 50)
for line in results:
    print(line)
print("=" * 50)
