import pandas
import matplotlib
import matplotlib.pyplot as plt



df = pandas.read_csv("./populationsmain.csv",  ",")
df2 = pandas.read_csv("./populationwithworld.csv",  ",")

selectElThree = Element('selectThree').value 
yearInput = Element('selectFour').value  
countryInput = Element('selectFive').value

yearInputInt = int(yearInput)

previousYear = str(yearInputInt - 1)
nextYear = str(yearInputInt + 1)

if (selectElThree == '0'):
    pyscript.write('chartmain', df[["Country Name", previousYear, yearInput, nextYear]])

if (selectElThree == '1'):
    pyscript.write('chartmain', df.nlargest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]])

if (selectElThree == '2'):
    pyscript.write('chartmain', df.nsmallest(10, yearInput)[["Country Name", previousYear, yearInput, nextYear]])

if (selectElThree == '3'):
    pyscript.write('chartmain', df2.loc[[int(countryInput), 214], ["Country Name", yearInput]])
    #Change out the int(countryInput) + 1 to a row with all the means

