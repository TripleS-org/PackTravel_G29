from cab_model.predict import predict_price

def return_price(distance, date_and_time):
    p = predict_price(distance, date_and_time)
    return p.generate_data_return_price()