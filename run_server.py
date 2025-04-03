import os
import sys
import webbrowser
from django.core.management import execute_from_command_line

def main():
    # Get the directory where the executable is located
    if getattr(sys, 'frozen', False):
        # If we're running as a compiled executable
        application_path = os.path.dirname(sys.executable)
    else:
        # If we're running as a script
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the application directory
    os.chdir(application_path)
    
    # Start the Django server
    sys.argv = ['manage.py', 'runserver']
    execute_from_command_line(sys.argv)
    
    # Open the browser
    webbrowser.open('http://127.0.0.1:8000')

if __name__ == '__main__':
    main() 