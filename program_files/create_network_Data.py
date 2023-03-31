import json

# --------------------------------------------------------

    # GO TO 'run_program.py' TO RUN WHOLE PROGRAM

# --------------------------------------------------------

# chose what file to use
file = "data/sw.json"

# finds nodes from .json file
def nodes():
    # open json file with information on characters and apperances
    with open(file) as input_file:
        json_data = json.load(input_file)

        global node_result
        node_result =  []
        for character in json_data["nodes"]:          
            for key, val in character.items():          
                if key == "name":     
                    temp1 = val                   
                if key == "value":
                    temp2 = val
                if key == "colour":
                    temp3 = val

                    # temp 1,2,3 : character, number of apperances, color
                    temp_list = [temp1, temp2, temp3]
                    node_result.append(temp_list)



        # returnes the list of lists : node_result
    return node_result




# finds edges/links from .json file
def edges():
    with open(file) as input_file:
        json_data = json.load(input_file)

        global edge_result
        edge_result =  []                                    
        for character in json_data["links"]:          
            for key, val in character.items():          
                if key == "source":     
                    temp1 = val                          
                if key == "target":
                    temp2 = val
                if key == "value":
                    temp3 = val

                    # temp 1,2,3 : from character, to character, number of times
                    temp_list =[temp1,temp2,temp3]
                    edge_result.append(temp_list)


        # returns the list of lists : edge_result 
    return edge_result



nodes()
edges()

    

