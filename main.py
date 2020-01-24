import numpy as np
import networkx as nx
import random
import copy
import graph_vector_operations as gv
import statistics as st
import matplotlib.pyplot as plt
from node2vec import Node2Vec
from scipy.spatial import distance

#Generating a normal networkx graph with the following parameters
num_nodes = 2000
prob = 0.2
graph = nx.read_gml('/home/ranveersingh/Desktop/Research/Graph Kernel Implementation/Graphs/Aarnet.gml')

#ICreating a deep copy of the same graph as before 
comparison_graph = copy.deepcopy(graph)
comparison_graph.remove_edge('Melbourne1','Melbourne2')


#Precompiling the probabilities and generating the walks for the original graph
#p and q are hyperparamters with the current values p = 1 , q = 2 suitable for the kind of embedding we want, controllers and switches
#Change workers = 1 if you are on windows
node2vec = Node2Vec(graph, p = 1, q =2 , dimensions=5, walk_length=100, num_walks=2000, workers=8)

#Embed nodes
original_model = node2vec.fit(window = 10, min_count = 1, batch_words = 4)

#Saving the embedding 
original_model.wv.save_word2vec_format('original_model_save')


#Doing the same for the comparison_graph
node2vec2 = Node2Vec(comparison_graph, p = 1, q =2 , dimensions=5, walk_length=100, num_walks=2000, workers=8)

#Embed nodes
comparison_model = node2vec2.fit(window = 10, min_count = 1, batch_words = 4)

#Saving the embedding 
comparison_model.wv.save_word2vec_format('comparison_model_save')



#Calculating the Euclidean Distance Matrix for the original graph
original_graph_vectors = gv.get_graph_vector('original_model_save')
print(original_graph_vectors)


#Calculating the Euclidean distance matrix for the comparison graph
comparison_graph_vectors = gv.get_graph_vector('comparison_model_save')
print(comparison_graph_vectors)


print("=============================================================================================\n\n\n\n\n\n\n\n\n")
matrix = []

#Getting the original_graph_vector without the label
matrix = gv.remove_label(original_graph_vectors)

original_euclidean_distance = distance.pdist(matrix)


print(original_euclidean_distance)

print("=============================================================================================\n\n\n\n\n\n\n\n\n")
matrix = gv.remove_label(comparison_graph_vectors)
comparison_euclidean_distance = distance.pdist(matrix)
print(comparison_euclidean_distance)

print("=============================================================================================\n\n\n\n\n\n\n\n\n")
difference = np.subtract(original_euclidean_distance,comparison_euclidean_distance)
print("The difference between these two is \n",difference)

percent_difference = []

n = len(original_euclidean_distance)
for i in range(n):
    percent_difference.append(abs(difference[i]/original_euclidean_distance[i] * 100))

percent_difference.sort()
print("=============================================================================================\n\n\n\n\n\n\n\n\n")
print(percent_difference)
print("average = ", sum(percent_difference)/len(percent_difference), "max = ", max(percent_difference), "min = ", min(percent_difference), "standard deviation = ", st.stdev(percent_difference))