import pandas

# Reading the CSV
yearworks_data = pandas.read_csv("./yearworks.csv")

yearworks_data.drop("Student_ID", axis=1, inplace=True)

print(yearworks_data.head())

yearworks_data.to_json(path_or_buf="yearworks.json",
                      orient='records')
yearworks_data.to_csv(path_or_buf="yearworks_edit.csv", index=False)
