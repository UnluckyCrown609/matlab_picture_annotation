# matlab_picture_annotation
A python file to annotate images

# How To Use

```
img = mpimg.imread('images/Fluid_Edge_24U_Liquid_Cooled.original.JPG')
imgplot = plt.imshow(img)
plt.axis('off')
annotate(800, 600, 'This is a Rack', (0.15, 0.60))
plt.tight_layout()
plt.savefig('images/annotate_Fluid_Edge_24U_Liquid_Cooled.original.JPG', dpi=1500, pad_inches=0, bbox_inches='tight')  # bbox_inches='tight'
```

- First line imports the image
- Second line import the image into a plot
- Third line turns off the axis of the plot
- Fourth line is the annotate function to put the arrow to a specific location as well as the box location
- Fifth line alters the layout to only show the picture (also can use `bbox_inches='tight'` in `plt.savefig()`)
- Sixth line save the figure in the same location under an adjusted name. (Note `dpi=1500` changes the resolution)

## Functions

- `annotate(x, y, text, xytext, ax=None)` Shows normal label with arrow to location

- `annotate_arrow_reverse(x, y, text, xtext, ytext, ax=None):` Shows normal label with reversed arrow