import pandas as pd
import glob
import os

# Wybierz wszystkie pliki CSV w katalogu
files = glob.glob("*.csv")   # np. jeśli masz w bieżącym folderze
# jeśli w podfolderze: glob.glob("sciezka/*.csv")

for file in files:
    # Wczytaj plik CSV
    df = pd.read_csv(file)

    # Zamień wartości w kolumnie "Seria"
    df['Seria'] = df['Seria'].replace({
        "Średnia": "Average",
        "Odch. std": "Std Dev"
    })

    # Zmień też nazwę nagłówka kolumny
    df = df.rename(columns={"Seria": "Series"})

    # Zapisz plik z powrotem (możesz nadpisać albo zapisać z inną nazwą)
    new_name = os.path.splitext(file)[0] + ".csv"
    df.to_csv(new_name, index=False)

    print(f"Przetworzono {file} → {new_name}")