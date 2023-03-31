# Star-Wars-Social-Network

This repository contains the social network of all characters from the Star Wars movies episode 1-7. The data i have used has been extracted from:
@misc{gabasova_star_wars_2016,
  author  = {Evelina Gabasova},
  title   = {{Star Wars social network}},
  year    = 2016,
  url     = {https://doi.org/10.5281/zenodo.1411479},
  doi     = {10.5281/zenodo.1411479}
 }
 
In short, I have taken the files named 'starwars-episode-N-mentions'. These files contains data from episode N, where the links/edges between characters/nodes are defined by the times the characters are mentioned withing the same scene from the movie script.

I have written the program in two different formats. One is with separate python files and the other one is a jupyter notebook. The folder program_files contains 3 python files: analysis_methods, create_ne

 ### Description of network data
 The json files representing the networks contain the following information:
 
 # Nodes
 The nodes contain the following fields:
  name: Name of the character
  value: Number of scenes the character appeared in
  colour: Colour in the visualization
  
# Links
Links represents connections between characters:
  source: zero-based index of the character that is one end of the link, the order of nodes is the order in which they are listed in the “nodes” element
  target: zero-based index of the character that is the the other end of the link.
  value: Number of scenes where the “source” and “target” of the link appeared together. Note that the network is undirected. Which character represents the source and the target is arbitrary. 
