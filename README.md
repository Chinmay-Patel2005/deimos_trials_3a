# deimos_trials_3a
aruco marker detection

replace "path_to_your_video.mp4" with actual video path

first we take the video from path and check if it exists.

if it does then we look at the video frame by frame until q is pressed on the keyboard.

we change the format of the video from rgb to greyscale for better detection.

then we detect and draw frames over the detected aruco markers using opencv aruco library.

then we display the changed frames using imshow
