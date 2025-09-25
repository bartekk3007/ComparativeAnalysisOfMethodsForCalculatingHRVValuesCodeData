import pandas as pd
import glob
import os

plikiAnomalie = ["0.csv", "10.csv", "22.csv", "26.csv", "40.csv", "42.csv", "45.csv", "68.csv", "72.csv", "73.csv", "84.csv"]
plikiPoprawnr = ["3.csv", "13.csv", "14.csv", "17.csv", "24.csv", "25.csv", "38.csv", "51.csv", "69.csv", "71.csv", "92.csv"]

files = glob.glob('./*.csv')
for file in files:
    file_name = os.path.basename(file)
    df = pd.read_csv(file_name, sep=';')  # Jeśli masz średniki
    y_true = []
    test = []
    if file_name in plikiAnomalie:
        for x in df["train_test"]:
            if x == "prediction":
                y_true.append(1)
                test.append(1)
            elif x == "train":
                y_true.append(0)
                test.append(0)
        df["label"] = y_true
    elif file_name in plikiPoprawnr:
        for x in df["train_test"]:
            if x == "prediction":
                y_true.append(0)
                test.append(1)
            elif x == "train":
                y_true.append(0)
                test.append(0)
        df["label"] = y_true