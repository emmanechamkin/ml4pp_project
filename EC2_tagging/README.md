# Read Me 

This folder was not used in my final project, but I included it for good 
measure. There are a lot of files here, and since this isn't final code that I
used in the final work I did, it is maybe less well-organized than ideal. 

In this directory, I cleaned tweets and sent them one at a time to an EC2 
instance on which I had downloaded and installed CoreNLP. I used CoreNLP. 
I had previously done this (well, something quite similar) in Alex Engler's 
Large Scale Data Methods class. 

There are about 125 lines of new code in this folder.

The files are:
- `cleaned_coded_MONTH.csv`: cleaned files of tweets, taken either as a 1 week window in April or a 1 week window in May
- `cleaned_dropped_MONTH.csv`, `final_output.csv`, `final_output_cleaned_sampled.csv`: output files from preparation 
- `code_sentiment.py`: script to prepare tweets and ping EC2 server. Although I had set up an EC2 instance as a server before, the code in this file (100 lines, about) is new.
- `combine_and_sample.py`: extremely quick script (is it even really a script?!) to sample tweets and catenate files 
- `creds.py`: credentials and configurations
- `ec2_info`: calls to start up shell. 