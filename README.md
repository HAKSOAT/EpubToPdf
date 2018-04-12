# EpubToPdf

This program converts epub documents to pdf documents.


**Installation**

Simply fork this repository to your machine.


**Requirements**

To install the requirements, run the following command:

```pip install -r requirements.txt```

After this, you install the _wkhtmltopdf_ which is a dependency of the _pdfkit_ module.


wkhtmltopdf file can be downloaded [here](https://wkhtmltopdf.org/downloads.html)

For Debian/Ubuntu users:


```$ sudo apt-get install wkhtmltopdf``` 

should do the trick.



**Usage**

Copy the epub file inside the repository folder when forked.

Run the main.py file, adding the name of the epub file as a commandline argument.

As shown below:

```python main.py epub-file-name```
