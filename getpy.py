from bs4 import BeautifulSoup as bs
import os
import re
import ntpath


class GetEngine(object):

	"""
		
		This class contains the methods needed to get the files,
		to help make the pdf file.

		The class contains the following methods:

		get_html() --- Which gets the html file names.

		get_pdf() --- Which gets the pdf file names.

		get_css() --- Which gets the css file names.

		get_images() --- Which gets the image file names.


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
		file = None
		directory_paths = []
		for root, dirs, files in os.walk(self.directory):
			#This traverses the directory passed in as an argument,
			#returns the current directory, the sub directories and all the files
			directory_paths.append(root)
			if file:
				continue
			for each in files:
				if each.endswith(".opf"):
					file = os.path.join(root, each)
					continue
		if not file:
			return

		xml_content = open(file, "r", encoding="utf-8").read()

		xml_tree = bs(xml_content, features = "xml")

		file_names = xml_tree.package.manifest.findAll('item')

		# Gets the name of all the documents in order
		# from the opf file, then saves the file name with its path
		# The file path in the opf file can't be relied upon
		# Hence, the need to extract file name and get its path

		for file in file_names:
			file_path_match = re.match(r'.+\.[a-zA-Z]+', file.get('href', ''))
			if not file_path_match:
				continue
			file_name = ntpath.basename(file_path_match.group())
			for path in directory_paths:
				filepath = path + '/' + file_name
				if os.path.exists(filepath):
					self.files.append(filepath)
