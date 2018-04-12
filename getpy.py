from bs4 import BeautifulSoup as bs
import os


class GetEngine(object):

	"""
		
		This class contains the methods needed to get the files,
		to help make the pdf file.

		The class contains the following methods:

		get_html() --- Which gets the html file names.

		get_pdf() --- Which gets the pdf file names.

		get_css() --- Which gets the css file names.

		get_images() --- Which gets the image file names.

		file_getter() --- Which gets all the files needed for document from the epub's .opf file.


		To create an instance of this object, pass in the name of the directory
		that stores all the extracted files from the epub file.


	"""

	def __init__(self, directory):
		self.html_files = []
		self.css_files = []
		self.image_files = []
		self.directory = directory
		self.files = []
		self.pdf_files = []

	def get_html(self):

		for file in self.files:
			if file.endswith(".xhtml") or file.endswith(".html"):
				self.html_files.append(file)

	def get_pdf(self):

		for file in self.html_files:
			self.pdf_files.append("{}.pdf".format(self.html_files.index(file)))

	def get_css(self):

		for file in self.files:
			if file.endswith(".css"):
				self.css_files.append(file)

	def get_images(self):

		for file in self.files:
			if file.endswith((".png", ".jpg", ".gif")):
				self.image_files.append(file)

	def get_all(self):

		for root, dirs, files in os.walk(self.directory):
			#This traverses the directory passed in as an argument,
			#returns the current directory, the sub directories and all the files
			for each in files:
				if each.endswith(".ncx"):
					root_dir = root
					file = os.path.join(root, each)
					break

		xml_content = open(file, "r").read()

		xml_tree = bs(xml_content, features = "xml")

		item_tags = xml_tree.ncx.navMap.findAll("content")

		#Gets the name of all the documents in order
		#from the opf file, then saves the file name with its path

		self.files = [root_dir + "/" + file["src"] for file in item_tags]

