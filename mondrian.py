import numpy as np
from itertools import cycle
WIDTH = 1024   
HEIGHT = 768
SPLIT_LOWER = 85
SPLIT_TOL = 1.5
rng = np.random.RandomState(None)
colors = ["yellow","red","blue","black","white","white","white","white"]
rng.shuffle(colors)
colors = cycle(colors)

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

#def choose_lines():
    
    ###
    ### function for choosing a random width of line
    ###

def split_both(x,y,w,h, list_svg):
    ###
    ### functio for making a horizontal and vertical split of rectangle
    ###
    
    #hsp - horizontal split point 
    #vsp - vertical split point
    hsp = np.random.uniform(0.33,0.68)
    vsp = np.random.uniform(0.33,0.68)
    #radnom width
    rand_width = round(hsp*w)
    #what's left from width
    width_left=w-rand_width
    #random height
    rand_height=round(vsp*h)
    #what's left from height
    height_left=h-rand_height
    mondrian(x,y,rand_width,rand_height, list_svg)
    mondrian(x+rand_width,y,width_left,rand_height, list_svg)
    mondrian(x,y+rand_height,rand_width, height_left, list_svg)
    mondrian(x+rand_width,y+rand_height,width_left,height_left, list_svg)
    
    

def split_hor(x,y,w,h, list_svg):

    ###
    ### function for making a horizontal split of rectangle, recurisve call of mondrian func
    ###
    
    hsp = np.random.uniform(0.33,0.68)
    rand_width = round(hsp * w)
    width_left = w - rand_width
    mondrian(x, y, rand_width, h, list_svg)
    mondrian(x + rand_width, y, width_left, h, list_svg)
  

def split_ver(x,y,w,h, list_svg):
    
    ###
    ### function for making a vertical split of rectangle, recursive call of mondrian func
    ###
    vsp = np.random.uniform(0.33,0.68)
    rand_height = round(vsp * h)
    height_left = h - rand_height
    mondrian(x, y, w, rand_height, list_svg)
    mondrian(x, y + rand_height, w, height_left, list_svg)
    
def mondrian(x,y,w,h, list_svg):
    
    ###
    ### functio which decides on what way a rectangle will be drawn
    ### put those rectangles in SVGlike form in list of strings
    ### which will be processed with make_svg(list) function
    ###

    if w > WIDTH/2 and h > HEIGHT/2:
        split_both(x,y,w,h,list_svg)
    elif w > WIDTH/2:
        split_hor(x,y,w,h, list_svg)
    elif h > HEIGHT/2:
        split_ver(x,y,w,h,list_svg)
    else:
        hsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * w) + 1, \
                                         SPLIT_LOWER + 1))
        #print(hsplit)
        vsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * h) + 1, \
                       SPLIT_LOWER + 1))
        #print(vsplit)
        if hsplit < w and vsplit < h:
            split_both(x,y,w,h, list_svg)
        elif hsplit < w:
            split_hor(x,y,w,h, list_svg)
        elif vsplit < h:
            split_ver(x,y,w,h, list_svg)
        else:
            color2 = next(colors)
            color = choose_color()
            #widdth = choose_width();
            list_svg.append('<rect x="{}" y="{}" width="{}" height="{}" style="fill: {}"/>'.format(x, y, w, h, color2))
            list_svg.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x,y,x+w,y))
            list_svg.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x,y+h,x,y))
            list_svg.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x+w,y+h,x+w,y))
            list_svg.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x+w,y+h,x,y+h))
list_svg=['<?xml version="1.0" encoding="utf-8"?>',
               '<svg xmlns="http://www.w3.org/2000/svg"',
               ' xmlns:xlink="http://www.w3.org/1999/xlink" width="{}"'
               ' height="{}" >'.format(WIDTH, HEIGHT),
               '<defs>',
               '    <style type="text/css"><![CDATA[',
               '        line {',
               '        stroke: #000;',
               '        stroke-width: 5px;',
               '        }',
               '    ]]></style>'
               '</defs>']
mondrian(0,0,1024,768, list_svg)
list_svg.append("</svg>")
#creating list_svg as a string with '\n' to send it as a argument to write
list_svg = '\n'.join(list_svg)
with open('example.svg', 'w') as fo:
            fo.write(list_svg)
#print(list_svg)


