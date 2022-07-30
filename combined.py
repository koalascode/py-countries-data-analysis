#Aaron Anidjar

import pandas
import matplotlib
import matplotlib.pyplot as plt
import warnings

import os
from matplotlib import font_manager as fm


warnings.simplefilter(action='ignore', category=FutureWarning)

df = pandas.read_csv("./gdppercapitadata.csv",  ",")
df2 = pandas.read_csv("./gdppercapitapppdata.csv",  ",")

fig, ax = plt.subplots()

fpath = "./Lato-Black.ttf"
prop = fm.FontProperties(fname = fpath)

fpath2 = "./Lato-Regular.ttf"
prop2 = fm.FontProperties(fname = fpath2)


selectElOne = Element('selectOne').value
selectElTwo = Element('selectTwo').value 

gdppcCheck = Element('gdppcselect').element.checked
gdppcpppCheck = Element('gdppcpppselect').element.checked

countryOne = int(selectElOne)
countryTwo = int(selectElTwo)

populationOne = []
populationTwo = []

yearsOne = []
yearsTwo = []

populationThree = []
populationFour = []

yearsThree = []
yearsFour = []

if (gdppcCheck == True):
    for i in range(1960, 2021):
        num = str(i)
        populationOne.append(df.iloc[countryOne][num])
        populationTwo.append(df.iloc[countryTwo][num])

        yearsOne.append(i)
        yearsTwo.append(i)

    plt.plot(yearsOne, populationOne, marker='.', ls='--', color='g', label=df.iloc[countryOne]["Country Name"])
    plt.plot(yearsTwo, populationTwo,  marker='.', ls='-', color='r', label=df.iloc[countryTwo]["Country Name"])

    plt.xlabel('Year')
    plt.ylabel('$ Current')
    plt.title('Year vs GDP Per Capita')
    plt.legend(loc='lower right')

   

if (gdppcpppCheck == True):
    for i in range(1960, 2021):
        num = str(i)
        populationThree.append(df2.iloc[countryOne][num])
        populationFour.append(df2.iloc[countryTwo][num])
        
        yearsThree.append(i)
        yearsFour.append(i)


    plt.plot(yearsThree, populationThree, marker='.', ls='--', color='y', label=df.iloc[countryOne]["Country Name"] + " PPP")
    plt.plot(yearsFour, populationFour,  marker='.', ls='-', color='b', label=df.iloc[countryTwo]["Country Name"] + " PPP")
    plt.legend(loc='lower right')

ax.set_title("Year vs GDP Per Capita", fontproperties = prop, size=15)
ax.set_xlabel("Year", fontproperties = prop2, size=12)
ax.set_ylabel("$ Current", fontproperties = prop2, size=12)

fig

#pyscript.write('output', len(populationTwo))


#pyscript.write('output', df[df["2020"] > 100000000].nlargest(15, "2020"))
