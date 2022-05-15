#!/usr/bin/env python3

from pathlib import Path
import sys
import graphviz as g

from rpLinker_classes import *

# Help function
def help(argv):
	message = argv[0] + """
generation of relationship graph between pc/npc of a role-playing campaign

Usage:
"""+ argv[0] +""" [DATA] [GRAPH NAME]"""
	print(message)
	exit()


#------------------------------------------------------------------------------
# Check arguments
#------------------------------------------------------------------------------
if "-h" in sys.argv or "--help" in sys.argv:
	help(sys.argv)

if len(sys.argv) != 3:
	print("Wrong usage (-h || --help)")
	exit()

# store the value
data       = sys.argv[1]
graph_name = sys.argv[2]


# check if the data file exist
if not Path(data).is_file():
	print("the data file must exist and be a file :p")
	exit()

#------------------------------------------------------------------------------
# start of the script itself
#------------------------------------------------------------------------------

# read data
nodes = []
edges = []

read_nodes = True

nl = 0

with open(data, "r") as d:
	for line in d:
		nl += 1
		# remove end-line character
		line = line.replace("\n","")
		line = line.replace("\r","")

		# Lines after "# Edges" describe ... edges !
		if line == "# Edges":
			read_nodes = False

		# manage error if the data file does not respect the format
		try:
			# don't pay attention to empty line and those starting with '#'
			if line != "" and line[0] != "#":
				if read_nodes:
					n = Node_rpg(line.split("\t"))
					nodes.append(n)
				else:
					e = Edge_rpg(line.split("\t"))
					edges.append(e)
		except Exception as e:
			print("error: Wrong format in DATA file line " + str(nl))
			exit()

print(len(nodes))
print(len(edges))


# draw graph
relationship = g.Digraph('relationship', comment='relationship graph between pc/npc')

for n in nodes:
	relationship.node(str(n._id), n._name)

for e in edges:
	relationship.edge(str(e._source),str(e._arrival), e._links)

relationship.render(outfile=graph_name).replace('\\', '/')
