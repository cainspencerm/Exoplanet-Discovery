# Attention Networks for Exoplanet Discovery

The use of machine learning techniques in observational astronomy is a rapidly expanding area of research. Until recently, the process of discovering exoplanets involved human agents manually analyzing large amounts of data. However, recent advances in machine learning have greatly improved the accuracy and feasibility of such methods for exoplanet discovery. In the following paper, we will present an efficient machine learning framework based on multi headed attention transformers.

Planets located outside of our solar system are referred to as exoplanets and are of great interest to astronomers, however locating such planets can be a laborious task if done manually. There are many methods for detecting exoplanets such as Doppler Spectroscopy, the Transit Method, Pulsar Timing, etc. The present paper will focus exclusively on the Transit Method which involves observing a particular star over time and measuring its brightness. Periodic dimming of a star’s light indicates that a planet is passing between a star and the observing telescope. However, an exoplanet must pass through a very narrow region of space in order to be observed, making such occurrences rare. Furthermore, the light is subject to interference from other objects thus producing a noisy signal. As a result, the task of finding exoplanets is tedious, error-prone, and until recently, unamenable to computational analysis. Currently, 4864 exoplanets have been located by various space missions and telescopes over the past few decades with the first, M51-ULS-1b, being discovered as early as 1992. In 2009, the Kepler mission was launched specifically to search for exoplanets. Further analysis of Kepler’s data has allowed astronomers to determine the chemical composition of the atmospheres of exoplanets offering insight into the question ”How many planets exist outside of the solar system?”

Ultimately, we discovered that the addition of attention to a standard classifier didn’t significantly improve the accuracy or the execution time of the model. However, we observed that the execution time of each epoch decreased considerably in the attention model yet there was a dramatic increase in the number of epochs needed to terminate. Some future directions that we want to consider is extending our current model to accommodate more information about the habitability of exoplanets. From the lightcurve data we can calculate the distance and size of an exoplanet from its star. Similarly, the data concerning the planets can be deduced from the dataset we already have. The preliminary results from our experiments have proven to be highly informative. We have demonstrated that attention transforms can dramatically reduce the number of epochs needed to research a high accuracy.

## Installation
Install dependencies with [pip](https://pip.pypa.io/en/stable/):
```bash
pip3 install -r requirements.txt
```

## Usage
To load tensorboard for accuracy and loss curves:
```bash
tensorboard dev upload --logdir LOG_DIR
```
To train the model:
```
usage: main.py [-h] [--tensorboard-dir TENSORBOARD_DIR] [--checkpoint-dir CHECKPOINT_DIR]
               [--num-layers NUM_LAYERS] --dataset DATASET [--num-folds NUM_FOLDS]
               [--d-model D_MODEL] [--dff DFF] [--num-heads NUM_HEADS] --batch-size BATCH_SIZE
               [--epochs EPOCHS] [--verbose {0,1,2}]

Train the model using k-fold cross validation.

optional arguments:
  -h, --help            show this help message and exit
  --tensorboard-dir TENSORBOARD_DIR
                        The directory in which to store tensorboard data
  --checkpoint-dir CHECKPOINT_DIR
                        The directory in which to save the model
  --num-layers NUM_LAYERS
                        The number of attention encoder layers
  --dataset DATASET     The directory in which the dataset was saved
  --num-folds NUM_FOLDS
                        The value of k in k-fold cross validation
  --d-model D_MODEL     The number of features in the input data
  --dff DFF             The dimensionality of the linear layer in the feed forward layer
  --num-heads NUM_HEADS
                        The number of heads in the multi-headed self-attention layer
  --batch-size BATCH_SIZE
                        The number of samples per batch in the dataset
  --epochs EPOCHS       The number of iterations on which to train the model
  --verbose {0,1,2}     There are three options for the message types: 0) Minimal output 1)
                        Default output 2) All output
```
To generate accuracy and loss plots:
```
usage: create_graphs.py [-h] --id ID --image-name IMAGE_NAME

Create epoch_accuracy and epoch_loss graphs

optional arguments:
  -h, --help            show this help message and exit
  --id ID               The experiment id provided by tensorboard.dev
  --image-name IMAGE_NAME
                        The name of the output png file
```
