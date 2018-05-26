import matplotlib.pyplot as plt


plt.scatter(2, 4, s=200)

# define the graph title and rename axis
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# define the size of labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

