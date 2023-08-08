"""with open("weather_data.csv") as file:
    list_of_lines = file.readlines()

print(list_of_lines)


import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        new_temp = row[1]
        if new_temp != "temp":
            temperatures.append(int(new_temp))

print(temperatures)
"""
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(type(data))
#print(data)
print(type((data["temp"])))

data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].tolist()
print(temp_list)


average = sum(temp_list) / len(temp_list)
print(average)

#the same with pandas
print(data["temp"].mean())

print(data["temp"].max())

# Get data by column
print(data["condition"])

print(data.condition)

#get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32

#Create a DataFrame
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}

data2 = pd.DataFrame(data_dict)
print(data2)
data2.to_csv("new_file.csv")

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
unique_color_counts = squirrel_data.value_counts(subset="Primary Fur Color")
print(unique_color_counts)
#print(squirrel_data)
#gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"].count()
#cinnamon_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"].count()
#black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"].count()
#print(gray_squirrels)
unique_color_counts.to_csv("squirrels_colors.csv")
