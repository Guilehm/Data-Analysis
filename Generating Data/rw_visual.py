import matplotlib.pyplot as plt

from random_walk import RandomWalk

# create random walk and plot
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # define the size of plt window
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds,
                edgecolors='none', s=8)

    # show the first and last dot
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig('graphs/rw_visual.png')
    plt.show()

    keep_running = input('Make another walk? y/n: ').lower()
    if keep_running == 'n':
        break
