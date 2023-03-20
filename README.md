# TypingSpeedTest
1.1 IDEA BEHIND  THE PROJECT:

In today's ever-evolving world, a student's ability to type fluently enables them to focus on what they're typing vs. how to type. Being able to quickly share thoughts and send them to their teacher from any location is much more efficient than using paper and pencil. Educators need to be able to connect to a student’s online world to engage and motivate them, because they are a new and different type of learner.  Typing is now an essential part of almost every job imaginable. It helps you complete your work faster and more efficiently, be comfortable with the computer, and help to communicate with co-workers and superiors. 

1.2 MAIN OBJECTIVE:
The main objective of this project is to design and develop a “Typing Speed Test with GUI using python” where one can know his typing speed and also can improve his/her Typing skills and accuracy. 

1.3 TOOLS USED: 
We will be using python GUI library like Tkinter, Pyglet to create a Typing Speed Test Graphical User Interface with Python on a user interface. We will be using some basic concepts like functions, loops, decision control statements and also some of the concepts of OOP. In order to develop our “Typing Speed Test” project, we will be using PyCharm IDE. We will be using some algorithmic techniques like recursions, iterations etc.

PROBLEM STATEMENT:

The problem of this study was to determine the rate at which typing speed and accuracy were achieved by a user so that the user can improve his typing skills and also be accurate with his typing by knowing about the errors made to master the skill of typing.

SUMMARY:

The Typing Test measures an individual's typing speed and accuracy. The test-taker is presented with a couple of sentences and given 45 seconds to type as much of the words/sentences as possible. 
The test generates three scores: 
Words per Minute (WPM), Number of Errors, Net Result.
The Typing Test takes about one minute to complete.
The two factors will define the proficiency of the person in typing. Some typing test used character-based calculation in which 5 characters count as a word, regardless how many characters in the particular word. These Character based calculation has its own benefit like it independent from the text passage, there may be more lengthy word in one passage then other, but it calculates same speed all time.
A Sentence "Here we are checking our typing speed." 
Total Words (Using character methods) = 38 / 5 = 7.6 Words.
The typing test above will show your typing speed in Word per Minute (WPM). Accuracy is gross and net speed ratio. Net Result will consider your final speed of typing. Here a highlighter will help you in identify where you are in the passage(blue in color). If you skip a word it will show in result that you skipped a word. If a word is incorrectly typed the GUI highlights the word with Red.

FORMULATION:

The parameters for measuring the typing speed are:
•	Average speed (in WPM)
•	Accuracy (in %)
•	Number of errors 
•	Net result (in WPM)
1) Average Speed:
The average speed is calculated as the number of words typed in the given time(45 secs). 
Average speed=number of words×60/45 WPM
2) Accuracy:
The ratio of number of correct words is to the total number of Characters multiplied by 100
Accuracy= (number of correct words/total number of words) ×100
3) Number of errors:
It gives the count of mistyped words
4) Net Result:
The average speed × accuracy obtained gives the net result. This factor makes sure that one’s accuracy depends on one’s typing speed 
Net result=Speed × Accuracy.
