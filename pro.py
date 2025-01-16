# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the credit card transaction dataset
data = pd.read_csv(r"C:\Users\prate\Desktop\creditcard.csv")

# Preprocessing: handle missing values, scale features, etc.
# For simplicity, preprocessing steps are not included in this example

# Split data into features and target variable
X = data.drop('Class', axis=1)
y = data['Class']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Evaluate model performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Real-time monitoring (mock implementation)
def monitor_transactions(new_transactions):
    # Preprocess new transactions
    # For simplicity, preprocessing steps are not included in this example

    # Make predictions on new transactions
    new_predictions = clf.predict(new_transactions)

    # Flag potential fraud in real-time
    for i, prediction in enumerate(new_predictions):
        if prediction == 1:
            print(f"Potential fraud detected in transaction {i+1}.")

# Example usage: monitor new transactions in real-time
new_transactions = pd.read_csv('new_transactions.csv')
monitor_transactions(new_transactions)
