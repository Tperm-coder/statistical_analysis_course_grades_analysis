import collections
from matplotlib import pyplot as plt

plt.style.use('bmh')
dec_to_bin = [[0,0],[0,1],[1,0],[1,1]]

def build_graph(data_lists, isKDE = False):

    fig, axs = plt.subplots(2,2)
    fig.set_size_inches(12, 8.5)
    fig.set_dpi(100)
    fig.suptitle('Grades Frequency\nX-axis: Grade , Y-axis: Grade Frequency')

    for index , data_list in enumerate(data_lists) :

        graph_title = data_list[-1]
        data_list = data_list[0]

        data_frequency = collections.Counter(data_list) #list to frequency map
        data_frequency = collections.OrderedDict(sorted(data_frequency.items())) #sort the map by keys ascending

        # spearate the data and the data's frequency in two differnet lists
        data = list(data_frequency.keys())
        frequency = list(data_frequency.values())

        axs[dec_to_bin[index][0],dec_to_bin[index][1]].title.set_text(graph_title)

        if isKDE :
            sns.histplot(x = data , y = frequency , ax=axs[dec_to_bin[index][0],dec_to_bin[index][1]])
            sns.set_theme(style="darkgrid")
        else :
            axs[dec_to_bin[index][0],dec_to_bin[index][1]].bar(data, frequency, color ='darkcyan')


file_path = "yearworks.csv"

file = open(file_path,'r')
data = file.read().split('\n') #from string to list where each '\n' in the string is the defrence between to elements
file.close()

data.pop() #remove the last empty row

midterm_grades = []
quiz_one_grades = []
quiz_two_grades = []
final_grades = []

for i in range(1,len(data)) : #starting from index 1 to skip headers
    data[i] = data[i].split(',')
    if data[i][0] != '':
        midterm_grades.append(float(data[i][0]))
    if data[i][2] != '':
        quiz_one_grades.append(float(data[i][2]))
    if data[i][3] != '':
        quiz_two_grades.append(float(data[i][3]))
    final_grades.append(float(data[i][6]))



build_graph([[final_grades,"Total Grades"],
[midterm_grades,"Midterm Grades"],
[quiz_one_grades,"Quiz One Grades"],
[quiz_two_grades,"Quiz Two Grades"]])

plt.subplots_adjust(left=0.1 , bottom=0.1 , right=0.9 , top=0.9 , wspace=0.2 , hspace=0.2)
plt.show()
