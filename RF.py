import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('Crop.csv')

data_cid_label=data.iloc[:,[5,9]]
group_cid_label= data_cid_label.groupby(['Cid','label'])
B1=group_cid_label.first()
index = dict(B1.index)
print('Crop Name and ID -')
print(index)

x = data[['temperature', 'humidity','ph','rainfall','N','P','K']]
y = data['Cid']

temperature=float(input("Enter Temperature:"))
humidity=float(input("Enter humidity:"))
ph=float(input("Enter ph:"))
rainfall=float(input("Enter rainfall:"))
Nvalue=int(input("Enter N-value:"))
Pvalue=int(input("Enter P-value:"))
Kvalue=int(input("Enter K-value:"))

#[22.05,82.5,6.0,170.5,60,40,40]
#[temperature,humidity,ph,rainfall,Nvalue,Pvalue,Kvalue]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#Train Data regressor Model+++++++++++++++++++++++++++
regressor = RandomForestClassifier(n_estimators=10, random_state=5)
regressor.fit(X_train, y_train)

print(X_train)
print(y_train)
newtrain = np.hsplit(X_train, 7)
X_trainnew=newtrain[0]
plt.scatter(X_trainnew, y_train, color = 'blue')

#Test Data Model+++++++++++++++++++++++++++
ytest_pred = regressor.predict(X_test)
print(ytest_pred)
newtest = np.hsplit(X_test, 7)
X_testnew=newtest[0]
plt.scatter(X_testnew,ytest_pred,color = 'green')

#['temperature', 'humidity','ph','rainfall','N','P','K']
#Set New predict value+++++++++++++++++++++++++++
newpredicttest = np.array([temperature,humidity,ph,rainfall,Nvalue,Pvalue,Kvalue]).reshape(1, 7)
Ynewtest_pred = regressor.predict(newpredicttest)
pcropval=int(Ynewtest_pred[0])

newptest = np.hsplit(newpredicttest, 7)
X_testnewpredict=newptest[0]
plt.scatter(X_testnewpredict,Ynewtest_pred,color = 'red')


print('Crop ID -',pcropval)
print('Crop Name -',index[pcropval])
print('Model Accuracy - ',accuracy_score(y_test, ytest_pred)*100,'%')

plt.title('Random Forest')
plt.xlabel('temperature')
plt.ylabel('Crop')
plt.show()
