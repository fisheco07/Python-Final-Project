# Python-Final-Project

This script allows you to clean and format CSV files and sends the contents of the input file to an output file.
It allows you to put in the input file that you would like to be cleaned or formatted and it transfers the data to a new output file that you designate the name for.

How to use:
A help option is included in this script by typing CSV_Cleanup.py -h, but this is an overall explanation of how to use the script.
To run the script you need to type depending on what version of Python you have either Python or py then the name of the script. For my case my version uses py.
To run the script type
 
 py .\CSV_Cleanup.py.

Then you need to include the input and output file and for this script it is input like this:

py .\CSV_Cleanup.py --input uncleaned_file.csv --output cleaned_file.csv

So for this script you need to identify the names of the files which are going to be your input and output files.
Running this will help formatt your data by removing duplicates and trimming the spaces around words, but it won't remove multiple spaces between the sections of your data.
To do this regex needs to be used, which this script supports. 
Adding regex to the command will make it so that the duplicates are removed, spaces around words are trimmed, and it will get rid of the multiple spaces between the sections of your data.
To run this script with regex it is the same without it but with --regex included at the backend.
So your full input will look like this:

py .\CSV_Cleanup.py --input uncleaned_file.csv --output cleaned_file.csv --regex

This will then cleanup the input file you put into the tool and send it to an output file which you determine the name of. 
The data data then will be more presentable and easier to read.

Why is it helpful?
This script is helpful because if you have a file that is not formatted and you want to be able to analyze and process the contents of the file a lot easier.
This script helps simplify the process of doing that because it automates that process.
Instead of having to go into the file and format it yourself you can use this script.
This script is also simple to use once you learn how to input the input and output files and how to use the regex option.
This script also helps with error handling because it determines if a file exists and it ensures that the input and output files are CSV files. And if the script determines that a CSV file is not used then it sends an error message telling the user that .csv files are the only supported file type and the script starts from the beginning.

