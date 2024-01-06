import csv 
import pandas

data = pandas.read_csv(r"CSV and Pandas\Squirrel Practice\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]

num_gray_squirrels = len(gray_squirrels)
num_black_squirrels = len(black_squirrels)
num_red_squirrels = len(red_squirrels)

new_dict = {
    "Fur Colors": ["Gray", "Black", "Red"],
    "Count": [num_gray_squirrels, num_black_squirrels, num_red_squirrels]
}

new_data = pandas.DataFrame(new_dict)
new_data.to_csv(r"CSV and Pandas\Squirrel Practice\new_data.csv")
print(new_data)