#included this block of code to ignore DeprecationWarning only due to using sklearn library with 
#some outdated syntax 
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

from jobs import * 
from dbms_connection import *

if __name__ == '__main__':
	mode = input("Press '1' to track data.\nPress '2' to activate machine learning.\n")
	if(mode == '1'):
		run_trackingjob()
	elif(mode == '2'):
		run_MLjob()
	else:
		exit(0) 
