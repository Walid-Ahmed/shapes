from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import random as rn
import numpy as np
import pygame
import cv2
import os


COL_LEVEL = 1
ROW_LEVEL = 0
GREEN = (0, 255, 0, 255)
BLUE = (255, 0, 0, 255)
RED = (0, 0, 255, 255)
BLACK = (0, 0, 0, 255)
DEPTH = 4
NEAR = .1
FAR = 50.0
WIDTH = 800
HEIGHT = 600
CAMERA_ANGLE = 45
ROTATION_ANGLE = 30.0
IMAGE_PATH = 'raw_imgs'

square = np.array([
	[+1.0, +1.0, 0.0, 1.0], 
	[+1.0, -1.0, 0.0, 1.0], 
	[-1.0, -1.0, 0.0, 1.0],
	[-1.0, +1.0, 0.0, 1.0]
])

triangle = np.array([
	[+1.0, +1.0, 0.0, 1.0], 
	[+1.0, -1.0, 0.0, 1.0], 
	[-1.0, -1.0, 0.0, 1.0]
])

def get_circle():
	SEGMENTS = 300
	pts = []
	for seg in range(SEGMENTS):
		theta = 2.0 * seg * pi / SEGMENTS
		pts.append([cos(theta), sin(theta), 0.0, 1.0])

	return np.array(pts)

circle = get_circle()

def draw(shape, color, name):

	# why height and width here
	(name_1, shape) = shape
	(name_2, color) = color
	[width, height] = abs(np.min(shape, axis=ROW_LEVEL) - np.max(shape, axis=ROW_LEVEL)) # this is the diagonal

	s = shape - np.min(shape, axis=ROW_LEVEL, keepdims=True)
	
	# the rows represent height while columns give the width
	g = np.zeros((int(height + 1), int(width + 1), DEPTH))

	cv2.fillPoly(g,[s.astype(int)], color)
	# cv2.polylines(g,[s.astype(int)], True, BLACK, lineType=cv2.LINE_AA)
	
	cv2.imwrite(os.path.join(IMAGE_PATH, '{}_{}_{}.png'.format(name_1, name_2, name)), g)

def get_red():
	c = rn.choice([
		[255, 192, 203, 255],
		[255, 145, 164, 255],
		[248, 131, 121, 255],
		[250, 128, 114, 255],
		[255, 0, 0, 255],
		[237, 28, 36, 255],
		[196, 2, 51, 255],
		[242, 0, 60, 255],
		[237, 41, 57, 255],
		[238, 32, 77, 255],
		[255, 36, 0, 255],
		[237, 41, 57, 255],
		[205, 92, 92, 255],
		[230, 0, 38, 255],
		[150, 0, 24, 255],
		[224, 17, 95, 255],
		[220, 20, 60, 255],
		[218, 44, 67, 255],
		[206, 32, 41, 255],
		[196, 30, 58, 255],
		[226, 61, 40, 255],
		[179, 27, 27, 255],
		[178, 34, 34, 255],
		[165, 0, 33, 255],
		[164, 90, 82, 255],
		[132, 22, 23, 255],
		[88, 17, 26, 255],
		[139, 0, 0, 255],
		[128, 0, 0, 255],
		[124, 10, 2, 255],
		[169, 17, 1, 255],
		[228, 77, 48, 255],
		[102, 0, 0, 255]

	])
	t = c[0]
	c[0] = c[2]
	c[2] = t
	return tuple(c)

def get_green():
	c = rn.choice([
		[143, 151, 121, 255],
		[75, 111, 68, 255],
		[135, 169, 107, 255],
		[86, 130, 3, 255],
		[1, 50, 32, 255],
		[79, 121, 66, 255],
		[113, 188, 120, 255],
		[34, 139, 34, 255],
		[218, 221, 152, 255],
		[73, 121, 107, 255],
		[41, 171, 135, 255],
		[169, 186, 157, 255],
		[144, 238, 144, 255],
		[116, 195, 101, 255],
		[152, 251, 152, 255],
		[138, 154, 91, 255],
		[74, 93, 35, 255],
		[49, 120, 115, 255],
		[1, 121, 111, 255],
		[108, 124, 89, 255],
		[0, 158, 96, 255],
		[208, 240, 192, 255],
		[0, 128, 128, 255],
		[128, 128, 0, 255],
		[00, 255, 00, 255],
		[0, 128, 0, 255],
		[0, 100, 0, 255],
		[00, 165, 80, 255],
		[0, 159, 107, 255],
		[0, 168, 119, 255],
		[0, 173, 131, 255],
		[28, 172, 120, 255],
		[75, 83, 32, 255],
		[0, 106, 78, 255],
		[102, 255, 0, 255],
		[79, 255, 176, 255],
		[27, 77, 62, 255],
		[30, 77, 43, 255],
		[0, 86, 59, 255],
		[172, 225, 175, 255],
		[47, 132, 124, 255],
		[3, 192, 60, 255],
		[0, 105, 62, 255],
		[80, 200, 120, 255],
		[77, 93, 83, 255],
		[0, 171, 102, 255],
		[173, 255, 47, 255],
		[63, 255, 0, 255],
		[53, 94, 59, 255],
		[19, 136, 8, 255],
		[0, 144, 0, 255],
		[0, 168, 107, 255],
		[76, 187, 23, 255],
		[11, 218, 81, 255],
		[0, 73, 83, 255],
		[24, 69, 59, 255],
		[57, 255, 20, 255],
		[0, 128, 0, 255],
		[0, 102, 0, 255],
		[80, 200, 120, 255],
		[0, 166, 147, 255],
		[68, 76, 56, 255],
		[103, 146, 103, 255],
		[0, 78, 56, 255],
		[118, 255, 122, 255],
		[46, 139, 87, 255],
		[85, 221, 51, 255],
		[0, 145, 80, 255],
		[5, 144, 51, 255],
		[1, 68, 33, 255]
	])

	t = c[0]
	c[0] = c[2]
	c[2] = t
	return tuple(c)

def get_blue():
	c = rn.choice([
		[137, 207, 240, 255],
		[173, 216, 230, 255],
		[204, 204, 255, 255],
		[176, 224, 230, 255],
		[153, 255, 255, 255],
		[141, 163, 153, 255],
		[0, 0, 255, 255],
		[51, 51, 153, 255],
		[0, 135, 189, 255],
		[0, 147, 175, 255],
		[0, 24, 168, 255],
		[31, 117, 254, 255],
		[0, 0, 205, 255],
		[108, 180, 238, 255],
		[118, 171, 223, 255],
		[0, 112, 184, 255],
		[84, 90, 167, 255],
		[16, 52, 166, 255],
		[64, 0, 255, 255],
		[70, 102, 255, 255],
		[31, 48, 94, 255],
		[0, 119, 145, 255],
		[0, 0, 139, 255],
		[0, 35, 185, 255],
		[34, 76, 152, 255],
		[0, 0, 128, 255],
		[25, 25, 112, 255],
		[8, 37, 103, 255],
		[146, 39, 135, 255],
		[76, 81, 109, 255],
		[29, 41, 81, 255],
		[21, 244, 238, 255],
		[0, 128, 128, 255],
		[54, 117, 136, 255]
	])

	t = c[0]
	c[0] = c[2]
	c[2] = t
	return tuple(c)


def get_trans_mat(mat_type):
	return np.array(list(glGetFloatv(mat_type))).reshape(4, 4)

	
def set_camera(angle, aspect_ratio, near, far):
	glLoadIdentity()
	gluPerspective(angle, (aspect_ratio), near, far)
	

def place_an_object(x=0.0, y=0.0, z=-15.0):
	glTranslatef(x, y, z)



def get_xy_plan(shape_info, display):
	(_, shape) = shape_info
	pc = np.dot(np.dot(shape, get_trans_mat(GL_MODELVIEW_MATRIX)), get_trans_mat(GL_PROJECTION_MATRIX))
	ndc = pc / ((pc[:, 3] + 1).reshape(shape.shape[0], 1))
	
	pts = np.zeros((shape.shape[0], 2)) # Xs and Ys
	pts[:, 0] = (.5 * ndc[:, 0] + .5) * display[0]
	pts[:, 1] = (.5 * ndc[:, 1] + .5) * display[1]
	return (_, pts)

def get_shape():
	return rn.choice([('circle', circle), ('square', square), ('triangle', triangle)])

# return bounded value between -10, -25
def get_rand(rng=5.0, shift=0.0):
	return floor(rng * rn.uniform(-2, 1) + shift)

# return random binary value 0.0 or 1.0
def get_binary(rng=1.0):
	return floor(rng * rn.uniform(0, 1) + .5)	

def get_color():
	return [('red', get_red()), ('green', get_green()), ('blue', get_blue())][rn.randint(0, 2)]
	
def reset_matrix():
	glPushMatrix()
	glPopMatrix()

def main():
	pygame.init()
	display = (WIDTH, HEIGHT)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	if not os.path.exists(IMAGE_PATH):
		os.makedirs(IMAGE_PATH)
	
	for i in range(10000):
		
		set_camera(CAMERA_ANGLE, display[0]/display[1], NEAR, FAR)	
		place_an_object()

		reset_matrix()

		glTranslatef(0.0, 0.0, get_rand())
		glRotatef(get_rand(ROTATION_ANGLE), get_binary(), get_binary(), get_binary())

		draw(get_xy_plan(get_shape(), display), get_color(), str(i))
	
main()

