<h1 align="center"> Cartoon Diffusion V1 </h1>
<h3 align="center">  Generate cartoon like images from user prompt </h3>

</br>

<p align="center">
  <img src="files/project_icon.png" alt="Sample signal" width="10%" height="10%">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project">About The Project</h2>

<p align="justify">
    The project aims to generate images from text provided by users as a web-based application
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2 id="liveApp" href=> <a href="https://rlcontrol.streamlit.app"> Try the App Live with Streamlit! </a> </h2>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- INSTALL HOW TO -->
<h2 id="install"> Installation Steps</h2>

<p align="justify">
  Please follow the [training guide](#README_TRAIN.md)

<p align="justify">
  
<h2 id="install">Run the App Locally </h2>
  
    1. Activate rlcontrol environment
      `conda activate rlcontrol`
    2. Run streamlit app and watch app at `http://localhost:8502`
      `streamlit run app.py` 
  
  Build for docker based deployment
  - `docker build -t t2img_docker .`

  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- PREREQUISITES -->
<h2 id="prerequisites"> :fork_and_knife: Prerequisites</h2>

<!--This project is written in Python programming language. <br>-->
The following open source packages are used in this project:
* torch
* tensorboardx
* tqdm
* numpy
* matplotlib
* plotly
* pandas
* streamlit

* 
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 id="future"> Future Work </h2>
  - Track experiments from db (postgresql)
  - Fix seeds
