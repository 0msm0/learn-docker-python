import requests

if __name__ == '__main__':
    res = requests.get("https://random.dog/woof.json").json()
    print(res)

# Some commands
# docker -v                     ## to check version
# docker ps                     ## list of docker containers running
# docker build -t python-dog .  ## to build docker image. 'python-dog' is an arbitrary name given to the image. '.' represents current directory
# docker run python-dog     ## to run container with the image python-dog

## Note - for interactive code such as input(), use focker run -t -i  (-i means interactive, which allows user to give his inputs)