# video2img

Convert a video to images and timestamp

The output format matches the format of *kitti* dataset.

## Requirements

Python3

## Usage

```bash
$ python3 convert.py [video path] [output path]
```

## Example

```bash
$ python3 convert.py sample.mp4 out
```

```bash
$ tree out
out
├── images
│   ├── 000000.png
│   ├── 000001.png
│   ├── 000002.png
...
│   └── 000738.png
└── timestamp.txt
```

## Notes

The total size of output images is much larger than the size of the input video file. Make sure there is enough space to store the converted images. 
(5MB video -> 750MB of images)
