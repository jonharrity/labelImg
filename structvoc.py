import os
import subprocess
import random

#look for xml files and images in this path:
path = '/home/jon/benches'
#percent_training portion of the images will go towards training; the rest will be used for evaluation
percent_training = 0.75 
out = os.path.join(os.getcwd(), 'vocout')

path_trainid = os.path.join(out, 'ImageSets/Main/trainval.txt')
path_testid = os.path.join(out, 'ImageSets/Main/test.txt')
path_annotations = os.path.join(out, 'Annotations')
path_images = os.path.join(out, 'JPEGImages')

os.system(f'rm {path_annotations}/*')
os.system(f'rm {path_images}/*')

def cp(a, b):
	os.system(f'cp {a} {b}')

ids = []

os.chdir(path)
l = subprocess.getoutput('ls').split('\n')
for s in l:
	h = s.split('.')
	if h[1] == 'xml':
		cp(s, path_annotations)
		cp(f'{h[0]}.jpg', path_images)
		ids.append(h[0])

random.shuffle(ids)
mid = len(ids)*3//4
train_ids = ids[:mid]
test_ids = ids[mid:]

with open(path_trainid, 'w') as f:
	f.write('\n'.join(train_ids))
with open(path_testid, 'w') as f:
	f.write('\n'.join(test_ids))
	
