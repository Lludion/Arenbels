'''
This file is mostly used to create the appropriate dictionaries .


Here is the format of the json files :

img : {name(str): path(str)}
characters : {name(str): [image(str), color_talk_r(int), color_talk_g(int), color_talk_b(int), inventory]}
dialogue : {name(str): [[name_bubble(str), character(str), image(str), x(int), y(int), is_last(bool)]]}
			= {name(str): [Dialogue_Bubble(list)]}
			= {name(str): talk(list)}
items : {name(str): [type(str), args*]}
'''

from pygame.image import load

def create_img(dct):
	""" creates the full dictionnary of pictures in dct. Used with dct_img.

	"arenbels/data/img/" is appened to the path"""
	for img in dct:
		dct[img] = load("arenbels/data/img/" + dct[img]).convert_alpha()
	return dct