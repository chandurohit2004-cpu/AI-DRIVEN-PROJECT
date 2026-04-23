# Selecting the features (input) and the target variable (output to predict)
features = ['Attendance (%)', 'Internal_Marks', 'External_Marks', 'Backlogs']
X = df[features]
y = df['Target_Grade']

# Splitting data and training a Decision Tree Classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Generating predictions and evaluating accuracy
predictions = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions)}")

# Why it's important: This shows your AI capabilities. 
# You aren't just displaying data; you are using Scikit-Learn to train an algorithm to predict student success based on historical features.
