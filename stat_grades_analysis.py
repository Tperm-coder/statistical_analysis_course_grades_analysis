import collections
from matplotlib import pyplot as plt


file_path = "stat_grades.txt"
file = open(file_path,'r')
data = file.read().split('\n') #from string to list where each '\n' in the string is the defrence between to elements
file.close()

final_grades = []
for i in range(len(data)):
    data[i] = data[i].split(' ')
    
    if data[i][0] == '': #avoinding headers, this space was left intentional to identify the required rows
        final_grades.append(float(data[i][-1])) #appending last element (the final grade)

grades_frequency = collections.Counter(final_grades) #list to frequency map
grades_frequency = collections.OrderedDict(sorted(grades_frequency.items())) #sort the map by keys ascending

# spearate the grade and the grade's frequency in two differnet lists
grades = list(grades_frequency.keys())
frequency = list(grades_frequency.values())

#intializing and plotting the graph
fig = plt.figure(figsize = (10, 5))

plt.bar(grades, frequency, color ='lightseagreen',width = 0.45)
plt.xlabel("Grades (out of 40)")
plt.ylabel("Grades frequency")
plt.title("Total grades frequency")

plt.show()
