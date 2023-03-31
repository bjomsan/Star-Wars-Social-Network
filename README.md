# Star-Wars-Social-Network

This repository contains the social network of all characters from the Star Wars movies episode 1-7. The data i have used the 'starwars-episode-N-mentions.json' files from: <br>
@misc{gabasova_star_wars_2016, <br>
  author  = {Evelina Gabasova},<br>
  title   = {{Star Wars social network}},<br>
  year    = 2016,<br>
  url     = {https://doi.org/10.5281/zenodo.1411479},<br>
  doi     = {10.5281/zenodo.1411479}<br>
 }<br>

In short, I have taken the files named 'starwars-episode-N-mentions'. These files contains data from episode N, where the links/edges between characters/nodes are defined by the times the characters are mentioned withing the same scene from the movie script. All these datafiles are stored in the folder 'data'. The file 'sw' is set as defult in the python programs, but you can easily change what file you use in the jupyter notebook or the 'program_files/create_network_Data' file. <br>

See the folder 'networks' for html files displaying all the different networks. <br>

## Description of network data
 The json files representing the networks contain the following information:<br>
 
 ### Nodes
 The nodes contain the following fields: <br>
  name: Name of the character <br>
  value: Number of scenes the character appeared in <br>
  colour: Colour in the visualization <br>
  
### Links
Links represents connections between characters: <br>
  source: zero-based index of the character that is one end of the link, the order of nodes is the order in which they are listed in the “nodes” element. <br>
  target: zero-based index of the character that is the the other end of the link. <br>
  value: Number of scenes where the “source” and “target” of the link appeared together. Note that the network is undirected. Which character represents the source and the target is arbitrary. 

## How to run the program
I have written the program in two different formats. One is with separate python files and the other one is a jupyter notebook. The jupyter notebook contains everything needed in one single file. <br>
Run the .py file 'run_program'. This python program executes the code from the folder 'program_files' that contains 3 python files: <br>
create_network_Data: file that extracts json data and rearrange the data into list og lists. <br>
visualize_network: take the extracted data and inserts into a network graph and displays the graph. <br>
analysis_methods: different types of analysis on the network. The program asks for input in terminal and prints output. 
