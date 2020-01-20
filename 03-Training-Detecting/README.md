# TRAIN

We need images and labels together store in eg. Data/Images/ForTraining folder 

We need create mycfg.cfg file. This file is oryginally copied from yolov3.cfg, we need to adapt this configuration to the needs of our model and our classes.

Copy yolov3.cfg

```
cp ultralytics/cfg/yolov3.cfg myproject/mycfg.cfg
```

Changes inside mycfg.cfg 

- Line 3: set `batch=24`, this means we will be using 24 images for every training step
- Line 4: set `subdivisions=8`, the batch will be divided by 8 to decrease GPU VRAM requirements.
- Line 603: set `filters=(classes + 5)*3` in our case `filters=21`
- Line 610: set `classes=2`, the number of categories we want to detect
- Line 689: set `filters=(classes + 5)*3` in our case `filters=21`
- Line 696: set `classes=2`, the number of categories we want to detect
- Line 776: set `filters=(classes + 5)*3` in our case `filters=21`
- Line 783: set `classes=2`, the number of categories we want to detect

Create list of images (if extension is jpg, and luched from this directory)

```
find ../Data/Images/ForTraining -name "*.jpg" > myproject/listimages.txt
```

Changes in mydata.data (for 2 classes, and names of classes stored in myproject/myimages.names)

```
classes=2 
train=myproject/listimages.txt
valid=myproject/listimages.txt
names=myproject/myimages.names
backup=myproject/backup
```

To start train from darknet53.conv.74, you can download it using wget

```
wget https://pjreddie.com/media/files/darknet53.conv.74
```

and after lunch command

```
python3 ultralytics/train.py --data myproject/mydata.data --cfg myproject/mycfg.cfg --weights darknet53.conv.74 --accumulate 1 --batch-size 12 --name myname01
```

Nvidia monitor
```
watch nvidia-smi
```

# DETECT