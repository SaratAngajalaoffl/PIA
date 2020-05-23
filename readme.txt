A simple python script that automates the following tasks:-

1)Creates a folder with the project name in my projects directory

2)Creates a readme.txt file

3)runs git init

4)opens github

5)creates a new github repository with the project name

6)gets the repository ssh link

7)sets the remote url to my project repository

8)runs git add

9)runs git commit with the message "First Commit"

10)pushes the first commit onto my repository

11)Opens my project folder in vscode with readme file open

Instructions if you wanna give it a test run:-

1)Install selenium python package using pip install selenium

2)Install the webdriver for your browser and add it to your path

3)Open the "create_project.bat" in your text editor and edit the paths on line 9,12 and 21.

4)Add your github username and password to the "userdata.json" file under corresponding keys

5)run create_project command with the arguments:-

1st argument:-
    -l for creating your project directory at path 1
    -p for creating your project directory at path 2
2nd argument:-
    The name of your project