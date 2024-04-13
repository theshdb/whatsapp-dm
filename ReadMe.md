# Requirements for running the project

## Downloading the latest version of Python

To download the latest version of Python, you can visit the official Python website at [https://www.python.org/](https://www.python.org/). From there, you can navigate to the Downloads section to find the installation files for various operating systems.

After downloading the installer, follow the installation instructions provided on the website to install Python on your system.

Remember to check the Python version using the `python --version` command in the terminal after installation to ensure it was successful.

To run this project, you need to install the following packages:

1. **Selenium**

   - Installation: `pip3 install selenium`
   - Description: Selenium is a powerful tool for automating web browsers. It is widely used for web scraping and automated testing.

2. **Webdriver Manager**

   - Installation: `pip3 install webdriver_manager`
   - Description: Webdriver Manager is a Python library that helps to manage browser drivers for Selenium automation.

3. **vObject**
   - Installation: `pip3 install vobject`
   - Description: vObject is a Python library for parsing and exporting iCalendar and VCard files.

Make sure to install these packages before running the project to ensure smooth execution.

## Setting up input files

Before running the project, if you want to send any files then make sure to add the files you want to send to the `inputFiles` directory. These can be images, documents, or any other files that you want to send along with the message.

Also, write the message you want to send to `inputMessage.txt`. You can format the message using markdown or WhatsApp text formatting styles like bold, URLs, etc.

To specify the phone numbers to which the message should be sent, add them to the file named `inputNumbers.txt`. You can copy and paste the numbers by scanning them from your camera lens from a document or manually enter them in this file.

Ensure that the input files are correctly formatted and placed in the designated directories before running the Python script.

## Running the Python file

To run a Python file from the terminal, use the following command:

```
python <filename.py>
```

Replace `<filename.py>` with the name of your Python file. Make sure you are in the same directory as the Python file or provide the full path to the file if it is located in a different directory.
