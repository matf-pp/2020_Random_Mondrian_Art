import numpy as np
import os

SPLIT_LOWER = 85
SPLIT_TOL = 1.5
svg_list = []
pattern_list = []
rect_list = []
ID=0


def make_svg():
    if os.path.exists("art.svg"):
        os.remove("art.svg")
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
        svg_list.extend(pattern_list)
        svg_list.extend(rect_list)
        svg_list.append('</svg>')
        svg_str = '\n'.join(svg_list)
        file.write(svg_str)
        pattern_list.clear()
        rect_list.clear()


def split_both(x,y,w,h):
    hsp = np.random.uniform(0.33,0.68)
    vsp = np.random.uniform(0.33,0.68)
    rand_width = round(hsp*w)
    width_left=w-rand_width
    rand_height=round(vsp*h)
    height_left=h-rand_height
    mondrian(x,y,rand_width,rand_height)
    mondrian(x+rand_width,y,width_left,rand_height)
    mondrian(x,y+rand_height,rand_width, height_left)
    mondrian(x+rand_width,y+rand_height,width_left,height_left)



def split_hor(x,y,w,h):
    hsp = np.random.uniform(0.33,0.68)
    rand_width = round(hsp * w)
    width_left = w - rand_width
    mondrian(x, y, rand_width, h)
    mondrian(x + rand_width, y, width_left, h)



def split_ver(x,y,w,h):
    vsp = np.random.uniform(0.33,0.68)
    rand_height = round(vsp * h)
    height_left = h - rand_height
    mondrian(x, y, w, rand_height)
    mondrian(x, y + rand_height, w, height_left)



def mondrian(x,y,w,h):
    if w > WIDTH/2 and h > HEIGHT/2:
        split_both(x,y,w,h)
    elif w > WIDTH/2:
        split_hor(x,y,w,h)
    elif h > HEIGHT/2:
        split_ver(x,y,w,h)
    else:
        hsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * w) + 1, \
                                         SPLIT_LOWER + 1))
        vsplit = np.random.uniform(SPLIT_LOWER, max(round(SPLIT_TOL * h) + 1, \
                       SPLIT_LOWER + 1))
        if hsplit < w and vsplit < h:
            split_both(x,y,w,h)
        elif hsplit < w:
            split_hor(x,y,w,h)
        elif vsplit < h:
            split_ver(x,y,w,h)
        else:
            fill = choose_fill()
            rect_list.append('<rect x="{}" y="{}" width="{}" height="{}" style="fill: {}"/>'.format(x, y, w, h, fill))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:rgb(0,0,0);stroke-width:2px" />'.format(x,y,x+w,y))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:rgb(0,0,0);stroke-width:2px" />'.format(x,y+h,x,y))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:rgb(0,0,0);stroke-width:2px" />'.format(x+w,y+h,x+w,y))
            rect_list.append('<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:rgb(0,0,0);stroke-width:2px"/>'.format(x+w,y+h,x,y+h))

def choose_fill():
    global ID
    np.random.shuffle(colors)

    if rb_ind and np.random.random_sample() > 0.8: 
        ind = np.random.randint(1, 7)
        if ind == 1:
            pattern_list.extend(['<pattern id="{}" x="0" y="0" width="25" height="25" patternUnits="userSpaceOnUse">'.format(str(ID)),
                     '<rect class="checker" x="0" width="12.5" height="12.5" y="0" fill="{}"></rect>'.format(colors[0]),
                     '<rect class="checker" x="12.5" width="12.5" height="12.5" y="12.5" fill="{}"></rect>'.format(colors[1]), 
                     '</pattern>'])
        if ind == 2:
            pattern_list.extend(['<pattern id="{}" x="0" y="0" width="15" height="15" patternUnits="userSpaceOnUse">'.format(str(ID)),
                    '<circle fill="{}" cx="5" cy="5" r="5"></circle>'.format(colors[0]),
                    '</pattern>'])
        if ind == 3:
            pattern_list.extend(['<pattern id="{}" x="0" y="0" width="30" height="47" patternUnits="userSpaceOnUse" viewBox="56 -254 112 190">'.format(str(ID)),
                    '<g id="hexagon" fill="{}">'.format(colors[1]),
                    '<path d="M168-127.1c0.5,0,1,0.1,1.3,0.3l53.4,30.5c0.7,0.4,1.3,1.4,1.3,2.2v61c0,0.8-0.6,1.8-1.3,2.2L169.3-0.3 c-0.7,0.4-1.9,0.4-2.6,0l-53.4-30.5c-0.7-0.4-1.3-1.4-1.3-2.2v-61c0-0.8,0.6-1.8,1.3-2.2l53.4-30.5C167-127,167.5-127.1,168-127.1 L168-127.1z" stroke="{}"  stroke-width="25" fill="white"></path>'.format(colors[0]),
                    '<path d="M112-222.5c0.5,0,1,0.1,1.3,0.3l53.4,30.5c0.7,0.4,1.3,1.4,1.3,2.2v61c0,0.8-0.6,1.8-1.3,2.2l-53.4,30.5 c-0.7,0.4-1.9,0.4-2.6,0l-53.4-30.5c-0.7-0.4-1.3-1.4-1.3-2.2v-61c0-0.8,0.6-1.8,1.3-2.2l53.4-30.5 C111-222.4,111.5-222.5,112-222.5L112-222.5z" stroke="{}"  stroke-width="25" fill="white"></path>'.format(colors[0]),
                    '<path d="M168-317.8c0.5,0,1,0.1,1.3,0.3l53.4,30.5c0.7,0.4,1.3,1.4,1.3,2.2v61c0,0.8-0.6,1.8-1.3,2.2L169.3-191 c-0.7,0.4-1.9,0.4-2.6,0l-53.4-30.5c-0.7-0.4-1.3-1.4-1.3-2.2v-61c0-0.8,0.6-1.8,1.3-2.2l53.4-30.5 C167-317.7,167.5-317.8,168-317.8L168-317.8z" stroke="{}"  stroke-width="25" fill="white"></path>'.format(colors[0]),
                    '</g>',
                    '</pattern>'])
        if ind == 4:
            pattern_list.extend(['<pattern id="{}" x="0" y="63" patternUnits="userSpaceOnUse" width="31" height="50" viewBox="0 0 10 16">'.format(str(ID)),
                    '<g id="cube">',
                    '<path class="left-shade" d="M0 0l5 3v5l-5 -3z" fill="{}" stroke="none"></path>'.format(colors[0]),
                    '<path class="right-shade" d="M10 0l-5 3v5l5 -3" fill="{}" stroke="none"></path>'.format(colors[0]),
                    '</g>',
                    '<use x="5" y="8" xlink:href="#cube"></use>',
                    '<use x="-5" y="8" xlink:href="#cube"></use>',
                    '</pattern>'])
        if ind == 5:
            pattern_list.extend(['<pattern id="{}" x="0" y="0" patternUnits="userSpaceOnUse" width="25" height="45" viewBox="0 0 10 18">'.format(str(ID)),
                    '<g id="chevron">',
                    '<path class="left" d="M0 0l5 3v5l-5 -3z" fill="{}"></path>'.format(colors[0]),
                    '<path class="right" d="M10 0l-5 3v5l5 -3" fill="{}"></path>'.format(colors[1]),
                    '</g>',
                    '<use x="0" y="9" xlink:href="#chevron"></use>',
                    '</pattern>'])
        if ind == 6:
            pattern_list.extend(['<pattern id="{}" viewBox="0,0,10,10" width="15%" height="15%">'.format(str(ID)),
                    '<polygon points="0,0 2,5 0,10 5,8 10,10 8,5 10,0 5,2" fill="{}"/>'.format(colors[0]),
                    '</pattern>'])
        fill =  'url(#{})'.format(str(ID))
        ID += 1
    else:
        np.random.shuffle(clrs)
        fill = clrs[0]
    return fill



def make_art(w, h, cl, rb):
    global rb_ind 
    rb_ind = rb
    global WIDTH
    WIDTH = w
    global HEIGHT
    HEIGHT = h
    global clrs
    global colors
    clrs = cl
    colors = cl.copy()
    n = len(cl)
    clrs.extend(clrs)
    clrs.extend(['white' for i in range(1, int(0.75*n))])
    clrs.append('black')
    mondrian(0, 0, w, h)
    string = make_svg()


