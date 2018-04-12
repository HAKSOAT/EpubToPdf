import sys
from manage import FileManager
from getpy import GetEngine
from pdfpy import PdfEngine

def process():

	if sys.argv[1].endswith(".epub"):
		
		epub_file = sys.argv[1]
		file = FileManager(epub_file)
		file.epub_to_zip()
		file.get_directory()
		file.extract_zip()
		engine = GetEngine(file.directory)
		engine.get_all()
		engine.get_html()
		engine.get_pdf()
		engine.get_css()
		engine.get_images()
		pdf = PdfEngine(engine.html_files, engine.css_files, 
						engine.pdf_files, file.directory)
		pdf.convert()
		pdf.combine()
		pdf.del_pdf()
		file.zip_to_epub()
		file.del_directory()

	else:

		print("File is not an epub file")
	

if __name__ == "__main__":
	process()

