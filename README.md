Do What?
========

`do-what.sh` helps you figure out what you have been doing. Executing the script will print the date and the name of the current foreground app. By adding this to a crontab every minute, for example, you can sample what you have been up to throughout the day.

`summarise.py` provides a simple script to summarise what you have been doing from data collected with `do-what.sh`. Usage is: summarise.py file [start] [end], where file is the stored data, start is the start time over which metrics should be processed (default 1 day ago), end is the end time with which metrics should be processed (default now).
