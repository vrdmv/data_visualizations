import matplotlib.pyplot as plt

from randomwalk_code import RandomWalk

# Keep making new walks, as long as the program is active.
active = True
while active:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none',
                s=1)
    plt.scatter(0, 0, c='green', edgecolor='none', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black',
                edgecolors='none',
                s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (yes/no): ")
    if keep_running == 'no':
        print("Thank you.")
        active = False
