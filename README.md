# Data analytics - feature selection - filter method

## Introduction
This repository contains the code for the development of the filtering method of the activage analysis tools. 
In this documentation you will find information on how to build, launch and deploy the project.

## Architecture
The project provides an HTTP REST server with a single endpoint for the execution of the analysis method.

## Build and deployment

### Prerequisites:
- Install Docker
````
sudo apt-get install docker-ce
````
- Install Docker Compose
````
sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
````

### Build

#### Build docker image
Assuming you are in the project root folder, the docker image of the methods can be built executing:

```bash
$ docker build -f docker/Dockerfile -t feature-selection-filter-method:develop .
```

### Deployment
The project rely on docker for development and production deployments. The following subsections explains in detail how to 
deploy the tool using docker technology and how to configure the tool with the required environmental variables or configuration files.

```bash
$ docker run -it -p 5000:8000 --name select-features feature-selection-filter-method:develop
```

## License
```bash
Copyright 2020 HOPU

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
