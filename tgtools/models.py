from pydantic import BaseModel

class Node(BaseModel):
    id: str
    properties: dict

class Edge(BaseModel):
    source: str
    target: str
    properties: dict


class DictGraph(BaseModel):
    nodes: list[Node]
    edges: list[Edge]