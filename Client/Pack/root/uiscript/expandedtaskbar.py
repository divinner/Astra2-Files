import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"

Y_ADD_POSITION = 0
window = {
	"name" : "ExpandTaskBar",

	"x" : SCREEN_WIDTH/2 - 5,
	"y" : SCREEN_HEIGHT - 74,

	"width" : 37,
	"height" : 37,

	"children" :
	[
		{
			"name" : "ExpanedTaskBar_Board",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 37,
			"height" : 37,

			"children" :
			[
				{
					"name" : "DragonSoulButton",
					"type" : "button",

					"x" : 0,
					"y" : 0,

					"width" : 37,
					"height" : 37,

					"tooltip_text" : uiScriptLocale.TASKBAR_DISABLE,

					"default_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_03.tga",
				},
			],
		},
	],
}

if ENABLE_GROWTH_PET_SYSTEM:
	window["width"] = 37*3
	window["children"][0]["width"] = window["children"][0]["width"] + 37
	window["children"][0]["children"] = window["children"][0]["children"] + [
					{
						"name" : "PetInfoButton",
						"type" : "button",
						"style" : ("ltr", ),

						"x" : 74,
						"y" : 0,

						"width" : 37,
						"height" : 37,

						"tooltip_text" : uiScriptLocale.TASKBAR_DISABLE,
								
						"default_image" : "d:/ymir work/ui/pet/TaskBar_Pet_Button_01.tga",
						"over_image" : "d:/ymir work/ui/pet/TaskBar_Pet_Button_02.tga",
						"down_image" : "d:/ymir work/ui/pet/TaskBar_Pet_Button_03.tga",
					},]

