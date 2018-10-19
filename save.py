import xml.etree.ElementTree as ET

class Description:

	def __init__(self, foldername, filename, path, depth, width, height):
		self.tree = ET.parse('temp.xml')
		self.root = self.tree.getroot()

		self.add_foldername(foldername)
		self.add_filename(filename)
		self.add_path(path)
		self.add_size(depth, width, height)




	def add_foldername(self, foldername):
		self.tree.find('.//folder').text = foldername
		

	def add_filename(self, filename):
		self.tree.find('.//filename').text = filename

	def add_path(self, path):
		self.tree.find('.//path').text = path

	def add_size(self, depth, width, height):
		self.tree.find('.//depth').text = depth
		self.tree.find('.//width').text = width
		self.tree.find('.//height').text = height



	def add_object(self, name, xmin, ymin, xmax, ymax):
		temp_object = '''<object>
			<name>def</name>
			<pose>Unspecified</pose>
			<truncated>0</truncated>
			<difficult>0</difficult>
			<bndbox>
				<xmin>0</xmin>
				<ymin>0</ymin>
				<xmax>0</xmax>
				<ymax>0</ymax>
			</bndbox>
		</object>'''

		object_node = ET.fromstring(temp_object)
		object_node.find('.//name').text = name
		object_node.find('.//xmin').text = xmin
		object_node.find('.//ymin').text = ymin
		object_node.find('.//xmax').text = xmax
		object_node.find('.//ymax').text = ymax

		self.root.append(object_node)

	def save(self, name):
		self.tree.write(open(name, 'wb'))

# obj = MyClass('test', 'test.xml', 'test_path', str(3), str(3), str(3))
# obj.save()