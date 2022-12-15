# EpubToPdf

This program converts epub documents to pdf documents.


**Installation**

Clone this repository to your machine.


**Requirements**

To install the requirements, run the following command:

```pip install -r requirements.txt```

After this, you install the _wkhtmltopdf_ which is a dependency of the _pdfkit_ module.


wkhtmltopdf file can be downloaded [here](https://wkhtmltopdf.org/downloads.html)

Make sure to add wkhtlmtopdf as an executable in Windows environment paths.

For Debian/Ubuntu users:


```$ sudo apt-get install wkhtmltopdf```

should do the trick.

If you get a `QXcbConnection: Could not connect to display` error, check [this issue](https://github.com/JazzCore/python-pdfkit/issues/82).



**Usage**

Copy the epub file inside the repository folder when forked.

Run the main.py file, adding the name of the epub file as a commandline argument.

As shown below:

```python main.py epub-file-name```
