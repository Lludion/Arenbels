from pygame import Surface

def blitpix(dis,p):
    """ Blits the pixel 'p' of size 'size' onto the Surface 'win' = dis._window."""
    col = p.get_color()
    size = sizepix(dis)
    pSurf = Surface((size,size))
    pSurf.fill(col)
    dis._window.blit(pSurf ,pospix(None,p,size))

def sizepix(dis):
    """ returns the size of a pixel
       into the Displayer dis """
    w = dis.world
    leng = w.l#len(w.grid)
    heig = w.h#len(w.grid[0])
    if leng>heig:
        size = int(dis.options["DISPLAYSIZE_Y"]/heig)
    else:
        size = int(dis.options["DISPLAYSIZE_X"]/leng)
    return size

def pospix(dis,p,size=None):
    """ returns the position of the pixel p

    optimisation trick : you can enter size if you know it, and None for the window."""
    if p.size < 0 or p.renew_size:
        if size is None:
            size = sizepix(dis)
        p.size = size
    else:
        size = p.size
    return (size*p.x,size*p.y)