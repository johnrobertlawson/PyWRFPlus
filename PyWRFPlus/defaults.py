""" Default settings that are used when the user does not specify their own.

"""

class Defaults:
    def __init__(self):
        self.domain = 1 
        self.font_prop = {'family':'sans-serif','sans-serif':['Liberation Sans'],
                          'weight':'normal','size':14}
        self.usetex = 0
        self.dpi = 200
        self.plot_titles = 1   # Generate a title for each plot
        self.basemap_res = 'i'  # Resolution of basemap coasts etc
