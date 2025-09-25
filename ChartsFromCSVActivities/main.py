import pandas as pd
import matplotlib.pyplot as plt
import os

# Wczytaj dane z CSV
df = pd.read_csv("output.csv")

# Lista unikalnych aktywności
activities = df['Aktywność'].unique()

# Lista unikalnych algorytmów
algorithms = df['Algorytm'].unique()

# Folder do zapisu wykresów
output_folder = "wykresy_angielski"
os.makedirs(output_folder, exist_ok=True)

# Pętla po aktywnościach
for activity in activities:
    plt.figure(figsize=(10, 6))

    if activity == "Spoczynek":
        activity_en = "Resting"
    elif activity == "Spacer":
        activity_en = "Walking"
    elif activity == "Sen":
        activity_en = "Sleep"

    # Filtrujemy dane dla danej aktywności
    df_activity = df[df['Aktywność'] == activity]

    # Pętla po algorytmach
    for alg in algorithms:
        df_alg = df_activity[df_activity['Algorytm'] == alg]
        plt.plot(df_alg['Seria'], df_alg['Mean RR'], marker='o', label=alg)

    plt.title(f"Mean RR - {activity_en}")
    plt.xlabel("Series")
    plt.ylabel("Mean RR Value")
    plt.legend()
    plt.grid(True)

    # Zapis wykresu do pliku PNG
    filename = os.path.join(output_folder, f"{activity}_MeanRR.png")
    plt.savefig(filename)

    plt.show()
    plt.close()

    print(f"Wykres zapisano jako {filename}")
