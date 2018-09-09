# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./test_images_output/solidWhiteCurve_final.jpg 

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

The pipeline consisted of 6 steps. The steps are described briefly below.
1. Images were converted to grayscale representation. The image was named as img_gray
2. The gray scale image is blurred using a gaussian distribution with a kernel size of 5. The resulting image is named as img_blur
3. Canny edge detection technique is applied to img_blur with a threshold value of 20 for low and 150 for high threshold. This image is termed as img_canny.
4. An approximate region where the lane lines are expected to be in a image is traced on the img_canny (canny edge image). This area is fine tuned till an image of good results are obtained. The resulting image is named as img_masked.
5. Hough transform is applied on this image (img_masked) to join convert the canny transformed image to hough space. This helps find line from canny edges. 
6. Upon finding the lines, this image is superimposed on the original image to obtain red colored pipeline on the true image.
These are the primary steps get the pipe line. But the pipeline is broken line and not the continous lines thatt we desire. Further changes are to be made to draw the full extend of the lane. This is made via draw_lines() function.

The function draw_lines() is modified in the following steps. This used to extrapolate the line segments that were detected to map out the full extend of the lane. The line segments are seperated by their respective slope to determine whether the lines are part of left lane or right lane. The right lane has negative slope and left lane has positive slope. We also know that due to perspective view, the line segment can not be zero. Thus the lines between the slope of -1 to 1 are ignored for effective working. The next step involves averaging the the position of the lines to get get two lines: left lane and right lane. These two lines are extrapolated to the top and bottom of the lane. The top and bottom positions are obtained by trial and error methods.

Upon verifying on all the test images, the technique is applied on the video which is the objective of the project. Video is after all a collection of images. VideoFileClip class is used to convert video file to images and each of the image is passed through the steps as mentioned before. Thus completed.


![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when the roads are curved. When the roads are curved then the lane lines will also get curved. This can cause the system to fail. This scenario was mentioned in the challenge section which I was unable to complete.

Another shortcoming could be the color of the lane marking. We assume the lane line to be of white of yellow color and we are not aware what color the lane markings will be. Also we expect the lane marking to be present uniformly through out the road which may not be the case always.

Also there will be distorted images and we have not accounted for that in our method.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to correct the distorted images obtained which may be techniques like distortin correction or avoiding images that are too corrupted. Also the extrapolation is done by assuming a fixed point for top and bottom and it is obtained from trial and error methods.

Canny edge dtection is a primitive technique and it can be replaced with an improved sobel edge detection technique. Also an improved technique like kernel based hough transform (KHT) can be used to get improved performance.
