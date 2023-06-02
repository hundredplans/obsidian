# Setting up Armature
1. Shift-A - Creates armature
2. Stick Figure in side-tab/Viewport Display/In Front
3. Change original bone to small pelvis bone (root)
4. Disconnect shoulder bone from top of spine bone with Alt P/Disconnect Bone to allow for independent movement
5. Thumb should be disconnected from hand bone
6. Disconnect leg bone from pelvis bone
7. Shoulder -> Upper Arm -> Lower Arm -> Hand
8. Root -> Lower Spine -> Upper Spine -> Head
9. Upper Leg -> Lower Leg -> Foot
10. Make sure elbow bone is slightly tilted backward, Leg bone is slightly tilted backward and knee bone is slightly tilted forward
11. Foot bone should be from the top of the heel to the tip of the toe
12. Spine should have a slight s curse shape
13. Create a leg pole and target from the knee & foot respectively, Clear Parent with Alt-P and move the leg pole in front of the knee. Keep the target in place
14. Disable deform for both bones in side-tab bone icon
15. Press Ctrl-1 on Numpad then Shift-N and then align towards View Axis for all the bones to face towards the front
16. Name knee bone IKPole.L and foot bone IKTarget.L

# Setting Up Inverse Kinematics
1. Select the lower leg and go into Pose Mode
2. Go into blue bone icon in side-tab and add a Inverse Kinematic bone constraint
3. Choose armature as the target for both settings, choose IKTarget.L and then IKPole.L for the two bones in that order
4. Set chain length to however many bones you want Inverse Kinematics to control (usually 2) to fix weird rotation of armature
5. Change Pole Angle to 90d to flip foot into the correct direction
6. To fix foot bone bending downwards go into side-tab/Green Bone/Relations/Inherit Rotation Off
7. To make Foot rotate as target rotates go into side-tab/Blue Bone/Bone Constraint/Copy Rotation with Target as Armature and bone as IKTarget.L
8. Change Target and Owner on copy rotation from previous point to Local Space
9. Invert X and Y in Copy Rotation constraint so IKTarget.L rotates foot correctly

# After Inverse Kinematics
1. F3 - Symmetrize Apply (Make sure you do Step 15 from Setting Up Armature correctly for this to work properly)
2. Select Character then Shift-Select Armature press ^p to parent with Automatic Weights
3. Fixing Unlinked Objects, L (Select Object), ^g - Remove from all then ^g - Set active group to desired bone then ^g - Assign to active group, don't forget
4. If you select a vertex on the left in Item/Vertex Weights you can see how much each Vertex is assigned to each bone
	1. To go into Weight Paint mode select Armature then shift-select Mesh and press Ctrl-Tab [[Weight Paint]]