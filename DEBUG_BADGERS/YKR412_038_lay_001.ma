//Maya ASCII 2015 scene
//Name: YKR412_038_lay_001.ma
//Last modified: Tue, Oct 25, 2016 10:38:11 AM
//Codeset: 1252
file -rdi 1 -ns "pr_arr03" -rfn "pr_arr03RN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/pr/pr_arr03/rig/pr_arr03_rig.ma";
file -rdi 1 -ns "pr_bow05" -rfn "pr_bow05RN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/pr/pr_bow05/rig/pr_bow05_rig.ma";
file -rdi 1 -ns "st_YKR412_0380" -rfn "st_YKR412_0380RN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/st/st_412_0380/rig/st_YKR412_0380_rig.ma";
file -rdi 1 -ns "ch_wildw" -rfn "ch_wildwRN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/ch/ch_wildw/low/ch_wildw_low.ma";
file -rdi 1 -ns "SH038_CAM" -rfn "SH038_CAMRN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/cam/yak_camera.ma";
file -r -ns "pr_arr03" -dr 1 -rfn "pr_arr03RN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/pr/pr_arr03/rig/pr_arr03_rig.ma";
file -r -ns "pr_bow05" -dr 1 -rfn "pr_bow05RN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/pr/pr_bow05/rig/pr_bow05_rig.ma";
file -r -ns "st_YKR412_0380" -dr 1 -rfn "st_YKR412_0380RN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/st/st_412_0380/rig/st_YKR412_0380_rig.ma";
file -r -ns "ch_wildw" -dr 1 -rfn "ch_wildwRN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/ch/ch_wildw/low/ch_wildw_low.ma";
file -r -ns "SH038_CAM" -dr 1 -rfn "SH038_CAMRN" -op "v=0;" "$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/cam/yak_camera.ma";
requires maya "2015";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2015.0.0";
requires -nodeType "mentalrayFramebuffer" -nodeType "mentalrayOptions" -nodeType "mentalrayGlobals"
		 -nodeType "mentalrayItemsList" -dataType "byteArray" "Mayatomr" "2015.0 - 3.12.1.12 ";
currentUnit -l centimeter -a degree -t pal;
fileInfo "application" "maya";
fileInfo "product" "Maya 2015";
fileInfo "version" "2015";
fileInfo "cutIdentifier" "201503261530-955654";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 386.55454244737393 436.74094222194503 503.99444163854804 ;
	setAttr ".r" -type "double3" -33.938352729602997 35.4 1.95095462216496e-015 ;
createNode camera -s -n "perspShape" -p "persp";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 683.32371243761372;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -11.65970859343593 35.004543142163008 5.5069072462838786 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "__SUBSET__";
createNode transform -n "__SET__";
createNode transform -n "platesHolder" -p "__SET__";
	addAttr -ci true -sn "size" -ln "size" -dv 1 -at "double";
	setAttr -k on ".size";
createNode parentConstraint -n "platesHolder_parentConstraint1" -p "platesHolder";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "camera_aimW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 6.8564358991690808 0 0 ;
	setAttr ".rst" -type "double3" 0 0 -200 ;
	setAttr -k on ".w0";
createNode transform -n "cameraMarker" -p "platesHolder";
createNode pointConstraint -n "cameraMarker_pointConstraint1" -p "cameraMarker";
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
	setAttr ".rst" -type "double3" 0 0 300 ;
	setAttr -k on ".w0";
createNode transform -n "SH038_CAM:plateCtrl3_offset" -p "platesHolder";
	setAttr ".t" -type "double3" 0 0 200 ;
createNode transform -n "SH038_CAM:plateCtrl3" -p "SH038_CAM:plateCtrl3_offset";
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
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -cb on ".ROTATION_OFFSET";
	setAttr -k on ".rotX";
	setAttr -k on ".rotY";
	setAttr -k on ".rotZ";
	setAttr -cb on ".PLATE_OPTIONS";
	setAttr -k on ".lockPlate" 1;
	setAttr -k on ".showPlate";
createNode nurbsCurve -n "SH038_CAM:plateCtrl3Shape" -p "SH038_CAM:plateCtrl3";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "SH038_CAM:plateCtrl3Shape1" -p "SH038_CAM:plateCtrl3";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode transform -n "plusPlate" -p "SH038_CAM:plateCtrl3";
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
createNode nurbsCurve -n "plusPlateShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".tw" yes;
createNode nurbsCurve -n "plusPlateShapeOrig" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "minusPlate" -p "SH038_CAM:plateCtrl3";
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
createNode nurbsCurve -n "minusPlateShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "minusPlateShapeOrig" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "resizingArrows" -p "SH038_CAM:plateCtrl3";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "resizingUp" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingUpShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingUp";
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
createNode transform -n "resizingDown" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingDownShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingDown";
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
createNode transform -n "resizingRight" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingRightShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingRight";
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
createNode transform -n "resizingLeft" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingLeftShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingLeft";
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
createNode nurbsCurve -n "plateCtrl3ShapeOrig" -p "SH038_CAM:plateCtrl3";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode nurbsCurve -n "plateCtrl3Shape1Orig" -p "SH038_CAM:plateCtrl3";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "SH038_CAM:plateCtrl3ClusteringHandle" -p "SH038_CAM:plateCtrl3_offset";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 1.1904288037202804 -1.7554995415183541 7.1654593736314816 ;
	setAttr ".sp" -type "double3" 1.1904288037202804 -1.7554995415183541 7.1654593736314816 ;
createNode clusterHandle -n "SH038_CAM:plateCtrl3ClusteringHandleShape" -p "SH038_CAM:plateCtrl3ClusteringHandle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.1904288037202804 -1.7554995415183541 7.1654593736314816 ;
createNode transform -n "SH038_CAM:plateCtrl2_offset" -p "platesHolder";
	setAttr ".t" -type "double3" 0 0 100 ;
createNode transform -n "SH038_CAM:plateCtrl2" -p "SH038_CAM:plateCtrl2_offset";
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
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -cb on ".ROTATION_OFFSET";
	setAttr -k on ".rotX";
	setAttr -k on ".rotY";
	setAttr -k on ".rotZ";
	setAttr -cb on ".PLATE_OPTIONS";
	setAttr -k on ".lockPlate" 1;
	setAttr -k on ".showPlate" 1;
createNode nurbsCurve -n "SH038_CAM:plateCtrl2Shape" -p "SH038_CAM:plateCtrl2";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "SH038_CAM:plateCtrl2Shape1" -p "SH038_CAM:plateCtrl2";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode transform -n "plusPlate" -p "SH038_CAM:plateCtrl2";
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
createNode nurbsCurve -n "plusPlateShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".tw" yes;
createNode nurbsCurve -n "plusPlateShapeOrig" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "minusPlate" -p "SH038_CAM:plateCtrl2";
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
createNode nurbsCurve -n "minusPlateShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "minusPlateShapeOrig" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "resizingArrows" -p "SH038_CAM:plateCtrl2";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "resizingUp" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingUpShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingUp";
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
createNode transform -n "resizingDown" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingDownShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingDown";
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
createNode transform -n "resizingRight" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingRightShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingRight";
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
createNode transform -n "resizingLeft" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingLeftShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingLeft";
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
createNode nurbsCurve -n "plateCtrl2ShapeOrig" -p "SH038_CAM:plateCtrl2";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode nurbsCurve -n "plateCtrl2Shape1Orig" -p "SH038_CAM:plateCtrl2";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "SH038_CAM:plateCtrl2ClusteringHandle" -p "SH038_CAM:plateCtrl2_offset";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 1.1904288037202804 -1.7554995415183541 -92.834540626368522 ;
	setAttr ".sp" -type "double3" 1.1904288037202804 -1.7554995415183541 -92.834540626368522 ;
createNode clusterHandle -n "SH038_CAM:plateCtrl2ClusteringHandleShape" -p "SH038_CAM:plateCtrl2ClusteringHandle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.1904288037202804 -1.7554995415183541 -92.834540626368522 ;
createNode transform -n "SH038_CAM:plateCtrl1_offset" -p "platesHolder";
createNode transform -n "SH038_CAM:plateCtrl1" -p "SH038_CAM:plateCtrl1_offset";
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
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 192.73516564731014 2.8421709430404064e-014 2.5243548967072378e-029 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -cb on ".ROTATION_OFFSET";
	setAttr -k on ".rotX";
	setAttr -k on ".rotY";
	setAttr -k on ".rotZ";
	setAttr -cb on ".PLATE_OPTIONS";
	setAttr -k on ".lockPlate" 1;
	setAttr -k on ".showPlate" 1;
createNode nurbsCurve -n "SH038_CAM:plateCtrl1Shape" -p "SH038_CAM:plateCtrl1";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode nurbsCurve -n "SH038_CAM:plateCtrl1Shape1" -p "SH038_CAM:plateCtrl1";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".tw" yes;
createNode transform -n "plusPlate" -p "SH038_CAM:plateCtrl1";
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
createNode nurbsCurve -n "plusPlateShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".tw" yes;
createNode nurbsCurve -n "plusPlateShapeOrig" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "minusPlate" -p "SH038_CAM:plateCtrl1";
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
createNode nurbsCurve -n "minusPlateShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".tw" yes;
createNode nurbsCurve -n "minusPlateShapeOrig" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "resizingArrows" -p "SH038_CAM:plateCtrl1";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "resizingUp" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingUpShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingUp";
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
createNode transform -n "resizingDown" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingDownShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingDown";
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
createNode transform -n "resizingRight" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingRightShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingRight";
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
createNode transform -n "resizingLeft" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
createNode nurbsCurve -n "resizingLeftShape" -p "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingLeft";
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
createNode nurbsCurve -n "plateCtrl1ShapeOrig" -p "SH038_CAM:plateCtrl1";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode nurbsCurve -n "plateCtrl1Shape1Orig" -p "SH038_CAM:plateCtrl1";
	setAttr -k off ".v";
	setAttr ".io" yes;
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
createNode transform -n "SH038_CAM:plateCtrl1ClusteringHandle" -p "SH038_CAM:plateCtrl1_offset";
	setAttr ".v" no;
	setAttr ".rp" -type "double3" 1.1904288037202804 -1.7554995415183541 -192.83454062636849 ;
	setAttr ".sp" -type "double3" 1.1904288037202804 -1.7554995415183541 -192.83454062636849 ;
createNode clusterHandle -n "SH038_CAM:plateCtrl1ClusteringHandleShape" -p "SH038_CAM:plateCtrl1ClusteringHandle";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 1.1904288037202804 -1.7554995415183541 -192.83454062636849 ;
createNode transform -n "__CAMERA__";
createNode transform -n "sh038ImagePlane" -p "__CAMERA__";
createNode imagePlane -n "sh038ImagePlaneShape" -p "sh038ImagePlane";
	setAttr -k off ".v";
	setAttr ".fc" 204;
	setAttr ".imn" -type "string" "$PROD_SERVER/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR412/animatic/panels/edit_01/YKR_412_038_01.jpg";
	setAttr ".ufe" yes;
	setAttr ".cov" -type "short2" 528 297 ;
	setAttr ".f" 0;
	setAttr ".dic" yes;
	setAttr ".s" -type "double2" 1 1 ;
createNode transform -n "__CHARS__";
createNode transform -n "__PROPS__";
createNode fosterParent -n "pr_arr03RNfosterParent1";
createNode parentConstraint -n "Global_SRT_parentConstraint2" -p "pr_arr03RNfosterParent1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "clnLyW_hand_RW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" -2.862994386389504 -6.2566680406381963 1.444979046578414 ;
	setAttr ".tg[0].tor" -type "double3" 86.270742495423207 0.72091261880439894 44.150386250623569 ;
	setAttr ".lr" -type "double3" 115.94066359746215 -7.1735913214385452 78.307508717156537 ;
	setAttr ".rst" -type "double3" -10.301710328995499 35.004543142163001 7.485114526311115 ;
	setAttr ".rsrr" -type "double3" 113.87965279869982 9.0838441583682936 86.794851812708828 ;
	setAttr -k on ".w0";
createNode fosterParent -n "pr_bow05RNfosterParent1";
createNode parentConstraint -n "Global_SRT_parentConstraint1" -p "pr_bow05RNfosterParent1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "clnLyW_hand_RW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" -2.8629943863895075 -6.2566680406382034 1.4449790465784123 ;
	setAttr ".tg[0].tor" -type "double3" 86.270742495423193 0.72091261880439428 44.150386250623569 ;
	setAttr ".lr" -type "double3" 115.94066359746215 -7.1735913214385372 78.307508717156523 ;
	setAttr ".rst" -type "double3" -14.865382870123373 50.511606265747467 10.801031062498 ;
	setAttr ".rsrr" -type "double3" 113.87965279869982 9.0838441583682865 86.794851812708828 ;
	setAttr -k on ".w0";
createNode fosterParent -n "st_YKR412_0380RNfosterParent1";
createNode parentConstraint -n "YKR412_038_03_GlobalSRT_FD_parentConstraint1" -p
		 "st_YKR412_0380RNfosterParent1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "plateCtrl3W0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 6.8564358991690852 0 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "YKR412_038_02_GlobalSRT_FX_parentConstraint1" -p "st_YKR412_0380RNfosterParent1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "plateCtrl2W0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 6.8564358991690852 0 0 ;
	setAttr ".rst" -type "double3" 0 0 -100 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "YKR412_038_01_GlobalSRT_BG_parentConstraint1" -p "st_YKR412_0380RNfosterParent1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "plateCtrl1W0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 6.8564358991690844 0 0 ;
	setAttr ".rst" -type "double3" 0 0 -200 ;
	setAttr -k on ".w0";
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 98 ".lnk";
	setAttr -s 98 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
	setAttr -s 24 ".adjs";
	setAttr ".adjs[0].val" 2;
	setAttr ".adjs[1].val" 0;
	setAttr ".adjs[2].val" 0;
	setAttr ".adjs[3].val" 0;
	setAttr ".adjs[4].val" 0;
	setAttr ".adjs[5].val" 0;
	setAttr ".adjs[6].val" 0;
	setAttr ".adjs[7].val" 0;
	setAttr ".adjs[8].val" 0;
	setAttr ".adjs[9].val" 0;
	setAttr ".adjs[10].val" 0;
	setAttr ".adjs[11].val" 0;
	setAttr ".adjs[12].val" 0;
	setAttr ".adjs[13].val" 0;
	setAttr ".adjs[14].val" 0;
	setAttr ".adjs[15].val" 0;
	setAttr ".adjs[16].val" 0;
	setAttr ".adjs[17].val" 0;
	setAttr ".adjs[18].val" 0;
	setAttr ".adjs[19].val" 0;
	setAttr ".adjs[20].val" 0;
	setAttr ".adjs[21].val" 0;
	setAttr ".adjs[22].val" 0;
	setAttr ".adjs[23].val" 0;
	setAttr -s 5 ".oajs";
	setAttr ".oajs[0].oaid" 0;
	setAttr ".oajs[1].oaid" 1;
	setAttr ".oajs[2].oaid" 2;
	setAttr ".oajs[3].oaid" 3;
	setAttr ".oajs[4].oaid" 4;
createNode reference -n "pr_arr03RN";
	setAttr -s 10 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"pr_arr03RN"
		"pr_arr03RN" 0
		"pr_arr03RN" 12
		0 "|pr_arr03:rig_group" "|__PROPS__" "-s -r "
		0 "|pr_arr03RNfosterParent1|Global_SRT_parentConstraint2" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT" 
		"-s -r "
		5 4 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.translateX" 
		"pr_arr03RN.placeHolderList[1]" ""
		5 4 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.translateY" 
		"pr_arr03RN.placeHolderList[2]" ""
		5 4 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.translateZ" 
		"pr_arr03RN.placeHolderList[3]" ""
		5 3 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.rotatePivot" 
		"pr_arr03RN.placeHolderList[4]" ""
		5 3 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.rotatePivotTranslate" 
		"pr_arr03RN.placeHolderList[5]" ""
		5 4 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.rotateX" 
		"pr_arr03RN.placeHolderList[6]" ""
		5 4 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.rotateY" 
		"pr_arr03RN.placeHolderList[7]" ""
		5 4 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.rotateZ" 
		"pr_arr03RN.placeHolderList[8]" ""
		5 3 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.rotateOrder" 
		"pr_arr03RN.placeHolderList[9]" ""
		5 3 "pr_arr03RN" "|__PROPS__|pr_arr03:rig_group|pr_arr03:TKRig|pr_arr03:Global_SRT_Root|pr_arr03:Global_SRT_NeutralPose|pr_arr03:Global_SRT.parentInverseMatrix" 
		"pr_arr03RN.placeHolderList[10]" "";
lockNode -l 1 ;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
lockNode -l 1 ;
createNode mentalrayItemsList -s -n "mentalrayItemsList";
	setAttr -s 2 ".opt";
createNode mentalrayGlobals -s -n "mentalrayGlobals";
	addAttr -s false -ci true -h true -sn "sunAndSkyShader" -ln "sunAndSkyShader" -at "message";
	setAttr ".rvb" 3;
	setAttr ".ivb" no;
createNode mentalrayOptions -s -n "miDefaultOptions";
	addAttr -ci true -m -sn "stringOptions" -ln "stringOptions" -at "compound" -nc 
		3;
	addAttr -ci true -sn "name" -ln "name" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "value" -ln "value" -dt "string" -p "stringOptions";
	addAttr -ci true -sn "type" -ln "type" -dt "string" -p "stringOptions";
	setAttr ".conr" 0.05000000074505806;
	setAttr ".cong" 0.05000000074505806;
	setAttr ".conb" 0.05000000074505806;
	setAttr ".cona" 0.05000000074505806;
	setAttr ".minsp" 0;
	setAttr ".maxsp" 2;
	setAttr ".fil" 4;
	setAttr ".mru" 2;
	setAttr -s 48 ".stringOptions";
	setAttr ".stringOptions[0].name" -type "string" "rast motion factor";
	setAttr ".stringOptions[0].value" -type "string" "1.0";
	setAttr ".stringOptions[0].type" -type "string" "scalar";
	setAttr ".stringOptions[1].name" -type "string" "rast transparency depth";
	setAttr ".stringOptions[1].value" -type "string" "8";
	setAttr ".stringOptions[1].type" -type "string" "integer";
	setAttr ".stringOptions[2].name" -type "string" "rast useopacity";
	setAttr ".stringOptions[2].value" -type "string" "true";
	setAttr ".stringOptions[2].type" -type "string" "boolean";
	setAttr ".stringOptions[3].name" -type "string" "importon";
	setAttr ".stringOptions[3].value" -type "string" "false";
	setAttr ".stringOptions[3].type" -type "string" "boolean";
	setAttr ".stringOptions[4].name" -type "string" "importon density";
	setAttr ".stringOptions[4].value" -type "string" "1.0";
	setAttr ".stringOptions[4].type" -type "string" "scalar";
	setAttr ".stringOptions[5].name" -type "string" "importon merge";
	setAttr ".stringOptions[5].value" -type "string" "0.0";
	setAttr ".stringOptions[5].type" -type "string" "scalar";
	setAttr ".stringOptions[6].name" -type "string" "importon trace depth";
	setAttr ".stringOptions[6].value" -type "string" "0";
	setAttr ".stringOptions[6].type" -type "string" "integer";
	setAttr ".stringOptions[7].name" -type "string" "importon traverse";
	setAttr ".stringOptions[7].value" -type "string" "true";
	setAttr ".stringOptions[7].type" -type "string" "boolean";
	setAttr ".stringOptions[8].name" -type "string" "shadowmap pixel samples";
	setAttr ".stringOptions[8].value" -type "string" "3";
	setAttr ".stringOptions[8].type" -type "string" "integer";
	setAttr ".stringOptions[9].name" -type "string" "ambient occlusion";
	setAttr ".stringOptions[9].value" -type "string" "false";
	setAttr ".stringOptions[9].type" -type "string" "boolean";
	setAttr ".stringOptions[10].name" -type "string" "ambient occlusion rays";
	setAttr ".stringOptions[10].value" -type "string" "64";
	setAttr ".stringOptions[10].type" -type "string" "integer";
	setAttr ".stringOptions[11].name" -type "string" "ambient occlusion cache";
	setAttr ".stringOptions[11].value" -type "string" "false";
	setAttr ".stringOptions[11].type" -type "string" "boolean";
	setAttr ".stringOptions[12].name" -type "string" "ambient occlusion cache density";
	setAttr ".stringOptions[12].value" -type "string" "1.0";
	setAttr ".stringOptions[12].type" -type "string" "scalar";
	setAttr ".stringOptions[13].name" -type "string" "ambient occlusion cache points";
	setAttr ".stringOptions[13].value" -type "string" "64";
	setAttr ".stringOptions[13].type" -type "string" "integer";
	setAttr ".stringOptions[14].name" -type "string" "irradiance particles";
	setAttr ".stringOptions[14].value" -type "string" "false";
	setAttr ".stringOptions[14].type" -type "string" "boolean";
	setAttr ".stringOptions[15].name" -type "string" "irradiance particles rays";
	setAttr ".stringOptions[15].value" -type "string" "256";
	setAttr ".stringOptions[15].type" -type "string" "integer";
	setAttr ".stringOptions[16].name" -type "string" "irradiance particles interpolate";
	setAttr ".stringOptions[16].value" -type "string" "1";
	setAttr ".stringOptions[16].type" -type "string" "integer";
	setAttr ".stringOptions[17].name" -type "string" "irradiance particles interppoints";
	setAttr ".stringOptions[17].value" -type "string" "64";
	setAttr ".stringOptions[17].type" -type "string" "integer";
	setAttr ".stringOptions[18].name" -type "string" "irradiance particles indirect passes";
	setAttr ".stringOptions[18].value" -type "string" "0";
	setAttr ".stringOptions[18].type" -type "string" "integer";
	setAttr ".stringOptions[19].name" -type "string" "irradiance particles scale";
	setAttr ".stringOptions[19].value" -type "string" "1.0";
	setAttr ".stringOptions[19].type" -type "string" "scalar";
	setAttr ".stringOptions[20].name" -type "string" "irradiance particles env";
	setAttr ".stringOptions[20].value" -type "string" "true";
	setAttr ".stringOptions[20].type" -type "string" "boolean";
	setAttr ".stringOptions[21].name" -type "string" "irradiance particles env rays";
	setAttr ".stringOptions[21].value" -type "string" "256";
	setAttr ".stringOptions[21].type" -type "string" "integer";
	setAttr ".stringOptions[22].name" -type "string" "irradiance particles env scale";
	setAttr ".stringOptions[22].value" -type "string" "1";
	setAttr ".stringOptions[22].type" -type "string" "integer";
	setAttr ".stringOptions[23].name" -type "string" "irradiance particles rebuild";
	setAttr ".stringOptions[23].value" -type "string" "true";
	setAttr ".stringOptions[23].type" -type "string" "boolean";
	setAttr ".stringOptions[24].name" -type "string" "irradiance particles file";
	setAttr ".stringOptions[24].value" -type "string" "";
	setAttr ".stringOptions[24].type" -type "string" "string";
	setAttr ".stringOptions[25].name" -type "string" "geom displace motion factor";
	setAttr ".stringOptions[25].value" -type "string" "1.0";
	setAttr ".stringOptions[25].type" -type "string" "scalar";
	setAttr ".stringOptions[26].name" -type "string" "contrast all buffers";
	setAttr ".stringOptions[26].value" -type "string" "true";
	setAttr ".stringOptions[26].type" -type "string" "boolean";
	setAttr ".stringOptions[27].name" -type "string" "finalgather normal tolerance";
	setAttr ".stringOptions[27].value" -type "string" "25.842";
	setAttr ".stringOptions[27].type" -type "string" "scalar";
	setAttr ".stringOptions[28].name" -type "string" "trace camera clip";
	setAttr ".stringOptions[28].value" -type "string" "false";
	setAttr ".stringOptions[28].type" -type "string" "boolean";
	setAttr ".stringOptions[29].name" -type "string" "unified sampling";
	setAttr ".stringOptions[29].value" -type "string" "false";
	setAttr ".stringOptions[29].type" -type "string" "boolean";
	setAttr ".stringOptions[30].name" -type "string" "samples quality";
	setAttr ".stringOptions[30].value" -type "string" "0.25 0.25 0.25 0.25";
	setAttr ".stringOptions[30].type" -type "string" "color";
	setAttr ".stringOptions[31].name" -type "string" "samples min";
	setAttr ".stringOptions[31].value" -type "string" "1.0";
	setAttr ".stringOptions[31].type" -type "string" "scalar";
	setAttr ".stringOptions[32].name" -type "string" "samples max";
	setAttr ".stringOptions[32].value" -type "string" "100";
	setAttr ".stringOptions[32].type" -type "string" "scalar";
	setAttr ".stringOptions[33].name" -type "string" "samples error cutoff";
	setAttr ".stringOptions[33].value" -type "string" "0.0 0.0 0.0 0.0";
	setAttr ".stringOptions[33].type" -type "string" "color";
	setAttr ".stringOptions[34].name" -type "string" "samples per object";
	setAttr ".stringOptions[34].value" -type "string" "false";
	setAttr ".stringOptions[34].type" -type "string" "boolean";
	setAttr ".stringOptions[35].name" -type "string" "progressive";
	setAttr ".stringOptions[35].value" -type "string" "false";
	setAttr ".stringOptions[35].type" -type "string" "boolean";
	setAttr ".stringOptions[36].name" -type "string" "progressive max time";
	setAttr ".stringOptions[36].value" -type "string" "0";
	setAttr ".stringOptions[36].type" -type "string" "integer";
	setAttr ".stringOptions[37].name" -type "string" "progressive subsampling size";
	setAttr ".stringOptions[37].value" -type "string" "4";
	setAttr ".stringOptions[37].type" -type "string" "integer";
	setAttr ".stringOptions[38].name" -type "string" "iray";
	setAttr ".stringOptions[38].value" -type "string" "false";
	setAttr ".stringOptions[38].type" -type "string" "boolean";
	setAttr ".stringOptions[39].name" -type "string" "light relative scale";
	setAttr ".stringOptions[39].value" -type "string" "0.31831";
	setAttr ".stringOptions[39].type" -type "string" "scalar";
	setAttr ".stringOptions[40].name" -type "string" "trace camera motion vectors";
	setAttr ".stringOptions[40].value" -type "string" "false";
	setAttr ".stringOptions[40].type" -type "string" "boolean";
	setAttr ".stringOptions[41].name" -type "string" "ray differentials";
	setAttr ".stringOptions[41].value" -type "string" "true";
	setAttr ".stringOptions[41].type" -type "string" "boolean";
	setAttr ".stringOptions[42].name" -type "string" "environment lighting mode";
	setAttr ".stringOptions[42].value" -type "string" "off";
	setAttr ".stringOptions[42].type" -type "string" "string";
	setAttr ".stringOptions[43].name" -type "string" "environment lighting quality";
	setAttr ".stringOptions[43].value" -type "string" "0.2";
	setAttr ".stringOptions[43].type" -type "string" "scalar";
	setAttr ".stringOptions[44].name" -type "string" "environment lighting shadow";
	setAttr ".stringOptions[44].value" -type "string" "transparent";
	setAttr ".stringOptions[44].type" -type "string" "string";
	setAttr ".stringOptions[45].name" -type "string" "environment lighting resolution";
	setAttr ".stringOptions[45].value" -type "string" "512";
	setAttr ".stringOptions[45].type" -type "string" "integer";
	setAttr ".stringOptions[46].name" -type "string" "environment lighting shader samples";
	setAttr ".stringOptions[46].value" -type "string" "2";
	setAttr ".stringOptions[46].type" -type "string" "integer";
	setAttr ".stringOptions[47].name" -type "string" "environment lighting scale";
	setAttr ".stringOptions[47].value" -type "string" "1.0 1.0 1.0";
	setAttr ".stringOptions[47].type" -type "string" "color";
createNode mentalrayFramebuffer -s -n "miDefaultFramebuffer";
	setAttr ".dat" 2;
createNode mentalrayOptions -s -n "miContourPreset";
createNode reference -n "pr_bow05RN";
	setAttr -s 10 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"pr_bow05RN"
		"pr_bow05RN" 0
		"pr_bow05RN" 13
		0 "|pr_bow05:rig_group" "|__PROPS__" "-s -r "
		0 "|pr_bow05RNfosterParent1|Global_SRT_parentConstraint1" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT" 
		"-s -r "
		2 "|__PROPS__|pr_bow05:rig_group|pr_bow05:Geometries|pr_bow05:rope|pr_bow05:ropeShape" 
		"uvSet[0].uvSetName" " -type \"string\" \"map1\""
		5 4 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.translateY" 
		"pr_bow05RN.placeHolderList[1]" ""
		5 4 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.translateX" 
		"pr_bow05RN.placeHolderList[2]" ""
		5 4 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.translateZ" 
		"pr_bow05RN.placeHolderList[3]" ""
		5 3 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.rotatePivot" 
		"pr_bow05RN.placeHolderList[4]" ""
		5 3 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.rotatePivotTranslate" 
		"pr_bow05RN.placeHolderList[5]" ""
		5 4 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.rotateX" 
		"pr_bow05RN.placeHolderList[6]" ""
		5 4 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.rotateY" 
		"pr_bow05RN.placeHolderList[7]" ""
		5 4 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.rotateZ" 
		"pr_bow05RN.placeHolderList[8]" ""
		5 3 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.rotateOrder" 
		"pr_bow05RN.placeHolderList[9]" ""
		5 3 "pr_bow05RN" "|__PROPS__|pr_bow05:rig_group|pr_bow05:TKRig|pr_bow05:TK_GlobalSRT_Root|pr_bow05:Global_SRT_NeutralPose|pr_bow05:Global_SRT.parentInverseMatrix" 
		"pr_bow05RN.placeHolderList[10]" "";
lockNode -l 1 ;
createNode reference -n "st_YKR412_0380RN";
	setAttr -s 54 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".phl[11]" 0;
	setAttr ".phl[12]" 0;
	setAttr ".phl[13]" 0;
	setAttr ".phl[14]" 0;
	setAttr ".phl[15]" 0;
	setAttr ".phl[16]" 0;
	setAttr ".phl[17]" 0;
	setAttr ".phl[18]" 0;
	setAttr ".phl[19]" 0;
	setAttr ".phl[20]" 0;
	setAttr ".phl[21]" 0;
	setAttr ".phl[22]" 0;
	setAttr ".phl[23]" 0;
	setAttr ".phl[24]" 0;
	setAttr ".phl[25]" 0;
	setAttr ".phl[26]" 0;
	setAttr ".phl[27]" 0;
	setAttr ".phl[28]" 0;
	setAttr ".phl[29]" 0;
	setAttr ".phl[30]" 0;
	setAttr ".phl[31]" 0;
	setAttr ".phl[32]" 0;
	setAttr ".phl[33]" 0;
	setAttr ".phl[34]" 0;
	setAttr ".phl[35]" 0;
	setAttr ".phl[36]" 0;
	setAttr ".phl[37]" 0;
	setAttr ".phl[38]" 0;
	setAttr ".phl[39]" 0;
	setAttr ".phl[40]" 0;
	setAttr ".phl[41]" 0;
	setAttr ".phl[42]" 0;
	setAttr ".phl[43]" 0;
	setAttr ".phl[44]" 0;
	setAttr ".phl[45]" 0;
	setAttr ".phl[46]" 0;
	setAttr ".phl[47]" 0;
	setAttr ".phl[48]" 0;
	setAttr ".phl[49]" 0;
	setAttr ".phl[50]" 0;
	setAttr ".phl[51]" 0;
	setAttr ".phl[52]" 0;
	setAttr ".phl[53]" 0;
	setAttr ".phl[54]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"st_YKR412_0380RN"
		"st_YKR412_0380RN" 0
		"st_YKR412_0380RN" 66
		0 "|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG" "|__SET__" "-s -r "
		0 "|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX" "|__SET__" "-s -r "
		0 "|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD" "|__SET__" "-s -r "
		0 "|st_YKR412_0380RNfosterParent1|YKR412_038_01_GlobalSRT_BG_parentConstraint1" 
		"|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG" "-s -r "
		0 "|st_YKR412_0380RNfosterParent1|YKR412_038_02_GlobalSRT_FX_parentConstraint1" 
		"|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX" "-s -r "
		0 "|st_YKR412_0380RNfosterParent1|YKR412_038_03_GlobalSRT_FD_parentConstraint1" 
		"|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD" "-s -r "
		2 "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG|st_YKR412_0380:YKR412_038_01_GlobalSRT_BGShape" 
		"visibility" " -k 0 0"
		2 "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG|st_YKR412_0380:YKR412_038_01_pPlane1_BG" 
		"overrideDisplayType" " 2"
		2 "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX|st_YKR412_0380:YKR412_038_02_GlobalSRT_FXShape" 
		"visibility" " -k 0 0"
		2 "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX|st_YKR412_0380:YKR412_038_02_pPlane1_FX" 
		"overrideDisplayType" " 2"
		2 "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD|st_YKR412_0380:YKR412_038_03_GlobalSRT_FDShape" 
		"visibility" " -k 0 0"
		2 "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD|st_YKR412_0380:YKR412_038_03_pPlane1_FD" 
		"overrideDisplayType" " 2"
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.translateX" 
		"st_YKR412_0380RN.placeHolderList[1]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.translateY" 
		"st_YKR412_0380RN.placeHolderList[2]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.translateZ" 
		"st_YKR412_0380RN.placeHolderList[3]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.rotateX" 
		"st_YKR412_0380RN.placeHolderList[4]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.rotateY" 
		"st_YKR412_0380RN.placeHolderList[5]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.rotateZ" 
		"st_YKR412_0380RN.placeHolderList[6]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.rotateOrder" 
		"st_YKR412_0380RN.placeHolderList[7]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.parentInverseMatrix" 
		"st_YKR412_0380RN.placeHolderList[8]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.rotatePivot" 
		"st_YKR412_0380RN.placeHolderList[9]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.rotatePivotTranslate" 
		"st_YKR412_0380RN.placeHolderList[10]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.scaleX" 
		"st_YKR412_0380RN.placeHolderList[11]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.scaleY" 
		"st_YKR412_0380RN.placeHolderList[12]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG.scaleZ" 
		"st_YKR412_0380RN.placeHolderList[13]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG|st_YKR412_0380:YKR412_038_01_pPlane1_BG.overrideEnabled" 
		"st_YKR412_0380RN.placeHolderList[14]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG|st_YKR412_0380:YKR412_038_01_pPlane1_BG.visibility" 
		"st_YKR412_0380RN.placeHolderList[15]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG|st_YKR412_0380:YKR412_038_01_pPlane1_BG.rotateX" 
		"st_YKR412_0380RN.placeHolderList[16]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG|st_YKR412_0380:YKR412_038_01_pPlane1_BG.rotateY" 
		"st_YKR412_0380RN.placeHolderList[17]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_01_GlobalSRT_BG|st_YKR412_0380:YKR412_038_01_pPlane1_BG.rotateZ" 
		"st_YKR412_0380RN.placeHolderList[18]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.translateX" 
		"st_YKR412_0380RN.placeHolderList[19]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.translateY" 
		"st_YKR412_0380RN.placeHolderList[20]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.translateZ" 
		"st_YKR412_0380RN.placeHolderList[21]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.rotateX" 
		"st_YKR412_0380RN.placeHolderList[22]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.rotateY" 
		"st_YKR412_0380RN.placeHolderList[23]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.rotateZ" 
		"st_YKR412_0380RN.placeHolderList[24]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.rotateOrder" 
		"st_YKR412_0380RN.placeHolderList[25]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.parentInverseMatrix" 
		"st_YKR412_0380RN.placeHolderList[26]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.rotatePivot" 
		"st_YKR412_0380RN.placeHolderList[27]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.rotatePivotTranslate" 
		"st_YKR412_0380RN.placeHolderList[28]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.scaleX" 
		"st_YKR412_0380RN.placeHolderList[29]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.scaleY" 
		"st_YKR412_0380RN.placeHolderList[30]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX.scaleZ" 
		"st_YKR412_0380RN.placeHolderList[31]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX|st_YKR412_0380:YKR412_038_02_pPlane1_FX.overrideEnabled" 
		"st_YKR412_0380RN.placeHolderList[32]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX|st_YKR412_0380:YKR412_038_02_pPlane1_FX.visibility" 
		"st_YKR412_0380RN.placeHolderList[33]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX|st_YKR412_0380:YKR412_038_02_pPlane1_FX.rotateX" 
		"st_YKR412_0380RN.placeHolderList[34]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX|st_YKR412_0380:YKR412_038_02_pPlane1_FX.rotateY" 
		"st_YKR412_0380RN.placeHolderList[35]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_02_GlobalSRT_FX|st_YKR412_0380:YKR412_038_02_pPlane1_FX.rotateZ" 
		"st_YKR412_0380RN.placeHolderList[36]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.translateX" 
		"st_YKR412_0380RN.placeHolderList[37]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.translateY" 
		"st_YKR412_0380RN.placeHolderList[38]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.translateZ" 
		"st_YKR412_0380RN.placeHolderList[39]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.rotateX" 
		"st_YKR412_0380RN.placeHolderList[40]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.rotateY" 
		"st_YKR412_0380RN.placeHolderList[41]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.rotateZ" 
		"st_YKR412_0380RN.placeHolderList[42]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.rotateOrder" 
		"st_YKR412_0380RN.placeHolderList[43]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.parentInverseMatrix" 
		"st_YKR412_0380RN.placeHolderList[44]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.rotatePivot" 
		"st_YKR412_0380RN.placeHolderList[45]" ""
		5 3 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.rotatePivotTranslate" 
		"st_YKR412_0380RN.placeHolderList[46]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.scaleX" 
		"st_YKR412_0380RN.placeHolderList[47]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.scaleY" 
		"st_YKR412_0380RN.placeHolderList[48]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD.scaleZ" 
		"st_YKR412_0380RN.placeHolderList[49]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD|st_YKR412_0380:YKR412_038_03_pPlane1_FD.overrideEnabled" 
		"st_YKR412_0380RN.placeHolderList[50]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD|st_YKR412_0380:YKR412_038_03_pPlane1_FD.visibility" 
		"st_YKR412_0380RN.placeHolderList[51]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD|st_YKR412_0380:YKR412_038_03_pPlane1_FD.rotateX" 
		"st_YKR412_0380RN.placeHolderList[52]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD|st_YKR412_0380:YKR412_038_03_pPlane1_FD.rotateY" 
		"st_YKR412_0380RN.placeHolderList[53]" ""
		5 4 "st_YKR412_0380RN" "|__SET__|st_YKR412_0380:YKR412_038_03_GlobalSRT_FD|st_YKR412_0380:YKR412_038_03_pPlane1_FD.rotateZ" 
		"st_YKR412_0380RN.placeHolderList[54]" "";
lockNode -l 1 ;
createNode reference -n "ch_wildwRN";
	setAttr -s 204 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".phl[11]" 0;
	setAttr ".phl[12]" 0;
	setAttr ".phl[13]" 0;
	setAttr ".phl[14]" 0;
	setAttr ".phl[15]" 0;
	setAttr ".phl[16]" 0;
	setAttr ".phl[17]" 0;
	setAttr ".phl[18]" 0;
	setAttr ".phl[19]" 0;
	setAttr ".phl[20]" 0;
	setAttr ".phl[21]" 0;
	setAttr ".phl[22]" 0;
	setAttr ".phl[23]" 0;
	setAttr ".phl[24]" 0;
	setAttr ".phl[25]" 0;
	setAttr ".phl[26]" 0;
	setAttr ".phl[27]" 0;
	setAttr ".phl[28]" 0;
	setAttr ".phl[29]" 0;
	setAttr ".phl[30]" 0;
	setAttr ".phl[31]" 0;
	setAttr ".phl[32]" 0;
	setAttr ".phl[33]" 0;
	setAttr ".phl[34]" 0;
	setAttr ".phl[35]" 0;
	setAttr ".phl[36]" 0;
	setAttr ".phl[37]" 0;
	setAttr ".phl[38]" 0;
	setAttr ".phl[39]" 0;
	setAttr ".phl[40]" 0;
	setAttr ".phl[41]" 0;
	setAttr ".phl[42]" 0;
	setAttr ".phl[43]" 0;
	setAttr ".phl[44]" 0;
	setAttr ".phl[45]" 0;
	setAttr ".phl[46]" 0;
	setAttr ".phl[47]" 0;
	setAttr ".phl[48]" 0;
	setAttr ".phl[49]" 0;
	setAttr ".phl[50]" 0;
	setAttr ".phl[51]" 0;
	setAttr ".phl[52]" 0;
	setAttr ".phl[53]" 0;
	setAttr ".phl[54]" 0;
	setAttr ".phl[55]" 0;
	setAttr ".phl[56]" 0;
	setAttr ".phl[57]" 0;
	setAttr ".phl[58]" 0;
	setAttr ".phl[59]" 0;
	setAttr ".phl[60]" 0;
	setAttr ".phl[61]" 0;
	setAttr ".phl[62]" 0;
	setAttr ".phl[63]" 0;
	setAttr ".phl[64]" 0;
	setAttr ".phl[65]" 0;
	setAttr ".phl[66]" 0;
	setAttr ".phl[67]" 0;
	setAttr ".phl[68]" 0;
	setAttr ".phl[69]" 0;
	setAttr ".phl[70]" 0;
	setAttr ".phl[71]" 0;
	setAttr ".phl[72]" 0;
	setAttr ".phl[73]" 0;
	setAttr ".phl[74]" 0;
	setAttr ".phl[75]" 0;
	setAttr ".phl[76]" 0;
	setAttr ".phl[77]" 0;
	setAttr ".phl[78]" 0;
	setAttr ".phl[79]" 0;
	setAttr ".phl[80]" 0;
	setAttr ".phl[81]" 0;
	setAttr ".phl[82]" 0;
	setAttr ".phl[83]" 0;
	setAttr ".phl[84]" 0;
	setAttr ".phl[85]" 0;
	setAttr ".phl[86]" 0;
	setAttr ".phl[87]" 0;
	setAttr ".phl[88]" 0;
	setAttr ".phl[89]" 0;
	setAttr ".phl[90]" 0;
	setAttr ".phl[91]" 0;
	setAttr ".phl[92]" 0;
	setAttr ".phl[93]" 0;
	setAttr ".phl[94]" 0;
	setAttr ".phl[95]" 0;
	setAttr ".phl[96]" 0;
	setAttr ".phl[97]" 0;
	setAttr ".phl[98]" 0;
	setAttr ".phl[99]" 0;
	setAttr ".phl[100]" 0;
	setAttr ".phl[101]" 0;
	setAttr ".phl[102]" 0;
	setAttr ".phl[103]" 0;
	setAttr ".phl[104]" 0;
	setAttr ".phl[105]" 0;
	setAttr ".phl[106]" 0;
	setAttr ".phl[107]" 0;
	setAttr ".phl[108]" 0;
	setAttr ".phl[109]" 0;
	setAttr ".phl[110]" 0;
	setAttr ".phl[111]" 0;
	setAttr ".phl[112]" 0;
	setAttr ".phl[113]" 0;
	setAttr ".phl[114]" 0;
	setAttr ".phl[115]" 0;
	setAttr ".phl[116]" 0;
	setAttr ".phl[117]" 0;
	setAttr ".phl[118]" 0;
	setAttr ".phl[119]" 0;
	setAttr ".phl[120]" 0;
	setAttr ".phl[121]" 0;
	setAttr ".phl[122]" 0;
	setAttr ".phl[123]" 0;
	setAttr ".phl[124]" 0;
	setAttr ".phl[125]" 0;
	setAttr ".phl[126]" 0;
	setAttr ".phl[127]" 0;
	setAttr ".phl[128]" 0;
	setAttr ".phl[129]" 0;
	setAttr ".phl[130]" 0;
	setAttr ".phl[131]" 0;
	setAttr ".phl[132]" 0;
	setAttr ".phl[133]" 0;
	setAttr ".phl[134]" 0;
	setAttr ".phl[135]" 0;
	setAttr ".phl[136]" 0;
	setAttr ".phl[137]" 0;
	setAttr ".phl[138]" 0;
	setAttr ".phl[139]" 0;
	setAttr ".phl[140]" 0;
	setAttr ".phl[141]" 0;
	setAttr ".phl[142]" 0;
	setAttr ".phl[143]" 0;
	setAttr ".phl[144]" 0;
	setAttr ".phl[145]" 0;
	setAttr ".phl[146]" 0;
	setAttr ".phl[147]" 0;
	setAttr ".phl[148]" 0;
	setAttr ".phl[149]" 0;
	setAttr ".phl[150]" 0;
	setAttr ".phl[151]" 0;
	setAttr ".phl[152]" 0;
	setAttr ".phl[153]" 0;
	setAttr ".phl[154]" 0;
	setAttr ".phl[155]" 0;
	setAttr ".phl[156]" 0;
	setAttr ".phl[157]" 0;
	setAttr ".phl[158]" 0;
	setAttr ".phl[159]" 0;
	setAttr ".phl[160]" 0;
	setAttr ".phl[161]" 0;
	setAttr ".phl[162]" 0;
	setAttr ".phl[163]" 0;
	setAttr ".phl[164]" 0;
	setAttr ".phl[165]" 0;
	setAttr ".phl[166]" 0;
	setAttr ".phl[167]" 0;
	setAttr ".phl[168]" 0;
	setAttr ".phl[169]" 0;
	setAttr ".phl[170]" 0;
	setAttr ".phl[171]" 0;
	setAttr ".phl[172]" 0;
	setAttr ".phl[173]" 0;
	setAttr ".phl[174]" 0;
	setAttr ".phl[175]" 0;
	setAttr ".phl[176]" 0;
	setAttr ".phl[177]" 0;
	setAttr ".phl[178]" 0;
	setAttr ".phl[179]" 0;
	setAttr ".phl[180]" 0;
	setAttr ".phl[181]" 0;
	setAttr ".phl[182]" 0;
	setAttr ".phl[183]" 0;
	setAttr ".phl[184]" 0;
	setAttr ".phl[185]" 0;
	setAttr ".phl[186]" 0;
	setAttr ".phl[187]" 0;
	setAttr ".phl[188]" 0;
	setAttr ".phl[189]" 0;
	setAttr ".phl[190]" 0;
	setAttr ".phl[191]" 0;
	setAttr ".phl[192]" 0;
	setAttr ".phl[193]" 0;
	setAttr ".phl[194]" 0;
	setAttr ".phl[195]" 0;
	setAttr ".phl[196]" 0;
	setAttr ".phl[197]" 0;
	setAttr ".phl[198]" 0;
	setAttr ".phl[199]" 0;
	setAttr ".phl[200]" 0;
	setAttr ".phl[201]" 0;
	setAttr ".phl[202]" 0;
	setAttr ".phl[203]" 0;
	setAttr ".phl[204]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"ch_wildwRN"
		"ch_wildwRN" 0
		"ch_wildwRN" 246
		0 "|ch_wildw:rig_group" "|__CHARS__" "-s -r "
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root" 
		"translate" " -type \"double3\" 41.674353444880509 0 90.901027102286605"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root" 
		"translateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root" 
		"translateY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root" 
		"translateZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root" 
		"rotate" " -type \"double3\" 19.602133702085482 0 0"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"visibility" " -av 1"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"translateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"translateY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"translateZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"rotate" " -type \"double3\" 5.2552380328677293 -6.094767052536854 2.7369827415325432"
		
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"rotateY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"rotateZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"scale" " -type \"double3\" 1 1 1"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"scaleX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"scaleY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head" 
		"scaleZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R" 
		"rotate" " -type \"double3\" 53.284216742118389 -24.077446032325096 10.999166985302811"
		
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R" 
		"rotateY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R" 
		"rotateZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R" 
		"rotate" " -type \"double3\" -48.653462344170201 36.782922926670565 -1.1654175724116649"
		
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R" 
		"rotateY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R" 
		"rotateZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L" 
		"rotate" " -type \"double3\" -91.324091385427479 -54.68870549091524 0.81430997312722886"
		
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L" 
		"rotateY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L" 
		"rotateZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L" 
		"rotate" " -type \"double3\" 24.590426208435286 -36.697611686458963 -43.69842945699552"
		
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L" 
		"rotateY" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L" 
		"rotateZ" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L" 
		"rotate" " -type \"double3\" -42.022752623818164 0 0"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R" 
		"rotate" " -type \"double3\" 51.563178137533839 0 0"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R" 
		"rotateX" " -av"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:TKRig|ch_wildw:TK_GlobalSRT_Root|ch_wildw:Global_SRT_NeutralPose|ch_wildw:Global_SRT" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|__CHARS__|ch_wildw:rig_group|ch_wildw:TKRig|ch_wildw:TK_GlobalSRT_Root|ch_wildw:Global_SRT_NeutralPose|ch_wildw:Global_SRT" 
		"rotate" " -type \"double3\" 0 28.179221165127537 0"
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.translateX" 
		"ch_wildwRN.placeHolderList[1]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.translateY" 
		"ch_wildwRN.placeHolderList[2]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.translateZ" 
		"ch_wildwRN.placeHolderList[3]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.rotateX" 
		"ch_wildwRN.placeHolderList[4]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.rotateY" 
		"ch_wildwRN.placeHolderList[5]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.rotateZ" 
		"ch_wildwRN.placeHolderList[6]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.visibility" 
		"ch_wildwRN.placeHolderList[7]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.scaleX" 
		"ch_wildwRN.placeHolderList[8]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.scaleY" 
		"ch_wildwRN.placeHolderList[9]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root.scaleZ" 
		"ch_wildwRN.placeHolderList[10]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.rotateX" 
		"ch_wildwRN.placeHolderList[11]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.rotateY" 
		"ch_wildwRN.placeHolderList[12]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.rotateZ" 
		"ch_wildwRN.placeHolderList[13]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.visibility" 
		"ch_wildwRN.placeHolderList[14]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.translateX" 
		"ch_wildwRN.placeHolderList[15]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.translateY" 
		"ch_wildwRN.placeHolderList[16]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.translateZ" 
		"ch_wildwRN.placeHolderList[17]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.scaleX" 
		"ch_wildwRN.placeHolderList[18]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.scaleY" 
		"ch_wildwRN.placeHolderList[19]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body.scaleZ" 
		"ch_wildwRN.placeHolderList[20]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.rotateX" 
		"ch_wildwRN.placeHolderList[21]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.rotateY" 
		"ch_wildwRN.placeHolderList[22]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.rotateZ" 
		"ch_wildwRN.placeHolderList[23]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.visibility" 
		"ch_wildwRN.placeHolderList[24]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.translateX" 
		"ch_wildwRN.placeHolderList[25]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.translateY" 
		"ch_wildwRN.placeHolderList[26]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.translateZ" 
		"ch_wildwRN.placeHolderList[27]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.scaleX" 
		"ch_wildwRN.placeHolderList[28]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.scaleY" 
		"ch_wildwRN.placeHolderList[29]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest.scaleZ" 
		"ch_wildwRN.placeHolderList[30]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.rotateX" 
		"ch_wildwRN.placeHolderList[31]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.rotateY" 
		"ch_wildwRN.placeHolderList[32]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.rotateZ" 
		"ch_wildwRN.placeHolderList[33]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.visibility" 
		"ch_wildwRN.placeHolderList[34]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.translateX" 
		"ch_wildwRN.placeHolderList[35]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.translateY" 
		"ch_wildwRN.placeHolderList[36]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.translateZ" 
		"ch_wildwRN.placeHolderList[37]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.scaleX" 
		"ch_wildwRN.placeHolderList[38]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.scaleY" 
		"ch_wildwRN.placeHolderList[39]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck.scaleZ" 
		"ch_wildwRN.placeHolderList[40]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.translateX" 
		"ch_wildwRN.placeHolderList[41]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.translateY" 
		"ch_wildwRN.placeHolderList[42]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.translateZ" 
		"ch_wildwRN.placeHolderList[43]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.rotateX" 
		"ch_wildwRN.placeHolderList[44]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.rotateY" 
		"ch_wildwRN.placeHolderList[45]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.rotateZ" 
		"ch_wildwRN.placeHolderList[46]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.scaleX" 
		"ch_wildwRN.placeHolderList[47]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.scaleY" 
		"ch_wildwRN.placeHolderList[48]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.scaleZ" 
		"ch_wildwRN.placeHolderList[49]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_neck|ch_wildw:clnLyW_head.visibility" 
		"ch_wildwRN.placeHolderList[50]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.rotateX" 
		"ch_wildwRN.placeHolderList[51]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.rotateY" 
		"ch_wildwRN.placeHolderList[52]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.rotateZ" 
		"ch_wildwRN.placeHolderList[53]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.visibility" 
		"ch_wildwRN.placeHolderList[54]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.translateX" 
		"ch_wildwRN.placeHolderList[55]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.translateY" 
		"ch_wildwRN.placeHolderList[56]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.translateZ" 
		"ch_wildwRN.placeHolderList[57]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.scaleX" 
		"ch_wildwRN.placeHolderList[58]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.scaleY" 
		"ch_wildwRN.placeHolderList[59]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R.scaleZ" 
		"ch_wildwRN.placeHolderList[60]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.rotateX" 
		"ch_wildwRN.placeHolderList[61]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.rotateY" 
		"ch_wildwRN.placeHolderList[62]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.rotateZ" 
		"ch_wildwRN.placeHolderList[63]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.visibility" 
		"ch_wildwRN.placeHolderList[64]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.translateX" 
		"ch_wildwRN.placeHolderList[65]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.translateY" 
		"ch_wildwRN.placeHolderList[66]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.translateZ" 
		"ch_wildwRN.placeHolderList[67]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.scaleX" 
		"ch_wildwRN.placeHolderList[68]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.scaleY" 
		"ch_wildwRN.placeHolderList[69]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R.scaleZ" 
		"ch_wildwRN.placeHolderList[70]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.translate" 
		"ch_wildwRN.placeHolderList[71]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.translate" 
		"ch_wildwRN.placeHolderList[72]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.translateX" 
		"ch_wildwRN.placeHolderList[73]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.translateY" 
		"ch_wildwRN.placeHolderList[74]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.translateZ" 
		"ch_wildwRN.placeHolderList[75]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotatePivot" 
		"ch_wildwRN.placeHolderList[76]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotatePivot" 
		"ch_wildwRN.placeHolderList[77]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotatePivotTranslate" 
		"ch_wildwRN.placeHolderList[78]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotatePivotTranslate" 
		"ch_wildwRN.placeHolderList[79]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotate" 
		"ch_wildwRN.placeHolderList[80]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotate" 
		"ch_wildwRN.placeHolderList[81]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotateX" 
		"ch_wildwRN.placeHolderList[82]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotateY" 
		"ch_wildwRN.placeHolderList[83]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotateZ" 
		"ch_wildwRN.placeHolderList[84]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotateOrder" 
		"ch_wildwRN.placeHolderList[85]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.rotateOrder" 
		"ch_wildwRN.placeHolderList[86]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.scale" 
		"ch_wildwRN.placeHolderList[87]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.scale" 
		"ch_wildwRN.placeHolderList[88]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.scaleX" 
		"ch_wildwRN.placeHolderList[89]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.scaleY" 
		"ch_wildwRN.placeHolderList[90]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.scaleZ" 
		"ch_wildwRN.placeHolderList[91]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.parentMatrix" 
		"ch_wildwRN.placeHolderList[92]" ""
		5 3 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.parentMatrix" 
		"ch_wildwRN.placeHolderList[93]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_R|ch_wildw:clnLyW_forearm_R|ch_wildw:clnLyW_hand_R.visibility" 
		"ch_wildwRN.placeHolderList[94]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.rotateX" 
		"ch_wildwRN.placeHolderList[95]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.rotateY" 
		"ch_wildwRN.placeHolderList[96]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.rotateZ" 
		"ch_wildwRN.placeHolderList[97]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.visibility" 
		"ch_wildwRN.placeHolderList[98]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.translateX" 
		"ch_wildwRN.placeHolderList[99]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.translateY" 
		"ch_wildwRN.placeHolderList[100]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.translateZ" 
		"ch_wildwRN.placeHolderList[101]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.scaleX" 
		"ch_wildwRN.placeHolderList[102]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.scaleY" 
		"ch_wildwRN.placeHolderList[103]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L.scaleZ" 
		"ch_wildwRN.placeHolderList[104]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.rotateX" 
		"ch_wildwRN.placeHolderList[105]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.rotateY" 
		"ch_wildwRN.placeHolderList[106]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.rotateZ" 
		"ch_wildwRN.placeHolderList[107]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.visibility" 
		"ch_wildwRN.placeHolderList[108]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.translateX" 
		"ch_wildwRN.placeHolderList[109]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.translateY" 
		"ch_wildwRN.placeHolderList[110]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.translateZ" 
		"ch_wildwRN.placeHolderList[111]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.scaleX" 
		"ch_wildwRN.placeHolderList[112]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.scaleY" 
		"ch_wildwRN.placeHolderList[113]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L.scaleZ" 
		"ch_wildwRN.placeHolderList[114]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.rotateX" 
		"ch_wildwRN.placeHolderList[115]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.rotateY" 
		"ch_wildwRN.placeHolderList[116]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.rotateZ" 
		"ch_wildwRN.placeHolderList[117]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.visibility" 
		"ch_wildwRN.placeHolderList[118]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.translateX" 
		"ch_wildwRN.placeHolderList[119]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.translateY" 
		"ch_wildwRN.placeHolderList[120]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.translateZ" 
		"ch_wildwRN.placeHolderList[121]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.scaleX" 
		"ch_wildwRN.placeHolderList[122]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.scaleY" 
		"ch_wildwRN.placeHolderList[123]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_body|ch_wildw:clnLyW_chest|ch_wildw:clnLyW_arm_L|ch_wildw:clnLyW_forearm_L|ch_wildw:clnLyW_hand_L.scaleZ" 
		"ch_wildwRN.placeHolderList[124]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.rotateX" 
		"ch_wildwRN.placeHolderList[125]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.rotateY" 
		"ch_wildwRN.placeHolderList[126]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.rotateZ" 
		"ch_wildwRN.placeHolderList[127]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.visibility" 
		"ch_wildwRN.placeHolderList[128]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.translateX" 
		"ch_wildwRN.placeHolderList[129]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.translateY" 
		"ch_wildwRN.placeHolderList[130]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.translateZ" 
		"ch_wildwRN.placeHolderList[131]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.scaleX" 
		"ch_wildwRN.placeHolderList[132]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.scaleY" 
		"ch_wildwRN.placeHolderList[133]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_01.scaleZ" 
		"ch_wildwRN.placeHolderList[134]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.rotateX" 
		"ch_wildwRN.placeHolderList[135]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.rotateY" 
		"ch_wildwRN.placeHolderList[136]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.rotateZ" 
		"ch_wildwRN.placeHolderList[137]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.visibility" 
		"ch_wildwRN.placeHolderList[138]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.translateX" 
		"ch_wildwRN.placeHolderList[139]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.translateY" 
		"ch_wildwRN.placeHolderList[140]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.translateZ" 
		"ch_wildwRN.placeHolderList[141]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.scaleX" 
		"ch_wildwRN.placeHolderList[142]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.scaleY" 
		"ch_wildwRN.placeHolderList[143]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_cloth_02.scaleZ" 
		"ch_wildwRN.placeHolderList[144]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.rotateX" 
		"ch_wildwRN.placeHolderList[145]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.rotateY" 
		"ch_wildwRN.placeHolderList[146]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.rotateZ" 
		"ch_wildwRN.placeHolderList[147]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.visibility" 
		"ch_wildwRN.placeHolderList[148]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.translateX" 
		"ch_wildwRN.placeHolderList[149]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.translateY" 
		"ch_wildwRN.placeHolderList[150]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.translateZ" 
		"ch_wildwRN.placeHolderList[151]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.scaleX" 
		"ch_wildwRN.placeHolderList[152]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.scaleY" 
		"ch_wildwRN.placeHolderList[153]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L.scaleZ" 
		"ch_wildwRN.placeHolderList[154]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.rotateX" 
		"ch_wildwRN.placeHolderList[155]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.rotateY" 
		"ch_wildwRN.placeHolderList[156]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.rotateZ" 
		"ch_wildwRN.placeHolderList[157]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.visibility" 
		"ch_wildwRN.placeHolderList[158]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.translateX" 
		"ch_wildwRN.placeHolderList[159]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.translateY" 
		"ch_wildwRN.placeHolderList[160]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.translateZ" 
		"ch_wildwRN.placeHolderList[161]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.scaleX" 
		"ch_wildwRN.placeHolderList[162]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.scaleY" 
		"ch_wildwRN.placeHolderList[163]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L.scaleZ" 
		"ch_wildwRN.placeHolderList[164]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.rotateX" 
		"ch_wildwRN.placeHolderList[165]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.rotateY" 
		"ch_wildwRN.placeHolderList[166]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.rotateZ" 
		"ch_wildwRN.placeHolderList[167]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.visibility" 
		"ch_wildwRN.placeHolderList[168]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.translateX" 
		"ch_wildwRN.placeHolderList[169]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.translateY" 
		"ch_wildwRN.placeHolderList[170]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.translateZ" 
		"ch_wildwRN.placeHolderList[171]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.scaleX" 
		"ch_wildwRN.placeHolderList[172]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.scaleY" 
		"ch_wildwRN.placeHolderList[173]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_L|ch_wildw:clnLyW_foreleg_L|ch_wildw:clnLyW_foot_L.scaleZ" 
		"ch_wildwRN.placeHolderList[174]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.rotateX" 
		"ch_wildwRN.placeHolderList[175]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.rotateY" 
		"ch_wildwRN.placeHolderList[176]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.rotateZ" 
		"ch_wildwRN.placeHolderList[177]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.visibility" 
		"ch_wildwRN.placeHolderList[178]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.translateX" 
		"ch_wildwRN.placeHolderList[179]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.translateY" 
		"ch_wildwRN.placeHolderList[180]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.translateZ" 
		"ch_wildwRN.placeHolderList[181]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.scaleX" 
		"ch_wildwRN.placeHolderList[182]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.scaleY" 
		"ch_wildwRN.placeHolderList[183]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R.scaleZ" 
		"ch_wildwRN.placeHolderList[184]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.rotateX" 
		"ch_wildwRN.placeHolderList[185]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.rotateY" 
		"ch_wildwRN.placeHolderList[186]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.rotateZ" 
		"ch_wildwRN.placeHolderList[187]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.visibility" 
		"ch_wildwRN.placeHolderList[188]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.translateX" 
		"ch_wildwRN.placeHolderList[189]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.translateY" 
		"ch_wildwRN.placeHolderList[190]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.translateZ" 
		"ch_wildwRN.placeHolderList[191]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.scaleX" 
		"ch_wildwRN.placeHolderList[192]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.scaleY" 
		"ch_wildwRN.placeHolderList[193]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R.scaleZ" 
		"ch_wildwRN.placeHolderList[194]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.rotateX" 
		"ch_wildwRN.placeHolderList[195]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.rotateY" 
		"ch_wildwRN.placeHolderList[196]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.rotateZ" 
		"ch_wildwRN.placeHolderList[197]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.visibility" 
		"ch_wildwRN.placeHolderList[198]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.translateX" 
		"ch_wildwRN.placeHolderList[199]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.translateY" 
		"ch_wildwRN.placeHolderList[200]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.translateZ" 
		"ch_wildwRN.placeHolderList[201]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.scaleX" 
		"ch_wildwRN.placeHolderList[202]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.scaleY" 
		"ch_wildwRN.placeHolderList[203]" ""
		5 4 "ch_wildwRN" "|__CHARS__|ch_wildw:rig_group|ch_wildw:Geometries|ch_wildw:clnLyW_root|ch_wildw:clnLyW_leg_R|ch_wildw:clnLyW_foreleg_R|ch_wildw:clnLyW_foot_R.scaleZ" 
		"ch_wildwRN.placeHolderList[204]" "";
lockNode -l 1 ;
createNode sequencer -n "sequencer1";
	addAttr -ci true -sn "project" -ln "project" -dt "string";
	addAttr -ci true -sn "episode" -ln "episode" -dt "string";
	addAttr -ci true -sn "sequence" -ln "sequence" -dt "string";
	setAttr ".mnf" 101;
	setAttr ".mxf" 147;
	setAttr -l on -k on ".project" -type "string" "yak";
	setAttr -l on -k on ".episode" -type "string" "412";
	setAttr -l on -k on ".sequence" -type "string" "sequencer1";
createNode shot -n "sh038";
	setAttr -l on ".sf" 101;
	setAttr -l on ".ef" 147;
	setAttr -l on ".ssf" 101;
	setAttr ".sn" -type "string" "sh038";
	setAttr ".wres" 1024;
	setAttr ".ca" 1;
createNode reference -n "SH038_CAMRN";
	setAttr -s 25 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".phl[11]" 0;
	setAttr ".phl[12]" 0;
	setAttr ".phl[13]" 0;
	setAttr ".phl[14]" 0;
	setAttr ".phl[15]" 0;
	setAttr ".phl[16]" 0;
	setAttr ".phl[17]" 0;
	setAttr ".phl[18]" 0;
	setAttr ".phl[19]" 0;
	setAttr ".phl[20]" 0;
	setAttr ".phl[21]" 0;
	setAttr ".phl[22]" 0;
	setAttr ".phl[23]" 0;
	setAttr ".phl[24]" 0;
	setAttr ".phl[25]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"SH038_CAMRN"
		"SH038_CAMRN" 0
		"SH038_CAMRN" 36
		0 "|SH038_CAM:camera_rig" "|__CAMERA__" "-s -r "
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global" "translate" 
		" -type \"double3\" 0 78.952261996173391 1.3891098167432907"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global" "rotate" " -type \"double3\" 6.8564358991690781 0 0"
		
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global" "controllersSize" 
		" -cb 1 4.5"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder" 
		"translate" " -type \"double3\" 0 0 170.84511554455696"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder" 
		"PROJ_focal" " -k 1 38"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraPROJ|SH038_CAM:cameraPROJShape" 
		"cameraAperture" " -type \"double2\" 2.2275590551181104 0.66377952755905523"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller|SH038_CAM:cameraHD|SH038_CAM:cameraHDShape" 
		"displaySafeAction" " 0"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller|SH038_CAM:cameraHD|SH038_CAM:cameraHDShape" 
		"displaySafeTitle" " 0"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim" 
		"translate" " -type \"double3\" 0 0 -300"
		2 "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:rig_extra|SH038_CAM:plateCtrl" 
		"visibility" " 0"
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global.controllersSize" 
		"SH038_CAMRN.placeHolderList[1]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global.controllersSize" 
		"SH038_CAMRN.placeHolderList[2]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global.controllersSize" 
		"SH038_CAMRN.placeHolderList[3]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global.controllersSize" 
		"SH038_CAMRN.placeHolderList[4]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global.controllersSize" 
		"SH038_CAMRN.placeHolderList[5]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global.controllersSize" 
		"SH038_CAMRN.placeHolderList[6]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder.near" 
		"SH038_CAMRN.placeHolderList[7]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder.focalCorrection" 
		"SH038_CAMRN.placeHolderList[8]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder.translate" 
		"SH038_CAMRN.placeHolderList[9]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder.rotatePivot" 
		"SH038_CAMRN.placeHolderList[10]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder.rotatePivotTranslate" 
		"SH038_CAMRN.placeHolderList[11]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder.parentMatrix" 
		"SH038_CAMRN.placeHolderList[12]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller.opacity" 
		"SH038_CAMRN.placeHolderList[13]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller.show" 
		"SH038_CAMRN.placeHolderList[14]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller|SH038_CAM:cameraHD|SH038_CAM:cameraHDShape.horizontalFilmOffset" 
		"SH038_CAMRN.placeHolderList[15]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller|SH038_CAM:cameraHD|SH038_CAM:cameraHDShape.verticalFilmOffset" 
		"SH038_CAMRN.placeHolderList[16]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller|SH038_CAM:cameraHD|SH038_CAM:cameraHDShape.message" 
		"SH038_CAMRN.placeHolderList[17]" ""
		5 4 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:cameras_holder|SH038_CAM:cameraHD_controller|SH038_CAM:cameraHD|SH038_CAM:cameraHDShape.imagePlane" 
		"SH038_CAMRN.placeHolderList[18]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim.rotate" 
		"SH038_CAMRN.placeHolderList[19]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim.scale" 
		"SH038_CAMRN.placeHolderList[20]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim.translate" 
		"SH038_CAMRN.placeHolderList[21]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim.rotatePivot" 
		"SH038_CAMRN.placeHolderList[22]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim.rotatePivotTranslate" 
		"SH038_CAMRN.placeHolderList[23]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim.parentMatrix" 
		"SH038_CAMRN.placeHolderList[24]" ""
		5 3 "SH038_CAMRN" "|__CAMERA__|SH038_CAM:camera_rig|SH038_CAM:camera_global|SH038_CAM:camera_aim.rotateOrder" 
		"SH038_CAMRN.placeHolderList[25]" "";
lockNode -l 1 ;
createNode animCurveTU -n "sh038ImagePlaneShape_frameExtension";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 1 114 2 131 3 143 4;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode audio -n "sh038Audio";
	setAttr ".o" 101;
	setAttr ".ef" 148;
	setAttr -l on ".ss";
	setAttr -l on ".se" 47;
	setAttr ".f" -type "string" "$PROD_SERVER/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR412/animatic/wav/YKR412_038.wav";
createNode cluster -n "SH038_CAM:plateCtrl3Clustering";
	setAttr -s 4 ".ip";
	setAttr -s 4 ".og";
	setAttr ".rel" yes;
	setAttr -s 4 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak1";
createNode tweak -n "tweak2";
createNode tweak -n "tweak3";
createNode tweak -n "tweak4";
createNode objectSet -n "SH038_CAM:plateCtrl3ClusteringSet";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 4 ".gn";
createNode groupId -n "SH038_CAM:plateCtrl3ClusteringGroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl3ClusteringGroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl3ClusteringGroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl3ClusteringGroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl3ClusteringGroupId2";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl3ClusteringGroupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl3ClusteringGroupId3";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl3ClusteringGroupParts3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId5";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts5";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet2";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId6";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts6";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet3";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId7";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts7";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet4";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId8";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts8";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode addDoubleLinear -n "SH038_CAM:plateCtrl3_zCoord";
createNode plusMinusAverage -n "SH038_CAM:plateCtrl3_zDistance";
	setAttr ".op" 2;
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode multDoubleLinear -n "SH038_CAM:plateCtrl3_factor";
	setAttr ".i2" 0.001;
createNode unitConversion -n "unitConversion1";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion2";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion3";
	setAttr ".cf" 0.017453292519943295;
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleX";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleY";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleZ";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleX";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleY";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleZ";
createNode cluster -n "SH038_CAM:plateCtrl2Clustering";
	setAttr -s 4 ".ip";
	setAttr -s 4 ".og";
	setAttr ".rel" yes;
	setAttr -s 4 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -100 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -100 1;
	setAttr ".gm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -100 1;
	setAttr ".gm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -100 1;
createNode tweak -n "tweak5";
createNode tweak -n "tweak6";
createNode tweak -n "tweak7";
createNode tweak -n "tweak8";
createNode objectSet -n "SH038_CAM:plateCtrl2ClusteringSet";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 4 ".gn";
createNode groupId -n "SH038_CAM:plateCtrl2ClusteringGroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl2ClusteringGroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl2ClusteringGroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl2ClusteringGroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl2ClusteringGroupId2";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl2ClusteringGroupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl2ClusteringGroupId3";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl2ClusteringGroupParts3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet5";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId13";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts13";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet6";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId14";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts14";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet7";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId15";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts15";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet8";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId16";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts16";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode addDoubleLinear -n "SH038_CAM:plateCtrl2_zCoord";
createNode plusMinusAverage -n "SH038_CAM:plateCtrl2_zDistance";
	setAttr ".op" 2;
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode multDoubleLinear -n "SH038_CAM:plateCtrl2_factor";
	setAttr ".i2" 0.001;
createNode unitConversion -n "unitConversion4";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion6";
	setAttr ".cf" 0.017453292519943295;
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleX";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleY";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleZ";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleX";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleY";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleZ";
createNode cluster -n "SH038_CAM:plateCtrl1Clustering";
	setAttr -s 4 ".ip";
	setAttr -s 4 ".og";
	setAttr ".rel" yes;
	setAttr -s 4 ".gm";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -200 1;
	setAttr ".gm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -200 1;
	setAttr ".gm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -200 1;
	setAttr ".gm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -200 1;
createNode tweak -n "tweak9";
createNode tweak -n "tweak10";
createNode tweak -n "tweak11";
createNode tweak -n "tweak12";
createNode objectSet -n "SH038_CAM:plateCtrl1ClusteringSet";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
	setAttr ".vo" yes;
	setAttr -s 4 ".gn";
createNode groupId -n "SH038_CAM:plateCtrl1ClusteringGroupId";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl1ClusteringGroupParts";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl1ClusteringGroupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl1ClusteringGroupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl1ClusteringGroupId2";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl1ClusteringGroupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode groupId -n "SH038_CAM:plateCtrl1ClusteringGroupId3";
	setAttr ".ihi" 0;
createNode groupParts -n "SH038_CAM:plateCtrl1ClusteringGroupParts3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet9";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId21";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts21";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet10";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId22";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts22";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet11";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId23";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts23";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode objectSet -n "tweakSet12";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId24";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts24";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode addDoubleLinear -n "SH038_CAM:plateCtrl1_zCoord";
createNode plusMinusAverage -n "SH038_CAM:plateCtrl1_zDistance";
	setAttr ".op" 2;
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode multDoubleLinear -n "SH038_CAM:plateCtrl1_factor";
	setAttr ".i2" 0.001;
createNode unitConversion -n "unitConversion7";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion8";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion9";
	setAttr ".cf" 0.017453292519943295;
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleX";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleY";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleZ";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleX";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleY";
createNode multDoubleLinear -n "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleZ";
createNode multiplyDivide -n "imagePlaneAlphaFactor";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 100 1 1 ;
createNode addDoubleLinear -n "depthCorrection";
	setAttr ".i2" 0.01;
createNode animCurveTA -n "clnLyW_root_rotateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 0 129 19.602133702085482 147 19.602133702085482;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTA -n "clnLyW_root_rotateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 0 129 0 147 0;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTA -n "clnLyW_root_rotateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 0 129 0 147 0;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTA -n "clnLyW_body_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_body_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_body_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_chest_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 -5.8173979798242232 129 -5.8173979798242232;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_chest_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_chest_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_arm_L_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -91.324091385427479;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_arm_L_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -54.68870549091524;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_arm_L_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 -33.375262557807403 129 0.81430997312722886;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_forearm_L_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 24.590426208435286;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_forearm_L_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -36.697611686458963;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_forearm_L_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -43.69842945699552;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_hand_L_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_hand_L_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_hand_L_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_arm_R_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 53.284216742118389;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_arm_R_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -24.077446032325096;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_arm_R_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 38.770966269253378 129 10.999166985302811;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_forearm_R_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -48.653462344170201;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_forearm_R_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 36.782922926670565;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_forearm_R_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -1.1654175724116649;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_hand_R_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_hand_R_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_hand_R_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_neck_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_neck_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_neck_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_head_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 -5.1101066354946347 114 44.944477430154663
		 119 8.4933923189270715 129 5.2552380328677293;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTA -n "clnLyW_head_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 0 114 -78.458664602307493 119 51.928777985850466
		 129 -6.094767052536854;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTA -n "clnLyW_head_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 0 114 -44.859857757296986 119 10.00151427064028
		 129 2.7369827415325432;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTA -n "clnLyW_cloth_01_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_cloth_01_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_cloth_01_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_cloth_02_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_cloth_02_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_cloth_02_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_leg_L_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 -42.022752623818164;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_leg_L_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_leg_L_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foreleg_L_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foreleg_L_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foreleg_L_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foot_L_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foot_L_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foot_L_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_leg_R_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_leg_R_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_leg_R_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foreleg_R_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 51.563178137533839;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foreleg_R_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foreleg_R_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foot_R_rotateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foot_R_rotateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTA -n "clnLyW_foot_R_rotateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_root_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 1 129 1 147 1;
	setAttr -s 3 ".kit[2]"  2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTL -n "clnLyW_root_translateX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 0 129 0 147 41.674353444880509;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTL -n "clnLyW_root_translateY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 0 129 0 147 -7.1054273576010019e-015;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTL -n "clnLyW_root_translateZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 0 129 0 147 90.901027102286605;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTU -n "clnLyW_root_scaleX";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 1 129 1 147 1;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTU -n "clnLyW_root_scaleY";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 1 129 1 147 1;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTU -n "clnLyW_root_scaleZ";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  101 1 129 1 147 1;
	setAttr -s 3 ".kit[0:2]"  18 9 2;
	setAttr -s 3 ".kot[0:2]"  5 9 2;
createNode animCurveTU -n "clnLyW_body_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_body_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_body_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_body_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_body_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_body_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_body_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_chest_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_chest_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_chest_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_chest_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_chest_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_chest_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_chest_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_neck_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_neck_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_neck_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_neck_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_neck_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_neck_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_neck_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_head_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 1 114 1 119 1 129 1;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTL -n "clnLyW_head_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 0 114 0 119 0 129 0;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTL -n "clnLyW_head_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 0 114 0 119 0 129 0;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTL -n "clnLyW_head_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 0 114 0 119 0 129 0;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTU -n "clnLyW_head_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 1 114 1 119 1 129 1;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTU -n "clnLyW_head_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 1 114 1 119 1 129 1;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTU -n "clnLyW_head_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  101 1 114 1 119 1 129 1;
	setAttr -s 4 ".kot[0:3]"  5 5 5 5;
createNode animCurveTU -n "clnLyW_arm_R_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_arm_R_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_arm_R_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_arm_R_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_arm_R_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_arm_R_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_arm_R_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_R_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_forearm_R_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_forearm_R_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_forearm_R_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_R_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_R_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_R_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_R_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_hand_R_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_hand_R_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_hand_R_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_R_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_R_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_R_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_arm_L_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_arm_L_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_arm_L_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_arm_L_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_arm_L_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_arm_L_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_arm_L_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_L_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_forearm_L_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_forearm_L_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_forearm_L_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_L_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_L_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_forearm_L_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_L_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_hand_L_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_hand_L_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_hand_L_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_L_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_L_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_hand_L_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_01_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_cloth_01_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_cloth_01_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_cloth_01_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_01_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_01_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_01_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_02_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_cloth_02_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_cloth_02_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_cloth_02_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_02_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_02_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_cloth_02_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_L_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_leg_L_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_leg_L_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_leg_L_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_L_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_L_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_L_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_L_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foreleg_L_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foreleg_L_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foreleg_L_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_L_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_L_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_L_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_L_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foot_L_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foot_L_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foot_L_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_L_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_L_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_L_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_R_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_leg_R_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_leg_R_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_leg_R_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_R_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_R_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_leg_R_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_R_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foreleg_R_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foreleg_R_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foreleg_R_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_R_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_R_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foreleg_R_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_R_visibility";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foot_R_translateX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foot_R_translateY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "clnLyW_foot_R_translateZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 0 129 0;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_R_scaleX";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_R_scaleY";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "clnLyW_foot_R_scaleZ";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  101 1 129 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode hyperGraphInfo -n "nodeEditorPanel1Info";
createNode hyperView -n "hyperView1";
	setAttr ".dag" no;
createNode hyperLayout -n "hyperLayout1";
	setAttr ".ihi" 0;
	setAttr -s 342 ".hyp";
	setAttr ".hyp[0].x" 515.71429443359375;
	setAttr ".hyp[0].y" -177.14285278320312;
	setAttr ".hyp[0].nvs" 1920;
	setAttr ".hyp[1].x" 241.42857360839844;
	setAttr ".hyp[1].y" -180;
	setAttr ".hyp[1].nvs" 1920;
	setAttr ".hyp[2].x" 1.4285714626312256;
	setAttr ".hyp[2].y" -180;
	setAttr ".hyp[2].nvs" 1920;
	setAttr ".hyp[3].x" 515.71429443359375;
	setAttr ".hyp[3].y" -72.857139587402344;
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
	setAttr ".hyp[21].nvs" 1920;
	setAttr ".hyp[22].nvs" 1920;
	setAttr ".hyp[23].nvs" 1920;
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
	setAttr ".hyp[39].nvs" 1920;
	setAttr ".hyp[40].nvs" 1920;
	setAttr ".hyp[41].nvs" 1920;
	setAttr ".hyp[42].nvs" 1920;
	setAttr ".hyp[43].nvs" 1920;
	setAttr ".hyp[44].nvs" 1920;
	setAttr ".hyp[45].nvs" 1920;
	setAttr ".hyp[46].nvs" 1920;
	setAttr ".hyp[47].nvs" 1920;
	setAttr ".hyp[48].nvs" 1920;
	setAttr ".hyp[49].nvs" 1920;
	setAttr ".hyp[50].nvs" 1920;
	setAttr ".hyp[51].nvs" 1920;
	setAttr ".hyp[52].nvs" 1920;
	setAttr ".hyp[53].nvs" 1920;
	setAttr ".hyp[54].nvs" 1920;
	setAttr ".hyp[55].nvs" 1920;
	setAttr ".hyp[56].nvs" 1920;
	setAttr ".hyp[57].nvs" 1920;
	setAttr ".hyp[58].nvs" 1920;
	setAttr ".hyp[59].nvs" 1920;
	setAttr ".hyp[60].nvs" 1920;
	setAttr ".hyp[61].nvs" 1920;
	setAttr ".hyp[62].nvs" 1920;
	setAttr ".hyp[63].nvs" 1920;
	setAttr ".hyp[64].nvs" 1920;
	setAttr ".hyp[65].nvs" 1920;
	setAttr ".hyp[66].nvs" 1920;
	setAttr ".hyp[67].nvs" 1920;
	setAttr ".hyp[68].nvs" 1920;
	setAttr ".hyp[69].nvs" 1920;
	setAttr ".hyp[70].nvs" 1920;
	setAttr ".hyp[71].nvs" 1920;
	setAttr ".hyp[72].nvs" 1920;
	setAttr ".hyp[73].nvs" 1920;
	setAttr ".hyp[74].nvs" 1920;
	setAttr ".hyp[75].nvs" 1920;
	setAttr ".hyp[76].nvs" 1920;
	setAttr ".hyp[77].nvs" 1920;
	setAttr ".hyp[78].nvs" 1920;
	setAttr ".hyp[79].nvs" 1920;
	setAttr ".hyp[80].nvs" 1920;
	setAttr ".hyp[81].nvs" 1920;
	setAttr ".hyp[82].nvs" 1920;
	setAttr ".hyp[83].nvs" 1920;
	setAttr ".hyp[84].nvs" 1920;
	setAttr ".hyp[85].nvs" 1920;
	setAttr ".hyp[86].nvs" 1920;
	setAttr ".hyp[87].nvs" 1920;
	setAttr ".hyp[88].nvs" 1920;
	setAttr ".hyp[89].nvs" 1920;
	setAttr ".hyp[90].nvs" 1920;
	setAttr ".hyp[91].nvs" 1920;
	setAttr ".hyp[92].nvs" 1920;
	setAttr ".hyp[93].nvs" 1920;
	setAttr ".hyp[94].nvs" 1920;
	setAttr ".hyp[95].nvs" 1920;
	setAttr ".hyp[96].nvs" 1920;
	setAttr ".hyp[97].nvs" 1920;
	setAttr ".hyp[98].nvs" 1920;
	setAttr ".hyp[99].nvs" 1920;
	setAttr ".hyp[100].nvs" 1920;
	setAttr ".hyp[101].nvs" 1920;
	setAttr ".hyp[102].nvs" 1920;
	setAttr ".hyp[103].nvs" 1920;
	setAttr ".hyp[104].nvs" 1920;
	setAttr ".hyp[105].nvs" 1920;
	setAttr ".hyp[106].nvs" 1920;
	setAttr ".hyp[107].nvs" 1920;
	setAttr ".hyp[108].nvs" 1920;
	setAttr ".hyp[109].nvs" 1920;
	setAttr ".hyp[110].nvs" 1920;
	setAttr ".hyp[111].nvs" 1920;
	setAttr ".hyp[112].nvs" 1920;
	setAttr ".hyp[113].nvs" 1920;
	setAttr ".hyp[114].nvs" 1920;
	setAttr ".hyp[115].nvs" 1920;
	setAttr ".hyp[116].nvs" 1920;
	setAttr ".hyp[117].nvs" 1920;
	setAttr ".hyp[118].nvs" 1920;
	setAttr ".hyp[119].nvs" 1920;
	setAttr ".hyp[120].nvs" 1920;
	setAttr ".hyp[121].nvs" 1920;
	setAttr ".hyp[122].nvs" 1920;
	setAttr ".hyp[123].nvs" 1920;
	setAttr ".hyp[124].nvs" 1920;
	setAttr ".hyp[125].nvs" 1920;
	setAttr ".hyp[126].nvs" 1920;
	setAttr ".hyp[127].nvs" 1920;
	setAttr ".hyp[128].nvs" 1920;
	setAttr ".hyp[129].nvs" 1920;
	setAttr ".hyp[130].nvs" 1920;
	setAttr ".hyp[131].nvs" 1920;
	setAttr ".hyp[132].nvs" 1920;
	setAttr ".hyp[133].nvs" 1920;
	setAttr ".hyp[134].nvs" 1920;
	setAttr ".hyp[135].nvs" 1920;
	setAttr ".hyp[136].nvs" 1920;
	setAttr ".hyp[137].nvs" 1920;
	setAttr ".hyp[138].nvs" 1920;
	setAttr ".hyp[139].nvs" 1920;
	setAttr ".hyp[140].nvs" 1920;
	setAttr ".hyp[141].nvs" 1920;
	setAttr ".hyp[142].nvs" 1920;
	setAttr ".hyp[143].nvs" 1920;
	setAttr ".hyp[144].nvs" 1920;
	setAttr ".hyp[145].nvs" 1920;
	setAttr ".hyp[146].nvs" 1920;
	setAttr ".hyp[147].nvs" 1920;
	setAttr ".hyp[148].nvs" 1920;
	setAttr ".hyp[149].nvs" 1920;
	setAttr ".hyp[150].nvs" 1920;
	setAttr ".hyp[151].nvs" 1920;
	setAttr ".hyp[152].nvs" 1920;
	setAttr ".hyp[153].nvs" 1920;
	setAttr ".hyp[154].nvs" 1920;
	setAttr ".hyp[155].nvs" 1920;
	setAttr ".hyp[156].nvs" 1920;
	setAttr ".hyp[157].nvs" 1920;
	setAttr ".hyp[158].nvs" 1920;
	setAttr ".hyp[159].nvs" 1920;
	setAttr ".hyp[160].nvs" 1920;
	setAttr ".hyp[161].nvs" 1920;
	setAttr ".hyp[162].nvs" 1920;
	setAttr ".hyp[163].nvs" 1920;
	setAttr ".hyp[164].nvs" 1920;
	setAttr ".hyp[165].nvs" 1920;
	setAttr ".hyp[166].nvs" 1920;
	setAttr ".hyp[167].nvs" 1920;
	setAttr ".hyp[168].nvs" 1920;
	setAttr ".hyp[169].nvs" 1920;
	setAttr ".hyp[170].nvs" 1920;
	setAttr ".hyp[171].nvs" 1920;
	setAttr ".hyp[172].nvs" 1920;
	setAttr ".hyp[173].nvs" 1920;
	setAttr ".hyp[174].nvs" 1920;
	setAttr ".hyp[175].nvs" 1920;
	setAttr ".hyp[176].nvs" 1920;
	setAttr ".hyp[177].nvs" 1920;
	setAttr ".hyp[178].nvs" 1920;
	setAttr ".hyp[179].nvs" 1920;
	setAttr ".hyp[180].nvs" 1920;
	setAttr ".hyp[181].nvs" 1920;
	setAttr ".hyp[182].nvs" 1920;
	setAttr ".hyp[183].nvs" 1920;
	setAttr ".hyp[184].nvs" 1920;
	setAttr ".hyp[185].nvs" 1920;
	setAttr ".hyp[186].nvs" 1920;
	setAttr ".hyp[187].nvs" 1920;
	setAttr ".hyp[188].nvs" 1920;
	setAttr ".hyp[189].nvs" 1920;
	setAttr ".hyp[190].nvs" 1920;
	setAttr ".hyp[191].nvs" 1920;
	setAttr ".hyp[192].nvs" 1920;
	setAttr ".hyp[193].nvs" 1920;
	setAttr ".hyp[194].nvs" 1920;
	setAttr ".hyp[195].nvs" 1920;
	setAttr ".hyp[196].nvs" 1920;
	setAttr ".hyp[197].nvs" 1920;
	setAttr ".hyp[198].nvs" 1920;
	setAttr ".hyp[199].nvs" 1920;
	setAttr ".hyp[200].nvs" 1920;
	setAttr ".hyp[201].nvs" 1920;
	setAttr ".hyp[202].nvs" 1920;
	setAttr ".hyp[203].nvs" 1920;
	setAttr ".hyp[204].nvs" 1920;
	setAttr ".hyp[205].nvs" 1920;
	setAttr ".hyp[206].nvs" 1920;
	setAttr ".hyp[207].nvs" 1920;
	setAttr ".hyp[208].nvs" 1920;
	setAttr ".hyp[209].nvs" 1920;
	setAttr ".hyp[210].nvs" 1920;
	setAttr ".hyp[211].nvs" 1920;
	setAttr ".hyp[212].nvs" 1920;
	setAttr ".hyp[213].nvs" 1920;
	setAttr ".hyp[214].nvs" 1920;
	setAttr ".hyp[215].nvs" 1920;
	setAttr ".hyp[216].nvs" 1920;
	setAttr ".hyp[217].nvs" 1920;
	setAttr ".hyp[218].nvs" 1920;
	setAttr ".hyp[219].nvs" 1920;
	setAttr ".hyp[220].nvs" 1920;
	setAttr ".hyp[221].nvs" 1920;
	setAttr ".hyp[222].nvs" 1920;
	setAttr ".hyp[223].nvs" 1920;
	setAttr ".hyp[224].nvs" 1920;
	setAttr ".hyp[225].nvs" 1920;
	setAttr ".hyp[226].nvs" 1920;
	setAttr ".hyp[227].nvs" 1920;
	setAttr ".hyp[228].nvs" 1920;
	setAttr ".hyp[229].nvs" 1920;
	setAttr ".hyp[230].nvs" 1920;
	setAttr ".hyp[231].nvs" 1920;
	setAttr ".hyp[232].nvs" 1920;
	setAttr ".hyp[233].nvs" 1920;
	setAttr ".hyp[234].nvs" 1920;
	setAttr ".hyp[235].nvs" 1920;
	setAttr ".hyp[236].nvs" 1920;
	setAttr ".hyp[237].nvs" 1920;
	setAttr ".hyp[238].nvs" 1920;
	setAttr ".hyp[239].nvs" 1920;
	setAttr ".hyp[240].nvs" 1920;
	setAttr ".hyp[241].nvs" 1920;
	setAttr ".hyp[242].nvs" 1920;
	setAttr ".hyp[243].nvs" 1920;
	setAttr ".hyp[244].nvs" 1920;
	setAttr ".hyp[245].nvs" 1920;
	setAttr ".hyp[246].nvs" 1920;
	setAttr ".hyp[247].nvs" 1920;
	setAttr ".hyp[248].nvs" 1920;
	setAttr ".hyp[249].nvs" 1920;
	setAttr ".hyp[250].nvs" 1920;
	setAttr ".hyp[251].nvs" 1920;
	setAttr ".hyp[252].nvs" 1920;
	setAttr ".hyp[253].nvs" 1920;
	setAttr ".hyp[254].nvs" 1920;
	setAttr ".hyp[255].nvs" 1920;
	setAttr ".hyp[256].nvs" 1920;
	setAttr ".hyp[257].nvs" 1920;
	setAttr ".hyp[258].nvs" 1920;
	setAttr ".hyp[259].nvs" 1920;
	setAttr ".hyp[260].nvs" 1920;
	setAttr ".hyp[261].nvs" 1920;
	setAttr ".hyp[262].nvs" 1920;
	setAttr ".hyp[263].nvs" 1920;
	setAttr ".hyp[264].nvs" 1920;
	setAttr ".hyp[265].nvs" 1920;
	setAttr ".hyp[266].nvs" 1920;
	setAttr ".hyp[267].nvs" 1920;
	setAttr ".hyp[268].nvs" 1920;
	setAttr ".hyp[269].nvs" 1920;
	setAttr ".hyp[270].nvs" 1920;
	setAttr ".hyp[271].nvs" 1920;
	setAttr ".hyp[272].nvs" 1920;
	setAttr ".hyp[273].nvs" 1920;
	setAttr ".hyp[274].nvs" 1920;
	setAttr ".hyp[275].nvs" 1920;
	setAttr ".hyp[276].nvs" 1920;
	setAttr ".hyp[277].nvs" 1920;
	setAttr ".hyp[278].nvs" 1920;
	setAttr ".hyp[279].nvs" 1920;
	setAttr ".hyp[280].nvs" 1920;
	setAttr ".hyp[281].nvs" 1920;
	setAttr ".hyp[282].nvs" 1920;
	setAttr ".hyp[283].nvs" 1920;
	setAttr ".hyp[284].nvs" 1920;
	setAttr ".hyp[285].nvs" 1920;
	setAttr ".hyp[286].nvs" 1920;
	setAttr ".hyp[287].nvs" 1920;
	setAttr ".hyp[288].nvs" 1920;
	setAttr ".hyp[289].nvs" 1920;
	setAttr ".hyp[290].nvs" 1920;
	setAttr ".hyp[291].nvs" 1920;
	setAttr ".hyp[292].nvs" 1920;
	setAttr ".hyp[293].nvs" 1920;
	setAttr ".hyp[294].nvs" 1920;
	setAttr ".hyp[295].nvs" 1920;
	setAttr ".hyp[296].nvs" 1920;
	setAttr ".hyp[297].nvs" 1920;
	setAttr ".hyp[298].nvs" 1920;
	setAttr ".hyp[299].nvs" 1920;
	setAttr ".hyp[300].nvs" 1920;
	setAttr ".hyp[301].nvs" 1920;
	setAttr ".hyp[302].nvs" 1920;
	setAttr ".hyp[303].nvs" 1920;
	setAttr ".hyp[304].nvs" 1920;
	setAttr ".hyp[305].nvs" 1920;
	setAttr ".hyp[306].nvs" 1920;
	setAttr ".hyp[307].nvs" 1920;
	setAttr ".hyp[308].nvs" 1920;
	setAttr ".hyp[309].nvs" 1920;
	setAttr ".hyp[310].nvs" 1920;
	setAttr ".hyp[311].nvs" 1920;
	setAttr ".hyp[312].nvs" 1920;
	setAttr ".hyp[313].nvs" 1920;
	setAttr ".hyp[314].nvs" 1920;
	setAttr ".hyp[315].nvs" 1920;
	setAttr ".hyp[316].nvs" 1920;
	setAttr ".hyp[317].nvs" 1920;
	setAttr ".hyp[318].nvs" 1920;
	setAttr ".hyp[319].nvs" 1920;
	setAttr ".hyp[320].nvs" 1920;
	setAttr ".hyp[321].nvs" 1920;
	setAttr ".hyp[322].nvs" 1920;
	setAttr ".hyp[323].nvs" 1920;
	setAttr ".hyp[324].nvs" 1920;
	setAttr ".hyp[325].nvs" 1920;
	setAttr ".hyp[326].nvs" 1920;
	setAttr ".hyp[327].nvs" 1920;
	setAttr ".hyp[328].nvs" 1920;
	setAttr ".hyp[329].nvs" 1920;
	setAttr ".hyp[330].nvs" 1920;
	setAttr ".hyp[331].nvs" 1920;
	setAttr ".hyp[332].nvs" 1920;
	setAttr ".hyp[333].nvs" 1920;
	setAttr ".hyp[334].nvs" 1920;
	setAttr ".hyp[335].nvs" 1920;
	setAttr ".hyp[336].nvs" 1920;
	setAttr ".hyp[337].nvs" 1920;
	setAttr ".hyp[338].nvs" 1920;
	setAttr ".hyp[339].nvs" 1920;
	setAttr ".hyp[340].nvs" 1920;
	setAttr ".hyp[341].nvs" 1920;
	setAttr ".anf" yes;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 101 -max 147 -ast 101 -aet 147 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 147;
	setAttr -av ".unw" 147;
select -ne :sequenceManager1;
	setAttr ".o" 147;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 98 ".st";
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
	setAttr -s 28 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -s 41 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 6 ".r";
select -ne :defaultTextureList1;
	setAttr -s 10 ".tx";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 7 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
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
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w" 1920;
	setAttr -av ".h" 1080;
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar" 1.7769999504089355;
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
connectAttr "Global_SRT_parentConstraint2.ctx" "pr_arr03RN.phl[1]";
connectAttr "Global_SRT_parentConstraint2.cty" "pr_arr03RN.phl[2]";
connectAttr "Global_SRT_parentConstraint2.ctz" "pr_arr03RN.phl[3]";
connectAttr "pr_arr03RN.phl[4]" "Global_SRT_parentConstraint2.crp";
connectAttr "pr_arr03RN.phl[5]" "Global_SRT_parentConstraint2.crt";
connectAttr "Global_SRT_parentConstraint2.crx" "pr_arr03RN.phl[6]";
connectAttr "Global_SRT_parentConstraint2.cry" "pr_arr03RN.phl[7]";
connectAttr "Global_SRT_parentConstraint2.crz" "pr_arr03RN.phl[8]";
connectAttr "pr_arr03RN.phl[9]" "Global_SRT_parentConstraint2.cro";
connectAttr "pr_arr03RN.phl[10]" "Global_SRT_parentConstraint2.cpim";
connectAttr "Global_SRT_parentConstraint1.cty" "pr_bow05RN.phl[1]";
connectAttr "Global_SRT_parentConstraint1.ctx" "pr_bow05RN.phl[2]";
connectAttr "Global_SRT_parentConstraint1.ctz" "pr_bow05RN.phl[3]";
connectAttr "pr_bow05RN.phl[4]" "Global_SRT_parentConstraint1.crp";
connectAttr "pr_bow05RN.phl[5]" "Global_SRT_parentConstraint1.crt";
connectAttr "Global_SRT_parentConstraint1.crx" "pr_bow05RN.phl[6]";
connectAttr "Global_SRT_parentConstraint1.cry" "pr_bow05RN.phl[7]";
connectAttr "Global_SRT_parentConstraint1.crz" "pr_bow05RN.phl[8]";
connectAttr "pr_bow05RN.phl[9]" "Global_SRT_parentConstraint1.cro";
connectAttr "pr_bow05RN.phl[10]" "Global_SRT_parentConstraint1.cpim";
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.ctx" "st_YKR412_0380RN.phl[1]"
		;
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.cty" "st_YKR412_0380RN.phl[2]"
		;
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.ctz" "st_YKR412_0380RN.phl[3]"
		;
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.crx" "st_YKR412_0380RN.phl[4]"
		;
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.cry" "st_YKR412_0380RN.phl[5]"
		;
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.crz" "st_YKR412_0380RN.phl[6]"
		;
connectAttr "st_YKR412_0380RN.phl[7]" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.cro"
		;
connectAttr "st_YKR412_0380RN.phl[8]" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.cpim"
		;
connectAttr "st_YKR412_0380RN.phl[9]" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.crp"
		;
connectAttr "st_YKR412_0380RN.phl[10]" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.crt"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleX.o" "st_YKR412_0380RN.phl[11]"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleY.o" "st_YKR412_0380RN.phl[12]"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleZ.o" "st_YKR412_0380RN.phl[13]"
		;
connectAttr "SH038_CAM:plateCtrl1.lockPlate" "st_YKR412_0380RN.phl[14]";
connectAttr "SH038_CAM:plateCtrl1.showPlate" "st_YKR412_0380RN.phl[15]";
connectAttr "unitConversion7.o" "st_YKR412_0380RN.phl[16]";
connectAttr "unitConversion8.o" "st_YKR412_0380RN.phl[17]";
connectAttr "unitConversion9.o" "st_YKR412_0380RN.phl[18]";
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.ctx" "st_YKR412_0380RN.phl[19]"
		;
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.cty" "st_YKR412_0380RN.phl[20]"
		;
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.ctz" "st_YKR412_0380RN.phl[21]"
		;
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.crx" "st_YKR412_0380RN.phl[22]"
		;
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.cry" "st_YKR412_0380RN.phl[23]"
		;
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.crz" "st_YKR412_0380RN.phl[24]"
		;
connectAttr "st_YKR412_0380RN.phl[25]" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.cro"
		;
connectAttr "st_YKR412_0380RN.phl[26]" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.cpim"
		;
connectAttr "st_YKR412_0380RN.phl[27]" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.crp"
		;
connectAttr "st_YKR412_0380RN.phl[28]" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.crt"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleX.o" "st_YKR412_0380RN.phl[29]"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleY.o" "st_YKR412_0380RN.phl[30]"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleZ.o" "st_YKR412_0380RN.phl[31]"
		;
connectAttr "SH038_CAM:plateCtrl2.lockPlate" "st_YKR412_0380RN.phl[32]";
connectAttr "SH038_CAM:plateCtrl2.showPlate" "st_YKR412_0380RN.phl[33]";
connectAttr "unitConversion4.o" "st_YKR412_0380RN.phl[34]";
connectAttr "unitConversion5.o" "st_YKR412_0380RN.phl[35]";
connectAttr "unitConversion6.o" "st_YKR412_0380RN.phl[36]";
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.ctx" "st_YKR412_0380RN.phl[37]"
		;
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.cty" "st_YKR412_0380RN.phl[38]"
		;
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.ctz" "st_YKR412_0380RN.phl[39]"
		;
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.crx" "st_YKR412_0380RN.phl[40]"
		;
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.cry" "st_YKR412_0380RN.phl[41]"
		;
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.crz" "st_YKR412_0380RN.phl[42]"
		;
connectAttr "st_YKR412_0380RN.phl[43]" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.cro"
		;
connectAttr "st_YKR412_0380RN.phl[44]" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.cpim"
		;
connectAttr "st_YKR412_0380RN.phl[45]" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.crp"
		;
connectAttr "st_YKR412_0380RN.phl[46]" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.crt"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleX.o" "st_YKR412_0380RN.phl[47]"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleY.o" "st_YKR412_0380RN.phl[48]"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleZ.o" "st_YKR412_0380RN.phl[49]"
		;
connectAttr "SH038_CAM:plateCtrl3.lockPlate" "st_YKR412_0380RN.phl[50]";
connectAttr "SH038_CAM:plateCtrl3.showPlate" "st_YKR412_0380RN.phl[51]";
connectAttr "unitConversion1.o" "st_YKR412_0380RN.phl[52]";
connectAttr "unitConversion2.o" "st_YKR412_0380RN.phl[53]";
connectAttr "unitConversion3.o" "st_YKR412_0380RN.phl[54]";
connectAttr "clnLyW_root_translateX.o" "ch_wildwRN.phl[1]";
connectAttr "clnLyW_root_translateY.o" "ch_wildwRN.phl[2]";
connectAttr "clnLyW_root_translateZ.o" "ch_wildwRN.phl[3]";
connectAttr "clnLyW_root_rotateX.o" "ch_wildwRN.phl[4]";
connectAttr "clnLyW_root_rotateY.o" "ch_wildwRN.phl[5]";
connectAttr "clnLyW_root_rotateZ.o" "ch_wildwRN.phl[6]";
connectAttr "clnLyW_root_visibility.o" "ch_wildwRN.phl[7]";
connectAttr "clnLyW_root_scaleX.o" "ch_wildwRN.phl[8]";
connectAttr "clnLyW_root_scaleY.o" "ch_wildwRN.phl[9]";
connectAttr "clnLyW_root_scaleZ.o" "ch_wildwRN.phl[10]";
connectAttr "clnLyW_body_rotateX.o" "ch_wildwRN.phl[11]";
connectAttr "clnLyW_body_rotateY.o" "ch_wildwRN.phl[12]";
connectAttr "clnLyW_body_rotateZ.o" "ch_wildwRN.phl[13]";
connectAttr "clnLyW_body_visibility.o" "ch_wildwRN.phl[14]";
connectAttr "clnLyW_body_translateX.o" "ch_wildwRN.phl[15]";
connectAttr "clnLyW_body_translateY.o" "ch_wildwRN.phl[16]";
connectAttr "clnLyW_body_translateZ.o" "ch_wildwRN.phl[17]";
connectAttr "clnLyW_body_scaleX.o" "ch_wildwRN.phl[18]";
connectAttr "clnLyW_body_scaleY.o" "ch_wildwRN.phl[19]";
connectAttr "clnLyW_body_scaleZ.o" "ch_wildwRN.phl[20]";
connectAttr "clnLyW_chest_rotateX.o" "ch_wildwRN.phl[21]";
connectAttr "clnLyW_chest_rotateY.o" "ch_wildwRN.phl[22]";
connectAttr "clnLyW_chest_rotateZ.o" "ch_wildwRN.phl[23]";
connectAttr "clnLyW_chest_visibility.o" "ch_wildwRN.phl[24]";
connectAttr "clnLyW_chest_translateX.o" "ch_wildwRN.phl[25]";
connectAttr "clnLyW_chest_translateY.o" "ch_wildwRN.phl[26]";
connectAttr "clnLyW_chest_translateZ.o" "ch_wildwRN.phl[27]";
connectAttr "clnLyW_chest_scaleX.o" "ch_wildwRN.phl[28]";
connectAttr "clnLyW_chest_scaleY.o" "ch_wildwRN.phl[29]";
connectAttr "clnLyW_chest_scaleZ.o" "ch_wildwRN.phl[30]";
connectAttr "clnLyW_neck_rotateX.o" "ch_wildwRN.phl[31]";
connectAttr "clnLyW_neck_rotateY.o" "ch_wildwRN.phl[32]";
connectAttr "clnLyW_neck_rotateZ.o" "ch_wildwRN.phl[33]";
connectAttr "clnLyW_neck_visibility.o" "ch_wildwRN.phl[34]";
connectAttr "clnLyW_neck_translateX.o" "ch_wildwRN.phl[35]";
connectAttr "clnLyW_neck_translateY.o" "ch_wildwRN.phl[36]";
connectAttr "clnLyW_neck_translateZ.o" "ch_wildwRN.phl[37]";
connectAttr "clnLyW_neck_scaleX.o" "ch_wildwRN.phl[38]";
connectAttr "clnLyW_neck_scaleY.o" "ch_wildwRN.phl[39]";
connectAttr "clnLyW_neck_scaleZ.o" "ch_wildwRN.phl[40]";
connectAttr "clnLyW_head_translateX.o" "ch_wildwRN.phl[41]";
connectAttr "clnLyW_head_translateY.o" "ch_wildwRN.phl[42]";
connectAttr "clnLyW_head_translateZ.o" "ch_wildwRN.phl[43]";
connectAttr "clnLyW_head_rotateX.o" "ch_wildwRN.phl[44]";
connectAttr "clnLyW_head_rotateY.o" "ch_wildwRN.phl[45]";
connectAttr "clnLyW_head_rotateZ.o" "ch_wildwRN.phl[46]";
connectAttr "clnLyW_head_scaleX.o" "ch_wildwRN.phl[47]";
connectAttr "clnLyW_head_scaleY.o" "ch_wildwRN.phl[48]";
connectAttr "clnLyW_head_scaleZ.o" "ch_wildwRN.phl[49]";
connectAttr "clnLyW_head_visibility.o" "ch_wildwRN.phl[50]";
connectAttr "clnLyW_arm_R_rotateX.o" "ch_wildwRN.phl[51]";
connectAttr "clnLyW_arm_R_rotateY.o" "ch_wildwRN.phl[52]";
connectAttr "clnLyW_arm_R_rotateZ.o" "ch_wildwRN.phl[53]";
connectAttr "clnLyW_arm_R_visibility.o" "ch_wildwRN.phl[54]";
connectAttr "clnLyW_arm_R_translateX.o" "ch_wildwRN.phl[55]";
connectAttr "clnLyW_arm_R_translateY.o" "ch_wildwRN.phl[56]";
connectAttr "clnLyW_arm_R_translateZ.o" "ch_wildwRN.phl[57]";
connectAttr "clnLyW_arm_R_scaleX.o" "ch_wildwRN.phl[58]";
connectAttr "clnLyW_arm_R_scaleY.o" "ch_wildwRN.phl[59]";
connectAttr "clnLyW_arm_R_scaleZ.o" "ch_wildwRN.phl[60]";
connectAttr "clnLyW_forearm_R_rotateX.o" "ch_wildwRN.phl[61]";
connectAttr "clnLyW_forearm_R_rotateY.o" "ch_wildwRN.phl[62]";
connectAttr "clnLyW_forearm_R_rotateZ.o" "ch_wildwRN.phl[63]";
connectAttr "clnLyW_forearm_R_visibility.o" "ch_wildwRN.phl[64]";
connectAttr "clnLyW_forearm_R_translateX.o" "ch_wildwRN.phl[65]";
connectAttr "clnLyW_forearm_R_translateY.o" "ch_wildwRN.phl[66]";
connectAttr "clnLyW_forearm_R_translateZ.o" "ch_wildwRN.phl[67]";
connectAttr "clnLyW_forearm_R_scaleX.o" "ch_wildwRN.phl[68]";
connectAttr "clnLyW_forearm_R_scaleY.o" "ch_wildwRN.phl[69]";
connectAttr "clnLyW_forearm_R_scaleZ.o" "ch_wildwRN.phl[70]";
connectAttr "ch_wildwRN.phl[71]" "Global_SRT_parentConstraint1.tg[0].tt";
connectAttr "ch_wildwRN.phl[72]" "Global_SRT_parentConstraint2.tg[0].tt";
connectAttr "clnLyW_hand_R_translateX.o" "ch_wildwRN.phl[73]";
connectAttr "clnLyW_hand_R_translateY.o" "ch_wildwRN.phl[74]";
connectAttr "clnLyW_hand_R_translateZ.o" "ch_wildwRN.phl[75]";
connectAttr "ch_wildwRN.phl[76]" "Global_SRT_parentConstraint1.tg[0].trp";
connectAttr "ch_wildwRN.phl[77]" "Global_SRT_parentConstraint2.tg[0].trp";
connectAttr "ch_wildwRN.phl[78]" "Global_SRT_parentConstraint1.tg[0].trt";
connectAttr "ch_wildwRN.phl[79]" "Global_SRT_parentConstraint2.tg[0].trt";
connectAttr "ch_wildwRN.phl[80]" "Global_SRT_parentConstraint1.tg[0].tr";
connectAttr "ch_wildwRN.phl[81]" "Global_SRT_parentConstraint2.tg[0].tr";
connectAttr "clnLyW_hand_R_rotateX.o" "ch_wildwRN.phl[82]";
connectAttr "clnLyW_hand_R_rotateY.o" "ch_wildwRN.phl[83]";
connectAttr "clnLyW_hand_R_rotateZ.o" "ch_wildwRN.phl[84]";
connectAttr "ch_wildwRN.phl[85]" "Global_SRT_parentConstraint1.tg[0].tro";
connectAttr "ch_wildwRN.phl[86]" "Global_SRT_parentConstraint2.tg[0].tro";
connectAttr "ch_wildwRN.phl[87]" "Global_SRT_parentConstraint1.tg[0].ts";
connectAttr "ch_wildwRN.phl[88]" "Global_SRT_parentConstraint2.tg[0].ts";
connectAttr "clnLyW_hand_R_scaleX.o" "ch_wildwRN.phl[89]";
connectAttr "clnLyW_hand_R_scaleY.o" "ch_wildwRN.phl[90]";
connectAttr "clnLyW_hand_R_scaleZ.o" "ch_wildwRN.phl[91]";
connectAttr "ch_wildwRN.phl[92]" "Global_SRT_parentConstraint1.tg[0].tpm";
connectAttr "ch_wildwRN.phl[93]" "Global_SRT_parentConstraint2.tg[0].tpm";
connectAttr "clnLyW_hand_R_visibility.o" "ch_wildwRN.phl[94]";
connectAttr "clnLyW_arm_L_rotateX.o" "ch_wildwRN.phl[95]";
connectAttr "clnLyW_arm_L_rotateY.o" "ch_wildwRN.phl[96]";
connectAttr "clnLyW_arm_L_rotateZ.o" "ch_wildwRN.phl[97]";
connectAttr "clnLyW_arm_L_visibility.o" "ch_wildwRN.phl[98]";
connectAttr "clnLyW_arm_L_translateX.o" "ch_wildwRN.phl[99]";
connectAttr "clnLyW_arm_L_translateY.o" "ch_wildwRN.phl[100]";
connectAttr "clnLyW_arm_L_translateZ.o" "ch_wildwRN.phl[101]";
connectAttr "clnLyW_arm_L_scaleX.o" "ch_wildwRN.phl[102]";
connectAttr "clnLyW_arm_L_scaleY.o" "ch_wildwRN.phl[103]";
connectAttr "clnLyW_arm_L_scaleZ.o" "ch_wildwRN.phl[104]";
connectAttr "clnLyW_forearm_L_rotateX.o" "ch_wildwRN.phl[105]";
connectAttr "clnLyW_forearm_L_rotateY.o" "ch_wildwRN.phl[106]";
connectAttr "clnLyW_forearm_L_rotateZ.o" "ch_wildwRN.phl[107]";
connectAttr "clnLyW_forearm_L_visibility.o" "ch_wildwRN.phl[108]";
connectAttr "clnLyW_forearm_L_translateX.o" "ch_wildwRN.phl[109]";
connectAttr "clnLyW_forearm_L_translateY.o" "ch_wildwRN.phl[110]";
connectAttr "clnLyW_forearm_L_translateZ.o" "ch_wildwRN.phl[111]";
connectAttr "clnLyW_forearm_L_scaleX.o" "ch_wildwRN.phl[112]";
connectAttr "clnLyW_forearm_L_scaleY.o" "ch_wildwRN.phl[113]";
connectAttr "clnLyW_forearm_L_scaleZ.o" "ch_wildwRN.phl[114]";
connectAttr "clnLyW_hand_L_rotateX.o" "ch_wildwRN.phl[115]";
connectAttr "clnLyW_hand_L_rotateY.o" "ch_wildwRN.phl[116]";
connectAttr "clnLyW_hand_L_rotateZ.o" "ch_wildwRN.phl[117]";
connectAttr "clnLyW_hand_L_visibility.o" "ch_wildwRN.phl[118]";
connectAttr "clnLyW_hand_L_translateX.o" "ch_wildwRN.phl[119]";
connectAttr "clnLyW_hand_L_translateY.o" "ch_wildwRN.phl[120]";
connectAttr "clnLyW_hand_L_translateZ.o" "ch_wildwRN.phl[121]";
connectAttr "clnLyW_hand_L_scaleX.o" "ch_wildwRN.phl[122]";
connectAttr "clnLyW_hand_L_scaleY.o" "ch_wildwRN.phl[123]";
connectAttr "clnLyW_hand_L_scaleZ.o" "ch_wildwRN.phl[124]";
connectAttr "clnLyW_cloth_01_rotateX.o" "ch_wildwRN.phl[125]";
connectAttr "clnLyW_cloth_01_rotateY.o" "ch_wildwRN.phl[126]";
connectAttr "clnLyW_cloth_01_rotateZ.o" "ch_wildwRN.phl[127]";
connectAttr "clnLyW_cloth_01_visibility.o" "ch_wildwRN.phl[128]";
connectAttr "clnLyW_cloth_01_translateX.o" "ch_wildwRN.phl[129]";
connectAttr "clnLyW_cloth_01_translateY.o" "ch_wildwRN.phl[130]";
connectAttr "clnLyW_cloth_01_translateZ.o" "ch_wildwRN.phl[131]";
connectAttr "clnLyW_cloth_01_scaleX.o" "ch_wildwRN.phl[132]";
connectAttr "clnLyW_cloth_01_scaleY.o" "ch_wildwRN.phl[133]";
connectAttr "clnLyW_cloth_01_scaleZ.o" "ch_wildwRN.phl[134]";
connectAttr "clnLyW_cloth_02_rotateX.o" "ch_wildwRN.phl[135]";
connectAttr "clnLyW_cloth_02_rotateY.o" "ch_wildwRN.phl[136]";
connectAttr "clnLyW_cloth_02_rotateZ.o" "ch_wildwRN.phl[137]";
connectAttr "clnLyW_cloth_02_visibility.o" "ch_wildwRN.phl[138]";
connectAttr "clnLyW_cloth_02_translateX.o" "ch_wildwRN.phl[139]";
connectAttr "clnLyW_cloth_02_translateY.o" "ch_wildwRN.phl[140]";
connectAttr "clnLyW_cloth_02_translateZ.o" "ch_wildwRN.phl[141]";
connectAttr "clnLyW_cloth_02_scaleX.o" "ch_wildwRN.phl[142]";
connectAttr "clnLyW_cloth_02_scaleY.o" "ch_wildwRN.phl[143]";
connectAttr "clnLyW_cloth_02_scaleZ.o" "ch_wildwRN.phl[144]";
connectAttr "clnLyW_leg_L_rotateX.o" "ch_wildwRN.phl[145]";
connectAttr "clnLyW_leg_L_rotateY.o" "ch_wildwRN.phl[146]";
connectAttr "clnLyW_leg_L_rotateZ.o" "ch_wildwRN.phl[147]";
connectAttr "clnLyW_leg_L_visibility.o" "ch_wildwRN.phl[148]";
connectAttr "clnLyW_leg_L_translateX.o" "ch_wildwRN.phl[149]";
connectAttr "clnLyW_leg_L_translateY.o" "ch_wildwRN.phl[150]";
connectAttr "clnLyW_leg_L_translateZ.o" "ch_wildwRN.phl[151]";
connectAttr "clnLyW_leg_L_scaleX.o" "ch_wildwRN.phl[152]";
connectAttr "clnLyW_leg_L_scaleY.o" "ch_wildwRN.phl[153]";
connectAttr "clnLyW_leg_L_scaleZ.o" "ch_wildwRN.phl[154]";
connectAttr "clnLyW_foreleg_L_rotateX.o" "ch_wildwRN.phl[155]";
connectAttr "clnLyW_foreleg_L_rotateY.o" "ch_wildwRN.phl[156]";
connectAttr "clnLyW_foreleg_L_rotateZ.o" "ch_wildwRN.phl[157]";
connectAttr "clnLyW_foreleg_L_visibility.o" "ch_wildwRN.phl[158]";
connectAttr "clnLyW_foreleg_L_translateX.o" "ch_wildwRN.phl[159]";
connectAttr "clnLyW_foreleg_L_translateY.o" "ch_wildwRN.phl[160]";
connectAttr "clnLyW_foreleg_L_translateZ.o" "ch_wildwRN.phl[161]";
connectAttr "clnLyW_foreleg_L_scaleX.o" "ch_wildwRN.phl[162]";
connectAttr "clnLyW_foreleg_L_scaleY.o" "ch_wildwRN.phl[163]";
connectAttr "clnLyW_foreleg_L_scaleZ.o" "ch_wildwRN.phl[164]";
connectAttr "clnLyW_foot_L_rotateX.o" "ch_wildwRN.phl[165]";
connectAttr "clnLyW_foot_L_rotateY.o" "ch_wildwRN.phl[166]";
connectAttr "clnLyW_foot_L_rotateZ.o" "ch_wildwRN.phl[167]";
connectAttr "clnLyW_foot_L_visibility.o" "ch_wildwRN.phl[168]";
connectAttr "clnLyW_foot_L_translateX.o" "ch_wildwRN.phl[169]";
connectAttr "clnLyW_foot_L_translateY.o" "ch_wildwRN.phl[170]";
connectAttr "clnLyW_foot_L_translateZ.o" "ch_wildwRN.phl[171]";
connectAttr "clnLyW_foot_L_scaleX.o" "ch_wildwRN.phl[172]";
connectAttr "clnLyW_foot_L_scaleY.o" "ch_wildwRN.phl[173]";
connectAttr "clnLyW_foot_L_scaleZ.o" "ch_wildwRN.phl[174]";
connectAttr "clnLyW_leg_R_rotateX.o" "ch_wildwRN.phl[175]";
connectAttr "clnLyW_leg_R_rotateY.o" "ch_wildwRN.phl[176]";
connectAttr "clnLyW_leg_R_rotateZ.o" "ch_wildwRN.phl[177]";
connectAttr "clnLyW_leg_R_visibility.o" "ch_wildwRN.phl[178]";
connectAttr "clnLyW_leg_R_translateX.o" "ch_wildwRN.phl[179]";
connectAttr "clnLyW_leg_R_translateY.o" "ch_wildwRN.phl[180]";
connectAttr "clnLyW_leg_R_translateZ.o" "ch_wildwRN.phl[181]";
connectAttr "clnLyW_leg_R_scaleX.o" "ch_wildwRN.phl[182]";
connectAttr "clnLyW_leg_R_scaleY.o" "ch_wildwRN.phl[183]";
connectAttr "clnLyW_leg_R_scaleZ.o" "ch_wildwRN.phl[184]";
connectAttr "clnLyW_foreleg_R_rotateX.o" "ch_wildwRN.phl[185]";
connectAttr "clnLyW_foreleg_R_rotateY.o" "ch_wildwRN.phl[186]";
connectAttr "clnLyW_foreleg_R_rotateZ.o" "ch_wildwRN.phl[187]";
connectAttr "clnLyW_foreleg_R_visibility.o" "ch_wildwRN.phl[188]";
connectAttr "clnLyW_foreleg_R_translateX.o" "ch_wildwRN.phl[189]";
connectAttr "clnLyW_foreleg_R_translateY.o" "ch_wildwRN.phl[190]";
connectAttr "clnLyW_foreleg_R_translateZ.o" "ch_wildwRN.phl[191]";
connectAttr "clnLyW_foreleg_R_scaleX.o" "ch_wildwRN.phl[192]";
connectAttr "clnLyW_foreleg_R_scaleY.o" "ch_wildwRN.phl[193]";
connectAttr "clnLyW_foreleg_R_scaleZ.o" "ch_wildwRN.phl[194]";
connectAttr "clnLyW_foot_R_rotateX.o" "ch_wildwRN.phl[195]";
connectAttr "clnLyW_foot_R_rotateY.o" "ch_wildwRN.phl[196]";
connectAttr "clnLyW_foot_R_rotateZ.o" "ch_wildwRN.phl[197]";
connectAttr "clnLyW_foot_R_visibility.o" "ch_wildwRN.phl[198]";
connectAttr "clnLyW_foot_R_translateX.o" "ch_wildwRN.phl[199]";
connectAttr "clnLyW_foot_R_translateY.o" "ch_wildwRN.phl[200]";
connectAttr "clnLyW_foot_R_translateZ.o" "ch_wildwRN.phl[201]";
connectAttr "clnLyW_foot_R_scaleX.o" "ch_wildwRN.phl[202]";
connectAttr "clnLyW_foot_R_scaleY.o" "ch_wildwRN.phl[203]";
connectAttr "clnLyW_foot_R_scaleZ.o" "ch_wildwRN.phl[204]";
connectAttr "SH038_CAMRN.phl[1]" "SH038_CAM:plateCtrl3ClusteringHandle.sx";
connectAttr "SH038_CAMRN.phl[2]" "SH038_CAM:plateCtrl3ClusteringHandle.sy";
connectAttr "SH038_CAMRN.phl[3]" "SH038_CAM:plateCtrl2ClusteringHandle.sx";
connectAttr "SH038_CAMRN.phl[4]" "SH038_CAM:plateCtrl2ClusteringHandle.sy";
connectAttr "SH038_CAMRN.phl[5]" "SH038_CAM:plateCtrl1ClusteringHandle.sx";
connectAttr "SH038_CAMRN.phl[6]" "SH038_CAM:plateCtrl1ClusteringHandle.sy";
connectAttr "SH038_CAMRN.phl[7]" "depthCorrection.i1";
connectAttr "SH038_CAMRN.phl[8]" "platesHolder.size";
connectAttr "SH038_CAMRN.phl[9]" "cameraMarker_pointConstraint1.tg[0].tt";
connectAttr "SH038_CAMRN.phl[10]" "cameraMarker_pointConstraint1.tg[0].trp";
connectAttr "SH038_CAMRN.phl[11]" "cameraMarker_pointConstraint1.tg[0].trt";
connectAttr "SH038_CAMRN.phl[12]" "cameraMarker_pointConstraint1.tg[0].tpm";
connectAttr "SH038_CAMRN.phl[13]" "imagePlaneAlphaFactor.i1x";
connectAttr "SH038_CAMRN.phl[14]" "sh038ImagePlaneShape.v";
connectAttr "SH038_CAMRN.phl[15]" "sh038ImagePlaneShape.ox";
connectAttr "SH038_CAMRN.phl[16]" "sh038ImagePlaneShape.oy";
connectAttr "SH038_CAMRN.phl[17]" "sh038.ccm";
connectAttr "sh038ImagePlaneShape.msg" "SH038_CAMRN.phl[18]";
connectAttr "SH038_CAMRN.phl[19]" "platesHolder_parentConstraint1.tg[0].tr";
connectAttr "SH038_CAMRN.phl[20]" "platesHolder_parentConstraint1.tg[0].ts";
connectAttr "SH038_CAMRN.phl[21]" "platesHolder_parentConstraint1.tg[0].tt";
connectAttr "SH038_CAMRN.phl[22]" "platesHolder_parentConstraint1.tg[0].trp";
connectAttr "SH038_CAMRN.phl[23]" "platesHolder_parentConstraint1.tg[0].trt";
connectAttr "SH038_CAMRN.phl[24]" "platesHolder_parentConstraint1.tg[0].tpm";
connectAttr "SH038_CAMRN.phl[25]" "platesHolder_parentConstraint1.tg[0].tro";
connectAttr "platesHolder.size" "platesHolder.sx";
connectAttr "platesHolder.size" "platesHolder.sy";
connectAttr "platesHolder_parentConstraint1.ctx" "platesHolder.tx";
connectAttr "platesHolder_parentConstraint1.cty" "platesHolder.ty";
connectAttr "platesHolder_parentConstraint1.ctz" "platesHolder.tz";
connectAttr "platesHolder_parentConstraint1.crx" "platesHolder.rx";
connectAttr "platesHolder_parentConstraint1.cry" "platesHolder.ry";
connectAttr "platesHolder_parentConstraint1.crz" "platesHolder.rz";
connectAttr "platesHolder_parentConstraint1.w0" "platesHolder_parentConstraint1.tg[0].tw"
		;
connectAttr "platesHolder.ro" "platesHolder_parentConstraint1.cro";
connectAttr "platesHolder.pim" "platesHolder_parentConstraint1.cpim";
connectAttr "platesHolder.rp" "platesHolder_parentConstraint1.crp";
connectAttr "platesHolder.rpt" "platesHolder_parentConstraint1.crt";
connectAttr "cameraMarker_pointConstraint1.ctx" "cameraMarker.tx";
connectAttr "cameraMarker_pointConstraint1.cty" "cameraMarker.ty";
connectAttr "cameraMarker_pointConstraint1.ctz" "cameraMarker.tz";
connectAttr "cameraMarker_pointConstraint1.w0" "cameraMarker_pointConstraint1.tg[0].tw"
		;
connectAttr "cameraMarker.pim" "cameraMarker_pointConstraint1.cpim";
connectAttr "cameraMarker.rp" "cameraMarker_pointConstraint1.crp";
connectAttr "cameraMarker.rpt" "cameraMarker_pointConstraint1.crt";
connectAttr "SH038_CAM:plateCtrl3_factor.o" "SH038_CAM:plateCtrl3_offset.sx";
connectAttr "SH038_CAM:plateCtrl3_factor.o" "SH038_CAM:plateCtrl3_offset.sy";
connectAttr "SH038_CAM:plateCtrl3Clustering.og[0]" "SH038_CAM:plateCtrl3Shape.cr"
		;
connectAttr "tweak1.pl[0].cp[0]" "SH038_CAM:plateCtrl3Shape.twl";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId.id" "SH038_CAM:plateCtrl3Shape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringSet.mwc" "SH038_CAM:plateCtrl3Shape.iog.og[0].gco"
		;
connectAttr "groupId5.id" "SH038_CAM:plateCtrl3Shape.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "SH038_CAM:plateCtrl3Shape.iog.og[1].gco";
connectAttr "SH038_CAM:plateCtrl3Clustering.og[1]" "SH038_CAM:plateCtrl3Shape1.cr"
		;
connectAttr "tweak2.pl[0].cp[0]" "SH038_CAM:plateCtrl3Shape1.twl";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId1.id" "SH038_CAM:plateCtrl3Shape1.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringSet.mwc" "SH038_CAM:plateCtrl3Shape1.iog.og[0].gco"
		;
connectAttr "groupId6.id" "SH038_CAM:plateCtrl3Shape1.iog.og[1].gid";
connectAttr "tweakSet2.mwc" "SH038_CAM:plateCtrl3Shape1.iog.og[1].gco";
connectAttr "SH038_CAM:plateCtrl3Clustering.og[2]" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.cr"
		;
connectAttr "tweak3.pl[0].cp[0]" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.twl"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId2.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringSet.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.iog.og[0].gco"
		;
connectAttr "groupId7.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.iog.og[1].gid"
		;
connectAttr "tweakSet3.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.iog.og[1].gco"
		;
connectAttr "SH038_CAM:plateCtrl3Clustering.og[3]" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.cr"
		;
connectAttr "tweak4.pl[0].cp[0]" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.twl"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId3.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringSet.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.iog.og[0].gco"
		;
connectAttr "groupId8.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.iog.og[1].gid"
		;
connectAttr "tweakSet4.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.iog.og[1].gco"
		;
connectAttr "SH038_CAM:plateCtrl3.showResizingArrows" "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows.v"
		;
connectAttr "SH038_CAM:plateCtrl2_factor.o" "SH038_CAM:plateCtrl2_offset.sx";
connectAttr "SH038_CAM:plateCtrl2_factor.o" "SH038_CAM:plateCtrl2_offset.sy";
connectAttr "SH038_CAM:plateCtrl2Clustering.og[0]" "SH038_CAM:plateCtrl2Shape.cr"
		;
connectAttr "tweak5.pl[0].cp[0]" "SH038_CAM:plateCtrl2Shape.twl";
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId.id" "SH038_CAM:plateCtrl2Shape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringSet.mwc" "SH038_CAM:plateCtrl2Shape.iog.og[0].gco"
		;
connectAttr "groupId13.id" "SH038_CAM:plateCtrl2Shape.iog.og[1].gid";
connectAttr "tweakSet5.mwc" "SH038_CAM:plateCtrl2Shape.iog.og[1].gco";
connectAttr "SH038_CAM:plateCtrl2Clustering.og[1]" "SH038_CAM:plateCtrl2Shape1.cr"
		;
connectAttr "tweak6.pl[0].cp[0]" "SH038_CAM:plateCtrl2Shape1.twl";
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId1.id" "SH038_CAM:plateCtrl2Shape1.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringSet.mwc" "SH038_CAM:plateCtrl2Shape1.iog.og[0].gco"
		;
connectAttr "groupId14.id" "SH038_CAM:plateCtrl2Shape1.iog.og[1].gid";
connectAttr "tweakSet6.mwc" "SH038_CAM:plateCtrl2Shape1.iog.og[1].gco";
connectAttr "SH038_CAM:plateCtrl2Clustering.og[2]" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.cr"
		;
connectAttr "tweak7.pl[0].cp[0]" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.twl"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId2.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringSet.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.iog.og[0].gco"
		;
connectAttr "groupId15.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.iog.og[1].gid"
		;
connectAttr "tweakSet7.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.iog.og[1].gco"
		;
connectAttr "SH038_CAM:plateCtrl2Clustering.og[3]" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.cr"
		;
connectAttr "tweak8.pl[0].cp[0]" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.twl"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId3.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringSet.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.iog.og[0].gco"
		;
connectAttr "groupId16.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.iog.og[1].gid"
		;
connectAttr "tweakSet8.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.iog.og[1].gco"
		;
connectAttr "SH038_CAM:plateCtrl2.showResizingArrows" "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows.v"
		;
connectAttr "SH038_CAM:plateCtrl1_factor.o" "SH038_CAM:plateCtrl1_offset.sx";
connectAttr "SH038_CAM:plateCtrl1_factor.o" "SH038_CAM:plateCtrl1_offset.sy";
connectAttr "SH038_CAM:plateCtrl1Clustering.og[0]" "SH038_CAM:plateCtrl1Shape.cr"
		;
connectAttr "tweak9.pl[0].cp[0]" "SH038_CAM:plateCtrl1Shape.twl";
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId.id" "SH038_CAM:plateCtrl1Shape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringSet.mwc" "SH038_CAM:plateCtrl1Shape.iog.og[0].gco"
		;
connectAttr "groupId21.id" "SH038_CAM:plateCtrl1Shape.iog.og[1].gid";
connectAttr "tweakSet9.mwc" "SH038_CAM:plateCtrl1Shape.iog.og[1].gco";
connectAttr "SH038_CAM:plateCtrl1Clustering.og[1]" "SH038_CAM:plateCtrl1Shape1.cr"
		;
connectAttr "tweak10.pl[0].cp[0]" "SH038_CAM:plateCtrl1Shape1.twl";
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId1.id" "SH038_CAM:plateCtrl1Shape1.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringSet.mwc" "SH038_CAM:plateCtrl1Shape1.iog.og[0].gco"
		;
connectAttr "groupId22.id" "SH038_CAM:plateCtrl1Shape1.iog.og[1].gid";
connectAttr "tweakSet10.mwc" "SH038_CAM:plateCtrl1Shape1.iog.og[1].gco";
connectAttr "SH038_CAM:plateCtrl1Clustering.og[2]" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.cr"
		;
connectAttr "tweak11.pl[0].cp[0]" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.twl"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId2.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringSet.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.iog.og[0].gco"
		;
connectAttr "groupId23.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.iog.og[1].gid"
		;
connectAttr "tweakSet11.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.iog.og[1].gco"
		;
connectAttr "SH038_CAM:plateCtrl1Clustering.og[3]" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.cr"
		;
connectAttr "tweak12.pl[0].cp[0]" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.twl"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId3.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.iog.og[0].gid"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringSet.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.iog.og[0].gco"
		;
connectAttr "groupId24.id" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.iog.og[1].gid"
		;
connectAttr "tweakSet12.mwc" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.iog.og[1].gco"
		;
connectAttr "SH038_CAM:plateCtrl1.showResizingArrows" "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows.v"
		;
connectAttr "sh038ImagePlaneShape_frameExtension.o" "sh038ImagePlaneShape.fe";
connectAttr "imagePlaneAlphaFactor.ox" "sh038ImagePlaneShape.ag";
connectAttr "depthCorrection.o" "sh038ImagePlaneShape.d";
connectAttr "Global_SRT_parentConstraint2.w0" "Global_SRT_parentConstraint2.tg[0].tw"
		;
connectAttr "Global_SRT_parentConstraint1.w0" "Global_SRT_parentConstraint1.tg[0].tw"
		;
connectAttr "SH038_CAM:plateCtrl3.t" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].tt"
		;
connectAttr "SH038_CAM:plateCtrl3.rp" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].trp"
		;
connectAttr "SH038_CAM:plateCtrl3.rpt" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].trt"
		;
connectAttr "SH038_CAM:plateCtrl3.r" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].tr"
		;
connectAttr "SH038_CAM:plateCtrl3.ro" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].tro"
		;
connectAttr "SH038_CAM:plateCtrl3.s" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].ts"
		;
connectAttr "SH038_CAM:plateCtrl3.pm" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].tpm"
		;
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.w0" "YKR412_038_03_GlobalSRT_FD_parentConstraint1.tg[0].tw"
		;
connectAttr "SH038_CAM:plateCtrl2.t" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].tt"
		;
connectAttr "SH038_CAM:plateCtrl2.rp" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].trp"
		;
connectAttr "SH038_CAM:plateCtrl2.rpt" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].trt"
		;
connectAttr "SH038_CAM:plateCtrl2.r" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].tr"
		;
connectAttr "SH038_CAM:plateCtrl2.ro" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].tro"
		;
connectAttr "SH038_CAM:plateCtrl2.s" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].ts"
		;
connectAttr "SH038_CAM:plateCtrl2.pm" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].tpm"
		;
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.w0" "YKR412_038_02_GlobalSRT_FX_parentConstraint1.tg[0].tw"
		;
connectAttr "SH038_CAM:plateCtrl1.t" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].tt"
		;
connectAttr "SH038_CAM:plateCtrl1.rp" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].trp"
		;
connectAttr "SH038_CAM:plateCtrl1.rpt" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].trt"
		;
connectAttr "SH038_CAM:plateCtrl1.r" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].tr"
		;
connectAttr "SH038_CAM:plateCtrl1.ro" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].tro"
		;
connectAttr "SH038_CAM:plateCtrl1.s" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].ts"
		;
connectAttr "SH038_CAM:plateCtrl1.pm" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].tpm"
		;
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.w0" "YKR412_038_01_GlobalSRT_BG_parentConstraint1.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr ":miDefaultFramebuffer.dat" "defaultRenderLayer.adjs[0].plg";
connectAttr "pr_arr03RNfosterParent1.msg" "pr_arr03RN.fp";
connectAttr "pr_bow05RNfosterParent1.msg" "pr_bow05RN.fp";
connectAttr "st_YKR412_0380RNfosterParent1.msg" "st_YKR412_0380RN.fp";
connectAttr "sh038.msg" "sequencer1.shts" -na;
connectAttr "sh038Audio.msg" "sh038.aud";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupParts.og" "SH038_CAM:plateCtrl3Clustering.ip[0].ig"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId.id" "SH038_CAM:plateCtrl3Clustering.ip[0].gi"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupParts1.og" "SH038_CAM:plateCtrl3Clustering.ip[1].ig"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId1.id" "SH038_CAM:plateCtrl3Clustering.ip[1].gi"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupParts2.og" "SH038_CAM:plateCtrl3Clustering.ip[2].ig"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId2.id" "SH038_CAM:plateCtrl3Clustering.ip[2].gi"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupParts3.og" "SH038_CAM:plateCtrl3Clustering.ip[3].ig"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId3.id" "SH038_CAM:plateCtrl3Clustering.ip[3].gi"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringHandle.wm" "SH038_CAM:plateCtrl3Clustering.ma"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringHandleShape.x" "SH038_CAM:plateCtrl3Clustering.x"
		;
connectAttr "groupParts5.og" "tweak1.ip[0].ig";
connectAttr "groupId5.id" "tweak1.ip[0].gi";
connectAttr "groupParts6.og" "tweak2.ip[0].ig";
connectAttr "groupId6.id" "tweak2.ip[0].gi";
connectAttr "groupParts7.og" "tweak3.ip[0].ig";
connectAttr "groupId7.id" "tweak3.ip[0].gi";
connectAttr "groupParts8.og" "tweak4.ip[0].ig";
connectAttr "groupId8.id" "tweak4.ip[0].gi";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId.msg" "SH038_CAM:plateCtrl3ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId1.msg" "SH038_CAM:plateCtrl3ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId2.msg" "SH038_CAM:plateCtrl3ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId3.msg" "SH038_CAM:plateCtrl3ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl3Shape.iog.og[0]" "SH038_CAM:plateCtrl3ClusteringSet.dsm"
		 -na;
connectAttr "SH038_CAM:plateCtrl3Shape1.iog.og[0]" "SH038_CAM:plateCtrl3ClusteringSet.dsm"
		 -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.iog.og[0]" "SH038_CAM:plateCtrl3ClusteringSet.dsm"
		 -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.iog.og[0]" "SH038_CAM:plateCtrl3ClusteringSet.dsm"
		 -na;
connectAttr "SH038_CAM:plateCtrl3Clustering.msg" "SH038_CAM:plateCtrl3ClusteringSet.ub[0]"
		;
connectAttr "tweak1.og[0]" "SH038_CAM:plateCtrl3ClusteringGroupParts.ig";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId.id" "SH038_CAM:plateCtrl3ClusteringGroupParts.gi"
		;
connectAttr "tweak2.og[0]" "SH038_CAM:plateCtrl3ClusteringGroupParts1.ig";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId1.id" "SH038_CAM:plateCtrl3ClusteringGroupParts1.gi"
		;
connectAttr "tweak3.og[0]" "SH038_CAM:plateCtrl3ClusteringGroupParts2.ig";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId2.id" "SH038_CAM:plateCtrl3ClusteringGroupParts2.gi"
		;
connectAttr "tweak4.og[0]" "SH038_CAM:plateCtrl3ClusteringGroupParts3.ig";
connectAttr "SH038_CAM:plateCtrl3ClusteringGroupId3.id" "SH038_CAM:plateCtrl3ClusteringGroupParts3.gi"
		;
connectAttr "groupId5.msg" "tweakSet1.gn" -na;
connectAttr "SH038_CAM:plateCtrl3Shape.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "plateCtrl3ShapeOrig.ws" "groupParts5.ig";
connectAttr "groupId5.id" "groupParts5.gi";
connectAttr "groupId6.msg" "tweakSet2.gn" -na;
connectAttr "SH038_CAM:plateCtrl3Shape1.iog.og[1]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "plateCtrl3Shape1Orig.ws" "groupParts6.ig";
connectAttr "groupId6.id" "groupParts6.gi";
connectAttr "groupId7.msg" "tweakSet3.gn" -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.iog.og[1]" "tweakSet3.dsm"
		 -na;
connectAttr "tweak3.msg" "tweakSet3.ub[0]";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShapeOrig.ws" "groupParts7.ig"
		;
connectAttr "groupId7.id" "groupParts7.gi";
connectAttr "groupId8.msg" "tweakSet4.gn" -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.iog.og[1]" "tweakSet4.dsm"
		 -na;
connectAttr "tweak4.msg" "tweakSet4.ub[0]";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShapeOrig.ws" "groupParts8.ig"
		;
connectAttr "groupId8.id" "groupParts8.gi";
connectAttr "SH038_CAM:plateCtrl3.tz" "SH038_CAM:plateCtrl3_zCoord.i1";
connectAttr "SH038_CAM:plateCtrl3_offset.tz" "SH038_CAM:plateCtrl3_zCoord.i2";
connectAttr "cameraMarker.tz" "SH038_CAM:plateCtrl3_zDistance.i1[0]";
connectAttr "SH038_CAM:plateCtrl3_zCoord.o" "SH038_CAM:plateCtrl3_zDistance.i1[1]"
		;
connectAttr "SH038_CAM:plateCtrl3_zDistance.o1" "SH038_CAM:plateCtrl3_factor.i1"
		;
connectAttr "SH038_CAM:plateCtrl3.rotX" "unitConversion1.i";
connectAttr "SH038_CAM:plateCtrl3.rotY" "unitConversion2.i";
connectAttr "SH038_CAM:plateCtrl3.rotZ" "unitConversion3.i";
connectAttr "SH038_CAM:plateCtrl3.sx" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleX.i1"
		;
connectAttr "SH038_CAM:plateCtrl3_factor.o" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleX.i2"
		;
connectAttr "SH038_CAM:plateCtrl3.sy" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleY.i1"
		;
connectAttr "SH038_CAM:plateCtrl3_factor.o" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleY.i2"
		;
connectAttr "SH038_CAM:plateCtrl3.sz" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleZ.i1"
		;
connectAttr "SH038_CAM:plateCtrl3_factor.o" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleZ.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleX.o" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleX.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleX.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleY.o" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleY.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleY.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleZ.o" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleZ.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleZ.i2"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupParts.og" "SH038_CAM:plateCtrl2Clustering.ip[0].ig"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId.id" "SH038_CAM:plateCtrl2Clustering.ip[0].gi"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupParts1.og" "SH038_CAM:plateCtrl2Clustering.ip[1].ig"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId1.id" "SH038_CAM:plateCtrl2Clustering.ip[1].gi"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupParts2.og" "SH038_CAM:plateCtrl2Clustering.ip[2].ig"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId2.id" "SH038_CAM:plateCtrl2Clustering.ip[2].gi"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupParts3.og" "SH038_CAM:plateCtrl2Clustering.ip[3].ig"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId3.id" "SH038_CAM:plateCtrl2Clustering.ip[3].gi"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringHandle.wm" "SH038_CAM:plateCtrl2Clustering.ma"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringHandleShape.x" "SH038_CAM:plateCtrl2Clustering.x"
		;
connectAttr "groupParts13.og" "tweak5.ip[0].ig";
connectAttr "groupId13.id" "tweak5.ip[0].gi";
connectAttr "groupParts14.og" "tweak6.ip[0].ig";
connectAttr "groupId14.id" "tweak6.ip[0].gi";
connectAttr "groupParts15.og" "tweak7.ip[0].ig";
connectAttr "groupId15.id" "tweak7.ip[0].gi";
connectAttr "groupParts16.og" "tweak8.ip[0].ig";
connectAttr "groupId16.id" "tweak8.ip[0].gi";
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId.msg" "SH038_CAM:plateCtrl2ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId1.msg" "SH038_CAM:plateCtrl2ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId2.msg" "SH038_CAM:plateCtrl2ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId3.msg" "SH038_CAM:plateCtrl2ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl2Shape.iog.og[0]" "SH038_CAM:plateCtrl2ClusteringSet.dsm"
		 -na;
connectAttr "SH038_CAM:plateCtrl2Shape1.iog.og[0]" "SH038_CAM:plateCtrl2ClusteringSet.dsm"
		 -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.iog.og[0]" "SH038_CAM:plateCtrl2ClusteringSet.dsm"
		 -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.iog.og[0]" "SH038_CAM:plateCtrl2ClusteringSet.dsm"
		 -na;
connectAttr "SH038_CAM:plateCtrl2Clustering.msg" "SH038_CAM:plateCtrl2ClusteringSet.ub[0]"
		;
connectAttr "tweak5.og[0]" "SH038_CAM:plateCtrl2ClusteringGroupParts.ig";
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId.id" "SH038_CAM:plateCtrl2ClusteringGroupParts.gi"
		;
connectAttr "tweak6.og[0]" "SH038_CAM:plateCtrl2ClusteringGroupParts1.ig";
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId1.id" "SH038_CAM:plateCtrl2ClusteringGroupParts1.gi"
		;
connectAttr "tweak7.og[0]" "SH038_CAM:plateCtrl2ClusteringGroupParts2.ig";
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId2.id" "SH038_CAM:plateCtrl2ClusteringGroupParts2.gi"
		;
connectAttr "tweak8.og[0]" "SH038_CAM:plateCtrl2ClusteringGroupParts3.ig";
connectAttr "SH038_CAM:plateCtrl2ClusteringGroupId3.id" "SH038_CAM:plateCtrl2ClusteringGroupParts3.gi"
		;
connectAttr "groupId13.msg" "tweakSet5.gn" -na;
connectAttr "SH038_CAM:plateCtrl2Shape.iog.og[1]" "tweakSet5.dsm" -na;
connectAttr "tweak5.msg" "tweakSet5.ub[0]";
connectAttr "plateCtrl2ShapeOrig.ws" "groupParts13.ig";
connectAttr "groupId13.id" "groupParts13.gi";
connectAttr "groupId14.msg" "tweakSet6.gn" -na;
connectAttr "SH038_CAM:plateCtrl2Shape1.iog.og[1]" "tweakSet6.dsm" -na;
connectAttr "tweak6.msg" "tweakSet6.ub[0]";
connectAttr "plateCtrl2Shape1Orig.ws" "groupParts14.ig";
connectAttr "groupId14.id" "groupParts14.gi";
connectAttr "groupId15.msg" "tweakSet7.gn" -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.iog.og[1]" "tweakSet7.dsm"
		 -na;
connectAttr "tweak7.msg" "tweakSet7.ub[0]";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShapeOrig.ws" "groupParts15.ig"
		;
connectAttr "groupId15.id" "groupParts15.gi";
connectAttr "groupId16.msg" "tweakSet8.gn" -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.iog.og[1]" "tweakSet8.dsm"
		 -na;
connectAttr "tweak8.msg" "tweakSet8.ub[0]";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShapeOrig.ws" "groupParts16.ig"
		;
connectAttr "groupId16.id" "groupParts16.gi";
connectAttr "SH038_CAM:plateCtrl2.tz" "SH038_CAM:plateCtrl2_zCoord.i1";
connectAttr "SH038_CAM:plateCtrl2_offset.tz" "SH038_CAM:plateCtrl2_zCoord.i2";
connectAttr "cameraMarker.tz" "SH038_CAM:plateCtrl2_zDistance.i1[0]";
connectAttr "SH038_CAM:plateCtrl2_zCoord.o" "SH038_CAM:plateCtrl2_zDistance.i1[1]"
		;
connectAttr "SH038_CAM:plateCtrl2_zDistance.o1" "SH038_CAM:plateCtrl2_factor.i1"
		;
connectAttr "SH038_CAM:plateCtrl2.rotX" "unitConversion4.i";
connectAttr "SH038_CAM:plateCtrl2.rotY" "unitConversion5.i";
connectAttr "SH038_CAM:plateCtrl2.rotZ" "unitConversion6.i";
connectAttr "SH038_CAM:plateCtrl2.sx" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleX.i1"
		;
connectAttr "SH038_CAM:plateCtrl2_factor.o" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleX.i2"
		;
connectAttr "SH038_CAM:plateCtrl2.sy" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleY.i1"
		;
connectAttr "SH038_CAM:plateCtrl2_factor.o" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleY.i2"
		;
connectAttr "SH038_CAM:plateCtrl2.sz" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleZ.i1"
		;
connectAttr "SH038_CAM:plateCtrl2_factor.o" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleZ.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleX.o" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleX.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleX.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleY.o" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleY.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleY.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleZ.o" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleZ.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleZ.i2"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupParts.og" "SH038_CAM:plateCtrl1Clustering.ip[0].ig"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId.id" "SH038_CAM:plateCtrl1Clustering.ip[0].gi"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupParts1.og" "SH038_CAM:plateCtrl1Clustering.ip[1].ig"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId1.id" "SH038_CAM:plateCtrl1Clustering.ip[1].gi"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupParts2.og" "SH038_CAM:plateCtrl1Clustering.ip[2].ig"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId2.id" "SH038_CAM:plateCtrl1Clustering.ip[2].gi"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupParts3.og" "SH038_CAM:plateCtrl1Clustering.ip[3].ig"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId3.id" "SH038_CAM:plateCtrl1Clustering.ip[3].gi"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringHandle.wm" "SH038_CAM:plateCtrl1Clustering.ma"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringHandleShape.x" "SH038_CAM:plateCtrl1Clustering.x"
		;
connectAttr "groupParts21.og" "tweak9.ip[0].ig";
connectAttr "groupId21.id" "tweak9.ip[0].gi";
connectAttr "groupParts22.og" "tweak10.ip[0].ig";
connectAttr "groupId22.id" "tweak10.ip[0].gi";
connectAttr "groupParts23.og" "tweak11.ip[0].ig";
connectAttr "groupId23.id" "tweak11.ip[0].gi";
connectAttr "groupParts24.og" "tweak12.ip[0].ig";
connectAttr "groupId24.id" "tweak12.ip[0].gi";
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId.msg" "SH038_CAM:plateCtrl1ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId1.msg" "SH038_CAM:plateCtrl1ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId2.msg" "SH038_CAM:plateCtrl1ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId3.msg" "SH038_CAM:plateCtrl1ClusteringSet.gn"
		 -na;
connectAttr "SH038_CAM:plateCtrl1Shape.iog.og[0]" "SH038_CAM:plateCtrl1ClusteringSet.dsm"
		 -na;
connectAttr "SH038_CAM:plateCtrl1Shape1.iog.og[0]" "SH038_CAM:plateCtrl1ClusteringSet.dsm"
		 -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.iog.og[0]" "SH038_CAM:plateCtrl1ClusteringSet.dsm"
		 -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.iog.og[0]" "SH038_CAM:plateCtrl1ClusteringSet.dsm"
		 -na;
connectAttr "SH038_CAM:plateCtrl1Clustering.msg" "SH038_CAM:plateCtrl1ClusteringSet.ub[0]"
		;
connectAttr "tweak9.og[0]" "SH038_CAM:plateCtrl1ClusteringGroupParts.ig";
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId.id" "SH038_CAM:plateCtrl1ClusteringGroupParts.gi"
		;
connectAttr "tweak10.og[0]" "SH038_CAM:plateCtrl1ClusteringGroupParts1.ig";
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId1.id" "SH038_CAM:plateCtrl1ClusteringGroupParts1.gi"
		;
connectAttr "tweak11.og[0]" "SH038_CAM:plateCtrl1ClusteringGroupParts2.ig";
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId2.id" "SH038_CAM:plateCtrl1ClusteringGroupParts2.gi"
		;
connectAttr "tweak12.og[0]" "SH038_CAM:plateCtrl1ClusteringGroupParts3.ig";
connectAttr "SH038_CAM:plateCtrl1ClusteringGroupId3.id" "SH038_CAM:plateCtrl1ClusteringGroupParts3.gi"
		;
connectAttr "groupId21.msg" "tweakSet9.gn" -na;
connectAttr "SH038_CAM:plateCtrl1Shape.iog.og[1]" "tweakSet9.dsm" -na;
connectAttr "tweak9.msg" "tweakSet9.ub[0]";
connectAttr "plateCtrl1ShapeOrig.ws" "groupParts21.ig";
connectAttr "groupId21.id" "groupParts21.gi";
connectAttr "groupId22.msg" "tweakSet10.gn" -na;
connectAttr "SH038_CAM:plateCtrl1Shape1.iog.og[1]" "tweakSet10.dsm" -na;
connectAttr "tweak10.msg" "tweakSet10.ub[0]";
connectAttr "plateCtrl1Shape1Orig.ws" "groupParts22.ig";
connectAttr "groupId22.id" "groupParts22.gi";
connectAttr "groupId23.msg" "tweakSet11.gn" -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.iog.og[1]" "tweakSet11.dsm"
		 -na;
connectAttr "tweak11.msg" "tweakSet11.ub[0]";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShapeOrig.ws" "groupParts23.ig"
		;
connectAttr "groupId23.id" "groupParts23.gi";
connectAttr "groupId24.msg" "tweakSet12.gn" -na;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.iog.og[1]" "tweakSet12.dsm"
		 -na;
connectAttr "tweak12.msg" "tweakSet12.ub[0]";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShapeOrig.ws" "groupParts24.ig"
		;
connectAttr "groupId24.id" "groupParts24.gi";
connectAttr "SH038_CAM:plateCtrl1.tz" "SH038_CAM:plateCtrl1_zCoord.i1";
connectAttr "SH038_CAM:plateCtrl1_offset.tz" "SH038_CAM:plateCtrl1_zCoord.i2";
connectAttr "cameraMarker.tz" "SH038_CAM:plateCtrl1_zDistance.i1[0]";
connectAttr "SH038_CAM:plateCtrl1_zCoord.o" "SH038_CAM:plateCtrl1_zDistance.i1[1]"
		;
connectAttr "SH038_CAM:plateCtrl1_zDistance.o1" "SH038_CAM:plateCtrl1_factor.i1"
		;
connectAttr "SH038_CAM:plateCtrl1.rotX" "unitConversion7.i";
connectAttr "SH038_CAM:plateCtrl1.rotY" "unitConversion8.i";
connectAttr "SH038_CAM:plateCtrl1.rotZ" "unitConversion9.i";
connectAttr "SH038_CAM:plateCtrl1.sx" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleX.i1"
		;
connectAttr "SH038_CAM:plateCtrl1_factor.o" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleX.i2"
		;
connectAttr "SH038_CAM:plateCtrl1.sy" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleY.i1"
		;
connectAttr "SH038_CAM:plateCtrl1_factor.o" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleY.i2"
		;
connectAttr "SH038_CAM:plateCtrl1.sz" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleZ.i1"
		;
connectAttr "SH038_CAM:plateCtrl1_factor.o" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleZ.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleX.o" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleX.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleX.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleY.o" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleY.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleY.i2"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleZ.o" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleZ.i1"
		;
connectAttr "platesHolder.sx" "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleZ.i2"
		;
connectAttr "hyperView1.msg" "nodeEditorPanel1Info.b[0]";
connectAttr "hyperLayout1.msg" "hyperView1.hl";
connectAttr "sh038ImagePlane.msg" "hyperLayout1.hyp[0].dn";
connectAttr "sh038ImagePlaneShape.msg" "hyperLayout1.hyp[1].dn";
connectAttr "sh038ImagePlaneShape_frameExtension.msg" "hyperLayout1.hyp[2].dn";
connectAttr "sh038Audio.msg" "hyperLayout1.hyp[3].dn";
connectAttr "platesHolder.msg" "hyperLayout1.hyp[4].dn";
connectAttr "platesHolder_parentConstraint1.msg" "hyperLayout1.hyp[5].dn";
connectAttr "cameraMarker.msg" "hyperLayout1.hyp[6].dn";
connectAttr "cameraMarker_pointConstraint1.msg" "hyperLayout1.hyp[7].dn";
connectAttr "SH038_CAM:plateCtrl3.msg" "hyperLayout1.hyp[8].dn";
connectAttr "SH038_CAM:plateCtrl3Shape.msg" "hyperLayout1.hyp[9].dn";
connectAttr "SH038_CAM:plateCtrl3Shape1.msg" "hyperLayout1.hyp[10].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate.msg" "hyperLayout1.hyp[11].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShape.msg" "hyperLayout1.hyp[12].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate.msg" "hyperLayout1.hyp[13].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShape.msg" "hyperLayout1.hyp[14].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows.msg" "hyperLayout1.hyp[15].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingUp.msg" "hyperLayout1.hyp[16].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingUp|resizingUpShape.msg" "hyperLayout1.hyp[17].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingDown.msg" "hyperLayout1.hyp[18].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingDown|resizingDownShape.msg" "hyperLayout1.hyp[19].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingRight.msg" "hyperLayout1.hyp[20].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingRight|resizingRightShape.msg" "hyperLayout1.hyp[21].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingLeft.msg" "hyperLayout1.hyp[22].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|resizingArrows|resizingLeft|resizingLeftShape.msg" "hyperLayout1.hyp[23].dn"
		;
connectAttr "SH038_CAM:plateCtrl3_offset.msg" "hyperLayout1.hyp[24].dn";
connectAttr "SH038_CAM:plateCtrl3Clustering.msg" "hyperLayout1.hyp[25].dn";
connectAttr "plateCtrl3ShapeOrig.msg" "hyperLayout1.hyp[26].dn";
connectAttr "tweak1.msg" "hyperLayout1.hyp[27].dn";
connectAttr "plateCtrl3Shape1Orig.msg" "hyperLayout1.hyp[28].dn";
connectAttr "tweak2.msg" "hyperLayout1.hyp[29].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|plusPlate|plusPlateShapeOrig.msg" "hyperLayout1.hyp[30].dn"
		;
connectAttr "tweak3.msg" "hyperLayout1.hyp[31].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl3_offset|SH038_CAM:plateCtrl3|minusPlate|minusPlateShapeOrig.msg" "hyperLayout1.hyp[32].dn"
		;
connectAttr "tweak4.msg" "hyperLayout1.hyp[33].dn";
connectAttr "SH038_CAM:plateCtrl3ClusteringSet.msg" "hyperLayout1.hyp[34].dn";
connectAttr "tweakSet1.msg" "hyperLayout1.hyp[35].dn";
connectAttr "tweakSet2.msg" "hyperLayout1.hyp[36].dn";
connectAttr "tweakSet3.msg" "hyperLayout1.hyp[37].dn";
connectAttr "tweakSet4.msg" "hyperLayout1.hyp[38].dn";
connectAttr "SH038_CAM:plateCtrl3ClusteringHandle.msg" "hyperLayout1.hyp[39].dn"
		;
connectAttr "SH038_CAM:plateCtrl3ClusteringHandleShape.msg" "hyperLayout1.hyp[40].dn"
		;
connectAttr "SH038_CAM:plateCtrl3_zCoord.msg" "hyperLayout1.hyp[41].dn";
connectAttr "SH038_CAM:plateCtrl3_zDistance.msg" "hyperLayout1.hyp[42].dn";
connectAttr "SH038_CAM:plateCtrl3_factor.msg" "hyperLayout1.hyp[43].dn";
connectAttr "YKR412_038_03_GlobalSRT_FD_parentConstraint1.msg" "hyperLayout1.hyp[44].dn"
		;
connectAttr "unitConversion1.msg" "hyperLayout1.hyp[45].dn";
connectAttr "unitConversion2.msg" "hyperLayout1.hyp[46].dn";
connectAttr "unitConversion3.msg" "hyperLayout1.hyp[47].dn";
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleX.msg" "hyperLayout1.hyp[48].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleY.msg" "hyperLayout1.hyp[49].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_trueScaleZ.msg" "hyperLayout1.hyp[50].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleX.msg" "hyperLayout1.hyp[51].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleY.msg" "hyperLayout1.hyp[52].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_03_GlobalSRT_FD_focal_trueScaleZ.msg" "hyperLayout1.hyp[53].dn"
		;
connectAttr "SH038_CAM:plateCtrl2.msg" "hyperLayout1.hyp[54].dn";
connectAttr "SH038_CAM:plateCtrl2Shape.msg" "hyperLayout1.hyp[55].dn";
connectAttr "SH038_CAM:plateCtrl2Shape1.msg" "hyperLayout1.hyp[56].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate.msg" "hyperLayout1.hyp[57].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShape.msg" "hyperLayout1.hyp[58].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate.msg" "hyperLayout1.hyp[59].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShape.msg" "hyperLayout1.hyp[60].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows.msg" "hyperLayout1.hyp[61].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingUp.msg" "hyperLayout1.hyp[62].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingUp|resizingUpShape.msg" "hyperLayout1.hyp[63].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingDown.msg" "hyperLayout1.hyp[64].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingDown|resizingDownShape.msg" "hyperLayout1.hyp[65].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingRight.msg" "hyperLayout1.hyp[66].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingRight|resizingRightShape.msg" "hyperLayout1.hyp[67].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingLeft.msg" "hyperLayout1.hyp[68].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|resizingArrows|resizingLeft|resizingLeftShape.msg" "hyperLayout1.hyp[69].dn"
		;
connectAttr "SH038_CAM:plateCtrl2_offset.msg" "hyperLayout1.hyp[70].dn";
connectAttr "SH038_CAM:plateCtrl2Clustering.msg" "hyperLayout1.hyp[71].dn";
connectAttr "plateCtrl2ShapeOrig.msg" "hyperLayout1.hyp[72].dn";
connectAttr "tweak5.msg" "hyperLayout1.hyp[73].dn";
connectAttr "plateCtrl2Shape1Orig.msg" "hyperLayout1.hyp[74].dn";
connectAttr "tweak6.msg" "hyperLayout1.hyp[75].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|plusPlate|plusPlateShapeOrig.msg" "hyperLayout1.hyp[76].dn"
		;
connectAttr "tweak7.msg" "hyperLayout1.hyp[77].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl2_offset|SH038_CAM:plateCtrl2|minusPlate|minusPlateShapeOrig.msg" "hyperLayout1.hyp[78].dn"
		;
connectAttr "tweak8.msg" "hyperLayout1.hyp[79].dn";
connectAttr "SH038_CAM:plateCtrl2ClusteringSet.msg" "hyperLayout1.hyp[80].dn";
connectAttr "tweakSet5.msg" "hyperLayout1.hyp[81].dn";
connectAttr "tweakSet6.msg" "hyperLayout1.hyp[82].dn";
connectAttr "tweakSet7.msg" "hyperLayout1.hyp[83].dn";
connectAttr "tweakSet8.msg" "hyperLayout1.hyp[84].dn";
connectAttr "SH038_CAM:plateCtrl2ClusteringHandle.msg" "hyperLayout1.hyp[85].dn"
		;
connectAttr "SH038_CAM:plateCtrl2ClusteringHandleShape.msg" "hyperLayout1.hyp[86].dn"
		;
connectAttr "SH038_CAM:plateCtrl2_zCoord.msg" "hyperLayout1.hyp[87].dn";
connectAttr "SH038_CAM:plateCtrl2_zDistance.msg" "hyperLayout1.hyp[88].dn";
connectAttr "SH038_CAM:plateCtrl2_factor.msg" "hyperLayout1.hyp[89].dn";
connectAttr "YKR412_038_02_GlobalSRT_FX_parentConstraint1.msg" "hyperLayout1.hyp[90].dn"
		;
connectAttr "unitConversion4.msg" "hyperLayout1.hyp[91].dn";
connectAttr "unitConversion5.msg" "hyperLayout1.hyp[92].dn";
connectAttr "unitConversion6.msg" "hyperLayout1.hyp[93].dn";
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleX.msg" "hyperLayout1.hyp[94].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleY.msg" "hyperLayout1.hyp[95].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_trueScaleZ.msg" "hyperLayout1.hyp[96].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleX.msg" "hyperLayout1.hyp[97].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleY.msg" "hyperLayout1.hyp[98].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_02_GlobalSRT_FX_focal_trueScaleZ.msg" "hyperLayout1.hyp[99].dn"
		;
connectAttr "SH038_CAM:plateCtrl1.msg" "hyperLayout1.hyp[100].dn";
connectAttr "SH038_CAM:plateCtrl1Shape.msg" "hyperLayout1.hyp[101].dn";
connectAttr "SH038_CAM:plateCtrl1Shape1.msg" "hyperLayout1.hyp[102].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate.msg" "hyperLayout1.hyp[103].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShape.msg" "hyperLayout1.hyp[104].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate.msg" "hyperLayout1.hyp[105].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShape.msg" "hyperLayout1.hyp[106].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows.msg" "hyperLayout1.hyp[107].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingUp.msg" "hyperLayout1.hyp[108].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingUp|resizingUpShape.msg" "hyperLayout1.hyp[109].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingDown.msg" "hyperLayout1.hyp[110].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingDown|resizingDownShape.msg" "hyperLayout1.hyp[111].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingRight.msg" "hyperLayout1.hyp[112].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingRight|resizingRightShape.msg" "hyperLayout1.hyp[113].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingLeft.msg" "hyperLayout1.hyp[114].dn"
		;
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|resizingArrows|resizingLeft|resizingLeftShape.msg" "hyperLayout1.hyp[115].dn"
		;
connectAttr "SH038_CAM:plateCtrl1_offset.msg" "hyperLayout1.hyp[116].dn";
connectAttr "SH038_CAM:plateCtrl1Clustering.msg" "hyperLayout1.hyp[117].dn";
connectAttr "plateCtrl1ShapeOrig.msg" "hyperLayout1.hyp[118].dn";
connectAttr "tweak9.msg" "hyperLayout1.hyp[119].dn";
connectAttr "plateCtrl1Shape1Orig.msg" "hyperLayout1.hyp[120].dn";
connectAttr "tweak10.msg" "hyperLayout1.hyp[121].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|plusPlate|plusPlateShapeOrig.msg" "hyperLayout1.hyp[122].dn"
		;
connectAttr "tweak11.msg" "hyperLayout1.hyp[123].dn";
connectAttr "|__SET__|platesHolder|SH038_CAM:plateCtrl1_offset|SH038_CAM:plateCtrl1|minusPlate|minusPlateShapeOrig.msg" "hyperLayout1.hyp[124].dn"
		;
connectAttr "tweak12.msg" "hyperLayout1.hyp[125].dn";
connectAttr "SH038_CAM:plateCtrl1ClusteringSet.msg" "hyperLayout1.hyp[126].dn";
connectAttr "tweakSet9.msg" "hyperLayout1.hyp[127].dn";
connectAttr "tweakSet10.msg" "hyperLayout1.hyp[128].dn";
connectAttr "tweakSet11.msg" "hyperLayout1.hyp[129].dn";
connectAttr "tweakSet12.msg" "hyperLayout1.hyp[130].dn";
connectAttr "SH038_CAM:plateCtrl1ClusteringHandle.msg" "hyperLayout1.hyp[131].dn"
		;
connectAttr "SH038_CAM:plateCtrl1ClusteringHandleShape.msg" "hyperLayout1.hyp[132].dn"
		;
connectAttr "SH038_CAM:plateCtrl1_zCoord.msg" "hyperLayout1.hyp[133].dn";
connectAttr "SH038_CAM:plateCtrl1_zDistance.msg" "hyperLayout1.hyp[134].dn";
connectAttr "SH038_CAM:plateCtrl1_factor.msg" "hyperLayout1.hyp[135].dn";
connectAttr "YKR412_038_01_GlobalSRT_BG_parentConstraint1.msg" "hyperLayout1.hyp[136].dn"
		;
connectAttr "unitConversion7.msg" "hyperLayout1.hyp[137].dn";
connectAttr "unitConversion8.msg" "hyperLayout1.hyp[138].dn";
connectAttr "unitConversion9.msg" "hyperLayout1.hyp[139].dn";
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleX.msg" "hyperLayout1.hyp[140].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleY.msg" "hyperLayout1.hyp[141].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_trueScaleZ.msg" "hyperLayout1.hyp[142].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleX.msg" "hyperLayout1.hyp[143].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleY.msg" "hyperLayout1.hyp[144].dn"
		;
connectAttr "st_YKR412_0380:YKR412_038_01_GlobalSRT_BG_focal_trueScaleZ.msg" "hyperLayout1.hyp[145].dn"
		;
connectAttr "imagePlaneAlphaFactor.msg" "hyperLayout1.hyp[146].dn";
connectAttr "depthCorrection.msg" "hyperLayout1.hyp[147].dn";
connectAttr "Global_SRT_parentConstraint1.msg" "hyperLayout1.hyp[148].dn";
connectAttr "Global_SRT_parentConstraint2.msg" "hyperLayout1.hyp[149].dn";
connectAttr "clnLyW_root_rotateX.msg" "hyperLayout1.hyp[150].dn";
connectAttr "clnLyW_root_rotateY.msg" "hyperLayout1.hyp[151].dn";
connectAttr "clnLyW_root_rotateZ.msg" "hyperLayout1.hyp[152].dn";
connectAttr "clnLyW_body_rotateX.msg" "hyperLayout1.hyp[153].dn";
connectAttr "clnLyW_body_rotateY.msg" "hyperLayout1.hyp[154].dn";
connectAttr "clnLyW_body_rotateZ.msg" "hyperLayout1.hyp[155].dn";
connectAttr "clnLyW_chest_rotateX.msg" "hyperLayout1.hyp[156].dn";
connectAttr "clnLyW_chest_rotateY.msg" "hyperLayout1.hyp[157].dn";
connectAttr "clnLyW_chest_rotateZ.msg" "hyperLayout1.hyp[158].dn";
connectAttr "clnLyW_arm_L_rotateX.msg" "hyperLayout1.hyp[159].dn";
connectAttr "clnLyW_arm_L_rotateY.msg" "hyperLayout1.hyp[160].dn";
connectAttr "clnLyW_arm_L_rotateZ.msg" "hyperLayout1.hyp[161].dn";
connectAttr "clnLyW_forearm_L_rotateX.msg" "hyperLayout1.hyp[162].dn";
connectAttr "clnLyW_forearm_L_rotateY.msg" "hyperLayout1.hyp[163].dn";
connectAttr "clnLyW_forearm_L_rotateZ.msg" "hyperLayout1.hyp[164].dn";
connectAttr "clnLyW_hand_L_rotateX.msg" "hyperLayout1.hyp[165].dn";
connectAttr "clnLyW_hand_L_rotateY.msg" "hyperLayout1.hyp[166].dn";
connectAttr "clnLyW_hand_L_rotateZ.msg" "hyperLayout1.hyp[167].dn";
connectAttr "clnLyW_arm_R_rotateX.msg" "hyperLayout1.hyp[168].dn";
connectAttr "clnLyW_arm_R_rotateY.msg" "hyperLayout1.hyp[169].dn";
connectAttr "clnLyW_arm_R_rotateZ.msg" "hyperLayout1.hyp[170].dn";
connectAttr "clnLyW_forearm_R_rotateX.msg" "hyperLayout1.hyp[171].dn";
connectAttr "clnLyW_forearm_R_rotateY.msg" "hyperLayout1.hyp[172].dn";
connectAttr "clnLyW_forearm_R_rotateZ.msg" "hyperLayout1.hyp[173].dn";
connectAttr "clnLyW_hand_R_rotateX.msg" "hyperLayout1.hyp[174].dn";
connectAttr "clnLyW_hand_R_rotateY.msg" "hyperLayout1.hyp[175].dn";
connectAttr "clnLyW_hand_R_rotateZ.msg" "hyperLayout1.hyp[176].dn";
connectAttr "clnLyW_neck_rotateX.msg" "hyperLayout1.hyp[177].dn";
connectAttr "clnLyW_neck_rotateY.msg" "hyperLayout1.hyp[178].dn";
connectAttr "clnLyW_neck_rotateZ.msg" "hyperLayout1.hyp[179].dn";
connectAttr "clnLyW_head_rotateX.msg" "hyperLayout1.hyp[180].dn";
connectAttr "clnLyW_head_rotateY.msg" "hyperLayout1.hyp[181].dn";
connectAttr "clnLyW_head_rotateZ.msg" "hyperLayout1.hyp[182].dn";
connectAttr "clnLyW_cloth_01_rotateX.msg" "hyperLayout1.hyp[183].dn";
connectAttr "clnLyW_cloth_01_rotateY.msg" "hyperLayout1.hyp[184].dn";
connectAttr "clnLyW_cloth_01_rotateZ.msg" "hyperLayout1.hyp[185].dn";
connectAttr "clnLyW_cloth_02_rotateX.msg" "hyperLayout1.hyp[186].dn";
connectAttr "clnLyW_cloth_02_rotateY.msg" "hyperLayout1.hyp[187].dn";
connectAttr "clnLyW_cloth_02_rotateZ.msg" "hyperLayout1.hyp[188].dn";
connectAttr "clnLyW_leg_L_rotateX.msg" "hyperLayout1.hyp[189].dn";
connectAttr "clnLyW_leg_L_rotateY.msg" "hyperLayout1.hyp[190].dn";
connectAttr "clnLyW_leg_L_rotateZ.msg" "hyperLayout1.hyp[191].dn";
connectAttr "clnLyW_foreleg_L_rotateX.msg" "hyperLayout1.hyp[192].dn";
connectAttr "clnLyW_foreleg_L_rotateY.msg" "hyperLayout1.hyp[193].dn";
connectAttr "clnLyW_foreleg_L_rotateZ.msg" "hyperLayout1.hyp[194].dn";
connectAttr "clnLyW_foot_L_rotateX.msg" "hyperLayout1.hyp[195].dn";
connectAttr "clnLyW_foot_L_rotateY.msg" "hyperLayout1.hyp[196].dn";
connectAttr "clnLyW_foot_L_rotateZ.msg" "hyperLayout1.hyp[197].dn";
connectAttr "clnLyW_leg_R_rotateX.msg" "hyperLayout1.hyp[198].dn";
connectAttr "clnLyW_leg_R_rotateY.msg" "hyperLayout1.hyp[199].dn";
connectAttr "clnLyW_leg_R_rotateZ.msg" "hyperLayout1.hyp[200].dn";
connectAttr "clnLyW_foreleg_R_rotateX.msg" "hyperLayout1.hyp[201].dn";
connectAttr "clnLyW_foreleg_R_rotateY.msg" "hyperLayout1.hyp[202].dn";
connectAttr "clnLyW_foreleg_R_rotateZ.msg" "hyperLayout1.hyp[203].dn";
connectAttr "clnLyW_foot_R_rotateX.msg" "hyperLayout1.hyp[204].dn";
connectAttr "clnLyW_foot_R_rotateY.msg" "hyperLayout1.hyp[205].dn";
connectAttr "clnLyW_foot_R_rotateZ.msg" "hyperLayout1.hyp[206].dn";
connectAttr "clnLyW_root_visibility.msg" "hyperLayout1.hyp[207].dn";
connectAttr "clnLyW_root_translateX.msg" "hyperLayout1.hyp[208].dn";
connectAttr "clnLyW_root_translateY.msg" "hyperLayout1.hyp[209].dn";
connectAttr "clnLyW_root_translateZ.msg" "hyperLayout1.hyp[210].dn";
connectAttr "clnLyW_root_scaleX.msg" "hyperLayout1.hyp[211].dn";
connectAttr "clnLyW_root_scaleY.msg" "hyperLayout1.hyp[212].dn";
connectAttr "clnLyW_root_scaleZ.msg" "hyperLayout1.hyp[213].dn";
connectAttr "clnLyW_body_visibility.msg" "hyperLayout1.hyp[214].dn";
connectAttr "clnLyW_body_translateX.msg" "hyperLayout1.hyp[215].dn";
connectAttr "clnLyW_body_translateY.msg" "hyperLayout1.hyp[216].dn";
connectAttr "clnLyW_body_translateZ.msg" "hyperLayout1.hyp[217].dn";
connectAttr "clnLyW_body_scaleX.msg" "hyperLayout1.hyp[218].dn";
connectAttr "clnLyW_body_scaleY.msg" "hyperLayout1.hyp[219].dn";
connectAttr "clnLyW_body_scaleZ.msg" "hyperLayout1.hyp[220].dn";
connectAttr "clnLyW_chest_visibility.msg" "hyperLayout1.hyp[221].dn";
connectAttr "clnLyW_chest_translateX.msg" "hyperLayout1.hyp[222].dn";
connectAttr "clnLyW_chest_translateY.msg" "hyperLayout1.hyp[223].dn";
connectAttr "clnLyW_chest_translateZ.msg" "hyperLayout1.hyp[224].dn";
connectAttr "clnLyW_chest_scaleX.msg" "hyperLayout1.hyp[225].dn";
connectAttr "clnLyW_chest_scaleY.msg" "hyperLayout1.hyp[226].dn";
connectAttr "clnLyW_chest_scaleZ.msg" "hyperLayout1.hyp[227].dn";
connectAttr "clnLyW_neck_visibility.msg" "hyperLayout1.hyp[228].dn";
connectAttr "clnLyW_neck_translateX.msg" "hyperLayout1.hyp[229].dn";
connectAttr "clnLyW_neck_translateY.msg" "hyperLayout1.hyp[230].dn";
connectAttr "clnLyW_neck_translateZ.msg" "hyperLayout1.hyp[231].dn";
connectAttr "clnLyW_neck_scaleX.msg" "hyperLayout1.hyp[232].dn";
connectAttr "clnLyW_neck_scaleY.msg" "hyperLayout1.hyp[233].dn";
connectAttr "clnLyW_neck_scaleZ.msg" "hyperLayout1.hyp[234].dn";
connectAttr "clnLyW_head_visibility.msg" "hyperLayout1.hyp[235].dn";
connectAttr "clnLyW_head_translateX.msg" "hyperLayout1.hyp[236].dn";
connectAttr "clnLyW_head_translateY.msg" "hyperLayout1.hyp[237].dn";
connectAttr "clnLyW_head_translateZ.msg" "hyperLayout1.hyp[238].dn";
connectAttr "clnLyW_head_scaleX.msg" "hyperLayout1.hyp[239].dn";
connectAttr "clnLyW_head_scaleY.msg" "hyperLayout1.hyp[240].dn";
connectAttr "clnLyW_head_scaleZ.msg" "hyperLayout1.hyp[241].dn";
connectAttr "clnLyW_arm_R_visibility.msg" "hyperLayout1.hyp[242].dn";
connectAttr "clnLyW_arm_R_translateX.msg" "hyperLayout1.hyp[243].dn";
connectAttr "clnLyW_arm_R_translateY.msg" "hyperLayout1.hyp[244].dn";
connectAttr "clnLyW_arm_R_translateZ.msg" "hyperLayout1.hyp[245].dn";
connectAttr "clnLyW_arm_R_scaleX.msg" "hyperLayout1.hyp[246].dn";
connectAttr "clnLyW_arm_R_scaleY.msg" "hyperLayout1.hyp[247].dn";
connectAttr "clnLyW_arm_R_scaleZ.msg" "hyperLayout1.hyp[248].dn";
connectAttr "clnLyW_forearm_R_visibility.msg" "hyperLayout1.hyp[249].dn";
connectAttr "clnLyW_forearm_R_translateX.msg" "hyperLayout1.hyp[250].dn";
connectAttr "clnLyW_forearm_R_translateY.msg" "hyperLayout1.hyp[251].dn";
connectAttr "clnLyW_forearm_R_translateZ.msg" "hyperLayout1.hyp[252].dn";
connectAttr "clnLyW_forearm_R_scaleX.msg" "hyperLayout1.hyp[253].dn";
connectAttr "clnLyW_forearm_R_scaleY.msg" "hyperLayout1.hyp[254].dn";
connectAttr "clnLyW_forearm_R_scaleZ.msg" "hyperLayout1.hyp[255].dn";
connectAttr "clnLyW_hand_R_visibility.msg" "hyperLayout1.hyp[256].dn";
connectAttr "clnLyW_hand_R_translateX.msg" "hyperLayout1.hyp[257].dn";
connectAttr "clnLyW_hand_R_translateY.msg" "hyperLayout1.hyp[258].dn";
connectAttr "clnLyW_hand_R_translateZ.msg" "hyperLayout1.hyp[259].dn";
connectAttr "clnLyW_hand_R_scaleX.msg" "hyperLayout1.hyp[260].dn";
connectAttr "clnLyW_hand_R_scaleY.msg" "hyperLayout1.hyp[261].dn";
connectAttr "clnLyW_hand_R_scaleZ.msg" "hyperLayout1.hyp[262].dn";
connectAttr "clnLyW_arm_L_visibility.msg" "hyperLayout1.hyp[263].dn";
connectAttr "clnLyW_arm_L_translateX.msg" "hyperLayout1.hyp[264].dn";
connectAttr "clnLyW_arm_L_translateY.msg" "hyperLayout1.hyp[265].dn";
connectAttr "clnLyW_arm_L_translateZ.msg" "hyperLayout1.hyp[266].dn";
connectAttr "clnLyW_arm_L_scaleX.msg" "hyperLayout1.hyp[267].dn";
connectAttr "clnLyW_arm_L_scaleY.msg" "hyperLayout1.hyp[268].dn";
connectAttr "clnLyW_arm_L_scaleZ.msg" "hyperLayout1.hyp[269].dn";
connectAttr "clnLyW_forearm_L_visibility.msg" "hyperLayout1.hyp[270].dn";
connectAttr "clnLyW_forearm_L_translateX.msg" "hyperLayout1.hyp[271].dn";
connectAttr "clnLyW_forearm_L_translateY.msg" "hyperLayout1.hyp[272].dn";
connectAttr "clnLyW_forearm_L_translateZ.msg" "hyperLayout1.hyp[273].dn";
connectAttr "clnLyW_forearm_L_scaleX.msg" "hyperLayout1.hyp[274].dn";
connectAttr "clnLyW_forearm_L_scaleY.msg" "hyperLayout1.hyp[275].dn";
connectAttr "clnLyW_forearm_L_scaleZ.msg" "hyperLayout1.hyp[276].dn";
connectAttr "clnLyW_hand_L_visibility.msg" "hyperLayout1.hyp[277].dn";
connectAttr "clnLyW_hand_L_translateX.msg" "hyperLayout1.hyp[278].dn";
connectAttr "clnLyW_hand_L_translateY.msg" "hyperLayout1.hyp[279].dn";
connectAttr "clnLyW_hand_L_translateZ.msg" "hyperLayout1.hyp[280].dn";
connectAttr "clnLyW_hand_L_scaleX.msg" "hyperLayout1.hyp[281].dn";
connectAttr "clnLyW_hand_L_scaleY.msg" "hyperLayout1.hyp[282].dn";
connectAttr "clnLyW_hand_L_scaleZ.msg" "hyperLayout1.hyp[283].dn";
connectAttr "clnLyW_cloth_01_visibility.msg" "hyperLayout1.hyp[284].dn";
connectAttr "clnLyW_cloth_01_translateX.msg" "hyperLayout1.hyp[285].dn";
connectAttr "clnLyW_cloth_01_translateY.msg" "hyperLayout1.hyp[286].dn";
connectAttr "clnLyW_cloth_01_translateZ.msg" "hyperLayout1.hyp[287].dn";
connectAttr "clnLyW_cloth_01_scaleX.msg" "hyperLayout1.hyp[288].dn";
connectAttr "clnLyW_cloth_01_scaleY.msg" "hyperLayout1.hyp[289].dn";
connectAttr "clnLyW_cloth_01_scaleZ.msg" "hyperLayout1.hyp[290].dn";
connectAttr "clnLyW_cloth_02_visibility.msg" "hyperLayout1.hyp[291].dn";
connectAttr "clnLyW_cloth_02_translateX.msg" "hyperLayout1.hyp[292].dn";
connectAttr "clnLyW_cloth_02_translateY.msg" "hyperLayout1.hyp[293].dn";
connectAttr "clnLyW_cloth_02_translateZ.msg" "hyperLayout1.hyp[294].dn";
connectAttr "clnLyW_cloth_02_scaleX.msg" "hyperLayout1.hyp[295].dn";
connectAttr "clnLyW_cloth_02_scaleY.msg" "hyperLayout1.hyp[296].dn";
connectAttr "clnLyW_cloth_02_scaleZ.msg" "hyperLayout1.hyp[297].dn";
connectAttr "clnLyW_leg_L_visibility.msg" "hyperLayout1.hyp[298].dn";
connectAttr "clnLyW_leg_L_translateX.msg" "hyperLayout1.hyp[299].dn";
connectAttr "clnLyW_leg_L_translateY.msg" "hyperLayout1.hyp[300].dn";
connectAttr "clnLyW_leg_L_translateZ.msg" "hyperLayout1.hyp[301].dn";
connectAttr "clnLyW_leg_L_scaleX.msg" "hyperLayout1.hyp[302].dn";
connectAttr "clnLyW_leg_L_scaleY.msg" "hyperLayout1.hyp[303].dn";
connectAttr "clnLyW_leg_L_scaleZ.msg" "hyperLayout1.hyp[304].dn";
connectAttr "clnLyW_foreleg_L_visibility.msg" "hyperLayout1.hyp[305].dn";
connectAttr "clnLyW_foreleg_L_translateX.msg" "hyperLayout1.hyp[306].dn";
connectAttr "clnLyW_foreleg_L_translateY.msg" "hyperLayout1.hyp[307].dn";
connectAttr "clnLyW_foreleg_L_translateZ.msg" "hyperLayout1.hyp[308].dn";
connectAttr "clnLyW_foreleg_L_scaleX.msg" "hyperLayout1.hyp[309].dn";
connectAttr "clnLyW_foreleg_L_scaleY.msg" "hyperLayout1.hyp[310].dn";
connectAttr "clnLyW_foreleg_L_scaleZ.msg" "hyperLayout1.hyp[311].dn";
connectAttr "clnLyW_foot_L_visibility.msg" "hyperLayout1.hyp[312].dn";
connectAttr "clnLyW_foot_L_translateX.msg" "hyperLayout1.hyp[313].dn";
connectAttr "clnLyW_foot_L_translateY.msg" "hyperLayout1.hyp[314].dn";
connectAttr "clnLyW_foot_L_translateZ.msg" "hyperLayout1.hyp[315].dn";
connectAttr "clnLyW_foot_L_scaleX.msg" "hyperLayout1.hyp[316].dn";
connectAttr "clnLyW_foot_L_scaleY.msg" "hyperLayout1.hyp[317].dn";
connectAttr "clnLyW_foot_L_scaleZ.msg" "hyperLayout1.hyp[318].dn";
connectAttr "clnLyW_leg_R_visibility.msg" "hyperLayout1.hyp[319].dn";
connectAttr "clnLyW_leg_R_translateX.msg" "hyperLayout1.hyp[320].dn";
connectAttr "clnLyW_leg_R_translateY.msg" "hyperLayout1.hyp[321].dn";
connectAttr "clnLyW_leg_R_translateZ.msg" "hyperLayout1.hyp[322].dn";
connectAttr "clnLyW_leg_R_scaleX.msg" "hyperLayout1.hyp[323].dn";
connectAttr "clnLyW_leg_R_scaleY.msg" "hyperLayout1.hyp[324].dn";
connectAttr "clnLyW_leg_R_scaleZ.msg" "hyperLayout1.hyp[325].dn";
connectAttr "clnLyW_foreleg_R_visibility.msg" "hyperLayout1.hyp[326].dn";
connectAttr "clnLyW_foreleg_R_translateX.msg" "hyperLayout1.hyp[327].dn";
connectAttr "clnLyW_foreleg_R_translateY.msg" "hyperLayout1.hyp[328].dn";
connectAttr "clnLyW_foreleg_R_translateZ.msg" "hyperLayout1.hyp[329].dn";
connectAttr "clnLyW_foreleg_R_scaleX.msg" "hyperLayout1.hyp[330].dn";
connectAttr "clnLyW_foreleg_R_scaleY.msg" "hyperLayout1.hyp[331].dn";
connectAttr "clnLyW_foreleg_R_scaleZ.msg" "hyperLayout1.hyp[332].dn";
connectAttr "clnLyW_foot_R_visibility.msg" "hyperLayout1.hyp[333].dn";
connectAttr "clnLyW_foot_R_translateX.msg" "hyperLayout1.hyp[334].dn";
connectAttr "clnLyW_foot_R_translateY.msg" "hyperLayout1.hyp[335].dn";
connectAttr "clnLyW_foot_R_translateZ.msg" "hyperLayout1.hyp[336].dn";
connectAttr "clnLyW_foot_R_scaleX.msg" "hyperLayout1.hyp[337].dn";
connectAttr "clnLyW_foot_R_scaleY.msg" "hyperLayout1.hyp[338].dn";
connectAttr "clnLyW_foot_R_scaleZ.msg" "hyperLayout1.hyp[339].dn";
connectAttr "sceneConfigurationScriptNode.msg" "hyperLayout1.hyp[341].dn";
connectAttr "sequencer1.msg" ":sequenceManager1.seqts[0]";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
dataStructure -fmt "raw" -as "name=externalContentTable:string=node:string=key:string=upath:uint32=upathcrc:string=rpath:string=roles";
applyMetadata -fmt "raw" -v "channel\nname externalContentTable\nstream\nname v1.0\nindexType numeric\nstructure externalContentTable\n0\n\"pr_arr03RN\" \"\" \"$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/pr/pr_arr03/rig/pr_arr03_rig.ma\" 4202899282 \"Y:/01_SAISON_4/08_ASSETS/3D/pr/pr_arr03/rig/pr_arr03_rig.ma\" \"FileRef\"\n1\n\"pr_bow05RN\" \"\" \"$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/pr/pr_bow05/rig/pr_bow05_rig.ma\" 3582197380 \"Y:/01_SAISON_4/08_ASSETS/3D/pr/pr_bow05/rig/pr_bow05_rig.ma\" \"FileRef\"\n2\n\"st_YKR412_0380RN\" \"\" \"$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/st/st_412_0380/rig/st_YKR412_0380_rig.ma\" 3882763989 \"Y:/01_SAISON_4/08_ASSETS/3D/st/st_412_0380/rig/st_YKR412_0380_rig.ma\" \"FileRef\"\n3\n\"ch_wildwRN\" \"\" \"$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/ch/ch_wildw/low/ch_wildw_low.ma\" 3500536803 \"Y:/01_SAISON_4/08_ASSETS/3D/ch/ch_wildw/low/ch_wildw_low.ma\" \"FileRef\"\n4\n\"SH038_CAMRN\" \"\" \"$PROD_SERVER/01_SAISON_4/08_ASSETS/3D/cam/yak_camera.ma\" 837872098 \"Y:/01_SAISON_4/08_ASSETS/3D/cam/yak_camera.ma\" \"FileRef\"\n5\n\"|__CAMERA__|sh038ImagePlane|sh038ImagePlaneShape\" \"imageName\" \"$PROD_SERVER/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR412/animatic/panels/edit_01/YKR_412_038_01.jpg\" 2517428784 \"Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR412/animatic/panels/edit_01/YKR_412_038_01.jpg\" \"fileSequence;sourceImages\"\n6\n\"sh038Audio\" \"filename\" \"$PROD_SERVER/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR412/animatic/wav/YKR412_038.wav\" 213379842 \"Y:/01_SAISON_4/09_EPISODES/04_Fabrication_3D/YKR412/animatic/wav/YKR412_038.wav\" \"audio\"\nendStream\nendChannel\nendAssociations\n" 
		-scn;
// End of YKR412_038_lay_001.ma
