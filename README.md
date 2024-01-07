### Guide on how to configure the Raspberry Pi 400 with a Webcam

#### Materials Needed
- Raspberry Pi 400
- MicroSD card with Raspberry Pi OS
- Logitech C310 HD Webcam
- Internet connection (Mobile Hotspot)

#### Section 1: Setting Up Raspberry Pi 400
1. **Install Raspberry Pi OS**:
- Download the official Imager Software from the following link and install it: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Connect the microSD card into the PC
- Start the Imager software
- Choose the following options and click 'Next':
![imager](https://github.com/drfuzzi/INF2009_Setup/assets/108112390/9abdedc2-2693-44ff-9a48-0ac1dfd688ad)

- You will see the following when you click on "Edit Settings".
![imager2](https://github.com/drfuzzi/INF2009_Setup/assets/108112390/21ba2607-cd45-4406-830f-95732daf01ed)
![settings](https://github.com/drfuzzi/INF2009_Setup/assets/108112390/588dbd32-0d1b-41fe-9a00-d2b6607daa71)
   - Give a unique name for your RPi hostname.
   - Pick an appropriate username and password
   - Configure the WiFi to your hotspot (SIT WiFi doesnt work well with RPi)
   - Click on "Save"
   - Click on "Yes" and "Yes" again.

2. **Assembling Hardware**:
   - Connect the Raspberry Pi 400 to the monitor, keyboard, and mouse.
   - Insert the MicroSD card into the slot.

- Power on the Raspberry Pi.
- Connect to RPi 400 via SSH (e.g. use Putty).
- Enable the VNC via "sudo raspi-config". Now with the arrows select Interfacing Options, navigate to VNC, choose Yes, and select Ok .

#### Section 2: Configuring Raspberry Pi
1. **Connect to Wi-Fi**: 
   - Click on the Wi-Fi icon in the top right corner and connect to your network.

2. **Update the System**:
   - Open Terminal.
   - Update the system with the following commands:
     ```
     sudo apt update
     sudo apt upgrade
     ```

#### Section 3: Setting Up and Testing the Webcam
1. **Connecting the Webcam**:
   - Plug the webcam into a USB port on the Raspberry Pi.

2. **Install Webcam Software**:
   - Install 'fswebcam' for capturing images:
     ```
     sudo apt install fswebcam
     ```

3. **Testing the Webcam**:
   - Capture an image to test the webcam:
     ```
     fswebcam test.jpg
     ```
   - View the captured image using an image viewer.

#### Section 4: Configuring Sound
1. **Sound Output Configuration**:
   - Right-click on the sound icon on the top right.
   - Select your output device (HDMI or 3.5mm jack).

2. **Testing Sound**:
   - Test the sound output by playing a sound file or video.

#### Section 5: Capturing and Handling Images
1. **Capture Image with Webcam**:
   - Use `fswebcam` to capture an image:
     ```
     fswebcam -r 1280x720 --no-banner image.jpg
     ```

2. **View and Edit Images**:
   - Install an image editor like GIMP:
     ```
     sudo apt install gimp
     ```
   - Open the captured image in GIMP for editing.

#### Section 6: Recording and Playing Videos
1. **Recording Video**:
   - Install `ffmpeg` to record video from the webcam:
     ```
     sudo apt install ffmpeg
     ```
   - Record a video from the webcam:
     ```
     ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mp4
     ```

2. **Play Video**:
   - Install VLC media player:
     ```
     sudo apt install vlc
     ```
   - Play the recorded video using VLC:
     ```
     vlc output.mp4
     ```

#### Section 7: Advanced Applications (Optional)
- **Python Scripting for Webcam**:
   - Introduction to using Python for controlling the webcam.
- **Creating a Surveillance System**:
   - Setting up motion detection using the webcam.

#### Conclusion
- Recap of the tasks completed.

#### Troubleshooting
- No video feed: Check webcam connections and drivers.
- No sound: Verify sound output settings.

### Additional Resources
- Raspberry Pi Documentation: [Official Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- Python Programming for Raspberry Pi: [Python Programming on Raspberry Pi](https://www.raspberrypi.org/documentation/usage/python/)

This guide provides a comprehensive setup for beginners and can be expanded with more advanced topics based on the user's interest and proficiency.
