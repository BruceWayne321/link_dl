# link_dl
This is a python tool that can be used to download files from a list of links
This tool makes use of multiprocessing to download files parallelly

## How to use
You will need python3 to be installed in your machine
Clone the repository
run:- pip install -r requirements.txt
(This command installs all the prerequisites)

Edit the 'urls.txt' file and add all the links which needs to be downloaded (this links will be downloaded simultanously using multiprocessing, keep that in mind)

run the python file:
python3 main.py urls.txt
