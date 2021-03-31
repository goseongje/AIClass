import networkx as nx
import matplotlib.pyplot as plt
import queue


def createGraph():
    cities_graph.add_node('San_Francisco')
    cities_graph.add_node('Los_Angeles')
    cities_graph.add_node('Salt_Lake_City')
    cities_graph.add_node('Portland')
    cities_graph.add_node('El_Paso')
    cities_graph.add_node('Phoenix')
    cities_graph.add_node('Las_Vegas')
    cities_graph.add_node('Denver')
    cities_graph.add_node('Helena')
    cities_graph.add_node('Seattle')
    cities_graph.add_node('Dallas')
    cities_graph.add_node('Santa_Fe')
    cities_graph.add_node('Kansas_City')
    cities_graph.add_node('Omaha')
    cities_graph.add_node('Duluth')
    cities_graph.add_node('Winnipeg')
    cities_graph.add_node('Calgary')
    cities_graph.add_node('Vancouver')
    cities_graph.add_node('Houston')
    cities_graph.add_node('Little_Rock')
    cities_graph.add_node('Oklahoma_City')
    cities_graph.add_node('Saint_Louis')
    cities_graph.add_node('Chicago')
    cities_graph.add_node('Sault_Ste_Marie')
    cities_graph.add_node('Winnipeg')
    cities_graph.add_node('New_Orleans')
    cities_graph.add_node('Nashville')
    cities_graph.add_node('Pittsburgh')
    cities_graph.add_node('Toronto')
    cities_graph.add_node('Montreal')
    cities_graph.add_node('Miami')
    cities_graph.add_node('Atlanta')
    cities_graph.add_node('Raleigh')
    cities_graph.add_node('Washington')
    cities_graph.add_node('New_York')
    cities_graph.add_node('Boston')
    cities_graph.add_node('Charleston')

    cities_graph.add_edge('San_Francisco', 'Los_Angeles', weight=100)
    cities_graph.add_edge('San_Francisco', 'Salt_Lake_City', weight=156)
    cities_graph.add_edge('San_Francisco', 'Portland', weight=151)
    cities_graph.add_edge('Los_Angeles', 'El_Paso', weight=191)
    cities_graph.add_edge('Los_Angeles', 'Phoenix', weight=109)
    cities_graph.add_edge('Los_Angeles', 'Las_Vegas', weight=66)
    cities_graph.add_edge('Salt_Lake_City', 'Las_Vegas', weight=89)
    cities_graph.add_edge('Salt_Lake_City', 'Denver', weight=101)
    cities_graph.add_edge('Salt_Lake_City', 'Helena', weight=116)
    cities_graph.add_edge('Salt_Lake_City', 'Portland', weight=175)
    cities_graph.add_edge('Portland', 'Seattle', weight=44)
    cities_graph.add_edge('El_Paso', 'Dallas', weight=140)
    cities_graph.add_edge('El_Paso', 'Santa_Fe', weight=65)
    cities_graph.add_edge('Phoenix', 'Santa_Fe', weight=85)
    cities_graph.add_edge('Phoenix', 'Denver', weight=128)
    cities_graph.add_edge('Denver', 'Santa_Fe', weight=70)
    cities_graph.add_edge('Denver', 'Kansas_City', weight=135)
    cities_graph.add_edge('Denver', 'Omaha', weight=130)
    cities_graph.add_edge('Denver', 'Helena', weight=126)
    cities_graph.add_edge('Helena', 'Omaha', weight=174)
    cities_graph.add_edge('Helena', 'Duluth', weight=150)
    cities_graph.add_edge('Helena', 'Winnipeg', weight=137)
    cities_graph.add_edge('Helena', 'Calgary', weight=130)
    cities_graph.add_edge('Helena', 'Seattle', weight=189)
    cities_graph.add_edge('Seattle', 'Calgary', weight=118)
    cities_graph.add_edge('Seattle', 'Vancouver', weight=45)
    cities_graph.add_edge('Dallas', 'Houston', weight=46)
    cities_graph.add_edge('Dallas', 'Little_Rock', weight=74)
    cities_graph.add_edge('Santa_Fe', 'Oklahoma_City', weight=121)
    cities_graph.add_edge('Kansas_City', 'Oklahoma_City', weight=61)
    cities_graph.add_edge('Kansas_City', 'Saint_Louis', weight=68)
    cities_graph.add_edge('Omaha', 'Chicago', weight=142)
    cities_graph.add_edge('Omaha', 'Duluth', weight=74)
    cities_graph.add_edge('Duluth', 'Chicago', weight=157)
    cities_graph.add_edge('Duluth', 'Sault_Ste_Marie', weight=110)
    cities_graph.add_edge('Duluth', 'Winnipeg', weight=103)
    cities_graph.add_edge('Winnipeg', 'Sault_Ste_Marie', weight=156)
    cities_graph.add_edge('Winnipeg', 'Calgary', weight=180)
    cities_graph.add_edge('Calgary', 'Vancouver', weight=100)
    cities_graph.add_edge('Houston', 'New_Orleans', weight=80)
    cities_graph.add_edge('Little_Rock', 'New_Orleans', weight=100)
    cities_graph.add_edge('Little_Rock', 'Nashville', weight=94)
    cities_graph.add_edge('Little_Rock', 'Saint_Louis', weight=60)
    cities_graph.add_edge('Little_Rock', 'Oklahoma_City', weight=72)
    cities_graph.add_edge('Saint_Louis', 'Nashville', weight=85)
    cities_graph.add_edge('Saint_Louis', 'Chicago', weight=104)
    cities_graph.add_edge('Chicago', 'Pittsburgh', weight=81)
    cities_graph.add_edge('Sault_Ste_Marie', 'Toronto', weight=90)
    cities_graph.add_edge('Sault_Ste_Marie', 'Montreal', weight=193)
    cities_graph.add_edge('Sault_Ste_Marie', 'Winnipeg', weight=156)
    cities_graph.add_edge('New_Orleans', 'Miami', weight=151)
    cities_graph.add_edge('New_Orleans', 'Atlanta', weight=120)
    cities_graph.add_edge('Nashville', 'Atlanta', weight=67)
    cities_graph.add_edge('Nashville', 'Raleigh', weight=128)
    cities_graph.add_edge('Pittsburgh', 'Washington', weight=85)
    cities_graph.add_edge('Pittsburgh', 'New_York', weight=69)
    cities_graph.add_edge('Pittsburgh', 'Toronto', weight=80)
    cities_graph.add_edge('Toronto', 'Montreal', weight=115)
    cities_graph.add_edge('Montreal', 'New_York', weight=99)
    cities_graph.add_edge('Montreal', 'Boston', weight=69)
    cities_graph.add_edge('Miami', 'Charleston', weight=80)
    cities_graph.add_edge('Miami', 'Atlanta', weight=116)
    cities_graph.add_edge('Atlanta', 'Raleigh', weight=96)
    cities_graph.add_edge('Raleigh', 'Charleston', weight=95)
    cities_graph.add_edge('Raleigh', 'Washington', weight=47)
    cities_graph.add_edge('Washington', 'New_York', weight=76)
    cities_graph.add_edge('New_York', 'Boston', weight=74)
    cities_graph.add_edge('New_York', 'Montreal', weight=99)

    # Cost List, Parents
    infinity = float('inf')
    for node in cities_graph.nodes:
        costs[node] = infinity
        parents[node] = None

# Breath first Search Algorithm
def bfs(graph, start, goal): 
    q = queue.Queue()
    costs[start] = 0
    q.put({'current': start, 'cost': costs[start]})
    while True:
        if q.empty(): 
            break 
        
        tmp = q.get() 
        current = tmp['current'] 
        cost = tmp['cost'] 
        costs[current] = cost 
        for next in graph[current]: 
            nextCost = graph[current][next]['weight'] + cost 
            
            # renew cost 
            if costs[next] >= nextCost: 
                costs[next] = nextCost 
                parents[next] = current
                q.put({'current': next, 'cost': nextCost})
                
    # path tracking
    current = goal 
    while current != start: 
        path.append(current) 
        current = parents[current] 
    path.append(start) 
    path.reverse() 
    
    print('------------ Breadth First Search Result ------------') 
    print('1. From :', start, 'To :', goal) 
    print('2. Shortest Distance : ', costs[goal]) 
    print('3. Paths : ', path)

# For Draw Graph
def drawGraph(graph):    
    # Create positions of all nodes
    pos = nx.spring_layout(graph)    
    # Draw the graph
    nx.draw(graph, pos, node_color=range(36), node_size=300, with_labels=True, font_size=10, linewidths=0.5)    
    # Create and Draw edges labels
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=8)
    # Create shortest edges list
    shortest = nx.Graph()
    for i in range(len(path)):
        tmp = len(path) - 1
        if i < tmp:
            shortest.add_edge(path[i], path[i+1])        
    # Draw Shortest path
    nx.draw_networkx_nodes(graph, pos, nodelist=shortest.nodes, node_color='g', node_size=400)
    nx.draw_networkx_edges(graph, pos, edgelist=shortest.edges, width=5, edge_color='r')
    plt.show()

# Main function
if __name__ == "__main__":
    cities_graph = nx.Graph()    
    costs = {}
    parents = {}
    path = []    
    createGraph()
    bfs(cities_graph, 'San_Francisco', 'Boston')
    drawGraph(cities_graph)
