In order to run this program you must activate the virtual env.
On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate
On Unix or MacOS, using the csh shell: source /path/to/venv/bin/activate.csh
On Unix or MacOS, using the fish shell: source /path/to/venv/bin/activate.fish
On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat
On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1

Open CMD in the root directory of the project and tun the following command - 
& pytest --html=report.html
After the run a new report.html file will be created and will represent if the test cases passed or fail