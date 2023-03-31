import networkx as nx
from pyvis.network import Network

from program_files.create_network_Data import node_result, edge_result
# node_result is list of lists: [[name, value]]
# edge_result is list of lists: [[source, target, value]]


# --------------------------------------------------------

    # GO TO 'run_program.py' TO RUN WHOLE PROGRAM

# --------------------------------------------------------


# create network graph
network = nx.Graph()



# adds nodes to the network
for val in node_result:
    temp1 = val[0]      # name of the character
    temp2 = val[1]      # value, num of apperances
    temp3 = val[2]      # color
    
    # colorcode "#808080" means the caracter is not a Main character.
    # we give nodes with other color a bigger font size and bigger value to adjust node size
    if temp3 != "#808080":
        network.add_node(temp1, label=temp1, font={"size":50, "color":"white"}, value=(temp2+500),
                         title=f"Name: {temp1}\nApperances: {temp2}", color=temp3)
    else:
        network.add_node(temp1, label=temp1, font={"size":20, "color":"white"},value=temp2,
                         title=f"Name: {temp1}\nApperances: {temp2}") 


# adds edges/links between the nodes
for val in edge_result:
    source = val[0]     # from character
    target = val[1]     # to -> character
    value = val[2]      # tot scenes 2 character are in together

    temp1 = node_result[source]     # source character
    temp2 = node_result[target]     # target character

    network.add_edge(temp1[0], temp2[0], color="#5689CE", value=value)


# draw network graph
net = Network(height="100%", width="100%", heading="STAR WARS social network", bgcolor="#272929")

net.force_atlas_2based()
net.toggle_physics(True)
net.from_nx(network)

# display graph in .html file
net.show("network_drawing.html")