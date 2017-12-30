## Objective:  
Implement multinomial naïve Bayes (MNB) for text classification tasks  

------   
Languages used: Python 2.7.10  
source code name: mnb.py  
This program is tested in terminal from MacOS 10.12.3  

------  
How to compile and run code:  
 1. Open terminal and set the path to where the source code is located at   
 2. Enter command:  
 > python mnb.py  
 3. This program will ask user to   
   3.1 Enter location of training root folder:     
 > training/    
   3.2 Enter location of test root folder:    
 > test/   
------  
Analysis of results:  
Based on the result, we can see that each accuracy of the given classes is greater than 80%. Besides excluding header portions of each file, we eliminate words with length less than 4 characters when building the vocabulary. For instance, “a”, “the”, “for”, or “are” are not useful words. Excluding those words increased the accuracy.
