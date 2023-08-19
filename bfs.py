from collections import deque





def breadthFirstSearch(graph : dict, search_queue : deque):
    persons_searched = []
    while search_queue:
        current_node = search_queue.popleft()
        if current_node not in persons_searched:
            if check_person_ends_with_z(current_node):
                persons_searched.append(current_node)
                retrace_path(persons_searched, graph)
                return "CLOSEST  PERSON WITH LETTER: " + str(persons_searched) 
            
            search_queue += graph[current_node] 
            persons_searched.append(current_node)
    
    return "NO ONE IN NETWORK WITH THE METRIC"


def check_person_ends_with_z(current_node : str):
    if current_node.endswith("ke"):
        return True
    return False

def retrace_path(persons_searched : list, graph : dict):
    persons_searched.reverse()
    target = persons_searched.pop(0)
    path = [target]
    for node in persons_searched:
        node_children = graph[node]
        if target in node_children:
            path.append(node)
            target = node
    path.reverse()
    print(f"path : {str(path)}")
    
            




graph = {}
graph["You"] = ["Bob", "Alice", "Elizabeth"]
graph["Bob"] = ["Samuel", "Jackson"]
graph["Alice"] = ["Prince", "Gabriel"]
graph["Elizabeth"] = []
graph["Samuel"] = ["Patience", "Gond"]
graph["Jackson"] = []
graph["Prince"] = ["Hugoz"]
graph["Gabriel"] = ["Hatake"]
graph ["Patience"] = []
graph["Gond"] = []
graph["Hugoz"] = []
graph["Hatake"] = []

search_queue = deque()
search_queue += graph["You"]
print(breadthFirstSearch(graph, search_queue))