### Steps to use
- Install Docker if not already
- clone repository
- commands
  - docker -v (use to cross check whether docker is installed)
  - docker ps (list of docker containers running)
  - docker build -t python-dog .  (to build docker image named 'python-dog'. You can choose any name. '.' at the end represents current directory)
  - docker run python-dog     (to run container with the image python-dog)
    
Run the commands from project directory (i.e. at the same level where main.py is)
