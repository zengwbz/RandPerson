# RandPerson
This project contains the ReandPerson dataset described in our paper "Surpassing Real-World Source Training Data: Random 3D Characters for Generalizable Person Re-Identification".

![fig1](https://github.com/VideoObjectSearch/RandPerson/blob/master/img/example.jpg)  

## Table of Contents

- [Dataset Description](#link-of-the-dataset)
- [Characters and Scenes](#characters-and-scenes)
- [Experimental Results](#experimental-results)
- [Citation](#citation)

## Dataset Description

The RandPerson dataset is generated by MakeHuman and Unity. For researching viewpoint, 8000 batch generation identities and 11 unity scenes are used in this version (as shown in the following figure), including eight outdoor and three indoorscenes. Due to the large amount of data, only a subset of the experiment is provided, currently.

Experiments subset images can be downloaded from the following links:<br>
* Baidu Yun Drive: 
	* images [link](https://pan.baidu.com/s/1peTSlhze9BzDQGbcakkz2w) (code:ueeg)<br>
* Google Drive: 
	* subset images [link](https://drive.google.com/file/d/12u1xdVo6-Q-i_knsbrBrRkClFkq10oNH/view?usp=sharing)<br>

Directories & Files of images
```shell
randperson_subset
├── 000000_c00_s00_f000264.jpg
├── 000000_c00_s00_f001032.jpg
├── 000000_c01_s00_f001632.jpg
```

Name of the image

Taking "000000_c00_s00_f000264.jpg" as an example: 
*  000000 is the id of the person
*  c00   is the id of the camera
*  s00   is the id of the scene
*  f000264   is the number of frames

## Characters and Scenes
MakeHuman (http://www.makehumancommunity.org/) is a free and open-source software used to create 3D character models. Characters in MakeHuman are built upon a standard 3D body shape, using various body extensions (e.g. hairstyles and beards), clothes, and accessories. Clothes models include most ordinary types of clothing, such as dresses, suits, shirts, coats, jeans, trousers, shorts, and skirts. Fig. 2 shows some examples of different types of clothing. In MakeHuman, new 3D characters are created through simple drag and drop operations in the working panel, so as to combine various components together and adjust their attributes, such as skeleton, body parameters, clothes, etc. Fig. 3 shows an example of how to create a 3D character in MakeHuman. After UV mapping, the textured 3D components can be applied to the standard 3D human model to form a new individualized 3D character.

![fig2](https://github.com/VideoObjectSearch/RandPerson/blob/master/img/makehuman.jpg)  

Since each clothing model comes with a UV texture map defining the clothing texture, altering this can significantly change the appearance of the clothing. Therefore, we propose to generate a large number of clothing models by altering the UV texture maps of available clothing models. Fig. 4 shows how to generate UV texture maps.

Now that we have a great number of UV texture maps, a new clothing model can be created by choosing an existing model, and replacing its UV texture map with one randomly sample from the pool of our downloaded or generated UV texture maps. Examples of generated clothing can be seen in Fig. 5, which shows how different UV maps can be used to texturize the same clothing model, and how the generated clothes and rendered images look differently. By utilizing these large numbers of UV texture maps, we obtain a series of different outfits, which can be further used to create different 3D characters.

![fig3](https://github.com/VideoObjectSearch/RandPerson/blob/master/img/texture.jpg)  

Unity3D (https://unity.com/) is a cross-platform game engine that can be used to create various 3D games. We obtain a set of customized environments, comprising streets, forest paths, highways and laboratories, among others, with bright light, dark light, blue light, etc. Fig. 6 shows some example scenarios used in this work.  We set up a network with multiple cameras for each scene, and run them simultaneously in the virtual environments, simulating real video surveillance. An example is shown in Fig. 7, where three cameras are mounted, represented in yellow, green, and red, respectively.

![fig5](https://github.com/VideoObjectSearch/RandPerson/blob/master/img/scenes.jpg)  

## Experimental Results

To validate the effectiveness of the RandPerson dataset, we apply a basic deep learning model for cross-dataset person re-identification. All experiments are implemented in PyTorch, using an adapted version of the Open-Source Person Re-Identification Library (open-reid). 

The experimental results are shown in the table below.


![fig6](https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table1.jpg)  

![fig7](https://github.com/VideoObjectSearch/RandPerson/blob/master/img/table2.jpg)  


## Citation
//BibTex of arXiv paper

