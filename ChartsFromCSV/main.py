import pandas as pd
import matplotlib.pyplot as plt
import os

# Wczytaj dane z CSV
df = pd.read_csv("output2.csv")

# Sprawdź dane
print(df.head())

activity_name = "Mieszane"
activity_name_en = "Mixed Activity"

# Lista unikalnych algorytmów
algorithms = df['Algorytm'].unique()

# Wykres
plt.figure(figsize=(10,6))

for alg in algorithms:
    # Wybierz dane dla konkretnego algorytmu
    df_alg = df[df['Algorytm'] == alg]
    # Rysuj linię: seria (x) vs Mean RR (y)
    plt.plot(df_alg['Seria'], df_alg['Mean RR'], marker='o', label=alg)

plt.title(f"Mean RR - {activity_name_en}")
plt.xlabel("Series")
plt.ylabel("Mean RR Value")
plt.legend()
plt.grid(True)

filename = f"{activity_name}_MeanRR"
plt.savefig(os.path.join(f"{filename}.png"))

plt.show()
plt.close()
print(f"Wykres zapisano jako {filename}")