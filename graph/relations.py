from utils.gptReqest import gptRequest


class Node:
    def __init__(self, idx, name, embedding):
        self.id = idx
        self.name = name
        self.embedding = embedding


class Relations:
    def __init__(self):
        self.nodes = []
        self.relations = []
        self.cnt = 0

    @staticmethod
    def getAllMethods(code):
        with open("../prompts/getMethods.txt", "r") as f:
            system = f.read()
        res = gptRequest(code, system)
        methods = res.split("\n")
        methods_formatted = []
        for method in methods:
            method_name, dependencies = method.split("->")
            method_name = method_name.split(".", 1)[1].strip()
            dependencies = dependencies.split(",")
            dependencies = [dependency.strip() for dependency in dependencies]
            methods_formatted.append((method_name, dependencies))
        return methods_formatted

    def addNodesFromFile(self, code):
        methods = self.getAllMethods(code)
        for method in methods:
            new_node = Node(self.cnt, method[0], None)

    def addRelation(self, node_from, node_to):
        pass
