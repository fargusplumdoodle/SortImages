# SORT IMAGES
Isaac Thiessen July 2019

This is a script that goes recursively through each image in the source directory and takes all of 
the images that meet any of the parameters set in the config file. 

By default, any image with a width greater than 1400 and a height greater than 800 will be considered a wallpaper.

### Setup
1. Update config.yml (src = source directory, dest = dest directory)
2. Configure systemd unit file and run ./systemd/install.sh
3. wait for your all of your memes to be seperated from your wonderful wallpapers

### Config.yml
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