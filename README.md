This script returns relevent information about advertaising campaigns using the Amplify API.

HOW TO RUN-
simply run the campaign_data_script.py file using the command - python campaign_data_script.py
PLEASE NOTE- the script expects a valid token in the 'API TOKEN.txt' file.
don't change the file location or name as the script will fail.

the script uses the following python packages - requests,json,pandas.
you can install them using the command "pip install 'package name'"

INPUT AND OUTPUT -
the script recievs a campaign id and an amount (for either you can press ENTER and a default option will be used).
the script prints to the screen the data for the given campaign id and the data for all campaigns with amount spend higher than the amount entered.
the script creates a csv file at the script's location named Jan_campaigns.csv which containes all the data for campaigns in the month of january.

HAVE FUN :)
