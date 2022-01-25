'''
用于生成 ffmpeg 拼接视频所需指引文件
专用于我习惯的视频格式，每个视频一个单独目录，目录名称和视频名称相同，视频格式为.mp4
把本文件复制到视频工程的父目录下面运行，然后手动删除生成文件中不属于视频文件的部分
'''

import os
import glob

paths = glob.glob('*')

with open('concat.txt', 'w') as f:
	for path in paths:
		f.write('file ' + "'" + os.path.join(path, path+'.mp4') + "'")
		f.write('\n')
