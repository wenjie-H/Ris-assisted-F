import matplotlib.pyplot as plt
import numpy as np

def plot_gps_points(points_list1, points_list2):

    plt.figure()
    for i, point in enumerate(points_list1):
        # 解析起始点坐标集合
        plt.plot(point[1], point[0], 'ro')
        plt.text(point[1], point[0], str(i+1), color='black', fontsize=12)

        # plt.scatter(start_x, start_y, color=color, marker=marker_start, label='Start {}'.format(i + 1))
        # plt.scatter(end_x, end_y, color=color, marker=marker_end, label='End {}'.format(i + 1))

    for i, point in enumerate(points_list2):
        plt.plot(point[1], point[0], 'bs', markersize ='20')


    # 绘制路径
    # path_coordinates = list(zip(*points_list))  # 将GPS坐标转置
    # plt.plot(path_coordinates[1], path_coordinates[0], 'b-')

    # 设置图形标题和轴标签
    plt.title('GPS Coordinates')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # 显示图形
    plt.show()

# def plot_gps_points(points_list):
#
#     plt.figure()
#     for i, point in enumerate(points_list):
#         # 解析起始点坐标集合
#         plt.plot(point[1], point[0], 'ro')
#         # plt.text(point[1], point[0], str(i+1), color='black', fontsize=12)
#
#         # plt.scatter(start_x, start_y, color=color, marker=marker_start, label='Start {}'.format(i + 1))
#         # plt.scatter(end_x, end_y, color=color, marker=marker_end, label='End {}'.format(i + 1))
#
#     # 绘制路径
#     # path_coordinates = list(zip(*points_list))  # 将GPS坐标转置
#     # plt.plot(path_coordinates[1], path_coordinates[0], 'b-')
#
#     # 设置图形标题和轴标签
#     plt.title('GPS Coordinates')
#     plt.xlabel('Longitude')
#     plt.ylabel('Latitude')
#
#     # 显示图形
#     plt.show()



def plot_gps_coordinates(start_coords_list, end_coords_list):
    # 创建一个新的图形
    plt.figure()

    colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan']
    markers_start = ['o', 's', '^', 'D', 'v', 'p']
    markers_end = ['x', '*', '+', 'h', 'H', 'd']

    # 绘制每个起始点和终止点集合
    for i, (start_coords, end_coords) in enumerate(zip(start_coords_list, end_coords_list)):
        # 解析起始点坐标集合
        start_x, start_y = zip(*start_coords)
        # 解析终止点坐标集合
        end_x, end_y = zip(*end_coords)

        # 使用不同颜色和标识符号绘制起始点和终止点
        color = colors[i % len(colors)]
        marker_start = markers_start[i % len(markers_start)]
        marker_end = markers_end[i % len(markers_end)]

        plt.scatter(start_x, start_y, color=color, marker=marker_start, label='Start {}'.format(i + 1))
        plt.scatter(end_x, end_y, color=color, marker=marker_end, label='End {}'.format(i + 1))

    # 添加图例和标签
    plt.legend()
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('GPS Coordinates')

    # 显示图形
    plt.show()

# import matplotlib.pyplot as plt

def plot_points_and_path(start_points, end_points, path_points):
    # 绘制起始点和终止点
    plt.scatter(start_points[:, 0], start_points[:, 1], c='b', marker='o')
    plt.scatter(end_points[:, 0], end_points[:, 1], c='r', marker='*')

    # 绘制路径连接起始点和终止点
    for i in range(len(path_points)-1):
        plt.plot([path_points[i][0], path_points[i+1][0]], [path_points[i][1], path_points[i+1][1]], 'k-')

    # 设置图形的标题和坐标轴标签
    plt.title('Points and Path')
    plt.xlabel('X')
    plt.ylabel('Y')

    # 显示图形
    plt.show()

# 示例用法
# start_points = [[1, 2], [3, 4], [5, 6]]
# end_points = [[7, 8], [9, 10], [11, 12]]
# start_points = np.array(start_points)
# end_points = np.array(end_points)
#
# plot_points_and_path(start_points, end_points, end_points)




if __name__ == '__main__':
    # print([1, 2, 3][:-2])
    # 示例起始点集合和终止点集合
    start_coords_list = [[(39.9526, -75.1652), (40.7128, -74.0060), (34.0522, -118.2437)],
                         [(35.6895, 139.6917), (37.7749, -122.4194), (25.7617, -80.1918)]]

    end_coords_list = [[(51.5074, -0.1278), (48.8566, 2.3522), (55.7558, 37.6176)],
                       [(55.7558, 37.6176), (51.5074, -0.1278), (48.8566, 2.3522)]]

    # 调用函数绘制图形
    plot_gps_coordinates(start_coords_list, end_coords_list)
    plot_gps_points([[30.685394, 104.003916, [0, 1]], [30.60732, 103.994267, [16, 1]], [30.577097, 103.963192, [0, 2]], [30.577097, 103.963192, [16, 2]], [30.675359, 104.046551, [0, 1]], [30.678060297808, 104.05418942944, [7, 1]], [30.678060297808, 104.05418942944, [15, 1]], [30.675295, 104.061003, [8, 1]], [30.637527535869, 104.05636939418, [3, 1]], [30.6638011932373, 104.073989868164, [10, 1]], [30.665198371012, 104.08001449556, [18, 1]], [30.659773, 104.080276, [8, 2]], [30.659116, 104.082644, [9, 1]], [30.663919, 104.084189, [11, 1]], [30.65433, 104.090191, [1, 1]], [30.671722, 104.090585, [12, 1]], [30.648959993664, 104.09670764933, [5, 1]], [30.559576, 104.074565, [2, 1]], [30.520522, 104.075599, [1, 2]], [30.412591, 104.085186, [6, 1]], [30.412591, 104.085186, [13, 1]], [30.412591, 104.085186, [14, 1]], [30.412591, 104.085186, [17, 1]], [30.412591, 104.085186, [19, 1]], [30.649975, 104.055247, [17, 2]], [30.692581, 104.080304, [6, 2]], [30.652973662622, 104.13253514373, [4, 1]], [30.635729, 104.145823, [2, 2]], [30.635729, 104.145823, [4, 2]], [30.635729, 104.145823, [11, 2]], [30.635729, 104.145823, [18, 2]], [30.583803, 103.964871, [5, 2]], [30.577097, 103.963192, [3, 2]], [30.577097, 103.963192, [7, 2]], [30.577097, 103.963192, [9, 2]], [30.577097, 103.963192, [10, 2]], [30.577097, 103.963192, [12, 2]], [30.577097, 103.963192, [13, 2]], [30.577097, 103.963192, [14, 2]], [30.577097, 103.963192, [15, 2]], [30.577097, 103.963192, [19, 2]]])
    plot_gps_points([[30.685394, 104.003916], [30.675359, 104.046551], [30.678060297808, 104.05418942944], [30.678060297808, 104.05418942944], [30.675295, 104.061003], [30.6638011932373, 104.073989868164], [30.665198371012, 104.08001449556], [30.659773, 104.080276], [30.659116, 104.082644], [30.577097, 103.963192], [30.577097, 103.963192], [30.65433, 104.090191], [30.648959993664, 104.09670764933], [30.412591, 104.085186], [30.663919, 104.084189], [30.559576, 104.074565], [30.671722, 104.090585], [30.412591, 104.085186], [30.637527535869, 104.05636939418], [30.652973662622, 104.13253514373], [30.577097, 103.963192], [30.577097, 103.963192], [30.577097, 103.963192], [30.577097, 103.963192], [30.577097, 103.963192], [30.412591, 104.085186], [30.60732, 103.994267], [30.412591, 104.085186], [30.583803, 103.964871], [30.412591, 104.085186], [30.520522, 104.075599], [30.577097, 103.963192], [30.577097, 103.963192], [30.577097, 103.963192], [30.577097, 103.963192], [30.635729, 104.145823], [30.635729, 104.145823], [30.635729, 104.145823], [30.635729, 104.145823], [30.649975, 104.055247], [30.692581, 104.080304]])