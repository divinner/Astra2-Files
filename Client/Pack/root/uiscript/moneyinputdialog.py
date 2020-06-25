import uiScriptLocale

window = {
	"name" : "InputDialog",

	"x" : 0,
	"y" : 0,

	"style" : ["movable", "float",],

	"width" : 200,
	"height" : 110,

	"children" :
	[
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 200,
			"height" : 110,

			"title" : "",

			"children" :
			[

				## Input Slot
				{
					"name" : "InputSlot",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"children" :
					[
						{
							"name" : "InputValue",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					],
				},

				## Input Slot
				{
					"name" : "MoneyValue",
					"type" : "text",

					"x" : 0,
					"y" : 59,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},

				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : - 61 - 5 + 30,
					"y" : 78,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 5 + 30,
					"y" : 78,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			],
		},
	],
}

if ENABLE_OFFLINE_PRIVATE_SHOP:
	window["height"] += 15
	window["children"][0]["height"] += 15
	window["children"][0]["children"][2]["y"] += 15
	window["children"][0]["children"][3]["y"] += 15
	window["children"][0]["children"] += [
				{
					"name" : "minText",
					"type" : "text",

					"x" : -71 - 5 + 30,
					"y" : 74,
					"text" : "Min: Yok",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				{
					"name" : "maxText",
					"type" : "text",

					"x" : 5 + 40,
					"y" : 74,
					"text" : "Max: Yok",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},]

