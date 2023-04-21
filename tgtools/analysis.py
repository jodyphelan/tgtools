import networkx as nx

def stats(G):
    """Print some statistics about the graph.

    Parameters
    ----------
    G : NetworkX Graph

    Examples
    --------
    >>> G=nx.read_tg('test.json')
    >>> stats(G)
    """
    print('Nodes: ', G.number_of_nodes())
    print('Edges: ', G.number_of_edges())
    print('Density: ', nx.density(G))
    print('Number of clusters: ', nx.number_connected_components(G))