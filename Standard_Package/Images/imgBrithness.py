import pathlib
import numpy as np
from PIL import Image
import csv 

def main():
    curFolder = str(pathlib.Path(__file__).parent.resolve());
    
    with open(curFolder+'\\views.csv','r') as readFile, open(curFolder+'\\viewsW.csv','w', newline='') as writeFile:
        reader = csv.DictReader(readFile)
        #writer  = csv.DictWriter(writeFile,fieldnames=['id','title','jap_title'])
        #or use reader add new item to list
        writer  = csv.DictWriter(writeFile,fieldnames=reader.fieldnames)
        writer.writeheader()
        dic = {"id":1,"title":'sdf',"jap_title":'adsfsfd'}
        # for row in reader:
        #     id,title,jap_title = row.values() 
            
        
        writer.writerow(dic)
        #     id,title,jap_title = row.values() cls
        #     filename =curFolder +'\\' +id + '.bmp'

        #     brtness = round(cal_brightness(filename),2)
        #     # writer.writerow({
        #     #     'id':id,
        #     #     'title':title,
        #     #     'jap_title':jap_title,
        #     #     'birghness':brtness
        #     # },)
        #     #or  add new key the dicctionary from reader 
        #     row['birghness'] = brtness
        #     writer.writerow(row)        

def cal_brightness(filename):
    with Image.open(filename) as image:
        with Image.open(filename) as image:
            brightness = np.mean(np.array(image.convert('L'))) /255
    return brightness

main()