from PIL import Image
from save import *
from math import *
import random as rn
import numpy as np


import os 


FULL_INTENSITY = 255
DEPTH = 4
WIDTH = 400
HEIGHT = 300
COLOR = 510
TRANS = 0

def get_scalled_size(width, height):
	factor = 1.2 * (rn.uniform(0, 1) +.5)
	return floor(factor * width), floor(factor * height)



def get_raw_imgs(source_folder):
	imgs_list = os.listdir(source_folder)
	try:
		print(imgs_list.pop(imgs_list.index('.DS_Store'))) # remove ds store
	except Exception as e:
		pass
	return imgs_list

def get_backgrounds(bg_folder):
	bg_list = os.listdir(bg_folder)
	try:
		bg_list.pop(bg_list.index('.DS_Store'))
	except Exception as e:
		pass
	
	return bg_list

def draw(i, source_folder, target_folder, bg_folder, train_folder, test_folder):
	
	drawn_objects = set([])
	# collage = Image.fromarray(FULL_INTENSITY * np.ones((HEIGHT, WIDTH, DEPTH), dtype=np.uint8), 'RGBA')
	collage = Image.open(os.path.join(bg_folder, rn.choice(bg_list)))
	[[WIDTH, HEIGHT]] = [collage.size]
	file = Description(target_folder, '{}.jpg'.format(i), os.path.join(os.getcwd(), '{}/{}.jpg'.format(target_folder, i)), str(DEPTH), str(WIDTH), str(HEIGHT))

	count = 0
	tries = 0
	while True:

		img_name = rn.choice(imgs_list)

		# load shape image
		shape = Image.open(os.path.join(source_folder, img_name))
		
		# disable scalling
		# shape = shape.resize(get_scalled_size(shape.size[0], shape.size[1]) ,Image.ANTIALIAS)

		# save their width and height for the bounding box
		[[width, height]] = [shape.size]

		start_pts = [[x, y]]= [[rn.randint(0, WIDTH-width), rn.randint(0, HEIGHT-height)]]

		# this means that any point/ coordinates of the shape is colofull
		# shape_arr = np.argwhere(np.array(shape).sum(axis=-1) <= COLOR) + start_pts

		# check transparency 
		shape_arr = np.argwhere(np.array(shape)[:, :, 3] > TRANS) + start_pts
		
		# convert it to hasable structure
		shape_pts = set(list(map(tuple, shape_arr)))
		
		intersection = set.intersection(drawn_objects, shape_pts)
		
		if len(intersection) <= 0:

			# add bounding box for shape and color
			file.add_object(img_name.split('_')[1] + img_name.split('_')[0], str(x), str(y), str(x+width), str(y+height))

			collage.paste(shape, tuple(start_pts[0]), mask=shape)
			drawn_objects = set.union(drawn_objects, shape_pts)
			count += 1
		else:
			print('collision happend')

		tries += 1

		if count >= 2 or tries >= 10:

			collage = collage.convert('RGB') # convert RGBA to RGB
			collage.save(os.path.join(target_folder, '{}.jpg'.format(i)))
			file.save(os.path.join(target_folder, '{}.xml'.format(i)))

			if rn.uniform(0, 1) >= .05:
				collage.save(os.path.join(train_folder, '{}.jpg'.format(i)))
				file.save(os.path.join(train_folder, '{}.xml'.format(i)))	
			else:
				collage.save(os.path.join(test_folder, '{}.jpg'.format(i)))
				file.save(os.path.join(test_folder, '{}.xml'.format(i)))				
			break

source_folder = 'raw_imgs'
bg_folder = 'backgrounds'

target_folder = 'imgs'

train_folder = os.path.join(target_folder, 'train')
test_folder = os.path.join(target_folder, 'test')


imgs_list = get_raw_imgs(source_folder)
bg_list = get_backgrounds(bg_folder)

# create images folder, subfolders train and test
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

if not os.path.exists(train_folder):
	os.makedirs(train_folder)

if not os.path.exists(test_folder):
	os.makedirs(test_folder)

for i in range(3200):
	# create description file
	draw(i, source_folder, target_folder, bg_folder, train_folder, test_folder)



