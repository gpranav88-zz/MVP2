import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
import copy
import asyncio
from asyncio import coroutine
random_state = 170
clusterSize = 10


def generate_data():
    data = []
    with open("dataset/total_order_user.csv", 'r') as f:
        user_data = list(csv.reader(f))

    # First element is total_order
    # Second element is total_amount
    # Third element is avg_amount
    # Fourth element is email
    for order in user_data:
        temp_data = [float(order[0])]
        temp_data.append(float(order[1]))
        temp_data.append(temp_data[1]/temp_data[0])
        temp_data.append(order[2])
        data.append(temp_data)
    return data


@coroutine
def write_mapping_to_csv(email_mapping, title):
    title = title.replace(' ', '_')
    for mapping in email_mapping:
        file_name = title+"cluster_"+str(mapping) + '.csv'
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
                map = {'order_id': '', 'hex_code': ''}
                map['order_id'] = d[-1]
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
def total_order_vs_avg_amount_graph(data):
    graph_data = copy.deepcopy(data)
    # Calculating percentage cancelled and Refund
    temp_graph_data = []
    for temp in graph_data:
        if (((temp[0]-temp[1])/temp[0])*100) >= 0:
            temp[2] = (((temp[0]-temp[1])/temp[0])*100)
            temp_graph_data.append(temp)

    yield from plot_graph(temp_graph_data, 222, "Total order vs Average Amount", 0, 2,
               'Total Order', 'Average Amount')


def main():
    data = generate_data()
    yield from total_order_vs_avg_amount_graph(data)
    pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())