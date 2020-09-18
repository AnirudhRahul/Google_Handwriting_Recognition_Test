import glob
import json


for fname in glob.glob('./json_output/*json'):
    output = json.load(open(fname,'r'))
    output_file = fname[:fname.rindex('.')]+'.txt'
    # print(output['responses']['textAnnotations']['description'])
    print(output['responses'][0]['textAnnotations'][0]['description'])
    with open(output_file, 'w') as f:
        f.write(output['responses'][0]
        ['textAnnotations'][0]
        ['description'])
