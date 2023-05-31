import random_surfer_generator as rs
import stdarray as arr
import numpy as np
import random as r
import matplotlib.pyplot as plt

LEAP_PROBABILITY = 0.1
LINK_PROBABILITY = 1 - LEAP_PROBABILITY

def random_surf(trans_matrix, amount_of_moves):
    loc = 0
    move = 0
    page_rank = arr.create1D(len(trans_matrix), 0)
    for i in range(amount_of_moves):
        random = r.uniform(0,1)
        prob = 0
        for j in range(len(trans_matrix)):
            prob += trans_matrix[loc][j]
            if random < prob:
                loc = j
                move += 1
                page_rank[j] += 1
                break
    for i in range(len(page_rank)):
        page_rank[i] /= amount_of_moves
    update_histogram(page_rank)   

def generate_transition_matrix(graph):
    link_counts = get_link_count(graph)
    link_prob = get_link_prob(link_counts)
    leap_prob = get_leap_prob(graph['Nodes'])
    return np.add(link_prob, leap_prob)
    
def get_link_count(graph):
    links = arr.create2D(graph['Nodes'], graph['Nodes'], 0)
    for link in graph['Links']:
        links[link[0]][link[1]] += 1
    return links

def get_link_prob(linkCount):
    tmp = arr.create1D(len(linkCount), 0)
    out = arr.create2D(len(linkCount),len(linkCount), 0)
    for i in range(len(linkCount)):
        for j in linkCount[i]:
            tmp[i] += j
    
    for i in range(len(linkCount)):
        for j in range(len(linkCount)):
            out[i][j] = linkCount[i][j] * (LINK_PROBABILITY/tmp[i])
    return out

def get_leap_prob(amount_of_nodes):
    return arr.create2D(amount_of_nodes, amount_of_nodes, LEAP_PROBABILITY/amount_of_nodes)

def print_arr_2d(arr):
    for a in arr:
        print(a)

def update_histogram(arr_val):
    # Create or update the histogram
    data = {}
    for i in range(len(arr_val)):
        data[str(i)] = arr_val[i]
    courses = list(data.keys())
    values = list(data.values())
      
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 1)
    
    plt.xlabel("Node")
    plt.ylabel("Rank")
    plt.title("Random Web Surfer")
    plt.show()

def main():
    int = rs.generate_internet(500, 25, 600)
    tm = generate_transition_matrix(int)
    #tm = generate_transition_matrix(rs.read_internet('tiny.txt'))
    random_surf(tm, 100000)
if __name__ == '__main__':
    main()