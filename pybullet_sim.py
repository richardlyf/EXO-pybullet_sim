# Author Richard Lin
# Stanford Robotics Exoskeleton team robot arm simulation.
# This program reads CSV file containing sensory data and translates that data to robot arm output.

import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -9.8)
armID = p.loadURDF("./exo-urdf/01-exo_arm.urdf", useFixedBase=True)

numJoints = p.getNumJoints(armID)
#print("number of joints discovered on the robot is: " + str(numJoints))
assert numJoints == 1, "More than 1 joint discovered. The rest of the code only considers one joint and the script will need to be modified to accomodate more joints."

# Info type: [jointIndex, jointName, jointType, qIndex, uIndex, flags, jointDamping, jointFriction, jointLowerLimit, jointUpperLimit, jointMaxForce, jointMaxVelocity, linkName, ...]
elbowJointID = 0
jointNameIndex = 1
jointTypeIndex = 2
jointLowerLimitIndex = 8
jointUpperLimitIndex = 9

elbowJointInfo = p.getJointInfo(armID, elbowJointID)
jointType = elbowJointInfo[jointTypeIndex]
jointLowerLimit = elbowJointInfo[jointLowerLimitIndex]
jointUpperLimit = elbowJointInfo[jointUpperLimitIndex]

#p.setJointMotorControl2(armID, elbowJointID, POSITION_CONTROL, targetPosition = 1.5)


for i in range(10000):
	pos = 2
	p.setJointMotorControl2(armID, elbowJointID, p.POSITION_CONTROL, targetPosition = pos)	
	print(p.getJointState(armID, elbowJointID)[0])
	p.stepSimulation()
	time.sleep(1/500)

p.disconnect()
	

