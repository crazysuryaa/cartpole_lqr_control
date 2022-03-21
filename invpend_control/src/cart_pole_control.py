#!/usr/bin/env python3
"""
LQR Controller for cart-pole problem
"""

import numpy as np
from std_msgs.msg import (UInt16, Float64)
from sensor_msgs.msg import JointState
from std_srvs.srv import Empty
from gazebo_msgs.msg import LinkState
from geometry_msgs.msg import Point
import control
import rospy
from scipy.signal import place_poles

class LQRController:
    def __init__(self):
        rospy.init_node('lqrcontroller', anonymous=True)
        self.pend_states_sub = rospy.Subscriber('/invpend/joint_states', JointState, self.state_check)
        self.publisher = rospy.Publisher('/invpend/joint1_velocity_controller/command', Float64, queue_size=10)
        self.cart_pos = 0
        self.cart_vel = 0
        self.pole_pos = 0
        self.pole_vel = 0
       
    def state_check(self, agent_info):
        self.cart_pos = agent_info.position[1]
        self.cart_vel = agent_info.velocity[1]
        self.pole_pos = agent_info.position[0]
        self.pole_vel = agent_info.velocity[0]

    def input(self,k):
        initial = np.array([0,0,0,0])
        current = np.array([self.cart_pos, self.cart_vel, self.pole_pos, self.pole_vel])
        self.publisher.publish(np.dot(k,(initial - current)))
        


def getK():
    """
    LQR controller
    
    The lqr() function computes the optimal state feedback controller 
    u = -K x that minimizes the quadratic cost
    
    
    K  - State feedback gains
    S - Solution to Riccati equation
    E  - Eigenvalues of the closed loop system
    """

    k,S,E = control.lqr(A,B,Q,R)
    controller =  control.place(A, B, E)
    return controller
    
if __name__ == '__main__':
    """
    A - Dynamics and input matrices

    B - Dynamics and input matrices

    sys- Linear system

    Q - State and input weight matrices

    R - State and input weight matrices
    """
    g = 9.8 
    l = 0.5 
    mass_pole = 2 
    mass_cart = 20  
    A = np.matrix([[0,1,0,0], [0,0,(-12*mass_pole*g)/((13*mass_cart)+ mass_pole),0], [0,0,0,1],[0,0,(12*g*(mass_cart + mass_pole))/(l * ((13*mass_cart) + mass_pole)),0]])
    B = np.matrix([ [0], [13 / ((13 * mass_cart) + mass_pole)], [0],  [-12 / (l * ((13 * mass_cart) + mass_pole))]])
    Q = np.diag([1,1,10,100])
    R = np.diag([0.01])
    try:
        model = LQRController()
        k=getK()
        while not rospy.is_shutdown():
            model.input(k)
    except rospy.ROSInterruptException as e:
        print(e.message)




