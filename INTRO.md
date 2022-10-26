# Hoffman2 Big Data Workshop

To follow along the workshop, you may want to setup your environment beforehand. 

## Clone this GitHub Repo

You will need to clone this repo to run these examples.

I would recommend to clone this in your `$SCRATCH` directory on Hoffman2.

First, login to Hoffman2

```{.bash}
ssh joebruin@hoffman2.idre.ucla.edu 
```

Clone the repo in your `$SCRATCH` directory

```{.bash}
cd $SCRATCH
git clone https://github.com/ucla-oarc-hpc/WS_BigDataOnHPC
```

You will have this repo located at `$SCRATCH/WS_BigDataOnHPC`

- Keep note of the full directory PATH of this Workshop

```{.bash}
echo $SCRATCH/WS_BigDataOnHPC
```

## Setup for running Jupyter

We will use Jupyter on Hoffman2. We have a easy to use script `h2jupynb` to start Jupyter

Make sure you have python3 on your LOCAL computer to run `h2jupynb`

The following code will need to run ran on your LOCAL computer.

```{.bash}
wget https://raw.githubusercontent.com/rdauria/jupyter-notebook/main/h2jupynb
chmod +x h2jupynb
```

To start Jupyter, you will run

```{.bash}
python3 ./h2jupynb -u joebruin -t 5 -m 10 -e 2 -s 1 -a intel-gold\\* -x yes -d /SCRATCH/PATH/WS_BigDataOnHPC
```

Replace `joebruin` with your Hoffman2 user account.

Replace `/SCRATCH/PATH/WS_BigDataOnHPC` with the full PATH name of the workshop on Hoffman2

More information on running Jupyter can be found on the Hoffman2 webpage.

<https://www.hoffman2.idre.ucla.edu/Using-H2/Connecting/Connecting.html#connecting-via-jupyter-notebook-lab>

## Install PySpark

We will use Spark and the python API, PySpark, in this workshop and install it with Anaconda on Hoffman2. 

You may want to install it before the workshop.

```{.bash}
module load anaconda3/2022.05
conda create -n mypyspark openjdk pyspark python=3.9 \
                          pyspark=3.3.0 py4j jupyterlab findspark \
                          h5py pytables pandas \
                          -c conda-forge -y
conda activate mypyspark
pip install ipykernel
ipython kernel install --user --name=mypyspark
```

This will create a conda env named, mypyspark, and add this kernel for use by Jupyter

Information on using Anaconda can be found on our recent Anaconda workshop.

<https://github.com/ucla-oarc-hpc/H2HH_anaconda>

## Install Spark

Although Spark was installed along PySpark with Anaconda, we will use an example with a separate Spark build downloaded from the Spark site.

```{.bash}
mkdir -pv $SCRATCH/WS_BigDataOnHPC/apps/spark
cd $SCRATCH/WS_BigDataOnHPC/apps/spark

wget https://dlcdn.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz
tar -vxf spark-3.3.0-bin-hadoop3.tgz
```

## Install Dask

We will install Dask using Anaconda

```{.bash}
conda create -n mydask python pandas jupyterlab  joblib \
                       dask dask-ml nodejs graphviz python-graphviz \
                       -c conda-forge -y
conda activate mydask
pip install ipykernel
ipython kernel install --user --name=mydask
```

This will create a conda env named, mydask, with Dask and Jupyter.


## Download Datasets

We will use multiple Datasets throughout this workshop

"The Hound of the Baskervilles, by Arthur Conan Doyle from Project Gutenberg <https://www.gutenberg.org/>

```{.bash}
cd $SCRATCH/WS_BigDataOnHPC
cd spark-ex1
wget https://www.gutenberg.org/files/3070/3070.txt
```

Million song subset <http://archive.ics.uci.edu/ml/datasets/YearPredictionMSD>

```{.bash}
cd $SCRATCH/WS_BigDataOnHPC
cd dask-ex2
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip
unzip YearPredictionMSD.txt.zip

cd $SCRATCH/WS_BigDataOnHPC
cd spark-ex2
cp $SCRATCH/WS_BigDataOnHPC/dask-ex2/YearPredictionMSD.txt
```

Dataset from LIBSVM. <https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/>

```{.bash}
cd $SCRATCH/WS_BigDataOnHPC
cd spark-bonus
wget https://raw.githubusercontent.com/apache/spark/master/data/mllib/sample_libsvm_data.txt
``` 
