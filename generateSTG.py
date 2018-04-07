#!/usr/bin/env python

#########################################
# Mattia Corradi - Dalla Chiara Michele #
#########################################

# coding=utf-8
import graphviz as gv
import functools
import sys
import os

digraph = functools.partial(gv.Digraph, format='png')


if len(sys.argv) == 1:
    print "Non hai messo come parametro il nome del file blif"
    exit()

blifFileName = sys.argv[1]


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


def parse_blif():
    with open(blifFileName) as f:
        lines = f.read().splitlines()

        start_pos = None
        stop_pos = None

        for i in range(len(lines)):
            if lines[i] == "#STG-START":
                start_pos = i+1
            if lines[i] == "#STG-STOP":
                stop_pos = i-1

        if start_pos is None:
            print "Manca il marcatore #STG-START. Assicurati di metterlo nella riga precedente alle transizioni"
            exit()

        if stop_pos is None:
            print "Manca il marcatore #STG-STOP. Assicurati di metterlo nella riga successiva alle transizioni"
            exit()

        lines = lines[start_pos:stop_pos]

        edges = []
        nodes = []

        for line in lines:
            line = line.split(' ')

            nodes.append(line[1])
            nodes.append(line[2])

            line = (line[1], line[2])

            edges.append(line)

        nodes = set(nodes)
        edges = set(edges)

        return {'edges': edges, 'nodes': nodes}


def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph


def render_graph():
    data = parse_blif()

    edges = data['edges']
    nodes = list(data['nodes'])
    #nodes.sort()

    g = add_edges(
        add_nodes(digraph(), nodes),
        edges
    )

    g = apply_styles(g, styles)
    g.render('fsm')
    try:
        os.remove('fsm')
    except OSError:
        pass
    print "STG generata correttamente!"



styles = {
    'graph': {
        'label': 'STG - Mattia Corradi Dalla Chiara Michele',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
        'splines': 'true',
        'overlap': 'false'
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'circle',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
        'arrowsize': '.5'
    }
}

render_graph()