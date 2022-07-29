import pandas
import matplotlib
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

df = pandas.read_csv("./gdppercapitadata.csv",  ",")


fig, ax = plt.subplots()

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

plt.xlabel('Year')
plt.ylabel('GDP (Current $)')
plt.title('Year vs Population')
plt.legend(loc='lower right')

fig
