import pandas as pd

def categorize_values(value, classes):
    for i in range(len(classes)-1):
        if classes[i] <= value <= classes[i+1]:
            return classes[i+1]
        if value < classes[i]:
            return classes[0]



classes = [2, 4, 6, 8, 10]

xs = [1, 3, 5, 5, 7, 7, 4, 2, 6, 3, 7, 10, 9, 8, 7, 5, 3, 1, 5, 6, 7]
categorized_data = [categorize_values(x, classes) for x in xs]


frequency_table_df = pd.DataFrame(categorized_data)
frequency_table_df.columns = ["Value"]
frequency_table = frequency_table_df["Value"].value_counts().sort_index(ascending=False)

print(frequency_table)