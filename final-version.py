# Import Required Library
from tkinter import *
from tkcalendar import Calendar

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor

with open('E:\\STUDY\\STUDY\\11th SEMESTER\\OFFICIAL THESIS\\Test\\test3.csv','r') as f:
    weather_df = pd.read_csv(f, parse_dates=["DATE"])
regRan2 = ""

def calculate():
    global regRan2
    print(weather_df.head())
    print(weather_df.columns)
    print(weather_df.shape)
    print(weather_df.isnull().any())

    weather_df.pop('TMAX')
    weather_df.pop('TMIN')
    weather_df.pop('STATION')
    weather_df.pop('NAME')
    weather_y = weather_df.pop("TAVG")
    weather_df.head()
    train_y = weather_y[0:1560]
    test_y = weather_y[1500:]
    weather_x = weather_df

    train_x = weather_x[0:1560]
    test_x = weather_x[1500:]
    print(train_x.head())

    regRan2 = RandomForestRegressor(max_depth=35, random_state=0, n_estimators=100)
    regRan2.fit(train_x, train_y)

calculate()

def predict(array):
    print(array)
    prediction5 = regRan2.predict(array)
    print(prediction5)
    temp.config(text="Selected Date Temperature : " + str(round(prediction5[0], 2))+u"\N{DEGREE SIGN} Celsius")



root = Tk()


root.geometry("400x400")

root.title("Weather Prediction")
cal = Calendar(root, selectmode='day',
               year=2021, month=5,
               day=22, date_pattern="ddmmyy")
cal.pack(pady=20)






def grad_date():
    print([[int(cal.get_date())]])
    predict([[int(cal.get_date())]])


Button(root, text="Predict Temperature",
       command=grad_date).pack(pady=20)

temp = Label(root, text="")
temp.pack(pady=20)

# Excecute Tkinter
root.mainloop()