from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop
import operator

VERBOSE = False

def debug(*args):
	if (VERBOSE):
		print ''.join([str(arg) for arg in args])

def dijkstras_shortest_path(src, dst, graph, adj):
	dist = {}
	prev = {}
	dist[src] = 0
	prev[src] = None # parent of the source node 

	queue = []
	
	# Python heapq (heap, item) : item can be a tuple or single value
	# If tuple is used, the first element will be used as key (key, data)
	heappush(queue, (dist[src], src )) 

	while queue : #(len(queue) > 0):
		pathCost, node = heappop(queue)  

		if node == dst:
			break

		adjacent = adj(graph, node)

		# Extract (position, cost) from list of adjacent states
		for   neighbor, cost in adjacent:
			totalCost = pathCost + cost
			#print totalCost
			if neighbor not in dist or totalCost < dist[neighbor]:
				dist[neighbor] = totalCost
				prev[neighbor] = node # parent of [ neighbor ] is node
				heappush(queue, ( totalCost, neighbor)) 
			

	path = []
	# Path found build it, else return empty path
	if node == dst:
		# Traverse up the parent tree
		while node: # while there is a parent (prev[src] = None)
			path.append(node) 
			node = prev[node] # update to the parent

		# Path is from dst to src, reverse it
		path.reverse()

	return path

def navigation_edges(level, cell):
	# Valid movement deltas
	deltas = {
			  'LEFT_DOWN':	(-1, -1), 
			  'LEFT': 		(-1, 0), 
			  'LEFT_UP': 	(-1, 1), 
	          'DOWN': 		(0, -1), 
	          'UP': 		(0, 1), 
	          'RIGHT_DOWN': (1, -1), 
	          'RIGHT': 		(1, 0), 
	          'RIGHT_UP':	(1, 1)
	         };
	#deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
	
	validMoves = []
	for pair in deltas.values():
	#for pair in deltas: 

		# Calculate new position: cell + deltas[i]
		position = tuple(map(operator.add, cell, pair)) # tuple(cell[0]+pair[0], cell[1]+pair[1])
		
		if position in level['spaces']:
			# Calculate edge cost
			cost = sqrt(pair[0] ** 2 + pair[1] ** 2)

			# Valid move is a tuple (nextState, edgeCost)
			validMoves.append((position, cost))
	
	return validMoves

def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	if VERBOSE:
		print("Level layout:")
		show_level(level)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		debug("Path: ", path)
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys

	# Use command line options
	from optparse import OptionParser

	parser = OptionParser(usage="usage: %prog [options] level_file src_waypoint dst_waypoint")
	parser.add_option("-v", "--verbose", dest="verbose", help="use verbose logging", action="store_true", default=False)

	(options, args) = parser.parse_args()
	# Make sure the appropriate number of arguments was supplied
	if (len(args) != 3):
		print "Unexpected argument count."
		parser.print_help()
	else:
		VERBOSE = options.verbose
		filename, src_waypoint, dst_waypoint = args
		test_route(filename, src_waypoint, dst_waypoint)
