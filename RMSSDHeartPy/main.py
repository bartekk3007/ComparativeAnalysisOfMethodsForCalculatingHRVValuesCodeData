import heartpy as hp
import pandas as pd

df = pd.read_csv("ecg_fragment.csv", header=None)
sygnal = df.iloc[:, 1].values
czas = df.iloc[:, 0].values

# Oblicz częstotliwość próbkowania
sample_rate = int(1 / (czas[1] - czas[0]))

# Przetwórz sygnał
wd, m = hp.process(sygnal, sample_rate)

print(f"RMSSD: {m['rmssd']:.2f} ms")