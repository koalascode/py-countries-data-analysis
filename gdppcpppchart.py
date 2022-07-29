import pandas
import matplotlib
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


df = pandas.read_csv("./gdppercapitapppdata.csv",  ",")

selectElThree = Element('selectThree').value 
yearInput = Element('selectFour').value  
countryInput = Element('selectFive').value

yearInputInt = int(yearInput)

previousYear = str(yearInputInt - 1)
nextYear = str(yearInputInt + 1)

if (selectElThree == '0'):
    if (yearInputInt == 2020):
        pyscript.write('chartmain', df[["Country Name", previousYear, yearInput]])
    elif (yearInputInt == 1960):
        pyscript.write('chartmain', df[["Country Name", yearInput, nextYear]])
    else:
        pyscript.write('chartmain', df[["Country Name", previousYear, yearInput, nextYear]])

if (selectElThree == '1'):
    if (yearInputInt == 2020):
        pyscript.write('chartmain', df.nlargest(10, yearInput)[["Country Name", previousYear, yearInput]])
    elif (yearInputInt == 1960):
        pyscript.write('chartmain', df.nlargest(10, yearInput)[["Country Name", yearInput, nextYear]])
    else:
        pyscript.write('chartmain', df.nlargest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]])

if (selectElThree == '2'):
    if (yearInputInt == 2020):
        pyscript.write('chartmain', df.nsmallest(10, yearInput)[["Country Name", previousYear, yearInput]])
    elif (yearInputInt == 1960):
        pyscript.write('chartmain', df.nsmallest(10, yearInput)[["Country Name", yearInput, nextYear]])
    else:
        pyscript.write('chartmain', df.nsmallest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]])
if (selectElThree == '3'):
    pyscript.write('chartmain', df.loc[[int(countryInput), 200], ["Country Name", yearInput]])
    #Change out the int(countryInput) + 1 to a row with all the means

