<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
    <a href="https://github.com/mauriciohc02/Perpendicular-Bisector">
        <img src="images/app_icon.png" alt="Logo" width="80" height="80">
    </a>
    <h3 align="center">Perpendicular-Bisector</h3>
    <p align="center">
        An awesome App to undersand how Perpendicular Bisectors are drawn!
        <br />
        <a href="https://github.com/mauriciohc02/Perpendicular-Bisector"><strong>Explore the docs »</strong></a>
        <br />
        <br />
        <a href="https://github.com/mauriciohc02/Perpendicular-Bisector">View Demo</a>
        ·
        <a href="https://github.com/mauriciohc02/Perpendicular-Bisector/issues">Report Bug</a>
        ·
        <a href="https://github.com/mauriciohc02/Perpendicular-Bisector/issues">Request Feature</a>
    </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#about-the-project">About The Project</a>
            <ul>
                <li><a href="#built-with">Built With</a></li>
            </ul>
        </li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li><a href="#prerequisites">Prerequisites</a></li>
                <li><a href="#installation">Installation</a></li>
            </ul>
        </li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#license">License</a></li>
    </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Perpendicular-Bisector Screen Shot][product-screenshot]](https://github.com/mauriciohc02/Perpendicular-Bisector/blob/main/images/screenshot.png)

The bisector of a segment is the line perpendicular to said segment drawn by its midpoint. Equivalently it can be defined as the locus of all points that are equidistant from the endpoints of the segment. 

The perpendicular bisectors of the sides of a triangle intersect at a common point, which is the center of the only circle to which the three vertices of the triangle belong. This point is called the circumcenter.

Move points A, B and C to see what happens.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Pyqt5][Pyqt5]][Pyqt5-url]
* [![Docker][Docker]][DockerImage-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Before you begin, it is good to know that there are two different ways to deploy the application:

1.  **Traditional Method:** Installing every single python library and package in order to run the app successfully.

2.  **Docker Method:** Pulling the docker image in order to run the app successfully.

So, to get a local copy up and running the project follow these simple steps.


### Prerequisites

* First of all, ensure you have met one of the following requirements, depending on the method already chosen:
    - [Python][Python-url]
    - [Docker][Docker-url]


### Installation

1. For both deploy methods **clone this repository**.
    ```bash
    git clone https://github.com/mauriciohc02/Perpendicular-Bisector.git
    ```

2.  Get into the **project directory**.
    ```bash
    cd Perpendicular-Bisector/
    ```

3.  If you chose the **Traditional Method** run the first command to install the modules or packages, otherwise for the **Docker Method** just pull the docker image as shown in the last command.
    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    docker pull mauriciohc/perpendicular-bisector
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1.  **Traditional Method:** Run the python command below:
    ```bash
    python3 main.py
    ```

2.  **Docker Method:** To deploy the project, you have to run some commands and the [`docker-compose.yml`][Compose-url], but with the [`run.sh`][Script-url] script you can run it with just the following command.
    ```bash
    bash run.sh
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE.md`][license-url] for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/mauriciohc02/Perpendicular-Bisector.svg?style=for-the-badge
[contributors-url]: https://github.com/mauriciohc02/Perpendicular-Bisector/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mauriciohc02/Perpendicular-Bisector.svg?style=for-the-badge
[forks-url]: https://github.com/mauriciohc02/Perpendicular-Bisector/network/members
[stars-shield]: https://img.shields.io/github/stars/mauriciohc02/Perpendicular-Bisector.svg?style=for-the-badge
[stars-url]: https://github.com/mauriciohc02/Perpendicular-Bisector/stargazers
[issues-shield]: https://img.shields.io/github/issues/mauriciohc02/Perpendicular-Bisector.svg?style=for-the-badge
[issues-url]: https://github.com/mauriciohc02/Perpendicular-Bisector/issues
[license-shield]: https://img.shields.io/github/license/mauriciohc02/Perpendicular-Bisector.svg?style=for-the-badge
[license-url]: https://github.com/mauriciohc02/Perpendicular-Bisector/blob/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mauricio-hernandez-cepeda
[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/PYTHON-V3.10-blue?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/
[Pyqt5]: https://img.shields.io/badge/PYQT5-V5.15.7-blue?style=for-the-badge&logo=qt
[Pyqt5-url]: https://pypi.org/project/PyQt5/
[Docker]: https://img.shields.io/docker/pulls/mauriciohc/perpendicular-bisector?logo=docker&style=for-the-badge
[DockerImage-url]: https://hub.docker.com/r/mauriciohc/perpendicular-bisector

[Docker-url]: https://hub.docker.com/
[Compose-url]: https://github.com/mauriciohc02/Perpendicular-Bisector/blob/main/docker-compose.yml
[Script-url]: https://github.com/mauriciohc02/Perpendicular-Bisector/blob/main/run.sh
