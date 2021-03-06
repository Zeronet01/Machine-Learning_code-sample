import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

cancer = load_breast_cancer()
cancer.keys()

#Convert sklearn dataset to a dataframe
data = pd.DataFrame(cancer.data, columns=[cancer.feature_names])
Target = pd.Series(data=cancer.target, index=data.index)

print(data.columns)

#Print data shape
print("Data's shape:\n",data.shape)

#Print class distribution of target variable
print("Class distribution of target variable:\n",
    pd.Series(data=[Target.value_counts().loc[0],Target.value_counts().loc[1]], index=['malignant', 'benign'])
      )

#Split data into train/test
from sklearn.model_selection import train_test_split
X,y = data, Target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#Tarin a KNN model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
a=knn.fit(X_train, y_train)

#Find the mean accuracy of knn classifier
ma = knn.score(X_test,y_test)
print("KNN classifier's accuracy\n",ma)

# How the effect of classifier changes with K
df=pd.DataFrame(data=[],columns=["k","Accuracy"])
for i in range(1,200,5):
    knn = KNeighborsClassifier(n_neighbors = i)
    a = knn.fit(X_train, y_train)
    ma = knn.score(X_test,y_test)
    df.loc[i]=[i,ma]


#Use cross-validation to verify the model effect

from sklearn.model_selection import cross_val_score

df_cv=pd.DataFrame(data=[],columns=["k","Accuracy"])
for i in range(1,50):
    clf = KNeighborsClassifier(n_neighbors = i)
    cv_scores = cross_val_score(clf,X,y,cv=5)
    df_cv.loc[i] = [i, np.mean(cv_scores)]

fig = plt.figure()
plt.scatter(df_cv.k, df_cv.Accuracy)
plt.xlabel("k")
plt.ylabel("Accuracy acore")
plt.title("How Accuracy score changed with k in K-NN")
plt.show()

fig.savefig('plot.png')
