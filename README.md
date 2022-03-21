SES 598 - Autonomy for cart pole system
Name - Cherupally Surya Kiran
ASU Id - 1223453127

Inverted-Pendulum-Control
Design of a Linear Quadratic Regulator balancing controller for the Inverted Pendulum. The balancing controller moves the rotary arm to keep the pendulum in the upright vertical position after manually initializing it in that position. Furthermore, it is capable of self-balancing, even in the presence of modest external disturbances.

We used the functions "pole place" and "lqr" from the python package "control" for this.For this to work, there were a few minor details that needed to be mathematically correct. To find out more, look at the code "cart_pole_control.py."
As a result of LQR, the system has been stabilized using Eigenvalues (Linear Quadratic Regular)

https://youtu.be/1yNWJUq7lF8

<h1>Execution instructions</h1>

1 cd catkin_ws/src  
2. git clone https://crazysuryaa/cartpole_lqr_control/  
3. cd ..  
4. catkin_make
5. chmod +x catkin_ws/src/cartpole_lqr_control/invpend_control/src/controller.py  
6. Run the below command in a terminal  
   roslaunch invpend_gazebo invpend_world.launch  
7. Run the below command in a new terminal  
    roslaunch invpend_control invpend_control.launch   
8. Run the below command in a new terminal  
    rosrun invpend_control cart_pole_control.py  
   

