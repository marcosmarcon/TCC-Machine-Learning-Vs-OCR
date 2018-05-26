import os
import segmentation
from sklearn.externals import joblib
import time
import json

# load the model
current_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.join(current_dir, 'models/svc/svc.pkl')
model = joblib.load(model_dir)

classification_result = []
for each_character in segmentation.characters:
    # converts it to a 1D array
    each_character = each_character.reshape(1, -1);
    result = model.predict(each_character)
    classification_result.append(result)
    print(each_character)
    #print(result)	
print "classification_result"
print(classification_result)

plate_string = ''
for eachPredict in classification_result:
    plate_string += eachPredict[0]
print "plate_string"
print(plate_string)

# it's possible the characters are wrongly arranged
# since that's a possibility, the column_list will be
# used to sort the letters in the right order

column_list_copy = segmentation.column_list[:]
segmentation.column_list.sort()
rightplate_string = ''
for each in segmentation.column_list:
    rightplate_string += plate_string[column_list_copy.index(each)]
print "rightplate_string"
print(rightplate_string)

with open('file-name.json') as data_file:    
    	    old_data = json.load(data_file)

data = [{"placa": rightplate_string,"dia": time.strftime("%d/%m/%Y"),"hora": time.strftime("%H:%M:%S")}]
data = old_data + data
path = '/home/marcos/license-plate-recognition/lpr'
filePathNameWExt =  path + '/' + 'file-name' + '.json'
with open(filePathNameWExt, 'w') as fp:
     json.dump(data, fp)







