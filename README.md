# lc-lq-automation

Read steps below under COSC_432_BERT_Classifier to set up environment. Largely based on code by Ryan Kraft.

Current implementation trains AI to classify an excerpt of RE text for language quality; limited to only classifying redundancy (RDC) and ambiguities (AMB). 

A better dataset could enable more accurate and granular classification. Currently training with a dataset generated from chatGPT.

# COSC_432_BERT_Classifier
**Step 1: Installing Miniconda**    
Miniconda is a package handeler that allows you to create a mini virtual enviornmant to run applications in and can be helpful for keeping project dependencies separate from your physical device and ensure that you will not ruin other projects that you have by downloading an out-dated dependency.    
https://www.youtube.com/watch?v=P6eGTN9QN2Q    
this video is a helpful guide to follow to get started with Miniconda. Once you have created a conda enviormnet like how the video shows, you can move on to the next step.   

**Step 2: Installing python and pip**    
You will need to have Python and pip installed on your device in order to get the python packages required to run the program. pip is the package manager for python. If you have ever used Javascript and used npm this should be a familiar concept for you.    
https://www.python.org/downloads/      
Use this link to get python on your device.    
https://pip.pypa.io/en/stable/installation/    
This is a short guide you can follow for installing pip on your device.        
https://www.youtube.com/watch?v=fJKdIf11GcI    
This video is a helpful guide for installing pip on windows.    

**Step 3: downloading dependencies**    
once you have pip installed and you have entered your conda enviornment you can begin downloading the dependencies required for the program.   
![image](https://github.com/Ryan4412/COSC_432_BERT_Classifier/assets/103439799/439b2a09-e5e2-417c-a566-853999680bd8)      
the following is a list of commands you can paste into your terminal to download all dependencies required:   
  
pip3 install torch     
pip install pandas    
pip install transformers   
pip install numpy   
pip install scikit-learn    
pip install ipykernel     
pip install matplotlib     
pip install tqdm    

**Step 4: Installing extentions on vscode**
there are a few extentions you will need to have downloaded on vscode in order to use Jupyter Notebook files.     
  - Jupyter         
    ![image](https://github.com/Ryan4412/COSC_432_BERT_Classifier/assets/103439799/ade6fe1f-5e84-46f4-b4d0-c95fb3916889)        
  - Jupyter Keymap          
    ![image](https://github.com/Ryan4412/COSC_432_BERT_Classifier/assets/103439799/a971833e-c0f3-41bf-a837-988b8d42c79a)        
  - Jupyter Cell Tags      
    ![image](https://github.com/Ryan4412/COSC_432_BERT_Classifier/assets/103439799/8ae978a5-d389-4f69-87ac-6ba4286fb8da)      
  - Jupyter Notebook Renderers          
    ![image](https://github.com/Ryan4412/COSC_432_BERT_Classifier/assets/103439799/5e66eae5-6cce-4d9a-8ca7-41464e2d5460)      
  - Jupyter Slide Show      
    ![image](https://github.com/Ryan4412/COSC_432_BERT_Classifier/assets/103439799/c80f1227-56c4-439f-beac-182ece354029)          
             
**Step 5: Selecting kernel on vscode**     
Once you have all dependencies installed, the last step is to select the kernel you would like to use to run the program. Open COSC_432_BERT_Classifier.ipynb file in vscode and in the top right you will see the select kernel button.     
![image](https://github.com/Ryan4412/COSC_432_BERT_Classifier/assets/103439799/6e3ce1ad-0471-4899-8b1d-bc965b8b6e18)     
Click on it and select "Python Enviornments..." in the dropdown and then select the conda enviornment you just created. once it loads you will be ready to run the code.
