//Maya ASCII 2015 scene
//Name: yak_camera.ma
//Last modified: Fri, Aug 26, 2016 02:51:36 PM
//Codeset: 1252
requires maya "2015";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2015.0.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2015";
fileInfo "version" "2015";
fileInfo "cutIdentifier" "201503261530-955654";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 32.843272291699002 26.539411726832967 25.919876967573217 ;
	setAttr ".r" -type "double3" -38.738352725199952 -2111.3999999994762 -4.8094625974083965e-015 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 50.197272096592116;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -5.3290705182007514e-015 0 7.0747332572936994 ;
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
	setAttr ".t" -type "double3" 25.080848852563353 -9.5429056674695651 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 120.47446897292539;
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
	addAttr -ci true -sn "OPTIONS" -ln "OPTIONS" -min 0 -max 0 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "show_guide" -ln "show_guide" -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "controllersSize" -ln "controllersSize" -dv 1 -min 0.1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -cb on ".OPTIONS";
	setAttr -cb on ".show_guide" 1;
	setAttr -cb on ".controllersSize";
createNode nurbsCurve -n "camera_globalShape" -p "camera_global";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".tw" yes;
createNode transform -n "cameras_holder" -p "camera_global";
	addAttr -ci true -sn "FOCALS" -ln "FOCALS" -min 0 -max 1 -en "--------------" -at "enum";
	addAttr -ci true -sn "HD_focal" -ln "HD_focal" -dv 60 -at "double";
	addAttr -ci true -sn "PROJ_focal" -ln "PROJ_focal" -dv 60 -at "double";
	addAttr -ci true -sn "CLIPPING_PLANES" -ln "CLIPPING_PLANES" -min 0 -max 1 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "near" -ln "near" -dv 0.1 -at "double";
	addAttr -ci true -sn "far" -ln "far" -dv 10000 -at "double";
	addAttr -ci true -sn "DISPLAY" -ln "DISPLAY" -min 0 -max 0 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "HD_gate" -ln "HD_gate" -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "HD_overscan" -ln "HD_overscan" -dv 1 -at "double";
	addAttr -ci true -sn "PROJ_gate" -ln "PROJ_gate" -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "PROJ_overscan" -ln "PROJ_overscan" -dv 1 -at "double";
	addAttr -ci true -sn "focalCorrection" -ln "focalCorrection" -at "double";
	setAttr -l on -k off ".v";
	setAttr ".ovc" 14;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -cb on ".FOCALS";
	setAttr -k on ".HD_focal";
	setAttr -k on ".PROJ_focal";
	setAttr -cb on ".CLIPPING_PLANES";
	setAttr -cb on ".near";
	setAttr -cb on ".far";
	setAttr -cb on ".DISPLAY";
	setAttr -cb on ".HD_gate" 1;
	setAttr -cb on ".HD_overscan";
	setAttr -cb on ".PROJ_gate" 1;
	setAttr -cb on ".PROJ_overscan";
createNode nurbsCurve -n "cameras_holderShape" -p "cameras_holder";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode transform -n "cameraPROJ" -p "cameras_holder";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 4.3520742565306136e-014 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode camera -n "cameraPROJShape" -p "cameraPROJ";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.7777 1 ;
	setAttr ".ff" 3;
	setAttr ".coi" 5.0000000000000435;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
	setAttr ".dgo" 1;
	setAttr ".dgc" -type "float3" 0 0 0 ;
createNode transform -n "cameraHD_controller" -p "cameras_holder";
	addAttr -ci true -sn "gateMask" -ln "gateMask" -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "overScan" -ln "overScan" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "cameraGuides" -ln "cameraGuides" -min 0 -max 1 -en "OFF:ON" 
		-at "enum";
	addAttr -ci true -sn "nearClipPlane" -ln "nearClipPlane" -dv 0.1 -min 0.1 -at "double";
	addAttr -ci true -sn "farClipPlane" -ln "farClipPlane" -dv 10000 -min 1 -at "double";
	addAttr -ci true -sn "MOVES_2D" -ln "MOVES_2D" -min 0 -max 1 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "panX" -ln "panX" -at "double";
	addAttr -ci true -sn "panY" -ln "panY" -at "double";
	addAttr -ci true -sn "roll" -ln "roll" -nn "Roll (viewport center)" -at "double";
	addAttr -ci true -sn "zoom" -ln "zoom" -nn "Zoom (viewport center)" -dv 1 -min 0 
		-at "double";
	addAttr -ci true -sn "zoomNew" -ln "zoomNew" -nn "Zoom (camera position)" -dv 1 
		-min 0 -at "double";
	addAttr -ci true -sn "panSensitivity" -ln "panSensitivity" -dv 1 -min 1 -at "double";
	addAttr -ci true -sn "IMAGE_PLANE" -ln "IMAGE_PLANE" -min 0 -max 0 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "opacity" -ln "opacity" -dv 50 -min 0 -max 100 -at "double";
	addAttr -ci true -sn "show" -ln "show" -min 0 -max 1 -en "OFF:ON" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".gateMask" 1;
	setAttr ".cameraGuides" 1;
	setAttr -cb on ".MOVES_2D";
	setAttr -k on ".panX";
	setAttr -k on ".panY";
	setAttr -k on ".roll";
	setAttr -k on ".zoom";
	setAttr -k on ".zoomNew";
	setAttr -cb on ".panSensitivity" 100;
	setAttr -cb on ".IMAGE_PLANE";
	setAttr -cb on ".opacity";
	setAttr -cb on ".show" 1;
createNode mesh -n "XXXShape" -p "cameraHD_controller";
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
	setAttr ".sdt" 0;
	setAttr ".ugsdt" no;
	setAttr ".vcs" 2;
createNode transform -n "cameraHD" -p "cameraHD_controller";
	setAttr ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode camera -n "cameraHDShape" -p "cameraHD";
	setAttr -k off ".v";
	setAttr ".ovc" 21;
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.7777 1 ;
	setAttr ".ct" -type "double2" 0 2.102142178599481e-018 ;
	setAttr -l on ".ff" 3;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
	setAttr ".dgo" 1;
	setAttr ".dgc" -type "float3" 0 0 0 ;
createNode mesh -n "XXXShapeOrig" -p "cameraHD_controller";
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
	setAttr ".sdt" 0;
	setAttr ".ugsdt" no;
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
createNode nurbsCurve -n "cameraHDLineShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "cameraHD_2dShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "nurbsCircleShape4" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "fake2dLineShape" -p "cameraHD_controller";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode transform -n "cameraHD_rig" -p "cameraHD_controller";
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
createNode transform -n "cameraHD_2d_cluster" -p "cameraHD_rig";
	setAttr ".v" no;
createNode clusterHandle -n "cameraHD_2d_clusterShape" -p "cameraHD_2d_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0.5830148458480835 1.1563360691070557 7.1626685708761215 ;
createNode transform -n "cameraLine_cluster1" -p "cameraHD_rig";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -11.75 0.25 -5.75 ;
	setAttr ".sp" -type "double3" -11.75 0.25 -5.75 ;
createNode transform -n "cluster7Handle" -p "cameraLine_cluster1";
	setAttr ".rp" -type "double3" -12 0 -6 ;
	setAttr ".sp" -type "double3" -12 0 -6 ;
createNode clusterHandle -n "cluster7HandleShape" -p "cluster7Handle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -12 0 -6 ;
createNode pointConstraint -n "cluster7Handle_pointConstraint1" -p "cluster7Handle";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "cameraHD_controllerW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
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
	setAttr ".rst" -type "double3" 12 0 6 ;
	setAttr -k on ".w0";
createNode transform -n "cameraLine_Cluster2" -p "cameraHD_rig";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.25 0.25 -5.75 ;
	setAttr ".sp" -type "double3" 0.25 0.25 -5.75 ;
createNode transform -n "cluster8Handle" -p "cameraLine_Cluster2";
	setAttr ".rp" -type "double3" 0 0 -6 ;
	setAttr ".sp" -type "double3" 0 0 -6 ;
createNode clusterHandle -n "cluster8HandleShape" -p "cluster8Handle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 0 -6 ;
createNode pointConstraint -n "cluster8Handle_pointConstraint1" -p "cluster8Handle";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "cameras_holderW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
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
	setAttr ".rst" -type "double3" 0 0 6 ;
	setAttr -k on ".w0";
createNode transform -n "mirino_cluster" -p "cameraHD_rig";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 0.25 0.25000000000000311 0.25000000000000189 ;
	setAttr ".sp" -type "double3" 0.25 0.25000000000000311 0.25000000000000189 ;
createNode transform -n "cluster9Handle" -p "mirino_cluster";
	setAttr ".rp" -type "double3" 0.016358610921655137 3.1086244689504383e-015 1.856615327255014e-015 ;
	setAttr ".sp" -type "double3" 0.016358610921655137 3.1086244689504383e-015 1.856615327255014e-015 ;
createNode clusterHandle -n "cluster9HandleShape" -p "cluster9Handle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 3.1086244689504383e-015 1.856615327255014e-015 ;
createNode transform -n "fake2dLineCluster1" -p "cameraHD_rig";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 12.25 0.25 0.25 ;
	setAttr ".sp" -type "double3" 12.25 0.25 0.25 ;
createNode transform -n "cluster10Handle" -p "fake2dLineCluster1";
	setAttr ".rp" -type "double3" 12 0 0 ;
	setAttr ".sp" -type "double3" 12 0 0 ;
createNode clusterHandle -n "cluster10HandleShape" -p "cluster10Handle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 12 0 0 ;
createNode pointConstraint -n "cluster10Handle_pointConstraint1" -p "cluster10Handle";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "cameraHD_controllerW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
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
	setAttr ".rst" -type "double3" -12 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "fake2dLineCluster2" -p "cameraHD_rig";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" -11.75 0.25 0.25 ;
	setAttr ".sp" -type "double3" -11.75 0.25 0.25 ;
createNode transform -n "cluster11Handle" -p "fake2dLineCluster2";
	setAttr ".rp" -type "double3" -12 0 0 ;
	setAttr ".sp" -type "double3" -12 0 0 ;
createNode clusterHandle -n "cluster11HandleShape" -p "cluster11Handle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -12 0 0 ;
createNode pointConstraint -n "cluster11Handle_pointConstraint1" -p "cluster11Handle";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "fake2dLocatorW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
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
	setAttr ".rst" -type "double3" 12 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "fake2dLocator" -p "cameraHD_rig";
	setAttr -l on -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "fake2dLocatorShape" -p "fake2dLocator";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "nurbsCircleShape4" -p "cameras_holder";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".tw" yes;
createNode nurbsCurve -n "cameras_holderShapeOrig" -p "cameras_holder";
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
createNode nurbsCurve -n "nurbsCircleShape4Orig" -p "cameras_holder";
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
createNode transform -n "cameras_holder_rig" -p "cameras_holder";
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
createNode aimConstraint -n "cameras_holder_aimConstraint1" -p "cameras_holder_rig";
	addAttr -ci true -sn "w0" -ln "camera_aimW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
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
	setAttr -k on ".w0";
createNode transform -n "holder_cluster" -p "cameras_holder_rig";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0.25 0.25000000000000799 0.25 ;
	setAttr ".sp" -type "double3" 0.25 0.25000000000000799 0.25 ;
createNode transform -n "holder_cluster" -p "|camera_rig|camera_global|cameras_holder|cameras_holder_rig|holder_cluster";
	setAttr ".rp" -type "double3" 0 7.9936057773011271e-015 -1.9721522630525295e-030 ;
	setAttr ".sp" -type "double3" 0 7.9936057773011271e-015 -1.9721522630525295e-030 ;
createNode clusterHandle -n "holder_clusterShape" -p "|camera_rig|camera_global|cameras_holder|cameras_holder_rig|holder_cluster|holder_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 7.9936057773011271e-015 -1.9721522630525295e-030 ;
createNode transform -n "camera_aim" -p "camera_global";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "camera_aimShape" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".sech" no;
	setAttr ".tw" yes;
createNode nurbsCurve -n "curveShape3" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "curveShape2" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "nurbsCircleShape3" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "nurbsCircleShape2" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "camera_aimShapeOrig" -p "camera_aim";
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
createNode nurbsCurve -n "curveShape3Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		6.2878082338675725 -7.0485897883296378e-016 -5.2845452833070624e-016
		-6.2878082338675725 1.3344866606488197e-015 -5.2845452833070723e-016
		;
createNode nurbsCurve -n "curveShape2Orig" -p "camera_aim";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 -4.6101281456295222 1.2842478815289644e-015
		0 4.6101281456295222 -1.2842478815289646e-015
		;
createNode nurbsCurve -n "nurbsCircleShape3Orig" -p "camera_aim";
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
createNode nurbsCurve -n "nurbsCircleShape2Orig" -p "camera_aim";
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
createNode nurbsCurve -n "aimLineShape" -p "camera_aim";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr -av ".iog[0].og[1].gco";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode transform -n "camera_aim_rig" -p "camera_aim";
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
createNode orientConstraint -n "camera_aim_orientConstraint1" -p "camera_aim_rig";
	addAttr -ci true -k true -sn "w0" -ln "cameras_holderW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
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
	setAttr -k on ".w0";
createNode transform -n "aim_cluster" -p "camera_aim_rig";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0.25 0.25 -0.98620010314736728 ;
	setAttr ".sp" -type "double3" 0.25 0.25 -0.98620010314736728 ;
createNode transform -n "aim_cluster" -p "|camera_rig|camera_global|camera_aim|camera_aim_rig|aim_cluster";
createNode clusterHandle -n "aim_clusterShape" -p "|camera_rig|camera_global|camera_aim|camera_aim_rig|aim_cluster|aim_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 0 -1.2362001031473673 ;
createNode transform -n "aimLineCluster1" -p "camera_aim_rig";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0.25 0.25 -11.75 ;
	setAttr ".sp" -type "double3" 0.25 0.25 -11.75 ;
createNode transform -n "cluster5Handle" -p "aimLineCluster1";
	setAttr ".rp" -type "double3" 0 0 -12 ;
	setAttr ".sp" -type "double3" 0 0 -12 ;
createNode clusterHandle -n "cluster5HandleShape" -p "cluster5Handle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 0 0 -12 ;
createNode pointConstraint -n "cluster5Handle_pointConstraint1" -p "cluster5Handle";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "cameras_holderW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
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
	setAttr ".rst" -type "double3" 0 0 12 ;
	setAttr -k on ".w0";
createNode transform -n "animLineCluster2" -p "camera_aim_rig";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0.25 0.25 0.25 ;
	setAttr ".sp" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "cluster6Handle" -p "animLineCluster2";
createNode clusterHandle -n "cluster6HandleShape" -p "cluster6Handle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
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
createNode transform -n "camera_global_rig" -p "camera_global";
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
createNode transform -n "upLocator" -p "camera_global_rig";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".t" -type "double3" 0 34.036392116963725 0 ;
	setAttr ".s" -type "double3" 4.9598516817404592 4.9598516817404592 4.9598516817404592 ;
createNode locator -n "upLocatorShape" -p "upLocator";
	setAttr -k off ".v";
createNode transform -n "global_cluster" -p "camera_global_rig";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 0.24999999999999467 0.25 0.25 ;
	setAttr ".sp" -type "double3" 0.24999999999999467 0.25 0.25 ;
createNode transform -n "global_cluster" -p "|camera_rig|camera_global|camera_global_rig|global_cluster";
	setAttr ".rp" -type "double3" -5.3290705182007514e-015 0 0 ;
	setAttr ".sp" -type "double3" -5.3290705182007514e-015 0 0 ;
createNode clusterHandle -n "global_clusterShape" -p "|camera_rig|camera_global|camera_global_rig|global_cluster|global_cluster";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -5.3290705182007514e-015 0 0 ;
createNode transform -n "rig_extra" -p "camera_rig";
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
createNode transform -n "plateCtrl" -p "rig_extra";
	addAttr -ci true -sn "showResizingArrows" -ln "showResizingArrows" -min 0 -max 
		1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "ROTATION_OFFSET" -ln "ROTATION_OFFSET" -min 0 -max 0 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "rotX" -ln "rotX" -at "double";
	addAttr -ci true -sn "rotY" -ln "rotY" -at "double";
	addAttr -ci true -sn "rotZ" -ln "rotZ" -at "double";
	addAttr -ci true -sn "PLATE_OPTIONS" -ln "PLATE_OPTIONS" -min 0 -max 0 -en "--------------" 
		-at "enum";
	addAttr -ci true -sn "lockPlate" -ln "lockPlate" -min 0 -max 1 -en "OFF:ON" -at "enum";
	addAttr -ci true -sn "showPlate" -ln "showPlate" -min 0 -max 1 -en "OFF:ON" -at "enum";
	setAttr -cb on ".ROTATION_OFFSET";
	setAttr -k on ".rotX";
	setAttr -k on ".rotY";
	setAttr -k on ".rotZ";
	setAttr -cb on ".PLATE_OPTIONS";
	setAttr -k on ".lockPlate" 1;
	setAttr -k on ".showPlate" 1;
createNode nurbsCurve -n "plateCtrlShape" -p "plateCtrl";
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
createNode nurbsCurve -n "plateCtrlShape1" -p "plateCtrl";
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
createNode transform -n "plusPlate" -p "plateCtrl";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 20.872834165681169 -15.246921914802668 2.6882918661949806 ;
	setAttr ".sp" -type "double3" 20.872834165681169 -15.246921914802668 2.6882918661949806 ;
createNode nurbsCurve -n "plusPlateShape" -p "plusPlate";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		19.879436246682246 -16.240319833801586 2.6882918661949815
		19.879436246682246 -18.227115671799417 2.6882918661949824
		21.866232084680085 -18.227115671799417 2.6882918661949824
		21.866232084680085 -16.240319833801586 2.6882918661949815
		23.853027922677924 -16.240319833801586 2.6882918661949815
		23.853027922677924 -14.253523995803748 2.6882918661949815
		21.866232084680085 -14.253523995803748 2.6882918661949815
		21.866232084680085 -12.266728157805913 2.6882918661949806
		19.879436246682246 -12.266728157805913 2.6882918661949806
		19.879436246682246 -14.253523995803748 2.6882918661949815
		17.892640408684411 -14.253523995803748 2.6882918661949815
		17.892640408684411 -16.240319833801586 2.6882918661949815
		19.879436246682246 -16.240319833801586 2.6882918661949815
		;
createNode transform -n "minusPlate" -p "plateCtrl";
	setAttr ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 20.925137530612343 -15.232547859228086 2.6882918661949806 ;
	setAttr ".sp" -type "double3" 20.925137530612343 -15.232547859228086 2.6882918661949806 ;
createNode nurbsCurve -n "minusPlateShape" -p "minusPlate";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		17.944943773615588 -14.23914994022917 2.6882918661949806
		23.905331287609094 -14.23914994022917 2.6882918661949806
		23.905331287609094 -16.225945778227008 2.6882918661949806
		17.944943773615588 -16.225945778227008 2.6882918661949806
		17.944943773615588 -14.23914994022917 2.6882918661949806
		;
createNode transform -n "resizingArrows" -p "plateCtrl";
	setAttr ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "resizingUp" -p "resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingUpShape" -p "resizingUp";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		2.0415231224593891 4.5330919517181135e-016 -1.0065486115080876e-031
		-2.0415231224593891 -4.5330919517181135e-016 1.0065486115080876e-031
		-2.0415231224593899 4.0830462449187772 -9.0661839034362251e-016
		-4.083046244918779 4.0830462449187772 -9.0661839034362251e-016
		-1.8132367806872454e-015 8.1660924898375562 -1.8132367806872454e-015
		4.0830462449187772 4.083046244918779 -9.066183903436229e-016
		2.0415231224593882 4.083046244918779 -9.066183903436229e-016
		2.0415231224593891 4.5330919517181135e-016 -1.0065486115080876e-031
		;
createNode transform -n "resizingDown" -p "resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingDownShape" -p "resizingDown";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		-2.0415231224593891 4.5330919517181135e-016 -1.0065486115080876e-031
		2.0415231224593891 -4.5330919517181135e-016 1.0065486115080876e-031
		2.0415231224593882 -4.083046244918779 9.066183903436229e-016
		4.0830462449187772 -4.083046244918779 9.066183903436229e-016
		-1.8132367806872454e-015 -8.1660924898375562 1.8132367806872454e-015
		-4.083046244918779 -4.0830462449187772 9.0661839034362251e-016
		-2.0415231224593899 -4.0830462449187772 9.0661839034362251e-016
		-2.0415231224593891 4.5330919517181135e-016 -1.0065486115080876e-031
		;
createNode transform -n "resizingRight" -p "resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingRightShape" -p "resizingRight";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0 2.0415231224593891 -4.5330919517181135e-016
		0 -2.0415231224593891 4.5330919517181135e-016
		4.0830462449187781 -2.0415231224593891 4.5330919517181135e-016
		4.0830462449187781 -4.0830462449187781 9.066183903436227e-016
		8.1660924898375562 0 0
		4.0830462449187781 4.0830462449187781 -9.066183903436227e-016
		4.0830462449187781 2.0415231224593891 -4.5330919517181135e-016
		0 2.0415231224593891 -4.5330919517181135e-016
		;
createNode transform -n "resizingLeft" -p "resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingLeftShape" -p "resizingLeft";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0 2.0415231224593891 -4.5330919517181135e-016
		0 -2.0415231224593891 4.5330919517181135e-016
		-4.0830462449187781 -2.0415231224593891 4.5330919517181135e-016
		-4.0830462449187781 -4.0830462449187781 9.066183903436227e-016
		-8.1660924898375562 0 0
		-4.0830462449187781 4.0830462449187781 -9.066183903436227e-016
		-4.0830462449187781 2.0415231224593891 -4.5330919517181135e-016
		0 2.0415231224593891 -4.5330919517181135e-016
		;
createNode transform -n "fake2dLine" -p "rig_extra";
	setAttr -l on ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode nurbsCurve -n "fake2dLineShapeOrig" -p "fake2dLine";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-12 0 0
		12 0 0
		;
createNode transform -n "aimLine" -p "rig_extra";
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
createNode nurbsCurve -n "aimLineShapeOrig" -p "aimLine";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 -12
		0 0 0
		;
createNode transform -n "cameraHDLine" -p "rig_extra";
	setAttr ".v" no;
createNode nurbsCurve -n "cameraHDLineShapeOrig" -p "cameraHDLine";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		0 0 -6
		-12 0 -6
		;
createNode transform -n "cameraHD_2d" -p "rig_extra";
	setAttr ".v" no;
	setAttr ".ovc" 14;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode nurbsCurve -n "cameraHD_2dShapeOrig" -p "cameraHD_2d";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 82 0 no 3
		87 0 0 0 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7 8 8 8 9 9 9 10 10 10 11
		 11 11 12 12 12 13 13 13 14 14 14 15 15 15 16 16 16 17 17 17 18 18 18 19 19 19 20
		 20 20 21 21 21 22 22 22 23 23 23 24 24 24 25 25 25 26 26 26 27 27 27 28 28 28
		85
		-0.54455122447199555 -2.6467758846832625 1.1670064510026038e-015
		-0.54455122447199555 -2.6467758846832625 1.1670064510026038e-015
		1.8296129512448315e-016 -3.4902026575867962 1.4546188654165929e-015
		1.8296129512448315e-016 -3.4902026575867962 1.4546188654165929e-015
		1.8296129512448315e-016 -3.4902026575867962 1.4546188654165929e-015
		1.8296129512448315e-016 -3.4902026575867962 3.2309757048168433e-015
		1.8296129512448315e-016 -3.4902026575867962 3.2309757048168433e-015
		1.8296129512448315e-016 -3.4902026575867962 3.2309757048168433e-015
		6.4852362511850074e-017 -3.4902026575867962 2.1230087434288778e-015
		6.4852362511850074e-017 -3.4902026575867962 2.1230087434288778e-015
		6.4852362511850074e-017 -3.4902026575867962 2.1230087434288778e-015
		1.8296129512448315e-016 -3.4902026575867962 3.2309757048168433e-015
		1.8296129512448315e-016 -3.4902026575867962 3.2309757048168433e-015
		1.8296129512448315e-016 -3.4902026575867962 3.2309757048168433e-015
		1.8296129512448315e-016 -3.4902026575867962 1.4546188654165931e-015
		1.8296129512448315e-016 -3.4902026575867962 1.4546188654165931e-015
		1.8296129512448315e-016 -3.4902026575867962 1.4546188654165931e-015
		0.54455122447199555 -2.6467758846832625 1.1670064510026038e-015
		0.54455122447199555 -2.6467758846832625 1.1670064510026038e-015
		0.54455122447199555 -2.6467758846832625 1.1670064510026038e-015
		2.3946161302690543 -2.4036363836241974 1.0001540014950941e-015
		3.1162273928293303 -0.51211713643772294 3.8900215033420124e-016
		3.1162273928293303 -0.51211713643772294 3.8900215033420124e-016
		3.9757551390631938 1.9148202303728006e-016 2.02994127926933e-015
		3.9757551390631938 1.9148202303728006e-016 2.02994127926933e-015
		3.9757551390631938 1.9148202303728006e-016 2.02994127926933e-015
		3.9757551390631938 1.9148202303728006e-016 4.05988255853866e-015
		3.9757551390631938 1.9148202303728006e-016 4.05988255853866e-015
		3.9757551390631938 1.9148202303728006e-016 4.05988255853866e-015
		3.9757551390631938 1.8995528415099325e-016 -3.2051057963325293e-031
		3.9757551390631938 1.8995528415099325e-016 -3.2051057963325293e-031
		3.9757551390631938 1.8995528415099325e-016 -3.2051057963325293e-031
		3.9757551390631938 1.9148202303728006e-016 3.0455447990623427e-015
		3.9757551390631938 1.9148202303728006e-016 3.0455447990623427e-015
		3.9757551390631938 1.9148202303728006e-016 3.0455447990623427e-015
		3.9757551390631938 1.9148202303728006e-016 1.5227723995311713e-015
		3.9757551390631938 1.9148202303728006e-016 1.5227723995311713e-015
		3.9757551390631938 1.9148202303728006e-016 1.5227723995311713e-015
		3.1162273928293303 0.51211713643772294 -3.8900215033420124e-016
		3.1162273928293303 0.51211713643772294 -3.8900215033420124e-016
		2.3946161302690543 2.4036363836241987 -1.0001540014950947e-015
		0.54455122447199555 2.6467758846832625 -1.1670064510026038e-015
		0.54455122447199555 2.6467758846832625 -1.1670064510026038e-015
		0.54455122447199555 2.6467758846832625 -1.1670064510026038e-015
		0 3.4902026575868024 -1.4546188654165931e-015
		0 3.4902026575868024 -1.4546188654165931e-015
		0 3.4902026575868024 -1.4546188654165931e-015
		0 3.4902026575868024 3.2173797398365759e-016
		0 3.4902026575868024 3.2173797398365759e-016
		0 3.4902026575868024 3.2173797398365759e-016
		6.4852362511850074e-017 3.4902026575868024 -2.1230087434288798e-015
		6.4852362511850074e-017 3.4902026575868024 -2.1230087434288798e-015
		6.4852362511850074e-017 3.4902026575868024 -2.1230087434288798e-015
		0 3.4902026575868024 3.2173797398365739e-016
		0 3.4902026575868024 3.2173797398365739e-016
		0 3.4902026575868024 3.2173797398365739e-016
		0 3.4902026575868024 -1.4546188654165931e-015
		0 3.4902026575868024 -1.4546188654165931e-015
		0 3.4902026575868024 -1.4546188654165931e-015
		-0.54455122447199555 2.6467758846832625 -1.1670064510026038e-015
		-0.54455122447199555 2.6467758846832625 -1.1670064510026038e-015
		-0.54455122447199555 2.6467758846832625 -1.1670064510026038e-015
		-2.3946161302690543 2.4036363836241987 -1.0001540014950947e-015
		-3.1167060748674325 0.51211713643772294 -3.8900215033420124e-016
		-3.1167060748674325 0.51211713643772294 -3.8900215033420124e-016
		-3.9430379172198835 1.2765468202485338e-016 1.5227723995311721e-015
		-3.9430379172198835 1.2765468202485338e-016 1.5227723995311721e-015
		-3.9430379172198835 1.2765468202485338e-016 1.5227723995311721e-015
		-3.9430379172198835 1.2765468202485338e-016 3.0455447990623443e-015
		-3.9430379172198835 1.2765468202485338e-016 3.0455447990623443e-015
		-3.9430379172198835 1.2765468202485338e-016 3.0455447990623443e-015
		-3.9430379172198835 1.3909884026734197e-016 -2.9589855569189435e-031
		-3.9430379172198835 1.3909884026734197e-016 -2.9589855569189435e-031
		-3.9430379172198835 1.3909884026734197e-016 -2.9589855569189435e-031
		-3.9430379172198835 1.2765468202485338e-016 5.8362393979389081e-015
		-3.9430379172198835 1.2765468202485338e-016 5.8362393979389081e-015
		-3.9430379172198835 1.2765468202485338e-016 5.8362393979389081e-015
		-3.9430379172198835 1.2765468202485338e-016 3.8062981186695789e-015
		-3.9430379172198835 1.2765468202485338e-016 3.8062981186695789e-015
		-3.9430379172198835 1.2765468202485338e-016 3.8062981186695789e-015
		-3.1167060748674325 -0.51211713643772294 3.8900215033420124e-016
		-3.1167060748674325 -0.51211713643772294 3.8900215033420124e-016
		-2.3946161302690543 -2.4036363836241974 1.0001540014950941e-015
		-0.54455122447199555 -2.6467758846832625 1.1670064510026038e-015
		-0.54455122447199555 -2.6467758846832625 1.1670064510026038e-015
		;
createNode nurbsCurve -n "nurbsCircleShape4Orig" -p "cameraHD_2d";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.8323876579101481 1.4804621913774618 -4.9997924162674402e-016
		-1.0373205522870559e-016 2.0936897096266005 -7.0707742441355579e-016
		-1.8323876579101455 1.480462191377462 -4.9997924162674422e-016
		-2.5913874773416019 2.2294959097400664e-016 -1.9725319630782583e-031
		-1.8323876579101464 -1.4804621913774618 4.9997924162674412e-016
		-3.2555220049748239e-016 -2.0936897096266009 7.0707742441355599e-016
		1.8323876579101448 -1.4804621913774623 4.9997924162674422e-016
		2.5913874773416019 -7.7719386348709397e-016 3.8741281557958807e-031
		1.8323876579101481 1.4804621913774618 -4.9997924162674402e-016
		-1.0373205522870559e-016 2.0936897096266005 -7.0707742441355579e-016
		-1.8323876579101455 1.480462191377462 -4.9997924162674422e-016
		;
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode hyperGraphInfo -n "nodeEditorPanel2Info";
createNode hyperView -n "hyperView1";
	setAttr ".vl" -type "double2" 1876.0450610036921 -2057.6909899962066 ;
	setAttr ".vh" -type "double2" 3545.2136248435704 -1181.2028947581114 ;
	setAttr ".dag" no;
createNode hyperGraphInfo -n "nodeEditorPanel1Info";
createNode hyperView -n "hyperView2";
	setAttr ".vl" -type "double2" -119.48711735974571 -303.61688551228974 ;
	setAttr ".vh" -type "double2" 69.881141508840145 230.13347244916682 ;
	setAttr ".dag" no;
createNode hyperGraphInfo -n "nodeEditorPanel3Info";
createNode hyperView -n "hyperView3";
	setAttr ".vl" -type "double2" -214.4360516280434 -407.14285714285717 ;
	setAttr ".vh" -type "double2" 627.53128972328147 83.333333333333357 ;
	setAttr ".dag" no;
createNode hyperGraphInfo -n "yak_camera_SHAPE_nodeEditorPanel1Info";
createNode hyperView -n "yak_camera_SHAPE_hyperView1";
	setAttr ".dag" no;
createNode hyperLayout -n "yak_camera_SHAPE_hyperLayout1";
	setAttr ".ihi" 0;
	setAttr -s 10 ".hyp";
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".anf" yes;
createNode hyperGraphInfo -n "yak_camera_SHAPE_nodeEditorPanel2Info";
createNode hyperView -n "yak_camera_SHAPE_hyperView2";
	setAttr ".vl" -type "double2" -362.71401454505497 -659.42478948324958 ;
	setAttr ".vh" -type "double2" 1042.328002261668 156.54159707137239 ;
	setAttr ".dag" no;
createNode hyperLayout -n "yak_camera_SHAPE_hyperLayout2";
	setAttr ".ihi" 0;
	setAttr -s 21 ".hyp";
	setAttr ".hyp[0].x" 481.42855834960937;
	setAttr ".hyp[0].y" -72.857139587402344;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 481.42855834960937;
	setAttr ".hyp[2].y" -358.57144165039062;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".hyp[10].nvs" 1920;
	setAttr ".hyp[11].nvs" 1920;
	setAttr ".hyp[12].nvs" 1920;
	setAttr ".hyp[13].nvs" 1920;
	setAttr ".hyp[14].nvs" 1920;
	setAttr ".hyp[15].nvs" 1920;
	setAttr ".hyp[16].nvs" 1920;
	setAttr ".hyp[17].nvs" 1920;
	setAttr ".hyp[18].nvs" 1920;
	setAttr ".hyp[19].nvs" 1920;
	setAttr ".hyp[20].nvs" 1920;
	setAttr ".anf" yes;
createNode hyperGraphInfo -n "yak_camera_SHAPE_nodeEditorPanel3Info";
createNode hyperView -n "yak_camera_SHAPE_hyperView3";
	setAttr ".vl" -type "double2" -113.09523809523817 -718.88415247755904 ;
	setAttr ".vh" -type "double2" 1102.948717948718 57.513142535120579 ;
	setAttr ".dag" no;
createNode hyperLayout -n "yak_camera_SHAPE_hyperLayout3";
	setAttr ".ihi" 0;
	setAttr -s 8 ".hyp";
	setAttr ".hyp[0].x" 498.57144165039062;
	setAttr ".hyp[0].y" -501.42855834960937;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 498.57144165039062;
	setAttr ".hyp[2].y" -72.857139587402344;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].x" 498.57144165039062;
	setAttr ".hyp[6].y" -215.71427917480469;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".anf" yes;
createNode hyperGraphInfo -n "yak_camera_SHAPE_nodeEditorPanel1Info1";
createNode hyperView -n "yak_camera_SHAPE_hyperView4";
	setAttr ".dag" no;
createNode hyperLayout -n "yak_camera_SHAPE_hyperLayout4";
	setAttr ".ihi" 0;
	setAttr -s 10 ".hyp";
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".anf" yes;
createNode hyperGraphInfo -n "yak_camera_SHAPE_nodeEditorPanel2Info1";
createNode hyperView -n "yak_camera_SHAPE_hyperView5";
	setAttr ".vl" -type "double2" -362.71401454505497 -659.42478948324958 ;
	setAttr ".vh" -type "double2" 1042.328002261668 156.54159707137239 ;
	setAttr ".dag" no;
createNode hyperGraphInfo -n "yak_camera_SHAPE_nodeEditorPanel3Info1";
createNode hyperView -n "yak_camera_SHAPE_hyperView6";
	setAttr ".vl" -type "double2" -113.09523809523817 -718.88415247755904 ;
	setAttr ".vh" -type "double2" 1102.948717948718 57.513142535120579 ;
	setAttr ".dag" no;
createNode multiplyDivide -n "focalCorrectionNode";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 60 0 0 ;
createNode hyperLayout -n "hyperLayout1";
	setAttr ".ihi" 0;
	setAttr -s 39 ".hyp";
	setAttr ".hyp[0].x" -183.86643981933594;
	setAttr ".hyp[0].y" 216.21400451660156;
	setAttr ".hyp[0].nvs" 1922;
	setAttr ".hyp[1].nvs" 1922;
	setAttr ".hyp[2].x" 100.05084228515625;
	setAttr ".hyp[2].y" 33.006191253662109;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].x" 104.24040985107422;
	setAttr ".hyp[3].y" -186.11492919921875;
	setAttr ".hyp[3].nvs" 1921;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".hyp[10].nvs" 1920;
	setAttr ".hyp[11].nvs" 1920;
	setAttr ".hyp[12].nvs" 1920;
	setAttr ".hyp[13].nvs" 1920;
	setAttr ".hyp[14].nvs" 1920;
	setAttr ".hyp[15].nvs" 1921;
	setAttr ".hyp[16].nvs" 1920;
	setAttr ".hyp[17].nvs" 1920;
	setAttr ".hyp[18].nvs" 1920;
	setAttr ".hyp[19].nvs" 1920;
	setAttr ".hyp[20].nvs" 1920;
	setAttr ".hyp[21].nvs" 1921;
	setAttr ".hyp[22].nvs" 1921;
	setAttr ".hyp[23].nvs" 1921;
	setAttr ".hyp[24].nvs" 1920;
	setAttr ".hyp[25].nvs" 1920;
	setAttr ".hyp[26].nvs" 1920;
	setAttr ".hyp[27].nvs" 1920;
	setAttr ".hyp[28].nvs" 1920;
	setAttr ".hyp[29].nvs" 1920;
	setAttr ".hyp[30].nvs" 1920;
	setAttr ".hyp[31].nvs" 1920;
	setAttr ".hyp[32].nvs" 1920;
	setAttr ".hyp[33].nvs" 1920;
	setAttr ".hyp[34].nvs" 1920;
	setAttr ".hyp[35].nvs" 1920;
	setAttr ".hyp[36].nvs" 1920;
	setAttr ".hyp[37].nvs" 1920;
	setAttr ".hyp[38].nvs" 1920;
	setAttr ".anf" yes;
createNode hyperLayout -n "hyperLayout2";
	setAttr ".ihi" 0;
	setAttr -s 83 ".hyp";
	setAttr ".hyp[0].x" 3205.71435546875;
	setAttr ".hyp[0].y" -2880;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].x" 978.5714111328125;
	setAttr ".hyp[1].y" -2712.857177734375;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 3497.142822265625;
	setAttr ".hyp[2].y" -2680;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].x" 1782.857177734375;
	setAttr ".hyp[3].y" -672.85711669921875;
	setAttr ".hyp[3].nvs" 1920;
	setAttr ".hyp[4].x" 2022.857177734375;
	setAttr ".hyp[4].y" -3408.571533203125;
	setAttr ".hyp[4].nvs" 1920;
	setAttr ".hyp[5].x" 1782.857177734375;
	setAttr ".hyp[5].y" -530;
	setAttr ".hyp[5].nvs" 1920;
	setAttr ".hyp[6].x" 2657.142822265625;
	setAttr ".hyp[6].y" -3222.857177734375;
	setAttr ".hyp[6].nvs" 1920;
	setAttr ".hyp[7].x" 2657.142822265625;
	setAttr ".hyp[7].y" -280;
	setAttr ".hyp[7].nvs" 1920;
	setAttr ".hyp[8].x" 721.4285888671875;
	setAttr ".hyp[8].y" -3312.857177734375;
	setAttr ".hyp[8].nvs" 1920;
	setAttr ".hyp[9].x" 2400;
	setAttr ".hyp[9].y" -1908.5714111328125;
	setAttr ".hyp[9].nvs" 1920;
	setAttr ".hyp[10].x" 3822.857177734375;
	setAttr ".hyp[10].y" -922.85711669921875;
	setAttr ".hyp[10].nvs" 1920;
	setAttr ".hyp[11].x" 3205.71435546875;
	setAttr ".hyp[11].y" -137.14285278320312;
	setAttr ".hyp[11].nvs" 1920;
	setAttr ".hyp[12].x" 3822.857177734375;
	setAttr ".hyp[12].y" -2680;
	setAttr ".hyp[12].nvs" 1920;
	setAttr ".hyp[13].x" 2657.142822265625;
	setAttr ".hyp[13].y" -1708.5714111328125;
	setAttr ".hyp[13].nvs" 1920;
	setAttr ".hyp[14].x" 3205.71435546875;
	setAttr ".hyp[14].y" -337.14285278320312;
	setAttr ".hyp[14].nvs" 1920;
	setAttr ".hyp[15].x" 978.5714111328125;
	setAttr ".hyp[15].y" -3262.857177734375;
	setAttr ".hyp[15].nvs" 1920;
	setAttr ".hyp[16].x" 721.4285888671875;
	setAttr ".hyp[16].y" -3170;
	setAttr ".hyp[16].nvs" 1920;
	setAttr ".hyp[17].x" 2657.142822265625;
	setAttr ".hyp[17].y" -2051.428466796875;
	setAttr ".hyp[17].nvs" 1920;
	setAttr ".hyp[18].x" 2914.28564453125;
	setAttr ".hyp[18].y" -237.14285278320312;
	setAttr ".hyp[18].nvs" 1920;
	setAttr ".hyp[19].x" 2657.142822265625;
	setAttr ".hyp[19].y" -2422.857177734375;
	setAttr ".hyp[19].nvs" 1920;
	setAttr ".hyp[20].x" 1782.857177734375;
	setAttr ".hyp[20].y" -2065.71435546875;
	setAttr ".hyp[20].nvs" 1920;
	setAttr ".hyp[21].x" 2914.28564453125;
	setAttr ".hyp[21].y" -1665.7142333984375;
	setAttr ".hyp[21].nvs" 1920;
	setAttr ".hyp[22].x" 2400;
	setAttr ".hyp[22].y" -765.71429443359375;
	setAttr ".hyp[22].nvs" 1920;
	setAttr ".hyp[23].x" 481.42855834960937;
	setAttr ".hyp[23].y" -3070;
	setAttr ".hyp[23].nvs" 1920;
	setAttr ".hyp[24].x" 4062.857177734375;
	setAttr ".hyp[24].y" -780;
	setAttr ".hyp[24].nvs" 1920;
	setAttr ".hyp[25].x" 3497.142822265625;
	setAttr ".hyp[25].y" -1222.857177734375;
	setAttr ".hyp[25].nvs" 1920;
	setAttr ".hyp[26].x" 2914.28564453125;
	setAttr ".hyp[26].y" -480;
	setAttr ".hyp[26].nvs" 1920;
	setAttr ".hyp[27].x" 2914.28564453125;
	setAttr ".hyp[27].y" -2522.857177734375;
	setAttr ".hyp[27].nvs" 1920;
	setAttr ".hyp[28].x" 2657.142822265625;
	setAttr ".hyp[28].y" -480;
	setAttr ".hyp[28].nvs" 1920;
	setAttr ".hyp[29].x" 3497.142822265625;
	setAttr ".hyp[29].y" -308.57144165039063;
	setAttr ".hyp[29].nvs" 1920;
	setAttr ".hyp[30].x" 2914.28564453125;
	setAttr ".hyp[30].y" -2780;
	setAttr ".hyp[30].nvs" 1920;
	setAttr ".hyp[31].x" 3205.71435546875;
	setAttr ".hyp[31].y" -3172.857177734375;
	setAttr ".hyp[31].nvs" 1920;
	setAttr ".hyp[32].x" 3205.71435546875;
	setAttr ".hyp[32].y" -3022.857177734375;
	setAttr ".hyp[32].nvs" 1920;
	setAttr ".hyp[33].x" 2657.142822265625;
	setAttr ".hyp[33].y" -3365.71435546875;
	setAttr ".hyp[33].nvs" 1920;
	setAttr ".hyp[34].x" 2914.28564453125;
	setAttr ".hyp[34].y" -3222.857177734375;
	setAttr ".hyp[34].nvs" 1920;
	setAttr ".hyp[35].x" 2400;
	setAttr ".hyp[35].y" -3308.571533203125;
	setAttr ".hyp[35].nvs" 1920;
	setAttr ".hyp[36].x" 3108.48193359375;
	setAttr ".hyp[36].y" -1213.5755615234375;
	setAttr ".hyp[36].nvs" 1922;
	setAttr ".hyp[37].x" 2400;
	setAttr ".hyp[37].y" -1565.7142333984375;
	setAttr ".hyp[37].nvs" 1920;
	setAttr ".hyp[38].x" 2914.28564453125;
	setAttr ".hyp[38].y" -1808.5714111328125;
	setAttr ".hyp[38].nvs" 1920;
	setAttr ".hyp[39].x" 3205.71435546875;
	setAttr ".hyp[39].y" -2051.428466796875;
	setAttr ".hyp[39].nvs" 1920;
	setAttr ".hyp[40].x" 2657.142822265625;
	setAttr ".hyp[40].y" -1908.5714111328125;
	setAttr ".hyp[40].nvs" 1920;
	setAttr ".hyp[41].x" 3497.142822265625;
	setAttr ".hyp[41].y" -1808.5714111328125;
	setAttr ".hyp[41].nvs" 1920;
	setAttr ".hyp[42].x" 1.4285714626312256;
	setAttr ".hyp[42].y" -3162.857177734375;
	setAttr ".hyp[42].nvs" 1920;
	setAttr ".hyp[43].x" 1.4285714626312256;
	setAttr ".hyp[43].y" -3305.71435546875;
	setAttr ".hyp[43].nvs" 1920;
	setAttr ".hyp[44].x" 2657.142822265625;
	setAttr ".hyp[44].y" -2880;
	setAttr ".hyp[44].nvs" 1920;
	setAttr ".hyp[45].x" 2400;
	setAttr ".hyp[45].y" -2422.857177734375;
	setAttr ".hyp[45].nvs" 1920;
	setAttr ".hyp[46].x" 3497.142822265625;
	setAttr ".hyp[46].y" -3172.857177734375;
	setAttr ".hyp[46].nvs" 1920;
	setAttr ".hyp[47].x" 4062.857177734375;
	setAttr ".hyp[47].y" -1065.7142333984375;
	setAttr ".hyp[47].nvs" 1920;
	setAttr ".hyp[48].x" 1782.857177734375;
	setAttr ".hyp[48].y" -2208.571533203125;
	setAttr ".hyp[48].nvs" 1920;
	setAttr ".hyp[49].x" 3497.142822265625;
	setAttr ".hyp[49].y" -1080;
	setAttr ".hyp[49].nvs" 1920;
	setAttr ".hyp[50].x" 3497.142822265625;
	setAttr ".hyp[50].y" -1365.7142333984375;
	setAttr ".hyp[50].nvs" 1920;
	setAttr ".hyp[51].x" 2400;
	setAttr ".hyp[51].y" -1708.5714111328125;
	setAttr ".hyp[51].nvs" 1920;
	setAttr ".hyp[52].x" 3822.857177734375;
	setAttr ".hyp[52].y" -1672.857177734375;
	setAttr ".hyp[52].nvs" 1920;
	setAttr ".hyp[53].x" 2400;
	setAttr ".hyp[53].y" -1080;
	setAttr ".hyp[53].nvs" 1920;
	setAttr ".hyp[54].x" 2400;
	setAttr ".hyp[54].y" -1422.857177734375;
	setAttr ".hyp[54].nvs" 1920;
	setAttr ".hyp[55].x" 3205.71435546875;
	setAttr ".hyp[55].y" -1565.7142333984375;
	setAttr ".hyp[55].nvs" 1920;
	setAttr ".hyp[56].x" 4062.857177734375;
	setAttr ".hyp[56].y" -922.85711669921875;
	setAttr ".hyp[56].nvs" 1920;
	setAttr ".hyp[57].x" 481.42855834960937;
	setAttr ".hyp[57].y" -3212.857177734375;
	setAttr ".hyp[57].nvs" 1920;
	setAttr ".hyp[58].x" 241.42857360839844;
	setAttr ".hyp[58].y" -3262.857177734375;
	setAttr ".hyp[58].nvs" 1920;
	setAttr ".hyp[59].x" 2400;
	setAttr ".hyp[59].y" -480;
	setAttr ".hyp[59].nvs" 1920;
	setAttr ".hyp[60].x" 2022.857177734375;
	setAttr ".hyp[60].y" -3265.71435546875;
	setAttr ".hyp[60].nvs" 1920;
	setAttr ".hyp[61].x" 2022.857177734375;
	setAttr ".hyp[61].y" -2972.857177734375;
	setAttr ".hyp[61].nvs" 1920;
	setAttr ".hyp[62].x" 978.5714111328125;
	setAttr ".hyp[62].y" -2855.71435546875;
	setAttr ".hyp[62].nvs" 1920;
	setAttr ".hyp[63].x" 1270;
	setAttr ".hyp[63].y" -2984.28564453125;
	setAttr ".hyp[63].nvs" 1920;
	setAttr ".hyp[64].x" 721.4285888671875;
	setAttr ".hyp[64].y" -3455.71435546875;
	setAttr ".hyp[64].nvs" 1920;
	setAttr ".hyp[65].x" 1963.493408203125;
	setAttr ".hyp[65].y" -1034.9326171875;
	setAttr ".hyp[65].nvs" 1922;
	setAttr ".hyp[66].x" 4062.857177734375;
	setAttr ".hyp[66].y" -1672.857177734375;
	setAttr ".hyp[66].nvs" 1920;
	setAttr ".hyp[67].x" 2914.28564453125;
	setAttr ".hyp[67].y" -2051.428466796875;
	setAttr ".hyp[67].nvs" 1920;
	setAttr ".hyp[68].x" 2400;
	setAttr ".hyp[68].y" -622.85711669921875;
	setAttr ".hyp[68].nvs" 1920;
	setAttr ".hyp[69].x" 2022.857177734375;
	setAttr ".hyp[69].y" -572.85711669921875;
	setAttr ".hyp[69].nvs" 1920;
	setAttr ".hyp[70].x" 3205.71435546875;
	setAttr ".hyp[70].y" -480;
	setAttr ".hyp[70].nvs" 1920;
	setAttr ".hyp[71].x" 2657.142822265625;
	setAttr ".hyp[71].y" -765.71429443359375;
	setAttr ".hyp[71].nvs" 1920;
	setAttr ".hyp[72].x" 2022.857177734375;
	setAttr ".hyp[72].y" -3115.71435546875;
	setAttr ".hyp[72].nvs" 1920;
	setAttr ".hyp[73].x" 2657.142822265625;
	setAttr ".hyp[73].y" -3022.857177734375;
	setAttr ".hyp[73].nvs" 1920;
	setAttr ".hyp[74].x" 2657.142822265625;
	setAttr ".hyp[74].y" -1565.7142333984375;
	setAttr ".hyp[74].nvs" 1920;
	setAttr ".hyp[75].x" 2914.28564453125;
	setAttr ".hyp[75].y" -3022.857177734375;
	setAttr ".hyp[75].nvs" 1920;
	setAttr ".hyp[76].x" 2400;
	setAttr ".hyp[76].y" -3072.857177734375;
	setAttr ".hyp[76].nvs" 1920;
	setAttr ".hyp[77].x" 2657.142822265625;
	setAttr ".hyp[77].y" -2622.857177734375;
	setAttr ".hyp[77].nvs" 1920;
	setAttr ".hyp[78].x" 2400;
	setAttr ".hyp[78].y" -1222.857177734375;
	setAttr ".hyp[78].nvs" 1920;
	setAttr ".hyp[79].x" 2400;
	setAttr ".hyp[79].y" -2158.571533203125;
	setAttr ".hyp[79].nvs" 1920;
	setAttr ".hyp[80].x" 2022.857177734375;
	setAttr ".hyp[80].y" -2108.571533203125;
	setAttr ".hyp[80].nvs" 1920;
	setAttr ".hyp[81].x" 3205.71435546875;
	setAttr ".hyp[81].y" -1808.5714111328125;
	setAttr ".hyp[81].nvs" 1920;
	setAttr ".hyp[82].x" 2756.898193359375;
	setAttr ".hyp[82].y" -1244.05859375;
	setAttr ".hyp[82].nvs" 1922;
	setAttr ".anf" yes;
createNode unitConversion -n "unitConversion1";
	setAttr ".cf" 0.017453292519943295;
createNode multiplyDivide -n "panX_multiplyDivide";
	setAttr ".op" 2;
createNode multiplyDivide -n "panY_multiplyDivide";
	setAttr ".op" 2;
createNode cluster -n "cameraHD_2d_clusterCluster";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak1";
createNode objectSet -n "cluster1Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster1GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster1GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode cluster -n "aim_clusterCluster";
	setAttr -s 5 ".ip";
	setAttr -s 5 ".og";
	setAttr ".rel" yes;
	setAttr -s 5 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak2";
createNode tweak -n "tweak3";
createNode tweak -n "tweak4";
createNode tweak -n "tweak5";
createNode tweak -n "tweak6";
createNode objectSet -n "cluster2Set";
	setAttr ".ihi" 0;
	setAttr -s 5 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 5 ".gn";
createNode groupId -n "cluster2GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "cluster2GroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "cluster2GroupId2";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "cluster2GroupId3";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "cluster2GroupId4";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster2GroupParts4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet2";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId8";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts8";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet3";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId9";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts9";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet4";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId10";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts10";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet5";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId11";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts11";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet6";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId12";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts12";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "global_clusterCluster";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak7";
createNode objectSet -n "cluster3Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster3GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster3GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet7";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId14";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts14";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "holder_clusterCluster";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".og";
	setAttr ".rel" yes;
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak8";
createNode tweak -n "tweak9";
createNode objectSet -n "cluster4Set";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 2 ".gn";
createNode groupId -n "cluster4GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster4GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "cluster4GroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster4GroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet8";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId17";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts17";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet9";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId18";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts18";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode hyperLayout -n "hyperLayout3";
	setAttr ".ihi" 0;
	setAttr -s 3 ".hyp";
	setAttr ".hyp[0].x" 1.4285714626312256;
	setAttr ".hyp[0].y" -177.14285278320312;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].x" 1.4285714626312256;
	setAttr ".hyp[1].y" -72.857139587402344;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 212.85714721679687;
	setAttr ".hyp[2].y" -177.14285278320312;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".anf" yes;
createNode cluster -n "cluster5";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster5Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode cluster -n "cluster6";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster6Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster6GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster6GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode groupParts -n "groupParts20";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "groupId20";
	setAttr ".ihi" 0;
createNode tweak -n "tweak10";
createNode groupParts -n "cluster5GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0]";
createNode groupId -n "cluster5GroupId";
	setAttr ".ihi" 0;
createNode objectSet -n "tweakSet10";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode cluster -n "cluster7";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak11";
createNode objectSet -n "cluster7Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster7GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster7GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode objectSet -n "tweakSet11";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId22";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts22";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "cluster8";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster8Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster8GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster8GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0]";
createNode cluster -n "cluster9";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".og";
	setAttr ".rel" yes;
	setAttr -s 2 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak12";
createNode tweak -n "tweak13";
createNode objectSet -n "cluster9Set";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 2 ".gn";
createNode groupId -n "cluster9GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster9GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "cluster9GroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster9GroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet12";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId25";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts25";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet13";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId26";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts26";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode unitConversion -n "unitConversion2";
	setAttr ".cf" 0.017453292519943295;
createNode multDoubleLinear -n "zoomFactor2d";
createNode cluster -n "cluster10";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak14";
createNode objectSet -n "cluster10Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster10GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster10GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode objectSet -n "tweakSet14";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId28";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts28";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode cluster -n "cluster11";
	setAttr ".rel" yes;
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster11Set";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster11GroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster11GroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0]";
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
lockNode -l 1 ;
createNode objectSet -n "RenderSet";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".an" -type "string" "gCharacterSet";
createNode script -n "scriptJobBuilderNode";
	setAttr ".b" -type "string" (
		"import maya.cmds as mc\ndef selectionListener(*args):\n    sel = mc.ls(sl=True)\n    if len(sel) == 1:\n        if sel[0].find(\"plusPlate\") != -1:\n            # \"PLUS\" icon selected: perform duplicate            \n            controller = mc.listRelatives(sel[0], parent=True)[0]\n            offset     = mc.listRelatives(controller, parent=True)[0]\n            plate      = mc.listConnections(controller + \".lockPlate\")[0]\n            locator    = mc.listRelatives(plate, parent=True)[0]\n            \n            #-----------------------------------------------\n            # WARNING: there's a heavy DAG ambiguity here; use the \"|\" to resolve\n\n            # Duplicate locator and plane\n            (locator_COPY, plate_COPY, constraint_COPY) = mc.duplicate(locator, name=locator + \"_COPY\")\n            mc.delete(locator_COPY + \"|\" + constraint_COPY) #WARNING: duplicating produces DAG ambiguities!!! use the \"|\" to resolve\n            tempTuple = mc.duplicate(offset, name=offset + \"_COPY\") \n            offset_COPY = tempTuple[0]\n"
		+ "            controller_COPY = offset_COPY + \"|\" + tempTuple[1] # DAG ambiguity here \n\n            # Hide the plus, show the minus\n            mc.setAttr(controller_COPY + \"|plusPlate.visibility\", 0)\n            mc.setAttr(controller_COPY + \"|minusPlate.visibility\", 1)\n\n            # Create cluster for rescaling Interface\n            #mc.select(newController + \"Shape\", newController + \"Shape1\", \n            #          newController + \"|plusPlate|plusPlateShape\", \n            #          newController + \"|minusPlate|minusPlateShape\", r=True)\n            #clusterTransform = mc.cluster(name = newController + \"Clustering\", relative=True)[1]\n            #mc.setAttr(clusterTransform + \".visibility\", 0)\n            \n            #camera_global = getOrInvalidate(\"camera_global\")\n            #mc.connectAttr(camera_global + \".controllersSize\", clusterTransform + \".sx\")\n            #mc.connectAttr(camera_global + \".controllersSize\", clusterTransform + \".sy\")\n            #mc.parent(clusterTransform, newController + \"_offset\", relative=True)\n"
		+ "            #-------------------------------------------------------------------------------------------------------\n            # IN WHAT FOLLOWS, DON'T ATTEMPT TO RENAME EVERYTHING COHERENTLY!!!\n            # It'd be a HUUUGE mess and in the end totally useless\n            \n            # MAKE PLATES DYNAMIC\n            # Add the Zs of controller and offset to get the Z relative to \"platesHolder\"\n            zCoordNode = mc.createNode (\"addDoubleLinear\")\n            mc.connectAttr(controller_COPY + \".tz\", zCoordNode + \".input1\")\n            mc.connectAttr(offset_COPY + \".tz\", zCoordNode + \".input2\")\n            # Compute orthogonal distance \n            zDistanceNode = mc.createNode (\"plusMinusAverage\")\n            mc.setAttr    (zDistanceNode + \".operation\", 2) #Subtract\n            mc.connectAttr(\"cameraMarker.tz\", zDistanceNode + \".input1D[0]\")\n            mc.connectAttr(zCoordNode + \".output\", zDistanceNode + \".input1D[1]\")\n            # Create a factorNode to have a first approximation of size\n            factorNode = mc.createNode (\"multDoubleLinear\")\n"
		+ "            mc.connectAttr(zDistanceNode + \".output1D\", factorNode + \".i1\") #Branch HERE the FOCAL LENGHT\n            mc.setAttr    (factorNode + \".i2\", .001) # <-- plug the factor HERE!!!\n            mc.connectAttr(factorNode + \".output\", offset_COPY + \".sx\")\n            mc.connectAttr(factorNode + \".output\", offset_COPY + \".sy\")\n\n            # The real plate is still unlinked to solve the rotation bug; do constraint now\n            mc.parentConstraint(controller_COPY, locator_COPY, mo=False)               \n            DAGChildren = mc.listRelatives(locator_COPY, children=True, type=\"transform\")\n            if DAGChildren != None:\n                    # Connect visibility and lock to the controller\n                    mc.setAttr(locator_COPY + \"|\" + DAGChildren[0] + \".overrideDisplayType\", 2) #Reference\n                    mc.connectAttr(controller_COPY + \".lockPlate\", locator_COPY + \"|\" + DAGChildren[0] + \".overrideEnabled\")\n                    mc.connectAttr(controller_COPY + \".showPlate\", locator_COPY + \"|\" + DAGChildren[0] + \".visibility\")\n"
		+ "                    mc.connectAttr(controller_COPY + \".rotX\", locator_COPY + \"|\" + DAGChildren[0] + \".rx\")\n                    mc.connectAttr(controller_COPY + \".rotY\", locator_COPY + \"|\" + DAGChildren[0] + \".ry\")\n                    mc.connectAttr(controller_COPY + \".rotZ\", locator_COPY + \"|\" + DAGChildren[0] + \".rz\")\n            \n            # Multiply togheter the dynamic plate scale with the controller scale\n            trueScaleX = mc.createNode (\"multDoubleLinear\")\n            trueScaleY = mc.createNode (\"multDoubleLinear\")\n            trueScaleZ = mc.createNode (\"multDoubleLinear\")\n\n            mc.connectAttr(controller_COPY + \".sx\", trueScaleX + \".input1\")\n            mc.connectAttr(controller_COPY + \".sy\", trueScaleY + \".input1\")\n            mc.connectAttr(controller_COPY + \".sz\", trueScaleZ + \".input1\")\n\n            mc.connectAttr(factorNode + \".output\", trueScaleX + \".input2\")\n            mc.connectAttr(factorNode + \".output\", trueScaleY + \".input2\")\n            mc.connectAttr(factorNode + \".output\", trueScaleZ + \".input2\")\n"
		+ "            # Don't forget the focal correction of PROJ\n            focalTrueScaleX = mc.createNode (\"multDoubleLinear\")\n            focalTrueScaleY = mc.createNode (\"multDoubleLinear\")\n            focalTrueScaleZ = mc.createNode (\"multDoubleLinear\")\n\n            mc.connectAttr(trueScaleX + \".output\", focalTrueScaleX + \".input1\")\n            mc.connectAttr(trueScaleY + \".output\", focalTrueScaleY + \".input1\")\n            mc.connectAttr(trueScaleZ + \".output\", focalTrueScaleZ + \".input1\")\n\n            mc.connectAttr(\"platesHolder.sx\", focalTrueScaleX + \".input2\") # \n            mc.connectAttr(\"platesHolder.sx\", focalTrueScaleY + \".input2\")\n            mc.connectAttr(\"platesHolder.sx\", focalTrueScaleZ + \".input2\")\n            \n            # finally link all together...\n            mc.connectAttr(focalTrueScaleX + \".output\", locator_COPY + \".sx\")\n            mc.connectAttr(focalTrueScaleY + \".output\", locator_COPY + \".sy\")\n            mc.connectAttr(focalTrueScaleZ + \".output\", locator_COPY + \".sz\")                    \n"
		+ "            \n            #------------------------------------------------------------------------------------\n            # Everything went well; select and finish\n            mc.select(controller_COPY, r=True)\n            mc.headsUpMessage(\"plate <<\" + plate + \">> DUPLICATED!\", time=2.0, selection=False, vo=0)\n           \n        elif sel[0].find(\"minusPlate\") != -1:\n            # \"MINUS\" icon selected: perform delete\n            # pickWalk(UP) does a FANTASTIC job in intercepting the proper parent DAGName!!!\n            controller = mc.pickWalk(sel[0], direction=\"up\")[0]\n            offset     = mc.pickWalk(controller, direction=\"up\")[0]\n            plate      = mc.listConnections(controller + \".lockPlate\")[0]\n            locator    = mc.listRelatives(plate, parent=True)[0]       \n            mc.delete(offset)\n            mc.delete(locator)\n            mc.headsUpMessage(\"plate <<\" + plate + \">> DELETED!\", time=2.0, selection=False, vo=0)\n# Hidden window scriptJob trick:\nif mc.window(\"selectionListener_WINHOLDER\", ex=1):\n"
		+ "    # Close the window, erase the scriptJob\n    mc.deleteUI(\"selectionListener_WINHOLDER\") \nmc.window(\"selectionListener_WINHOLDER\")\nmc.scriptJob(event=[\"SelectionChanged\", selectionListener], parent=\"selectionListener_WINHOLDER\")\n# At this point, no matter what, there'll be exactly ONE \"selectionListener\" job active!!!\n# Activated every time the \"camera.ma\" is referenced/imported/open.   \nmc.headsUpMessage(\"<< SELECTION LISTENER >> activated\", time=4.0, selection=False, vo=0)\n\n");
	setAttr ".st" 2;
	setAttr ".stp" 1;
createNode addDoubleLinear -n "addDoubleLinear1";
createNode multiplyDivide -n "multiplyDivide1";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
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
	setAttr -s 6 ".u";
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
connectAttr "global_clusterCluster.og[0]" "camera_globalShape.cr";
connectAttr "tweak7.pl[0].cp[0]" "camera_globalShape.twl";
connectAttr "cluster3GroupId.id" "camera_globalShape.iog.og[0].gid";
connectAttr "cluster3Set.mwc" "camera_globalShape.iog.og[0].gco";
connectAttr "groupId14.id" "camera_globalShape.iog.og[1].gid";
connectAttr "tweakSet7.mwc" "camera_globalShape.iog.og[1].gco";
connectAttr "cameras_holder_aimConstraint1.crx" "cameras_holder.rx" -l on;
connectAttr "cameras_holder_aimConstraint1.cry" "cameras_holder.ry" -l on;
connectAttr "cameras_holder_aimConstraint1.crz" "cameras_holder.rz" -l on;
connectAttr "focalCorrectionNode.ox" "cameras_holder.focalCorrection";
connectAttr "holder_clusterCluster.og[0]" "cameras_holderShape.cr";
connectAttr "tweak8.pl[0].cp[0]" "cameras_holderShape.twl";
connectAttr "cluster4GroupId.id" "cameras_holderShape.iog.og[0].gid";
connectAttr "cluster4Set.mwc" "cameras_holderShape.iog.og[0].gco";
connectAttr "groupId17.id" "cameras_holderShape.iog.og[1].gid";
connectAttr "tweakSet8.mwc" "cameras_holderShape.iog.og[1].gco";
connectAttr "cameras_holder.far" "cameraPROJShape.fcp";
connectAttr "cameras_holder.near" "cameraPROJShape.ncp";
connectAttr "cameras_holder.PROJ_focal" "cameraPROJShape.fl";
connectAttr "cameras_holder.PROJ_overscan" "cameraPROJShape.ovr";
connectAttr "cameras_holder.PROJ_gate" "cameraPROJShape.dgm";
connectAttr "cameras_holder.PROJ_gate" "cameraPROJShape.dfg";
connectAttr "cameraHD_2d_clusterCluster.og[0]" "XXXShape.i";
connectAttr "tweak1.vl[0].vt[0]" "XXXShape.twl";
connectAttr "cluster1GroupId.id" "XXXShape.iog.og[2].gid";
connectAttr "cluster1Set.mwc" "XXXShape.iog.og[2].gco";
connectAttr "groupId2.id" "XXXShape.iog.og[3].gid";
connectAttr "tweakSet1.mwc" "XXXShape.iog.og[3].gco";
connectAttr "cameras_holder.far" "cameraHDShape.fcp";
connectAttr "cameras_holder.near" "cameraHDShape.ncp";
connectAttr "cameras_holder.HD_focal" "cameraHDShape.fl";
connectAttr "cameras_holder.HD_overscan" "cameraHDShape.ovr";
connectAttr "cameras_holder.HD_gate" "cameraHDShape.dfg";
connectAttr "cameras_holder.HD_gate" "cameraHDShape.dgm";
connectAttr "panX_multiplyDivide.ox" "cameraHDShape.hfo";
connectAttr "panY_multiplyDivide.ox" "cameraHDShape.vfo";
connectAttr "cameraHD_controller.zoom" "cameraHDShape.psc";
connectAttr "unitConversion1.o" "cameraHDShape.frv";
connectAttr "multiplyDivide1.ox" "cameraHDShape.cs";
connectAttr "camera_global.show_guide" "cameraHDLineShape.v";
connectAttr "cluster8.og[0]" "cameraHDLineShape.cr";
connectAttr "tweak11.pl[0].cp[0]" "cameraHDLineShape.twl";
connectAttr "cluster7GroupId.id" "cameraHDLineShape.iog.og[0].gid";
connectAttr "cluster7Set.mwc" "cameraHDLineShape.iog.og[0].gco";
connectAttr "groupId22.id" "cameraHDLineShape.iog.og[1].gid";
connectAttr "tweakSet11.mwc" "cameraHDLineShape.iog.og[1].gco";
connectAttr "cluster8GroupId.id" "cameraHDLineShape.iog.og[2].gid";
connectAttr "cluster8Set.mwc" "cameraHDLineShape.iog.og[2].gco";
connectAttr "cluster9GroupId.id" "cameraHD_2dShape.iog.og[0].gid";
connectAttr "cluster9Set.mwc" "cameraHD_2dShape.iog.og[0].gco";
connectAttr "groupId25.id" "cameraHD_2dShape.iog.og[1].gid";
connectAttr "tweakSet12.mwc" "cameraHD_2dShape.iog.og[1].gco";
connectAttr "cluster9.og[0]" "cameraHD_2dShape.cr";
connectAttr "tweak12.pl[0].cp[0]" "cameraHD_2dShape.twl";
connectAttr "cluster9GroupId1.id" "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.iog.og[0].gid"
		;
connectAttr "cluster9Set.mwc" "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.iog.og[0].gco"
		;
connectAttr "groupId26.id" "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.iog.og[1].gid"
		;
connectAttr "tweakSet13.mwc" "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.iog.og[1].gco"
		;
connectAttr "cluster9.og[1]" "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.cr"
		;
connectAttr "tweak13.pl[0].cp[0]" "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.twl"
		;
connectAttr "camera_global.show_guide" "fake2dLineShape.v";
connectAttr "cluster11.og[0]" "fake2dLineShape.cr";
connectAttr "tweak14.pl[0].cp[0]" "fake2dLineShape.twl";
connectAttr "cluster10GroupId.id" "fake2dLineShape.iog.og[0].gid";
connectAttr "cluster10Set.mwc" "fake2dLineShape.iog.og[0].gco";
connectAttr "groupId28.id" "fake2dLineShape.iog.og[1].gid";
connectAttr "tweakSet14.mwc" "fake2dLineShape.iog.og[1].gco";
connectAttr "cluster11GroupId.id" "fake2dLineShape.iog.og[2].gid";
connectAttr "cluster11Set.mwc" "fake2dLineShape.iog.og[2].gco";
connectAttr "camera_global.controllersSize" "cameraHD_2d_cluster.sx";
connectAttr "camera_global.controllersSize" "cameraHD_2d_cluster.sy";
connectAttr "camera_global.controllersSize" "cameraHD_2d_cluster.sz";
connectAttr "cluster7Handle_pointConstraint1.ctx" "cluster7Handle.tx";
connectAttr "cluster7Handle_pointConstraint1.cty" "cluster7Handle.ty";
connectAttr "cluster7Handle_pointConstraint1.ctz" "cluster7Handle.tz";
connectAttr "cluster7Handle.pim" "cluster7Handle_pointConstraint1.cpim";
connectAttr "cluster7Handle.rp" "cluster7Handle_pointConstraint1.crp";
connectAttr "cluster7Handle.rpt" "cluster7Handle_pointConstraint1.crt";
connectAttr "cameraHD_controller.t" "cluster7Handle_pointConstraint1.tg[0].tt";
connectAttr "cameraHD_controller.rp" "cluster7Handle_pointConstraint1.tg[0].trp"
		;
connectAttr "cameraHD_controller.rpt" "cluster7Handle_pointConstraint1.tg[0].trt"
		;
connectAttr "cameraHD_controller.pm" "cluster7Handle_pointConstraint1.tg[0].tpm"
		;
connectAttr "cluster7Handle_pointConstraint1.w0" "cluster7Handle_pointConstraint1.tg[0].tw"
		;
connectAttr "cluster8Handle_pointConstraint1.ctx" "cluster8Handle.tx";
connectAttr "cluster8Handle_pointConstraint1.cty" "cluster8Handle.ty";
connectAttr "cluster8Handle_pointConstraint1.ctz" "cluster8Handle.tz";
connectAttr "cluster8Handle.pim" "cluster8Handle_pointConstraint1.cpim";
connectAttr "cluster8Handle.rp" "cluster8Handle_pointConstraint1.crp";
connectAttr "cluster8Handle.rpt" "cluster8Handle_pointConstraint1.crt";
connectAttr "cameras_holder.t" "cluster8Handle_pointConstraint1.tg[0].tt";
connectAttr "cameras_holder.rp" "cluster8Handle_pointConstraint1.tg[0].trp";
connectAttr "cameras_holder.rpt" "cluster8Handle_pointConstraint1.tg[0].trt";
connectAttr "cameras_holder.pm" "cluster8Handle_pointConstraint1.tg[0].tpm";
connectAttr "cluster8Handle_pointConstraint1.w0" "cluster8Handle_pointConstraint1.tg[0].tw"
		;
connectAttr "cameraHD_controller.panY" "cluster9Handle.ty";
connectAttr "cameraHD_controller.panX" "cluster9Handle.tx";
connectAttr "unitConversion2.o" "cluster9Handle.rz";
connectAttr "zoomFactor2d.o" "cluster9Handle.sx";
connectAttr "zoomFactor2d.o" "cluster9Handle.sy";
connectAttr "zoomFactor2d.o" "cluster9Handle.sz";
connectAttr "cluster10Handle_pointConstraint1.ctx" "cluster10Handle.tx";
connectAttr "cluster10Handle_pointConstraint1.cty" "cluster10Handle.ty";
connectAttr "cluster10Handle_pointConstraint1.ctz" "cluster10Handle.tz";
connectAttr "cluster10Handle.pim" "cluster10Handle_pointConstraint1.cpim";
connectAttr "cluster10Handle.rp" "cluster10Handle_pointConstraint1.crp";
connectAttr "cluster10Handle.rpt" "cluster10Handle_pointConstraint1.crt";
connectAttr "cameraHD_controller.t" "cluster10Handle_pointConstraint1.tg[0].tt";
connectAttr "cameraHD_controller.rp" "cluster10Handle_pointConstraint1.tg[0].trp"
		;
connectAttr "cameraHD_controller.rpt" "cluster10Handle_pointConstraint1.tg[0].trt"
		;
connectAttr "cameraHD_controller.pm" "cluster10Handle_pointConstraint1.tg[0].tpm"
		;
connectAttr "cluster10Handle_pointConstraint1.w0" "cluster10Handle_pointConstraint1.tg[0].tw"
		;
connectAttr "cluster11Handle_pointConstraint1.ctx" "cluster11Handle.tx";
connectAttr "cluster11Handle_pointConstraint1.cty" "cluster11Handle.ty";
connectAttr "cluster11Handle_pointConstraint1.ctz" "cluster11Handle.tz";
connectAttr "cluster11Handle.pim" "cluster11Handle_pointConstraint1.cpim";
connectAttr "cluster11Handle.rp" "cluster11Handle_pointConstraint1.crp";
connectAttr "cluster11Handle.rpt" "cluster11Handle_pointConstraint1.crt";
connectAttr "fake2dLocator.t" "cluster11Handle_pointConstraint1.tg[0].tt";
connectAttr "fake2dLocator.rp" "cluster11Handle_pointConstraint1.tg[0].trp";
connectAttr "fake2dLocator.rpt" "cluster11Handle_pointConstraint1.tg[0].trt";
connectAttr "fake2dLocator.pm" "cluster11Handle_pointConstraint1.tg[0].tpm";
connectAttr "cluster11Handle_pointConstraint1.w0" "cluster11Handle_pointConstraint1.tg[0].tw"
		;
connectAttr "cameraHD_controller.panX" "fake2dLocator.tx" -l on;
connectAttr "cameraHD_controller.panY" "fake2dLocator.ty" -l on;
connectAttr "holder_clusterCluster.og[1]" "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.cr"
		;
connectAttr "tweak9.pl[0].cp[0]" "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.twl"
		;
connectAttr "cluster4GroupId1.id" "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.iog.og[0].gid"
		;
connectAttr "cluster4Set.mwc" "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.iog.og[0].gco"
		;
connectAttr "groupId18.id" "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.iog.og[1].gid"
		;
connectAttr "tweakSet9.mwc" "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.iog.og[1].gco"
		;
connectAttr "cameras_holder.pim" "cameras_holder_aimConstraint1.cpim";
connectAttr "cameras_holder.t" "cameras_holder_aimConstraint1.ct";
connectAttr "cameras_holder.rp" "cameras_holder_aimConstraint1.crp";
connectAttr "cameras_holder.rpt" "cameras_holder_aimConstraint1.crt";
connectAttr "cameras_holder.ro" "cameras_holder_aimConstraint1.cro";
connectAttr "camera_aim.t" "cameras_holder_aimConstraint1.tg[0].tt";
connectAttr "camera_aim.rp" "cameras_holder_aimConstraint1.tg[0].trp";
connectAttr "camera_aim.rpt" "cameras_holder_aimConstraint1.tg[0].trt";
connectAttr "camera_aim.pm" "cameras_holder_aimConstraint1.tg[0].tpm";
connectAttr "cameras_holder_aimConstraint1.w0" "cameras_holder_aimConstraint1.tg[0].tw"
		;
connectAttr "upLocator.wm" "cameras_holder_aimConstraint1.wum";
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|cameras_holder|cameras_holder_rig|holder_cluster|holder_cluster.sx"
		;
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|cameras_holder|cameras_holder_rig|holder_cluster|holder_cluster.sy"
		;
connectAttr "camera_aim_orientConstraint1.crx" "camera_aim.rx" -l on;
connectAttr "camera_aim_orientConstraint1.cry" "camera_aim.ry" -l on;
connectAttr "camera_aim_orientConstraint1.crz" "camera_aim.rz" -l on;
connectAttr "aim_clusterCluster.og[0]" "camera_aimShape.cr";
connectAttr "tweak2.pl[0].cp[0]" "camera_aimShape.twl";
connectAttr "cluster2GroupId.id" "camera_aimShape.iog.og[0].gid";
connectAttr "cluster2Set.mwc" "camera_aimShape.iog.og[0].gco";
connectAttr "groupId8.id" "camera_aimShape.iog.og[1].gid";
connectAttr "tweakSet2.mwc" "camera_aimShape.iog.og[1].gco";
connectAttr "aim_clusterCluster.og[1]" "curveShape3.cr";
connectAttr "tweak3.pl[0].cp[0]" "curveShape3.twl";
connectAttr "cluster2GroupId1.id" "curveShape3.iog.og[0].gid";
connectAttr "cluster2Set.mwc" "curveShape3.iog.og[0].gco";
connectAttr "groupId9.id" "curveShape3.iog.og[1].gid";
connectAttr "tweakSet3.mwc" "curveShape3.iog.og[1].gco";
connectAttr "aim_clusterCluster.og[2]" "curveShape2.cr";
connectAttr "tweak4.pl[0].cp[0]" "curveShape2.twl";
connectAttr "cluster2GroupId2.id" "curveShape2.iog.og[0].gid";
connectAttr "cluster2Set.mwc" "curveShape2.iog.og[0].gco";
connectAttr "groupId10.id" "curveShape2.iog.og[1].gid";
connectAttr "tweakSet4.mwc" "curveShape2.iog.og[1].gco";
connectAttr "aim_clusterCluster.og[3]" "nurbsCircleShape3.cr";
connectAttr "tweak5.pl[0].cp[0]" "nurbsCircleShape3.twl";
connectAttr "cluster2GroupId3.id" "nurbsCircleShape3.iog.og[0].gid";
connectAttr "cluster2Set.mwc" "nurbsCircleShape3.iog.og[0].gco";
connectAttr "groupId11.id" "nurbsCircleShape3.iog.og[1].gid";
connectAttr "tweakSet5.mwc" "nurbsCircleShape3.iog.og[1].gco";
connectAttr "aim_clusterCluster.og[4]" "nurbsCircleShape2.cr";
connectAttr "tweak6.pl[0].cp[0]" "nurbsCircleShape2.twl";
connectAttr "cluster2GroupId4.id" "nurbsCircleShape2.iog.og[0].gid";
connectAttr "cluster2Set.mwc" "nurbsCircleShape2.iog.og[0].gco";
connectAttr "groupId12.id" "nurbsCircleShape2.iog.og[1].gid";
connectAttr "tweakSet6.mwc" "nurbsCircleShape2.iog.og[1].gco";
connectAttr "camera_global.show_guide" "aimLineShape.v";
connectAttr "cluster5GroupId.id" "aimLineShape.iog.og[0].gid";
connectAttr "cluster5Set.mwc" "aimLineShape.iog.og[0].gco";
connectAttr "tweakSet10.mwc" "aimLineShape.iog.og[1].gco";
connectAttr "groupId20.id" "aimLineShape.iog.og[1].gid";
connectAttr "cluster6GroupId.id" "aimLineShape.iog.og[2].gid";
connectAttr "cluster6Set.mwc" "aimLineShape.iog.og[2].gco";
connectAttr "cluster6.og[0]" "aimLineShape.cr";
connectAttr "tweak10.pl[0].cp[0]" "aimLineShape.twl";
connectAttr "camera_aim.ro" "camera_aim_orientConstraint1.cro";
connectAttr "camera_aim.pim" "camera_aim_orientConstraint1.cpim";
connectAttr "cameras_holder.r" "camera_aim_orientConstraint1.tg[0].tr";
connectAttr "cameras_holder.ro" "camera_aim_orientConstraint1.tg[0].tro";
connectAttr "cameras_holder.pm" "camera_aim_orientConstraint1.tg[0].tpm";
connectAttr "camera_aim_orientConstraint1.w0" "camera_aim_orientConstraint1.tg[0].tw"
		;
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|camera_aim|camera_aim_rig|aim_cluster|aim_cluster.sx"
		;
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|camera_aim|camera_aim_rig|aim_cluster|aim_cluster.sy"
		;
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|camera_aim|camera_aim_rig|aim_cluster|aim_cluster.sz"
		;
connectAttr "cluster5Handle_pointConstraint1.ctx" "cluster5Handle.tx";
connectAttr "cluster5Handle_pointConstraint1.cty" "cluster5Handle.ty";
connectAttr "cluster5Handle_pointConstraint1.ctz" "cluster5Handle.tz";
connectAttr "cluster5Handle.pim" "cluster5Handle_pointConstraint1.cpim";
connectAttr "cluster5Handle.rp" "cluster5Handle_pointConstraint1.crp";
connectAttr "cluster5Handle.rpt" "cluster5Handle_pointConstraint1.crt";
connectAttr "cameras_holder.t" "cluster5Handle_pointConstraint1.tg[0].tt";
connectAttr "cameras_holder.rp" "cluster5Handle_pointConstraint1.tg[0].trp";
connectAttr "cameras_holder.rpt" "cluster5Handle_pointConstraint1.tg[0].trt";
connectAttr "cameras_holder.pm" "cluster5Handle_pointConstraint1.tg[0].tpm";
connectAttr "cluster5Handle_pointConstraint1.w0" "cluster5Handle_pointConstraint1.tg[0].tw"
		;
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|camera_global_rig|global_cluster|global_cluster.sx"
		;
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|camera_global_rig|global_cluster|global_cluster.sy"
		;
connectAttr "camera_global.controllersSize" "|camera_rig|camera_global|camera_global_rig|global_cluster|global_cluster.sz"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "hyperView1.msg" "nodeEditorPanel2Info.b[0]";
connectAttr "hyperLayout2.msg" "hyperView1.hl";
connectAttr "hyperView2.msg" "nodeEditorPanel1Info.b[0]";
connectAttr "hyperLayout1.msg" "hyperView2.hl";
connectAttr "hyperView3.msg" "nodeEditorPanel3Info.b[0]";
connectAttr "hyperLayout3.msg" "hyperView3.hl";
connectAttr "yak_camera_SHAPE_hyperView1.msg" "yak_camera_SHAPE_nodeEditorPanel1Info.b[0]"
		;
connectAttr "yak_camera_SHAPE_hyperLayout1.msg" "yak_camera_SHAPE_hyperView1.hl"
		;
connectAttr "yak_camera_SHAPE_hyperView2.msg" "yak_camera_SHAPE_nodeEditorPanel2Info.b[0]"
		;
connectAttr "yak_camera_SHAPE_hyperLayout2.msg" "yak_camera_SHAPE_hyperView2.hl"
		;
connectAttr ":lightLinker1.msg" "yak_camera_SHAPE_hyperLayout2.hyp[0].dn";
connectAttr ":renderPartition.msg" "yak_camera_SHAPE_hyperLayout2.hyp[2].dn";
connectAttr "yak_camera_SHAPE_hyperView3.msg" "yak_camera_SHAPE_nodeEditorPanel3Info.b[0]"
		;
connectAttr "yak_camera_SHAPE_hyperLayout3.msg" "yak_camera_SHAPE_hyperView3.hl"
		;
connectAttr ":lightLinker1.msg" "yak_camera_SHAPE_hyperLayout3.hyp[0].dn";
connectAttr ":renderPartition.msg" "yak_camera_SHAPE_hyperLayout3.hyp[2].dn";
connectAttr "yak_camera_SHAPE_hyperLayout2.msg" "yak_camera_SHAPE_hyperLayout3.hyp[6].dn"
		;
connectAttr "yak_camera_SHAPE_hyperView4.msg" "yak_camera_SHAPE_nodeEditorPanel1Info1.b[0]"
		;
connectAttr "yak_camera_SHAPE_hyperLayout4.msg" "yak_camera_SHAPE_hyperView4.hl"
		;
connectAttr "yak_camera_SHAPE_hyperView5.msg" "yak_camera_SHAPE_nodeEditorPanel2Info1.b[0]"
		;
connectAttr "yak_camera_SHAPE_hyperView6.msg" "yak_camera_SHAPE_nodeEditorPanel3Info1.b[0]"
		;
connectAttr "cameras_holder.PROJ_focal" "focalCorrectionNode.i2x";
connectAttr "camera_global.msg" "hyperLayout1.hyp[0].dn";
connectAttr "camera_globalShape.msg" "hyperLayout1.hyp[2].dn";
connectAttr "camera_globalShapeOrig.msg" "hyperLayout1.hyp[3].dn";
connectAttr "cluster9Set.msg" "hyperLayout2.hyp[0].dn";
connectAttr "cluster1Set.msg" "hyperLayout2.hyp[1].dn";
connectAttr "cameraHD_2dShape.msg" "hyperLayout2.hyp[2].dn";
connectAttr "groupId22.msg" "hyperLayout2.hyp[3].dn";
connectAttr "groupId26.msg" "hyperLayout2.hyp[4].dn";
connectAttr "cameraHDLineShapeOrig.msg" "hyperLayout2.hyp[5].dn";
connectAttr "cluster9GroupId1.msg" "hyperLayout2.hyp[6].dn";
connectAttr "cluster7HandleShape.msg" "hyperLayout2.hyp[7].dn";
connectAttr "cameraHD_2d_cluster.msg" "hyperLayout2.hyp[8].dn";
connectAttr "cluster10GroupId.msg" "hyperLayout2.hyp[9].dn";
connectAttr "cameraHDLineShape.msg" "hyperLayout2.hyp[10].dn";
connectAttr "cluster8Handle.msg" "hyperLayout2.hyp[11].dn";
connectAttr "tweakSet12.msg" "hyperLayout2.hyp[12].dn";
connectAttr "cluster10Handle.msg" "hyperLayout2.hyp[13].dn";
connectAttr "cluster8HandleShape.msg" "hyperLayout2.hyp[14].dn";
connectAttr "cameraHD_2d_clusterCluster.msg" "hyperLayout2.hyp[15].dn";
connectAttr "cluster1GroupParts.msg" "hyperLayout2.hyp[16].dn";
connectAttr "fake2dLocator.msg" "hyperLayout2.hyp[17].dn";
connectAttr "cluster8GroupId.msg" "hyperLayout2.hyp[18].dn";
connectAttr "zoomFactor2d.msg" "hyperLayout2.hyp[19].dn";
connectAttr "fake2dLineShapeOrig.msg" "hyperLayout2.hyp[20].dn";
connectAttr "cluster11GroupId.msg" "hyperLayout2.hyp[21].dn";
connectAttr "cluster7Handle_pointConstraint1.msg" "hyperLayout2.hyp[22].dn";
connectAttr "cluster1GroupId.msg" "hyperLayout2.hyp[23].dn";
connectAttr "cluster8Set.msg" "hyperLayout2.hyp[24].dn";
connectAttr "tweakSet14.msg" "hyperLayout2.hyp[25].dn";
connectAttr "cluster7.msg" "hyperLayout2.hyp[26].dn";
connectAttr "cluster9Handle.msg" "hyperLayout2.hyp[27].dn";
connectAttr "cluster7GroupParts.msg" "hyperLayout2.hyp[28].dn";
connectAttr "cluster8.msg" "hyperLayout2.hyp[29].dn";
connectAttr "cluster9HandleShape.msg" "hyperLayout2.hyp[30].dn";
connectAttr "tweakSet13.msg" "hyperLayout2.hyp[31].dn";
connectAttr "cluster9.msg" "hyperLayout2.hyp[32].dn";
connectAttr "tweak13.msg" "hyperLayout2.hyp[33].dn";
connectAttr "cluster9GroupParts1.msg" "hyperLayout2.hyp[34].dn";
connectAttr "groupParts26.msg" "hyperLayout2.hyp[35].dn";
connectAttr "cameraHDShape.msg" "hyperLayout2.hyp[36].dn";
connectAttr "panX_multiplyDivide.msg" "hyperLayout2.hyp[37].dn";
connectAttr "cluster10.msg" "hyperLayout2.hyp[38].dn";
connectAttr "cluster11Handle.msg" "hyperLayout2.hyp[39].dn";
connectAttr "cluster10GroupParts.msg" "hyperLayout2.hyp[40].dn";
connectAttr "cluster11.msg" "hyperLayout2.hyp[41].dn";
connectAttr "groupId2.msg" "hyperLayout2.hyp[42].dn";
connectAttr "XXXShapeOrig.msg" "hyperLayout2.hyp[43].dn";
connectAttr "cluster9GroupId.msg" "hyperLayout2.hyp[44].dn";
connectAttr "addDoubleLinear1.msg" "hyperLayout2.hyp[45].dn";
connectAttr "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.msg" "hyperLayout2.hyp[46].dn"
		;
connectAttr "tweakSet11.msg" "hyperLayout2.hyp[47].dn";
connectAttr "groupId28.msg" "hyperLayout2.hyp[48].dn";
connectAttr "camera_global.msg" "hyperLayout2.hyp[49].dn";
connectAttr "cluster10Set.msg" "hyperLayout2.hyp[50].dn";
connectAttr "cluster10Handle_pointConstraint1.msg" "hyperLayout2.hyp[51].dn";
connectAttr "fake2dLineShape.msg" "hyperLayout2.hyp[52].dn";
connectAttr "hyperLayout2.msg" "hyperLayout2.hyp[53].dn";
connectAttr "unitConversion1.msg" "hyperLayout2.hyp[54].dn";
connectAttr "cluster11HandleShape.msg" "hyperLayout2.hyp[55].dn";
connectAttr "cluster7Set.msg" "hyperLayout2.hyp[56].dn";
connectAttr "tweak1.msg" "hyperLayout2.hyp[57].dn";
connectAttr "groupParts2.msg" "hyperLayout2.hyp[58].dn";
connectAttr "cluster7GroupId.msg" "hyperLayout2.hyp[59].dn";
connectAttr "|camera_rig|rig_extra|cameraHD_2d|nurbsCircleShape4Orig.msg" "hyperLayout2.hyp[60].dn"
		;
connectAttr "groupId25.msg" "hyperLayout2.hyp[61].dn";
connectAttr "tweakSet1.msg" "hyperLayout2.hyp[62].dn";
connectAttr "XXXShape.msg" "hyperLayout2.hyp[63].dn";
connectAttr "cameraHD_2d_clusterShape.msg" "hyperLayout2.hyp[64].dn";
connectAttr "cameraHD_controller.msg" "hyperLayout2.hyp[65].dn";
connectAttr "cluster11Set.msg" "hyperLayout2.hyp[66].dn";
connectAttr "cluster11Handle_pointConstraint1.msg" "hyperLayout2.hyp[67].dn";
connectAttr "tweak11.msg" "hyperLayout2.hyp[68].dn";
connectAttr "groupParts22.msg" "hyperLayout2.hyp[69].dn";
connectAttr "cluster8GroupParts.msg" "hyperLayout2.hyp[70].dn";
connectAttr "cluster7Handle.msg" "hyperLayout2.hyp[71].dn";
connectAttr "cameraHD_2dShapeOrig.msg" "hyperLayout2.hyp[72].dn";
connectAttr "tweak12.msg" "hyperLayout2.hyp[73].dn";
connectAttr "cluster10HandleShape.msg" "hyperLayout2.hyp[74].dn";
connectAttr "cluster9GroupParts.msg" "hyperLayout2.hyp[75].dn";
connectAttr "groupParts25.msg" "hyperLayout2.hyp[76].dn";
connectAttr "unitConversion2.msg" "hyperLayout2.hyp[77].dn";
connectAttr "panY_multiplyDivide.msg" "hyperLayout2.hyp[78].dn";
connectAttr "tweak14.msg" "hyperLayout2.hyp[79].dn";
connectAttr "groupParts28.msg" "hyperLayout2.hyp[80].dn";
connectAttr "cluster11GroupParts.msg" "hyperLayout2.hyp[81].dn";
connectAttr "multiplyDivide1.msg" "hyperLayout2.hyp[82].dn";
connectAttr "cameraHD_controller.roll" "unitConversion1.i";
connectAttr "cameraHD_controller.panX" "panX_multiplyDivide.i1x";
connectAttr "cameraHD_controller.panSensitivity" "panX_multiplyDivide.i2x";
connectAttr "cameraHD_controller.panY" "panY_multiplyDivide.i1x";
connectAttr "cameraHD_controller.panSensitivity" "panY_multiplyDivide.i2x";
connectAttr "cluster1GroupParts.og" "cameraHD_2d_clusterCluster.ip[0].ig";
connectAttr "cluster1GroupId.id" "cameraHD_2d_clusterCluster.ip[0].gi";
connectAttr "cameraHD_2d_cluster.wm" "cameraHD_2d_clusterCluster.ma";
connectAttr "cameraHD_2d_clusterShape.x" "cameraHD_2d_clusterCluster.x";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "cluster1GroupId.msg" "cluster1Set.gn" -na;
connectAttr "XXXShape.iog.og[2]" "cluster1Set.dsm" -na;
connectAttr "cameraHD_2d_clusterCluster.msg" "cluster1Set.ub[0]";
connectAttr "tweak1.og[0]" "cluster1GroupParts.ig";
connectAttr "cluster1GroupId.id" "cluster1GroupParts.gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "XXXShape.iog.og[3]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "XXXShapeOrig.w" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "cluster2GroupParts.og" "aim_clusterCluster.ip[0].ig";
connectAttr "cluster2GroupId.id" "aim_clusterCluster.ip[0].gi";
connectAttr "cluster2GroupParts1.og" "aim_clusterCluster.ip[1].ig";
connectAttr "cluster2GroupId1.id" "aim_clusterCluster.ip[1].gi";
connectAttr "cluster2GroupParts2.og" "aim_clusterCluster.ip[2].ig";
connectAttr "cluster2GroupId2.id" "aim_clusterCluster.ip[2].gi";
connectAttr "cluster2GroupParts3.og" "aim_clusterCluster.ip[3].ig";
connectAttr "cluster2GroupId3.id" "aim_clusterCluster.ip[3].gi";
connectAttr "cluster2GroupParts4.og" "aim_clusterCluster.ip[4].ig";
connectAttr "cluster2GroupId4.id" "aim_clusterCluster.ip[4].gi";
connectAttr "|camera_rig|camera_global|camera_aim|camera_aim_rig|aim_cluster|aim_cluster.wm" "aim_clusterCluster.ma"
		;
connectAttr "aim_clusterShape.x" "aim_clusterCluster.x";
connectAttr "groupParts8.og" "tweak2.ip[0].ig";
connectAttr "groupId8.id" "tweak2.ip[0].gi";
connectAttr "groupParts9.og" "tweak3.ip[0].ig";
connectAttr "groupId9.id" "tweak3.ip[0].gi";
connectAttr "groupParts10.og" "tweak4.ip[0].ig";
connectAttr "groupId10.id" "tweak4.ip[0].gi";
connectAttr "groupParts11.og" "tweak5.ip[0].ig";
connectAttr "groupId11.id" "tweak5.ip[0].gi";
connectAttr "groupParts12.og" "tweak6.ip[0].ig";
connectAttr "groupId12.id" "tweak6.ip[0].gi";
connectAttr "cluster2GroupId.msg" "cluster2Set.gn" -na;
connectAttr "cluster2GroupId1.msg" "cluster2Set.gn" -na;
connectAttr "cluster2GroupId2.msg" "cluster2Set.gn" -na;
connectAttr "cluster2GroupId3.msg" "cluster2Set.gn" -na;
connectAttr "cluster2GroupId4.msg" "cluster2Set.gn" -na;
connectAttr "camera_aimShape.iog.og[0]" "cluster2Set.dsm" -na;
connectAttr "curveShape3.iog.og[0]" "cluster2Set.dsm" -na;
connectAttr "curveShape2.iog.og[0]" "cluster2Set.dsm" -na;
connectAttr "nurbsCircleShape3.iog.og[0]" "cluster2Set.dsm" -na;
connectAttr "nurbsCircleShape2.iog.og[0]" "cluster2Set.dsm" -na;
connectAttr "aim_clusterCluster.msg" "cluster2Set.ub[0]";
connectAttr "tweak2.og[0]" "cluster2GroupParts.ig";
connectAttr "cluster2GroupId.id" "cluster2GroupParts.gi";
connectAttr "tweak3.og[0]" "cluster2GroupParts1.ig";
connectAttr "cluster2GroupId1.id" "cluster2GroupParts1.gi";
connectAttr "tweak4.og[0]" "cluster2GroupParts2.ig";
connectAttr "cluster2GroupId2.id" "cluster2GroupParts2.gi";
connectAttr "tweak5.og[0]" "cluster2GroupParts3.ig";
connectAttr "cluster2GroupId3.id" "cluster2GroupParts3.gi";
connectAttr "tweak6.og[0]" "cluster2GroupParts4.ig";
connectAttr "cluster2GroupId4.id" "cluster2GroupParts4.gi";
connectAttr "groupId8.msg" "tweakSet2.gn" -na;
connectAttr "camera_aimShape.iog.og[1]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "camera_aimShapeOrig.ws" "groupParts8.ig";
connectAttr "groupId8.id" "groupParts8.gi";
connectAttr "groupId9.msg" "tweakSet3.gn" -na;
connectAttr "curveShape3.iog.og[1]" "tweakSet3.dsm" -na;
connectAttr "tweak3.msg" "tweakSet3.ub[0]";
connectAttr "curveShape3Orig.ws" "groupParts9.ig";
connectAttr "groupId9.id" "groupParts9.gi";
connectAttr "groupId10.msg" "tweakSet4.gn" -na;
connectAttr "curveShape2.iog.og[1]" "tweakSet4.dsm" -na;
connectAttr "tweak4.msg" "tweakSet4.ub[0]";
connectAttr "curveShape2Orig.ws" "groupParts10.ig";
connectAttr "groupId10.id" "groupParts10.gi";
connectAttr "groupId11.msg" "tweakSet5.gn" -na;
connectAttr "nurbsCircleShape3.iog.og[1]" "tweakSet5.dsm" -na;
connectAttr "tweak5.msg" "tweakSet5.ub[0]";
connectAttr "nurbsCircleShape3Orig.ws" "groupParts11.ig";
connectAttr "groupId11.id" "groupParts11.gi";
connectAttr "groupId12.msg" "tweakSet6.gn" -na;
connectAttr "nurbsCircleShape2.iog.og[1]" "tweakSet6.dsm" -na;
connectAttr "tweak6.msg" "tweakSet6.ub[0]";
connectAttr "nurbsCircleShape2Orig.ws" "groupParts12.ig";
connectAttr "groupId12.id" "groupParts12.gi";
connectAttr "cluster3GroupParts.og" "global_clusterCluster.ip[0].ig";
connectAttr "cluster3GroupId.id" "global_clusterCluster.ip[0].gi";
connectAttr "|camera_rig|camera_global|camera_global_rig|global_cluster|global_cluster.wm" "global_clusterCluster.ma"
		;
connectAttr "global_clusterShape.x" "global_clusterCluster.x";
connectAttr "groupParts14.og" "tweak7.ip[0].ig";
connectAttr "groupId14.id" "tweak7.ip[0].gi";
connectAttr "cluster3GroupId.msg" "cluster3Set.gn" -na;
connectAttr "camera_globalShape.iog.og[0]" "cluster3Set.dsm" -na;
connectAttr "global_clusterCluster.msg" "cluster3Set.ub[0]";
connectAttr "tweak7.og[0]" "cluster3GroupParts.ig";
connectAttr "cluster3GroupId.id" "cluster3GroupParts.gi";
connectAttr "groupId14.msg" "tweakSet7.gn" -na;
connectAttr "camera_globalShape.iog.og[1]" "tweakSet7.dsm" -na;
connectAttr "tweak7.msg" "tweakSet7.ub[0]";
connectAttr "camera_globalShapeOrig.ws" "groupParts14.ig";
connectAttr "groupId14.id" "groupParts14.gi";
connectAttr "cluster4GroupParts.og" "holder_clusterCluster.ip[0].ig";
connectAttr "cluster4GroupId.id" "holder_clusterCluster.ip[0].gi";
connectAttr "cluster4GroupParts1.og" "holder_clusterCluster.ip[1].ig";
connectAttr "cluster4GroupId1.id" "holder_clusterCluster.ip[1].gi";
connectAttr "|camera_rig|camera_global|cameras_holder|cameras_holder_rig|holder_cluster|holder_cluster.wm" "holder_clusterCluster.ma"
		;
connectAttr "holder_clusterShape.x" "holder_clusterCluster.x";
connectAttr "groupParts17.og" "tweak8.ip[0].ig";
connectAttr "groupId17.id" "tweak8.ip[0].gi";
connectAttr "groupParts18.og" "tweak9.ip[0].ig";
connectAttr "groupId18.id" "tweak9.ip[0].gi";
connectAttr "cluster4GroupId.msg" "cluster4Set.gn" -na;
connectAttr "cluster4GroupId1.msg" "cluster4Set.gn" -na;
connectAttr "cameras_holderShape.iog.og[0]" "cluster4Set.dsm" -na;
connectAttr "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.iog.og[0]" "cluster4Set.dsm"
		 -na;
connectAttr "holder_clusterCluster.msg" "cluster4Set.ub[0]";
connectAttr "tweak8.og[0]" "cluster4GroupParts.ig";
connectAttr "cluster4GroupId.id" "cluster4GroupParts.gi";
connectAttr "tweak9.og[0]" "cluster4GroupParts1.ig";
connectAttr "cluster4GroupId1.id" "cluster4GroupParts1.gi";
connectAttr "groupId17.msg" "tweakSet8.gn" -na;
connectAttr "cameras_holderShape.iog.og[1]" "tweakSet8.dsm" -na;
connectAttr "tweak8.msg" "tweakSet8.ub[0]";
connectAttr "cameras_holderShapeOrig.ws" "groupParts17.ig";
connectAttr "groupId17.id" "groupParts17.gi";
connectAttr "groupId18.msg" "tweakSet9.gn" -na;
connectAttr "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4.iog.og[1]" "tweakSet9.dsm"
		 -na;
connectAttr "tweak9.msg" "tweakSet9.ub[0]";
connectAttr "|camera_rig|camera_global|cameras_holder|nurbsCircleShape4Orig.ws" "groupParts18.ig"
		;
connectAttr "groupId18.id" "groupParts18.gi";
connectAttr "plateCtrlShape1.msg" "hyperLayout3.hyp[0].dn";
connectAttr "plateCtrl.msg" "hyperLayout3.hyp[1].dn";
connectAttr "plateCtrlShape.msg" "hyperLayout3.hyp[2].dn";
connectAttr "cluster5GroupParts.og" "cluster5.ip[0].ig";
connectAttr "cluster5GroupId.id" "cluster5.ip[0].gi";
connectAttr "cluster5Handle.wm" "cluster5.ma";
connectAttr "cluster5HandleShape.x" "cluster5.x";
connectAttr "cluster5GroupId.msg" "cluster5Set.gn" -na;
connectAttr "aimLineShape.iog.og[0]" "cluster5Set.dsm" -na;
connectAttr "cluster5.msg" "cluster5Set.ub[0]";
connectAttr "cluster6GroupParts.og" "cluster6.ip[0].ig";
connectAttr "cluster6GroupId.id" "cluster6.ip[0].gi";
connectAttr "cluster6Handle.wm" "cluster6.ma";
connectAttr "cluster6HandleShape.x" "cluster6.x";
connectAttr "cluster6GroupId.msg" "cluster6Set.gn" -na;
connectAttr "aimLineShape.iog.og[2]" "cluster6Set.dsm" -na;
connectAttr "cluster6.msg" "cluster6Set.ub[0]";
connectAttr "cluster5.og[0]" "cluster6GroupParts.ig";
connectAttr "cluster6GroupId.id" "cluster6GroupParts.gi";
connectAttr "aimLineShapeOrig.ws" "groupParts20.ig";
connectAttr "groupId20.id" "groupParts20.gi";
connectAttr "groupParts20.og" "tweak10.ip[0].ig";
connectAttr "groupId20.id" "tweak10.ip[0].gi";
connectAttr "tweak10.og[0]" "cluster5GroupParts.ig";
connectAttr "cluster5GroupId.id" "cluster5GroupParts.gi";
connectAttr "groupId20.msg" "tweakSet10.gn" -na;
connectAttr "aimLineShape.iog.og[1]" "tweakSet10.dsm" -na;
connectAttr "tweak10.msg" "tweakSet10.ub[0]";
connectAttr "cluster7GroupParts.og" "cluster7.ip[0].ig";
connectAttr "cluster7GroupId.id" "cluster7.ip[0].gi";
connectAttr "cluster7Handle.wm" "cluster7.ma";
connectAttr "cluster7HandleShape.x" "cluster7.x";
connectAttr "groupParts22.og" "tweak11.ip[0].ig";
connectAttr "groupId22.id" "tweak11.ip[0].gi";
connectAttr "cluster7GroupId.msg" "cluster7Set.gn" -na;
connectAttr "cameraHDLineShape.iog.og[0]" "cluster7Set.dsm" -na;
connectAttr "cluster7.msg" "cluster7Set.ub[0]";
connectAttr "tweak11.og[0]" "cluster7GroupParts.ig";
connectAttr "cluster7GroupId.id" "cluster7GroupParts.gi";
connectAttr "groupId22.msg" "tweakSet11.gn" -na;
connectAttr "cameraHDLineShape.iog.og[1]" "tweakSet11.dsm" -na;
connectAttr "tweak11.msg" "tweakSet11.ub[0]";
connectAttr "cameraHDLineShapeOrig.ws" "groupParts22.ig";
connectAttr "groupId22.id" "groupParts22.gi";
connectAttr "cluster8GroupParts.og" "cluster8.ip[0].ig";
connectAttr "cluster8GroupId.id" "cluster8.ip[0].gi";
connectAttr "cluster8Handle.wm" "cluster8.ma";
connectAttr "cluster8HandleShape.x" "cluster8.x";
connectAttr "cluster8GroupId.msg" "cluster8Set.gn" -na;
connectAttr "cameraHDLineShape.iog.og[2]" "cluster8Set.dsm" -na;
connectAttr "cluster8.msg" "cluster8Set.ub[0]";
connectAttr "cluster7.og[0]" "cluster8GroupParts.ig";
connectAttr "cluster8GroupId.id" "cluster8GroupParts.gi";
connectAttr "cluster9GroupParts.og" "cluster9.ip[0].ig";
connectAttr "cluster9GroupId.id" "cluster9.ip[0].gi";
connectAttr "cluster9GroupParts1.og" "cluster9.ip[1].ig";
connectAttr "cluster9GroupId1.id" "cluster9.ip[1].gi";
connectAttr "cluster9Handle.wm" "cluster9.ma";
connectAttr "cluster9HandleShape.x" "cluster9.x";
connectAttr "groupParts25.og" "tweak12.ip[0].ig";
connectAttr "groupId25.id" "tweak12.ip[0].gi";
connectAttr "groupParts26.og" "tweak13.ip[0].ig";
connectAttr "groupId26.id" "tweak13.ip[0].gi";
connectAttr "cluster9GroupId.msg" "cluster9Set.gn" -na;
connectAttr "cluster9GroupId1.msg" "cluster9Set.gn" -na;
connectAttr "cameraHD_2dShape.iog.og[0]" "cluster9Set.dsm" -na;
connectAttr "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.iog.og[0]" "cluster9Set.dsm"
		 -na;
connectAttr "cluster9.msg" "cluster9Set.ub[0]";
connectAttr "tweak12.og[0]" "cluster9GroupParts.ig";
connectAttr "cluster9GroupId.id" "cluster9GroupParts.gi";
connectAttr "tweak13.og[0]" "cluster9GroupParts1.ig";
connectAttr "cluster9GroupId1.id" "cluster9GroupParts1.gi";
connectAttr "groupId25.msg" "tweakSet12.gn" -na;
connectAttr "cameraHD_2dShape.iog.og[1]" "tweakSet12.dsm" -na;
connectAttr "tweak12.msg" "tweakSet12.ub[0]";
connectAttr "cameraHD_2dShapeOrig.ws" "groupParts25.ig";
connectAttr "groupId25.id" "groupParts25.gi";
connectAttr "groupId26.msg" "tweakSet13.gn" -na;
connectAttr "|camera_rig|camera_global|cameras_holder|cameraHD_controller|nurbsCircleShape4.iog.og[1]" "tweakSet13.dsm"
		 -na;
connectAttr "tweak13.msg" "tweakSet13.ub[0]";
connectAttr "|camera_rig|rig_extra|cameraHD_2d|nurbsCircleShape4Orig.ws" "groupParts26.ig"
		;
connectAttr "groupId26.id" "groupParts26.gi";
connectAttr "cameraHD_controller.roll" "unitConversion2.i";
connectAttr "camera_global.controllersSize" "zoomFactor2d.i1";
connectAttr "addDoubleLinear1.o" "zoomFactor2d.i2";
connectAttr "cluster10GroupParts.og" "cluster10.ip[0].ig";
connectAttr "cluster10GroupId.id" "cluster10.ip[0].gi";
connectAttr "cluster10Handle.wm" "cluster10.ma";
connectAttr "cluster10HandleShape.x" "cluster10.x";
connectAttr "groupParts28.og" "tweak14.ip[0].ig";
connectAttr "groupId28.id" "tweak14.ip[0].gi";
connectAttr "cluster10GroupId.msg" "cluster10Set.gn" -na;
connectAttr "fake2dLineShape.iog.og[0]" "cluster10Set.dsm" -na;
connectAttr "cluster10.msg" "cluster10Set.ub[0]";
connectAttr "tweak14.og[0]" "cluster10GroupParts.ig";
connectAttr "cluster10GroupId.id" "cluster10GroupParts.gi";
connectAttr "groupId28.msg" "tweakSet14.gn" -na;
connectAttr "fake2dLineShape.iog.og[1]" "tweakSet14.dsm" -na;
connectAttr "tweak14.msg" "tweakSet14.ub[0]";
connectAttr "fake2dLineShapeOrig.ws" "groupParts28.ig";
connectAttr "groupId28.id" "groupParts28.gi";
connectAttr "cluster11GroupParts.og" "cluster11.ip[0].ig";
connectAttr "cluster11GroupId.id" "cluster11.ip[0].gi";
connectAttr "cluster11Handle.wm" "cluster11.ma";
connectAttr "cluster11HandleShape.x" "cluster11.x";
connectAttr "cluster11GroupId.msg" "cluster11Set.gn" -na;
connectAttr "fake2dLineShape.iog.og[2]" "cluster11Set.dsm" -na;
connectAttr "cluster11.msg" "cluster11Set.ub[0]";
connectAttr "cluster10.og[0]" "cluster11GroupParts.ig";
connectAttr "cluster11GroupId.id" "cluster11GroupParts.gi";
connectAttr ":TurtleDefaultBakeLayer.idx" ":TurtleBakeLayerManager.bli[0]";
connectAttr ":TurtleRenderOptions.msg" ":TurtleDefaultBakeLayer.rset";
connectAttr "cameraHD.iog" "RenderSet.dsm" -na;
connectAttr "cameraPROJ.iog" "RenderSet.dsm" -na;
connectAttr "cameraHD_controller.zoom" "addDoubleLinear1.i1";
connectAttr "cameraHD_controller.zoomNew" "addDoubleLinear1.i2";
connectAttr "cameraHD_controller.zoomNew" "multiplyDivide1.i2x";
connectAttr "focalCorrectionNode.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "panX_multiplyDivide.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "panY_multiplyDivide.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "zoomFactor2d.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "addDoubleLinear1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multiplyDivide1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":perspShape.msg" ":defaultRenderGlobals.sc";
// End of yak_camera.ma
