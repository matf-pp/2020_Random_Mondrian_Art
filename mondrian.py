import numpy as np
from itertools import cycle
WIDTH = 1024   
HEIGHT = 768
SPLIT_LOWER = 85
SPLIT_TOL = 1.5


    
def make_svg(rect_list):
    
    ### fuction for writing rectangles from list in .svg file

    with open('art.svg', 'w') as file:
        svg_list= ['<?xml version="1.0" encoding="utf-8"?>',
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
        svg_list.extend(rect_list)
        svg_list.append('</svg>')
        svg_str = '\n'.join(svg_list)
        file.write(svg_str)

def split_both(x,y,w,h, rect_list):

    ### functio for making a horizontal and vertical split of rectangle

    hsp = np.random.uniform(0.33,0.68) #hsp - horizontal split point
    vsp = np.random.uniform(0.33,0.68) #vsp - vertical split point
    rand_width = round(hsp*w)
    width_left=w-rand_width
    rand_height=round(vsp*h)
    height_left=h-rand_height
    mondrian(x,y,rand_width,rand_height, rect_list)
    mondrian(x+rand_width,y,width_left,rand_height, rect_list)
    mondrian(x,y+rand_height,rand_width, height_left, rect_list)
    mondrian(x+rand_width,y+rand_height,width_left,height_left, rect_list)



def split_hor(x,y,w,h, rect_list):

    ### function for making a horizontal split of rectangle, recurisve call of mondrian func

    hsp = np.random.uniform(0.33,0.68)
    rand_width = round(hsp * w)
    width_left = w - rand_width
    mondrian(x, y, rand_width, h, rect_list)
    mondrian(x + rand_width, y, width_left, h, rect_list)


def split_ver(x,y,w,h, rect_list):

    ### function for making a vertical split of rectangle, recursive call of mondrian func

    vsp = np.random.uniform(0.33,0.68)
    rand_height = round(vsp * h)
    height_left = h - rand_height
    mondrian(x, y, w, rand_height, rect_list)
    mondrian(x, y + rand_height, w, height_left, rect_list)

def mondrian(x,y,w,h, rect_list):

    ### functio which decides on what way a rectangle will be drawn
    ### put those rectangles in SVGlike form in list of strings
    ### which will be processed with make_svg(list) function

    if w > WIDTH/2 and h > HEIGHT/2:
        split_both(x,y,w,h,rect_list)
    elif w > WIDTH/2:
        split_hor(x,y,w,h, rect_list)
    elif h > HEIGHT/2:
        split_ver(x,y,w,h,rect_list)
    else:
        hsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * w) + 1, \
                                         SPLIT_LOWER + 1))
        vsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * h) + 1, \
                       SPLIT_LOWER + 1))
        if hsplit < w and vsplit < h:
            split_both(x,y,w,h, rect_list)
        elif hsplit < w:
            split_hor(x,y,w,h, rect_list)
        elif vsplit < h:
            split_ver(x,y,w,h, rect_list)
        else:
            color = next(colors)
            rect_list.append('<rect x="{}" y="{}" width="{}" height="{}" style="fill: {}"/>'.format(x, y, w, h, color))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x,y,x+w,y))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x,y+h,x,y))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x+w,y+h,x+w,y))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x+w,y+h,x,y+h))

## mondrian and make_svg is called in main()
def function(w, h, cl):
    global colors 
    colors = cycle(cl)
    rect_list = []
    mondrian(0, 0, w, h, rect_list)
    make_svg(rect_list)


function(1090, 720, ['red', 'blue', 'yellow'])
