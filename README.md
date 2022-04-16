[![CI](https://github.com/ekimdev/espws/actions/workflows/github-ci.yml/badge.svg)](https://github.com/ekimdev/espws/actions/workflows/github-ci.yml)
![black](https://img.shields.io/badge/code%20style-black-black)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

<br />
<div align="center">
  </a>
  <h3 align="center">ESP8266 Weather Station</h3>
  <p align="center">
    <img src="assets/DHT11-Nodemcu.png" title="pin diagram">
    <br />
    <a href="https://github.com/ekimdev/espws/issues">Report Bug</a>
    ·
    <a href="https://github.com/ekimdev/espws/issues">Request Feature</a>
  </p>
</div>

**Weather Station** powered by ESP8266, Python, Docker, MQTT  and InfluxDB
![diagram](assets/diagram.png)

## Getting Started

### Prerequisites
Have installed on your pc:
  - Python >= 3.7
  - Docker and Docker Compose

And an ESP8266.

### Installation
1. Clone the repo
  ```
  git clone https://github.com/ekimdev/espws.git
  ```
2. Change the macros in firmware/config.h with the network data
3. Compile and upload the firmware to your ESP
4. Start docker services
  ```
  docker-compose up
  ```
5. Connect your ESP and the listener will start sending data! :)

### Usage
