import pandas as pd
import neurokit2 as nk

# Wczytaj dane (brak nagłówka)
df = pd.read_csv("ecg_fragment.csv", header=None)
sygnal = df.iloc[:, 1].values  # napięcie
czas = df.iloc[:, 0].values    # czas (opcjonalnie)

# Określ częstotliwość próbkowania (Hz) — np. 1000 Hz = 1 ms odstępy
sampling_rate = int(1 / (czas[1] - czas[0])) if len(czas) > 1 else 1000

# Przetwórz sygnał EKG
signals, info = nk.ecg_process(sygnal, sampling_rate=sampling_rate)

# Wyciągnij odstępy RR
rr = signals["ECG_RR_Interval"].dropna().values * 1000  # na ms

# Oblicz RMSSD
rmssd = nk.hrv_time(signals, sampling_rate=sampling_rate)["HRV_RMSSD"].values[0]

print(f"RMSSD: {rmssd:.2f} ms")