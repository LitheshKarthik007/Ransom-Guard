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


choice = input("Enter 1 for Ransomware or 2 for Benign: ")


if choice == "1":
    sample = ransomware_rows.iloc[[0]]

elif choice == "2":
    sample = benign_rows.iloc[[0]]

else:
    print("Invalid choice")
    exit()


sample = sample.drop(["Class", "Category"], axis=1)


prediction, confidence, risk = predict_ransomware(
    model, sample
)


print("Prediction:", prediction)
print("Confidence:", confidence, "%")
print("Risk Level:", risk)

if risk == "HIGH":
    print("WARNING: Potential ransomware activity detected!")
    print("Early threat alert triggered.")

elif risk == "MEDIUM":
    print("WARNING: Suspicious activity detected!")
    print("Further investigation is recommended.")

else:
    print("No immediate ransomware threat detected.")