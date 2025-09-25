import pandas as pd
import numpy as np

# Wczytaj dane
df = pd.read_csv('ecg_fragment.csv')  # zamień na swoją nazwę pliku
# Wyciągnij kolumnę napięcia
napiecie = df.iloc[:, 1]  # lub df.iloc[:, 1] jeśli kolumny nie mają nazw
# Oblicz średnią
srednia = np.mean(napiecie)
# Oblicz RMSD
rmsd = np.sqrt(np.mean((napiecie - srednia) ** 2))
print(f"RMSD napięcia: {rmsd:.3f} mV")