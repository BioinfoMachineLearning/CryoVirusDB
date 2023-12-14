# CryoVirusDB: An Expert Labelled Cryo-EM Image Dataset for AI-Driven Virus Particle recognition and Extraction
CryoVirusDB is a dataset of labeled virus particles in cryo-EM micrographs (images) for training and testing machine learning methods of virus particle picking. This repository contains scripts used to crawl, download, process, annotate, and post procress the CryoVirusDB dataset.

![Picture1](https://github.com/BioinfoMachineLearning/CryoVirusDB/assets/24986485/4def3167-c8c9-4a46-ab94-b6a57146c078)


## Data Download and Extraction in one of the three ways

## Option 1: Direct download all data from our server

Path to CryoVirusDB Dataset: https://calla.rnet.missouri.edu/CryoVirusDB/

Each EMPIAR ID in CryoVirusDB is available as a compressed file (tar.gz) that can be downloaded by simply clicking on the file. Once you have downloaded the file, you must extract its contents. If you are using a Windows operating system, you can use tools such as WinRAR or 7zip to extract the file. \
OR \
To download and extract dataset (ex: 11060), use command: \
`wget https://calla.rnet.missouri.edu/CryoVirusDB/11060.tar.gz` \
`tar -zxvf 11060.tar.gz -C` 


## Option 2: Use scripts to download all the cryo-EM micrographs from EMPIAR and virus particles coordinates from Zenodo
`git clone https://github.com/BioinfoMachineLearning/CryoVirusDB.git` \
`cd download_micrographs` \
`python download_micrographs_from_EMPIAR.py` 

These commands will enable you to download all the motion corrected micrographs from EMPIAR. Next, you should retrieve the virus particle labels from Zenodo by accessing this link: https://zenodo.org/record/TODO


## Option 3: Download a light version of the data: CryoVirusDB_Lite, if space constraints
If storage space is a concern, researchers can opt for a more lightweight version of CryoVirusDB called CryoVirusDB_Lite.  
CryoVirusDB_Lite includes truncated versions of the original micrographs and particle ground truth files that result in a total storage size of TODO GB, making it easier to store and transfer. This version includes an 8-bit representation of micrographs in JPG format, along with the necessary particle coordinate files for 9 Cryo-EM virus datasets.

Path to CryoVirusDB_Lite Dataset: https://calla.rnet.missouri.edu/CryoVirusDB_Lite/ \
The steps to download and extract the data files are identical to the instructions provided in option 1.


## CryoVirusDB Dataset Directory Structure:

![Picture5](https://github.com/BioinfoMachineLearning/CryoVirusDB/assets/24986485/b0b24c85-476d-43dd-b4e6-d77685f058fe)


CryoVirusDB is an expert-labeled dataset containing coordinates of accurately selected virus particles in cryo-EM micrographs. CryoVirusDB comprises 9,941 micrographs featuring 9 different viruses along with the coordinates of 0.2 Million virus particles in total. We anticipate that CryoVirusDB will enhance the capabilities of deep learning in accurately identifying virus particles in cryo-EM micrographs, thereby facilitating the subsequent 2D-3D reconstruction process. 


## Data Records


Each data folder (titled after the corresponding EMPIAR dataset ID) for all expert labelled data includes the following: motion corrected micrographs, ground truth, and particles stack. 


## CryoVirusDB Statistics
Statistics of true virus particles for each EMPIAR database in CryoVirusDB: 

| **SN** | **EMPAIR ID** | **Virus Type**                      | **Number of<br>Micrographs** | **Micrograph size** | **Particle<br>Diameter (px)** | **Number of True<br>Virus Particles** |
| ------ | ------------- | ----------------------------------- | ---------------------------- | ------------------- | ----------------------------- | ------------------------------------- |
| 1      | 10192         | Feline calicivirus                  | 1000                         | (4096, 4096)        | 470                           | 9660                                  |
| 2      | 11060         | Nudaurelia capensis omega virus     | 1276                         | (4096, 4096)        | 516                           | 11916                                 |
| 3      | 10203         | Macrobrachium rosenbergii nodavirus | 1000                         | (3838, 3710)        | 377                           | 16601                                 |
| 4      | 10033         | Human parechovirus 3                | 1000                         | (4096, 4096)        | 350                           | 55732                                 |
| 5      | 10652         | Coxsackievirus                      | 1127                         | (3838, 3710)        | 374                           | 11144                                 |
| 6      | 10341         | Bovine enterovirus                  | 1274                         | (4096, 4096)        | 376                           | 22694                                 |
| 7      | 10193         | Feline calicivirus                  | 1000                         | (4096, 4096)        | 516                           | 4103                                  |
| 8      | 10205         | Cowpea mosaic virus                 | 1000                         | (4096, 4096)        | 310                           | 55471                                 |
| 9      | 10555         | Nudaurelia capensis omega virus     | 1264                         | (4096, 4096)        | 564                           | 34488                                 |
|        |               | **Total**                           | **9941**                     |                     |                               | **221809**                            |

## Data Usage for ML-Based Applications:

Researchers can use CryoVirusDB to train and test their Machine Learning / Deep Learning based methods for automated cryo-EM virus particle picking. 

Users are supposed to use motion corrected 2D images (micrographs) as input. The virus particle's coordinate information for corresponding micrographs are located inside 'ground_truth' >>
'particle_coordinates' folder. The file naming convention for both the micrographs and their corresponding particle's coordinate are same for user's ease. 

### Example: 
For EMPIAR 11060, the motion corrected micrograph is: 11060>>micrographs>>micrograph1.mrc 
and the corresponding particle's coordinate information is found here: 11060>>ground_truth>>particle_coordinates>>micrograph1.csv

The particle stack is: 11060>>particles_stack>>micrograph1.mrc 
and the corresponding star file for all virus particles in EMPIAR 11060 is store as .star file in: 11060>>ground_truth>>empiar-micrograph1.star 


-----

## Rights and Permissions
Open Access \
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.


** Link to CryoVirusDB paper ** : TO Update once deposited in bioRxiv

## Cite this work
If you use the code or data associated with this research work or otherwise find this data useful, please cite: \
TOUPDATE
}
