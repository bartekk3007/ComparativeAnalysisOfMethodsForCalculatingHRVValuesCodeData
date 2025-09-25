import pandas as pd

# wczytaj CSV
df = pd.read_csv("Mieszane_U-Net.csv")

# ostatnie dwa wiersze to "Średnia" i "Odch. std"
mean_row = df.iloc[-2]
std_row = df.iloc[-1]

# dane numeryczne do sprawdzania (tylko pierwsze 10 wierszy)
data = df.iloc[0:10].copy()

# dla każdej kolumny od 1 do końca (pomijamy "Seria")
for col in df.columns[1:]:
    mean_val = mean_row[col]
    # oblicz odległość od średniej
    diffs = (data[col] - mean_val).abs()
    idx_closest = diffs.idxmin()
    # podmień wartość na boldowaną
    data.loc[idx_closest, col] = f"\\textbf{{{data.loc[idx_closest, col]}}}"

# doklej średnią i odchylenie
final = pd.concat([data, df.iloc[-2:]], ignore_index=True)

# zapisz jako CSV do LaTeXa
final.to_csv("Mieszane_U-Net.csv", index=False)
