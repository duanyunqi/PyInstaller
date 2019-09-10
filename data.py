import pandas as pd

from sklearn.cluster import KMeans


def data_cluster(data, n):
    kmeans = KMeans(n_clusters=n, random_state=9)
    result = kmeans.fit(data)
    labels = kmeans.labels_
    cluster_centers = pd.DataFrame(kmeans.cluster_centers_)

    return labels, cluster_centers

filename = input('请输入文件名称：')

print("*******************读取文件***************")
data = pd.read_csv(filename + '.csv')
data = data.set_index('date')

print('*******************典型日生成*************')
labels, cluster_center = data_cluster(data, 4)

print('*******************保存结果***************')
data_excel = pd.DataFrame(labels).to_csv(filename + '_result.csv', index=False)

input('Press Enter to exit...')

