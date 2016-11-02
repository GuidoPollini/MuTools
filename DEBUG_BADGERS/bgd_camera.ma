//Maya ASCII 2015 scene
//Name: [10] bgd_camera.ma
//Last modified: Wed, Nov 02, 2016 04:14:10 PM
//Codeset: 1252
requires maya "2015";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2015";
fileInfo "version" "2015";
fileInfo "cutIdentifier" "201503261530-955654";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 41.619703908829756 26.761515108968279 34.363826186350281 ;
	setAttr ".r" -type "double3" -25.538352712060735 -2103.7999999996127 0 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 58.057488268378236;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0.25 0.25 0.25 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 6.865568693072202 100.1 6.0202866658023684 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 104.77096700237166;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 4.2374483334174942 -2.818087182432504 102.79910264528505 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 11.393070863833374;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 3.418190897161169 5.9293189664852477 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 9.5081382148821856;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "camera_rig";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "camera_global" -p "camera_rig";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "camera_globalShape" -p "camera_global";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".tw" yes;
createNode transform -n "cameras_holder" -p "camera_global";
	addAttr -ci true -sn "_placeHolder" -ln "_placeHolder" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "activeCamera" -ln "activeCamera" -nn "Active camera" -min 
		0 -max 1 -en "HD:PROJ" -at "enum";
	addAttr -ci true -sn "_placeHolder2" -ln "_placeHolder2" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "controllers_size" -ln "controllers_size" -nn "Controllers' visual size" 
		-dv 1 -min 0.1 -at "double";
	addAttr -ci true -sn "showGate" -ln "showGate" -nn "Show gate" -min 0 -max 1 -en 
		"OFF:ON" -at "enum";
	addAttr -ci true -sn "overscan" -ln "overscan" -dv 1 -min 0.1 -at "double";
	addAttr -ci true -sn "farClippingPlane" -ln "farClippingPlane" -nn "Far clipping plane" 
		-dv 10000 -min 1 -at "double";
	addAttr -ci true -sn "nearClippingPlane" -ln "nearClippingPlane" -nn "Near clipping plane" 
		-dv 1 -min 0.1 -at "double";
	addAttr -ci true -sn "_placeHolder3" -ln "_placeHolder3" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "imagePlaneSize" -ln "imagePlaneSize" -nn "Image Plane Size" 
		-dv 1 -min 0.001 -at "double";
	addAttr -ci true -sn "imagePlaneOpacity" -ln "imagePlaneOpacity" -dv 50 -min 0 -max 
		100 -at "double";
	addAttr -ci true -sn "imagePlaneShow" -ln "imagePlaneShow" -min 0 -max 1 -en "ON:OFF" 
		-at "enum";
	addAttr -ci true -sn "_placeHolder4" -ln "_placeHolder4" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHolder5" -ln "_placeHolder5" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHolder6" -ln "_placeHolder6" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHolder7" -ln "_placeHolder7" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	setAttr -l on -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -cb on "._placeHolder";
	setAttr -cb on ".activeCamera";
	setAttr -cb on "._placeHolder2";
	setAttr -cb on ".controllers_size";
	setAttr -cb on ".showGate" 1;
	setAttr -cb on ".overscan";
	setAttr -cb on ".farClippingPlane";
	setAttr -cb on ".nearClippingPlane";
	setAttr -cb on "._placeHolder3";
	setAttr -cb on ".imagePlaneSize";
	setAttr -cb on ".imagePlaneOpacity";
	setAttr -cb on ".imagePlaneShow";
	setAttr -cb on "._placeHolder4";
	setAttr -cb on "._placeHolder5";
	setAttr -cb on "._placeHolder6";
	setAttr -cb on "._placeHolder7";
createNode nurbsCurve -n "cameras_holderShape_2" -p "cameras_holder";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "cameras_holderShape_1" -p "cameras_holder";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode aimConstraint -n "cameras_holder_aimConstraint" -p "cameras_holder";
	addAttr -dcb 0 -ci true -sn "w0" -ln "camera_aimW0" -dv 1 -at "double";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".a" -type "double3" 0 0 -1 ;
	setAttr ".wut" 2;
	setAttr -k off ".ox";
	setAttr -k off ".oy";
	setAttr -k off ".oz";
createNode transform -n "cameraBG" -p "cameras_holder";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode camera -n "cameraBGShape" -p "cameraBG";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.41732 0.94488 ;
	setAttr -l on ".fio";
	setAttr -l on ".psc";
	setAttr -l on ".ct";
	setAttr -l on ".frp";
	setAttr -l on ".frv";
	setAttr -l on ".ptsc";
	setAttr ".ff" 0;
	setAttr -l on ".cs";
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
createNode transform -n "cameraHD_controller" -p "cameras_holder";
	addAttr -ci true -sn "_placeHolder" -ln "_placeHolder" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "focalLength" -ln "focalLength" -nn "Focal length" -dv 60 -min 
		1 -at "double";
	addAttr -ci true -sn "cameraBGFocalLength" -ln "cameraBGFocalLength" -nn "Camera BG Focal Length" 
		-dv 60 -min 1 -at "double";
	addAttr -ci true -sn "_placeHolder4" -ln "_placeHolder4" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHolder5" -ln "_placeHolder5" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHolder6" -ln "_placeHolder6" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHolder7" -ln "_placeHolder7" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	setAttr -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -cb on "._placeHolder";
	setAttr -k on ".focalLength";
	setAttr -cb on ".cameraBGFocalLength";
	setAttr -cb on "._placeHolder4";
	setAttr -cb on "._placeHolder5";
	setAttr -cb on "._placeHolder6";
	setAttr -cb on "._placeHolder7";
createNode mesh -n "cameraHD_controllerShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ovs" no;
	setAttr ".ovt" no;
	setAttr ".ovp" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".mb" no;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".vis" no;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".ds" no;
	setAttr ".smo" no;
	setAttr ".fbda" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -l on ".lev" 0;
	setAttr -l on ".ugsdt" no;
	setAttr -l on ".dsc";
	setAttr -l on ".uspr" no;
	setAttr -l on ".rsl" 0;
	setAttr -l on ".atm";
	setAttr ".dsm" 2;
	setAttr ".vcs" 2;
createNode mesh -n "cameraHD_controllerShapeOrig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 163 ".uvst[0].uvsp[0:162]" -type "float2" 0.125 0.012421131
		 0.13327681 1.4901161e-008 0.36672321 0.25 0.13327681 0.25 0.125 0.23757887 0.63327682
		 1.4901161e-008 0.86672324 1.4901161e-008 0.875 0.012421116 0.875 0.23757888 0.86672318
		 0.25 0.63327682 0.25 0.375 0.012421131 0.625 0.23757888 0.375 0.2582767 0.625 0.49172318
		 0.375 0.7582767 0.625 0.99172318 0.375 0.99172318 0.375 0.51242113 0.625 0.73757887
		 0.36672321 1.4901161e-008 0.625 0.012421131 0.37500003 0.23757888 0.625 0.25827682
		 0.375 0.49172321 0.625 0.51242113 0.37500003 0.73757893 0.625 0.75827682 0.375 0.3125
		 0.39583334 0.3125 0.39583334 0.40648496 0.375 0.40648496 0.41666669 0.3125 0.41666669
		 0.40648496 0.43750003 0.3125 0.43750003 0.40648496 0.45833337 0.3125 0.45833337 0.40648496
		 0.47916672 0.3125 0.47916672 0.40648496 0.50000006 0.3125 0.50000006 0.40648496 0.52083337
		 0.3125 0.52083337 0.40648496 0.54166669 0.3125 0.54166669 0.40648496 0.5625 0.3125
		 0.5625 0.40648496 0.58333331 0.3125 0.58333331 0.40648496 0.60416663 0.3125 0.60416663
		 0.40648496 0.62499994 0.3125 0.62499994 0.40648496 0.39583334 0.50046992 0.375 0.50046992
		 0.41666669 0.50046992 0.43750003 0.50046992 0.45833337 0.50046992 0.47916672 0.50046992
		 0.50000006 0.50046992 0.52083337 0.50046992 0.54166669 0.50046992 0.5625 0.50046992
		 0.58333331 0.50046992 0.60416663 0.50046992 0.62499994 0.50046992 0.375 0.68843985
		 0.39583334 0.68843985 0.41666669 0.68843985 0.43750003 0.68843985 0.45833337 0.68843985
		 0.47916672 0.68843985 0.50000006 0.68843985 0.52083337 0.68843985 0.54166669 0.68843985
		 0.5625 0.68843985 0.58333331 0.68843985 0.60416663 0.68843985 0.62499994 0.68843985
		 0.375 0.3125 0.39583334 0.3125 0.39583334 0.68843985 0.375 0.68843985 0.41666669
		 0.3125 0.41666669 0.68843985 0.54166669 0.3125 0.5625 0.3125 0.5625 0.68843985 0.54166669
		 0.68843985 0.58333331 0.3125 0.58333331 0.68843985 0.60416663 0.3125 0.60416663 0.68843985
		 0.62499994 0.3125 0.62499994 0.68843985 0.65625 0.15625 0.63531649 0.234375 0.578125
		 0.29156646 0.5 0.3125 0.5 0 0.578125 0.020933539 0.63531649 0.078125 0.5 1 0.5 0.6875
		 0.578125 0.70843351 0.63531649 0.765625 0.65625 0.84375 0.63531649 0.921875 0.578125
		 0.97906649 0.375 0.3125 0.39583334 0.3125 0.39583334 0.68843985 0.375 0.68843985
		 0.41666669 0.3125 0.41666669 0.68843985 0.54166669 0.3125 0.5625 0.3125 0.5625 0.68843985
		 0.54166669 0.68843985 0.58333331 0.3125 0.58333331 0.68843985 0.60416663 0.3125 0.60416663
		 0.68843985 0.62499994 0.3125 0.62499994 0.68843985 0.65625 0.15625 0.63531649 0.234375
		 0.578125 0.29156646 0.5 0.3125 0.5 0 0.578125 0.020933539 0.63531649 0.078125 0.5
		 1 0.5 0.6875 0.578125 0.70843351 0.63531649 0.765625 0.65625 0.84375 0.63531649 0.921875
		 0.578125 0.97906649 0.375 0.012421131 0.625 0.012421131 0.625 0.23757888 0.37500003
		 0.23757888 0.375 0.2582767 0.625 0.25827682 0.625 0.49172318 0.375 0.49172321 0.375
		 0.51242113 0.625 0.51242113 0.625 0.73757887 0.37500003 0.73757893 0.375 0.7582767
		 0.625 0.75827682 0.625 0.99172318 0.375 0.99172318 0.63327682 1.4901161e-008 0.86672324
		 1.4901161e-008 0.875 0.012421116 0.875 0.23757888 0.86672318 0.25 0.63327682 0.25
		 0.36672321 1.4901161e-008;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".ds" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 108 ".vt[0:107]"  -2.70397902 -3.3243084 12.86805344 -2.70397902 -2.93633556 13.24501133
		 2.70397902 -3.3243084 12.86805344 2.70397902 -2.93633556 13.24501133 -1.96297193 3.38357735 11.064520836
		 -1.96297193 2.99560428 11.44147587 1.96297193 3.38357735 11.064520836 1.96297193 2.99560428 11.44147587
		 -1.96297193 4.096460342 2.2571137 -1.96297193 4.48443365 2.63406825 1.96297193 4.096460342 2.2571137
		 1.96297193 4.48443365 2.63406825 -2.70397902 -3.3243084 2.23607969 -2.70397902 -2.93633556 1.85912442
		 2.70397902 -3.3243084 2.23607969 2.70397902 -2.93633556 1.85912442 1.024481654 0.59148479 0.42281163
		 0.59148473 1.024481773 0.42281163 6.2721462e-008 1.18296957 0.42281163 -0.59148479 1.024481535 0.42281163
		 -1.024481654 0.59148467 0.42281163 -1.18296957 -9.2055579e-008 0.42281163 -1.024481773 -0.59148484 0.42281163
		 -0.59148473 -1.024481654 0.42281163 9.4082253e-008 -1.18296957 0.42281163 0.59148484 -1.024481654 0.42281163
		 1.024481773 -0.59148479 0.42281163 1.18296957 -6.4980412e-008 0.42281157 1.15119576 0.66464329 0.17587063
		 0.66464323 1.15119588 0.17587063 0 1.32928658 0.17587063 -0.66464323 1.15119588 0.17587063
		 -1.15119565 0.66464329 0.17587063 -1.32928646 -8.6640547e-008 0.17587063 -1.15119588 -0.66464317 0.17587078
		 -0.66464329 -1.15119576 0.17587063 0 -1.32928646 0.17587078 0.66464323 -1.15119576 0.17587078
		 1.15119576 -0.66464323 0.17587078 1.32928646 1.0830068e-008 0.1758707 1.4151715 0.81704962 0.33888561
		 0.81704962 1.4151715 0.33888561 0 1.63409925 0.33888549 -0.81704962 1.4151715 0.33888561
		 -1.4151715 0.81704962 0.33888561 -1.63409925 0 0.33888561 -1.4151715 -0.81704962 0.33888549
		 -0.81704962 -1.4151715 0.33888566 0 -1.63409925 0.33888566 0.81704962 -1.4151715 0.33888566
		 1.4151715 -0.81704962 0.33888549 1.63409925 0 0.33888561 1.78411531 1.028691173 2.10402799
		 1.030059576 1.78174496 2.14288449 0 2.057382107 2.15710855 -1.030059576 1.78174496 2.14288449
		 -1.78411531 1.028691173 2.10402799 -2.060119152 0 2.050947666 -1.78411531 -1.028690696 1.9978689
		 -1.030059576 -1.78174496 1.95901203 0 -2.057381868 1.94478929 1.030059576 -1.78174496 1.95901203
		 1.78411531 -1.028690696 1.9978689 2.060119152 0 2.050947666 1.20474553 1.53355229 13.37396049
		 1.15276527 2.25106454 12.39020157 1.15276527 2.34870362 11.64439011 1.52913404 -2.57204318 13.12580299
		 1.45182347 -1.89579237 13.81311798 1.36331391 -0.75235534 14.14946651 1.26983738 0.54026997 13.96860695
		 -1.20474505 1.53355205 13.37396049 -1.15276527 2.25106478 12.39020157 -1.15276527 2.34870362 11.64439011
		 -1.52913404 -2.57204199 13.12580299 -1.45182323 -1.89579177 13.81311798 -1.36331534 -0.75235534 14.14946651
		 -1.26983786 0.54027021 13.96860695 0.92999113 5.48014116 5.39166403 1.056087852 5.072662354 4.49561501
		 1.1396656 4.3297472 3.90099597 1.1396656 3.55734468 9.77828121 1.081413746 4.41893721 9.31930828
		 0.95765841 5.22173119 8.35870457 0.84793699 5.63698053 6.86966324 -0.9299913 5.48014069 5.39166403
		 -1.056087613 5.072660446 4.49561501 -1.1396656 4.32974529 3.90099597 -1.1396656 3.55734324 9.77828121
		 -1.081413507 4.41893578 9.31930828 -0.95765913 5.22173119 8.35870457 -0.84793699 5.63698053 6.86966324
		 2.66706657 -3.21015263 11.13594627 2.66706657 -2.87508368 11.40727806 3.87000871 -3.0071365833 10.75451565
		 3.87000871 -2.72123671 10.99777412 2.067451477 2.51730633 9.30865192 2.067451477 2.18223763 9.57998466
		 2.97412825 1.79320812 9.11628914 3.07848382 1.50730848 9.35954666 2.067451477 2.56481981 3.74212503
		 2.067451477 2.89988852 4.013456345 3.07848382 1.88989043 4.15162992 2.97412825 2.17579031 4.39488745
		 2.66706657 -3.21015263 3.76308107 2.66706657 -2.87508368 3.49174905 3.87000871 -3.0071365833 4.1445117
		 3.87000871 -2.72123671 3.90125394;
	setAttr -s 174 ".ed";
	setAttr ".ed[0:165]"  1 5 0 0 1 0 3 7 0 2 3 0 4 9 0 5 4 0 6 11 0 6 7 0 8 13 0
		 9 8 0 10 15 0 10 11 0 12 0 0 12 13 0 14 2 0 14 15 0 1 3 1 2 0 1 4 6 1 7 5 1 8 10 1
		 11 9 1 12 14 1 15 13 1 16 17 0 17 18 0 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0 23 24 0
		 24 25 0 25 26 0 26 27 0 27 16 0 28 29 1 29 30 1 30 31 1 31 32 1 32 33 1 33 34 1 34 35 1
		 35 36 1 36 37 1 37 38 1 38 39 1 39 28 1 40 41 1 41 42 1 42 43 1 43 44 1 44 45 1 45 46 1
		 46 47 1 47 48 1 48 49 1 49 50 1 50 51 1 51 40 1 52 53 0 53 54 0 54 55 0 55 56 0 56 57 0
		 57 58 0 58 59 0 59 60 0 60 61 0 61 62 0 62 63 0 63 52 0 16 28 1 17 29 1 18 30 1 19 31 1
		 20 32 1 21 33 1 22 34 1 23 35 1 24 36 1 25 37 1 26 38 1 27 39 1 28 40 1 29 41 1 30 42 1
		 31 43 1 32 44 1 33 45 1 34 46 1 35 47 1 36 48 1 37 49 1 38 50 1 39 51 1 40 52 1 51 63 1
		 50 62 1 49 61 1 48 60 1 47 59 1 46 58 1 45 57 1 44 56 1 43 55 1 42 54 1 41 53 1 64 65 0
		 65 66 0 67 68 0 68 69 0 69 70 0 70 64 0 71 72 0 72 73 0 74 75 0 75 76 0 76 77 0 77 71 0
		 64 71 1 65 72 1 66 73 0 67 74 0 68 75 1 69 76 1 70 77 1 67 66 0 74 73 0 78 79 0 79 80 0
		 81 82 0 82 83 0 83 84 0 84 78 0 85 86 0 86 87 0 88 89 0 89 90 0 90 91 0 91 85 0 78 85 1
		 79 86 1 80 87 0 81 88 0 82 89 1 83 90 1 84 91 1 81 80 0 88 87 0 93 97 0 92 93 0 95 99 0
		 94 95 0 96 101 0 97 96 0 98 103 0 98 99 0 100 105 0 101 100 0 102 107 0 102 103 0
		 104 92 0 104 105 0 106 94 0 106 107 0;
	setAttr ".ed[166:173]" 93 95 1 94 92 1 96 98 1 99 97 1 100 102 1 103 101 1
		 104 106 1 107 105 1;
	setAttr -s 71 -ch 308 ".fc[0:70]" -type "polyFaces" 
		f 4 16 2 19 -1
		mu 0 4 11 21 12 22
		f 4 18 6 21 -5
		mu 0 4 13 23 14 24
		f 4 20 10 23 -9
		mu 0 4 18 25 19 26
		f 4 22 14 17 -13
		mu 0 4 15 27 16 17
		f 8 -4 -15 15 -11 11 -7 7 -3
		mu 0 8 21 5 6 7 8 9 10 12
		f 8 -14 12 1 0 5 4 9 8
		mu 0 8 0 1 20 11 22 2 3 4
		f 4 -2 -18 3 -17
		mu 0 4 11 20 5 21
		f 4 -6 -20 -8 -19
		mu 0 4 13 22 12 23
		f 4 -10 -22 -12 -21
		mu 0 4 18 24 14 25
		f 4 13 -24 -16 -23
		mu 0 4 15 26 19 27
		f 4 24 73 -37 -73
		mu 0 4 28 29 30 31
		f 4 25 74 -38 -74
		mu 0 4 29 32 33 30
		f 4 26 75 -39 -75
		mu 0 4 32 34 35 33
		f 4 27 76 -40 -76
		mu 0 4 34 36 37 35
		f 4 28 77 -41 -77
		mu 0 4 36 38 39 37
		f 4 29 78 -42 -78
		mu 0 4 38 40 41 39
		f 4 30 79 -43 -79
		mu 0 4 40 42 43 41
		f 4 31 80 -44 -80
		mu 0 4 42 44 45 43
		f 4 32 81 -45 -81
		mu 0 4 44 46 47 45
		f 4 33 82 -46 -82
		mu 0 4 46 48 49 47
		f 4 34 83 -47 -83
		mu 0 4 48 50 51 49
		f 4 35 72 -48 -84
		mu 0 4 50 52 53 51
		f 4 36 85 -49 -85
		mu 0 4 31 30 54 55
		f 4 37 86 -50 -86
		mu 0 4 30 33 56 54
		f 4 38 87 -51 -87
		mu 0 4 33 35 57 56
		f 4 39 88 -52 -88
		mu 0 4 35 37 58 57
		f 4 40 89 -53 -89
		mu 0 4 37 39 59 58
		f 4 41 90 -54 -90
		mu 0 4 39 41 60 59
		f 4 42 91 -55 -91
		mu 0 4 41 43 61 60
		f 4 43 92 -56 -92
		mu 0 4 43 45 62 61
		f 4 44 93 -57 -93
		mu 0 4 45 47 63 62
		f 4 45 94 -58 -94
		mu 0 4 47 49 64 63
		f 4 46 95 -59 -95
		mu 0 4 49 51 65 64
		f 4 47 84 -60 -96
		mu 0 4 51 53 66 65
		f 4 -97 48 107 -61
		mu 0 4 67 55 54 68
		f 4 49 106 -62 -108
		mu 0 4 54 56 69 68
		f 4 50 105 -63 -107
		mu 0 4 56 57 70 69
		f 4 51 104 -64 -106
		mu 0 4 57 58 71 70
		f 4 52 103 -65 -105
		mu 0 4 58 59 72 71
		f 4 53 102 -66 -104
		mu 0 4 59 60 73 72
		f 4 54 101 -67 -103
		mu 0 4 60 61 74 73
		f 4 55 100 -68 -102
		mu 0 4 61 62 75 74
		f 4 56 99 -69 -101
		mu 0 4 62 63 76 75
		f 4 57 98 -70 -100
		mu 0 4 63 64 77 76
		f 4 58 97 -71 -99
		mu 0 4 64 65 78 77
		f 4 59 96 -72 -98
		mu 0 4 65 66 79 78
		f 4 108 121 -115 -121
		mu 0 4 80 81 82 83
		f 4 109 122 -116 -122
		mu 0 4 81 84 85 82
		f 4 110 124 -117 -124
		mu 0 4 86 87 88 89
		f 4 111 125 -118 -125
		mu 0 4 87 90 91 88
		f 4 112 126 -119 -126
		mu 0 4 90 92 93 91
		f 4 113 120 -120 -127
		mu 0 4 92 94 95 93
		f 7 -113 -112 -111 127 -110 -109 -114
		mu 0 7 96 97 98 99 100 101 102
		f 7 -129 116 117 118 119 114 115
		mu 0 7 103 104 105 106 107 108 109
		f 4 129 142 -136 -142
		mu 0 4 110 111 112 113
		f 4 130 143 -137 -143
		mu 0 4 111 114 115 112
		f 4 131 145 -138 -145
		mu 0 4 116 117 118 119
		f 4 132 146 -139 -146
		mu 0 4 117 120 121 118
		f 4 133 147 -140 -147
		mu 0 4 120 122 123 121
		f 4 134 141 -141 -148
		mu 0 4 122 124 125 123
		f 7 -134 -133 -132 148 -131 -130 -135
		mu 0 7 126 127 128 129 130 131 132
		f 7 -150 137 138 139 140 135 136
		mu 0 7 133 134 135 136 137 138 139
		f 4 166 152 169 -151
		mu 0 4 140 141 142 143
		f 4 168 156 171 -155
		mu 0 4 144 145 146 147
		f 4 170 160 173 -159
		mu 0 4 148 149 150 151
		f 4 172 164 167 -163
		mu 0 4 152 153 154 155
		f 8 -154 -165 165 -161 161 -157 157 -153
		mu 0 8 141 156 157 158 159 160 161 142
		f 4 -152 -168 153 -167
		mu 0 4 140 162 156 141
		f 4 -156 -170 -158 -169
		mu 0 4 144 143 142 145
		f 4 -160 -172 -162 -171
		mu 0 4 148 147 146 149
		f 4 163 -174 -166 -173
		mu 0 4 152 151 150 153;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode nurbsCurve -n "curveShape4Orig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 29 0 no 3
		34 0 0 0 2.6757161317629898 3.3774734574810914 4.388220641932806 5.5421219838992162
		 6.6236968027734884 8.1938447911947812 8.5390961181818934 9.2789203902961752 10.296016084431432
		 11.259036370729735 11.756641247981126 12.788013313288351 13.513781169124076 14.290471866431979
		 16.022218351309899 16.917755712496039 18.031168138376525 18.950943620624201 19.531854451518306
		 20.108657298034064 20.916572329476807 22.315149540821203 23.554456311883527 24.631509635976062
		 26.092462288909225 27.090567203377763 27.70847765956227 28.686894538504564 29 29
		 29
		32
		7.4282758447845021 1.3973960219272816e-015 6.2933122036407196
		7.0692193947600721 1.4922546856502972e-015 6.7205176462365532
		6.9280387543437829 1.7225063896760278e-015 7.7574791346882606
		7.7082743419625563 1.83772390224578e-015 8.2763726813639487
		8.1469507948818158 1.9288396216341826e-015 8.6867214012491534
		9.0263069614078599 1.9081305833458151e-015 8.5934561841304582
		9.0457794584875195 1.6669638164909847e-015 7.5073376227889019
		8.1444947581526783 1.6509925360709536e-015 7.4354093702406168
		7.6909790727343115 1.7155407419141147e-015 7.7261086460233148
		7.2019520839911522 1.742521053869058e-015 7.8476171688899363
		7.2166663797798849 1.8911670323896637e-015 8.5170591423654542
		6.9515135131833015 1.994542073342884e-015 8.9826189382817905
		7.0959400063994282 2.1098453047366169e-015 9.5018985282212203
		7.0054114998035963 2.216675061270879e-015 9.9830169799410058
		7.6997151362281908 2.3129947538691159e-015 10.416802311634866
		7.6491054907811353 2.0834583076182582e-015 9.3830620578315482
		6.7714703928020237 2.0373566902941744e-015 9.1754388312296307
		6.0527124354148363 2.0982713576547313e-015 9.4497741044560364
		5.4984284227607274 2.1625130817927357e-015 9.7390931093455873
		5.0699339923758631 2.2258806767910792e-015 10.024475386567493
		4.552182374576395 2.2499945598361454e-015 10.133074661263709
		4.6857268857194221 2.3677038176123459e-015 10.663190030722665
		5.2627747517275356 2.4101280707152463e-015 10.854251881188357
		5.9000301235617574 2.473859414993499e-015 11.141272339531719
		6.7952776792673166 2.4509651631181705e-015 11.03816579531706
		7.1526686146332938 2.6265895967207056e-015 11.829107929046597
		7.5267936111172453 2.7839276331743064e-015 12.537695451390238
		8.215620878510288 2.7942064556580425e-015 12.583987152497798
		8.7701267829422704 2.7852035320290987e-015 12.543441588997238
		9.0458120840401453 2.7115051008276139e-015 12.211533361700445
		9.2505612348390667 2.6733531889340503e-015 12.039712425513118
		9.3034744977354311 2.6648556120159893e-015 12.001442741271386
		;
createNode nurbsCurve -n "HShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "DShape1" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "DShape2" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "HShapeOrig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 12 2 no 3
		13 0 0.30000000000000004 1.3 2.4000000000000004 3.4000000000000004 3.7000000000000002
		 5.8000000000000007 6.1000000000000005 7 8.0999999999999996 9 9.3000000000000007 11.4
		
		13
		3.8362011663027147 -2.5246955278296173 5.4817846473213674
		3.836658351296188 -2.5249527968616197 5.601808173478541
		3.7628433756128503 -2.1317405305740547 5.6029321900994047
		3.7645197205889191 -2.1326838503580632 6.0430184526757085
		3.8383346962722569 -2.5258961166456282 6.0418944360548448
		3.8387918812657302 -2.5261533856776301 6.1619179622120193
		3.6837804323307211 -1.7004076264737444 6.1642783971158313
		3.6833232473372477 -1.7001503574417423 6.0442548709586577
		3.7497567254522517 -2.0540413971005504 6.0432432559998803
		3.7480803804761829 -2.0530980773165419 5.6031569934235765
		3.6816469023611789 -1.6992070376577337 5.6041686083823539
		3.6811897173677055 -1.6989497686257313 5.4841450822251794
		3.8362011663027147 -2.5246955278296173 5.4817846473213674
		;
createNode nurbsCurve -n "DShape1Orig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 9 1 no 3
		12 0 0 1 1 1.6906263828488595 1.6906263828488595 3.7906263828488598 3.7906263828488598
		 4.481252765697719 4.481252765697719 5.481252765697719 5.481252765697719
		11
		3.7544199942905103 -2.1050204803289017 4.6028063909003896
		3.832848476350577 -2.5228088882616007 4.6016121221687598
		3.8345391062502996 -2.5237602465169786 5.0454485666894886
		3.8350653462808584 -2.5240563744852964 5.1836009229006459
		3.8355915863114172 -2.5243525024536142 5.3217532791118032
		3.7580858618439126 -2.1114796228516717 5.3229334965637092
		3.680580137376408 -1.6986067432497285 5.3241137140156152
		3.6800538973458492 -1.6983106152814105 5.1859613578044579
		3.6795276573152904 -1.6980144873130927 5.0478090015933006
		3.6778370274155678 -1.6970631290577147 4.6039725570725727
		3.7544199942905103 -2.1050204803289017 4.6028063909003896
		;
createNode nurbsCurve -n "DShape2Orig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 15 1 no 3
		18 0 0 1 2 3 4 4 4.3937514305333032 4.3937514305333032 6.0937514305333034 6.0937514305333034
		 6.4875028610666066 6.4875028610666066 7.4875028610666066 8.4875028610666057 9.4875028610666057
		 10.487502861066606 10.487502861066606
		17
		3.7548771792839837 -2.1052777493609041 4.7228299170575632
		3.7403448594661524 -2.0278641031856477 4.723051207776197
		3.7177379741310785 -1.9068927225245977 4.7534029231954609
		3.701982480238355 -1.8216472634428196 4.8261611451049529
		3.6939263345773234 -1.7764519301081312 4.9519408228742083
		3.6942858900356073 -1.776654260643963 5.0463339341274738
		3.6945859187776047 -1.776823094059601 5.1250996593308713
		3.6948859475196021 -1.776991927475239 5.2038653845342688
		3.7576286768504392 -2.1112223538196693 5.2029099704065356
		3.8203714061812764 -2.4454527801640991 5.2019545562788014
		3.8200713774392789 -2.4452839467484613 5.1231888310754039
		3.8197713486972811 -2.4451151133328231 5.0444231058720064
		3.8194117932389977 -2.4449127827969912 4.9500299946187409
		3.8101723903069442 -2.3979520648994437 4.8257640212610937
		3.7936290276839446 -2.3111642525524729 4.7522472931247535
		3.7698708497394877 -2.1851490097006736 4.7226016011278524
		3.7548771792839837 -2.1052777493609041 4.7228299170575632
		;
createNode transform -n "cameraHD" -p "cameraHD_controller";
	setAttr ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode camera -n "cameraHDShape" -p "cameraHD";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.7777777777777777 1 ;
	setAttr -l on ".fio";
	setAttr -l on ".psc";
	setAttr -l on ".ct";
	setAttr -l on ".frp";
	setAttr -l on ".frv";
	setAttr -l on ".ptsc";
	setAttr ".ff" 3;
	setAttr -l on ".ffo";
	setAttr -l on ".cs";
	setAttr ".ncp" 1;
	setAttr ".coi" 11.025515882143505;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
	setAttr ".dgo" 1;
	setAttr ".dgc" -type "float3" 0 0 0 ;
createNode nurbsCurve -n "__cameraAim_cameraHD_lineShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "__cameraAim_cameraHD_lineShapeOrig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 10
		0 0 0
		;
createNode transform -n "__cameraAim_cameraHD_line_cluster_holder" -p "cameraHD_controller";
	setAttr -l on ".v" no;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".tx";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0.25 0.25 0.25 ;
	setAttr ".sp" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "__cameraAim_cameraHD_line_cluster" -p "__cameraAim_cameraHD_line_cluster_holder";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0 0 10 ;
	setAttr ".sp" -type "double3" 0 0 10 ;
createNode clusterHandle -n "__cameraAim_cameraHD_line_clusterShape" -p "__cameraAim_cameraHD_line_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v" no;
	setAttr ".or" -type "double3" 0 0 10 ;
createNode pointConstraint -n "__cameraAim_cameraHD_line_cluster_pointConstraint1" 
		-p "__cameraAim_cameraHD_line_cluster";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "cameras_holderW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 0 -10 ;
	setAttr -k on ".w0";
createNode nurbsCurve -n "focalCircle1HDShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "focalCircle2HDShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "focalCircle1ShapeOrig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1766992929027924 1.1766992929027904 -1.89227678477546e-016
		-1.8985437992126872e-016 1.6641040988579585 -2.6760834927932116e-016
		-1.1766992929027911 1.1766992929027911 -1.8922767847754612e-016
		-1.6641040988579585 4.8221573525161483e-016 -7.7546204588859417e-032
		-1.1766992929027915 -1.1766992929027908 1.8922767847754605e-016
		-5.0142704183843658e-016 -1.6641040988579587 2.6760834927932121e-016
		1.1766992929027904 -1.1766992929027913 1.8922767847754612e-016
		1.6641040988579585 -8.9379355772183028e-016 1.4373296643075375e-031
		1.1766992929027924 1.1766992929027904 -1.89227678477546e-016
		-1.8985437992126872e-016 1.6641040988579585 -2.6760834927932116e-016
		-1.1766992929027911 1.1766992929027911 -1.8922767847754612e-016
		;
createNode nurbsCurve -n "focalCircle2ShapeOrig" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.3751627926219696 1.3751627926219674 -2.2114304338079611e-016
		-2.218754450340375e-016 1.9447738717968477 -3.1274349117358378e-016
		-1.3751627926219683 1.3751627926219683 -2.2114304338079626e-016
		-1.9447738717968477 5.635468136459975e-016 -9.0625239517722713e-032
		-1.3751627926219685 -1.3751627926219678 2.2114304338079618e-016
		-5.8599832200942876e-016 -1.9447738717968479 3.1274349117358383e-016
		1.3751627926219674 -1.3751627926219683 2.2114304338079626e-016
		1.9447738717968477 -1.0445418402795073e-015 1.6797513918883914e-031
		1.3751627926219696 1.3751627926219674 -2.2114304338079611e-016
		-2.218754450340375e-016 1.9447738717968477 -3.1274349117358378e-016
		-1.3751627926219683 1.3751627926219683 -2.2114304338079626e-016
		;
createNode transform -n "__focalCircles_HD_cluster_holder" -p "cameraHD_controller";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0.25 0.24999999999999989 0.25 ;
	setAttr ".sp" -type "double3" 0.25 0.24999999999999989 0.25 ;
createNode transform -n "__focalCircles_HD_cluster" -p "__focalCircles_HD_cluster_holder";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0 -1.1102230246251565e-016 2.4651903288156619e-032 ;
	setAttr ".sp" -type "double3" 0 -1.1102230246251565e-016 2.4651903288156619e-032 ;
createNode clusterHandle -n "__focalCircles_HD_clusterShape" -p "__focalCircles_HD_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 -1.1102230246251565e-016 2.4651903288156619e-032 ;
createNode transform -n "cameraPROJ_controller" -p "cameras_holder";
	addAttr -ci true -sn "zoom" -ln "zoom" -dv 1 -min 0.1 -at "double";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	addAttr -ci true -sn "_placeHodler" -ln "_placeHodler" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "focalLength" -ln "focalLength" -nn "Focal length" -dv 60 -min 
		1 -at "double";
	addAttr -ci true -sn "cameraBGFocalLength" -ln "cameraBGFocalLength" -nn "Camera BG Focal Length" 
		-dv 60 -min 1 -at "double";
	addAttr -ci true -sn "_placeHodler6" -ln "_placeHodler6" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "panSensitivity" -ln "panSensitivity" -nn "Pan sensitivity" 
		-dv 100 -min 1 -at "double";
	addAttr -ci true -sn "_placeHodler2" -ln "_placeHodler2" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHodler3" -ln "_placeHodler3" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHodler4" -ln "_placeHodler4" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	addAttr -ci true -sn "_placeHodler5" -ln "_placeHodler5" -nn " " -min 0 -max 0 -en 
		"   " -at "enum";
	setAttr -k off ".v";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".zoom";
	setAttr ".aal" -type "attributeAlias" {"Roll","rotateZ","PanX","translateX","PanY"
		,"translateY"} ;
	setAttr -cb on "._placeHodler";
	setAttr -cb on ".focalLength";
	setAttr -cb on ".cameraBGFocalLength";
	setAttr -cb on "._placeHodler6";
	setAttr -cb on ".panSensitivity";
	setAttr -cb on "._placeHodler2";
	setAttr -cb on "._placeHodler3";
	setAttr -cb on "._placeHodler4";
	setAttr -cb on "._placeHodler5";
createNode mesh -n "cameraPROJ_controllerShape" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ovs" no;
	setAttr ".ovt" no;
	setAttr ".ovp" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".mb" no;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".vis" no;
	setAttr ".pv" -type "double2" 0.5 0.5 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".ds" no;
	setAttr ".smo" no;
	setAttr ".fbda" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -l on ".lev" 0;
	setAttr -l on ".ugsdt" no;
	setAttr -l on ".dsc";
	setAttr -l on ".uspr" no;
	setAttr -l on ".rsl" 0;
	setAttr -l on ".atm";
	setAttr ".dsm" 2;
	setAttr ".vcs" 2;
createNode mesh -n "cameraPROJ_controllerShapeOrig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".csh" no;
	setAttr ".rcsh" no;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 163 ".uvst[0].uvsp[0:162]" -type "float2" 0.125 0.012421131
		 0.13327681 1.4901161e-008 0.36672321 0.25 0.13327681 0.25 0.125 0.23757887 0.63327682
		 1.4901161e-008 0.86672324 1.4901161e-008 0.875 0.012421116 0.875 0.23757888 0.86672318
		 0.25 0.63327682 0.25 0.375 0.012421131 0.625 0.23757888 0.375 0.2582767 0.625 0.49172318
		 0.375 0.7582767 0.625 0.99172318 0.375 0.99172318 0.375 0.51242113 0.625 0.73757887
		 0.36672321 1.4901161e-008 0.625 0.012421131 0.37500003 0.23757888 0.625 0.25827682
		 0.375 0.49172321 0.625 0.51242113 0.37500003 0.73757893 0.625 0.75827682 0.375 0.3125
		 0.39583334 0.3125 0.39583334 0.40648496 0.375 0.40648496 0.41666669 0.3125 0.41666669
		 0.40648496 0.43750003 0.3125 0.43750003 0.40648496 0.45833337 0.3125 0.45833337 0.40648496
		 0.47916672 0.3125 0.47916672 0.40648496 0.50000006 0.3125 0.50000006 0.40648496 0.52083337
		 0.3125 0.52083337 0.40648496 0.54166669 0.3125 0.54166669 0.40648496 0.5625 0.3125
		 0.5625 0.40648496 0.58333331 0.3125 0.58333331 0.40648496 0.60416663 0.3125 0.60416663
		 0.40648496 0.62499994 0.3125 0.62499994 0.40648496 0.39583334 0.50046992 0.375 0.50046992
		 0.41666669 0.50046992 0.43750003 0.50046992 0.45833337 0.50046992 0.47916672 0.50046992
		 0.50000006 0.50046992 0.52083337 0.50046992 0.54166669 0.50046992 0.5625 0.50046992
		 0.58333331 0.50046992 0.60416663 0.50046992 0.62499994 0.50046992 0.375 0.68843985
		 0.39583334 0.68843985 0.41666669 0.68843985 0.43750003 0.68843985 0.45833337 0.68843985
		 0.47916672 0.68843985 0.50000006 0.68843985 0.52083337 0.68843985 0.54166669 0.68843985
		 0.5625 0.68843985 0.58333331 0.68843985 0.60416663 0.68843985 0.62499994 0.68843985
		 0.375 0.3125 0.39583334 0.3125 0.39583334 0.68843985 0.375 0.68843985 0.41666669
		 0.3125 0.41666669 0.68843985 0.54166669 0.3125 0.5625 0.3125 0.5625 0.68843985 0.54166669
		 0.68843985 0.58333331 0.3125 0.58333331 0.68843985 0.60416663 0.3125 0.60416663 0.68843985
		 0.62499994 0.3125 0.62499994 0.68843985 0.65625 0.15625 0.63531649 0.234375 0.578125
		 0.29156646 0.5 0.3125 0.5 0 0.578125 0.020933539 0.63531649 0.078125 0.5 1 0.5 0.6875
		 0.578125 0.70843351 0.63531649 0.765625 0.65625 0.84375 0.63531649 0.921875 0.578125
		 0.97906649 0.375 0.3125 0.39583334 0.3125 0.39583334 0.68843985 0.375 0.68843985
		 0.41666669 0.3125 0.41666669 0.68843985 0.54166669 0.3125 0.5625 0.3125 0.5625 0.68843985
		 0.54166669 0.68843985 0.58333331 0.3125 0.58333331 0.68843985 0.60416663 0.3125 0.60416663
		 0.68843985 0.62499994 0.3125 0.62499994 0.68843985 0.65625 0.15625 0.63531649 0.234375
		 0.578125 0.29156646 0.5 0.3125 0.5 0 0.578125 0.020933539 0.63531649 0.078125 0.5
		 1 0.5 0.6875 0.578125 0.70843351 0.63531649 0.765625 0.65625 0.84375 0.63531649 0.921875
		 0.578125 0.97906649 0.375 0.012421131 0.625 0.012421131 0.625 0.23757888 0.37500003
		 0.23757888 0.375 0.2582767 0.625 0.25827682 0.625 0.49172318 0.375 0.49172321 0.375
		 0.51242113 0.625 0.51242113 0.625 0.73757887 0.37500003 0.73757893 0.375 0.7582767
		 0.625 0.75827682 0.625 0.99172318 0.375 0.99172318 0.63327682 1.4901161e-008 0.86672324
		 1.4901161e-008 0.875 0.012421116 0.875 0.23757888 0.86672318 0.25 0.63327682 0.25
		 0.36672321 1.4901161e-008;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".ds" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 108 ".vt[0:107]"  -2.70397902 -3.3243084 12.86805344 -2.70397902 -2.93633556 13.24501133
		 2.70397902 -3.3243084 12.86805344 2.70397902 -2.93633556 13.24501133 -1.96297193 3.38357735 11.064520836
		 -1.96297193 2.99560428 11.44147587 1.96297193 3.38357735 11.064520836 1.96297193 2.99560428 11.44147587
		 -1.96297193 4.096460342 2.2571137 -1.96297193 4.48443365 2.63406825 1.96297193 4.096460342 2.2571137
		 1.96297193 4.48443365 2.63406825 -2.70397902 -3.3243084 2.23607969 -2.70397902 -2.93633556 1.85912442
		 2.70397902 -3.3243084 2.23607969 2.70397902 -2.93633556 1.85912442 1.024481654 0.59148479 0.42281163
		 0.59148473 1.024481773 0.42281163 6.2721462e-008 1.18296957 0.42281163 -0.59148479 1.024481535 0.42281163
		 -1.024481654 0.59148467 0.42281163 -1.18296957 -9.2055579e-008 0.42281163 -1.024481773 -0.59148484 0.42281163
		 -0.59148473 -1.024481654 0.42281163 9.4082253e-008 -1.18296957 0.42281163 0.59148484 -1.024481654 0.42281163
		 1.024481773 -0.59148479 0.42281163 1.18296957 -6.4980412e-008 0.42281157 1.15119576 0.66464329 0.17587063
		 0.66464323 1.15119588 0.17587063 0 1.32928658 0.17587063 -0.66464323 1.15119588 0.17587063
		 -1.15119565 0.66464329 0.17587063 -1.32928646 -8.6640547e-008 0.17587063 -1.15119588 -0.66464317 0.17587078
		 -0.66464329 -1.15119576 0.17587063 0 -1.32928646 0.17587078 0.66464323 -1.15119576 0.17587078
		 1.15119576 -0.66464323 0.17587078 1.32928646 1.0830068e-008 0.1758707 1.4151715 0.81704962 0.33888561
		 0.81704962 1.4151715 0.33888561 0 1.63409925 0.33888549 -0.81704962 1.4151715 0.33888561
		 -1.4151715 0.81704962 0.33888561 -1.63409925 0 0.33888561 -1.4151715 -0.81704962 0.33888549
		 -0.81704962 -1.4151715 0.33888566 0 -1.63409925 0.33888566 0.81704962 -1.4151715 0.33888566
		 1.4151715 -0.81704962 0.33888549 1.63409925 0 0.33888561 1.78411531 1.028691173 2.10402799
		 1.030059576 1.78174496 2.14288449 0 2.057382107 2.15710855 -1.030059576 1.78174496 2.14288449
		 -1.78411531 1.028691173 2.10402799 -2.060119152 0 2.050947666 -1.78411531 -1.028690696 1.9978689
		 -1.030059576 -1.78174496 1.95901203 0 -2.057381868 1.94478929 1.030059576 -1.78174496 1.95901203
		 1.78411531 -1.028690696 1.9978689 2.060119152 0 2.050947666 1.20474553 1.53355229 13.37396049
		 1.15276527 2.25106454 12.39020157 1.15276527 2.34870362 11.64439011 1.52913404 -2.57204318 13.12580299
		 1.45182347 -1.89579237 13.81311798 1.36331391 -0.75235534 14.14946651 1.26983738 0.54026997 13.96860695
		 -1.20474505 1.53355205 13.37396049 -1.15276527 2.25106478 12.39020157 -1.15276527 2.34870362 11.64439011
		 -1.52913404 -2.57204199 13.12580299 -1.45182323 -1.89579177 13.81311798 -1.36331534 -0.75235534 14.14946651
		 -1.26983786 0.54027021 13.96860695 0.92999113 5.48014116 5.39166403 1.056087852 5.072662354 4.49561501
		 1.1396656 4.3297472 3.90099597 1.1396656 3.55734468 9.77828121 1.081413746 4.41893721 9.31930828
		 0.95765841 5.22173119 8.35870457 0.84793699 5.63698053 6.86966324 -0.9299913 5.48014069 5.39166403
		 -1.056087613 5.072660446 4.49561501 -1.1396656 4.32974529 3.90099597 -1.1396656 3.55734324 9.77828121
		 -1.081413507 4.41893578 9.31930828 -0.95765913 5.22173119 8.35870457 -0.84793699 5.63698053 6.86966324
		 2.66706657 -3.21015263 11.13594627 2.66706657 -2.87508368 11.40727806 3.87000871 -3.0071365833 10.75451565
		 3.87000871 -2.72123671 10.99777412 2.067451477 2.51730633 9.30865192 2.067451477 2.18223763 9.57998466
		 2.97412825 1.79320812 9.11628914 3.07848382 1.50730848 9.35954666 2.067451477 2.56481981 3.74212503
		 2.067451477 2.89988852 4.013456345 3.07848382 1.88989043 4.15162992 2.97412825 2.17579031 4.39488745
		 2.66706657 -3.21015263 3.76308107 2.66706657 -2.87508368 3.49174905 3.87000871 -3.0071365833 4.1445117
		 3.87000871 -2.72123671 3.90125394;
	setAttr -s 174 ".ed";
	setAttr ".ed[0:165]"  1 5 0 0 1 0 3 7 0 2 3 0 4 9 0 5 4 0 6 11 0 6 7 0 8 13 0
		 9 8 0 10 15 0 10 11 0 12 0 0 12 13 0 14 2 0 14 15 0 1 3 1 2 0 1 4 6 1 7 5 1 8 10 1
		 11 9 1 12 14 1 15 13 1 16 17 0 17 18 0 18 19 0 19 20 0 20 21 0 21 22 0 22 23 0 23 24 0
		 24 25 0 25 26 0 26 27 0 27 16 0 28 29 1 29 30 1 30 31 1 31 32 1 32 33 1 33 34 1 34 35 1
		 35 36 1 36 37 1 37 38 1 38 39 1 39 28 1 40 41 1 41 42 1 42 43 1 43 44 1 44 45 1 45 46 1
		 46 47 1 47 48 1 48 49 1 49 50 1 50 51 1 51 40 1 52 53 0 53 54 0 54 55 0 55 56 0 56 57 0
		 57 58 0 58 59 0 59 60 0 60 61 0 61 62 0 62 63 0 63 52 0 16 28 1 17 29 1 18 30 1 19 31 1
		 20 32 1 21 33 1 22 34 1 23 35 1 24 36 1 25 37 1 26 38 1 27 39 1 28 40 1 29 41 1 30 42 1
		 31 43 1 32 44 1 33 45 1 34 46 1 35 47 1 36 48 1 37 49 1 38 50 1 39 51 1 40 52 1 51 63 1
		 50 62 1 49 61 1 48 60 1 47 59 1 46 58 1 45 57 1 44 56 1 43 55 1 42 54 1 41 53 1 64 65 0
		 65 66 0 67 68 0 68 69 0 69 70 0 70 64 0 71 72 0 72 73 0 74 75 0 75 76 0 76 77 0 77 71 0
		 64 71 1 65 72 1 66 73 0 67 74 0 68 75 1 69 76 1 70 77 1 67 66 0 74 73 0 78 79 0 79 80 0
		 81 82 0 82 83 0 83 84 0 84 78 0 85 86 0 86 87 0 88 89 0 89 90 0 90 91 0 91 85 0 78 85 1
		 79 86 1 80 87 0 81 88 0 82 89 1 83 90 1 84 91 1 81 80 0 88 87 0 93 97 0 92 93 0 95 99 0
		 94 95 0 96 101 0 97 96 0 98 103 0 98 99 0 100 105 0 101 100 0 102 107 0 102 103 0
		 104 92 0 104 105 0 106 94 0 106 107 0;
	setAttr ".ed[166:173]" 93 95 1 94 92 1 96 98 1 99 97 1 100 102 1 103 101 1
		 104 106 1 107 105 1;
	setAttr -s 71 -ch 308 ".fc[0:70]" -type "polyFaces" 
		f 4 16 2 19 -1
		mu 0 4 11 21 12 22
		f 4 18 6 21 -5
		mu 0 4 13 23 14 24
		f 4 20 10 23 -9
		mu 0 4 18 25 19 26
		f 4 22 14 17 -13
		mu 0 4 15 27 16 17
		f 8 -4 -15 15 -11 11 -7 7 -3
		mu 0 8 21 5 6 7 8 9 10 12
		f 8 -14 12 1 0 5 4 9 8
		mu 0 8 0 1 20 11 22 2 3 4
		f 4 -2 -18 3 -17
		mu 0 4 11 20 5 21
		f 4 -6 -20 -8 -19
		mu 0 4 13 22 12 23
		f 4 -10 -22 -12 -21
		mu 0 4 18 24 14 25
		f 4 13 -24 -16 -23
		mu 0 4 15 26 19 27
		f 4 24 73 -37 -73
		mu 0 4 28 29 30 31
		f 4 25 74 -38 -74
		mu 0 4 29 32 33 30
		f 4 26 75 -39 -75
		mu 0 4 32 34 35 33
		f 4 27 76 -40 -76
		mu 0 4 34 36 37 35
		f 4 28 77 -41 -77
		mu 0 4 36 38 39 37
		f 4 29 78 -42 -78
		mu 0 4 38 40 41 39
		f 4 30 79 -43 -79
		mu 0 4 40 42 43 41
		f 4 31 80 -44 -80
		mu 0 4 42 44 45 43
		f 4 32 81 -45 -81
		mu 0 4 44 46 47 45
		f 4 33 82 -46 -82
		mu 0 4 46 48 49 47
		f 4 34 83 -47 -83
		mu 0 4 48 50 51 49
		f 4 35 72 -48 -84
		mu 0 4 50 52 53 51
		f 4 36 85 -49 -85
		mu 0 4 31 30 54 55
		f 4 37 86 -50 -86
		mu 0 4 30 33 56 54
		f 4 38 87 -51 -87
		mu 0 4 33 35 57 56
		f 4 39 88 -52 -88
		mu 0 4 35 37 58 57
		f 4 40 89 -53 -89
		mu 0 4 37 39 59 58
		f 4 41 90 -54 -90
		mu 0 4 39 41 60 59
		f 4 42 91 -55 -91
		mu 0 4 41 43 61 60
		f 4 43 92 -56 -92
		mu 0 4 43 45 62 61
		f 4 44 93 -57 -93
		mu 0 4 45 47 63 62
		f 4 45 94 -58 -94
		mu 0 4 47 49 64 63
		f 4 46 95 -59 -95
		mu 0 4 49 51 65 64
		f 4 47 84 -60 -96
		mu 0 4 51 53 66 65
		f 4 -97 48 107 -61
		mu 0 4 67 55 54 68
		f 4 49 106 -62 -108
		mu 0 4 54 56 69 68
		f 4 50 105 -63 -107
		mu 0 4 56 57 70 69
		f 4 51 104 -64 -106
		mu 0 4 57 58 71 70
		f 4 52 103 -65 -105
		mu 0 4 58 59 72 71
		f 4 53 102 -66 -104
		mu 0 4 59 60 73 72
		f 4 54 101 -67 -103
		mu 0 4 60 61 74 73
		f 4 55 100 -68 -102
		mu 0 4 61 62 75 74
		f 4 56 99 -69 -101
		mu 0 4 62 63 76 75
		f 4 57 98 -70 -100
		mu 0 4 63 64 77 76
		f 4 58 97 -71 -99
		mu 0 4 64 65 78 77
		f 4 59 96 -72 -98
		mu 0 4 65 66 79 78
		f 4 108 121 -115 -121
		mu 0 4 80 81 82 83
		f 4 109 122 -116 -122
		mu 0 4 81 84 85 82
		f 4 110 124 -117 -124
		mu 0 4 86 87 88 89
		f 4 111 125 -118 -125
		mu 0 4 87 90 91 88
		f 4 112 126 -119 -126
		mu 0 4 90 92 93 91
		f 4 113 120 -120 -127
		mu 0 4 92 94 95 93
		f 7 -113 -112 -111 127 -110 -109 -114
		mu 0 7 96 97 98 99 100 101 102
		f 7 -129 116 117 118 119 114 115
		mu 0 7 103 104 105 106 107 108 109
		f 4 129 142 -136 -142
		mu 0 4 110 111 112 113
		f 4 130 143 -137 -143
		mu 0 4 111 114 115 112
		f 4 131 145 -138 -145
		mu 0 4 116 117 118 119
		f 4 132 146 -139 -146
		mu 0 4 117 120 121 118
		f 4 133 147 -140 -147
		mu 0 4 120 122 123 121
		f 4 134 141 -141 -148
		mu 0 4 122 124 125 123
		f 7 -134 -133 -132 148 -131 -130 -135
		mu 0 7 126 127 128 129 130 131 132
		f 7 -150 137 138 139 140 135 136
		mu 0 7 133 134 135 136 137 138 139
		f 4 166 152 169 -151
		mu 0 4 140 141 142 143
		f 4 168 156 171 -155
		mu 0 4 144 145 146 147
		f 4 170 160 173 -159
		mu 0 4 148 149 150 151
		f 4 172 164 167 -163
		mu 0 4 152 153 154 155
		f 8 -154 -165 165 -161 161 -157 157 -153
		mu 0 8 141 156 157 158 159 160 161 142
		f 4 -152 -168 153 -167
		mu 0 4 140 162 156 141
		f 4 -156 -170 -158 -169
		mu 0 4 144 143 142 145
		f 4 -160 -172 -162 -171
		mu 0 4 148 147 146 149
		f 4 163 -174 -166 -173
		mu 0 4 152 151 150 153;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode nurbsCurve -n "JShape" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "OShape2" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "OShape1" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "RShape2" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "RShape1" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "PShape2" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "PShape1" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "JShapeOrig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 26 1 no 3
		29 0 0 1 2 3 4 4 5 6 7 8 8 8.0531242847333484 8.0531242847333484 8.3531242847333491
		 8.3531242847333491 9.3531242847333491 9.3531242847333491 10.353124284733349 11.353124284733349
		 12.353124284733349 13.353124284733349 13.353124284733349 14.804686045624475 14.804686045624475
		 15.104686045624476 15.104686045624476 16.506247043564507 16.506247043564507
		28
		3.7814189125420219 -2.2482448365274341 4.6353953193361797
		3.7954899943566129 -2.3232014685416353 4.6351810521134826
		3.8150983977701891 -2.4270995238761346 4.6655151030809003
		3.8276726558094616 -2.4929708165583171 4.7265889040948519
		3.8336766152801109 -2.5232749020280325 4.819021170780486
		3.8339052066141486 -2.5234035358897544 4.8790326286188037
		3.8341147506081814 -2.523521451353465 4.9340436403710441
		3.8286764697146727 -2.492986186618261 5.0203984603225544
		3.8185272781781103 -2.437821041748669 5.0811931140506434
		3.8036621929640759 -2.3580221394282455 5.1151785618050134
		3.7944352928450504 -2.3088704561414355 5.1153190643114064
		3.792474608952157 -2.2984258959439825 5.115348920600912
		3.7905139250592637 -2.2879813357465295 5.1153787768904184
		3.7902853325625268 -2.2878527012305283 5.0553670138118312
		3.7900567400657903 -2.2877240667145271 4.9953552507332448
		3.8195827303391252 -2.445008973229553 4.9949056440848993
		3.8191422114774811 -2.4447610826322417 4.8792574319429765
		3.8190302970186378 -2.4446981056647017 4.8498768350946451
		3.8162013237724404 -2.4304676682415365 4.8036580672976736
		3.8089290622313983 -2.3923069118742122 4.7718858312225816
		3.795831841690668 -2.3228443340325091 4.7552063345734252
		3.7855669026368783 -2.2681630188755437 4.7553626438047409
		3.7319934045953578 -1.9827770740473598 4.7561784335774657
		3.6784199065538372 -1.6973911292191757 4.7569942233501914
		3.6781913140571003 -1.6972624947031745 4.696982460271605
		3.6779627215603639 -1.6971338601871735 4.6369706971930178
		3.7296908170511927 -1.9726893483573038 4.6361830082645987
		3.7814189125420219 -2.2482448365274341 4.6353953193361797
		;
createNode nurbsCurve -n "OShape2Orig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 19 1 no 3
		22 0 0 1 2 3 4 4 5 6 7 8 8 9 10 11 12 12 13 14 15 16 16
		21
		3.8219496140590552 -2.4463408758339287 5.6162771547983494
		3.8216995918514396 -2.4462001823023156 5.5506395083225879
		3.8126279108332639 -2.3998833458304052 5.4401240737398284
		3.7961760737879287 -2.3136965373913507 5.3603542685924488
		3.7727067621509165 -2.1894923473517851 5.3157007484679291
		3.7578284293548307 -2.1102354905531437 5.3159273080948708
		3.7428347588993267 -2.0303642302133738 5.3161556240245815
		3.7198260508055654 -1.9069687331622833 5.3621420559450597
		3.7040967502027708 -1.8217380136770389 5.4417767306336486
		3.6962093707734147 -1.7777366496868128 5.5513000724364012
		3.6964522493565046 -1.7778733233284623 5.6150623226996812
		3.6966998903559447 -1.7780126768967546 5.6800748371046152
		3.7056608834966198 -1.8237171897507207 5.7918422938469369
		3.7219950016743617 -1.9092882546853258 5.870988723226259
		3.7453513591855296 -2.0328793824556421 5.9162697422049124
		3.7601143543221971 -2.1115218357131553 5.9160449388807397
		3.7749926871182828 -2.1907786925117962 5.9158183792537979
		3.7981238741705901 -2.3147926116854212 5.8717049767624943
		3.8139637500164518 -2.4006350547851518 5.7908182816294822
		3.8221972550584957 -2.4464802294022205 5.6812896692032835
		3.8219496140590552 -2.4463408758339287 5.6162771547983494
		;
createNode nurbsCurve -n "OShape1Orig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 19 1 no 3
		22 0 0 1 2 3 4 4 5 6 7 8 8 9 10 11 12 12 13 14 15 16 16
		21
		3.6816940166361878 -1.6992335499975919 5.616537390165508
		3.6813487461015577 -1.6990392579331295 5.5258944608566658
		3.6919481246785404 -1.7583042357095517 5.3713189233462151
		3.7118209855456565 -1.866197609428941 5.25911300996784
		3.7400708207174889 -2.0178188903588046 5.1961672239227914
		3.757601919680194 -2.1112070286033982 5.1959002693321592
		3.7747870056646442 -2.2027519562246063 5.195638583649834
		3.8033929730941849 -2.3540241411167133 5.256468262009153
		3.8244666867221184 -2.4642417644404619 5.3686758302661417
		3.8363530514120407 -2.5247809972470519 5.5216586297403722
		3.836705465571197 -2.5249793092014778 5.6141769552616951
		3.8370578797303527 -2.5251776211559043 5.706695280783018
		3.8264583885189372 -2.465912043376024 5.8612708200086088
		3.8064701899924027 -2.3574042661155064 5.9734784896897528
		3.7781026382783756 -2.2051672429897509 6.0358015104472811
		3.760802214634507 -2.1130079118274141 6.0360649524323753
		3.7431557780123836 -2.0190053700416923 6.0363336633257765
		3.7143143705222572 -1.8665016968321284 5.9742566229498051
		3.693584288664403 -1.7581259441684436 5.861418653713681
		3.6820440495871685 -1.6994305219886969 5.7084305836160034
		3.6816940166361878 -1.6992335499975919 5.616537390165508
		;
createNode nurbsCurve -n "RShape2Orig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 10 1 no 3
		13 0 0 0.61406271457999551 0.61406271457999551 1.6140627145799955 2.6140627145799957
		 2.6140627145799957 3.6140627145799957 3.6140627145799957 4.2703135728999779 4.2703135728999779
		 5.0703135728999777 5.0703135728999777
		12
		3.7597022371305719 -2.0948054563627778 6.7162544672965003
		3.7592343367003096 -2.0945421574958298 6.5934178468206044
		3.7587664362700468 -2.0942788586288823 6.4705812263447093
		3.7583759227800853 -2.0940591072613164 6.3680607876901538
		3.7446468362964214 -2.0225919258113385 6.2763719341262787
		3.728038551243495 -1.9341196158992302 6.276624836579618
		3.6989739116078328 -1.7792923235487175 6.2770674180168866
		3.6996501631026422 -1.779672866589157 6.4546018737290698
		3.7001502098432719 -1.7799542549609415 6.5858777771611301
		3.7006502565839017 -1.780235643332726 6.7171536805931904
		3.7301762468572366 -1.9375205498477519 6.7167040739448449
		3.7597022371305719 -2.0948054563627778 6.7162544672965003
		;
createNode nurbsCurve -n "RShape1Orig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 35 1 no 3
		38 0 0 0.29999999999999982 0.29999999999999982 0.89899452633145838 0.89899452633145838
		 1.8989945263314585 2.8989945263314585 3.8989945263314585 4.8989945263314585 4.8989945263314585
		 5.4255574316492279 5.4255574316492279 6.3255574316492282 6.3255574316492282 6.6255574316492281
		 6.6255574316492281 8.7255574316492286 8.7255574316492286 9.6661830515469926 9.6661830515469926
		 10.666183051546993 11.666183051546993 12.666183051546993 13.666183051546993 13.666183051546993
		 14.666183051546993 15.666183051546993 15.666183051546993 16.666183051546994 17.666183051546994
		 18.666183051546994 19.666183051546994 19.666183051546994 20.666183051546994 20.666183051546994
		 21.284223051269791 21.284223051269791
		37
		3.8386127854148766 -2.5260526041190876 6.1149004182276823
		3.8388413779116135 -2.5261812386350888 6.1749121813062686
		3.83906997040835 -2.52630987315109 6.234923944384855
		3.8184053889086549 -2.4154979596574497 6.275561055594375
		3.7977408074089594 -2.3046860461638099 6.3161981668038942
		3.7923605305897166 -2.2758324591106964 6.3269079565229642
		3.7833870758788817 -2.2273728959290877 6.3633037523540166
		3.7771163927063487 -2.1930727534231775 6.4127869267087458
		3.7735365750312408 -2.1729253317763586 6.4722318192330182
		3.773662776739136 -2.1729963485238262 6.5053632085063118
		3.7740640045031877 -2.1732221290720584 6.6106964362393192
		3.7744652322672394 -2.173447909620291 6.7160296639723276
		3.8076819713247412 -2.3503934294496949 6.7155238564929389
		3.8408987103822434 -2.5273389492790992 6.7150180490135503
		3.8411273028789799 -2.5274675837951004 6.7750298120921375
		3.8413558953757168 -2.5275962183111012 6.8350415751707247
		3.7638501709082122 -2.1147233387091582 6.8362217926226307
		3.6863444464407076 -1.7018504591072154 6.8374020100745367
		3.6856277132442177 -1.7014471360360361 6.6492400039180248
		3.6849109800477282 -1.7010438129648566 6.4610779977615129
		3.684780015923482 -1.7009701162907469 6.4266963443465652
		3.6850007542264089 -1.7032917954649158 6.3635515921776369
		3.686867290427303 -1.7142331450500738 6.30850957745609
		3.6907112329701355 -1.7356287332691047 6.2578130196027191
		3.6942008666087531 -1.754626405669619 6.2352544318627805
		3.7000506796825943 -1.7864917133874769 6.1964055279231864
		3.7176624401744869 -1.8810242423336476 6.1567523507454514
		3.7270046779529307 -1.930790329161586 6.1566100919362903
		3.7350782014777737 -1.9737979770371128 6.156487152457589
		3.7489031660976435 -2.0469670755754041 6.1825330923525357
		3.7596997374075345 -2.1035955171827943 6.2311312069720213
		3.767237350397644 -2.1424550934719266 6.3022843967259083
		3.7692494351952122 -2.1523793462539085 6.3460149303589555
		3.7738754774220098 -2.1786105062711134 6.258422142100315
		3.7967569394900775 -2.3013848986559116 6.209311195647933
		3.8176848624524773 -2.4137187513874996 6.1621058069378076
		3.8386127854148766 -2.5260526041190876 6.1149004182276823
		;
createNode nurbsCurve -n "PShape2Orig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 13 1 no 3
		16 0 0 0.57187609674219875 0.57187609674219875 1.5718760967421987 2.5718760967421987
		 2.5718760967421987 3.5718760967421987 4.5718760967421987 5.5718760967421987 6.5718760967421987
		 6.5718760967421987 7.1328145265888452 7.1328145265888452 7.932814526588845 7.932814526588845
		
		15
		3.7627501370870609 -2.0965205832427931 7.5164113083443249
		3.7623143818044662 -2.096275373226403 7.4020136655843247
		3.761878626521872 -2.0960301632100129 7.2876160228243254
		3.7614452536101521 -2.0957862938112228 7.1738438173754222
		3.7458494463366514 -2.0144771960367582 7.0765568743032699
		3.7306251005623112 -1.9333771286147319 7.0767887028385195
		3.7216288757621219 -1.8854542524101787 7.0769256927393736
		3.7105769619735836 -1.8259340855249384 7.1127279699494439
		3.7045726699171189 -1.7928828482425452 7.1715840022805022
		3.7026790133937282 -1.7813772737626026 7.249757658210279
		3.7028433144324295 -1.7814697299232094 7.2928911606168052
		3.7032707354864098 -1.7817102500679756 7.4051008411289097
		3.7036981565403906 -1.7819507702127413 7.517310521641015
		3.7332241468137255 -1.9392356767277672 7.5168609149926695
		3.7627501370870609 -2.0965205832427931 7.5164113083443249
		;
createNode nurbsCurve -n "PShape1Orig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		2 17 1 no 3
		20 0 0 0.8375005722133213 0.8375005722133213 1.8375005722133213 2.8375005722133215
		 3.8375005722133215 4.8375005722133215 4.8375005722133215 5.8375005722133215 6.8375005722133215
		 6.8375005722133215 7.398439002059968 7.398439002059968 8.2984390020599683 8.2984390020599683
		 8.598439002059969 8.598439002059969 10.698439002059969 10.698439002059969
		19
		3.6893923463971965 -1.7035655859872307 7.6375588511223613
		3.6887541919077944 -1.703206481051373 7.4700258980628718
		3.6881160374183923 -1.702847376115515 7.3024929450033831
		3.6878588715862506 -1.7027026626939381 7.2349799023151409
		3.6911862858455677 -1.7227080508458223 7.1092722312442813
		3.7006255540616513 -1.774726740067242 7.0134789613485848
		3.7170195350295923 -1.8630784558975555 6.9569653934818891
		3.729821902590583 -1.9312766489593447 6.9567704455896529
		3.7521970706144208 -2.0504691359278708 6.9564297279978557
		3.7760296604590664 -2.1743282511282014 7.126734719219761
		3.7766582901157673 -2.1746819962107744 7.2917671439959415
		3.7770857111697476 -2.1749225163555401 7.4039768245080468
		3.7775131322237283 -2.1751630365003063 7.5161865050201522
		3.8107298712812301 -2.3521085563297102 7.5156806975407635
		3.8439466103387323 -2.5290540761591145 7.5151748900613748
		3.8441752028354688 -2.5291827106751157 7.5751866531399621
		3.8444037953322057 -2.5293113451911164 7.6351984162185493
		3.7668980708647011 -2.1164384655891739 7.6363786336704553
		3.6893923463971965 -1.7035655859872307 7.6375588511223613
		;
createNode nurbsCurve -n "__cameraAim_cameraPROJ_lineShape" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "__cameraAim_cameraPROJ_lineShapeOrig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 10
		0 0 0
		;
createNode transform -n "__cameraAim_cameraPROJ_line_cluster_holder" -p "cameraPROJ_controller";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0.25 0.25 0.25 ;
	setAttr ".sp" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "__cameraAim_cameraPROJ_line_cluster" -p "__cameraAim_cameraPROJ_line_cluster_holder";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0 0 10 ;
	setAttr ".sp" -type "double3" 0 0 10 ;
createNode clusterHandle -n "__cameraAim_cameraPROJ_line_clusterShape" -p "__cameraAim_cameraPROJ_line_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v" no;
	setAttr ".or" -type "double3" 0 0 10 ;
createNode pointConstraint -n "__cameraAim_cameraPROJ_line_cluster_pointConstraint1" 
		-p "__cameraAim_cameraPROJ_line_cluster";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "cameras_holderW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 0 -10 ;
	setAttr -k on ".w0";
createNode nurbsCurve -n "focalCircle1PROJShape" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "focalCircle2PROJShape" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "focalCircle1ShapeOrig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1766992929027924 1.1766992929027904 -1.89227678477546e-016
		-1.8985437992126872e-016 1.6641040988579585 -2.6760834927932116e-016
		-1.1766992929027911 1.1766992929027911 -1.8922767847754612e-016
		-1.6641040988579585 4.8221573525161483e-016 -7.7546204588859417e-032
		-1.1766992929027915 -1.1766992929027908 1.8922767847754605e-016
		-5.0142704183843658e-016 -1.6641040988579587 2.6760834927932121e-016
		1.1766992929027904 -1.1766992929027913 1.8922767847754612e-016
		1.6641040988579585 -8.9379355772183028e-016 1.4373296643075375e-031
		1.1766992929027924 1.1766992929027904 -1.89227678477546e-016
		-1.8985437992126872e-016 1.6641040988579585 -2.6760834927932116e-016
		-1.1766992929027911 1.1766992929027911 -1.8922767847754612e-016
		;
createNode nurbsCurve -n "focalCircle2ShapeOrig" -p "cameraPROJ_controller";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.3751627926219696 1.3751627926219674 -2.2114304338079611e-016
		-2.218754450340375e-016 1.9447738717968477 -3.1274349117358378e-016
		-1.3751627926219683 1.3751627926219683 -2.2114304338079626e-016
		-1.9447738717968477 5.635468136459975e-016 -9.0625239517722713e-032
		-1.3751627926219685 -1.3751627926219678 2.2114304338079618e-016
		-5.8599832200942876e-016 -1.9447738717968479 3.1274349117358383e-016
		1.3751627926219674 -1.3751627926219683 2.2114304338079626e-016
		1.9447738717968477 -1.0445418402795073e-015 1.6797513918883914e-031
		1.3751627926219696 1.3751627926219674 -2.2114304338079611e-016
		-2.218754450340375e-016 1.9447738717968477 -3.1274349117358378e-016
		-1.3751627926219683 1.3751627926219683 -2.2114304338079626e-016
		;
createNode transform -n "__focalCircles_PROJ_cluster_holder" -p "cameraPROJ_controller";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0.25 0.24999999999999989 0.25 ;
	setAttr ".sp" -type "double3" 0.25 0.24999999999999989 0.25 ;
createNode transform -n "__focalCircles_PROJ_cluster" -p "__focalCircles_PROJ_cluster_holder";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0 -1.1102230246251565e-016 2.4651903288156619e-032 ;
	setAttr ".sp" -type "double3" 0 -1.1102230246251565e-016 2.4651903288156619e-032 ;
createNode clusterHandle -n "__focalCircles_PROJ_clusterShape" -p "__focalCircles_PROJ_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 -1.1102230246251565e-016 2.4651903288156619e-032 ;
createNode nurbsCurve -n "cameras_holderShape_2Orig" -p "cameras_holder";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		9.0304765228844968 6.8562850341282893 -1.1822040801876588e-015
		-1.2344654604033792e-015 9.6962512827599117 -1.671889043694198e-015
		-9.0304765228844879 6.8562850341282928 -1.1822040801876592e-015
		-12.771022373355077 2.7499062815786318e-015 -4.8447161750121495e-031
		-9.0304765228844914 -6.856285034128291 1.182204080187659e-015
		-3.3598595312868418e-015 -9.6962512827599134 1.6718890436941984e-015
		9.0304765228844861 -6.8562850341282937 1.1822040801876594e-015
		12.771022373355077 -5.2677002378931749e-015 8.9797486677973466e-031
		9.0304765228844968 6.8562850341282893 -1.1822040801876588e-015
		-1.2344654604033792e-015 9.6962512827599117 -1.671889043694198e-015
		-9.0304765228844879 6.8562850341282928 -1.1822040801876592e-015
		;
createNode nurbsCurve -n "cameras_holderShape_1Orig" -p "cameras_holder";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 82 0 no 3
		87 0 0 0 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7 8 8 8 9 9 9 10 10 10 11
		 11 11 12 12 12 13 13 13 14 14 14 15 15 15 16 16 16 17 17 17 18 18 18 19 19 19 20
		 20 20 21 21 21 22 22 22 23 23 23 24 24 24 25 25 25 26 26 26 27 27 27 28 28 28
		85
		-2.4342276327867465 -9.424138897339926 2.1215179130655614e-015
		-2.4342276327867465 -9.424138897339926 2.1215179130655614e-015
		-1.8674595519542403 -11.514819007329987 2.6443726827843559e-015
		-1.8674595519542403 -11.514819007329987 2.6443726827843559e-015
		-1.8674595519542403 -11.514819007329987 2.6443726827843559e-015
		-3.3849613593345116 -11.514819007329987 2.6443726827843559e-015
		-3.3849613593345116 -11.514819007329987 2.6443726827843559e-015
		-3.3849613593345116 -11.514819007329987 2.6443726827843559e-015
		4.9354637037025843e-017 -15.467782402621523 3.8594483131688562e-015
		4.9354637037025843e-017 -15.467782402621523 3.8594483131688562e-015
		4.9354637037025843e-017 -15.467782402621523 3.8594483131688562e-015
		3.3849613593345116 -11.514819007329987 2.6443726827843559e-015
		3.3849613593345116 -11.514819007329987 2.6443726827843559e-015
		3.3849613593345116 -11.514819007329987 2.6443726827843559e-015
		1.8674595519542403 -11.514819007329987 2.6443726827843559e-015
		1.8674595519542403 -11.514819007329987 2.6443726827843559e-015
		1.8674595519542403 -11.514819007329987 2.6443726827843559e-015
		2.4342276327867465 -9.424138897339926 2.1215179130655614e-015
		2.4342276327867465 -9.424138897339926 2.1215179130655614e-015
		2.4342276327867465 -9.424138897339926 2.1215179130655614e-015
		9.4570454784302775 -8.0516482201335133 1.8181944308646397e-015
		11.638062675522393 -3.4473989166478742 7.0717263768852043e-016
		11.638062675522393 -3.4473989166478742 7.0717263768852043e-016
		14.656805215476588 -2.0761361105245011 4.6099482243200398e-016
		14.656805215476588 -2.0761361105245011 4.6099482243200398e-016
		14.656805215476588 -2.0761361105245011 4.6099482243200398e-016
		14.656805215476588 -3.7322224837500069 9.2198964486400776e-016
		14.656805215476588 -3.7322224837500069 9.2198964486400776e-016
		14.656805215476588 -3.7322224837500069 9.2198964486400776e-016
		20.216322453068528 2.6240710531185599e-015 -5.8266082028492148e-031
		20.216322453068528 2.6240710531185599e-015 -5.8266082028492148e-031
		20.216322453068528 2.6240710531185599e-015 -5.8266082028492148e-031
		14.656805215476588 3.7322224837500033 -9.2198964486400697e-016
		14.656805215476588 3.7322224837500033 -9.2198964486400697e-016
		14.656805215476588 3.7322224837500033 -9.2198964486400697e-016
		14.656805215476588 2.0761361105244989 -4.6099482243200349e-016
		14.656805215476588 2.0761361105244989 -4.6099482243200349e-016
		14.656805215476588 2.0761361105244989 -4.6099482243200349e-016
		11.638062675522393 3.4473989166478742 -7.0717263768852043e-016
		11.638062675522393 3.4473989166478742 -7.0717263768852043e-016
		9.4570454784302775 8.0516482201335187 -1.8181944308646409e-015
		2.4342276327867465 9.424138897339926 -2.1215179130655614e-015
		2.4342276327867465 9.424138897339926 -2.1215179130655614e-015
		2.4342276327867465 9.424138897339926 -2.1215179130655614e-015
		1.8674595519542403 11.514819007329987 -2.6443726827843559e-015
		1.8674595519542403 11.514819007329987 -2.6443726827843559e-015
		1.8674595519542403 11.514819007329987 -2.6443726827843559e-015
		3.384961359334512 11.514819007329987 -2.6443726827843559e-015
		3.384961359334512 11.514819007329987 -2.6443726827843559e-015
		3.384961359334512 11.514819007329987 -2.6443726827843559e-015
		4.9354637037025843e-017 15.467782402621539 -3.8594483131688601e-015
		4.9354637037025843e-017 15.467782402621539 -3.8594483131688601e-015
		4.9354637037025843e-017 15.467782402621539 -3.8594483131688601e-015
		-3.3849613593345107 11.514819007329987 -2.6443726827843559e-015
		-3.3849613593345107 11.514819007329987 -2.6443726827843559e-015
		-3.3849613593345107 11.514819007329987 -2.6443726827843559e-015
		-1.8674595519542403 11.514819007329987 -2.6443726827843559e-015
		-1.8674595519542403 11.514819007329987 -2.6443726827843559e-015
		-1.8674595519542403 11.514819007329987 -2.6443726827843559e-015
		-2.4342276327867465 9.424138897339926 -2.1215179130655614e-015
		-2.4342276327867465 9.424138897339926 -2.1215179130655614e-015
		-2.4342276327867465 9.424138897339926 -2.1215179130655614e-015
		-9.4570454784302775 8.0516482201335187 -1.8181944308646409e-015
		-11.638062675522393 3.4473989166478742 -7.0717263768852043e-016
		-11.638062675522393 3.4473989166478742 -7.0717263768852043e-016
		-14.656805215476588 2.0761361105244989 -4.6099482243200349e-016
		-14.656805215476588 2.0761361105244989 -4.6099482243200349e-016
		-14.656805215476588 2.0761361105244989 -4.6099482243200349e-016
		-14.656805215476588 3.7322224837500033 -9.2198964486400697e-016
		-14.656805215476588 3.7322224837500033 -9.2198964486400697e-016
		-14.656805215476588 3.7322224837500033 -9.2198964486400697e-016
		-20.216322453068528 2.6240710531185599e-015 -5.8266082028492148e-031
		-20.216322453068528 2.6240710531185599e-015 -5.8266082028492148e-031
		-20.216322453068528 2.6240710531185599e-015 -5.8266082028492148e-031
		-14.656805215476588 -3.7322224837500069 9.2198964486400776e-016
		-14.656805215476588 -3.7322224837500069 9.2198964486400776e-016
		-14.656805215476588 -3.7322224837500069 9.2198964486400776e-016
		-14.656805215476588 -2.0761361105245011 4.6099482243200398e-016
		-14.656805215476588 -2.0761361105245011 4.6099482243200398e-016
		-14.656805215476588 -2.0761361105245011 4.6099482243200398e-016
		-11.638062675522393 -3.4473989166478742 7.0717263768852043e-016
		-11.638062675522393 -3.4473989166478742 7.0717263768852043e-016
		-9.4570454784302775 -8.0516482201335133 1.8181944308646397e-015
		-2.4342276327867465 -9.424138897339926 2.1215179130655614e-015
		-2.4342276327867465 -9.424138897339926 2.1215179130655614e-015
		;
createNode transform -n "cameraPROJ_roller" -p "cameras_holder";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "cameraPROJ" -p "cameraPROJ_roller";
	setAttr ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode camera -n "cameraPROJShape" -p "cameraPROJ";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.7777777777777699 1 ;
	setAttr -l on ".psc";
	setAttr -l on ".ct";
	setAttr -l on ".frp";
	setAttr -l on ".frv";
	setAttr -l on ".ptsc";
	setAttr ".ff" 3;
	setAttr -l on ".ffo";
	setAttr ".ncp" 1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
	setAttr ".dgo" 1;
	setAttr ".dgc" -type "float3" 0 0 0 ;
createNode nurbsCurve -n "camera_globalShapeOrig" -p "camera_global";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		5.4540025537360854 15.493791955194576 -3.0282908366375916e-015
		5.1453503875491715e-015 20.117515330938538 -3.9320062841151257e-015
		-5.4540025537360943 15.493791955194576 -3.0282908366375916e-015
		-9.7751794459281687 9.7751794459281651 -1.5719687471650597e-015
		-18.83121811166907 6.385417028698547 -9.4022621363486081e-016
		-24.450910413492281 -1.1278614624225602e-015 1.8137395634191338e-031
		-18.831218111669063 -6.3854170286985479 9.402262136348612e-016
		-9.7751794459281687 -9.7751794459281722 1.5719687471650609e-015
		-5.4540025537360926 -15.493791955194583 3.0282908366375932e-015
		1.5770625363874974e-015 -20.117515330938538 3.9320062841151257e-015
		5.4540025537360961 -15.493791955194576 3.0282908366375916e-015
		9.7751794459281651 -9.7751794459281651 1.5719687471650601e-015
		18.831218111669077 -6.3854170286985426 9.4022621363486041e-016
		24.45091041349227 4.2005443074541867e-015 -6.7549904417873383e-031
		18.83121811166907 6.3854170286985523 -9.4022621363486179e-016
		9.7751794459281633 9.7751794459281687 -1.5719687471650605e-015
		5.4540025537360854 15.493791955194576 -3.0282908366375916e-015
		5.1453503875491715e-015 20.117515330938538 -3.9320062841151257e-015
		-5.4540025537360943 15.493791955194576 -3.0282908366375916e-015
		;
createNode transform -n "camera_aim" -p "camera_global";
	setAttr -l on -k off ".v";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "camera_aim_circleShape_1" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "camera_aim_crossShape_1" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "camera_aim_crossShape_2" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "camera_aim_circleShape_3" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "camera_aim_circleShape_2" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "camera_aim_circleShape_1Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.8837168980137067 3.5667429376609068 -7.1959247622513163e-016
		-7.8796260775862392e-016 5.0441362359385122 -1.0176574392592209e-015
		-4.8837168980137022 3.5667429376609077 -7.1959247622513182e-016
		-6.9066186719616391 1.7280552465237047e-015 -2.2068293309346718e-031
		-4.883716898013704 -3.5667429376609068 7.1959247622513172e-016
		-2.0810989962494157e-015 -5.0441362359385122 1.0176574392592211e-015
		4.8837168980137005 -3.5667429376609081 7.1959247622513192e-016
		6.9066186719616391 -2.4428246524193982e-015 6.2079452883048853e-031
		4.8837168980137067 3.5667429376609068 -7.1959247622513163e-016
		-7.8796260775862392e-016 5.0441362359385122 -1.0176574392592209e-015
		-4.8837168980137022 3.5667429376609077 -7.1959247622513182e-016
		;
createNode nurbsCurve -n "camera_aim_crossShape_1Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		6.2878082338675725 -7.0485897883296378e-016 -5.2845452833070624e-016
		-6.2878082338675725 1.3344866606488197e-015 -5.2845452833070723e-016
		;
createNode nurbsCurve -n "camera_aim_crossShape_2Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 -4.6101281456295222 1.2842478815289644e-015
		0 4.6101281456295222 -1.2842478815289646e-015
		;
createNode nurbsCurve -n "camera_aim_circleShape_3Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.7612923613709448 4.9379995366211231 -2.4724002062947354
		-1.0908997536387017e-015 6.9833859156816596 -2.4724002062947359
		-6.7612923613709377 4.9379995366211267 -2.4724002062947354
		-9.5619113566203939 2.2900012875169131e-015 -2.4724002062947346
		-6.7612923613709395 -4.937999536621124 -2.4724002062947337
		-2.881190503143373e-015 -6.9833859156816596 -2.4724002062947332
		6.7612923613709324 -4.9379995366211267 -2.4724002062947337
		9.5619113566203939 -3.4843994383706256e-015 -2.4724002062947346
		6.7612923613709448 4.9379995366211231 -2.4724002062947354
		-1.0908997536387017e-015 6.9833859156816596 -2.4724002062947359
		-6.7612923613709377 4.9379995366211267 -2.4724002062947354
		;
createNode nurbsCurve -n "camera_aim_circleShape_2Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		5.9054690874060443 4.3129629749109899 -1.2968705911388803
		-9.5281706931926876e-016 6.0994507331321408 -1.2968705911388807
		-5.9054690874060345 4.3129629749109952 -1.2968705911388803
		-8.3515944755846832 2.0338589859262778e-015 -1.2968705911388794
		-5.9054690874060363 -4.3129629749109908 -1.2968705911388785
		-2.5164984061998291e-015 -6.0994507331321426 -1.296870591138878
		5.9054690874060265 -4.3129629749109961 -1.2968705911388785
		8.3515944755846832 -3.0096361275004572e-015 -1.2968705911388794
		5.9054690874060443 4.3129629749109899 -1.2968705911388803
		-9.5281706931926876e-016 6.0994507331321408 -1.2968705911388807
		-5.9054690874060345 4.3129629749109952 -1.2968705911388803
		;
createNode orientConstraint -n "camera_aim_orientConstraint" -p "camera_aim";
	addAttr -dcb 0 -ci true -sn "w0" -ln "cameras_holderW0" -dv 1 -min 0 -at "double";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k off ".ox";
	setAttr -k off ".oy";
	setAttr -k off ".oz";
	setAttr -k off ".int";
createNode nurbsCurve -n "__cameraAim_camerasHolder_lineShape" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr -av ".iog[0].og[4].gco";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode transform -n "__cameraAim_camerasHolder_line_cluster" -p "camera_aim";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0 0 -10 ;
	setAttr ".sp" -type "double3" 0 0 -10 ;
createNode clusterHandle -n "__cameraAim_camerasHolder_line_clusterShape" -p "__cameraAim_camerasHolder_line_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v" no;
	setAttr ".or" -type "double3" 0 0 -10 ;
createNode pointConstraint -n "cluster1Handle_pointConstraint1" -p "__cameraAim_camerasHolder_line_cluster";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "cameras_holderW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 0 10 ;
	setAttr -k on ".w0";
createNode nurbsCurve -n "__cameraAim_camerasHolder_lineShape5Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 0
		0 0 -10
		;
createNode transform -n "__internals" -p "camera_rig";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "plate_controller" -p "__internals";
	addAttr -ci true -sn "showResizingArrows" -ln "showResizingArrows" -min 0 -max 
		1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "ROTATION_OFFSET" -ln "ROTATION_OFFSET" -min 0 -max 0 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "rotX" -ln "rotX" -at "double";
	addAttr -ci true -sn "rotY" -ln "rotY" -at "double";
	addAttr -ci true -sn "rotZ" -ln "rotZ" -at "double";
	addAttr -ci true -sn "PLATE_OPTIONS" -ln "PLATE_OPTIONS" -min 0 -max 0 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "showPlate" -ln "showPlate" -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "showPivot" -ln "showPivot" -min 0 -max 1 -en "OFF:ON" -at "enum";
	setAttr -cb on ".ROTATION_OFFSET";
	setAttr -k on ".rotX";
	setAttr -k on ".rotY";
	setAttr -k on ".rotZ";
	setAttr -cb on ".PLATE_OPTIONS";
	setAttr -k on ".showPlate" 1;
	setAttr -k on ".showPivot";
createNode nurbsCurve -n "plate_controllerShape_0" -p "plate_controller";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		11.060845530016065 13.184885057749252 2.7136728028332193
		1.038962099152745e-014 13.636247074798371 2.7136728028332184
		-11.060845530016083 13.184885057749252 2.7136728028332193
		-16.838184947844173 11.011689897414053 5.4268933126021155
		-19.484580063829927 6.6722851379577106 9.9874653104909203
		-19.94500651631834 -6.4615596053190866e-016 11.642626881067983
		-19.484580063829913 -6.6722851379577106 9.9874653104909221
		-16.838184947844173 -11.011689897414058 5.4268933126021199
		-11.060845530016083 -13.184885057749252 2.7136728028332247
		6.6309392439080916e-015 -13.636247074798371 2.7136728028332251
		11.060845530016088 -13.184885057749252 2.7136728028332247
		16.838184947844173 -11.011689897414051 5.4268933126021199
		19.484580063829934 -6.6722851379577071 9.9874653104909221
		19.945006516318319 2.4065072104777758e-015 11.642626881067983
		19.484580063829927 6.6722851379577115 9.9874653104909203
		16.838184947844169 11.011689897414053 5.4268933126021155
		11.060845530016065 13.184885057749252 2.7136728028332193
		1.038962099152745e-014 13.636247074798371 2.7136728028332184
		-11.060845530016083 13.184885057749252 2.7136728028332193
		;
createNode nurbsCurve -n "plate_controllerShape_1" -p "plate_controller";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		11.936766142264856 14.229010713502518 2.7136728028332184
		1.0826557830156371e-014 14.716116588762709 2.7136728028332184
		-11.936766142264879 14.229010713502518 2.7136728028332184
		-18.171619469522408 11.883717820655704 5.4268933126021155
		-21.027585546783776 7.2006707905082594 9.9874653104909203
		-21.524473680168533 -6.973257669469246e-016 11.642626881067983
		-21.027585546783758 -7.2006707905082612 9.9874653104909221
		-18.171619469522408 -11.883717820655709 5.4268933126021199
		-11.936766142264878 -14.229010713502522 2.7136728028332251
		6.7702219105581414e-015 -14.716116588762709 2.7136728028332251
		11.936766142264881 -14.229010713502518 2.7136728028332251
		18.171619469522405 -11.883717820655704 5.4268933126021199
		21.027585546783779 -7.200670790508255 9.9874653104909221
		21.524473680168519 2.5970811827353694e-015 11.642626881067983
		21.027585546783776 7.2006707905082621 9.9874653104909203
		18.171619469522405 11.883717820655709 5.4268933126021155
		11.936766142264856 14.229010713502518 2.7136728028332184
		1.0826557830156371e-014 14.716116588762709 2.7136728028332184
		-11.936766142264879 14.229010713502518 2.7136728028332184
		;
createNode transform -n "plate_pivot" -p "__internals";
createNode nurbsCurve -n "plate_pivotShape_0" -p "plate_pivot";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.2187347930125085 4.2187347930125014 5.8159335252307329
		-6.8067116468118607e-016 5.9661919603335365 5.8159335252307329
		-4.2187347930125041 4.2187347930125041 5.8159335252307329
		-5.9661919603335365 1.7288531677669272e-015 5.8159335252307338
		-4.2187347930125059 -4.2187347930125032 5.8159335252307347
		-1.7977300745568685e-015 -5.9661919603335383 5.8159335252307347
		4.2187347930125014 -4.218734793012505 5.8159335252307347
		5.9661919603335365 -3.2044533403514309e-015 5.8159335252307338
		4.2187347930125085 4.2187347930125014 5.8159335252307329
		-6.8067116468118607e-016 5.9661919603335365 5.8159335252307329
		-4.2187347930125041 4.2187347930125041 5.8159335252307329
		;
createNode nurbsCurve -n "plate_pivotShape_1" -p "plate_pivot";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.3989203666467023 3.3989203666466969 5.8159335252307329
		-5.4839832275210654e-016 4.8067992799378958 5.8159335252307329
		-3.3989203666466992 3.3989203666466992 5.8159335252307329
		-4.8067992799378958 1.3928901747029669e-015 5.8159335252307338
		-3.3989203666467005 -3.3989203666466983 5.8159335252307347
		-1.4483824331089017e-015 -4.8067992799378967 5.8159335252307347
		3.3989203666466969 -3.3989203666466996 5.8159335252307347
		4.8067992799378958 -2.5817412700436707e-015 5.8159335252307338
		3.3989203666467023 3.3989203666466969 5.8159335252307329
		-5.4839832275210654e-016 4.8067992799378958 5.8159335252307329
		-3.3989203666466992 3.3989203666466992 5.8159335252307329
		;
createNode nurbsCurve -n "plate_pivotShape_2" -p "plate_pivot";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.8019862240500504 3.8019862240500442 5.8159335252307329
		-6.1343092614219695e-016 5.3768204820072496 5.8159335252307329
		-3.8019862240500464 3.8019862240500464 5.8159335252307329
		-5.3768204820072496 1.558068058258162e-015 5.8159335252307338
		-3.8019862240500482 -3.8019862240500459 5.8159335252307347
		-1.6201409458936376e-015 -5.3768204820072514 5.8159335252307347
		3.8019862240500442 -3.8019862240500473 5.8159335252307347
		5.3768204820072496 -2.8879007696351259e-015 5.8159335252307338
		3.8019862240500504 3.8019862240500442 5.8159335252307329
		-6.1343092614219695e-016 5.3768204820072496 5.8159335252307329
		-3.8019862240500464 3.8019862240500464 5.8159335252307329
		;
createNode joint -n "__controllersVisualScaler" -p "__internals";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -cb off ".radi" 6.68;
createNode transform -n "__2dCameraMovementsData" -p "__internals";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
createNode transform -n "__upLocator" -p "__internals";
	setAttr -l on -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "__upLocatorShape" -p "__upLocator";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode parentConstraint -n "__upLocator_parentConstraint" -p "__upLocator";
	addAttr -dcb 0 -ci true -sn "w0" -ln "camera_globalW0" -dv 1 -min 0 -at "double";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 40 0 ;
	setAttr ".rst" -type "double3" 0 40 0 ;
	setAttr -k off ".int";
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
	setAttr ".cdl" 1;
	setAttr -s 2 ".dli[1]"  1;
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode skinCluster -n "skinCluster1";
	setAttr -s 108 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".wl[19].w[0]"  1;
	setAttr ".wl[20].w[0]"  1;
	setAttr ".wl[21].w[0]"  1;
	setAttr ".wl[22].w[0]"  1;
	setAttr ".wl[23].w[0]"  1;
	setAttr ".wl[24].w[0]"  1;
	setAttr ".wl[25].w[0]"  1;
	setAttr ".wl[26].w[0]"  1;
	setAttr ".wl[27].w[0]"  1;
	setAttr ".wl[28].w[0]"  1;
	setAttr ".wl[29].w[0]"  1;
	setAttr ".wl[30].w[0]"  1;
	setAttr ".wl[31].w[0]"  1;
	setAttr ".wl[32].w[0]"  1;
	setAttr ".wl[33].w[0]"  1;
	setAttr ".wl[34].w[0]"  1;
	setAttr ".wl[35].w[0]"  1;
	setAttr ".wl[36].w[0]"  1;
	setAttr ".wl[37].w[0]"  1;
	setAttr ".wl[38].w[0]"  1;
	setAttr ".wl[39].w[0]"  1;
	setAttr ".wl[40].w[0]"  1;
	setAttr ".wl[41].w[0]"  1;
	setAttr ".wl[42].w[0]"  1;
	setAttr ".wl[43].w[0]"  1;
	setAttr ".wl[44].w[0]"  1;
	setAttr ".wl[45].w[0]"  1;
	setAttr ".wl[46].w[0]"  1;
	setAttr ".wl[47].w[0]"  1;
	setAttr ".wl[48].w[0]"  1;
	setAttr ".wl[49].w[0]"  1;
	setAttr ".wl[50].w[0]"  1;
	setAttr ".wl[51].w[0]"  1;
	setAttr ".wl[52].w[0]"  1;
	setAttr ".wl[53].w[0]"  1;
	setAttr ".wl[54].w[0]"  1;
	setAttr ".wl[55].w[0]"  1;
	setAttr ".wl[56].w[0]"  1;
	setAttr ".wl[57].w[0]"  1;
	setAttr ".wl[58].w[0]"  1;
	setAttr ".wl[59].w[0]"  1;
	setAttr ".wl[60].w[0]"  1;
	setAttr ".wl[61].w[0]"  1;
	setAttr ".wl[62].w[0]"  1;
	setAttr ".wl[63].w[0]"  1;
	setAttr ".wl[64].w[0]"  1;
	setAttr ".wl[65].w[0]"  1;
	setAttr ".wl[66].w[0]"  1;
	setAttr ".wl[67].w[0]"  1;
	setAttr ".wl[68].w[0]"  1;
	setAttr ".wl[69].w[0]"  1;
	setAttr ".wl[70].w[0]"  1;
	setAttr ".wl[71].w[0]"  1;
	setAttr ".wl[72].w[0]"  1;
	setAttr ".wl[73].w[0]"  1;
	setAttr ".wl[74].w[0]"  1;
	setAttr ".wl[75].w[0]"  1;
	setAttr ".wl[76].w[0]"  1;
	setAttr ".wl[77].w[0]"  1;
	setAttr ".wl[78].w[0]"  1;
	setAttr ".wl[79].w[0]"  1;
	setAttr ".wl[80].w[0]"  1;
	setAttr ".wl[81].w[0]"  1;
	setAttr ".wl[82].w[0]"  1;
	setAttr ".wl[83].w[0]"  1;
	setAttr ".wl[84].w[0]"  1;
	setAttr ".wl[85].w[0]"  1;
	setAttr ".wl[86].w[0]"  1;
	setAttr ".wl[87].w[0]"  1;
	setAttr ".wl[88].w[0]"  1;
	setAttr ".wl[89].w[0]"  1;
	setAttr ".wl[90].w[0]"  1;
	setAttr ".wl[91].w[0]"  1;
	setAttr ".wl[92].w[0]"  1;
	setAttr ".wl[93].w[0]"  1;
	setAttr ".wl[94].w[0]"  1;
	setAttr ".wl[95].w[0]"  1;
	setAttr ".wl[96].w[0]"  1;
	setAttr ".wl[97].w[0]"  1;
	setAttr ".wl[98].w[0]"  1;
	setAttr ".wl[99].w[0]"  1;
	setAttr ".wl[100].w[0]"  1;
	setAttr ".wl[101].w[0]"  1;
	setAttr ".wl[102].w[0]"  1;
	setAttr ".wl[103].w[0]"  1;
	setAttr ".wl[104].w[0]"  1;
	setAttr ".wl[105].w[0]"  1;
	setAttr ".wl[106].w[0]"  1;
	setAttr ".wl[107].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak15";
createNode objectSet -n "skinCluster1Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet15";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId30";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts30";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode dagPose -n "bindPose1";
	setAttr -s 4 ".wm";
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".wm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 4 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 3 ".m";
	setAttr -s 3 ".p";
	setAttr -s 3 ".g[1:3]" yes yes yes;
	setAttr ".bp" yes;
createNode skinCluster -n "skinCluster3";
	setAttr -s 108 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".wl[19].w[0]"  1;
	setAttr ".wl[20].w[0]"  1;
	setAttr ".wl[21].w[0]"  1;
	setAttr ".wl[22].w[0]"  1;
	setAttr ".wl[23].w[0]"  1;
	setAttr ".wl[24].w[0]"  1;
	setAttr ".wl[25].w[0]"  1;
	setAttr ".wl[26].w[0]"  1;
	setAttr ".wl[27].w[0]"  1;
	setAttr ".wl[28].w[0]"  1;
	setAttr ".wl[29].w[0]"  1;
	setAttr ".wl[30].w[0]"  1;
	setAttr ".wl[31].w[0]"  1;
	setAttr ".wl[32].w[0]"  1;
	setAttr ".wl[33].w[0]"  1;
	setAttr ".wl[34].w[0]"  1;
	setAttr ".wl[35].w[0]"  1;
	setAttr ".wl[36].w[0]"  1;
	setAttr ".wl[37].w[0]"  1;
	setAttr ".wl[38].w[0]"  1;
	setAttr ".wl[39].w[0]"  1;
	setAttr ".wl[40].w[0]"  1;
	setAttr ".wl[41].w[0]"  1;
	setAttr ".wl[42].w[0]"  1;
	setAttr ".wl[43].w[0]"  1;
	setAttr ".wl[44].w[0]"  1;
	setAttr ".wl[45].w[0]"  1;
	setAttr ".wl[46].w[0]"  1;
	setAttr ".wl[47].w[0]"  1;
	setAttr ".wl[48].w[0]"  1;
	setAttr ".wl[49].w[0]"  1;
	setAttr ".wl[50].w[0]"  1;
	setAttr ".wl[51].w[0]"  1;
	setAttr ".wl[52].w[0]"  1;
	setAttr ".wl[53].w[0]"  1;
	setAttr ".wl[54].w[0]"  1;
	setAttr ".wl[55].w[0]"  1;
	setAttr ".wl[56].w[0]"  1;
	setAttr ".wl[57].w[0]"  1;
	setAttr ".wl[58].w[0]"  1;
	setAttr ".wl[59].w[0]"  1;
	setAttr ".wl[60].w[0]"  1;
	setAttr ".wl[61].w[0]"  1;
	setAttr ".wl[62].w[0]"  1;
	setAttr ".wl[63].w[0]"  1;
	setAttr ".wl[64].w[0]"  1;
	setAttr ".wl[65].w[0]"  1;
	setAttr ".wl[66].w[0]"  1;
	setAttr ".wl[67].w[0]"  1;
	setAttr ".wl[68].w[0]"  1;
	setAttr ".wl[69].w[0]"  1;
	setAttr ".wl[70].w[0]"  1;
	setAttr ".wl[71].w[0]"  1;
	setAttr ".wl[72].w[0]"  1;
	setAttr ".wl[73].w[0]"  1;
	setAttr ".wl[74].w[0]"  1;
	setAttr ".wl[75].w[0]"  1;
	setAttr ".wl[76].w[0]"  1;
	setAttr ".wl[77].w[0]"  1;
	setAttr ".wl[78].w[0]"  1;
	setAttr ".wl[79].w[0]"  1;
	setAttr ".wl[80].w[0]"  1;
	setAttr ".wl[81].w[0]"  1;
	setAttr ".wl[82].w[0]"  1;
	setAttr ".wl[83].w[0]"  1;
	setAttr ".wl[84].w[0]"  1;
	setAttr ".wl[85].w[0]"  1;
	setAttr ".wl[86].w[0]"  1;
	setAttr ".wl[87].w[0]"  1;
	setAttr ".wl[88].w[0]"  1;
	setAttr ".wl[89].w[0]"  1;
	setAttr ".wl[90].w[0]"  1;
	setAttr ".wl[91].w[0]"  1;
	setAttr ".wl[92].w[0]"  1;
	setAttr ".wl[93].w[0]"  1;
	setAttr ".wl[94].w[0]"  1;
	setAttr ".wl[95].w[0]"  1;
	setAttr ".wl[96].w[0]"  1;
	setAttr ".wl[97].w[0]"  1;
	setAttr ".wl[98].w[0]"  1;
	setAttr ".wl[99].w[0]"  1;
	setAttr ".wl[100].w[0]"  1;
	setAttr ".wl[101].w[0]"  1;
	setAttr ".wl[102].w[0]"  1;
	setAttr ".wl[103].w[0]"  1;
	setAttr ".wl[104].w[0]"  1;
	setAttr ".wl[105].w[0]"  1;
	setAttr ".wl[106].w[0]"  1;
	setAttr ".wl[107].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak17";
createNode objectSet -n "skinCluster3Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster3GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster3GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet17";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId34";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts34";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode skinCluster -n "skinCluster4";
	setAttr -s 16 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak18";
createNode objectSet -n "skinCluster4Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster4GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster4GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet18";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId36";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts36";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster5";
	setAttr -s 8 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak19";
createNode objectSet -n "skinCluster5Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster5GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster5GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet19";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId38";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts38";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster6";
	setAttr -s 85 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".wl[19].w[0]"  1;
	setAttr ".wl[20].w[0]"  1;
	setAttr ".wl[21].w[0]"  1;
	setAttr ".wl[22].w[0]"  1;
	setAttr ".wl[23].w[0]"  1;
	setAttr ".wl[24].w[0]"  1;
	setAttr ".wl[25].w[0]"  1;
	setAttr ".wl[26].w[0]"  1;
	setAttr ".wl[27].w[0]"  1;
	setAttr ".wl[28].w[0]"  1;
	setAttr ".wl[29].w[0]"  1;
	setAttr ".wl[30].w[0]"  1;
	setAttr ".wl[31].w[0]"  1;
	setAttr ".wl[32].w[0]"  1;
	setAttr ".wl[33].w[0]"  1;
	setAttr ".wl[34].w[0]"  1;
	setAttr ".wl[35].w[0]"  1;
	setAttr ".wl[36].w[0]"  1;
	setAttr ".wl[37].w[0]"  1;
	setAttr ".wl[38].w[0]"  1;
	setAttr ".wl[39].w[0]"  1;
	setAttr ".wl[40].w[0]"  1;
	setAttr ".wl[41].w[0]"  1;
	setAttr ".wl[42].w[0]"  1;
	setAttr ".wl[43].w[0]"  1;
	setAttr ".wl[44].w[0]"  1;
	setAttr ".wl[45].w[0]"  1;
	setAttr ".wl[46].w[0]"  1;
	setAttr ".wl[47].w[0]"  1;
	setAttr ".wl[48].w[0]"  1;
	setAttr ".wl[49].w[0]"  1;
	setAttr ".wl[50].w[0]"  1;
	setAttr ".wl[51].w[0]"  1;
	setAttr ".wl[52].w[0]"  1;
	setAttr ".wl[53].w[0]"  1;
	setAttr ".wl[54].w[0]"  1;
	setAttr ".wl[55].w[0]"  1;
	setAttr ".wl[56].w[0]"  1;
	setAttr ".wl[57].w[0]"  1;
	setAttr ".wl[58].w[0]"  1;
	setAttr ".wl[59].w[0]"  1;
	setAttr ".wl[60].w[0]"  1;
	setAttr ".wl[61].w[0]"  1;
	setAttr ".wl[62].w[0]"  1;
	setAttr ".wl[63].w[0]"  1;
	setAttr ".wl[64].w[0]"  1;
	setAttr ".wl[65].w[0]"  1;
	setAttr ".wl[66].w[0]"  1;
	setAttr ".wl[67].w[0]"  1;
	setAttr ".wl[68].w[0]"  1;
	setAttr ".wl[69].w[0]"  1;
	setAttr ".wl[70].w[0]"  1;
	setAttr ".wl[71].w[0]"  1;
	setAttr ".wl[72].w[0]"  1;
	setAttr ".wl[73].w[0]"  1;
	setAttr ".wl[74].w[0]"  1;
	setAttr ".wl[75].w[0]"  1;
	setAttr ".wl[76].w[0]"  1;
	setAttr ".wl[77].w[0]"  1;
	setAttr ".wl[78].w[0]"  1;
	setAttr ".wl[79].w[0]"  1;
	setAttr ".wl[80].w[0]"  1;
	setAttr ".wl[81].w[0]"  1;
	setAttr ".wl[82].w[0]"  1;
	setAttr ".wl[83].w[0]"  1;
	setAttr ".wl[84].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak20";
createNode objectSet -n "skinCluster6Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster6GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster6GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet20";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId40";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts40";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster7";
	setAttr -s 8 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak21";
createNode objectSet -n "skinCluster7Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster7GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster7GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet21";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId42";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts42";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster8";
	setAttr -s 2 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak22";
createNode objectSet -n "skinCluster8Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster8GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster8GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet22";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId44";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts44";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster9";
	setAttr -s 2 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak23";
createNode objectSet -n "skinCluster9Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster9GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster9GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet23";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId46";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts46";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster10";
	setAttr -s 8 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak24";
createNode objectSet -n "skinCluster10Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster10GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster10GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet24";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId48";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts48";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster11";
	setAttr -s 8 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak25";
createNode objectSet -n "skinCluster11Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster11GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster11GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet25";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId50";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts50";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode condition -n "isCameraPROJ";
	setAttr ".st" 1;
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 1 1 ;
createNode condition -n "isCameraHD";
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 1 1 ;
createNode skinCluster -n "skinCluster12";
	setAttr -s 28 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".wl[19].w[0]"  1;
	setAttr ".wl[20].w[0]"  1;
	setAttr ".wl[21].w[0]"  1;
	setAttr ".wl[22].w[0]"  1;
	setAttr ".wl[23].w[0]"  1;
	setAttr ".wl[24].w[0]"  1;
	setAttr ".wl[25].w[0]"  1;
	setAttr ".wl[26].w[0]"  1;
	setAttr ".wl[27].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak26";
createNode objectSet -n "skinCluster12Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster12GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster12GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet26";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId52";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts52";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster13";
	setAttr -s 21 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".wl[19].w[0]"  1;
	setAttr ".wl[20].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak27";
createNode objectSet -n "skinCluster13Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster13GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster13GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet27";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId54";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts54";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster14";
	setAttr -s 21 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".wl[19].w[0]"  1;
	setAttr ".wl[20].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak28";
createNode objectSet -n "skinCluster14Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster14GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster14GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet28";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId56";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts56";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster15";
	setAttr -s 12 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak29";
createNode objectSet -n "skinCluster15Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster15GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster15GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet29";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId58";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts58";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster16";
	setAttr -s 37 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".wl[19].w[0]"  1;
	setAttr ".wl[20].w[0]"  1;
	setAttr ".wl[21].w[0]"  1;
	setAttr ".wl[22].w[0]"  1;
	setAttr ".wl[23].w[0]"  1;
	setAttr ".wl[24].w[0]"  1;
	setAttr ".wl[25].w[0]"  1;
	setAttr ".wl[26].w[0]"  1;
	setAttr ".wl[27].w[0]"  1;
	setAttr ".wl[28].w[0]"  1;
	setAttr ".wl[29].w[0]"  1;
	setAttr ".wl[30].w[0]"  1;
	setAttr ".wl[31].w[0]"  1;
	setAttr ".wl[32].w[0]"  1;
	setAttr ".wl[33].w[0]"  1;
	setAttr ".wl[34].w[0]"  1;
	setAttr ".wl[35].w[0]"  1;
	setAttr ".wl[36].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak30";
createNode objectSet -n "skinCluster16Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster16GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster16GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet30";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId60";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts60";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster17";
	setAttr -s 15 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak31";
createNode objectSet -n "skinCluster17Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster17GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster17GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet31";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId62";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts62";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster18";
	setAttr -s 19 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".wl[17].w[0]"  1;
	setAttr ".wl[18].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak32";
createNode objectSet -n "skinCluster18Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster18GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster18GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet32";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId64";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts64";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster19";
	setAttr -s 12 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak33";
createNode objectSet -n "skinCluster19Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster19GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster19GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet33";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId66";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts66";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster20";
	setAttr -s 11 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak34";
createNode objectSet -n "skinCluster20Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster20GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster20GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet34";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId68";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts68";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode skinCluster -n "skinCluster21";
	setAttr -s 17 ".wl";
	setAttr ".wl[0].w[0]"  1;
	setAttr ".wl[1].w[0]"  1;
	setAttr ".wl[2].w[0]"  1;
	setAttr ".wl[3].w[0]"  1;
	setAttr ".wl[4].w[0]"  1;
	setAttr ".wl[5].w[0]"  1;
	setAttr ".wl[6].w[0]"  1;
	setAttr ".wl[7].w[0]"  1;
	setAttr ".wl[8].w[0]"  1;
	setAttr ".wl[9].w[0]"  1;
	setAttr ".wl[10].w[0]"  1;
	setAttr ".wl[11].w[0]"  1;
	setAttr ".wl[12].w[0]"  1;
	setAttr ".wl[13].w[0]"  1;
	setAttr ".wl[14].w[0]"  1;
	setAttr ".wl[15].w[0]"  1;
	setAttr ".wl[16].w[0]"  1;
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mi" 1;
	setAttr ".ucm" yes;
createNode tweak -n "tweak35";
createNode objectSet -n "skinCluster21Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster21GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster21GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet35";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId70";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts70";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode multiplyDivide -n "panX_sensitivityCorrection";
	setAttr ".op" 2;
createNode multiplyDivide -n "panY_sensitivityCorrection";
	setAttr ".op" 2;
createNode multiplyDivide -n "fromZoomToScale";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 1 1 ;
createNode objectSet -n "RenderSet";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
createNode condition -n "cameraBGFocalLength_switch";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 60 0 0 ;
createNode cluster -n "__cameraAim_camerasHolder_line_clusterCluster";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster1Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupParts -n "groupParts72";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "groupId72";
	setAttr ".ihi" 0;
createNode tweak -n "tweak36";
createNode objectSet -n "tweakSet36";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupParts -n "cluster1GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode groupId -n "cluster1GroupId";
	setAttr ".ihi" 0;
createNode cluster -n "__cameraAim_cameraHD_line_clusterCluster";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak37";
createNode objectSet -n "cluster2Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster2GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0]";
createNode objectSet -n "tweakSet37";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId74";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts74";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "__cameraAim_cameraHD_line_clusterCluster1";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster2Set1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster2GroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0]";
createNode tweak -n "tweak38";
createNode objectSet -n "tweakSet38";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId75";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts75";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "__focalCircles_HD_clusterCluster";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".og";
	setAttr ".rel" yes;
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak39";
createNode tweak -n "tweak40";
createNode objectSet -n "cluster3Set";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 2 ".gn";
createNode groupId -n "cluster3GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster3GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0:7]";
createNode groupId -n "cluster3GroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster3GroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0:7]";
createNode objectSet -n "tweakSet39";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId78";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts78";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet40";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId79";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts79";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "ficalCirclesHD_clusterCluster1";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".og";
	setAttr ".rel" yes;
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster3Set1";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 2 ".gn";
createNode groupId -n "cluster3GroupId2";
	setAttr ".ihi" 0;
createNode groupId -n "cluster3GroupId3";
	setAttr ".ihi" 0;
createNode tweak -n "tweak41";
createNode objectSet -n "tweakSet41";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId80";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts80";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupParts -n "cluster3GroupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0:7]";
createNode tweak -n "tweak42";
createNode objectSet -n "tweakSet42";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId81";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts81";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupParts -n "cluster3GroupParts3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0:7]";
createNode multiplyDivide -n "normalizeFocalHD";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 60 1 1 ;
createNode multDoubleLinear -n "globalScaleHD";
createNode multDoubleLinear -n "globalScalePROJ";
createNode multiplyDivide -n "normalizeFocalPROJ";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 60 1 1 ;
createNode multiplyDivide -n "cameraBGFocalFactor";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 60 0 0 ;
createNode hyperGraphInfo -n "nodeEditorPanel2Info";
createNode hyperView -n "hyperView1";
	setAttr ".vl" -type "double2" -333.718487394958 -584.34873949579821 ;
	setAttr ".vh" -type "double2" 1273.0042016806724 259.34873949579838 ;
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout1";
	setAttr ".ihi" 0;
	setAttr -s 9 ".hyp";
	setAttr ".hyp[0].x" 530;
	setAttr ".hyp[0].y" -177.14285278320312;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].x" 530;
	setAttr ".hyp[1].y" -72.857139587402344;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 1.4285714626312256;
	setAttr ".hyp[2].y" -180;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].x" 741.4285888671875;
	setAttr ".hyp[3].y" -177.14285278320312;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".anf" yes;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av ".unw" 1;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -s 11 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -av -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bf";
	setAttr -k on ".fii";
	setAttr -av -k on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -av -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr -k on ".fn";
	setAttr -k on ".if";
	setAttr -k on ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -av -k on ".fir";
	setAttr -k on ".aap";
	setAttr -av -k on ".gh";
	setAttr -cb on ".sd";
connectAttr "skinCluster4.og[0]" "camera_globalShape.cr";
connectAttr "tweak18.pl[0].cp[0]" "camera_globalShape.twl";
connectAttr "skinCluster4GroupId.id" "camera_globalShape.iog.og[2].gid";
connectAttr "skinCluster4Set.mwc" "camera_globalShape.iog.og[2].gco";
connectAttr "groupId36.id" "camera_globalShape.iog.og[3].gid";
connectAttr "tweakSet18.mwc" "camera_globalShape.iog.og[3].gco";
connectAttr "cameras_holder_aimConstraint.crx" "cameras_holder.rx" -l on;
connectAttr "cameras_holder_aimConstraint.cry" "cameras_holder.ry" -l on;
connectAttr "cameras_holder_aimConstraint.crz" "cameras_holder.rz" -l on;
connectAttr "skinCluster5.og[0]" "cameras_holderShape_2.cr";
connectAttr "tweak19.pl[0].cp[0]" "cameras_holderShape_2.twl";
connectAttr "skinCluster5GroupId.id" "cameras_holderShape_2.iog.og[2].gid";
connectAttr "skinCluster5Set.mwc" "cameras_holderShape_2.iog.og[2].gco";
connectAttr "groupId38.id" "cameras_holderShape_2.iog.og[3].gid";
connectAttr "tweakSet19.mwc" "cameras_holderShape_2.iog.og[3].gco";
connectAttr "skinCluster6.og[0]" "cameras_holderShape_1.cr";
connectAttr "tweak20.pl[0].cp[0]" "cameras_holderShape_1.twl";
connectAttr "skinCluster6GroupId.id" "cameras_holderShape_1.iog.og[2].gid";
connectAttr "skinCluster6Set.mwc" "cameras_holderShape_1.iog.og[2].gco";
connectAttr "groupId40.id" "cameras_holderShape_1.iog.og[3].gid";
connectAttr "tweakSet20.mwc" "cameras_holderShape_1.iog.og[3].gco";
connectAttr "cameras_holder.pim" "cameras_holder_aimConstraint.cpim";
connectAttr "cameras_holder.t" "cameras_holder_aimConstraint.ct";
connectAttr "cameras_holder.rp" "cameras_holder_aimConstraint.crp";
connectAttr "cameras_holder.rpt" "cameras_holder_aimConstraint.crt";
connectAttr "cameras_holder.ro" "cameras_holder_aimConstraint.cro";
connectAttr "camera_aim.t" "cameras_holder_aimConstraint.tg[0].tt";
connectAttr "camera_aim.rp" "cameras_holder_aimConstraint.tg[0].trp";
connectAttr "camera_aim.rpt" "cameras_holder_aimConstraint.tg[0].trt";
connectAttr "camera_aim.pm" "cameras_holder_aimConstraint.tg[0].tpm";
connectAttr "cameras_holder_aimConstraint.w0" "cameras_holder_aimConstraint.tg[0].tw"
		;
connectAttr "__upLocator.wm" "cameras_holder_aimConstraint.wum";
connectAttr "cameraBGFocalLength_switch.ocr" "cameraBGShape.fl";
connectAttr "isCameraHD.ocr" "cameraHD_controller.v";
connectAttr "skinCluster1.og[0]" "cameraHD_controllerShape.i";
connectAttr "tweak15.vl[0].vt[0]" "cameraHD_controllerShape.twl";
connectAttr "skinCluster1GroupId.id" "cameraHD_controllerShape.iog.og[6].gid";
connectAttr "skinCluster1Set.mwc" "cameraHD_controllerShape.iog.og[6].gco";
connectAttr "groupId30.id" "cameraHD_controllerShape.iog.og[7].gid";
connectAttr "tweakSet15.mwc" "cameraHD_controllerShape.iog.og[7].gco";
connectAttr "skinCluster19.og[0]" "HShape.cr";
connectAttr "tweak33.pl[0].cp[0]" "HShape.twl";
connectAttr "skinCluster19GroupId.id" "HShape.iog.og[0].gid";
connectAttr "skinCluster19Set.mwc" "HShape.iog.og[0].gco";
connectAttr "groupId66.id" "HShape.iog.og[1].gid";
connectAttr "tweakSet33.mwc" "HShape.iog.og[1].gco";
connectAttr "skinCluster20.og[0]" "DShape1.cr";
connectAttr "tweak34.pl[0].cp[0]" "DShape1.twl";
connectAttr "skinCluster20GroupId.id" "DShape1.iog.og[0].gid";
connectAttr "skinCluster20Set.mwc" "DShape1.iog.og[0].gco";
connectAttr "groupId68.id" "DShape1.iog.og[1].gid";
connectAttr "tweakSet34.mwc" "DShape1.iog.og[1].gco";
connectAttr "skinCluster21.og[0]" "DShape2.cr";
connectAttr "tweak35.pl[0].cp[0]" "DShape2.twl";
connectAttr "skinCluster21GroupId.id" "DShape2.iog.og[0].gid";
connectAttr "skinCluster21Set.mwc" "DShape2.iog.og[0].gco";
connectAttr "groupId70.id" "DShape2.iog.og[1].gid";
connectAttr "tweakSet35.mwc" "DShape2.iog.og[1].gco";
connectAttr "cameraHD_controller.focalLength" "cameraHDShape.fl";
connectAttr "cameras_holder.farClippingPlane" "cameraHDShape.fcp";
connectAttr "cameras_holder.nearClippingPlane" "cameraHDShape.ncp";
connectAttr "cameras_holder.showGate" "cameraHDShape.dfg";
connectAttr "cameras_holder.showGate" "cameraHDShape.dgm";
connectAttr "cameras_holder.overscan" "cameraHDShape.ovr";
connectAttr "cameraHD_controller.v" "__cameraAim_cameraHD_lineShape.v";
connectAttr "__cameraAim_cameraHD_line_clusterCluster.og[0]" "__cameraAim_cameraHD_lineShape.cr"
		;
connectAttr "tweak37.pl[0].cp[0]" "__cameraAim_cameraHD_lineShape.twl";
connectAttr "cluster2GroupId.id" "__cameraAim_cameraHD_lineShape.iog.og[0].gid";
connectAttr "cluster2Set.mwc" "__cameraAim_cameraHD_lineShape.iog.og[0].gco";
connectAttr "groupId74.id" "__cameraAim_cameraHD_lineShape.iog.og[1].gid";
connectAttr "tweakSet37.mwc" "__cameraAim_cameraHD_lineShape.iog.og[1].gco";
connectAttr "__cameraAim_cameraHD_line_cluster_pointConstraint1.ctx" "__cameraAim_cameraHD_line_cluster.tx"
		;
connectAttr "__cameraAim_cameraHD_line_cluster_pointConstraint1.cty" "__cameraAim_cameraHD_line_cluster.ty"
		;
connectAttr "__cameraAim_cameraHD_line_cluster_pointConstraint1.ctz" "__cameraAim_cameraHD_line_cluster.tz"
		;
connectAttr "__cameraAim_cameraHD_line_cluster.pim" "__cameraAim_cameraHD_line_cluster_pointConstraint1.cpim"
		;
connectAttr "__cameraAim_cameraHD_line_cluster.rp" "__cameraAim_cameraHD_line_cluster_pointConstraint1.crp"
		;
connectAttr "__cameraAim_cameraHD_line_cluster.rpt" "__cameraAim_cameraHD_line_cluster_pointConstraint1.crt"
		;
connectAttr "cameras_holder.t" "__cameraAim_cameraHD_line_cluster_pointConstraint1.tg[0].tt"
		;
connectAttr "cameras_holder.rp" "__cameraAim_cameraHD_line_cluster_pointConstraint1.tg[0].trp"
		;
connectAttr "cameras_holder.rpt" "__cameraAim_cameraHD_line_cluster_pointConstraint1.tg[0].trt"
		;
connectAttr "cameras_holder.pm" "__cameraAim_cameraHD_line_cluster_pointConstraint1.tg[0].tpm"
		;
connectAttr "__cameraAim_cameraHD_line_cluster_pointConstraint1.w0" "__cameraAim_cameraHD_line_cluster_pointConstraint1.tg[0].tw"
		;
connectAttr "cameraHD_controller.v" "focalCircle1HDShape.v";
connectAttr "__focalCircles_HD_clusterCluster.og[0]" "focalCircle1HDShape.cr";
connectAttr "tweak39.pl[0].cp[0]" "focalCircle1HDShape.twl";
connectAttr "cluster3GroupId.id" "focalCircle1HDShape.iog.og[0].gid";
connectAttr "cluster3Set.mwc" "focalCircle1HDShape.iog.og[0].gco";
connectAttr "groupId78.id" "focalCircle1HDShape.iog.og[1].gid";
connectAttr "tweakSet39.mwc" "focalCircle1HDShape.iog.og[1].gco";
connectAttr "cameraHD_controller.v" "focalCircle2HDShape.v";
connectAttr "__focalCircles_HD_clusterCluster.og[1]" "focalCircle2HDShape.cr";
connectAttr "tweak40.pl[0].cp[0]" "focalCircle2HDShape.twl";
connectAttr "cluster3GroupId1.id" "focalCircle2HDShape.iog.og[0].gid";
connectAttr "cluster3Set.mwc" "focalCircle2HDShape.iog.og[0].gco";
connectAttr "groupId79.id" "focalCircle2HDShape.iog.og[1].gid";
connectAttr "tweakSet40.mwc" "focalCircle2HDShape.iog.og[1].gco";
connectAttr "globalScaleHD.o" "__focalCircles_HD_cluster.sx";
connectAttr "globalScaleHD.o" "__focalCircles_HD_cluster.sy";
connectAttr "isCameraPROJ.ocr" "cameraPROJ_controller.v";
connectAttr "skinCluster3.og[0]" "cameraPROJ_controllerShape.i";
connectAttr "tweak17.vl[0].vt[0]" "cameraPROJ_controllerShape.twl";
connectAttr "skinCluster3GroupId.id" "cameraPROJ_controllerShape.iog.og[4].gid";
connectAttr "skinCluster3Set.mwc" "cameraPROJ_controllerShape.iog.og[4].gco";
connectAttr "groupId34.id" "cameraPROJ_controllerShape.iog.og[5].gid";
connectAttr "tweakSet17.mwc" "cameraPROJ_controllerShape.iog.og[5].gco";
connectAttr "skinCluster12.og[0]" "JShape.cr";
connectAttr "tweak26.pl[0].cp[0]" "JShape.twl";
connectAttr "skinCluster12GroupId.id" "JShape.iog.og[0].gid";
connectAttr "skinCluster12Set.mwc" "JShape.iog.og[0].gco";
connectAttr "groupId52.id" "JShape.iog.og[1].gid";
connectAttr "tweakSet26.mwc" "JShape.iog.og[1].gco";
connectAttr "skinCluster13.og[0]" "OShape2.cr";
connectAttr "tweak27.pl[0].cp[0]" "OShape2.twl";
connectAttr "skinCluster13GroupId.id" "OShape2.iog.og[0].gid";
connectAttr "skinCluster13Set.mwc" "OShape2.iog.og[0].gco";
connectAttr "groupId54.id" "OShape2.iog.og[1].gid";
connectAttr "tweakSet27.mwc" "OShape2.iog.og[1].gco";
connectAttr "skinCluster14.og[0]" "OShape1.cr";
connectAttr "tweak28.pl[0].cp[0]" "OShape1.twl";
connectAttr "skinCluster14GroupId.id" "OShape1.iog.og[0].gid";
connectAttr "skinCluster14Set.mwc" "OShape1.iog.og[0].gco";
connectAttr "groupId56.id" "OShape1.iog.og[1].gid";
connectAttr "tweakSet28.mwc" "OShape1.iog.og[1].gco";
connectAttr "skinCluster15.og[0]" "RShape2.cr";
connectAttr "tweak29.pl[0].cp[0]" "RShape2.twl";
connectAttr "skinCluster15GroupId.id" "RShape2.iog.og[0].gid";
connectAttr "skinCluster15Set.mwc" "RShape2.iog.og[0].gco";
connectAttr "groupId58.id" "RShape2.iog.og[1].gid";
connectAttr "tweakSet29.mwc" "RShape2.iog.og[1].gco";
connectAttr "skinCluster16.og[0]" "RShape1.cr";
connectAttr "tweak30.pl[0].cp[0]" "RShape1.twl";
connectAttr "skinCluster16GroupId.id" "RShape1.iog.og[0].gid";
connectAttr "skinCluster16Set.mwc" "RShape1.iog.og[0].gco";
connectAttr "groupId60.id" "RShape1.iog.og[1].gid";
connectAttr "tweakSet30.mwc" "RShape1.iog.og[1].gco";
connectAttr "skinCluster17.og[0]" "PShape2.cr";
connectAttr "tweak31.pl[0].cp[0]" "PShape2.twl";
connectAttr "skinCluster17GroupId.id" "PShape2.iog.og[0].gid";
connectAttr "skinCluster17Set.mwc" "PShape2.iog.og[0].gco";
connectAttr "groupId62.id" "PShape2.iog.og[1].gid";
connectAttr "tweakSet31.mwc" "PShape2.iog.og[1].gco";
connectAttr "skinCluster18.og[0]" "PShape1.cr";
connectAttr "tweak32.pl[0].cp[0]" "PShape1.twl";
connectAttr "skinCluster18GroupId.id" "PShape1.iog.og[0].gid";
connectAttr "skinCluster18Set.mwc" "PShape1.iog.og[0].gco";
connectAttr "groupId64.id" "PShape1.iog.og[1].gid";
connectAttr "tweakSet32.mwc" "PShape1.iog.og[1].gco";
connectAttr "cameraPROJ_controller.v" "__cameraAim_cameraPROJ_lineShape.v";
connectAttr "cluster2GroupId1.id" "__cameraAim_cameraPROJ_lineShape.iog.og[0].gid"
		;
connectAttr "cluster2Set1.mwc" "__cameraAim_cameraPROJ_lineShape.iog.og[0].gco";
connectAttr "groupId75.id" "__cameraAim_cameraPROJ_lineShape.iog.og[1].gid";
connectAttr "tweakSet38.mwc" "__cameraAim_cameraPROJ_lineShape.iog.og[1].gco";
connectAttr "__cameraAim_cameraHD_line_clusterCluster1.og[0]" "__cameraAim_cameraPROJ_lineShape.cr"
		;
connectAttr "tweak38.pl[0].cp[0]" "__cameraAim_cameraPROJ_lineShape.twl";
connectAttr "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.ctx" "__cameraAim_cameraPROJ_line_cluster.tx"
		;
connectAttr "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.cty" "__cameraAim_cameraPROJ_line_cluster.ty"
		;
connectAttr "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.ctz" "__cameraAim_cameraPROJ_line_cluster.tz"
		;
connectAttr "__cameraAim_cameraPROJ_line_cluster.pim" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.cpim"
		;
connectAttr "__cameraAim_cameraPROJ_line_cluster.rp" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.crp"
		;
connectAttr "__cameraAim_cameraPROJ_line_cluster.rpt" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.crt"
		;
connectAttr "cameras_holder.t" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.tg[0].tt"
		;
connectAttr "cameras_holder.rp" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.tg[0].trp"
		;
connectAttr "cameras_holder.rpt" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.tg[0].trt"
		;
connectAttr "cameras_holder.pm" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.tg[0].tpm"
		;
connectAttr "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.w0" "__cameraAim_cameraPROJ_line_cluster_pointConstraint1.tg[0].tw"
		;
connectAttr "cameraPROJ_controller.v" "focalCircle1PROJShape.v";
connectAttr "cluster3GroupId2.id" "focalCircle1PROJShape.iog.og[0].gid";
connectAttr "cluster3Set1.mwc" "focalCircle1PROJShape.iog.og[0].gco";
connectAttr "groupId81.id" "focalCircle1PROJShape.iog.og[1].gid";
connectAttr "tweakSet42.mwc" "focalCircle1PROJShape.iog.og[1].gco";
connectAttr "ficalCirclesHD_clusterCluster1.og[0]" "focalCircle1PROJShape.cr";
connectAttr "tweak42.pl[0].cp[0]" "focalCircle1PROJShape.twl";
connectAttr "cameraPROJ_controller.v" "focalCircle2PROJShape.v";
connectAttr "ficalCirclesHD_clusterCluster1.og[1]" "focalCircle2PROJShape.cr";
connectAttr "cluster3GroupId3.id" "focalCircle2PROJShape.iog.og[0].gid";
connectAttr "cluster3Set1.mwc" "focalCircle2PROJShape.iog.og[0].gco";
connectAttr "groupId80.id" "focalCircle2PROJShape.iog.og[1].gid";
connectAttr "tweakSet41.mwc" "focalCircle2PROJShape.iog.og[1].gco";
connectAttr "tweak41.pl[0].cp[0]" "focalCircle2PROJShape.twl";
connectAttr "globalScalePROJ.o" "__focalCircles_PROJ_cluster.sx";
connectAttr "globalScalePROJ.o" "__focalCircles_PROJ_cluster.sy";
connectAttr "cameraPROJ_controller.rz" "cameraPROJ_roller.rz";
connectAttr "cameraPROJ_controller.focalLength" "cameraPROJShape.fl";
connectAttr "panX_sensitivityCorrection.ox" "cameraPROJShape.hfo";
connectAttr "panY_sensitivityCorrection.ox" "cameraPROJShape.vfo";
connectAttr "fromZoomToScale.ox" "cameraPROJShape.cs";
connectAttr "cameras_holder.farClippingPlane" "cameraPROJShape.fcp";
connectAttr "cameras_holder.nearClippingPlane" "cameraPROJShape.ncp";
connectAttr "cameras_holder.showGate" "cameraPROJShape.dgm";
connectAttr "cameras_holder.showGate" "cameraPROJShape.dfg";
connectAttr "cameras_holder.overscan" "cameraPROJShape.ovr";
connectAttr "camera_aim_orientConstraint.crx" "camera_aim.rx" -l on;
connectAttr "camera_aim_orientConstraint.cry" "camera_aim.ry" -l on;
connectAttr "camera_aim_orientConstraint.crz" "camera_aim.rz" -l on;
connectAttr "skinCluster7.og[0]" "camera_aim_circleShape_1.cr";
connectAttr "tweak21.pl[0].cp[0]" "camera_aim_circleShape_1.twl";
connectAttr "skinCluster7GroupId.id" "camera_aim_circleShape_1.iog.og[2].gid";
connectAttr "skinCluster7Set.mwc" "camera_aim_circleShape_1.iog.og[2].gco";
connectAttr "groupId42.id" "camera_aim_circleShape_1.iog.og[3].gid";
connectAttr "tweakSet21.mwc" "camera_aim_circleShape_1.iog.og[3].gco";
connectAttr "skinCluster8.og[0]" "camera_aim_crossShape_1.cr";
connectAttr "tweak22.pl[0].cp[0]" "camera_aim_crossShape_1.twl";
connectAttr "skinCluster8GroupId.id" "camera_aim_crossShape_1.iog.og[2].gid";
connectAttr "skinCluster8Set.mwc" "camera_aim_crossShape_1.iog.og[2].gco";
connectAttr "groupId44.id" "camera_aim_crossShape_1.iog.og[3].gid";
connectAttr "tweakSet22.mwc" "camera_aim_crossShape_1.iog.og[3].gco";
connectAttr "skinCluster9.og[0]" "camera_aim_crossShape_2.cr";
connectAttr "tweak23.pl[0].cp[0]" "camera_aim_crossShape_2.twl";
connectAttr "skinCluster9GroupId.id" "camera_aim_crossShape_2.iog.og[2].gid";
connectAttr "skinCluster9Set.mwc" "camera_aim_crossShape_2.iog.og[2].gco";
connectAttr "groupId46.id" "camera_aim_crossShape_2.iog.og[3].gid";
connectAttr "tweakSet23.mwc" "camera_aim_crossShape_2.iog.og[3].gco";
connectAttr "skinCluster10.og[0]" "camera_aim_circleShape_3.cr";
connectAttr "tweak24.pl[0].cp[0]" "camera_aim_circleShape_3.twl";
connectAttr "skinCluster10GroupId.id" "camera_aim_circleShape_3.iog.og[2].gid";
connectAttr "skinCluster10Set.mwc" "camera_aim_circleShape_3.iog.og[2].gco";
connectAttr "groupId48.id" "camera_aim_circleShape_3.iog.og[3].gid";
connectAttr "tweakSet24.mwc" "camera_aim_circleShape_3.iog.og[3].gco";
connectAttr "skinCluster11.og[0]" "camera_aim_circleShape_2.cr";
connectAttr "tweak25.pl[0].cp[0]" "camera_aim_circleShape_2.twl";
connectAttr "skinCluster11GroupId.id" "camera_aim_circleShape_2.iog.og[2].gid";
connectAttr "skinCluster11Set.mwc" "camera_aim_circleShape_2.iog.og[2].gco";
connectAttr "groupId50.id" "camera_aim_circleShape_2.iog.og[3].gid";
connectAttr "tweakSet25.mwc" "camera_aim_circleShape_2.iog.og[3].gco";
connectAttr "camera_aim.ro" "camera_aim_orientConstraint.cro";
connectAttr "camera_aim.pim" "camera_aim_orientConstraint.cpim";
connectAttr "cameras_holder.r" "camera_aim_orientConstraint.tg[0].tr";
connectAttr "cameras_holder.ro" "camera_aim_orientConstraint.tg[0].tro";
connectAttr "cameras_holder.pm" "camera_aim_orientConstraint.tg[0].tpm";
connectAttr "camera_aim_orientConstraint.w0" "camera_aim_orientConstraint.tg[0].tw"
		;
connectAttr "cluster1GroupId.id" "__cameraAim_camerasHolder_lineShape.iog.og[3].gid"
		;
connectAttr "cluster1Set.mwc" "__cameraAim_camerasHolder_lineShape.iog.og[3].gco"
		;
connectAttr "tweakSet36.mwc" "__cameraAim_camerasHolder_lineShape.iog.og[4].gco"
		;
connectAttr "groupId72.id" "__cameraAim_camerasHolder_lineShape.iog.og[4].gid";
connectAttr "__cameraAim_camerasHolder_line_clusterCluster.og[0]" "__cameraAim_camerasHolder_lineShape.cr"
		;
connectAttr "tweak36.pl[0].cp[0]" "__cameraAim_camerasHolder_lineShape.twl";
connectAttr "cluster1Handle_pointConstraint1.ctx" "__cameraAim_camerasHolder_line_cluster.tx"
		;
connectAttr "cluster1Handle_pointConstraint1.cty" "__cameraAim_camerasHolder_line_cluster.ty"
		;
connectAttr "cluster1Handle_pointConstraint1.ctz" "__cameraAim_camerasHolder_line_cluster.tz"
		;
connectAttr "__cameraAim_camerasHolder_line_cluster.pim" "cluster1Handle_pointConstraint1.cpim"
		;
connectAttr "__cameraAim_camerasHolder_line_cluster.rp" "cluster1Handle_pointConstraint1.crp"
		;
connectAttr "__cameraAim_camerasHolder_line_cluster.rpt" "cluster1Handle_pointConstraint1.crt"
		;
connectAttr "cameras_holder.t" "cluster1Handle_pointConstraint1.tg[0].tt";
connectAttr "cameras_holder.rp" "cluster1Handle_pointConstraint1.tg[0].trp";
connectAttr "cameras_holder.rpt" "cluster1Handle_pointConstraint1.tg[0].trt";
connectAttr "cameras_holder.pm" "cluster1Handle_pointConstraint1.tg[0].tpm";
connectAttr "cluster1Handle_pointConstraint1.w0" "cluster1Handle_pointConstraint1.tg[0].tw"
		;
connectAttr "cameras_holder.controllers_size" "__controllersVisualScaler.sx";
connectAttr "cameras_holder.controllers_size" "__controllersVisualScaler.sy";
connectAttr "cameras_holder.controllers_size" "__controllersVisualScaler.sz";
connectAttr "cameraPROJShape.hfo" "__2dCameraMovementsData.tx";
connectAttr "cameraPROJShape.vfo" "__2dCameraMovementsData.ty";
connectAttr "cameraPROJ_roller.rz" "__2dCameraMovementsData.rz";
connectAttr "cameraPROJShape.cs" "__2dCameraMovementsData.sz";
connectAttr "__upLocator_parentConstraint.ctx" "__upLocator.tx";
connectAttr "__upLocator_parentConstraint.cty" "__upLocator.ty";
connectAttr "__upLocator_parentConstraint.ctz" "__upLocator.tz";
connectAttr "__upLocator_parentConstraint.crx" "__upLocator.rx";
connectAttr "__upLocator_parentConstraint.cry" "__upLocator.ry";
connectAttr "__upLocator_parentConstraint.crz" "__upLocator.rz";
connectAttr "__upLocator.ro" "__upLocator_parentConstraint.cro";
connectAttr "__upLocator.pim" "__upLocator_parentConstraint.cpim";
connectAttr "__upLocator.rp" "__upLocator_parentConstraint.crp";
connectAttr "__upLocator.rpt" "__upLocator_parentConstraint.crt";
connectAttr "camera_global.t" "__upLocator_parentConstraint.tg[0].tt";
connectAttr "camera_global.rp" "__upLocator_parentConstraint.tg[0].trp";
connectAttr "camera_global.rpt" "__upLocator_parentConstraint.tg[0].trt";
connectAttr "camera_global.r" "__upLocator_parentConstraint.tg[0].tr";
connectAttr "camera_global.ro" "__upLocator_parentConstraint.tg[0].tro";
connectAttr "camera_global.s" "__upLocator_parentConstraint.tg[0].ts";
connectAttr "camera_global.pm" "__upLocator_parentConstraint.tg[0].tpm";
connectAttr "__upLocator_parentConstraint.w0" "__upLocator_parentConstraint.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose1.msg" "skinCluster1.bp";
connectAttr "__controllersVisualScaler.wm" "skinCluster1.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster1.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster1.ifcl[0]";
connectAttr "groupParts30.og" "tweak15.ip[0].ig";
connectAttr "groupId30.id" "tweak15.ip[0].gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "cameraHD_controllerShape.iog.og[6]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "tweak15.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupId30.msg" "tweakSet15.gn" -na;
connectAttr "cameraHD_controllerShape.iog.og[7]" "tweakSet15.dsm" -na;
connectAttr "tweak15.msg" "tweakSet15.ub[0]";
connectAttr "cameraHD_controllerShapeOrig.w" "groupParts30.ig";
connectAttr "groupId30.id" "groupParts30.gi";
connectAttr "__controllersVisualScaler.msg" "bindPose1.m[0]";
connectAttr "camera_rig.msg" "bindPose1.m[2]";
connectAttr "__internals.msg" "bindPose1.m[3]";
connectAttr "bindPose1.m[3]" "bindPose1.p[0]";
connectAttr "bindPose1.w" "bindPose1.p[1]";
connectAttr "camera_rig.msg" "bindPose1.p[3]";
connectAttr "__controllersVisualScaler.bps" "bindPose1.wm[0]";
connectAttr "skinCluster3GroupParts.og" "skinCluster3.ip[0].ig";
connectAttr "skinCluster3GroupId.id" "skinCluster3.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster3.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster3.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster3.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster3.bp";
connectAttr "groupParts34.og" "tweak17.ip[0].ig";
connectAttr "groupId34.id" "tweak17.ip[0].gi";
connectAttr "skinCluster3GroupId.msg" "skinCluster3Set.gn" -na;
connectAttr "cameraPROJ_controllerShape.iog.og[4]" "skinCluster3Set.dsm" -na;
connectAttr "skinCluster3.msg" "skinCluster3Set.ub[0]";
connectAttr "tweak17.og[0]" "skinCluster3GroupParts.ig";
connectAttr "skinCluster3GroupId.id" "skinCluster3GroupParts.gi";
connectAttr "groupId34.msg" "tweakSet17.gn" -na;
connectAttr "cameraPROJ_controllerShape.iog.og[5]" "tweakSet17.dsm" -na;
connectAttr "tweak17.msg" "tweakSet17.ub[0]";
connectAttr "cameraPROJ_controllerShapeOrig.w" "groupParts34.ig";
connectAttr "groupId34.id" "groupParts34.gi";
connectAttr "skinCluster4GroupParts.og" "skinCluster4.ip[0].ig";
connectAttr "skinCluster4GroupId.id" "skinCluster4.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster4.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster4.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster4.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster4.bp";
connectAttr "groupParts36.og" "tweak18.ip[0].ig";
connectAttr "groupId36.id" "tweak18.ip[0].gi";
connectAttr "skinCluster4GroupId.msg" "skinCluster4Set.gn" -na;
connectAttr "camera_globalShape.iog.og[2]" "skinCluster4Set.dsm" -na;
connectAttr "skinCluster4.msg" "skinCluster4Set.ub[0]";
connectAttr "tweak18.og[0]" "skinCluster4GroupParts.ig";
connectAttr "skinCluster4GroupId.id" "skinCluster4GroupParts.gi";
connectAttr "groupId36.msg" "tweakSet18.gn" -na;
connectAttr "camera_globalShape.iog.og[3]" "tweakSet18.dsm" -na;
connectAttr "tweak18.msg" "tweakSet18.ub[0]";
connectAttr "camera_globalShapeOrig.ws" "groupParts36.ig";
connectAttr "groupId36.id" "groupParts36.gi";
connectAttr "skinCluster5GroupParts.og" "skinCluster5.ip[0].ig";
connectAttr "skinCluster5GroupId.id" "skinCluster5.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster5.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster5.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster5.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster5.bp";
connectAttr "groupParts38.og" "tweak19.ip[0].ig";
connectAttr "groupId38.id" "tweak19.ip[0].gi";
connectAttr "skinCluster5GroupId.msg" "skinCluster5Set.gn" -na;
connectAttr "cameras_holderShape_2.iog.og[2]" "skinCluster5Set.dsm" -na;
connectAttr "skinCluster5.msg" "skinCluster5Set.ub[0]";
connectAttr "tweak19.og[0]" "skinCluster5GroupParts.ig";
connectAttr "skinCluster5GroupId.id" "skinCluster5GroupParts.gi";
connectAttr "groupId38.msg" "tweakSet19.gn" -na;
connectAttr "cameras_holderShape_2.iog.og[3]" "tweakSet19.dsm" -na;
connectAttr "tweak19.msg" "tweakSet19.ub[0]";
connectAttr "cameras_holderShape_2Orig.ws" "groupParts38.ig";
connectAttr "groupId38.id" "groupParts38.gi";
connectAttr "skinCluster6GroupParts.og" "skinCluster6.ip[0].ig";
connectAttr "skinCluster6GroupId.id" "skinCluster6.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster6.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster6.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster6.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster6.bp";
connectAttr "groupParts40.og" "tweak20.ip[0].ig";
connectAttr "groupId40.id" "tweak20.ip[0].gi";
connectAttr "skinCluster6GroupId.msg" "skinCluster6Set.gn" -na;
connectAttr "cameras_holderShape_1.iog.og[2]" "skinCluster6Set.dsm" -na;
connectAttr "skinCluster6.msg" "skinCluster6Set.ub[0]";
connectAttr "tweak20.og[0]" "skinCluster6GroupParts.ig";
connectAttr "skinCluster6GroupId.id" "skinCluster6GroupParts.gi";
connectAttr "groupId40.msg" "tweakSet20.gn" -na;
connectAttr "cameras_holderShape_1.iog.og[3]" "tweakSet20.dsm" -na;
connectAttr "tweak20.msg" "tweakSet20.ub[0]";
connectAttr "cameras_holderShape_1Orig.ws" "groupParts40.ig";
connectAttr "groupId40.id" "groupParts40.gi";
connectAttr "skinCluster7GroupParts.og" "skinCluster7.ip[0].ig";
connectAttr "skinCluster7GroupId.id" "skinCluster7.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster7.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster7.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster7.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster7.bp";
connectAttr "groupParts42.og" "tweak21.ip[0].ig";
connectAttr "groupId42.id" "tweak21.ip[0].gi";
connectAttr "skinCluster7GroupId.msg" "skinCluster7Set.gn" -na;
connectAttr "camera_aim_circleShape_1.iog.og[2]" "skinCluster7Set.dsm" -na;
connectAttr "skinCluster7.msg" "skinCluster7Set.ub[0]";
connectAttr "tweak21.og[0]" "skinCluster7GroupParts.ig";
connectAttr "skinCluster7GroupId.id" "skinCluster7GroupParts.gi";
connectAttr "groupId42.msg" "tweakSet21.gn" -na;
connectAttr "camera_aim_circleShape_1.iog.og[3]" "tweakSet21.dsm" -na;
connectAttr "tweak21.msg" "tweakSet21.ub[0]";
connectAttr "camera_aim_circleShape_1Orig.ws" "groupParts42.ig";
connectAttr "groupId42.id" "groupParts42.gi";
connectAttr "skinCluster8GroupParts.og" "skinCluster8.ip[0].ig";
connectAttr "skinCluster8GroupId.id" "skinCluster8.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster8.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster8.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster8.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster8.bp";
connectAttr "groupParts44.og" "tweak22.ip[0].ig";
connectAttr "groupId44.id" "tweak22.ip[0].gi";
connectAttr "skinCluster8GroupId.msg" "skinCluster8Set.gn" -na;
connectAttr "camera_aim_crossShape_1.iog.og[2]" "skinCluster8Set.dsm" -na;
connectAttr "skinCluster8.msg" "skinCluster8Set.ub[0]";
connectAttr "tweak22.og[0]" "skinCluster8GroupParts.ig";
connectAttr "skinCluster8GroupId.id" "skinCluster8GroupParts.gi";
connectAttr "groupId44.msg" "tweakSet22.gn" -na;
connectAttr "camera_aim_crossShape_1.iog.og[3]" "tweakSet22.dsm" -na;
connectAttr "tweak22.msg" "tweakSet22.ub[0]";
connectAttr "camera_aim_crossShape_1Orig.ws" "groupParts44.ig";
connectAttr "groupId44.id" "groupParts44.gi";
connectAttr "skinCluster9GroupParts.og" "skinCluster9.ip[0].ig";
connectAttr "skinCluster9GroupId.id" "skinCluster9.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster9.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster9.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster9.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster9.bp";
connectAttr "groupParts46.og" "tweak23.ip[0].ig";
connectAttr "groupId46.id" "tweak23.ip[0].gi";
connectAttr "skinCluster9GroupId.msg" "skinCluster9Set.gn" -na;
connectAttr "camera_aim_crossShape_2.iog.og[2]" "skinCluster9Set.dsm" -na;
connectAttr "skinCluster9.msg" "skinCluster9Set.ub[0]";
connectAttr "tweak23.og[0]" "skinCluster9GroupParts.ig";
connectAttr "skinCluster9GroupId.id" "skinCluster9GroupParts.gi";
connectAttr "groupId46.msg" "tweakSet23.gn" -na;
connectAttr "camera_aim_crossShape_2.iog.og[3]" "tweakSet23.dsm" -na;
connectAttr "tweak23.msg" "tweakSet23.ub[0]";
connectAttr "camera_aim_crossShape_2Orig.ws" "groupParts46.ig";
connectAttr "groupId46.id" "groupParts46.gi";
connectAttr "skinCluster10GroupParts.og" "skinCluster10.ip[0].ig";
connectAttr "skinCluster10GroupId.id" "skinCluster10.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster10.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster10.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster10.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster10.bp";
connectAttr "groupParts48.og" "tweak24.ip[0].ig";
connectAttr "groupId48.id" "tweak24.ip[0].gi";
connectAttr "skinCluster10GroupId.msg" "skinCluster10Set.gn" -na;
connectAttr "camera_aim_circleShape_3.iog.og[2]" "skinCluster10Set.dsm" -na;
connectAttr "skinCluster10.msg" "skinCluster10Set.ub[0]";
connectAttr "tweak24.og[0]" "skinCluster10GroupParts.ig";
connectAttr "skinCluster10GroupId.id" "skinCluster10GroupParts.gi";
connectAttr "groupId48.msg" "tweakSet24.gn" -na;
connectAttr "camera_aim_circleShape_3.iog.og[3]" "tweakSet24.dsm" -na;
connectAttr "tweak24.msg" "tweakSet24.ub[0]";
connectAttr "camera_aim_circleShape_3Orig.ws" "groupParts48.ig";
connectAttr "groupId48.id" "groupParts48.gi";
connectAttr "skinCluster11GroupParts.og" "skinCluster11.ip[0].ig";
connectAttr "skinCluster11GroupId.id" "skinCluster11.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster11.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster11.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster11.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster11.bp";
connectAttr "groupParts50.og" "tweak25.ip[0].ig";
connectAttr "groupId50.id" "tweak25.ip[0].gi";
connectAttr "skinCluster11GroupId.msg" "skinCluster11Set.gn" -na;
connectAttr "camera_aim_circleShape_2.iog.og[2]" "skinCluster11Set.dsm" -na;
connectAttr "skinCluster11.msg" "skinCluster11Set.ub[0]";
connectAttr "tweak25.og[0]" "skinCluster11GroupParts.ig";
connectAttr "skinCluster11GroupId.id" "skinCluster11GroupParts.gi";
connectAttr "groupId50.msg" "tweakSet25.gn" -na;
connectAttr "camera_aim_circleShape_2.iog.og[3]" "tweakSet25.dsm" -na;
connectAttr "tweak25.msg" "tweakSet25.ub[0]";
connectAttr "camera_aim_circleShape_2Orig.ws" "groupParts50.ig";
connectAttr "groupId50.id" "groupParts50.gi";
connectAttr "cameras_holder.activeCamera" "isCameraPROJ.ft";
connectAttr "cameras_holder.activeCamera" "isCameraHD.ft";
connectAttr "skinCluster12GroupParts.og" "skinCluster12.ip[0].ig";
connectAttr "skinCluster12GroupId.id" "skinCluster12.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster12.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster12.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster12.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster12.bp";
connectAttr "groupParts52.og" "tweak26.ip[0].ig";
connectAttr "groupId52.id" "tweak26.ip[0].gi";
connectAttr "skinCluster12GroupId.msg" "skinCluster12Set.gn" -na;
connectAttr "JShape.iog.og[0]" "skinCluster12Set.dsm" -na;
connectAttr "skinCluster12.msg" "skinCluster12Set.ub[0]";
connectAttr "tweak26.og[0]" "skinCluster12GroupParts.ig";
connectAttr "skinCluster12GroupId.id" "skinCluster12GroupParts.gi";
connectAttr "groupId52.msg" "tweakSet26.gn" -na;
connectAttr "JShape.iog.og[1]" "tweakSet26.dsm" -na;
connectAttr "tweak26.msg" "tweakSet26.ub[0]";
connectAttr "JShapeOrig.ws" "groupParts52.ig";
connectAttr "groupId52.id" "groupParts52.gi";
connectAttr "skinCluster13GroupParts.og" "skinCluster13.ip[0].ig";
connectAttr "skinCluster13GroupId.id" "skinCluster13.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster13.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster13.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster13.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster13.bp";
connectAttr "groupParts54.og" "tweak27.ip[0].ig";
connectAttr "groupId54.id" "tweak27.ip[0].gi";
connectAttr "skinCluster13GroupId.msg" "skinCluster13Set.gn" -na;
connectAttr "OShape2.iog.og[0]" "skinCluster13Set.dsm" -na;
connectAttr "skinCluster13.msg" "skinCluster13Set.ub[0]";
connectAttr "tweak27.og[0]" "skinCluster13GroupParts.ig";
connectAttr "skinCluster13GroupId.id" "skinCluster13GroupParts.gi";
connectAttr "groupId54.msg" "tweakSet27.gn" -na;
connectAttr "OShape2.iog.og[1]" "tweakSet27.dsm" -na;
connectAttr "tweak27.msg" "tweakSet27.ub[0]";
connectAttr "OShape2Orig.ws" "groupParts54.ig";
connectAttr "groupId54.id" "groupParts54.gi";
connectAttr "skinCluster14GroupParts.og" "skinCluster14.ip[0].ig";
connectAttr "skinCluster14GroupId.id" "skinCluster14.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster14.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster14.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster14.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster14.bp";
connectAttr "groupParts56.og" "tweak28.ip[0].ig";
connectAttr "groupId56.id" "tweak28.ip[0].gi";
connectAttr "skinCluster14GroupId.msg" "skinCluster14Set.gn" -na;
connectAttr "OShape1.iog.og[0]" "skinCluster14Set.dsm" -na;
connectAttr "skinCluster14.msg" "skinCluster14Set.ub[0]";
connectAttr "tweak28.og[0]" "skinCluster14GroupParts.ig";
connectAttr "skinCluster14GroupId.id" "skinCluster14GroupParts.gi";
connectAttr "groupId56.msg" "tweakSet28.gn" -na;
connectAttr "OShape1.iog.og[1]" "tweakSet28.dsm" -na;
connectAttr "tweak28.msg" "tweakSet28.ub[0]";
connectAttr "OShape1Orig.ws" "groupParts56.ig";
connectAttr "groupId56.id" "groupParts56.gi";
connectAttr "skinCluster15GroupParts.og" "skinCluster15.ip[0].ig";
connectAttr "skinCluster15GroupId.id" "skinCluster15.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster15.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster15.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster15.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster15.bp";
connectAttr "groupParts58.og" "tweak29.ip[0].ig";
connectAttr "groupId58.id" "tweak29.ip[0].gi";
connectAttr "skinCluster15GroupId.msg" "skinCluster15Set.gn" -na;
connectAttr "RShape2.iog.og[0]" "skinCluster15Set.dsm" -na;
connectAttr "skinCluster15.msg" "skinCluster15Set.ub[0]";
connectAttr "tweak29.og[0]" "skinCluster15GroupParts.ig";
connectAttr "skinCluster15GroupId.id" "skinCluster15GroupParts.gi";
connectAttr "groupId58.msg" "tweakSet29.gn" -na;
connectAttr "RShape2.iog.og[1]" "tweakSet29.dsm" -na;
connectAttr "tweak29.msg" "tweakSet29.ub[0]";
connectAttr "RShape2Orig.ws" "groupParts58.ig";
connectAttr "groupId58.id" "groupParts58.gi";
connectAttr "skinCluster16GroupParts.og" "skinCluster16.ip[0].ig";
connectAttr "skinCluster16GroupId.id" "skinCluster16.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster16.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster16.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster16.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster16.bp";
connectAttr "groupParts60.og" "tweak30.ip[0].ig";
connectAttr "groupId60.id" "tweak30.ip[0].gi";
connectAttr "skinCluster16GroupId.msg" "skinCluster16Set.gn" -na;
connectAttr "RShape1.iog.og[0]" "skinCluster16Set.dsm" -na;
connectAttr "skinCluster16.msg" "skinCluster16Set.ub[0]";
connectAttr "tweak30.og[0]" "skinCluster16GroupParts.ig";
connectAttr "skinCluster16GroupId.id" "skinCluster16GroupParts.gi";
connectAttr "groupId60.msg" "tweakSet30.gn" -na;
connectAttr "RShape1.iog.og[1]" "tweakSet30.dsm" -na;
connectAttr "tweak30.msg" "tweakSet30.ub[0]";
connectAttr "RShape1Orig.ws" "groupParts60.ig";
connectAttr "groupId60.id" "groupParts60.gi";
connectAttr "skinCluster17GroupParts.og" "skinCluster17.ip[0].ig";
connectAttr "skinCluster17GroupId.id" "skinCluster17.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster17.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster17.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster17.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster17.bp";
connectAttr "groupParts62.og" "tweak31.ip[0].ig";
connectAttr "groupId62.id" "tweak31.ip[0].gi";
connectAttr "skinCluster17GroupId.msg" "skinCluster17Set.gn" -na;
connectAttr "PShape2.iog.og[0]" "skinCluster17Set.dsm" -na;
connectAttr "skinCluster17.msg" "skinCluster17Set.ub[0]";
connectAttr "tweak31.og[0]" "skinCluster17GroupParts.ig";
connectAttr "skinCluster17GroupId.id" "skinCluster17GroupParts.gi";
connectAttr "groupId62.msg" "tweakSet31.gn" -na;
connectAttr "PShape2.iog.og[1]" "tweakSet31.dsm" -na;
connectAttr "tweak31.msg" "tweakSet31.ub[0]";
connectAttr "PShape2Orig.ws" "groupParts62.ig";
connectAttr "groupId62.id" "groupParts62.gi";
connectAttr "skinCluster18GroupParts.og" "skinCluster18.ip[0].ig";
connectAttr "skinCluster18GroupId.id" "skinCluster18.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster18.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster18.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster18.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster18.bp";
connectAttr "groupParts64.og" "tweak32.ip[0].ig";
connectAttr "groupId64.id" "tweak32.ip[0].gi";
connectAttr "skinCluster18GroupId.msg" "skinCluster18Set.gn" -na;
connectAttr "PShape1.iog.og[0]" "skinCluster18Set.dsm" -na;
connectAttr "skinCluster18.msg" "skinCluster18Set.ub[0]";
connectAttr "tweak32.og[0]" "skinCluster18GroupParts.ig";
connectAttr "skinCluster18GroupId.id" "skinCluster18GroupParts.gi";
connectAttr "groupId64.msg" "tweakSet32.gn" -na;
connectAttr "PShape1.iog.og[1]" "tweakSet32.dsm" -na;
connectAttr "tweak32.msg" "tweakSet32.ub[0]";
connectAttr "PShape1Orig.ws" "groupParts64.ig";
connectAttr "groupId64.id" "groupParts64.gi";
connectAttr "skinCluster19GroupParts.og" "skinCluster19.ip[0].ig";
connectAttr "skinCluster19GroupId.id" "skinCluster19.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster19.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster19.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster19.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster19.bp";
connectAttr "groupParts66.og" "tweak33.ip[0].ig";
connectAttr "groupId66.id" "tweak33.ip[0].gi";
connectAttr "skinCluster19GroupId.msg" "skinCluster19Set.gn" -na;
connectAttr "HShape.iog.og[0]" "skinCluster19Set.dsm" -na;
connectAttr "skinCluster19.msg" "skinCluster19Set.ub[0]";
connectAttr "tweak33.og[0]" "skinCluster19GroupParts.ig";
connectAttr "skinCluster19GroupId.id" "skinCluster19GroupParts.gi";
connectAttr "groupId66.msg" "tweakSet33.gn" -na;
connectAttr "HShape.iog.og[1]" "tweakSet33.dsm" -na;
connectAttr "tweak33.msg" "tweakSet33.ub[0]";
connectAttr "HShapeOrig.ws" "groupParts66.ig";
connectAttr "groupId66.id" "groupParts66.gi";
connectAttr "skinCluster20GroupParts.og" "skinCluster20.ip[0].ig";
connectAttr "skinCluster20GroupId.id" "skinCluster20.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster20.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster20.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster20.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster20.bp";
connectAttr "groupParts68.og" "tweak34.ip[0].ig";
connectAttr "groupId68.id" "tweak34.ip[0].gi";
connectAttr "skinCluster20GroupId.msg" "skinCluster20Set.gn" -na;
connectAttr "DShape1.iog.og[0]" "skinCluster20Set.dsm" -na;
connectAttr "skinCluster20.msg" "skinCluster20Set.ub[0]";
connectAttr "tweak34.og[0]" "skinCluster20GroupParts.ig";
connectAttr "skinCluster20GroupId.id" "skinCluster20GroupParts.gi";
connectAttr "groupId68.msg" "tweakSet34.gn" -na;
connectAttr "DShape1.iog.og[1]" "tweakSet34.dsm" -na;
connectAttr "tweak34.msg" "tweakSet34.ub[0]";
connectAttr "DShape1Orig.ws" "groupParts68.ig";
connectAttr "groupId68.id" "groupParts68.gi";
connectAttr "skinCluster21GroupParts.og" "skinCluster21.ip[0].ig";
connectAttr "skinCluster21GroupId.id" "skinCluster21.ip[0].gi";
connectAttr "__controllersVisualScaler.wm" "skinCluster21.ma[0]";
connectAttr "__controllersVisualScaler.liw" "skinCluster21.lw[0]";
connectAttr "__controllersVisualScaler.obcc" "skinCluster21.ifcl[0]";
connectAttr "bindPose1.msg" "skinCluster21.bp";
connectAttr "groupParts70.og" "tweak35.ip[0].ig";
connectAttr "groupId70.id" "tweak35.ip[0].gi";
connectAttr "skinCluster21GroupId.msg" "skinCluster21Set.gn" -na;
connectAttr "DShape2.iog.og[0]" "skinCluster21Set.dsm" -na;
connectAttr "skinCluster21.msg" "skinCluster21Set.ub[0]";
connectAttr "tweak35.og[0]" "skinCluster21GroupParts.ig";
connectAttr "skinCluster21GroupId.id" "skinCluster21GroupParts.gi";
connectAttr "groupId70.msg" "tweakSet35.gn" -na;
connectAttr "DShape2.iog.og[1]" "tweakSet35.dsm" -na;
connectAttr "tweak35.msg" "tweakSet35.ub[0]";
connectAttr "DShape2Orig.ws" "groupParts70.ig";
connectAttr "groupId70.id" "groupParts70.gi";
connectAttr "cameraPROJ_controller.panSensitivity" "panX_sensitivityCorrection.i2x"
		;
connectAttr "cameraPROJ_controller.tx" "panX_sensitivityCorrection.i1x";
connectAttr "cameraPROJ_controller.panSensitivity" "panY_sensitivityCorrection.i2x"
		;
connectAttr "cameraPROJ_controller.ty" "panY_sensitivityCorrection.i1x";
connectAttr "cameraPROJ_controller.zoom" "fromZoomToScale.i2x";
connectAttr "cameraHD.iog" "RenderSet.dsm" -na;
connectAttr "cameraPROJ.iog" "RenderSet.dsm" -na;
connectAttr "cameraBG.iog" "RenderSet.dsm" -na;
connectAttr "__2dCameraMovementsData.iog" "RenderSet.dsm" -na;
connectAttr "isCameraHD.ocr" "cameraBGFocalLength_switch.ft";
connectAttr "cameraHD_controller.cameraBGFocalLength" "cameraBGFocalLength_switch.ctr"
		;
connectAttr "cameraPROJ_controller.cameraBGFocalLength" "cameraBGFocalLength_switch.cfr"
		;
connectAttr "cluster1GroupParts.og" "__cameraAim_camerasHolder_line_clusterCluster.ip[0].ig"
		;
connectAttr "cluster1GroupId.id" "__cameraAim_camerasHolder_line_clusterCluster.ip[0].gi"
		;
connectAttr "__cameraAim_camerasHolder_line_cluster.wm" "__cameraAim_camerasHolder_line_clusterCluster.ma"
		;
connectAttr "__cameraAim_camerasHolder_line_clusterShape.x" "__cameraAim_camerasHolder_line_clusterCluster.x"
		;
connectAttr "cluster1GroupId.msg" "cluster1Set.gn" -na;
connectAttr "__cameraAim_camerasHolder_lineShape.iog.og[3]" "cluster1Set.dsm" -na
		;
connectAttr "__cameraAim_camerasHolder_line_clusterCluster.msg" "cluster1Set.ub[0]"
		;
connectAttr "__cameraAim_camerasHolder_lineShape5Orig.ws" "groupParts72.ig";
connectAttr "groupId72.id" "groupParts72.gi";
connectAttr "groupParts72.og" "tweak36.ip[0].ig";
connectAttr "groupId72.id" "tweak36.ip[0].gi";
connectAttr "groupId72.msg" "tweakSet36.gn" -na;
connectAttr "__cameraAim_camerasHolder_lineShape.iog.og[4]" "tweakSet36.dsm" -na
		;
connectAttr "tweak36.msg" "tweakSet36.ub[0]";
connectAttr "tweak36.og[0]" "cluster1GroupParts.ig";
connectAttr "cluster1GroupId.id" "cluster1GroupParts.gi";
connectAttr "cluster2GroupParts.og" "__cameraAim_cameraHD_line_clusterCluster.ip[0].ig"
		;
connectAttr "cluster2GroupId.id" "__cameraAim_cameraHD_line_clusterCluster.ip[0].gi"
		;
connectAttr "__cameraAim_cameraHD_line_cluster.wm" "__cameraAim_cameraHD_line_clusterCluster.ma"
		;
connectAttr "__cameraAim_cameraHD_line_clusterShape.x" "__cameraAim_cameraHD_line_clusterCluster.x"
		;
connectAttr "groupParts74.og" "tweak37.ip[0].ig";
connectAttr "groupId74.id" "tweak37.ip[0].gi";
connectAttr "cluster2GroupId.msg" "cluster2Set.gn" -na;
connectAttr "__cameraAim_cameraHD_lineShape.iog.og[0]" "cluster2Set.dsm" -na;
connectAttr "__cameraAim_cameraHD_line_clusterCluster.msg" "cluster2Set.ub[0]";
connectAttr "tweak37.og[0]" "cluster2GroupParts.ig";
connectAttr "cluster2GroupId.id" "cluster2GroupParts.gi";
connectAttr "groupId74.msg" "tweakSet37.gn" -na;
connectAttr "__cameraAim_cameraHD_lineShape.iog.og[1]" "tweakSet37.dsm" -na;
connectAttr "tweak37.msg" "tweakSet37.ub[0]";
connectAttr "__cameraAim_cameraHD_lineShapeOrig.ws" "groupParts74.ig";
connectAttr "groupId74.id" "groupParts74.gi";
connectAttr "cluster2GroupParts1.og" "__cameraAim_cameraHD_line_clusterCluster1.ip[0].ig"
		;
connectAttr "cluster2GroupId1.id" "__cameraAim_cameraHD_line_clusterCluster1.ip[0].gi"
		;
connectAttr "__cameraAim_cameraPROJ_line_cluster.wm" "__cameraAim_cameraHD_line_clusterCluster1.ma"
		;
connectAttr "__cameraAim_cameraPROJ_line_clusterShape.x" "__cameraAim_cameraHD_line_clusterCluster1.x"
		;
connectAttr "cluster2GroupId1.msg" "cluster2Set1.gn" -na;
connectAttr "__cameraAim_cameraPROJ_lineShape.iog.og[0]" "cluster2Set1.dsm" -na;
connectAttr "__cameraAim_cameraHD_line_clusterCluster1.msg" "cluster2Set1.ub[0]"
		;
connectAttr "tweak38.og[0]" "cluster2GroupParts1.ig";
connectAttr "cluster2GroupId1.id" "cluster2GroupParts1.gi";
connectAttr "groupParts75.og" "tweak38.ip[0].ig";
connectAttr "groupId75.id" "tweak38.ip[0].gi";
connectAttr "groupId75.msg" "tweakSet38.gn" -na;
connectAttr "__cameraAim_cameraPROJ_lineShape.iog.og[1]" "tweakSet38.dsm" -na;
connectAttr "tweak38.msg" "tweakSet38.ub[0]";
connectAttr "__cameraAim_cameraPROJ_lineShapeOrig.ws" "groupParts75.ig";
connectAttr "groupId75.id" "groupParts75.gi";
connectAttr "cluster3GroupParts.og" "__focalCircles_HD_clusterCluster.ip[0].ig";
connectAttr "cluster3GroupId.id" "__focalCircles_HD_clusterCluster.ip[0].gi";
connectAttr "cluster3GroupParts1.og" "__focalCircles_HD_clusterCluster.ip[1].ig"
		;
connectAttr "cluster3GroupId1.id" "__focalCircles_HD_clusterCluster.ip[1].gi";
connectAttr "__focalCircles_HD_cluster.wm" "__focalCircles_HD_clusterCluster.ma"
		;
connectAttr "__focalCircles_HD_clusterShape.x" "__focalCircles_HD_clusterCluster.x"
		;
connectAttr "groupParts78.og" "tweak39.ip[0].ig";
connectAttr "groupId78.id" "tweak39.ip[0].gi";
connectAttr "groupParts79.og" "tweak40.ip[0].ig";
connectAttr "groupId79.id" "tweak40.ip[0].gi";
connectAttr "cluster3GroupId.msg" "cluster3Set.gn" -na;
connectAttr "cluster3GroupId1.msg" "cluster3Set.gn" -na;
connectAttr "focalCircle1HDShape.iog.og[0]" "cluster3Set.dsm" -na;
connectAttr "focalCircle2HDShape.iog.og[0]" "cluster3Set.dsm" -na;
connectAttr "__focalCircles_HD_clusterCluster.msg" "cluster3Set.ub[0]";
connectAttr "tweak39.og[0]" "cluster3GroupParts.ig";
connectAttr "cluster3GroupId.id" "cluster3GroupParts.gi";
connectAttr "tweak40.og[0]" "cluster3GroupParts1.ig";
connectAttr "cluster3GroupId1.id" "cluster3GroupParts1.gi";
connectAttr "groupId78.msg" "tweakSet39.gn" -na;
connectAttr "focalCircle1HDShape.iog.og[1]" "tweakSet39.dsm" -na;
connectAttr "tweak39.msg" "tweakSet39.ub[0]";
connectAttr "|camera_rig|camera_global|cameras_holder|cameraHD_controller|focalCircle1ShapeOrig.ws" "groupParts78.ig"
		;
connectAttr "groupId78.id" "groupParts78.gi";
connectAttr "groupId79.msg" "tweakSet40.gn" -na;
connectAttr "focalCircle2HDShape.iog.og[1]" "tweakSet40.dsm" -na;
connectAttr "tweak40.msg" "tweakSet40.ub[0]";
connectAttr "|camera_rig|camera_global|cameras_holder|cameraHD_controller|focalCircle2ShapeOrig.ws" "groupParts79.ig"
		;
connectAttr "groupId79.id" "groupParts79.gi";
connectAttr "cluster3GroupParts2.og" "ficalCirclesHD_clusterCluster1.ip[0].ig";
connectAttr "cluster3GroupId2.id" "ficalCirclesHD_clusterCluster1.ip[0].gi";
connectAttr "cluster3GroupParts3.og" "ficalCirclesHD_clusterCluster1.ip[1].ig";
connectAttr "cluster3GroupId3.id" "ficalCirclesHD_clusterCluster1.ip[1].gi";
connectAttr "__focalCircles_PROJ_cluster.wm" "ficalCirclesHD_clusterCluster1.ma"
		;
connectAttr "__focalCircles_PROJ_clusterShape.x" "ficalCirclesHD_clusterCluster1.x"
		;
connectAttr "cluster3GroupId2.msg" "cluster3Set1.gn" -na;
connectAttr "cluster3GroupId3.msg" "cluster3Set1.gn" -na;
connectAttr "focalCircle1PROJShape.iog.og[0]" "cluster3Set1.dsm" -na;
connectAttr "focalCircle2PROJShape.iog.og[0]" "cluster3Set1.dsm" -na;
connectAttr "ficalCirclesHD_clusterCluster1.msg" "cluster3Set1.ub[0]";
connectAttr "groupParts80.og" "tweak41.ip[0].ig";
connectAttr "groupId80.id" "tweak41.ip[0].gi";
connectAttr "groupId80.msg" "tweakSet41.gn" -na;
connectAttr "focalCircle2PROJShape.iog.og[1]" "tweakSet41.dsm" -na;
connectAttr "tweak41.msg" "tweakSet41.ub[0]";
connectAttr "|camera_rig|camera_global|cameras_holder|cameraPROJ_controller|focalCircle2ShapeOrig.ws" "groupParts80.ig"
		;
connectAttr "groupId80.id" "groupParts80.gi";
connectAttr "tweak42.og[0]" "cluster3GroupParts2.ig";
connectAttr "cluster3GroupId2.id" "cluster3GroupParts2.gi";
connectAttr "groupParts81.og" "tweak42.ip[0].ig";
connectAttr "groupId81.id" "tweak42.ip[0].gi";
connectAttr "groupId81.msg" "tweakSet42.gn" -na;
connectAttr "focalCircle1PROJShape.iog.og[1]" "tweakSet42.dsm" -na;
connectAttr "tweak42.msg" "tweakSet42.ub[0]";
connectAttr "|camera_rig|camera_global|cameras_holder|cameraPROJ_controller|focalCircle1ShapeOrig.ws" "groupParts81.ig"
		;
connectAttr "groupId81.id" "groupParts81.gi";
connectAttr "tweak41.og[0]" "cluster3GroupParts3.ig";
connectAttr "cluster3GroupId3.id" "cluster3GroupParts3.gi";
connectAttr "cameraHD_controller.focalLength" "normalizeFocalHD.i1x";
connectAttr "normalizeFocalHD.ox" "globalScaleHD.i1";
connectAttr "cameras_holder.controllers_size" "globalScaleHD.i2";
connectAttr "cameras_holder.controllers_size" "globalScalePROJ.i1";
connectAttr "normalizeFocalPROJ.ox" "globalScalePROJ.i2";
connectAttr "cameraPROJ_controller.focalLength" "normalizeFocalPROJ.i1x";
connectAttr "cameraBGShape.fl" "cameraBGFocalFactor.i2x";
connectAttr "hyperView1.msg" "nodeEditorPanel2Info.b[0]";
connectAttr "hyperLayout1.msg" "hyperView1.hl";
connectAttr "plate_pivotShape_0.msg" "hyperLayout1.hyp[0].dn";
connectAttr "plate_pivotShape_2.msg" "hyperLayout1.hyp[1].dn";
connectAttr "plate_pivot.msg" "hyperLayout1.hyp[2].dn";
connectAttr "plate_pivotShape_1.msg" "hyperLayout1.hyp[3].dn";
connectAttr "isCameraPROJ.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "isCameraHD.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "panX_sensitivityCorrection.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "panY_sensitivityCorrection.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "fromZoomToScale.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "cameraBGFocalLength_switch.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "normalizeFocalHD.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "globalScaleHD.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "globalScalePROJ.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "normalizeFocalPROJ.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "cameraBGFocalFactor.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":perspShape.msg" ":defaultRenderGlobals.sc";
// End of [10] bgd_camera.ma
