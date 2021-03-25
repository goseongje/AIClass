import queue

graph = {}
infinity = float("inf")
costs = {}
parents = {}
processed = []

# Initialization
def init():
    global graph, infinity, costs, parents, processed

    graph = {}
    ######### L0 ##########
    graph["San_Francisco"] = {}
    graph["San_Francisco"]["Los_Angeles"] = 100
    graph["San_Francisco"]["Salt_Lake_City"] = 156
    graph["San_Francisco"]["Portland"] = 151
    
    ######### L1 ##########
    graph["Los_Angeles"] = {}
    graph["Los_Angeles"]["El_Paso"] = 191
    graph["Los_Angeles"]["Phoenix"] = 109
    graph["Los_Angeles"]["Las_Vegas"] = 66

    graph["Salt_Lake_City"] = {}
    graph["Salt_Lake_City"]["Las_Vegas"] = 89
    graph["Salt_Lake_City"]["Denver"] = 101
    graph["Salt_Lake_City"]["Helena"] = 116
    graph["Salt_Lake_City"]["Portland"] = 175
    
    graph["Portland"] = {}
    graph["Portland"]["Seattle"] = 44

    ######### L2 ##########
    graph["El_Paso"] = {}
    graph["El_Paso"]["Dallas"] = 140
    graph["El_Paso"]["Santa_Fe"] = 65

    graph["Phoenix"] = {}
    graph["Phoenix"]["Santa_Fe"] = 85
    graph["Phoenix"]["Denver"] = 128

    graph["Las_Vegas"] = {}

    graph["Denver"] = {}
    graph["Denver"]["Santa_Fe"] = 70
    graph["Denver"]["Kansas_City"] = 135 
    graph["Denver"]["Omaha"] = 130 
    graph["Denver"]["Helena"] = 126

    graph["Helena"] = {}
    graph["Helena"]["Omaha"] = 174
    graph["Helena"]["Duluth"] = 150
    graph["Helena"]["Winnipeg"] = 137
    graph["Helena"]["Calgary"] = 130
    graph["Helena"]["Seattle"] = 189
    
    graph["Seattle"] = {}
    graph["Seattle"]["Calgary"] = 118
    graph["Seattle"]["Vancouver"] = 45

    ######### L3 ##########
    graph["Dallas"] = {}
    graph["Dallas"]["Houston"] = 46 
    graph["Dallas"]["Little_Rock"] = 74

    graph["Santa_Fe"] = {}
    graph["Santa_Fe"]["Oklahoma_City"] = 121

    graph["Kansas_City"] = {}
    graph["Kansas_City"]["Oklahoma_City"] = 61
    graph["Kansas_City"]["Saint_Louis"] = 68 

    graph["Omaha"] = {}
    graph["Omaha"]["Chicago"] = 142
    graph["Omaha"]["Duluth"] = 74
    
    graph["Duluth"] = {}
    graph["Duluth"]["Chicago"] = 157
    graph["Duluth"]["Sault_Ste_Marie"] = 110 
    graph["Duluth"]["Winnipeg"] = 103

    graph["Winnipeg"] = {}
    graph["Winnipeg"]["Sault_Ste_Marie"] = 156
    graph["Winnipeg"]["Calgary"] = 180

    graph["Calgary"] = {}
    graph["Calgary"]["Vancouver"] = 100

    graph["Vancouver"] = {}

    ######### L4 ##########
    graph["Houston"] = {}
    graph["Houston"]["New_Orleans"] = 80  

    graph["Little_Rock"] = {}
    graph["Little_Rock"]["New_Orleans"] = 100
    graph["Little_Rock"]["Nashville"] = 94
    graph["Little_Rock"]["Saint_Louis"] = 60
    graph["Little_Rock"]["Oklahoma_City"] = 72

    graph["Oklahoma_City"] = {}
    
    graph["Saint_Louis"] = {}
    graph["Saint_Louis"]["Nashville"] = 85
    graph["Saint_Louis"]["Chicago"] = 104

    graph["Chicago"] = {}
    graph["Chicago"]["Pittsburgh"] = 81

    graph["Sault_Ste_Marie"] = {}
    graph["Sault_Ste_Marie"]["Toronto"] = 90
    graph["Sault_Ste_Marie"]["Montreal"] = 193
    graph["Sault_Ste_Marie"]["Winnipeg"] = 156    
    
    graph["Winnipeg"] = {}

    ######### L5 ##########
    graph["New_Orleans"] = {}
    graph["New_Orleans"]["Miami"] = 151
    graph["New_Orleans"]["Atlanta"] = 120

    graph["Nashville"] = {}
    graph["Nashville"]["Atlanta"] = 67
    graph["Nashville"]["Raleigh"] = 128   

    graph["Pittsburgh"] = {}
    graph["Pittsburgh"]["Washington"] = 85
    graph["Pittsburgh"]["New_York"] = 69  
    graph["Pittsburgh"]["Toronto"] = 80

    graph["Toronto"] = {}
    graph["Toronto"]["Montreal"] = 115

    graph["Montreal"] = {}
    graph["Montreal"]["New_York"] = 99
    graph["Montreal"]["Boston"] = 69

    ######### L6 ##########
    graph["Miami"] = {}
    graph["Miami"]["Charleston"] = 80 
    graph["Miami"]["Atlanta"] = 116

    graph["Atlanta"] = {}
    graph["Atlanta"]["Raleigh"] = 96

    graph["Raleigh"] = {}
    graph["Raleigh"]["Charleston"] = 95
    graph["Raleigh"]["Washington"] = 47

    graph["Washington"] = {}
    graph["Washington"]["New_York"] = 76
    
    graph["New_York"] = {}
    graph["New_York"]["Boston"] = 74
    graph["New_York"]["Montreal"] = 99

    graph["Boston"] = {} 

    ######### L7 ##########
    graph["Charleston"] = {}

    infinity = float("inf")

    costs = {}
    costs["San_Francisco"] = infinity
    costs["Los_Angeles"] = infinity
    costs["Salt_Lake_City"] = infinity
    costs["Portland"] = infinity
    costs["El_Paso"] = infinity
    costs["Phoenix"] = infinity
    costs["Las_Vegas"] = infinity
    costs["Denver"] = infinity
    costs["Helena"] = infinity
    costs["Seattle"] = infinity
    costs["Dallas"] = infinity
    costs["Santa_Fe"] = infinity
    costs["Kansas_City"] = infinity
    costs["Omaha"] = infinity
    costs["Duluth"] = infinity
    costs["Winnipeg"] = infinity
    costs["Calgary"] = infinity
    costs["Vancouver"] = infinity
    costs["Houston"] = infinity
    costs["Little_Rock"] = infinity
    costs["Oklahoma_City"] = infinity
    costs["Saint_Louis"] = infinity
    costs["Chicago"] = infinity
    costs["Sault_Ste_Marie"] = infinity
    costs["Winnipeg"] = infinity
    costs["New_Orleans"] = infinity
    costs["Nashville"] = infinity
    costs["Pittsburgh"] = infinity
    costs["Toronto"] = infinity
    costs["Montreal"] = infinity
    costs["Miami"] = infinity
    costs["Atlanta"] = infinity
    costs["Raleigh"] = infinity
    costs["Washington"] = infinity
    costs["New_York"] = infinity
    costs["Boston"] = infinity
    costs["Charleston"] = infinity

    parents = {}        
    parents["Los_Angeles"] = None
    parents["Salt_Lake_City"] = None
    parents["Portland"] = None
    parents["El_Paso"] = None
    parents["Phoenix"] = None
    parents["Las_Vegas"] = None
    parents["Denver"] = None
    parents["Helena"] = None
    parents["Seattle"] = None
    parents["Dallas"] = None
    parents["Santa_Fe"] = None
    parents["Kansas_City"] = None
    parents["Omaha"] = None
    parents["Duluth"] = None
    parents["Winnipeg"] = None
    parents["Calgary"] = None
    parents["Vancouver"] = None
    parents["Houston"] = None
    parents["Little_Rock"] = None
    parents["Oklahoma_City"] = None
    parents["Saint_Louis"] = None
    parents["Chicago"] = None
    parents["Sault_Ste_Marie"] = None
    parents["Winnipeg"] = None
    parents["New_Orleans"] = None
    parents["Nashville"] = None
    parents["Pittsburgh"] = None
    parents["Toronto"] = None
    parents["Montreal"] = None
    parents["Miami"] = None
    parents["Atlanta"] = None
    parents["Raleigh"] = None
    parents["Washington"] = None
    parents["New_York"] = None
    parents["Boston"] = None
    parents["Charleston"] = None

    processed = []

def find_lowest_cost_node(costs): 
    lowest_cost = float("inf") 
    lowest_cost_node = None
    for node in costs: 
        cost = costs[node] 
        if cost < lowest_cost and node not in processed: 
            lowest_cost = cost 
            lowest_cost_node = node 
        
    return lowest_cost_node

def bfs(graph, start, final): 
    q = queue.Queue()
    costs[start] = 0
    q.put({"cur": start, "cost": costs[start]})
    while True:
        if q.empty(): 
            break 
        
        val = q.get() 
        cur = val["cur"] 
        cost = val["cost"] 
        costs[cur] = cost 
        for next in graph[cur]: 
            nextCost = graph[cur][next] + cost 
            
            # next의 cost가 nextCost보다 크다면 갱신해준다.(더 최단거리로) 
            if costs[next] >= nextCost: 
                costs[next] = nextCost 
                parents[next] = cur 
                q.put({"cur": next, "cost": nextCost}) 
                
    # 추적 경로
    trace = [] 
    current = final 
    while current != start: 
        trace.append(current) 
        current = parents[current] 
    trace.append(start) 
    trace.reverse() 
    
    print("=== BFS ===") 
    print("From :", start, "To :", final) 
    print("Shortest Distance : ", costs[final]) 
    print("Paths : ", trace)


init()
bfs(graph, "San_Francisco", "Boston")

