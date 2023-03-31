from program_files.analysis_methods import number_of_apperances
from program_files.analysis_methods import number_of_relations
from program_files.analysis_methods import most_apperances
from program_files.analysis_methods import network_diameter
from program_files.analysis_methods import network_bridges
from program_files.analysis_methods import tot_num_Nodes
from program_files.analysis_methods import show_network_graph
from program_files.analysis_methods import see_options

# --------------------------------------------------------

    # RUN THIS TO START WHOLE PROGRAM

# --------------------------------------------------------


# --------------------------------------------------------

    # Dataset Citation:

        # @misc{gabasova_star_wars_2016,
        #  author  = {Evelina Gabasova},
        #  title   = {{Star Wars social network}},
        #  year    = 2016,
        #  url     = {https://doi.org/10.5281/zenodo.1411479},
        #  doi     = {10.5281/zenodo.1411479}
        # }

# --------------------------------------------------------




see_options()

menu = {
    1: number_of_apperances, 2: number_of_relations, 3: most_apperances,
    4: network_diameter, 5: network_bridges, 6: tot_num_Nodes, 7: show_network_graph,
}


while True:
    a = int(input("> "))

    # Get the function corresponding to the users choice
    func = menu.get(a)

    # Execute the function if it exists, exit the loop if it doesnt
    if func:
        func()
    else:
        break