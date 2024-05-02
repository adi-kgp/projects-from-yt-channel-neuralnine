import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from lime import lime_tabular

data = load_breast_cancer()

X, y = data['data'], data['target']

print(X)
print(y)
print(data['target_names'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Decision Tree : inherently explainable
# tree_clf = DecisionTreeClassifier()
# tree_clf.fit(X_train, y_train)

# print(tree_clf.score(X_test, y_test))

# plt.figure(figsize=(20,10))
# plot_tree(tree_clf, filled=True, feature_names=data['feature_names'], class_names=data['target_names'], rounded=True)
# plt.show()

# Random Forests: inherently inexplanable
forest_clf = RandomForestClassifier()
forest_clf.fit(X_train, y_train)

print(forest_clf.score(X_test, y_test))

explainer = lime_tabular.LimeTabularExplainer(
    training_data=X_train, 
    feature_names=data['feature_names'],
    class_names = data['target_names'],
    mode = 'classification'
)

for i in range(20):
    print('Correct: ', 'benign' if y_test[i] else 'malignant')
    print('Classification: ', forest_clf.predict([X_test[i]]))
    print(dict(zip(data['feature_names'], X_test[i])))
    instance = X_test[i]

    explanation = explainer.explain_instance(
        data_row = X_test[i],
        predict_fn = forest_clf.predict_proba,
        num_features = 30
    )

    fig = explanation.as_pyplot_figure()
    plt.tight_layout()
    plt.show()
    
# plt.figure(figsize=(20,10))
# plot_tree(forest_clf, filled=True, feature_names=data['feature_names'], class_names=data['target_names'], rounded=True)
# plt.show()

print(dict(zip(data['feature_names'], forest_clf.feature_importances_))) # how decisions are made is not clear