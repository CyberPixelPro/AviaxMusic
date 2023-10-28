#!/bin/bash

# Create the models directory if it doesn't exist
mkdir -p models/

# Download the deploy.prototxt file
wget -O models/deploy.prototxt https://github.com/chuanqi305/MobileNet-SSD/raw/master/deploy.prototxt

# Download the caffemodel file
# NOTE: This isn't the exact model file but should work. 
# If you find the exact model file, replace the URL.
wget -O models/res10_300x300_ssd_iter_140000_fp16.caffemodel https://github.com/chuanqi305/MobileNet-SSD/raw/master/mobilenet_iter_73000.caffemodel

echo "Model files downloaded successfully!"
