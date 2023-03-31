import networkx as nx
from program_files.visualize_network import network, net
from program_files.create_network_Data import node_result


# --------------------------------------------------------

    # GO TO 'run_program.py' TO RUN WHOLE PROGRAM

# --------------------------------------------------------


graph = network.degree

# Implementation of Quick Sort algorithm. This is used to sort the
# characters number of apperances by High -> Low
def quick_sort(arr):
    if not arr:
        return arr
    
    pivot = arr[0]
    lesser = [i for i in arr[1:] if i[1] <= pivot[1]]
    greater = [i for i in arr[1:] if i[1] > pivot[1]]

    return quick_sort(greater) + [pivot] + \
            quick_sort(lesser)


# ----------------------------------------------------
    # Network analysis methods
# ----------------------------------------------------

    # 1 - Chosen characters total apperances
def number_of_apperances():
    user_choice = str(input("Check character apperances: ")).upper()
    
    for i in node_result:
        if i[0] == user_choice:
            print(f"{i[0]} has {i[1]} apperances")



    # 2 - Chosen characters total relations
def number_of_relations():
    user_choice = str(input("Check total characters relations: ")).upper()

    for name, value in graph:
        if name == user_choice:
            print(f"{name} has a total of {value} relations")


    # 3 - Character with most apperances
def most_apperances():
    result = quick_sort(node_result)[0]
    print(f"Most apperances: {result[:2]}")


    # 4 - Longest distance in network/graph (diameter)
def network_diameter():
    print(f"The longest distance(diameter) is: {nx.diameter(network)}")


    # 5 - check for bridges in graph
def network_bridges():
    a = nx.has_bridges(network)
    if a == True:
        print(f"There is a bridge between:{list(nx.bridges(network))}")
    else:
        print("There is NONE bridges in Graph")


    # 6 - Total number of characters/nodes
def tot_num_Nodes():
    print(f"Total number of characters/nodes: {len(network)}")


    # 7 - Show Network Graph
def show_network_graph():
    net.show("network_drawing.html")


def see_options():
    print("""Request Graph information:
    1 - Number of apperances of a character
    2 - Number of relations of a character
    3 - Character with most apperances
    4 - Longest distanse(diameter) between 2 characters
    5 - Bridges in Graph
    6 - Total characters in Graph
    7 - Show Network graph
    """)



