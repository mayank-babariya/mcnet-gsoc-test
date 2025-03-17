import pyhepmc
import matplotlib.pyplot as plt
import numpy as np
import os

def start_analysis(input_file):
    top_quark_pT = []
    all_events = dict()
    with pyhepmc.open(input_file) as f:
        for event in f:
            num_particles = len(event.particles)
            final_particles = [p for p in event.particles if p.status == 1]
            num_final_particles = len(final_particles)

            total_px, total_py, total_pz, total_e = 0, 0, 0, 0
            for p in event.particles:
                total_px += p.momentum.px
                total_py += p.momentum.py
                total_pz += p.momentum.pz
                total_e += p.momentum.e

                if abs(p.pid) == 6:
                    pT = np.sqrt(p.momentum.px**2 + p.momentum.py**2)
                    top_quark_pT.append(pT)
            all_events[event.event_number] = {
                'Event Number': event.event_number,
                'Total Particles': num_particles,
                'Final state particles': num_final_particles,
                'Momentum sums': {'px':total_px,'py':total_py,'pz':total_pz,'e':total_e},
            }

    # Plot transverse momentum (pT) distribution of top quarks
    plt.figure(figsize=(8, 6))
    plt.hist(top_quark_pT, bins=30, alpha=0.7, color="b", edgecolor="black")
    plt.xlabel(r"$p_T$ of Top Quarks [GeV]")
    plt.ylabel("Frequency")
    plt.title(r"Transverse Momentum Distribution of Top Quarks")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.getcwd()+'/base/static/top_quarks.png', format="PNG")
    plt.close()
    return all_events

def get_particle_interaction():
    import networkx as nx
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go

    # Define particles and interactions (edges)
    edges = [
        ("e+", "γ"),  # e+ emits a photon
        ("e-", "γ"),  # e- emits a photon
        ("γ", "μ+"),  # Photon converts to μ+
        ("γ", "μ-"),  # Photon converts to μ-
    ]

    # Create a directed graph
    G = nx.DiGraph()
    G.add_edges_from(edges)

    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", arrows=True)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color="gray"),
        hoverinfo="none",
        mode="lines"
    )

    node_x = [pos[n][0] for n in G.nodes()]
    node_y = [pos[n][1] for n in G.nodes()]
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        text=list(G.nodes()),
        mode="markers+text",
        textposition="top center",
        marker=dict(size=20, color="lightblue"),
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(title="Interactive Particle Interaction Graph", showlegend=False)
    fig.write_html(os.getcwd()+'/base/templates/event_graph.html')
    return
