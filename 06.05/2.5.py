end_dict = {}


data = [
	{
		2: "Kirsten Cherry"
	},
	{
		1: "Leigh Emerson"
	},
	{
		"third": "Kaseem Holt"
	},
	{
		'four': "Henry Padilla"
	},
	{
		'fifty': "Ivor Padilla"
	}
]
for k, v in data.items():
	if k in end_dict:
		end_dict[k].extend(v)
	else:
		end_dict[k] = v
print(end_dict)
