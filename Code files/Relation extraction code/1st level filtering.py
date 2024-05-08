import os
import csv
import re
import shutil
import pandas as pd

from pdfminer.high_level import extract_text
from glob import glob

os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet")

#csvdata= pd.read_csv("test.csv")
csvdata= pd.read_csv("Level1_Keep.csv")
Ids= csvdata.Id
Foods= csvdata.Foods
Nutrients= csvdata.Nutrients
Foods_count= csvdata.Foods_count
Nutrients_count= csvdata.Nutrients_count

import nltk
from nltk.corpus import wordnet

enhance = []
inhibit = []
  
for syn in wordnet.synsets("enhance"):
    for l in syn.lemmas():
        enhance.append(l.name())
        
for syn in wordnet.synsets("inhibit"):
    for l in syn.lemmas():
        inhibit.append(l.name())

os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\R\\R")
#os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\Matched\\R1")

source_folder = r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\R\\R\\"
matched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\R\\R\\Matched\\"
unmatched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\R\\R\\Unmatched\\"

#source_folder = r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\Matched\\R1\\"
#matched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\Matched\\Matched\\"
#unmatched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\Matched\\Unmatched\\"

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

data= []

fileExt= r"*.pdf"
count=0
filecount=0
for id in glob(fileExt):
    filecount+=1
    print("------------"+id+"-------------")
    print(filecount)
    try:
        text= extract_text(id)
        text= text.replace("\n", "")
        text= re.sub("\(.*?\)","",text)
        text= text.encode("ascii", "ignore")
        text= str(text.decode())
        lines= text.split(".")
        last= len(lines)-5
        i=0
        while i<last:
            start=i
            end=i+5
            textlines=""
            enhancelist=[]
            inhibitlist=[]
            foodlist=[]
            nutrientlist=[]

            for j in range(start, end):
                textlines += str(lines[j])
            #print(textlines)
        
            for k in range(0, len(nutrients)):
                #print(nutrients[k])
                if re.search(str(nutrients[k]), textlines):
                    #print(nutrients[k])
                    nutrientlist.append(str(nutrients[k]))
                    #print("Nutrients added")
            
            for k in range(0, len(food)):
                if re.search(str(food[k]), textlines):
                    foodlist.append(str(food[k]))
            
            for k in range(0, len(enhance)):
                if re.search(str(enhance[k]), textlines):
                    enhancelist.append(str(enhance[k]))
                    
            for k in range(0, len(inhibit)):
                if re.search(str(inhibit[k]), textlines):
                    inhibitlist.append(str(inhibit[k]))
            
            nutrientlist= set(nutrientlist)
            foodlist= set(foodlist)
            enhancelist= set(enhancelist)
            inhibitlist= set(inhibitlist)
            
            foodlen=len(foodlist)
            if foodlen==0:
                foodlist.add("")
            nutrientlen=len(nutrientlist)
            if nutrientlen==0:
                nutrientlist.add("")
            enhancelen=len(enhancelist)
            if enhancelen==0:
                enhancelist.add("")
            inhibitlen=len(inhibitlist)
            if inhibitlen==0:
                inhibitlist.add("")
                
            if foodlen>1 and (enhancelen>=1 or inhibitlen>=1):
                count+=1
                entry= [id, textlines, nutrientlist, foodlist, enhancelist, inhibitlist]
                print("********food entry********")
                print(entry)
                data.append(entry)
                source = source_folder + id
                destination = matched + id
                shutil.copy(source, destination)
                i+=5                
            elif foodlen>=1 and nutrientlen>=1 and (enhancelen>=1 or inhibitlen>=1):
                count+=1
                entry= [id, textlines, nutrientlist, foodlist, enhancelist, inhibitlist]
                print("************food and nutrient entry*******")
                print(entry)
                data.append(entry)
                source = source_folder + id
                destination = matched + id
                shutil.copy(source, destination)
                i+=5   
            else:
                source = source_folder + id
                destination = unmatched + id
                shutil.copy(source, destination)
                #print('Copied Unmatched: ', str(id))
                i+=1
    except:
        pass

print("Total entries: "+ str(count))
#print(data)

os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet")

filename = "test2.csv"

fields= ["Id", "Text", "Nutrients", "Foods", "Enhance", "Inhibit"]
# writing to csv file 
with open(filename, 'a+', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    print("----csv file opened----")
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    csvwriter.writerows(data)
    print("------csv data entered into file------")
    
 