# Automated Student Registration System

 I built this project as my final year Extended Qualification Project(EPQ) for the year 2018. It is an automated student registration system that utilises live video feed from a camera and performs face detection and recognition. Recognised students are marked as "present" in a database for each registration session. The output of this process can also be accessed through a excel file that is generated for each session of registration.

## Prerequisites

When creating the program, I used a computer running Ubuntu Linux Operating System. To ensure the execution runs as required, make sure it is executed in a Standard Unix terminal/command line interface.

Ensure your computer is running Python version 2.7.0 

## Installation

You will first need to obtain an API key. This can be done by going to the microsoft azure website and signing up for the FaceAPI. You will then be given an API key. You will then use this key to replace the pre-existing(old) key in the following text file

     /Student Registration Project Files/resources/APIkey.txt

API key can be obtained from official cognitive face API using the link below

	https://azure.microsoft.com/en-gb/try/cognitive-services/?api=face-api




Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries in the requirements text file.

	pip install -r requirements.txt

NOTE: execute this command in te folder containing the requirements text file.


Run the program using a command line interface(make sure you are in the correct directory)
	type the following to run.
	
	./run.sh

## Usage

The program has a GUI integrated which is labelled with straight forward guidelines on how to operate it.

## Author

Martin Namukombo - [mastadict](https://github.com/mastadict) 

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE.md file for details
