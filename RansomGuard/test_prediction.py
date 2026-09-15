import pandas as pd
from predict import model, predict_ransomware


data = pd.read_csv("Obfuscated-MalMem2022.csv")


ransomware_rows = data[
    data["Category"].str.contains(
        "Ransomware", case=False, na=False
    )
]


benign_rows = data[
    data["Category"] == "Benign"
]


ransomware_sample = ransomware_rows.iloc[[0]]
benign_sample = benign_rows.iloc[[0]]


ransomware_sample = ransomware_sample.drop(
    ["Class", "Category"], axis=1
)

benign_sample = benign_sample.drop(
    ["Class", "Category"], axis=1
)


prediction, confidence, risk = predict_ransomware(
    model, ransomware_sample
)

print("Ransomware Sample")
print("Prediction:", prediction)
print("Confidence:", confidence, "%")
print("Risk Level:", risk)


prediction, confidence, risk = predict_ransomware(
    model, benign_sample
)

print("\nBenign Sample")
print("Prediction:", prediction)
print("Confidence:", confidence, "%")
print("Risk Level:", risk)