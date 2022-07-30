#Aaron Anidjar

import pandas
import matplotlib
import matplotlib.pyplot as plt
import warnings

from matplotlib import font_manager as fm

warnings.simplefilter(action='ignore', category=FutureWarning)

page = Element('sectionheader').element.innerHTML

if (page == "Population Data"):
    df = pandas.read_csv("./populationsmain.csv",  ",")
elif (page == "GDP Data"):
    df = pandas.read_csv("./gdpdata.csv",  ",")
elif (page == "GDP Per Capita Data"):
    df = pandas.read_csv("./gdppercapitadata.csv",  ",")
elif (page == "GDP Per Capita PPP Data"):
    df = pandas.read_csv("./gdppercapitapppdata.csv",  ",")

fig, ax = plt.subplots()

fpath = "./Lato-Black.ttf"
prop = fm.FontProperties(fname = fpath)

fpath2 = "./Lato-Regular.ttf"
prop2 = fm.FontProperties(fname = fpath2)

selectElOne = Element('selectOne').value
selectElTwo = Element('selectTwo').value 

countryOne = int(selectElOne)
countryTwo = int(selectElTwo)

populationOne = []
populationTwo = []

yearsOne = []
yearsTwo = []

for i in range(1960, 2021):
    num = str(i)
    populationOne.append(df.iloc[countryOne][num])
    populationTwo.append(df.iloc[countryTwo][num])

    yearsOne.append(i)
    yearsTwo.append(i)

plt.plot(yearsOne, populationOne, marker='o', ls='--', color='g', label=df.iloc[countryOne]["Country Name"])
plt.plot(yearsTwo, populationTwo,  marker='d', ls='-', color='r', label=df.iloc[countryTwo]["Country Name"])


plt.legend(loc='lower right')

if (page == "Population Data"):
    title = "Year vs Population"
    xlabel = "Year"
    ylabel = "Population"
elif (page == "GDP Data"):
    title = "Year vs GDP"
    xlabel = "Year"
    ylabel = "$ Current"
elif (page == "GDP Per Capita Data"):
    title = "Year vs GDP Per Capita"
    xlabel = "Year"
    ylabel = "$ Current"
elif (page == "GDP Per Capita PPP Data"):
    title = "Year vs GDP Per Capita PPP"
    xlabel = "Year"
    ylabel = "$ Current"

ax.set_title(title, fontproperties = prop, size=15)
ax.set_xlabel(xlabel, fontproperties = prop2, size=12)
ax.set_ylabel(ylabel, fontproperties = prop2, size=12)

fig


#pyscript.write('output', len(populationTwo))


#pyscript.write('output', df[df["2020"] > 100000000].nlargest(15, "2020"))


