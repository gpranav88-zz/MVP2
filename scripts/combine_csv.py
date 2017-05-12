import csv

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

for email in order_dict:
    temp_data = {}
    temp_data['email'] = email
    temp_data['cancelled'] = int(refund_dict.get(email, 0))
    temp_data['refund'] = int(cancel_dict.get(email, 0))
    temp_data['total'] = int(order_dict[email])
    data.append(temp_data)


with open('combined_data.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['email', 'total', 'refund', 'cancelled'])
    writer.writeheader()
    writer.writerows(data)