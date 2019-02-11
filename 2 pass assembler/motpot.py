mot = {
	"la": {
		"type": "rx", 
		"length": 4,
		"binary" : 56	
	},
	
	"sr":{
		"type" : "rr",
		"length": 2,
		"binary" : 56	
	},

	"l":{
		"type" : "rx",
		"length": 4,
		"binary" : 12
	},
		
	"ar":{
		"type" : "rr",
		"length": 2,
		"binary" : 12
	},
	
	"a":{
		"type" : "rx",
		"length": 4,
		"binary" : 12
	},
	"st":{
		"type" : "rx",
		"length": 4,
		"binary" : 12
	},
	
	"c":{
		"type" : "rx",
		"length": 4,
		"binary" : 12
	},

	"lr":{
		"type" : "rr",
		"length": 2,
		"binary" : 12
	},
	
	"br":{
		"type" : "rr",
		"length": 2,
		"binary" : 12,
		"mask": 15
	},
	"bne":{
		"type" : "rx",
		"length": 4,
		"binary" : 12,
		"mask": 7
	}
}

pot = [
    "using",
      "start",
      "equ",
      "ltorg",
      "drop",
      "end",
      "dc",
      "ds"
]


