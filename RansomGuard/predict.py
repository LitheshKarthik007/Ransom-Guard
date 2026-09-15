import joblib


model = joblib.load("models/ransomguard_model.pkl")
#load the previously trained model from the saved file

def calculate_risk(prediction,confidence):
    if prediction =="Ransomware":
        if confidence>=80:
            return "HIGH"
        else:
            return "MEDIUM"
    else:
        return "LOW"

def predict_ransomware(model, sample):

    prediction = model.predict(sample)
    #predict whether the smaple is benign or ransomware

    probability = model.predict_proba(sample)
    #get the probability for each possible class


    class_index = model.classes_.tolist().index(prediction[0])
    #find the position of the prediction class in the model's class list

    confidence = probability[0][class_index] * 100


    #determine the risk level based on the predicted class

    risk=calculate_risk(prediction[0],confidence)

    return prediction[0], confidence, risk
