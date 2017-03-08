#TensorFlow Lab
We've prepared a Jupyter notebook that will guide you through the process of creating a single layer neural network in TensorFlow. You'll implement data normalization, then build and train the network with TensorFlow.

Getting the notebook
The notebook and all related files are available from our GitHub repository. Either clone the repository or download it as a Zip file.

Use Git to clone the repository.

git clone https://github.com/udacity/deep-learning.git

Once you have the repo cloned or downloaded, change directories into the repo, then the intro-to-tensorflow directory. In there you'll find the lab notebook, as well as Conda environment files for installing all the necessary packages.
Windows Instructions
We've provided a Conda environment file for you to easily install all the necessary packages. In the intro-to-tensorflow directory, enter

conda env create -f environment_win.yml
This will create an environment called dlnd-tf-lab. You can enter the environment with the command

activate dlnd-tf-lab
All the necessary packages should be installed for you.
OS X and Linux Instructions
We've provided a Conda environment file for you to easily install all the necessary packages. In the intro-to-tensorflow directory, enter

conda env create -f environment.yml
This will create an environment called dlnd-tf-lab. You can enter the environment with the command

source activate dlnd-tf-lab
All the necessary packages should be installed for you.
View The Notebook
In the directory with the notebook file, start your Jupyter notebook server

jupyter notebook
This should open a browser window for you. If it doesn't, go to http://localhost:8888/tree. Although, the port number might be different if you have other notebook servers running, so try 8889 instead of 8888 if you can't find the right server.

You should see the notebook intro_to_tensorflow.ipynb, this is the notebook you'll be working on. The notebook has 3 problems for you to solve:

Problem 1: Normalize the features
Problem 2: Use TensorFlow operations to create features, labels, weight, and biases tensors
Problem 3: Tune the learning rate, number of steps, and batch size for the best accuracy
This is a self-assessed lab. Compare your answers to the solutions here. If you have any difficulty completing the lab, Udacity provides a few services to answer any questions you might have.

Help
Remember that you can get assistance from your mentor, the Forums (click the link on the left side of the classroom), or the Slack channel. You can also review the concepts from the previous lessons.
