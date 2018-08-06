from sklearn import tree
#[height, weight,shoe size]
x=[[181, 80, 44], [177, 70, 43], [160,60,38], [154,54,37], [166, 65,40], [190,90,47], [175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]
y=['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
h = int(input("height "))
w = int(input("weight "))
s = int(input("shoe size "))
prediction = clf.predict([[h,w,s]])
print(prediction)