import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# show title and axis names
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# define the size of labels
plt.tick_params(axis='both', labelsize=14)

plt.savefig('graphs/mpl_squares.png')
plt.show()


