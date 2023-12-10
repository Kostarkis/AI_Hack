from graph.relations import Relations
import os

with open("../graph/sample.txt", "r") as f:
    sample_code = f.read()

relations = Relations()

relations.addNodesFromFile(sample_code)
