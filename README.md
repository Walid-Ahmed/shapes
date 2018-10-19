## SHAPES DATASET GENERATOR
---

### Overview: Shape Generator

The goal of this program is to create images dataset. A single image consists of background and multiple shapes (circle, triangle, and square). The project is broken into three parts. First part is resposible for create the shapes with differnt colors, viewing angles, and sizes. The second builds various backgrounds with solid colors (shades of white and yellow). Finally, the third collects some shapes and merge them with a background producing the final image.


#### Part 1: Draw

The first part draws one of three shapes (circle, triangle, and square). It controls the color and viewing angle. The available colors are the shades of red, green, and blue which is very wide range. The shapes are drawn in 2D space (flat shapes). However, the viewing angle in 3D space, making the shape may look differently thant it normally would. This part also control the size of the shape by placing it far or near of the view (camera).

The utility name is draw.py. It runs a follow:

`python draw.py`

generating a large set of shapes saving them into folder named `raw_imgs`.

### Part 2: Backgrounds

The second step is to build different backgrounds which maybe the simplest one. It constructs 400x300 images made of solid colors. It uses the shades of white and yellow. Then, it save them to backgrounds folder for later use. 

The utility name is background.py. It runs as follow:

`python draw.py`

generating various coloring backgroudns. 


#### Part 3: Collage

Collage is the final step for creating labeled dataset that can be used in the subsequent task (object detection). It combines the shapes and backgrounds creating an image of multiple objects by overlaying some randomly selected objects on the background. It reduces the overlap as minimum as possible between the object. Moreover, it produces `xml` files using `save.py` utility that describe shape type, color, and position on the image. It saves the data into `imgs/train/` and `imgs/test/`.

The utility name is `Collage.py`

generating images with different shapes, colors, and backgrounds

#### Part 4: TF records creation

