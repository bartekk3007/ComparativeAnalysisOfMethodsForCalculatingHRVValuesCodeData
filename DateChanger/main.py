import os
import time
import datetime

# 🔧 ZMIEŃ TE WARTOŚCI
PLIK = r"C:\Users\48571\OneDrive\Obrazy\PowiatyMapaKibice.jpg"   # Ścieżka do pliku
NOWA_DATA = "2025-08-18 19:30:00"         # Nowa data modyfikacji (YYYY-MM-DD HH:MM:SS)

def set_modification_time(path, dt_str):
    # Zamieniamy tekst na timestamp (sekundy od epoki)
    dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(dt.timetuple())

    # Pobieramy aktualny czas dostępu, żeby go nie zmieniać
    stat = os.stat(path)
    atime = stat.st_atime  # czas dostępu (zostaje ten sam)

    # Ustawiamy nowy czas modyfikacji
    os.utime(path, (atime, timestamp))
    print(f"✅ Zmieniono datę modyfikacji pliku: {path} → {dt}")

if __name__ == "__main__":
    set_modification_time(PLIK, NOWA_DATA)
