import pandas
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime

# Returns log file data as a Dataframe
#
def ReadLog(filepath):
    cols = [
        "Timestamp",
        "Elapsed Time",
        "Client",
        "Log Tag & HTTP Code",
        "Size",
        "Method",
        "URL",
        "UserID",
        "Hierarchy & Hostname",
        "Content type",
    ]

    df = pandas.read_csv(filepath, names=cols, delim_whitespace=True, header=None)

    df[["Log Tag", "HTTP Code"]] = df[cols[3]].str.split("/", expand=True)
    df[["Hierarchy", "Hostname"]] = df[cols[8]].str.split("/", expand=True)

    df = df.drop([cols[3], cols[8]], axis=1)

    return df


# returns the number of occurrence of each unique element in a dataframe column
def FindCount(dataFrame, columnName):
    columnList = dataFrame[columnName].values
    counterObj = Counter(columnList)
    elementDictionary = {}
    for key, value in counterObj.items():
        elementDictionary[key] = value

    return elementDictionary


# plots the histogram given a dictionary of key-value pairs
def PlotHistogram(dictionaryObject, xLabel, yLabel):
    plt.bar(dictionaryObject.keys(), dictionaryObject.values())
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()


# function to find the most and least frequently visited ip
def FindMostLeastFrequent(elementDictionary):
    ipMax = max(elementDictionary, key=elementDictionary.get)
    ipMin = min(elementDictionary, key=elementDictionary.get)

    return (ipMax, ipMin)


# returns the number of occurrence of a particular element from a column
def CountRequest(dataFrame, columnName, requestType):
    tagDictionary = FindCount(dataFrame, columnName)
    return tagDictionary[requestType]

def min_max_traffic_time(dataFrame):
    count_entry = [0]*24
    time = list(dataFrame["Timestamp"])
    for i in time:
        temp = datetime.fromtimestamp(i).hour
        count_entry[temp]+=1
    max_traffic_hour = []
    min_traffic_hour = []
    max_traffic = max(count_entry)
    min_traffic = min(count_entry)
    for i in range(24):
        if count_entry == max_traffic:
            max_traffic_hour.append(i)
        if count_entry ==min_traffic:
            min_traffic_hour.append(i)
    
    return [max_traffic_hour,min_traffic,max_traffic,min_traffic]
