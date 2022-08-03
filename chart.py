import pandas
import matplotlib
import matplotlib.pyplot as plt
import warnings
from pyodide import create_proxy

warnings.simplefilter(action='ignore', category=FutureWarning)


def main(e):

    page = Element("sectionheader").element.innerHTML

    if (page == "Population Data"):
        df = pandas.read_csv("./populationsmain.csv",  ",")
    elif (page == "GDP Data"):
        df = pandas.read_csv("./gdpdata.csv",  ",")
    elif (page == "GDP Per Capita Data"):
        df = pandas.read_csv("./gdppercapitadata.csv",  ",")
    elif (page == "GDP Per Capita PPP Data"):
        df = pandas.read_csv("./gdppercapitapppdata.csv",  ",")


    selectElThree = Element('selectThree').value 
    yearInput = Element('selectFour').value  
    countryInput = Element('selectFive').value
    
    yearInputInt = int(yearInput)

    previousYear = str(yearInputInt - 1)
    nextYear = str(yearInputInt + 1)

    chartMain = Element('chartmain')
    chartMain.clear()

    shape = Element('shape')
    shape.clear()

    if (selectElThree == '0'):
        if (yearInputInt == 2020):
            pyscript.write('chartmain', df[["Country Name", previousYear, yearInput]])
            pyscript.write('shape', "Shape: " + str(df[["Country Name", previousYear, yearInput]].shape))
        elif (yearInputInt == 1960):
            pyscript.write('chartmain', df[["Country Name", yearInput, nextYear]])
            pyscript.write('shape', "Shape: " + str(df[["Country Name", yearInput, nextYear]].shape))
        else:
            pyscript.write('chartmain', df[["Country Name", previousYear, yearInput, nextYear]])
            pyscript.write('shape', "Shape: " + str(df[["Country Name", previousYear, yearInput, nextYear]].shape)) 

    if (selectElThree == '1'):
        if (yearInputInt == 2020):
            pyscript.write('chartmain', df.nlargest(10, yearInput)[["Country Name", previousYear, yearInput]])
            pyscript.write('shape', "Shape: " + str(df.nlargest(10, yearInput)[["Country Name", previousYear, yearInput]].shape)) 
        elif (yearInputInt == 1960):
            pyscript.write('chartmain', df.nlargest(10, yearInput)[["Country Name", yearInput, nextYear]])
            pyscript.write('shape', "Shape: " + str(df.nlargest(10, yearInput)[["Country Name", yearInput, nextYear]].shape))
        else:
            pyscript.write('chartmain', df.nlargest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]])
            pyscript.write('shape', "Shape: " + str(df.nlargest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]].shape))

    if (selectElThree == '2'):
        if (yearInputInt == 2020):
            pyscript.write('chartmain', df.nsmallest(10, yearInput)[["Country Name", previousYear, yearInput]])
            pyscript.write('shape', "Shape: " + str(df.nsmallest(10, yearInput)[["Country Name", previousYear, yearInput]].shape))
        elif (yearInputInt == 1960):
            pyscript.write('chartmain', df.nsmallest(10, yearInput)[["Country Name", yearInput, nextYear]])
            pyscript.write('shape', "Shape: " + str(df.nsmallest(10, yearInput)[["Country Name", yearInput, nextYear]].shape))
        else:
            pyscript.write('chartmain', df.nsmallest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]])
            pyscript.write('shape', "Shape: " + str(df.nsmallest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]].shape))
    if (selectElThree == '3'):
        pyscript.write('chartmain', df.loc[[int(countryInput), 200], ["Country Name", yearInput]]) 
        pyscript.write('shape', "Shape: " + str(df.loc[[int(countryInput), 200], ["Country Name", yearInput]].shape))

    if (selectElThree == '4'):
        amountInput = Element('amountinput').value
        pyscript.write('chartmain', df.loc[df[yearInput] > int(amountInput)][["Country Name", yearInput]])
        pyscript.write('shape', "Shape: " + str(df.loc[df[yearInput] > int(amountInput)][["Country Name", yearInput]].shape))
    if (selectElThree == '5'):
        amountInput = Element('amountinput').value
        pyscript.write('chartmain', df.loc[df[yearInput] < int(amountInput)][["Country Name", yearInput]])
        pyscript.write('shape', "Shape: " + str(df.loc[df[yearInput] < int(amountInput)][["Country Name", yearInput]].shape))
    

button = document.getElementById("buttoninput")
button.addEventListener("click", create_proxy(main))




