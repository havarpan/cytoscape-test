# console: python ./random_graph.py > ./public/graph.json

import networkx as nx
import random
import json


# cytoscape-compatible json from G
def cyto_json(G):

    final = {}
    final["nodes"] = []
    final["edges"] = [] 

    for node in G.nodes():
        nd = {}
        nd["data"] = {}
        nd["data"]["id"] = node
        nd["data"]["label"] = node
        final["nodes"].append(nd)

    for edge in G.edges():
        nd = {}
        nd["data"]={}
        nd["data"]["id"]=str(edge[0])+str(edge[1])
        nd["data"]["source"]=edge[0]
        nd["data"]["target"]=edge[1]
        nd["data"]["weight"]=G.edges[edge[0],edge[1]]['weight']
        final["edges"].append(nd)

    return json.dumps(final, indent=4)


# create a connected graph with some randomness
def create_graph():
    G = nx.erdos_renyi_graph(random.randint(5,12), 0.4, directed=False)
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(random.randint(5,12), 0.4, directed=False)

    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = random.randint(17,42)
        
    return G

def get_json():
    return cyto_json(create_graph())
    
if __name__ == "__main__":
    print(get_json())
