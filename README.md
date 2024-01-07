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

#### Section 2: Configuring Raspberry Pi
1. **Assembling Hardware**:
- Insert the MicroSD card, power adapter and USB Webcam into the Raspberry Pi 400.
- Power on the Raspberry Pi.
![20240107_182836](https://github.com/drfuzzi/INF2009_Setup/assets/108112390/9fd5dfa1-ddee-4cb5-a557-0e4283a513a7)

2. **Enabling VNC**:
- Connect to RPi 400 via SSH (e.g. use Putty).
- You can find the RPi400's IP via your mobile hotspot or router.
- Enable the VNC using the following command and selecting "Interfacing Options", navigate to "VNC", choose "Yes", select "Ok" and select "Finish".
  ```
  sudo raspi-config
  ```
![raspiconfig](https://github.com/drfuzzi/INF2009_Setup/assets/108112390/8ea119c9-8b27-48b8-80b2-4f32821ffd51)

3. **Setting Up a Static IP (Optional)**:
   - For easier connection, assign a static IP to your RPi 400.
   - Open Terminal and edit the `dhcpcd.conf` file:
     ```
     sudo nano /etc/dhcpcd.conf
     ```
   - Add the following lines at the end of the file (replace with your network details):
     ```
     interface eth0
     static ip_address=192.168.x.xxx/24
     static routers=192.168.x.x
     static domain_name_servers=192.168.x.x
     ```
   - Save and exit the editor (CTRL+X, then Y, then Enter).
   - Reboot the RPi 400.

4. **Installing VNC Viewer on Your Laptop**:
   - Download and install VNC Viewer on your laptop from the official [VNC Viewer website](https://www.realvnc.com/en/connect/download/viewer/).

5. **Connecting to the Raspberry Pi**:
   - Open VNC Viewer on your laptop.
   - Enter the IP address of your Raspberry Pi (same IP address as used with SSH) and press Enter.
   - When prompted, enter the Raspberry Pi's username and password.

6. **Using Raspberry Pi Desktop Remotely**:
   - Once connected, you should see the Raspberry Pi's desktop interface on your laptop.
   - You can now use the Raspberry Pi as if you were working directly on it.

7. **Update the RPi 400 System**:
   - Open Terminal.
   - Update the system with the following commands:
     ```
     sudo apt update
     sudo apt upgrade
     ```

#### Section 3: Setting Up and Testing the Webcam

1. **Connecting the Webcam**:
   - Plug the webcam into a USB port on the RPi 400.
   - The drivers for the webcam should be automatically installed.
     ```
     lsusb
     ```

2. **Install Software to capture image**:
   - Ensure that you have internet access.
   - Install 'fswebcam' for capturing images:
     ```
     sudo apt install fswebcam
     ```

3. **Capture Image with Webcam**:
   - Use `fswebcam` to capture an image:
     ```
     fswebcam -r 1280x720 --no-banner image.jpg
     ```

4. **View and Edit Images (Optional)**:
   - Install an image editor like GIMP:
     ```
     sudo apt install gimp
     ```
   - Open the captured image in GIMP for editing.

5. **Recording Video**:
   - Install `ffmpeg` to record video from the webcam:
     ```
     sudo apt install ffmpeg
     ```
   - Record a video from the webcam:
     ```
     ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mp4
     ```
   - this command tells ffmpeg to capture video from the first connected webcam at a resolution of 640x480 pixels and a frame rate of 25 fps, and save it to a file named output.mp4. In addition, "-f" specifies the format to be used while "v4l2" stands for Video4Linux2, which is the standard video driver model for Linux for video capture.

6. **Play Video (Optional)**:
   - Install VLC media player:
     ```
     sudo apt install vlc
     ```
   - Play the recorded video using VLC:
     ```
     vlc output.mp4
     ```

7. **Checking for Audio Device**:
   - First, check if your system has recognized the webcam's microphone.
   - Open Terminal and type the following command to list all audio input devices:
     ```
     arecord -l
     ```
   - Look for your webcam in the list. The following image shows what you might see.
![arecord](https://github.com/drfuzzi/INF2009_Setup/assets/108112390/ce795948-b92a-4486-a933-eab2fe27b0b5)

8. **Use the arecord Command**:
   - To test if the microphone is working, record a short audio clip:
     ```
     arecord -D plughw:<CardNumber>,<DeviceNumber> -d 10 test.wav
     ```
   - Replace `<CardNumber>` and `<DeviceNumber>` with the numbers you found in the previous step. The `-d 10` flag tells `arecord` to record for 10 seconds.
   - Based on the above screenshot, the USB audio device is listed as `card 2, device 0`, I specify these in the command.
   - To record a short audio clip, use the following command in the terminal:
     ```
     arecord -D plughw:2,0 -d 10 test.wav
     ```
   - Here's what each part of the command means:
     - `arecord`: This is the command to start recording audio.
     - `-D plughw:2,0`: The `-D` option specifies the audio device. `plughw:2,0` refers to `card 2, device 0`, which is your USB audio device.
     - `-d 10`: This option specifies the duration of the recording. `-d 10` means the recording will last for 10 seconds.
     - `test.wav`: This is the name of the file where the audio will be saved. It will be saved in the current directory.

9. **Playing the Recorded Audio**:
   - Play the recorded audio to check the quality:
     ```
     aplay test.wav
     ```
   - If you don’t hear anything, adjust the microphone levels using the sound settings or `alsamixer` in the terminal.

#### Section 4: Advanced Applications (Optional)

a. Setting up and using a Virtual Environment
Using a Python virtual environment allows you to manage Python packages independently of the system packages. This is a recommended approach to avoid conflicts between packages installed via `apt` and `pip`.

1. **Install Virtual Environment Package**:
   ```bash
   sudo apt install python3-venv
   ```

2. **Create a Virtual Environment**:
   Navigate to the directory where you want to create your virtual environment and run:
   ```bash
   python3 -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   ```bash
   source myenv/bin/activate
   ```

4. **Install Packages Using pip**:
   Now you can install packages using pip without encountering the `externally-managed-environment` error:
   ```bash
   pip install opencv-python
   ```

5. **Upgrade pip**:
   Ensure you are using the latest version of pip:
   ```bash
   pip install --upgrade pip
   ```
Remember, after using the virtual environment, you can deactivate it by simply running `deactivate` in your terminal. Using virtual environments is a good practice as it keeps your global Python environment clean and prevents version conflicts between different Python projects.

b. **Python Scripting for Webcam**:
   - Introduction to using Python for controlling the webcam.
   - [Here](adv/capimg.py) is a simple script to capture a single video frame from the webcam and save it.

c. **Creating a Surveillance System**:
   - Setting up motion detection using the webcam.
   - [Here](adv/capvid.py) is another simple script to stream a video from the webcam and notify on screen if you detect motion using simple algorithm.

### Additional Resources
- Raspberry Pi Documentation: [Official Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- Python Programming for Raspberry Pi: [Python Programming on Raspberry Pi](https://www.raspberrypi.org/documentation/usage/python/)
