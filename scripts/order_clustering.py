import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
import copy
import asyncio
from asyncio import coroutine
n_samples = 1500
random_state = 170
clusterSize = 10


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


@coroutine
def write_mapping_to_csv(email_mapping, title):
    title = title.replace(' ', '_')
    for mapping in email_mapping:
        file_name = title+"_cluster_"+str(mapping) + '.csv'
        with open(file_name, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=['email', 'hex_code'])
            writer.writeheader()
            writer.writerows(email_mapping[mapping])

@coroutine
def get_email_cluster_mapping(data, scatter_data, y_pred, title):
    email_cluster_mapping = {}
    for i in range(0, clusterSize):
        email_cluster_mapping[i] = []
    for d in data:
        for i in range(0, clusterSize):
            if y_pred[data.index(d)] == i:
                map = {'email': '', 'hex_code': ''}
                map['email'] = d[-1]
                if data.index(d) < len(scatter_data._facecolors):
                    try:
                        if len(scatter_data._facecolors[data.index(d)]) >= 3:
                            color = scatter_data._facecolors[data.index(d)][0:3]
                            hex_color = '#%02x%02x%02x' % (
                            int(255 * color[0]), int(255 * color[1]), int(255 * color[2]))
                            map['hex_code'] = hex_color
                    except:
                        pass
                email_cluster_mapping[i].append(map)
                break
    yield from write_mapping_to_csv(email_cluster_mapping, title)


@coroutine
def plot_graph(data, plotId, title, posX, posY, xAxisLabel, yAxisLabel):
    graph_data = copy.deepcopy(data)
    # Removing email from the data for plotting
    temp_graph_data = [temp[:-1] for temp in graph_data]
    npData = np.array(temp_graph_data, dtype=np.float)
    y_pred = KMeans(n_clusters=clusterSize, random_state=random_state).fit_predict(npData)
    plt.subplot(plotId)
    scatter_data = plt.scatter(npData[:, posX], npData[:, posY], c=y_pred)
    plt.title(title)
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.subplots_adjust(hspace=.5)
    plt.show()
    asyncio.async(get_email_cluster_mapping(graph_data, scatter_data, y_pred, title))


@coroutine
def refund_vs_total_order(data):
    yield from plot_graph(data, 221, "Total vs Refunded Order Count", 0, 1, 'Total Order Count',
               'Refunded Order Count')

@coroutine
def cancelled_vs_total_order(data):
    yield from plot_graph(data, 223, "Total vs Cancelled Order Count", 0, 2, 'Total Order Count',
               'Cancelled Order Count')

@coroutine
def refund_vs_cancel_percent_graph(data):
    graph_data = copy.deepcopy(data)
    # Calculating percentage cancelled and Refund
    temp_graph_data = []
    for temp in graph_data:
        # Consider only order count greater than 5
        if temp[0] > 5:
            temp[1] = temp[1] * 100 / temp[0]
            temp[2] = temp[2] * 100 / temp[0]
            temp_graph_data.append(temp)

    yield from plot_graph(temp_graph_data, 222, "Cancelled vs Refunded Order Percentage", 1, 2,
               'Cancelled Order Percentage', 'Refunded Order Percentage')


def main():
    data = generate_data()
    # yield from refund_vs_cancel_percent_graph(data)
    # yield from refund_vs_total_order(data)
    yield from cancelled_vs_total_order(data)
    pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())