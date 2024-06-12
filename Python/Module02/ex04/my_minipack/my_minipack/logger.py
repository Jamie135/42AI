import time
import os

def logger(ft):

    def wrapper(*args, **kwargs):
        # get the user from the environment variable
        user = os.getenv('USER', 'unknown')

        start = time.time()
        
        # Execute the ft
        res = ft(*args, **kwargs)
        
        end = time.time()
        
        # execution time in milliseconds (hence * 1000)
        exec_time = (end - start) * 1000
        
        # format the log message by using each decorator's name, replace the _ by a space and use title() method on it
        log_msg = f"({user})Running: {ft.__name__.replace('_', ' ').title():<20} [ exec-time = {exec_time:.3f} ms ]\n"
        
        # Write the log msg to the log file
        with open('machine.log', 'a') as log_file:
            log_file.write(log_msg)
        
        return res
    
    return wrapper
