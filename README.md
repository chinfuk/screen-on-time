# screen-on-time

this project reads a csv file that is filled with data collected by tasker 

link to tasker profile https://taskernet.com/shares/?user=AS35m8l6Hhkw6YgyqX83vusWAS%2B4J%2FaaZPCyamgMwsF1vmH%2FwdQWCqheSW99M5kVNulrzg%3D%3D&id=Project%3AScreen+On

take note of where tasker is spitting out the csv files. there is an 'upload to google drive' action in the writecsv task (optional).

tasker will flash total everytime the screen is unlocked, add a  1x1 tasker widget to the home screen and link it to 'flash' to show the current total at any time by clicking the widget.

included is a small sample.csv file for testing

at the moment the csv is added with the comand line arguments. ie, '>python screentime.py sample.csv' 
i hope to make this more autonomous in the future
