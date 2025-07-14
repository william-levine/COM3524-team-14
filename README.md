# COM3524
running python tools on docker container

#  MACOS
Steps:
1. Install docker desktop 
2. Install xQuartz
3. xhost +IP_ADDRESS
4. Run the docker file 
> [!IMPORTANT]
> 

# WindowsOS
Steps:
1. Installl vcxsrv and docker
2. Run both applications on the back
3. Run the vcxsrv with variable set to 0 instead of -1
4. Run the following commands 

```bash 
    Docker build —no-cache -t com3524-toolkit
```

```bash
    Docker run -it -p 5000:5000 -e DISPLAY=host.docker.internal:0 com3524-toolkit
```

# LinuxOS
1. Install linux cli using online website installation for docker - docs.docker.com/engine/install/ubuntu
2. Set up docker repository
3. Test docker using sudo docker run hello-world
4. Use this website hosting.com/tutorials/how-to-fix-docker-permission-denied-error
5. Run it with docker run it -e DISPLAY=:0 -v/tmp/ .X11-unix:/tmp/.X11-unix 




