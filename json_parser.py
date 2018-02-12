# Group Name: InsaneSprinters
# Group Members: Sri Santhosh Hari, Kunal Kotian, Devesh Maheshwari, Vinay Patlolla

import json
import sys
import os

def json_parser(prefix):
    '''
    prefix - prefix of the files to be parsed
    '''

    json_dir = '/srv/runme/'

    files = os.listdir(json_dir)
    output = list()
    for f in files:
        if f.startswith(prefix):
            try:
                fd = open(os.path.join(json_dir, f))
                for line in fd.readlines():
                    try:
                        d = json.loads(line)
                        name = str(d.get('name', ''))
                        age = int(d['prop'].get('age', ''))
                        if name != '' and age >=0 and (u'age' not in d.keys()) and (u'name' not in d['prop'].keys()):
                            output.append((name, age))
                    except:
                        pass
            except:
                pass

    output_file = os.path.join(json_dir, '{}.txt'.format(prefix))

    if os.path.exists(output_file):
        os.remove(output_file)

    #os.mknod(output_file)

    with open(output_file, 'w+') as f:
        for name, age in output:
            entry = name + '\t' + str(age) + '\n'
            f.write(entry)

    return None

# Read input argument and execute parser function
prefix = sys.argv[1]
json_parser(prefix)
