import os
import zipfile
import shutil


class FileManager(object):


	"""
		
		This class is used for file interactions.

		It has the following methods:

		epub_to_zip() --- Which converts the epub file to a zip file

		extract_zip() --- Which extracts the content of the zip file

		get_directory() --- Which gets the directory name where content of
		 					zip file was extracted

		zip_to_epub() --- Which converts the zip file back to epub

		del_directory() --- Which deletes the directory where zip files
							were extracted

		del_pdf() --- Which deletes the pdf files created by 


	"""

	def __init__(self, epub_file):
		self.epub_file = epub_file
		self.zip_file = "{}.zip".format(epub_file.split(".epub")[0])
		self.directory = ""


	def epub_to_zip(self):
		os.rename(self.epub_file, self.zip_file)


	def extract_zip(self):
		extracted_files = zipfile.ZipFile(self.zip_file)
		extracted_files.extractall(self.directory)
		extracted_files.close()

	def get_directory(self):
		minus_open_paren = self.epub_file.split(".epub")[0].replace("(", "")
		minus_close_paren = minus_open_paren.replace(")", "")
		self.directory = minus_close_paren.replace(" ", "")
		

	def zip_to_epub(self):
		os.rename(self.zip_file, self.epub_file)


	def del_directory(self):
		shutil.rmtree(self.directory)



