import random
"""
You'll want to implement a smarter decision logic. This is skeleton code that you should copy and replace in your repository.
"""
class PercolationPlayer:
    
	#alright, lets return an uncolored dot with the most lines attched to it.
	#If two dots have the same amount of line, take the one with the most hostiles.  
    #1. Get a list of all the verticies that are uncolored and the number of edges attached to them. 
    #2. Get all of the verticies that are tied for first in the num_edges department. 
    #3. Find the one out of that subset which is surrounded by the most hostile nodes.
    def ChooseVertexToColor(graph, player): 
        #1.
        uncolored_verticies = []
        for v in graph.V:
        	#if it is uncolored
        	if v.color == -1:
        		#finding the amount of edges they have attached
        		#the current number of edges attached to this vertex (that have been found)
        		num_edges = 0
        		for e in graph.E:
        			#if an edge is made up of one of these verticies. 
        			if e.a == v or e.b == v:
        				#we found an edge!
        				num_edges += 1
        		#Now that we have both the number of edges and the node, lets add it to our List
        		uncolored_verticies.append((v,num_edges))

        #lets sort this list by num_edges
        uncolored_verticies.sort(key = lambda vertex: vertex[1])
        #print("#############################################################################")
        #print(uncolored_verticies)

        #2. 
        #Since the list is sorted by the number of edges a vertex has, 
        #we know at least one of the best nodes will be at the end
        better_verticies = [uncolored_verticies.pop()]
        highest_num_edges = better_verticies[0][1]

        for v in uncolored_verticies:
        	if v[1] == highest_num_edges:
        		better_verticies.append(v)
        #3.
        # we now have a list of vertecies, 
        # but they have a different amount of hostile nodes
        # lets pick the one with the most hostile neighbors
        best_verticies = []
        for v in better_verticies:
        	best_verticies.append((v, PercolationPlayer.CountHostileNeighbors(v, graph, player)))
        #sorting by most hostile neighbors
        best_verticies.sort(key = lambda best_vertex: best_vertex[1])
        #print( "vertex chosen: ", best_verticies[-1][0][1])
        #print("#############################################################################")
        return best_verticies[-1][0][0]
    
    #This returns the number of hostile neighbors a node has
    def CountHostileNeighbors(v, graph, player):
    	hostile_neighbors = 0
    	for e in graph.E:
        	if (e.a == v):
        		if e.b.color == (player - 1) * -1:
        			hostile_neighbors += 1
        	elif (e.b == v):
        		if e.a.color == (player - 1) * -1:
        			hostile_neighbors += 1
    	return hostile_neighbors

    #Counts the number of neighbors a node has
    def CountNeighbors(v, graph):
    	num_neighbors = 0
    	for e in graph.E:
        	if (e.a == v):
        		num_neighbors += 0 
        	elif (e.b == v):
        		num_neighbors += 0
    	return num_neighbors
    
    #We now need to get the best node to remove!
    #1. Lets get a list of all the nodes and thier sorted A - D scores.
    #2. Now lets see about the ties. Lets make a list of only the best nodes.
    #3. If tie, lets take th one with the least neighbors.
    def ChooseVertexToRemove(graph, player):
    	#1.
    	nodes = []
    	for v in graph.V:
    		if v.color == player:
    			A_D_Score = PercolationPlayer.CountHostileNeighbors(v, graph, player) - PercolationPlayer.CountNeighbors(v, graph)
    			nodes.append((v, A_D_Score))
    	#lets sort them now
    	nodes.sort(key = lambda A_D: A_D[1])

    	#2.
    	better_nodes = [nodes.pop()]
    	highest_A_D = better_nodes[0][1]

    	for v in nodes:
        	if v[1] == highest_A_D:
        		better_nodes.append(v)

        #3.
    	best_nodes = []
    	for v in better_nodes:
        	best_nodes.append((v, PercolationPlayer.CountNeighbors(v, graph)))
        #sorting by most neighbors
    	best_nodes.sort(key = lambda best_vertex: best_vertex[1])
        #we want the lowest number of neighbors picked first, 
        #so we will take the first vertex
    	return best_nodes[0][0][0]

    