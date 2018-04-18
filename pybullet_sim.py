# Author Richard Lin
# Stanford Robotics Exoskeleton team robot arm simulation.
# This program reads CSV file containing sensory data and translates that data to robot arm output.

import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -9.8)

quaternionAngle = p.getQuaternionFromEuler([0, 0, -1])
armID = p.loadURDF("./exo-urdf/01-exo_arm.urdf", basePosition = [0, 0, -2], baseOrientation = quaternionAngle, useFixedBase=True, globalScaling = 4)

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

#p.setJointMotorControl2(armID, elbowJointID, p.POSITION_CONTROL, targetPosition = 1.5)

test_data = []
for i in range(20):
	test_data.append(i * 0.1)
print(test_data)

data_rate = 1
for i in range(10000):
	if i < len(test_data):
		pos = test_data[i]
	p.setJointMotorControl2(armID, elbowJointID, p.POSITION_CONTROL, targetPosition = pos, positionGain = 1)	
	print(p.getJointState(armID, elbowJointID)[0])
	p.stepSimulation()
	#print("1s interval: " + str(time.time()))
	time.sleep(data_rate)

p.disconnect()
	

