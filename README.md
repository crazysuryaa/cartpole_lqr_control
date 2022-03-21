SES 598 - Autonomy for cart pole system
Name - Cherupally Surya Kiran
ASU Id - 1223453127

Inverted-Pendulum-Control
Design of a Linear Quadratic Regulator balance controller for the Inverted Pendulum. After manually initializing the pendulum in the upright vertical position, the balance controller moves the rotary arm to keep the pendulum in this upright position. Moreover it is capable of balancing itself, even if minor external disturbances are given.

For this we have made used of the python package control for the functions pole_place and lqr. In the future will try and understand how these work and implement these. There were a few subtle things that need to be mathematically correct for this to work. Look at the code”controller.py” to know the exact details.

Here is the system stabilized using Eigenvalues as a result of LQR (Linear Quadratic Regular)

https://youtu.be/1yNWJUq7lF8


Github Link:



Execution instructions

1 cd catkin_ws/src  
2. git clone https://github.com/venkatrebba/cartpole_lqr_control/  
3. cd ..  
4. catkin_make
5. chmod +x catkin_ws/src/cartpole_lqr_control/invpend_control/src/controller.py  
6. Run the below command in a terminal  
   roslaunch invpend_gazebo invpend_world.launch  
7. Run the below command in a new terminal  
    roslaunch invpend_control invpend_control.launch   
8. Run the below command in a new terminal  
    rosrun invpend_control controller.py  
   

