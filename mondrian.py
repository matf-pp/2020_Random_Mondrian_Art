import numpy as np
WIDTH = 1024   
HEIGHT = 768
SPLIT_LOWER = 85
SPLIT_TOL = 1.5
#
#
def choose_color():
def choose_lines():
def split_both(x,y,w,h):
def split_hor(x,y,w,h):
def split_ver(x,y,w,h):
def make_svg():
#
#
def mondrian(x,y,w,h):
    #algoritam zasnovan na rekurziji
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
        #funkcija za random boju, random debljinu linije        
        #stavljanje u svg
if __name__ == '__main__':
    mondrian(0,0,1024,768)