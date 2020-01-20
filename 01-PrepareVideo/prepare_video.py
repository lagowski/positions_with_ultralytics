#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import argparse
import ffmpeg
import sys


parser = argparse.ArgumentParser(description='Convert video in images ')
parser.add_argument('in_filename', help='Input video')
parser.add_argument('out_filename', help='Output base name')
parser.add_argument(
    '--fps', type=int, default=10, help='Frames per second')
parser.add_argument(
    '--time', type=int, default=0.1, help='Time offset')
parser.add_argument(
    '--crop', help='Crop Parameters - Mustbe 4 parameters: x,y,width,height')   


# parser.add_argument(
#     '--', type=int, default=120,
#     help='Width of output thumbnail (height automatically determined by aspect ratio)')


def generate_frames(in_filename, out_filename, time, fps, crop):
    if crop:
        try:
            x,y,width,height = crop.split(",")
            print(x,y,z,v)
            (
                ffmpeg
                .input(in_filename, ss=time)
                .filter('fps', fps=fps, round='up')
                .filter('crop', x, y, width, height)
                .output(out_filename+"_%04d.jpg")
                .run()
            )
        except ffmpeg.Error as e:
            print(e.stderr.decode(), file=sys.stderr)
            sys.exit(1)
    else:        
        try:
            (
                ffmpeg
                .input(in_filename, ss=time)
                .filter('fps', fps=fps, round='up')
                .output(out_filename+"_%04d.jpg")
                .run()
            )
        except ffmpeg.Error as e:
            print(e.stderr.decode(), file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    args = parser.parse_args()
    generate_frames(args.in_filename, args.out_filename, args.time, args.fps, args.crop)