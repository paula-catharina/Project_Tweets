Tweets Project Documentation and Tutorial

For this project there was two hypothesis considered:
-hashtags shouldn't be considered as words for word count;
-stopwords shouldn't be removed since there was no indication that they shouldn't be counted as words for this project.
-------------------------------------------------------------------------------------------------------------------------------
1.Building and running code with docker:

1.1. Download and install docker following the instructions of the website:
https://docs.docker.com/install/

1.2. Set directory with files 

Examples:
-windows: C:\Project_Tweets
-linux: /home/user/Project_Tweets

1.3. On cmd prompt or Linux bash go to the directory chosen

1.4. Create a docker image ready to run python script with requirements using the following command:
docker build --tag prepared_python_image.

1.5. Run script with following command:

Windows: 
docker run -t -i -v C:/Project_Tweets:/Project_Tweets  prepared_python_image /bin/bash -c "cd /Project_Tweets; python tweets_processor.py"

Linux:
docker run -t -i -v /home/user/Project_Tweets:/Project_Tweets  prepared_python_image /bin/bash -c "cd /Project_Tweets; python tweets_processor.py"

Obs.: This command will run the script inside of a container with prepared_python_image using the shared host directory(give permission for sharing if necessary). This approach was chosen because the container shuts down after the application is over and loses its data, so it wouldn't be possible to check output files if the script and dataset were included inside docker image.

1.6. After running, output files can be found on shared host directory and they are:
-output1.csv: list of every unique word among all tweets and a count of all repeated words;
-output2.csv: the median number of unique words per each tweet;
-unique_words.png: plot of the count of unique words per tweet;
-unique_words_count_boxplot.png: boxplot of unique word count per tweet;
-words_frequecy.png: horizontal bars plot for the 30 most common words and its frequencies.
-------------------------------------------------------------------------------------------------------------------------------
2.Building and running *without* docker

2.1. Set directory with files 

Examples:
-windows: C:\Project_Tweets
-linux: /home/user/Project_Tweets

2.2. On cmd prompt or Linux bash go to the directory chosen

2.3. Install the requirements using the following command:
pip install -r requirements.txt

2.4. Run script with the following command:
python tweets_processor.py

2.4. After running, output files can be found at the chosen directory (for descriptions see section 1.6).