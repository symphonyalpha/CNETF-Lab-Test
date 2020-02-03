# CNETF-Lab-Test
This is my lab test submission for one of my modules. 

# Overview
'TA11.csv' is the complete list of 26 students in the class, TA11.

The class wanted to organize an event and 'Sign_Up.txt' is the list of students who sign up for the event.
There are some discrepancies in the list:
- "Lin Zhi Jia" signed up "Zhi Jia"
- "Wong Kai Chee" signed up as "Ki Chee"
- "Eldo Wang Ming Yee" signed up "Yee Eldo"
- "Lim Chee Kow" signed up as "Chee Kow"
- "Roger Lee Chong" signed up as "roger lee chong"
- Some of the names have spaces in front and/or behind the names

Without modifying 'Sign_Up.txt', write a Python script and read the raw 'Sign_Up.txt' and produce a list with the following format:
- <sign up name as in 'Sign_Up.txt'>, <name in 'TA11.csv'>, <Student Number>
- e.g. Zhi Jia,LIN ZHI JIA,S97030947W

As "Wong Kai Chee" is spelt wrongly, we do not expect a match. Output for "Wong Ki Chee" will consist of the sign up name only:
- Wong Ki Chee

All the rest should find a match.
The expected output file is 'signup_new.csv'
