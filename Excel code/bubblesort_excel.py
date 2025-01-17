import pandas as pd
#Generic bubble sort
def bubble_sort(item):
    n = len(item)
    for i in range(n):
        for j in range(0, n - i - 1):
            if item[j]['Price'] > item[j + 1]['Price']:
                item[j], item[j + 1] = item[j + 1], item[j]
#Read cvs file function
def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe

# Column names you want to read from the CSV file
columns = [0,4]
# Escaping the backslashes
filepath = 'D:\Python_Excel_Task\DiamondValues.csv'
# Read the specified columns from the CSV file into a DataFrame
dataframe = read_csv(filepath, columns)
# Print the original CSV data
print("CSV Data: ")
print(dataframe)
print("")
# Convert DataFrame to list of dictionaries to perform bubble sort
data_list = dataframe.to_dict('records') #making a list / dictinary value list
print(" ")
print(data_list)
print(" ")
# Sort the data using bubble sort based on the 'Price' column
bubble_sort(data_list)
# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)
print("Bubble Sorted Data:")
print(sorted_dataframe)