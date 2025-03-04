import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def load_data_from_csv(file_path):
    # Load the dataset
    df = pd.read_csv(file_path, parse_dates=["Date"])
    
    # Ensure the data contains required columns
    required_columns = {"Date", "Temperature", "Humidity", "Energy_Consumption"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The dataset must contain the following columns: {required_columns}")
    
    return df

def train_model(df):
    # Feature Engineering
    df["Day_of_Week"] = df["Date"].dt.dayofweek
    df["Month"] = df["Date"].dt.month
    features = ["Temperature", "Humidity", "Day_of_Week", "Month"]

    # Split the data into training and testing sets
    X = df[features]
    y = df["Energy_Consumption"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

    # Train the XGBoost model
    model = XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)

    return model, X_train, X_test, y_train, y_test

def evaluate_model(model, X_test, y_test, df, X_train):
    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("Model Evaluation:")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    # Plot the actual vs predicted energy consumption
    plt.figure(figsize=(10, 6))
    plt.plot(df["Date"].iloc[len(X_train):], y_test.values, label="Actual", color="blue")
    plt.plot(df["Date"].iloc[len(X_train):], y_pred, label="Predicted", color="red", linestyle="--")
    plt.title("Energy Consumption Prediction")
    plt.xlabel("Date")
    plt.ylabel("Energy Consumption")
    plt.legend()
    plt.grid()
    plt.show()

def menu():
    print("\nMenu:")
    print("1. Train the model")
    print("2. Evaluate the model")
    print("3. Exit")
    return int(input("Enter your choice: "))

def main():
    file_path = input("Enter the path to the CSV file: ")
    df = load_data_from_csv(file_path)
    model, X_train, X_test, y_train, y_test = None, None, None, None, None

    while True:
        choice = menu()
        if choice == 1:
            model, X_train, X_test, y_train, y_test = train_model(df)
            print("Model trained successfully.")
        elif choice == 2:
            if model is not None:
                evaluate_model(model, X_test, y_test, df, X_train)
            else:
                print("Please train the model first.")
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
