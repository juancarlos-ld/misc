
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import csv

def get_data():
    '''
    Get data from a CSV file
    '''
    with open("$HOME/weather.csv") as file:
        reader = csv.reader(file,delimiter=",")
        weather_data = list()
        for row in reader:
            weather_data.append(row)
    return weather_data

def split_axis(weather_data):
    '''
    Split dates and max temp in two different vectors
    so it can be graphed
    '''
    x_axis = list()
    y_axis = list()
    for day in weather_data:
            x_axis.append(day[0])
            #convert strings to float before appending it to the array
            y_axis.append(float(day[1]))
    return x_axis, y_axis

def color_scheme(y_axis):
    '''
    Creates an array of colors based on 
    a temperature range 
    '''

    cc = ['colors']  * len(y_axis)

    for a in range(0,len(y_axis)):
        if y_axis[a] <= 0:
            cc[a] = 'blue'
        elif (y_axis[a] > 0) and (y_axis[a] < 10):
            cc[a] = 'royalblue'
        elif (y_axis[a] >= 10) and (y_axis[a] < 15):
            cc[a] = 'lightgreen'
        elif (y_axis[a] >= 15) and (y_axis[a] < 20):
            cc[a] = 'green'
        elif (y_axis[a] >= 20) and (y_axis[a] < 25):
            cc[a] = 'gold'
        elif (y_axis[a] >= 25) and (y_axis[a] < 30):
            cc[a] = 'salmon'
        elif (y_axis[a] >= 30) and (y_axis[a] < 35):
            cc[a] = 'red'
        elif (y_axis[a] >= 35):
            cc[a] = 'darkred'
    return cc

def plot_data(x_axis, y_axis, cc):
    '''
    Print values and alongside with its color code
    '''
    plt.bar(x_axis, y_axis, color = cc)
    plt.show()

def main():
    '''
    Program to graph the weather on a region
    based on a CSV file which has date and max temp
    '''
    weather = get_data()
    x_axis, y_axis = split_axis(weather)
    color_code = color_scheme(y_axis)
    plot_data(x_axis, y_axis, color_code)
    
if __name__ == '__main__':
    main()
