import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
pd.options.plotting.backend = "plotly"


def annotate(x, y, text, xytext, ax=None):
    text = text
    if not ax:
        ax = plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops = dict(arrowstyle='->', fc="k", ec="k", lw=4)
    kw = dict(xycoords='data', textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="left", va="top", size=15)
    ax.annotate(text, xy=(x, y), xytext=xytext, **kw)
    annotate_outline(x, y, text, xytext)


def annotate_outline(x, y, text, xytext, ax=None):
    text = text
    if not ax:
        ax = plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops = dict(arrowstyle='->', color='w', lw=2)
    kw = dict(xycoords='data', textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="left", va="top", size=15)
    ax.annotate(text, xy=(x, y), xytext=xytext, **kw)


def annotate_arrow_reverse(x, y, text, xtext, ytext, ax=None):
    text = text
    if not ax:
        ax = plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops = dict(arrowstyle='<-', fc="k", ec="k", lw=4)
    kw = dict(xycoords='data', textcoords='data',
              arrowprops=arrowprops, bbox=bbox_props, ha="left", va="top", size=10)
    ax.annotate(text, xy=(x, y), xytext=(xtext, ytext), **kw)
    annotate_outline_arrow_reverse(x, y, text, xtext, ytext)


def annotate_outline_arrow_reverse(x, y, text, xtext, ytext, ax=None):
    text = text
    if not ax:
        ax = plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops = dict(arrowstyle='<-', color='w', lw=2)
    kw = dict(xycoords='data', textcoords='data',
              arrowprops=arrowprops, bbox=bbox_props, ha="left", va="top", size=10)
    ax.annotate(text, xy=(x, y), xytext=(xtext, ytext), **kw)


img = mpimg.imread('images/Fluid_Edge_24U_Liquid_Cooled.original.JPG')
imgplot = plt.imshow(img)
plt.axis('off')
annotate(800, 600, 'This is a Rack', (0.15, 0.60))
plt.tight_layout()
plt.savefig('images/annotate_Fluid_Edge_24U_Liquid_Cooled.original.JPG', dpi=1500, pad_inches=0, bbox_inches='tight')  # bbox_inches='tight'
