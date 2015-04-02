from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
	dist = {}
	prev = {}
	dist[src] = 0
	prev[src] = None # parent of the source node 

	queue = []
	
	heappush(queue, (src, dist[src])) # ( (0,0), 0)

	while queue: #(len(queue) > 0):
		node, cost = heappop(queue) 

		if node == dst:
			break

		adjacent = adj(graph, node)

		for neighbor in adjacent:
			
			# exponentiation in Python is done using a ** b and not a ^ b
			cost = sqrt(   (neighbor[0] - node[0]) ** 2  + (neighbor[1] - node[1]) ** 2  )
			totalCost = dist[node] + cost

			if neighbor not in dist or totalCost < dist[neighbor]:
				dist[neighbor] = totalCost
				prev[neighbor] = node # parent of [ neigbor ] is node
				heappush(queue, (neighbor, totalCost))

	# Path found build it
	if node == dst:
		# path = [dst]  
		# nextNode = prev[node] # gets the previous node of the destination node
		nextNode = dst
		path = []
		while prev[nextNode]: # while there is parent of that node
			
			path.append(nextNode) 
			nextNode = prev[nextNode] # find the parent of this node

		path.append(nextNode) # add the last node, which is the source
		path.reverse() 
		return path  #return a list of nodes from source node to destination node
		#pass

	return []

def navigation_edges(level, cell):
	# Valid movement deltas
	deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
	validMoves = []
	for pair in deltas:
		position = (cell[0] + pair[0], cell[1] + pair[1])
		if position in level['spaces']:
			validMoves.append(position)

	return validMoves

def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		print path
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
