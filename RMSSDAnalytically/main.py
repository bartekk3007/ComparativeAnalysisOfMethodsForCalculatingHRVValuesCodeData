import pandas as pd
import numpy as np
from scipy.signal import find_peaks

# Wczytaj dane z pliku (zakładamy: kolumna 0 = czas [s], kolumna 1 = napięcie [mV])
df = pd.read_csv('ecg_fragment.csv', header=None)
czas = df.iloc[:, 0]
napiecie = df.iloc[:, 1]

# Wykryj załamki R (szczyty sygnału)
# Wysokość i odstęp muszą być dobrane empirycznie do Twojego sygnału
peaks, _ = find_peaks(napiecie, height=0.5, distance=150)

# Oblicz czasy uderzeń serca
czasy_uderzen = czas.iloc[peaks].values

# Oblicz odstępy RR (w milisekundach)
rr = np.diff(czasy_uderzen) * 1000  # różnice czasu w ms

# Oblicz RMSSD
rmssd = np.sqrt(np.mean(np.square(np.diff(rr))))

print(f"RMSSD: {rmssd:.2f} ms")