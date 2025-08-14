File description:
1. HomeCreditDefault.ipynb: main model
2. scaler.pkl, model.pkl: pkl files of model and scaler
3. app.py: main app file
4. training dataset.xlsx: training dataset
5. link&steps_to_follow.docx: links to datset, github and website
6. requirements.txt: file needed to declare xgboost in streamlit env and remove modulenotfounderror.


Steps to follow:
In order to use the website, the input has to be provided in a comma delimited fashion, this is done as there are almost 70 fields that will need to be filled and this would make the process of input easier for underwriters using the app, Some examples are given below, kindly select one and paste them to the text box:

Option 1:
Cash loans,M,N,Y,0,99000,222768,17370,180000,Unaccompanied,Working,Secondary / secondary special,Married,House / apartment,0.035792,-18064,-4469,-9118,-1623,1,1,0,1,0,0,Low-skill Laborers,2,2,2,FRIDAY,9,0,0,0,0,0,0,0.291655532,0.432961667,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3

Option 2:
Revolving loans,M,N,Y,0,180000,157500,7875,157500,Spouse, partner,Working,Secondary / secondary special,Civil marriage,House / apartment,0.031329,-12091,-1830,-1042,-4221,1,1,0,0,0,0,Laborers,2,2,2,TUESDAY,9,0,0,0,1,1,0,0.485769931,0.579727423,0,0,0,0,-765,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0
Option 3:
Cash loans,F,Y,N,0,157500,869049,31342.5,733500,Family,Commercial associate,Higher education,Married,House / apartment,0.010147,-16462,-2757,-4150,-9,1,1,0,1,0,0,Sales staff,2,2,2,FRIDAY,10,0,0,0,0,0,0,0.644822718,0.698667555,0,0,0,0,-2358,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3

Option 4:
Cash loans,F,N,Y,0,202500,1907010,66415.5,1741500,Family,Working,Higher education,Married,House / apartment,0.019689,-21975,-1083,-12431,-4962,1,1,1,1,1,1,Core staff,2,2,2,WEDNESDAY,8,0,0,0,0,0,0,0.59426873,0.639707568,5,1,5,1,-1363,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4

Post adding this to the text box click “fill form” for the form to be automatically filled. And then proceed to “predict” to get the default probability.

***Description of each field is present in : HomeCredit_columns_description.csv
****Other input samples present in: Training dataset.xlsx [please use chatgpt to produce comma separated values

