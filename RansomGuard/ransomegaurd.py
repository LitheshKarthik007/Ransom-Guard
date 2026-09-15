import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier  # sklearn
                                                         #|___ ensemble  (combines multiple model to make a one strong prediction)
                                                                 #|___randomforestclassifier 

from sklearn.metrics import accuracy_score   #used to calculate how many test predctions were correct
from sklearn.metrics import confusion_matrix # used to detect the mistaked part in the detction (very important for this project) shows the incorrect part in a matrix form 
from sklearn.metrics import precision_score,recall_score,f1_score 
from sklearn.metrics import classification_report # used the display precision,recall and f1_scores
import matplotlib.pyplot as plt
import joblib #often used to save/load trained scikit-leran models

data=pd.read_csv("Obfuscated-MalMem2022.csv")
#print(data.shape)

"""
print(data.columns)     # Shows all column names in the dataset

print(data.head())         # Shows the first 5 rows of the dataset

print(data["Class"].value_counts())  # Counts how many samples belong to each Class

print(data["Category"].value_counts()) # Counts how many samples belong to each Category 

"""

condition=data["Category"].str.contains("Ransomware",case=False,na=False)
#print(data[condition].shape)  #Finds rows where Category contains Ransomware


conditionII=data["Category"]=="Benign"
#print(data[conditionII].shape)  #Finds rows where Category is exactly Benign

#combining the two conditions 

finalcondition=condition | conditionII
new_data=data[finalcondition]
#print(new_data.shape)

new_data=new_data.copy()   # creates an independent copy of the filtered data
new_data["Class"]=new_data["Category"].apply(
    lambda x: "Ransomware" 
         if "Ransomware" in x 
         else "Benign"
)
#print(new_data["Class"].value_counts())   # this one converts the detailed category into our final target either benign or ransomware

 # data splitting process (x and y)

x=new_data.drop(["Class","Category"],axis=1) # axis=0 -> rows and axis=1 -> columns 
# this removes the class and category from the newdata and keeps the remaining part

y=new_data["Class"] #stores the class as the target that we want to predict

#print(x.shape)

#print(y.shape)

# test/train splitting of data 

# x_train -> questions given for practice , y_train ->answer to those practice questions
# x_test -> new exam questions , y_test -> offical answer key 

(x_train , x_test , y_train , y_test) = train_test_split( x,y,
                                                         test_size=0.2,
                                                         random_state=42,
                                                         stratify=y) 
# the randome_state=42 is often used to get the same split every time when we run the project 42 is just a random number any numbe can be used
# stratify=y is often used to say python split the data with the same proportion in both test and train 

"""print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)"""

model=RandomForestClassifier(random_state=42)  # creates a random forest model

model.fit(x_train,y_train)   # model learns the relationship b/w the x_train and y_train to distinguish b/w the output (it teaches the model)

# Save the trained Random Forest model to a file so it can be reused later without retraining
joblib.dump(model,"models/ransomguard_model.pkl")

prediction=model.predict(x_test) # this is used to predict the unseen datas (it takes only one argument)
print(prediction)

accuracy=accuracy_score(y_test,prediction)
print(accuracy)

conmat=confusion_matrix(y_test,prediction)
print(conmat)

precision=precision_score(y_test,prediction,pos_label="Ransomware")
# this is  to calculates how trust worthy are the postive predictions

recal=recall_score(y_test,prediction,pos_label="Ransomware")
#this is to calculate how many actaull threats did the model catch

fscore=f1_score(y_test,prediction,pos_label="Ransomware")
# it is the combination of precision and recall

print("presicion:",precision)
print("recall:",recal)
print("f1_score:",fscore)

print(classification_report(y_test,prediction))

importance=model.feature_importances_
#gets the importance score of each feature from the trained model

print(importance)

feature_importance=pd.DataFrame({
    "Feature":x.columns,
    "Importance":importance
})
#Creates a table showing each feature and its importance score
print(feature_importance)

feature_importance=feature_importance.sort_values("Importance",ascending=False)

top=feature_importance.head(10)
#Select the top 10 most important features

plt.bar(top["Feature"],top["Importance"])
# Create a bar chart

plt.xticks(rotation=90)
# Rotate feature names for better readability

plt.xlabel("Features")
# Set X-axis label

plt.ylabel("Importance")
# Set Y-axis label

plt.title("Top 10 Features for Ransomware Detection")
# Set graph title

plt.tight_layout()
# Adjust the spacing of the graph automatically

plt.show()
# Display the graph in a separate window
