# WebScrapper
WebScrapper using python libraries

first install the required libraries for this project that is requests and BeautifulSoup4
then create the conda env by downloading it first from browser then write the following command:
1. conda create --name env_name python=3.10 // here I used python 3.11.3 and you can give any name to env_name
2. now you have to activate the environment by running the command: conda activate env_name

Now the environment setup is done
Run the python code by:
python3 <filename> <url> <output_file_name>  for this project this command is wirtten as :- 
python3 Project1.py https://www.reddit.com/r/funny/comments/16ke3e5/can_anyone_verify_this_stuff/ output.txt

this will create a file name output.txt containing all the dump data

to create the yaml package:
conda env export > requirement.yaml

this will give you a yaml file of conda environment
