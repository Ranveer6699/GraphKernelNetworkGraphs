import matplotlib.pyplot as plt
#Reading the original_model_save file and plotting the 2d plot on the graph
f = open('original_model_save','r')
string = f.readline()
split_string = string.split()
print(split_string)
num = int(split_string[0])
x = []
y = []
l = []
for i in range(num):
    string = f.readline()
    print(string)
    split_string = string.split()
    string_size = len(split_string)
    while(split_string[1].replace('.', '', 1).replace('-','',1).isnumeric()  == False):
        split_string[0] = split_string[0] + " " + split_string[1]
        print(split_string[1])
        split_string.remove(split_string[1])
    l.append(split_string[0])
    x.append(float(split_string[1]))
    y.append(float(split_string[2]))

fig, ax = plt.subplots()
ax.scatter(y, x)

for i, txt in enumerate(l):
    ax.annotate(txt, (y[i], x[i]))

f = open('comparison_model_save','r')
string = f.readline()
split_string = string.split()
print(split_string)
num = int(split_string[0])
x = []
y = []
l = []
for i in range(num):
    string = f.readline()
    print(string)
    split_string = string.split()
    string_size = len(split_string)
    while(split_string[1].replace('.', '', 1).replace('-','',1).isnumeric()  == False):
        split_string[0] = split_string[0] + " " + split_string[1]
        print(split_string[1])
        split_string.remove(split_string[1])
    l.append(split_string[0])
    x.append(float(split_string[1]))
    y.append(float(split_string[2]))

fig, ax = plt.subplots()
ax.scatter(y, x)

for i, txt in enumerate(l):
    ax.annotate(txt, (y[i], x[i]))

plt.show()