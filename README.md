# Module 3: PyPoll with Python

## Overview of Election Audit

### Purpose
The purpose of this analysis is to perform an election audit of the tabulated results for U.S Congressional precinct in Colorado. This analysis will determine the candidates of the election, their total vote count, their total vote percentage from the total count, and the winning candidate. Information regarding the voter turnout for each county, percentage of votes from each county from the total count, and the county with the highest voter turnout will also be analyzed. 

### Resources
- Data Source: [election_results.csv](https://github.com/daniel-sh-au/UofT_DataBC_Module03_election-analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.6.7, Visual Studio Code 1.67.2
- PyPoll Challenge Code: [PyPoll_Challenge.py](https://github.com/daniel-sh-au/UofT_DataBC_Module03_election-analysis/blob/main/PyPoll_Challenge.py)


## Election-Audit Results
Please refer to the election results from the following text file: [election_results.txt](https://github.com/daniel-sh-au/UofT_DataBC_Module03_election-analysis/blob/main/analysis/election_results.txt)

- **369,711** votes were cast in this congrssional election.

- A breakdown of each county and their results are listed below:
  - Jefferson: **38,855** votes were casted from Jefferson, which made up **10.5%** of the total vote count.
  - Denver: **306,055** votes were casted from Denver, which made up **82.8%** of the total vote count.
  - Arapahoe: **24,801** votes were casted from Arapahoe, which made up **6.7%** of the total vote count. 

- The county with the highest voter turnout was **Denver**. 

- A breakdown of each candidate and their results are listed below: 
  - Charles Casper Stockham: **85,213** votes were casted for Stockham, which made up **23.0%** of the total vote count.
  - Diana DeGette: **272,892** votes were casted for DeGette, which made up **73.8%** of the total vote count.
  - Raymon Anthony Doane: **11,606** votes were casted for Doane, which made up **3.1%%** of the total vote count.

- The candidate with the highest vote count was **Diana DeGette** with **272,892** votes (**73.8%** of the total vote count)

## Election-Audit Summary
For future elections, this script can be modified to check the Ballot ID column for duplicates. This can be useful for determining if anybody voted twice during the election. Additionally, for larger elections, it may be beneficial to modify the script to read from multiple csv files and report the consolidated results. Since Excel has a limit of 1,048,576 rows and U.S. federal elections can exceed 158 million ballots (in 2020), reading from multiple files will optimize the analysis for these elections. Alternatively, the U.S. may choose to store their federal election data in databases and in that scenario, the script should be modified to extract data from databases instead of csv files. 
