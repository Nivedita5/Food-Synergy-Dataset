import nltk
from nltk.corpus import wordnet

import pandas as pd
import os
import re
import csv

os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet")

source_folder = r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\Matched\\Matched\\"
matched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\Matched\\Matched\\Extracted\\"
unmatched= r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet\\Research\\Matched\\Matched\\Unmatched\\"

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

enhance = []
inhibit = []
  
for syn in wordnet.synsets("enhance"):
    for l in syn.lemmas():
        enhance.append(l.name())
        
for syn in wordnet.synsets("inhibit"):
    for l in syn.lemmas():
        inhibit.append(l.name())

dataset= pd.read_csv("Level3.csv")
Ids= dataset['Id']
Text= dataset['Text']

data= []

count=0
i=0
for id in Ids:
    try:
        nutrientlist=[]
        foodlist=[]
        enhancelist=[]
        inhibitlist=[]

        print(i)
        print(id)
        text= Text[i]

        for k in range(0, len(nutrients)):
            if re.search(r"\b"+str(nutrients[k])+r"\b", text):
                nutrientlist.append(str(nutrients[k])) 
                #print(str(nutrients[k])+" nut appended")
        
        for k in range(0, len(food)):
            if re.search(r"\b"+str(food[k])+r"\b", text):
                foodlist.append(str(food[k]))
                #print(str(food[k])+" food appended")

        for k in range(0, len(enhance)):
            if re.search(str(enhance[k]), text):
                enhancelist.append(str(enhance[k]))

        for k in range(0, len(inhibit)):
            if re.search(str(inhibit[k]), text):
                inhibitlist.append(str(inhibit[k]))

        nutrientlist= set(nutrientlist)
        foodlist= set(foodlist)
        enhancelist= set(enhancelist)
        inhibitlist= set(inhibitlist)
        
        #print(nutrientlist)
        #print(foodlist)
        #print(enhancelist)
        #print(inhibitlist)

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
            entry= [id, text, nutrientlist, foodlist, enhancelist, inhibitlist]
            data.append(entry)
            #print(entry)
            count+=1
            source = source_folder + id
            destination = matched + id
            shutil.copy(source, destination)
        elif foodlen>=1 and nutrientlen>=1 and (enhancelen>=1 or inhibitlen>=1):
            entry= [id, text, nutrientlist, foodlist, enhancelist, inhibitlist]
            data.append(entry)
            #print(entry)
            count+=1
            source = source_folder + id
            destination = matched + id
            shutil.copy(source, destination)
        else:
            source = source_folder + id            
            destination = unmatched + id
            shutil.copy(source, destination)
    except:
        pass
    i+=1
    
print("count: "+ str(count))
#print(data)


os.chdir(r"F:\\IIT RPR\\Research Projects\\Building Food Synergy DataSet")

filename = "Level5.csv"

fields= ["Id", "Text", "Nutrients", "Foods", "Enhance", "Inhibit"]

try: 
    with open(filename, 'w+', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(data)
        print("------csv data entered into file------")
except:
    pass
    

    