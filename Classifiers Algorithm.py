import numpy as np
from sklearn import  neighbors
from sklearn.model_selection import train_test_split
import DataGenerator

df = DataGenerator.changetoNumbers()
prediction_measures = []

X=np.array(df.drop(['price'], 1))
y = np.array(df['price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier(n_neighbors=21, weights='distance',algorithm="auto",leaf_size=1000,n_jobs=-1)
clf.fit(X_train, y_train)

for i in range(0,2):
    data = DataGenerator.Data()
    prediction_measures.insert(i,data)

prediction = clf.predict(prediction_measures)
accuracy = clf.score(X_train, y_train)
print 'Inputted Values: ' + str(prediction_measures) + '\nPredicted Price: ' +  str(prediction) + '\nAccuracy: ' + str(accuracy)

