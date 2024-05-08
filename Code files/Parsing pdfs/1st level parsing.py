# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:58:54 2022

@author: HP
"""

import re
import os
import shutil
import csv

from glob import glob

from pdfminer.high_level import extract_text

os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\R11")

source_folder = r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\R11\\"
matched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\matched\\"
unmatched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\unmatched\\"

nutrients=['moisture','protein','ash','fat','dietary fibre','carbohydrate','energy']

food= ['lemon','butter', 'ghee', 'gourd', 'chicken', 'capsicum', 'grapes','mustard','oil', 'barley','flour', 'mint','pomegranate', 'garlic', 'cauliflower', 
 'beans', 'mangodi', 'orange', 'peas', 'mace', 'cardamom', 'lentils', 'urad','dal', 'peach', 'lettuce', 'ragi', 'chilli','egg', 'rice','semolina',
 'dates', 'wheat', 'khoya','jamun', 'lady fingers',  'soya', 'bean', 'mushroom', 'lotus', 'maize',  'pumpkin', 'gram', 'turmuric', 'spinach',
 'lamb', 'eggplants', 'moong', 'squid','palak', 'corn', 'avacado', 'bombay duck','chillies','radish', 'zucchini','horsegram',
 'papaya', 'sorghum', 'mint', 'basmati rice', 'avocado', 'pears', 'asafoetida', 'mango', 'brussels', 'rajma','potatoes', 'meat', 'brinjal',
 'tomato', 'figs', 'parsley', 'almond', 'millet','curry leaves', 'curd', 'tinda', 'fish', 'sesame','seeds','celery','bamboo', 
 'parwal','cabbage','fenugreek','ginger', 'jasmine', 'beetroot','moth', 'yolk','sunflower', 'coriander', 'onion', 'vermicelli', 'milk', 
 'custard apples', 'apples','jaggery', 'poppy', 'apricots', 'guava', 'pineapple', 'cashewnut', 'rajgira', 'groundnut', 'potato', 
 'parwar', 'hilsa', 'chana', 'drumstick', 'pistachios', 'amla', 'crab', 'masala', 'peach', 'currants', 'javantri', 'baby rawas',
 'jowar', 'amaranth', 'cauiliflower', 'nachni', 'banana', 'bathua', 'sweetcorn', 'raisins','cherry', 'milk', 'cucumber', 'watermelon', 'melon','seafood', 
 'pepper','pearl spot','microgreens', 'toddy', 'masala','burghul','peanut', 'betel','jackfruit', 'strawberry','prawn','almonds','cheese', 'mirch',
 'soyabean','carrot', 'sugar','garden cress','blackberry', 'cumin', 'knolkhol', 'prawns','nutmeg', 'basil', 'parsley', 'coconut', 
 'vinegar', 'colocasia', 'babycorn', 'tamarind','bajra', 'paneer', 'quinoa','clove','vanaspati', 'turmeric','bulghur','lime', 'sugarcane', 'pak choy', 
 'gooseberrie','beansprouts', 'riceflakes', 'jaiphal','muskmelon','lemongrass','plantains','peanut','walnut','cotton seed oil',
 'gingelly oil', 'groundnut oil', 'mustard oil','palm oil', 'rice bran oil', 'safflower oil', 'soyabean oil','sunflower oil', 'mustard seeds', 'curry leaves',
 'gingelly','moth bean','paneer','walnut','cashew','cauliflower','cowpea','nutmeg','country hen', 'lobster','ricebean','goat','sheep','beef',
 'calf','mithun','pork', 'rabbit','tuna','quinoa','sugarcane','eri meen','jathi vela meen', 'karimeen','myil meen', 'pomfret','salmon', 'sardine',
 'silver carp', 'tilapia', 'vanjaram','bulgur','octopus', 'catla', 'freshwater eel', 'gold fish','pangas', 'rohu']

fields= ["Id", "Nutrients", "Nutrients_count", "Foods", "Foods_count", "Keep"]

data= []

fileExt= r"*.pdf"
parsedfilecount=0
totalfilecount=0

for file in glob(fileExt):
    try:
        print("------"+str(file)+"-----")
        totalfilecount+=1
        text = extract_text(file)
        nutrientslist=[]
        nutrients_count=0
        foodslist=[]
        food_count=0
        keep="No"

        for j in range(0, len(nutrients)):
            if re.search(str(nutrients[j]),text):
                nutrients_count+=1
                nutrientslist.append(str(nutrients[j]))
                #print(nutrients[j]+ "---------Pattern Found")

        for j in range(0, len(food)):
            if re.search(str(food[j]),text):
                food_count+=1
                foodslist.append(str(food[j]))
                #print(food[j]+ "---------Pattern Found")

        if nutrients_count>0 and food_count>0:
            parsedfilecount+=1
            keep="Yes"
            source = source_folder + file
            destination = matched + file
            shutil.copy(source, destination)
            print('Copied Matched: ', str(file))

        else:
            source = source_folder + file
            destination = unmatched + file
            shutil.copy(source, destination)
            print('Copied Unmatched: ', str(file))

        entry = [str(file), nutrientslist, nutrients_count, foodslist, food_count, keep]

        data.append(entry)

        print("The nutrients keywords appeared for "+str(nutrients_count)+ " times") 
        print("The food keywords appeared for "+str(food_count)+ " times") 
        print("File Count: "+str(parsedfilecount))
        print("File Count: "+str(totalfilecount)+" \n \n")
    except:
        pass
    #print(repr(text))   
    
    
    
#print("Final File Count: "+str(filecount))
print(data)

os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet")

filename = "Level1.csv"

# writing to csv file 
with open(filename, 'a+') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    print("----csv file opened----")
        
    # writing the fields 
    #csvwriter.writerow(fields) 
        
    csvwriter.writerows(data)
    print("------csv data entered into file------")
    
#print(output_string.getvalue())