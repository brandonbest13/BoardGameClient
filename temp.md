---
layout: homework
title: Homework 2 - Select
---

# Homework 2 - Select Module

## Introduction

In this homework you will practice

- Working with classes and objects
- class dunder functions
- using instance variables
- class specific funtions
- writing a main function

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking CS 2316, the TAs and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name and canvasID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.

## Problem Description

Congrats! You are the Supply Chain Manager at a major company, and you're tasked with deciding your intern team for the Summer. Luckily, HR has summarized applicant data for you, and your job is to decide who to hire and their offer details.


## Solution Description

You will be creating a module called select that takes in command line arguments and calculates candidate desirability in 3 categories: relevant experience, interview scores, and academic performance.  This information will be provided by HR, and your job is to process this data and rank the candidates, provide your recommendation for pay, and match interns to supervisors. The module will satisfy the requirements using object oriented programming.
 
Here is the info provided by HR - these will be supplied as command line arguments in this order. Note that all 4 arguments will always be supplied in this order. 
 
1. A list of tuples with each element being (CandidateName, CandidateID, CandidateGPA) : will be called *candidateList*
```Python
    ex: [ (John Doe, 17462, 3.45), (Jane Doe, 16745, 3.67)]
```
2. A list of dictionaries - each dictionary maps candidateID to all work experiences. An empty list signifies no experience. will be called *experienceDict*
```Python
    ex: [ {17462 : ["Supply Chain Intern", "Production Planning Intern"]}, {16745: ["Bussiness Analyst", "Publix Cashier"]} ]
```
3. A list of dictionaries mapping interviewer by employee ID to a list of candidates and scores. The first score is the technical interview score, and the second score is the behavioral interview score, each out of 5. Note that interviewer IDs are preceded by an S. Will be called *interviewDict*
```Python
    ex: [ { "S35" : [ (17462,4,1), (16745,3,2)] } , { "S23" : [ (17462,3,3), (16745,4,2)] } ]
```
4. A list of available positions. Will be called *positionList*
```Python
    ex: [ "Production Planning Intern", "Quality Intern", "Purchasing Intern" ]
```

## Code

Write a module called *Select.py* with the following classes:

### `Candidate`

```Python
class Candidate:
    """An object of Candidate will have a candidateID, a name, a experienceScore, an interviewScore,a gpaScore 
       and an hourly rate.
    """

    def __init__(self, candidateID, name, experienceScore, interviewScore, gpaScore, hourlyRate):
        """Creates a new candidate object with the instance attributes of its type.

         Parameters:
            self
            candidateID : int
            name: String
            experienceScore: Float -- score for experience calcuated in the function calcExperience
            interviewScore : Float -- score for interview calcuated in the function calcInterview
            gpaScore : Float -- gpa of candidate expressed on a 10 point scale ex. 3.5/4 = 8.75/10
            hourlyRate : Float -- hourly rate of candidate, default is $15/hour
        """

    def __repr__(self):
        """Create a string representation for each Candidate created in the format (CandidateName, AverageScore). 
           This will be used in the report function.

        Parameters:
            self
        """

    def __eq__(self, other):
        """Compares two Candidates to test equality. Candidates are equal if their candidateIDs are equal.

        Parameters:
            self
            other: Candidate Object -- the second Candidate you are comparing to the first

 
    def __gt__(self, other):
        """Comparison function to allow sorting of Candidate. Candidates are sorted by average score form the 3 
           scores of gpa, experience, and interview.
        Parameters:
            self
            other: Candidate Object -- the second Candidate you are comparing to the first

    def calcExperience(self, experienceDict, positionList):
        """ Calculates the experience score for the candidate.The experience score is number of relevant experiences
            divided by number of positions available. A Relevant Experience is an experience where a keyword from the 
            available positions list matches a keyword in the candidate's work experience. For each keyword match
            $1 should be added to the candidates hourlyRate. Note that co-op and intern should not be keywords that 
            are matched.

            ex: if a candidate has "Business Analyst" as a relevant work experience and "Supply Chain Analyst" is an 
            available position, this is a match. If "Analyst" is a keyword in multiple available positions, all are 
            considered matches. 

            Parameters:
                self
                experienceDict : dictionary supplied by user, see above for full description
                positionList : list supplied by user, see above for full description

    def calcInterview(self, interviewDict):
        """Calculates the interview score for the candidate. The behavioral and technical scores are each out of 5, 
           and these will be added together for each interviewer that interviewed the candidate. The overall Interview 
           score is the average over all interviewer scores.

           ex: Interviewer 1 gave a 3 and 4 for a total of 7. Interviewer 2 gave a 4 and 1 for a total of 5. The overall 
               interviewScore for the candidate (5+7)/20.


        Parameters:
            self
            interviewDict : dictionary supplied by user, see above for full description


```
### `Interviewer`
```Python
class Interviewer:
    """This is class is to make the interviwer objects, who are the people that interviewed the candidates.
       These interviewers need to be matched to the Candidate objects.
    """

    def __init__(self, superID, candidateList):
        """ Initializes a new instance of the interviewer class with the following: a superID and a candidateList.
            The candidatelist will contain candidate objects that match with the interns and is initialized to be an
            empty list.

        Parameters:
            self
            superID: string - the ID to identify a supervisor. Note these begin with a letter
            candidateList: list - the list of matched candidate objects
        """

   def matchCandidates(self,interviewerDict):
        """This method matches interviewers to candidates. An interviewer should be matched with the candidates 
           he/she gave the top 2 behavioral scores to. Recall that the scores are in the format (technical, behavioral).
           If there are ties, include all candidates that tie.

           Parameters:
           self
           interviewerDict : dictionary supplied by user, see above for full description

```

### `Main`

The main function should take in the command line arguments as inputs and create candiate and interview objects.
Then, using the methods above, a list of tuples ranking the candidates should be returned. Each tuple is in the format(CandidateID, hourlyRate, matchedInterviewers). The matchedInterviewers should be a list of all interviewers that have matched with the candidate. The output list should be ranked in descending order with the candidate with the highest average score first, and lowest average score last.


```Python
def main(args):
    # code intended to be executed when run as a script

if __name__=="__main__":
   import sys
   main(sys.argv)
```

Here is a sample run of the homework. Note that each argument is separated by a space. 
```sh
python hw2.py  [(John Doe,17462,3.45),(Jane Doe,16745,3.67)] [{17462:["Supply Chain Intern","Bussiness Analyst Intern"]}, {16745:["Bussiness Supply Intern", "Publix Cashier"]}] [{"S35":[(17462,4,1),(16745,3,2)] },{"S23":[ (17462,3,3),(16745,4,2)]}] ["Production Planning Intern", "Quality Analyst", "Supply Chain" Intern"]
```

The expected output for running the file with these arguments is:
```sh
 [(17462,18,"S23"), (16745,16,"S35")]
```

Feel free to make longer test cases to check your output.

## Submission Instructions

Attach your `hw2.py` file to your Canvas HW2 assignment submission.

## Verify Your Canvas Submission!

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

## Rubric

Candidate Class - 50 Points
- init: 5 Points for instantiating variables correctly
- repr: 5 Points for a string representation of the object
- eq: 5 points for testing equality
- gt: 5 points for correct implementation
- calcExperience : 15 points for correct implementation
- calcInterview : 15 points for correct implementation

Interview Class - 20 points
- init : 5 points
- matchInterns : 15 points

Main - 30 points
- 20 points for creating Candidate and Interview Objects from the input
- 10 points for correctly ordering output

  
