import pandas as pd
from prophet import Prophet

# Initialize model once
prophet = Prophet()
# NOTE: You must fit prophet with data — this is just an example
# prophet.fit(df)  # Fit it with real data

def forecast_future():
    future = prophet.make_future_dataframe(periods=30)
    forecast = prophet.predict(future)
    return forecast[['ds', 'yhat']].to_dict(orient='records')
