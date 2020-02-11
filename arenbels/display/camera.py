from arenbels.display.engine import Rect
from arenbels.display.engine import Vector
import time

from arenbels.tools import T
from pygame.transform import rotate

""" A Camera object that represents what will be shown to the player. It uses a Rect (cf Rect) to define what is inside the view of the camera and then rescales and translates things so that they fit exactly in the window (it's the distorsion). This distorsion is a couple of Transform : (tr_scale,tr_translate) """

class Camera:
    """ Camera object """
    def __init__(self):
        self.rect = Rect()
        self.win = None #Undefined yet
        self.angle = 0
        self.rotation_effect = False #Timed effect of rotation
        self.remove_rotation_effect = True #Possibility to remove it
        self.world = None

    def move(self,v):
        """ Translates the camera by vector v"""
        self.rect.translate(v)

    def link_world(self,w):
        """ Set the world attribute """
        self.world = w

    def set_position(self,pos):
        """ Sets the position of the camera in the World"""
        self.rect.set_position(pos)
        if not(self.win is None):
            self.compute_distorsion()

    def set_dimension(self,size):
        """ Set the dimension of the Camera (useful to zoom).
        Note that size is a Vector. """
        self.rect.set_dimension(size)
        if not(self.win is None):
            self.compute_distorsion()

    def get_position(self):
        """ Returns the position of the camera """
        return self.rect.get_position()

    def get_dimension(self):
        """ Returns the dimension of the camera """
        return self.rect.get_dimension()

    def set_win(self,fen):
        """ Set the window in which the camera will output """
        self.win = fen
        self.compute_distorsion()

    def get_win(self):
        """ Returns the windows associated with the camera """
        return self.win

    def set_distorsion(self,dis):
        """ Set the distorsion of the camera (rescale objects and """
        self.distorsion = dis

    def get_distorsion(self):
        """ Returns the distorsion of the camera """
        return self.distorsion

    def compute_distorsion(self):
        """ Computes the distorsion of the camera """
        (width,height) = (self.win.get_width(),self.win.get_height())
        dim = self.get_dimension()
        pos = self.get_position()

        distorsion_scale = Vector(width/dim.x,height/dim.y)
        distorsion_translate = -pos
        self.distorsion = (distorsion_scale,distorsion_translate)

    def is_in_camera(self,rect):
        """ Returns true if the polygon is completely in the camera's rect or if it intersects a side """
        r = self.rect.intersect(rect)
        return r

    def center_on(self,pos):
        """ Centers the camera on a position """
        pos = pos
        pos = pos + (-self.get_dimension()/2)
        self.set_position(pos)

    def threeforth_on(self,pos):
        """ Makes a 3/4 on the position (this position will be on the left and 3/4 of the screen is free on the right -> useful for a Canabalt style game """
        dim = self.get_dimension()
        pos += (-Vector(dim.x/4,dim.y/2))
        self.set_position(pos)

    def flashblack(self):
        """ Fill the camera with black in order to blit images right after """
        self.win.fill((0,0,0))

    def reset_rotation(self):
        """ Reset the rotation """
        self.angle = 0

    def rotate(self, angle):
        """ Add the rotation of [angle] to the camera """
        self.angle += angle

    def set_rotation_effect(self):
        self.rotation_effect = True
        self.rotate(0.5)

    def rotate_view(self, angle):
        """ Rotates the current content of the window by "angle" degrees """
        if self.rotation_effect:
            self.rotate(0.5)
            if self.angle%360 == 0 and self.remove_rotation_effect:
                self.rotation_effect = False
        center = self.win.get_rect().center
        rotated_fen = rotate(self.win,angle)
        rotated_rect = rotated_fen.get_rect()
        rotated_rect.center = center

        self.flashblack()
        self.win.blit(rotated_fen, rotated_rect.topleft)

    def aff(self,objects,dt,score=0,bg=None):
        """ Show all objects of the given argument that are in the camera
        as well as the background and the score """
        #Starts with a flashblack
        if self.win is not None:
            self.flashblack()
            if bg is not None:
                bg.show()#Shows the Background (see Background)

            #Shows all objects that are in the camera
            for o in objects:
                if self.is_in_camera(o.get_size()): #Checks if the hitbox is in the camera
                    o.aff(self.win,self.get_distorsion(),dt)

            # Rotation
            self.rotate_view(self.angle)

            self.show_score(score)

    def __repr__(self):
        txt = "Camera("+str(self.rect)+")"
        if self.win is None: txt += "(not init)"
        return txt

    def show_score(self,score):
        #Show the score
        d = self.get_dimension()
        x = int(d.x*15/16) #Computes where to put it
        y = int(d.y*1/16)
        distorsion_scale = self.get_distorsion()[0]
        vpos = Vector(x,y) * distorsion_scale
        T(self.win,str(score),vpos.x,vpos.y,255,255,255,size=45)
