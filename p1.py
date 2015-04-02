from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
	dist = {}
	prev = {}
	dist[src] = 0
	prev[src] = None

	queue = []
	heappush(queue, (src, dst[src])

	while len(queue) > 0:
		node = heappop(queue)

		if node == dst:
			break

		adjacent = adj(graph, node)
		for neighbor in adjacent:
			cost = sqrt((neighbor[0] - node[0])^2 + (neighbor[1] - node[1])^2)
			totalCost = dist[node] + cost

			if neighbor not in dist or totalCost < dist[neighbor]:
				dist[neighbor] = totalCost
				prev[neighbor] = node
				heappush(queue, (neighbor, totalCost))

	# Path found build it
	if node == dst:
		pass

	raise NotImplementedError	

def navigation_edges(level, cell):
	# Valid movement deltas
	deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
	validMoves = []
	for pair in delta:
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
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
