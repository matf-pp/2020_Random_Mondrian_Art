import numpy as np
WIDTH = 1024   
HEIGHT = 768
SPLIT_LOWER = 85
SPLIT_TOL = 1.5

def choose_color():
    
    ###
    ### function for choosing a random color for rectangele 
    ###
    
    clrs = []
    n = np.random.randint(4,900)
    for i in range(n):
        rv = np.random.exponential()
        if rv < 0.15:
            clrs.append("red")
        elif rv < 0.30:
            clrs.append("skyblue")
        elif rv < 0.50:
            clrs.append("yellow")
        elif rv < 0.70:
            clrs.append("black")
        else:
            clrs.append("white")
    np.random.shuffle(clrs)
    color = np.random.choice(clrs)
    return color

def choose_lines():
    
    ###
    ### function for choosing a random width of line
    ###

def split_both(x,y,w,h):
    
    ###
    ### functio for making a horisontal and vertical split of rectangle
    ###

def split_hor(x,y,w,h):

    ###
    ### function for making a horisontal split of rectangle, recurisve call of mondrian func
    ###

def split_ver(x,y,w,h):
    
    ###
    ### function for making a vertical split of rectangle, recursive call of mondrian func
    ###

def make_svg():

    ###
    ### function which recives a list of string and makes
    ###


def mondrian(x,y,w,h):
    
    ###
    ### functio which decides on what way a rectangle will be drawn
    ### put those rectangles in SVGlike form in list of strings
    ### which will be processed with make_svg(list) function
    ###

    if w > WIDTH/2 and h > HEIGHT/2:
        split_both(x,y,w,h)
    elif w > WIDTH/2:
        split_hor(x,y,w,h)
    elif h > HEIGHT/2:
        split_ver(x,y,w,h)
    else:
        hsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * w) + 1, \
                                         SPLIT_LOWER + 1))
        #print(hsplit)
        vsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * h) + 1, \
                       SPLIT_LOWER + 1))
        #print(vsplit)
        if hsplit < w and vsplit < h:
            split_both(x,y,w,h)
        elif hsplit < w:
            split_hor(x,y,w,h)
        elif vsplit < h:
            split_ver(x,y,w,h)
        else:
        #choose_color() call
        #choose_width() call
        #apend in list in SVGlike format
if __name__ == '__main__':
    ###
    ### determinating screen resolutio in crossplatfor environment is possible with
    ### pyGtk, pyQt5, wxPython, tKinter etc.
    ###
    mondrian(0,0,1024,768)
