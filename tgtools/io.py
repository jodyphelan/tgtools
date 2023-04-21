import networkx as nx
import json

def load(filename: str):
    """Load a graph from a json file in the format used by the
    tb-tools.

    Parameters
    ----------
    filename : string
       File name

    Returns
    -------
    G : NetworkX Graph

    Examples
    --------
    >>> G=tg.load('test.json')
    """
    print(filename)
    G = nx.Graph()
    data = json.load(open(filename))
    for node in data['nodes']:
        G.add_node(node['id'], **node['properties'])
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], **edge['properties'])
    return G


def dump(G, filename: str):
    """Dump a graph to a json file in the format used by the
    tb-tools.

    Parameters
    ----------
    G : NetworkX Graph
    filename : string
       File name

    Examples
    --------
    >>> G=tg.load('test.json')
    >>> dump(G, 'test2.json')
    """
    data = {'nodes': [], 'edges': []}
    for node in G.nodes(data=True):
        data['nodes'].append({'id': node[0], 'properties': node[1]})
    for edge in G.edges(data=True):
        data['edges'].append({'source': edge[0], 'target': edge[1], 'properties': edge[2]})
    json.dump(data, open(filename, 'w'))