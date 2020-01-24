
def get_graph_vector(filename):
    """
    Returns the list of vectors for the vectors provided in the input file
    """
    f = open(filename,'r')
    string = f.readline()
    split_string = string.split()
    num = int(split_string[0])
    vectors = []
    for i in range(num):
        string = f.readline()
        split_string = string.split()
        while(split_string[1].replace('.', '', 1).replace('-','',1).isnumeric()  == False):
            split_string[0] = split_string[0] + " " + split_string[1]
            split_string.remove(split_string[1])
        vectors.append([split_string[0],split_string[1],split_string[2],split_string[3],split_string[4],split_string[5]])
    vectors.sort()
    return vectors



def remove_label(vectors):
    """
    Returns the same list of vectors without the label
    """
    new_vectors = []
    for vector in vectors:
        new_vectors.append(vector[1:])

    return new_vectors

