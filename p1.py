from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop
import operator

def dijkstras_shortest_path(src, dst, graph, adj):
	dist = {}
	prev = {}
	dist[src] = 0
	prev[src] = None # parent of the source node 

	queue = []
	
	heappush(queue, (src, dist[src])) # ( (0,0), 0)

	while queue: #(len(queue) > 0):
		node, pathCost = heappop(queue) 

		if node == dst:
			break

		adjacent = adj(graph, node)

		# Extract (position, cost) from list of adjacent states
		for neighbor, cost in adjacent:
			totalCost = pathCost + cost

			if neighbor not in dist or totalCost < dist[neighbor]:
				dist[neighbor] = totalCost
				prev[neighbor] = node # parent of [ neighbor ] is node
				heappush(queue, (neighbor, totalCost))

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
	deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
	validMoves = []
	for pair in deltas:
		# Calculate new position: cell + deltas[i]
		position = tuple(map(operator.add, cell, pair))
		# Calculate edge cost
		cost = sqrt(pair[0] ** 2 + pair[1] ** 2)
		if position in level['spaces']:
			# Valid move is a tuple (nextState, edgeCost)
			validMoves.append((position, cost))

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
