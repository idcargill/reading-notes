# Data Visualization

[Matplot Lib](https://github.com/rougier/matplotlib-tutorial)

pyplot.plot is a simpler and less customizable plot.  
Accessing properties directly in an OOP style with axes is more specific and controllable. 

plt.plot(x, y, 'r--') red dashes
plt.plot(x, y, 'bs') blue squares
plt.plot(x,y, 'g^') green triangle

## Artists

- primitives: standard graphical objects that appear on canvas
- containers: places to put primitives. Axis, Axes, and figures.


### Axes Class

Build in Figure

contains most figure elements
> Axis, Tick, Line2D, Text, Polygon...

### Subplot

- SubplotBase classes are Axes instances with additional methods.



## Labels

- plt.xlabel('str')
- plt.ylabel('str')
- plt.title('str')
- plt.text(x, y, r'text to display at coordinates')
- plt.axis([list])
- plt.grid(True)
- plt.show()
- plt.xlim()
- plt.ylim()
- plt.xticks([list])
- plt.yticks([list])
- plt.
 
## Multiple Figures and axes

- gca() returns current axes
- gcf() returns current figure
- clf() clear current figure
- cla() clear current axes


- subplot(rows, cols ,fignum)

```python
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])
```

### Multiple Plots with Axes objects

```python
fig = plt.figure()
ax = fig.add_subplot(2,1,1) # 2 rows, 1 column, first plot
ax.set_xticks([1,2,4,6])

fig2 = plt.figure()
ax2 = fig2.add_subplot(2,2,2)
ax2.set_title('Cats')
plt.show()

```


[cusomizing matplot](https://matplotlib.org/2.0.2/api/pyplot_api.html)

[Plot](https://matplotlib.org/2.0.2/users/pyplot_tutorial.html)

[plot Line API](https://matplotlib.org/stable/api/artist_api.html)

[pyplot](https://matplotlib.org/2.0.2/api/pyplot_api.html)

[Seaborn](https://seaborn.pydata.org/tutorial.html)

[Bokeh](https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb)

[Seaborn Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)

