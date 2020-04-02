import pdfkit
import os
from PyPDF2 import PdfFileMerger
from PyPDF2.utils import PdfReadError


class PdfEngine(object):

	"""
		This class carries operations on pdf files.

		It has the following methods:

		convert() --- Which converts each of the markup file
		passed in to pdf. Markup file should be html

		combine() --- Which merges all of the pdf files created by
		the convert method, creating a new file.

		del_pdf() --- Which deletes all the pdf files created by
		the convert method.

	"""

	def __init__(self, markup_files, style_files, pdf_files, directory):
		self.markup_files = markup_files
		self.style_files = style_files
		self.pdf_files = pdf_files
		self.directory = directory

	def convert(self):
		for each in self.markup_files:

			# Prevent conversion process from showing terminal updates
		
			options = {'quiet': ''}

			pdfkit.from_file(each, "{}.pdf".format(self.markup_files.index(each)),
							 options=options)

	def combine(self):

		merger = PdfFileMerger()

		for pdf in self.pdf_files:
			try:
				merger.append(pdf, import_bookmarks=False)
			except PdfReadError:
				pass

		merger.write("{}.pdf".format(self.directory))

	def del_pdf(self):
			for each in self.pdf_files:
				os.remove(each)
