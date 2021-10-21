import numpy as np
import pickle as pkl
import networkx as nx
import scipy.sparse as sp
import sys

dataset_str = sys.argv[1]

def parse_index_file(filename):
    """Parse index file."""
    index = []
    for line in open(filename):
        index.append(int(line.strip()))
    return index


def load_data():
    """Load data."""
    names = ['x', 'y', 'tx', 'ty', 'allx', 'ally', 'graph']
    objects = []
    for i in range(len(names)):
        with open("./{}/ind.{}.{}".format(dataset_str, dataset_str, names[i]), 'rb') as f:
            if sys.version_info > (3, 0):
                objects.append(pkl.load(f, encoding='latin1'))
            else:
                objects.append(pkl.load(f))

    x, y, tx, ty, allx, ally, graph = tuple(objects)
    test_idx_reorder = parse_index_file(
        "./{}/ind.{}.test.index".format(dataset_str, dataset_str))
    test_idx_range = np.sort(test_idx_reorder)

    if dataset_str == 'citeseer':
        # Fix citeseer dataset (there are some isolated nodes in the graph)
        # Find isolated nodes, add them as zero-vecs into the right position
        test_idx_range_full = range(
            min(test_idx_reorder), max(test_idx_reorder)+1)
        tx_extended = sp.lil_matrix((len(test_idx_range_full), x.shape[1]))
        tx_extended[test_idx_range-min(test_idx_range), :] = tx
        tx = tx_extended
        ty_extended = np.zeros((len(test_idx_range_full), y.shape[1]))
        ty_extended[test_idx_range-min(test_idx_range), :] = ty
        ty = ty_extended

    features = sp.vstack((allx, tx)).tolil()
    adj = nx.adjacency_matrix(nx.from_dict_of_lists(graph))

    labels = np.vstack((ally, ty))

    return adj, features, labels


def write_edge_list(adj):
    adj = adj.tolil()
    f = open("{}/{}_edgelist.txt".format(dataset_str, dataset_str), "w")
    n_row = 0
    for row in adj.rows:
        for i in range(len(row)):
            f.write("{} {}\n".format(n_row, row[i]))
        n_row += 1

    f.close()


def write_features(features):
    f = open("{}/{}.features".format(dataset_str, dataset_str), "w")
    features = features.tolil()
    feature_dim = features.shape[1]
    n_row = 0
    for row in features.rows:
        f.write("{}".format(n_row))
        feat = np.zeros(feature_dim)
        feat[row] = 1
        for i in range(feature_dim):
            f.write(" {}".format(int(feat[i])))
        f.write("\n")
        n_row += 1
    f.write("Now the file has more content!")
    f.close()


def write_labels(labels):
    f = open("{}/{}_labels.txt".format(dataset_str, dataset_str), "w")
    labels = np.argmax(labels, axis=1)
    for i in range(len(labels)):
        f.write("{} {}\n".format(i, labels[i]))
    f.close()


def main():
    adj, features, labels = load_data()
    write_edge_list(adj)
    write_features(features)
    write_labels(labels)


if __name__ == "__main__":
    main()