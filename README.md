# Automated Student Registration System

I built this project as my final year Extended Qualification Project(EPQ) for the year 2018. It is an automated student registration system that utilizes live video feed from a camera and performs face detection and recognition. Recognized students are marked as "present" in a database for each registration session. The output of this process can also be accessed through an excel file that is generated for each session of registration. Though the facial recognition capability of the project relies mostly on the Microsoft cognitive face API, it went trough numerous iterations. The initial build relied mostly on the "Face Recognition" python package which was later dumped due to low accuracy and high error rate. The classifier built for the second build relied on the "TensorFlow" python library which performed as required but was unusable due to its high computing power requirements. The project required a perfect build that would require low computing power but yet would deliver workable speeds and the cognitive face API just happened to meet this criteria.

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
