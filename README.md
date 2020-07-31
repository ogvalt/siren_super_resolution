## Siren super resolution

### ToDo:
- [x] try poetry  
- [x] install hydra-core, catalyst, dotenv 
- [x] build runtime based on Dockerfile 

### Install

### Dataset

https://data.vision.ee.ethz.ch/cvl/DIV2K/

## Known Issues

1. Repo heavily rely on `pytorch`. 
`pytorch` sync their release schedule with `CUDA` schedule.
This leads to a situation when you'll need to update your runtime
environment with `CUDA` releases too.  
If you are getting any `CUDA` related errors or `pytorch` could find
any `CUDA` devices, make sure that you have you the same supported 
version in your runtime environment and installed `pytorch`.
Fixes: 
```
# check docker/Dockerfile
FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
# to e.g.
FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04
# set it to proper version of cuda

# or

# downgrade pytorch manually by checking
# https://pytorch.org/get-started/locally/
# e.g.
pip install torch==1.6.0+cu101 \
            torchvision==0.7.0+cu101 \
            -f https://download.pytorch.org/whl/torch_stable.html
# for cuda 10.1 version 
```  
