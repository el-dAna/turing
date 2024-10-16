# import all the necessary modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the data
df = pd.read_csv("flight.csv")

# Analyse the dataframe
print(df.head(5))
print(df.info())
print(df.describe())

# Find out the null values and fill if any
print(data.isnull().sum())

# Find out the null values and fill them if any
data = df.fillna(method="ffill")

# Encoding categorical variables
le = LabelEncoder()
categorical_columns = ["Airline", "Origin", "Destination"]
for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

# Split the data into training and testing set
X = data.drop("Is_Delayed", axis=1)
y = data["Is_Delayed"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a classifier using sklearn
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")
