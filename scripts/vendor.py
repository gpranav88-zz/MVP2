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
    vendor_data = []
    unique_vendor = set()

    with open("dataset/vendor_amount_less_than_10.csv") as f:
        vendor_order_less_than_ten = list(csv.reader(f))
    with open("dataset/vendor_amount_greater_than_10.csv") as f:
        vendor_order_greater_than_ten = list(csv.reader(f))

    vendor_less_than_10 = {}
    vendor_greater_than_10 = {}

    for d in vendor_order_less_than_ten:
        vendor_less_than_10[d[1]] = d[0]
        unique_vendor.add(d[1])

    for d in vendor_order_greater_than_ten:
        vendor_greater_than_10[d[1]] = d[0]
        unique_vendor.add(d[1])

    for vendor_id in unique_vendor:
        # First element is vendor id
        # Second element is vendor total order count
        # Third element is less than ten percent margin order count
        # Fourth element is greater than ten percent margin
        temp_data = [vendor_id]
        less_than_10_order = int(vendor_less_than_10.get(vendor_id, 0))
        greater_than_10_order = int(vendor_greater_than_10.get(vendor_id, 0))

        temp_data.append(less_than_10_order+greater_than_10_order)
        temp_data.append(less_than_10_order)
        temp_data.append(greater_than_10_order)

        vendor_data.append(temp_data)
    return vendor_data


def generate_data_after_jan():
    vendor_data_after_jan = []
    unique_vendor_after_jan = set()

    with open("dataset/vendor_amount_less_than_10_after_january.csv") as f:
        vendor_order_less_than_ten_after_jan = list(csv.reader(f))
    with open("dataset/vendor_amount_greater_than_10_after_january.csv") as f:
        vendor_order_greater_than_ten_after_jan = list(csv.reader(f))

    vendor_less_than_10_after_jan = {}
    vendor_greater_than_10_after_jan = {}

    for d in vendor_order_less_than_ten_after_jan:
        vendor_less_than_10_after_jan[d[1]] = d[0]
        unique_vendor_after_jan.add(d[1])

    for d in vendor_order_greater_than_ten_after_jan:
        vendor_greater_than_10_after_jan[d[1]] = d[0]
        unique_vendor_after_jan.add(d[1])

    for vendor_id in unique_vendor_after_jan:
        # First element is vendor id
        # Second element is vendor total order count
        # Third element is less than ten percent margin order count
        # Fourth element is greater than ten percent margin
        temp_data = [vendor_id]
        less_than_10_order = int(vendor_less_than_10_after_jan.get(vendor_id, 0))
        greater_than_10_order = int(vendor_greater_than_10_after_jan.get(vendor_id, 0))

        temp_data.append(less_than_10_order + greater_than_10_order)
        temp_data.append(less_than_10_order)
        temp_data.append(greater_than_10_order)

        vendor_data_after_jan.append(temp_data)
    return vendor_data_after_jan


def write_mapping_to_csv(email_mapping, title):
    title = title.replace(' ', '_')
    for mapping in email_mapping:
        file_name = title+"_cluster_"+str(mapping) + '.csv'
        with open(file_name, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=['vendor_id', 'hex_code'])
            writer.writeheader()
            writer.writerows(email_mapping[mapping])


def get_email_cluster_mapping(data, scatter_data, y_pred, title):
    email_cluster_mapping = {}
    for i in range(0, clusterSize):
        email_cluster_mapping[i] = []
    for d in data:
        for i in range(0, clusterSize):
            if y_pred[data.index(d)] == i:
                map = {'vendor_id': '', 'hex_code': ''}
                map['vendor_id'] = d[0]
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
    write_mapping_to_csv(email_cluster_mapping, title)


def plot_graph(data, plotId, title, posX, posY, xAxisLabel, yAxisLabel):
    graph_data = copy.deepcopy(data)

    temp_graph_data = []
    for _data in graph_data:
        temp = []
        greater_than_10 = (_data[3] / _data[1]) * 100
        less_than_10 = (_data[2] / _data[1]) * 100
        temp.append(greater_than_10)
        temp.append(less_than_10)

        temp_graph_data.append(temp)

    npData = np.array(temp_graph_data, dtype=np.float)
    y_pred = KMeans(n_clusters=clusterSize, random_state=random_state).fit_predict(npData)
    plt.subplot(plotId)
    scatter_data = plt.scatter(npData[:, posX], npData[:, posY], c=y_pred)
    plt.title(title)
    plt.xlabel(xAxisLabel)
    plt.ylabel(yAxisLabel)
    plt.subplots_adjust(hspace=.5)
    plt.show()
    get_email_cluster_mapping(graph_data, scatter_data, y_pred, title)


# data = generate_data()
# plot_graph(data, 221,
#            "Greater vs Less than 10 % margin order count", 0, 1, "Greater than 10 % margin", "Less than 10 % margin")

data_after_jan = generate_data_after_jan()
plot_graph(data_after_jan, 111,
           "Greater vs Less than 10 % margin order count", 0, 1, "Greater than 10 % margin",
           "Less than 10 % margin")

plt.show()