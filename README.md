WRO-2022-Future-Engineer
===========================

In this repository you can see all our documentation files: programs, robot photo, team photo, robot presentation video.  

Description of files
---------------------------
Our robot is controlled by the following programs:  
**main.py** is the program that is loaded into PyBoard. This program receives data from the **Raspberry** and controls the servo and motor.  
**qualification.py** (for qualification) or **Final.py** (for final) - these programs are loaded on Raspberry. These programs contain the driving algorithm itself, and also these programs read the readings from the camera and process them. These programs also send other data to PyBoard.  
**RobotAPI.py** is the library that **Raspberry** uses to read the image from the camera.  
**start_robot.py** is an application for connecting a **Raspberry**, displaying an image from a camera, and launching programs.  
**autosatrt.py** is a program that starts automatically after turning on the **Raspberry**. It loads **qualification.py** or **Final.py**.  

main.py
---------------------------
**main.py** - this program on **PyBoard** waits for the message "9999999" from Raspberry that the system has booted and the buzzer is triggered. After that, she is ready to start. It waits for subsequent messages from **Raspberry** in which the speed of the motor and the angle of rotation of the servo are already transmitted, and after decrypting the message, it transmits the data to the motor and servo.

qualification.py
---------------------------
**qualification.py** is a **Raspberry** program. After starting the **Raspberry**, it sends the message “9999999” to the **PyBoard**, which means that the **Raspberry** has started and is ready to work, after which the data from the camera is read and displayed. There are two sensors on the sides of the display that determine the black color, in order to ride along the walls to the left and to the right, as the robot rides on one sensor, there is also an HSV sensor in the center that reads blue and orange lines.  
The program works according to the following algorithm:
First, the robot is in state 0 in which it centers the position of the servo and waits for a button to be pressed.  
After the button has been pressed, the robot goes to state 2 (goes to state 2 immediately, since state 1 is in manual control) in which the robot travels along two sensors using the PD controller until the first intersection.  
After the robot reaches the first line, the program remembers what this line was and goes to state 3. In state 3, the program checks which line was seen first, if blue then the robot turns left and if orange then right, this is done so that the robot reads only one line.  
After turning, the robot goes to state 4. In state 4, the robot also uses the data that was collected in state 2, namely what color the line was and based on this determines which sensor to go if blue is on the right if orange is on the left and it goes until he sees the line and then goes back to state 3 and the algorithm repeats.  
After the robot has passed 12 lines, this means that it has passed 12 turns, that is, 3 laps, and the program ends with a speed reset to zero.

Final.py
---------------------------
**Final.py** is a similar program with the same algorithm, only one more HSV sensor is added above the color detection sensor that reads red and green, since the barrels that the robot must go around are painted in it. In state 4, a condition is added if he notices a green barrel, then the robot turns left, and if red, then right. Also in this program, the speed for high-speed passage has been increased.

autostart.py
---------------------------
**autostart.py** as described above is a program that automatically starts when the robot is turned on. In order to load a launch program into **autostart.py**, for example, **qualification.py,** you need to:  
* Open the **autostart.py** file.
* Find the **import** line.


![Безымянный](https://user-images.githubusercontent.com/99865132/168015534-51dd1125-0522-4c75-b545-280dd4f46cd3.png)
* Enter the name of the file that should start automatically in this line.


Software installation
===========================
Our robot is programmed with **PyCharm** and uses the **Python** language. Here are instructions on how to install all the necessary software and open the repository.
1. **Installing PyCharm.**
	* Go to the official **Pycharm** website.
	![12й](https://user-images.githubusercontent.com/99865132/168006290-20d750a5-c94d-40dd-bf8e-92b863529f8f.png)
	* Next, select the Windows operating system.
	* Click the **download** button.
	* Next, the installation file will be downloaded.


	![13й](https://user-images.githubusercontent.com/99865132/168006320-a603946c-1eb0-498d-ba2a-ac392610b678.png)
	* After installation, open and run the file.
	* Next, select the options you need.
2. **Installing Python version 3.9.**
	* Go to the official **Python** website.
	![14й](https://user-images.githubusercontent.com/99865132/168006348-5e8710ac-00d2-4672-b926-e78335f867d2.png)
	* Click on the **download** button.


	![15й](https://user-images.githubusercontent.com/99865132/168006375-5048e824-c618-4d20-9937-26fa530af35a.png)
	* Scroll down, you will see a list of versions available for download, select **Python 3.9.**
	![16й](https://user-images.githubusercontent.com/99865132/168006407-58c166cb-3fab-46ab-8094-a12b762814be.png)
	* You will see a page for this version, scroll down and select the version for the 64-bit operating system.
	![17й](https://user-images.githubusercontent.com/99865132/168006434-e10061fc-f4fb-4eb0-85af-29714b226280.png)
	* The next step is to install the language file.
	* Once it is installed, launch it, select the options you want, and download the language.
	* Then we go into **PyCharm**, in the upper left corner there will be a **“File”** button.
	![18й](https://user-images.githubusercontent.com/99865132/168006479-0790610f-7114-4a1f-acc5-18fc41d6f2a8.png)
	* Then click on the **"Settings"** button.
	![19й](https://user-images.githubusercontent.com/99865132/168006522-b4163917-95d2-43b4-b8ac-4bbaf6a99552.png)
	* Then go to this section and select **Python 3.9.  **
	![20й](https://user-images.githubusercontent.com/99865132/168006543-17a017f4-9ad0-4116-b779-d18bc5f393ee.png)
	
3. **Installing a folder with a project from the Github repository.**
	* To get started, go to the main page of the repository.
	![21й](https://user-images.githubusercontent.com/99865132/168006584-5026761c-1cf1-4511-8c8e-3ddd3e328ff6.png)
	* Then click on the green **"Code"** button, then download the zip file.


	![22й](https://user-images.githubusercontent.com/99865132/168006608-5b2d6d7d-693d-419d-9645-345967b915c1.png)
	* The download of the project archive should begin.
	* Then unzip the file to a regular folder.
	![image](https://user-images.githubusercontent.com/99865132/168013974-a79810f4-d60a-42de-adf3-19209c9b8721.png)


Connecting to PyBoard
---------------------------
To connect to **PyBoard**, you need a microUSB cable, one end must be connected to **PyBoard**, and the other end to the computer, after which **PyBoard** will open as a USB flash drive and all that remains is to transfer the **main.py** file. Then you should wait until the red LED goes out and press the reset button on the board.
![WhatsApp Image 2022-05-13 at 23 50 18](https://user-images.githubusercontent.com/99865132/168299298-baf9ed55-fe87-40b9-a90d-a7972201fe51.jpeg)
![WhatsApp Image 2022-05-13 at 23 55 37](https://user-images.githubusercontent.com/99865132/168299321-8f6fc2ff-f034-4eca-b796-0df86876b882.jpeg)


Starting the robot
---------------------------
* Insert the batteries into the battery compartment of the robot. Do not confuse + and - batteries to avoid consequences.
* Press the big red power button.
* After the power is supplied, do not rush to turn on the robot, since the Raspberry has not yet started, when the Raspberry boots up, a squeaker will sound, which means that the robot is ready to start.

Uploading a project to a robot
---------------------------
* Open **PyCharm** and click on the **“File”** button.
![18й](https://user-images.githubusercontent.com/99865132/168006479-0790610f-7114-4a1f-acc5-18fc41d6f2a8.png)
* Click on the **“Open”** button.
![image](https://user-images.githubusercontent.com/99865132/168014556-9d52b9d5-df75-4ab7-8ae9-10c3529c0a0a.png)
* By poking through the folders, find the unzipped **GitHub** repository **WRO-2022-Future-Engineers**.
![image](https://user-images.githubusercontent.com/99865132/168015700-e785c8f4-9d19-4207-8f51-e97e365ab069.png)
* You must open the project folder.
* Launch **Raspberry** and connect to it via Wi-Fi.
* Now return to **PyCharm** in the project files menu, select and open the **start_robot** program.
![image](https://user-images.githubusercontent.com/99865132/168015999-05a4f1a2-c0e1-4568-b873-1c8687272920.png)
* On the right side of the buttons at the top of the screen, click the **“Run”** button.


![23й](https://user-images.githubusercontent.com/99865132/168016170-a953aee0-f539-4c81-955a-6c0ce166a7fe.png)
* In the small window that opens, select **start_robot**


![image](https://user-images.githubusercontent.com/99865132/168016282-2e53acec-6b26-42a3-96ac-a8fa1d6cd929.png)
* This window will open


![image](https://user-images.githubusercontent.com/99865132/168017318-6276e432-869f-4ff4-b523-548920565a0f.png)
* To download the program, click on the **“load start”** button
![image](https://user-images.githubusercontent.com/99865132/168017359-d755c6bf-7d9f-4584-9ce2-bbf7d8e6f1e4.png)
* The **“start”** button is used to start the program.
![image](https://user-images.githubusercontent.com/99865132/168017416-add425a2-c137-4b5e-a4cf-a455f787f0d6.png)
* The **“stop”** button is used to stop the program.
![image](https://user-images.githubusercontent.com/99865132/168017455-b3ae978a-d458-4afc-a7c1-c87898680699.png)
* To start the test program, use the **“Raw”** button; at startup, just an image and FPS are displayed to check the performance.
![image](https://user-images.githubusercontent.com/99865132/168017603-62b039e3-7b37-4ff1-8492-da1be4916322.png)
* **“Video”** button is used to output video
![image](https://user-images.githubusercontent.com/99865132/168017679-6458132b-4aca-41cb-942b-4bedf91158bd.png)
* To connect to the robot, press the **“connect to robot”** button and then a window will pop up with connected devices via Wi-Fi
![image](https://user-images.githubusercontent.com/99865132/168017717-5e7effe9-31f0-470d-89bb-933b0b58b37e.png)
* Click on the top line


![image](https://user-images.githubusercontent.com/99865132/168017830-fc9c3bbd-1db9-4b84-b633-ab05b43c246c.png)
* After that, **Raspberry** will successfully connect to the program.
