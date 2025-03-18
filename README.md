# mcnet-gsoc-test

# Particle Event Analysis and Visualization

This project provides a set of Python scripts and a web server for analyzing and visualizing particle collision events. It parses event data, generates particle interaction graphs, and serves the data through a simple web application.

## Features

- **MC Event File Parsing**: A Python script that processes particle collision data from an event file, extracts key information (e.g., particle count, momentum sums), and plots the transverse-momentum distribution of top quarks.
  
- **Event-Graph Rendering**: A Python script that visualizes particle interactions as node-edge diagrams. The graph is rendered using libraries like `NetworkX`, and `matplotlib`.

- **Web Server**: A Flask web server that reads particle collision event data from a JSON file and serves it via an endpoint. The data can be visualized interactively in a web browser using front-end scripts (HTML/JavaScript).

## Live Demo

You can try out the live demo of the web application here:  
[Live Demo on PythonAnywhere](https://mcnetmayank.pythonanywhere.com)

## Requirements

To run this project locally, you need to install the following Python packages:

- `pyhepmc` (for processing event file Ex. (.LHE))
- `Flask` (for web server)
- `matplotlib` (for plotting)
- `numpy` (for numerical computations)
- `networkx` (for graph rendering)

