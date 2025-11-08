# BFS_LAB1.py
# BSD3513 - Introduction to Artificial Intelligence
# Chapter 2: Breadth-First Search (BFS)
# Developed by: [Your Name] | [Your Student ID]
# Lecturer: Dr. Ku Muhammad Na’im Ku Khalif

import streamlit as st
from collections import deque

st.set_page_config(page_title="BFS Search Algorithm", page_icon="🔍")

st.title("🔍 Breadth-First Search (BFS)")
st.subheader("AI Search Algorithm Demonstration")
st.write("This Streamlit app demonstrates how **Breadth-First Search (BFS)** works on a directed graph "
         "based on the topic from Chapter 2: Search Algorithms.")

# Define the directed graph
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'G': ['F', 'H'],
    'H': [],
    'F': []
}

st.subheader("Graph Structure")
st.json(graph)

# BFS Function
def bfs(graph, start):
    visited = []
    queue = deque([(start, 0)])  # Include level tracking
    levels = {start: 0}
    
    while queue:
        node, level = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbour in sorted(graph[node]):  # Alphabetical order
                if neighbour not in visited and neighbour not in levels:
                    queue.append((neighbour, level + 1))
                    levels[neighbour] = level + 1
    return visited, levels

# Input Section
start_node = st.text_input("Enter the starting node (default = A):", "A").upper()

if st.button("Run BFS"):
    if start_node in graph:
        result, level = bfs(graph, start_node)
        st.success(f"Traversal Order: {' → '.join(result)}")
        st.write("### Level Explanation:")
        for node in result:
            st.write(f"**Level {level[node]}:** {node}")
        st.info("BFS explores all nodes level by level using a queue (FIFO).")
    else:
        st.error("Invalid node. Please enter a valid node label (A–H).")

st.markdown("---")
st.caption("Developed for BSD3513 – Introduction to Artificial Intelligence | UMPSA 2025")
