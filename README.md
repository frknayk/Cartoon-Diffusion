<h1 align="center"> Composer </h1>
<h3 align="center">  Generate images from text input </h3>

</br>

<p align="center">
  <img src="files/project_icon.png" alt="Sample signal" width="10%" height="10%">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify">
    The project aims to generate images from text provided by users as a web-based application
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2 id="liveApp" href=> <a href="https://rlcontrol.streamlit.app"> Try the App Live with Streamlit! </a> </h2>


<p align="center">
  <img src="files/training_page.jpg" alt="Training Page" width="80%" height="80%">
</p>
<p align="center">
  <img src="files/test_page.jpg" alt="Testing Page" width="80%" height="80%">
</p>
<p align="center">
  <img src="files/pid_page.jpg" alt="PID Control Page" width="80%" height="80%">
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- INSTALL HOW TO -->
<h2 id="install"> Installation Steps</h2>

<p align="justify">
  Follow steps below,

    1. Create Conda environment:
        - 'conda env create --name rlcontrol --file=environment.yml'

    2. Install OpenAI Gym Environment
        - Install gym_control environment: `pip install -e .`

    - Export conda env yaml: `conda env export > environment.yml --no-builds`
    - Export conda env yaml as requirements.txt: `conda list -e > requirements.txt`

<p align="justify">
  
<h2 id="install">Run the App Locally </h2>
  
    1. Activate rlcontrol environment
      `conda activate rlcontrol`
    2. Run streamlit app and watch app at `http://localhost:8502`
      `streamlit run app.py` 
  
  Build for docker based deployment
  - `docker build -t streamlit .`

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
