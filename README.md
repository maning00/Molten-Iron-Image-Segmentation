# Semantic Segmentation For Molten Iron Slag Skimming
In the metallurgical industry, molten iron slag skimming is still dependent on manual operation. This study uses the production environment data and images provided by [Baosteel](http://www.baosteel.com/group_en/) for image segmentation to provide the basis for subsequent control to achieve automatic skimming of slag.


Original            |  Pred
:-------------------------:|:-------------------------:
![alt text-1](https://dsc.cloud/8532ed/img_772.png)  |  ![alt text-2](https://dsc.cloud/8532ed/img_772_L.png)



## Description
This repository is an implementation for molten iron slag skimming image segmentation. The operation is divided into two steps:

- Image noise reduction and de-fogging(Non-essential)
- Image Segmentation

## Directories
 **Utility**: This folder contains some utilities, implementations of image defogging and traditional image segmentation. <br>
 **Image_Segmentation**: This folder contains deep Learning-based image segmentation.
