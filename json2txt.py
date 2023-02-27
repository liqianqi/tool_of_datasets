import os
import json
import numpy as np

def json2txt(path_json,path_txt):
    with open(path_json,'r') as path_json:
        jsonx=json.load(path_json)
        with open(path_txt,'w+') as ftxt:
            width = jsonx['imageWidth']
            height = jsonx['imageHeight']
            for shape in jsonx['shapes']:
                xy=np.array(shape['points'])
                label=str(shape['label']) + ' '
                strxy = ''
                for m,n in xy:
                    m = m/width
                    n = n/height
                    strxy+=str(m)+' '+str(n) + ' '
                strxy = strxy.rstrip()
                label = label + strxy
                # label.rstrip()
                ftxt.writelines(label+"\n")

current_path = os.getcwd()
dir_json = current_path + '/labels_json/'
dir_txt = current_path + '/labels_yolo/'
if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
list_json = os.listdir(dir_json)
for cnt,json_name in enumerate(list_json):
    print('cnt=%d,name=%s'%(cnt,json_name))
    path_json = dir_json + json_name
    path_txt = dir_txt + json_name.replace('.json','.txt')
    #print(path_json,path_txt)
    json2txt(path_json,path_txt)
