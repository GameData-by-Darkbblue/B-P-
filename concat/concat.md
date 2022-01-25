```bash
ffmpeg -f concat -i <some file> -c copy <output filename>

# 如果文件名有空格等 (-safe的位置有影响)
ffmpeg -f concat -safe 0 -i <some file> -c copy <output filename>
```

-i文件的内容  
```text
file 'filename0'
file 'filename1'
...
```
