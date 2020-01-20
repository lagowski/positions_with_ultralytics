# Retrain YOLOv3: PREPARE VIDEO

In order to train images we can tag them by extracting images from videos. For that we need to divide video into images. Here with help comes ffmpeg program

For recognition we may need the videos or some image sequences.

In my case, splitting video into frames saves me time and allows me to analyze recognition errors and then improve tagging.

So I treat the video I use [**ffmpeg**](https://www.ffmpeg.org/)

### Examples of use of ffmpeg - video to video

* Crop only fragment from video for analysis
```
ffmpeg -i in_video.mp4 -filter:v "crop=out_w:out_h:x:y" out_video.mp4
```

### More complex Example video to images 

- crop from video area rectangle 100x200px with right-upper corner in 950,110 
- get only 30sec video, starting from 00:00:10. 
- frequency 1 frame per sec. 
- result store in JPG files with quality 2 (of max 9) 
- name of output file will be "out" and four digits numbering
- without printing copyright notice, etc.
```
ffmpeg -ss 00:00:10 -t 00:00:30 \
    -i in_video.mp4 \
    -vf "fps=1, crop=170:270:950:110" \
    -q:v 2 out%04d.jpg \
    -hide_banner
```

