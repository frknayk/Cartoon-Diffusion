<h1 align="center"> Cartoon Diffusion V1 </h1>
<h3 align="center">  Generate cartoon like images from user prompt </h3>

</br>

<p align="center">
  <img src="files/project_icon.png" alt="Sample signal" width="10%" height="10%">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png) 
<h2 id="about-the-project">Project Overview</h2>
<p align="left">
  <img src="files/App_Overview.png" alt="Project Overview" width="40%" height="40%">
</p>

<h2 id="liveApp" href=> <a href="https://text2imagegen.streamlit.app/"> Try App Live with Streamlit! </a> </h2>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project">About The Project</h2>

<p align="justify">
Welcome to the Stable Diffusion based text-to-image generative AI repository!
</p>
This readme file provides you with all the necessary information to install, run, and understand the Stable Diffusion AI model.
</p>

<!-- ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2 id="liveApp" href=> <a href="https://rlcontrol.streamlit.app"> Try the App Live with Streamlit! </a> </h2> -->


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- INSTALL HOW TO -->
<h2 id="install"> Installation and Training Steps</h2>

<p align="justify">
  <a href="README_TRAIN.md" target="_blank">Please follow the training guide</a>

<p align="justify">


  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 id="install">Running App Locally </h2>
  
    0. Install the requirements
      Follow 'Installation' section in README_TRAIN.md file
    1. Create and activate tti_env environment
      `conda activate tti_env`
    2. Train the algorithm
      Follow 'Running Training' section in README_TRAIN.md file
    3. Run the app for test trained AI and watch app at `http://localhost:8502`
      `streamlit run app.py` 

<h2 id="install">Deployment</h2>

  Build docker image for web/cloud deployment. 
  - `docker build -t t2img_docker .`

  Streamlit/Gradio will automatically build docker image from this dockerfile.

  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- PREREQUISITES -->
<h2 id="prerequisites"> :fork_and_knife: Prerequisites</h2>

The following open source packages are used in this project:
* torchvision
* accelerate>=0.16.0
* transformers>=4.25.1
* datasets
* ftfy
* tensorboard
* Jinja2
* xformers
* bitsandbytes
* scipy
* streamlit

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 id="future"> Future Work </h2>

* Add different models
* Search datasets online
* Add training page(requires hardware)
