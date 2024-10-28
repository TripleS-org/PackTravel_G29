import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

class RideDemandPredictor:
    def __init__(self, model_path='ride_demand_model.pkl'):
        self.model_path = model_path
        self.model = None
        self.is_trained = False

    def load_data(self, file_path):
        data = pd.read_csv(file_path)
        data['time_of_day'] = pd.to_datetime(data['time_of_day']).dt.hour
        data['location'] = data['location'].astype('category').cat.codes
        return data

    def train_model(self, data):
        X = data[['time_of_day', 'location']]
        y = data['ride_demand']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f'Model Mean Squared Error: {mse:.2f}')

        joblib.dump(self.model, self.model_path)
        self.is_trained = True

    def load_model(self):
        self.model = joblib.load(self.model_path)
        self.is_trained = True

    def predict_demand(self, time_of_day, location):
        if not self.is_trained:
            raise Exception("Model is not trained. Call 'train_model' or 'load_model' first.")

        input_data = pd.DataFrame([[time_of_day, location]], columns=['time_of_day', 'location'])
        demand_prediction = self.model.predict(input_data)
        return demand_prediction[0]

if __name__ == "__main__":
    predictor = RideDemandPredictor()
    historical_data_path = 'historical_data.csv'
    data = predictor.load_data(historical_data_path)

    train_model_flag = False

    if train_model_flag:
        predictor.train_model(data)
    else:
        predictor.load_model()

    time_of_day = 8
    location = 0
    prediction = predictor.predict_demand(time_of_day, location)

    print(f"Predicted ride demand for time {time_of_day}:00 and location code {location} is: {prediction}")
