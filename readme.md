# LabelImg

[Link to original project](https://github.com/tzutalin/labelImg)


## What's new in this fork?

1. Minor bug fix when the app crashes when hitting the "Duplicate" button
2. Added utility that exports labeled images and relevent data to the same file structure as in the VOC training sets

## Tell me more about the added utility

##### Purpose: 
Let's say you're following a tutorial such as [this one](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Object-Detection) and want an easy way to use your labeled images from this app to train a SSD. This utility structures the labeled images so that it can be parsed by code that's expecting images in in the VOC file structure

##### What's the VOC file structure
```
-main
|---Annotations
   |---a0.xml
   |---more.xml
|---JPegImages
   |---a0.jpg
   |---more.jpg
|---ImageSets
   |---Main
      |---test.xml
      |---trainval.txt
```

Annotations contains all the xml files produced by LabelImg, JPegImages contains all the source images, test.xml lists all the files used for testing, trainval.txt lists all the files used for training

##### How do I use the utility

1. Label your images using LabelImg
2. Important: this utility assumes you save the xml files in same directory as the images, with the same filename prefix
3. Note the folder you were using, let's say the path was /home/x/dogs
4. Edit structvoc.py
..* Change 'path' to be the path from step 3
..* Set percent_training to equal the percent of images that you want to use for training (the rest for testing)
5. Run structvoc.py: "python structvoc.py"
	
