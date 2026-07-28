import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(['recordDate'])
    shift = weather.shift(1)
    return weather.loc[(weather['temperature'] > shift['temperature']) & ((weather['recordDate'] - shift['recordDate']).dt.days == 1), ['id']]