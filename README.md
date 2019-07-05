# SORT IMAGES
Isaac Thiessen July 2019

This is a script that goes recursively through each image in the source directory and takes all of 
the images that meet any of the parameters set in the config file. 

By default, any image with a width greater than 1400 and a height greater than 800 will be considered a wallpaper. 
For more information read the config section.

Sort Images ensures that no duplicate images are added to the destination through the use of MD5 sums on each image.

I wrote this in a morning so let me know if you find any mistakes.
### Setup
1. Update config.yml (src = source directory, dest = dest directory)
2. Configure systemd unit file and run ./systemd/install.sh
3. wait for your all of your memes to be seperated from your wonderful wallpapers

### Config
Recommended config, only change src and dest
```yaml
src: /home/fargus/Pictures/
dest: /tmp/SortWallpaper/
exclude:
  - excludeme
verbose: true
params:
  Desktop:
    min_width: 1400
    min_height: 800
    min_ratio: 1.3
    max_ratio: 1.9
  Phone:
    min_width: 720
    min_height: 1500
    min_ratio: 0.36
    max_ratio: 0.76
filetypes:
  - png
  - jpg
  - JPG
  - JPEG
  - PNG
```
### Config explanation

**src**: source directory

**dest**: destination directory, created if it doesn't exist. Each profile will be a subdirectory of the destination directory.

**exclude**: a list of directories you dont want to include from the source directory

**verbose**: boolean, if the program will produce a lot of output

**params**: a list of objects for each set of parameters on images. I recommend having a desktop one and a phone one based on your screen size

**min_width**, **min_height**: screen size in pixels

**min_ratio**, **max_ratio**: if greater than 1, it is a landscape oriented picture. ratio is calculated from height/width
 
**filetypes**: list of file types that will be considered images, probably dont change.
