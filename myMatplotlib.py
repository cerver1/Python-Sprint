# import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt
import numpy as np

# Functional Method

x = np.linspace(0,5,11)
y = x ** 2
'''
print(x)
print(y)
plt.subplot(1,2,1)
plt.plot(x,y, 'r')
plt.subplot(1,2,2)
plt.plot(y,x, 'b')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()
'''
# Object Oriented Method
'''
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes.plot(x,y)
axes2.plot(y,x)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('LARGER')
axes2.set_title('SMALLER')
plt.show()
'''

'''
fig, axes = plt.subplots(1,2)
# to fix overlapping numbers
plt.tight_layout()

# you can iterate over the figures within the subplot
for current_ax in axes:
    current_ax.plot(x,y)

# you can also index over the subplots
axes[0].plot(x,y)

# Figure size and DPI

fig = plt.figure(figsize=(8,2))
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


'''

# save Figure to a file
# fig.savefig('my_picture.png', dpi = 200)

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label = 'X Squared')
ax.plot(x,x**3, label = 'X Cubed')

ax.legend(loc=0)
plt.show()