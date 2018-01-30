import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import DataGenerator

df = DataGenerator.changetoNumbers()
prediction_measures = []

X=np.array(df.drop(['price'], 1))
y = np.array(df['price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = svm.SVC()
clf.fit(X_train, y_train)

for i in range(0,2):
    data = DataGenerator.Data()
    prediction_measures.insert(i,data)

accuracy = clf.score(X_train, y_train)
prediction = clf.predict(prediction_measures)


print 'Inputted Values: ' + str(prediction_measures) + '\nPredicted Price: ' +  str(prediction) + '\nAccuracy: ' + str(accuracy)
