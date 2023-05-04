import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color = fur_color.to_list()
gray = []
cinnamon = []
black = []
for color in fur_color:
    if color == "Gray":
        gray.append(color)
    elif color == "Cinnamon":
        cinnamon.append(color)
    elif color == "Black":
        black.append(color)
# print(len(cinnamon))
# print(len(black))
# print(len(gray))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [len(gray), len(cinnamon), len(black)]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Squirrel Count.csv")
