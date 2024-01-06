import csv 
import pandas

# with open("CSV and Pandas\Practice\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

def CtoF(celsius):
    return (celsius * 9/5) + 32

data = pandas.read_csv("CSV and Pandas\Practice\weather_data.csv")
# print(data["temp"])
# print(data.temp)

data_dict = data.to_dict()
# print(data_dict)

temp_list = data.temp.to_list()
# print(temp_list)
# print(f"The average temp is {round(data.temp.mean())}")
# print(f"The highest temp is {data.temp.max()}")
high_temp = data[data.temp == data.temp.max()].day
# print(high_temp)

monday = data[data.day == "Monday"]
# print(CtoF(monday.temp))

new_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(new_dict)
new_data.to_csv(r"CSV and Pandas\Practice\new_data.csv")
print(new_data)


