import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
import copy

n_samples = 1500
random_state = 170


def generate_data():
    data = []
    with open("dataset/cancel.csv", 'r') as f:
        cancel_data = list(csv.reader(f))
    with open("dataset/refund.csv", 'r') as f:
        refund_data = list(csv.reader(f))
    with open("dataset/order.csv", 'r') as f:
        order_data = list(csv.reader(f))

    cancel_dict = {}
    for d in cancel_data:
        cancel_dict[d[1]] = d[0]

    refund_dict = {}
    for d in refund_data:
        refund_dict[d[1]] = d[0]

    order_dict = {}
    for d in order_data:
        order_dict[d[1]] = d[0]

    # First element is total order count
    # Second element is refunded order count
    # Third element is cancelled order count
    # Fourth element is user email
    for email in order_dict:
        if int(order_dict[email]) > 5:
            temp_data = [int(order_dict[email])]
            temp_data.append(int(refund_dict.get(email, 0)))
            temp_data.append(int(cancel_dict.get(email, 0)))
            temp_data.append(email)
            data.append(temp_data)
    return data


def plot_graph(data, plotId, title, posX, posY):
    npData = np.array(data, dtype=np.float)
    y_pred = KMeans(n_clusters=10, random_state=random_state).fit_predict(npData)
    plt.subplot(plotId)
    plt.scatter(npData[:, posX], npData[:, posY], c=y_pred)
    plt.title(title)


def refund_vs_total_order(data):
    graph_data = copy.deepcopy(data)
    # Removing email from the data for plotting
    graph_data = [temp[:-1] for temp in graph_data]
    plot_graph(graph_data, 221, "Refund vs Total Order Count", 0, 1)


def cancelled_vs_total_order(data):
    graph_data = copy.deepcopy(data)
    # Removing email from the data for plotting
    graph_data = [temp[:-1] for temp in graph_data]
    plot_graph(graph_data, 223, "Cancelled vs Total Order Count", 0, 2)


def refund_vs_cancel_percent_graph(data):
    graph_data = copy.deepcopy(data)
    # Removing email from the data for plotting
    graph_data = [temp[:-1] for temp in graph_data]
    # Calculating percentage cancelled and Refund
    temp_graph_data = []
    for temp in graph_data:
        # Consider only order count greater than 5
        if temp[0] > 5:
            temp[1] = temp[1]*100/temp[0]
            temp[2] = temp[2]*100 / temp[0]
            temp_graph_data.append(temp)

    plot_graph(temp_graph_data, 222, "Refund vs Cancelled Order Percentage", 1, 2)


data = generate_data()
refund_vs_cancel_percent_graph(data)
refund_vs_total_order(data)
cancelled_vs_total_order(data)
plt.show()
