from typing import Any, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series
import seaborn as sns
import requests

Garda_Station_Stats = pd.read_csv(r"C:\Users\tlyons\Desktop\Python\garda_stations.csv")

#API DATA REQUEST DEMO
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=db8d1f33bc594362a1a9bdcde20de55b')
response = requests.get(url)
print(response.json())


#Showing use of loop to list column names
for col in Garda_Station_Stats.columns:
    print(col)

#drop two columns which are not relevant
GSS = Garda_Station_Stats.drop(columns=['x', 'y'])

#Use of loop to confirm columns were removed
for col in GSS.columns:
    print(col)

print(GSS.head(20))

# Command to sort entire dataframe by Divisions and then Station
GSS_SORTED_DIVISIONS = GSS.sort_values(["Divisions", "Station"])
print(GSS_SORTED_DIVISIONS.head(10))

# Command to view  as grouped by Division
GSS_GROUPBY_DIVISIONS = GSS_SORTED_DIVISIONS.groupby("Divisions")
print(GSS_GROUPBY_DIVISIONS.head(10))


# Reducing entire Databse to a list of Divisions. This shows total Divisions is 29
Num_Divisions = GSS.drop_duplicates(subset=["Divisions"])
DD = Num_Divisions[["Divisions"]]
print(DD.sort_values("Divisions"))


# Creating a  list all Dublin, Galway and Cork Divisions
Dublin = [" D.M.R. Eastern Division", " D.M.R. North Central Division", " D.M.R. Northern Division",
          " D.M.R. South Central Division", " D.M.R. Southern Division", " D.M.R. Western Division"]
Galway = [" Galway Division"]
Cork = [" Cork City Division", " Cork North Division", " Cork West Division"]

#Creating a variable as the subset of GSS for all rows where the Division was included in a my above created lists
Dublin_Crime = GSS[GSS["Divisions"].isin(Dublin)]
Galway_Crime = GSS[GSS["Divisions"].isin(Galway)]
Cork_Crime = GSS[GSS["Divisions"].isin(Cork)]

print(Dublin_Crime)
print(Galway_Crime)
print(Cork_Crime)


# Function to return Drug crime between 2003 and 2015 based on a given list of Division.
# These lists have previously been defined under Dublin_Crime, Galway_Crime, Cork_Crime
def Drug_Crime_peryear(drug_crime):
    drug_crime_Station_Divisions = drug_crime.loc[:, "Station":"Divisions"]

    drug_crime_Drugs_YEARS = drug_crime.iloc[:, 100:113]

    drug_crime_Drugs_Final = pd.concat([drug_crime_Station_Divisions, drug_crime_Drugs_YEARS], axis=1).sort_values(
        ["Divisions", "Station"])

    return drug_crime_Drugs_Final


Dublin_Crime_Drugs_Final = Drug_Crime_peryear(Dublin_Crime)
Galway_Crime_Drugs_Final = Drug_Crime_peryear(Galway_Crime)
Cork_Crime_Drugs_Final = Drug_Crime_peryear(Cork_Crime)

print(Dublin_Crime_Drugs_Final)
print(Galway_Crime_Drugs_Final)
print(Cork_Crime_Drugs_Final)


# Function to return Burglary crime between 2003 and 2015 based on a given list of Divisions.
# These lists have previously been defined under Dublin_Crime, Galway_Crime, Cork_Crime

def Burg_Crime_peryear(burg_crime):
    burg_crime_Station_Divisions = burg_crime.loc[:, "Station":"Divisions"]

    burg_crime_Burg_YEARS = burg_crime.iloc[:, 58:71]

    burg_crime_Burg_Final = pd.concat([burg_crime_Station_Divisions, burg_crime_Burg_YEARS], axis=1).sort_values(
        ["Divisions", "Station"])

    return burg_crime_Burg_Final


Dublin_Crime_Burg_Final = Burg_Crime_peryear(Dublin_Crime)
Galway_Crime_Burg_Final = Burg_Crime_peryear(Galway_Crime)
Cork_Crime_Burg_Final = Burg_Crime_peryear(Cork_Crime)


#Print Iterrows for my 6 Primary Dataframes

for Info in Dublin_Crime_Drugs_Final.iterrows():
    print(Info)

for Info in Galway_Crime_Drugs_Final.iterrows():
    print(Info)

for Info in Cork_Crime_Drugs_Final.iterrows():
    print(Info)

for Info in Dublin_Crime_Burg_Final.iterrows():
    print(Info)

for Info in Galway_Crime_Burg_Final.iterrows():
    print(Info)

for Info in Cork_Crime_Burg_Final.iterrows():
    print(Info)




fig, ax = plt.subplots()
plt.figure(1)
ax.bar(Dublin_Crime_Drugs_Final["Station"], Dublin_Crime_Drugs_Final["Controlled drug offences 2003"], color='r', label="2003")
ax.bar(Dublin_Crime_Drugs_Final["Station"], Dublin_Crime_Drugs_Final["Controlled drug offences 2009"],
        bottom= Dublin_Crime_Drugs_Final["Controlled drug offences 2003"], color='b', label="2009")
ax.bar(Dublin_Crime_Drugs_Final["Station"], Dublin_Crime_Drugs_Final["Controlled drug offences 2015"],
        bottom=  Dublin_Crime_Drugs_Final["Controlled drug offences 2003"] + Dublin_Crime_Drugs_Final["Controlled drug offences 2009"], color='g', label="2015")
plt.xticks(rotation=90)
ax.set_xlabel("Gardai Stations")
ax.set_ylabel("Reported Cases")
ax.set_title("Drug Offense Rates reported in Dublin")
plt.legend()



fig, ax = plt.subplots()
plt.figure(2)
ax.bar(Dublin_Crime_Burg_Final["Station"], Dublin_Crime_Burg_Final["Burglary and related offences 2003"], color='r', label="2003")
ax.bar(Dublin_Crime_Burg_Final["Station"], Dublin_Crime_Burg_Final["Burglary and related offences 2009"],
        bottom=Dublin_Crime_Burg_Final["Burglary and related offences 2003"], color='b', label="2009")
ax.bar(Dublin_Crime_Burg_Final["Station"], Dublin_Crime_Burg_Final["Burglary and related offences 2015"],
        bottom=Dublin_Crime_Burg_Final["Burglary and related offences 2003"] + Dublin_Crime_Burg_Final["Burglary and related offences 2009"], color='g', label="2015")
plt.xticks(rotation=90)
ax.set_xlabel("Gardai Stations")
ax.set_ylabel("Reported Cases")
ax.set_title("Burglary Offense Rates reported in Dublin")
plt.legend()

fig, ax = plt.subplots()
plt.figure(3)
ax.bar(Galway_Crime_Burg_Final["Station"], Galway_Crime_Burg_Final["Burglary and related offences 2003"], color='r', label="2003")
ax.bar(Galway_Crime_Burg_Final["Station"], Galway_Crime_Burg_Final["Burglary and related offences 2009"],
        bottom=Galway_Crime_Burg_Final["Burglary and related offences 2003"], color='b', label="2009")
ax.bar(Galway_Crime_Burg_Final["Station"], Galway_Crime_Burg_Final["Burglary and related offences 2015"],
        bottom=Galway_Crime_Burg_Final["Burglary and related offences 2003"] + Galway_Crime_Burg_Final["Burglary and related offences 2009"], color='g', label="2015")
plt.xticks(rotation=90)
ax.set_xlabel("Gardai Stations")
ax.set_ylabel("Reported Cases")
ax.set_title("Burglary Offense Rates reported in Galway")
plt.legend()

fig, ax = plt.subplots()
plt.figure(4)
ax.bar(Galway_Crime_Drugs_Final["Station"], Galway_Crime_Drugs_Final["Controlled drug offences 2003"], color='r', label="2003")
ax.bar(Galway_Crime_Drugs_Final["Station"], Galway_Crime_Drugs_Final["Controlled drug offences 2009"],
        bottom=Galway_Crime_Drugs_Final["Controlled drug offences 2003"], color='b', label="2009")
ax.bar(Galway_Crime_Drugs_Final["Station"], Galway_Crime_Drugs_Final["Controlled drug offences 2015"],
        bottom=Galway_Crime_Drugs_Final["Controlled drug offences 2003"] + Galway_Crime_Drugs_Final["Controlled drug offences 2009"], color='g', label="2015")
plt.xticks(rotation=90)
ax.set_xlabel("Gardai Stations")
ax.set_ylabel("Reported Cases")
ax.set_title("Drug Offense Rates reported in Galway")
plt.legend()


fig, ax = plt.subplots()
plt.figure(5)
ax.bar(Cork_Crime_Burg_Final["Station"], Cork_Crime_Burg_Final["Burglary and related offences 2003"], color='r', label="2003")
ax.bar(Cork_Crime_Burg_Final["Station"], Cork_Crime_Burg_Final["Burglary and related offences 2009"],
       bottom=Cork_Crime_Burg_Final["Burglary and related offences 2003"], color='b', label="2009")
ax.bar(Cork_Crime_Burg_Final["Station"], Cork_Crime_Burg_Final["Burglary and related offences 2015"],
       bottom=Cork_Crime_Burg_Final["Burglary and related offences 2003"] + Cork_Crime_Burg_Final["Burglary and related offences 2009"], color='g', label="2015")

plt.xticks(rotation=90)
ax.set_xlabel("Gardai Stations")
ax.set_ylabel("Reported Cases")
ax.set_title("Burglary Offense Rates reported in Cork")
plt.legend()



fig, ax = plt.subplots()
plt.figure(6)
ax.bar(Cork_Crime_Drugs_Final["Station"], Cork_Crime_Drugs_Final["Controlled drug offences 2003"], color='r', label="2003")
ax.bar(Cork_Crime_Drugs_Final["Station"], Cork_Crime_Drugs_Final["Controlled drug offences 2009"],
bottom=Cork_Crime_Drugs_Final["Controlled drug offences 2003"], color='b', label="2009")
ax.bar(Cork_Crime_Drugs_Final["Station"], Cork_Crime_Drugs_Final["Controlled drug offences 2015"],
       bottom = Cork_Crime_Drugs_Final["Controlled drug offences 2003"]
+ Cork_Crime_Drugs_Final["Controlled drug offences 2009"], color='g', label="2015")

plt.xticks(rotation=90)
ax.set_xlabel("Gardai Stations")
ax.set_ylabel("Reported Cases")
ax.set_title("Drug Offense Rates reported in Cork")
plt.legend()




#Seaborn  Bar Chart

sns.set_palette("RdBu")
g = sns.catplot(x="Controlled drug offences 2015", y="Station",
           data=Dublin_Crime_Drugs_Final,
           kind="bar")
g.fig.suptitle("Dublin Drug Crime rates 2015")
plt.xticks(rotation=0)


sns.set_palette("RdBu")
g = sns.catplot(x="Burglary and related offences 2015", y="Station",
           data=Dublin_Crime_Burg_Final,
           kind="bar")
g.fig.suptitle("Dublin Burglary Crime rates 2015")
plt.xticks(rotation=0)


plt.show()


