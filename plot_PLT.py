import matplotlib.pyplot as plt
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
import numpy as np 
import sys

plt.rcParams['text.latex.preamble']=[r'\boldmath']
params = {
		  'font.size' : 20,
		  'legend.fontsize': 18,
		  'text.latex.unicode': True,
		  }
plt.rcParams.update(params)

plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

def simplify_cdf(data):
	'''Return the cdf and data to plot
		Remove unnecessary points in the CDF in case of repeated data
		'''
	data_len = len(data)
	assert data_len != 0
	cdf = np.arange(data_len) / data_len
	simple_cdf = [0]
	simple_data = [data[0]]

	if data_len > 1:
		simple_cdf.append(1.0 / data_len)
		simple_data.append(data[1])
		for cdf_value, data_value in zip(cdf, data):
			if data_value == simple_data[-1]:
				simple_cdf[-1] = cdf_value
			else:
				simple_cdf.append(cdf_value)
				simple_data.append(data_value)
	assert len(simple_cdf) == len(simple_data)
	# to have cdf up to 1
	simple_cdf.append(1)
	simple_data.append(data[-1])

	return simple_cdf, simple_data

def cdfplot(data_in):
	"""Plot the cdf of a data array
		Wrapper to call the plot method of axes
		"""
	# cannot shortcut lambda, otherwise it will drop values at 0
	data = sorted(filter(lambda x: (x is not None and ~np.isnan(x)
									and ~np.isinf(x)),
						 data_in))

	data_len = len(data)
	if data_len == 0:
		return

	simple_cdf, simple_data = simplify_cdf(data)
	return simple_data, simple_cdf


# PLT1 = [1,23,44,45,33,2,2,9,10,15]
# PLT2 = [11,12,55,34,33,20,12,20,15]

#Page Load Time
# PLT1 = ["3702", "3737", "13790", "15967", "15256", "6047", "27984", "18622", "166", "73806", "15580", "18016", "16676", "43595", "20455", "6867", "1663", "6941", "3274", "11177", "19221", "7175", "19883", "103380", "13558", "14135", "11243", "11418", "20855", "14232", "29703", "13085", "5643", "5495", "4625", "6385", "1521", "4605", "14357", "6186", "87295", "7124", "1464", "6295", "9815", "15692", "9485", "6578", "3266", "18144", "4057", "17067", "11166", "5209", "37482", "93794", "20890", "19591", "22604", "4438", "27977", "92", "14114", "30451", "96873", "7225", "43296", "108", "10203"]
# PLT2 = ["1004", "2660", "8262", "9880", "12800", "1828", "27385", "5478", "111", "6900", "12255", "9088", "8671", "23941", "16330", "463", "416", "3983", "1448", "5114", "14618", "4228", "16365", "6994", "5212", "6919", "10507", "6414", "14283", "2776", "11456", "10426", "5373", "2472", "3065", "2430", "406", "2582", "5347", "479", "14851", "5865", "643", "4142", "4697", "13280", "4854", "3481", "2100", "13019", "2910", "12254", "4640", "4490", "5321", "3295", "5046", "8861", "10871", "2005", "19043", "37224", "11293", "18922", "19486", "1929", "24385", "130", "5684"]

#Page Size
PLT1 = ["5557", "46461", "17532", "96893", "92365", "17203", "19780", "13137", "0", "13165", "15224", "61135", "11672", "7057", "17637", "6586", "1393", "13875", "2718", "33634", "4687", "8078", "11637", "7285", "73343", "7285", "49464", "9522", "39863", "8647", "26854", "18707", "4571", "3327", "8098", "7052", "1309", "3703", "7212", "0", "12391", "12363", "473", "8494", "426159", "16964", "24824", "293903", "8313", "36209", "3334", "19675", "3588", "7464", "43628", "26213", "33575", "13029", "11806", "46043", "28927", "0", "119656", "11350", "23541", "7409", "20341", "0", "71303"]
PLT2 = ["5444", "15689", "17183", "96881", "89657", "0", "19780", "0", "0", "13049", "15226", "578", "11018", "6608", "17632", "0", "1393", "13534", "2718", "32811", "4687", "8092", "11481", "7285", "73377", "7284", "49256", "9243", "390", "8647", "26852", "18470", "4572", "0", "230", "7165", "0", "3646", "0", "0", "12408", "11613", "473", "8305", "426980", "16134", "24958", "293870", "8210", "0", "3386", "18173", "0", "44380", "42766", "25630", "32660", "12881", "0", "16089", "28921", "3448", "118445", "0", "23530", "7351", "20160", "0", "71167"]

#Num of resources
# PLT1 = ["7", "12", "24", "50", "39", "13", "120", "65", "0", "39", "96", "34", "64", "84", "89", "6", "0", "13", "5", "24", "41", "23", "71", "58", "35", "58", "60", "42", "97", "20", "81", "112", "24", "27", "7", "14", "3", "28", "30", "0", "148", "37", "0", "31", "15", "85", "41", "16", "19", "139", "16", "104", "44", "6", "64", "17", "24", "85", "85", "12", "250", "0", "99", "100", "194", "7", "138", "0", "34"]
# PLT2 = ["5", "7", "17", "31", "75", "6", "84", "43", "0", "14", "69", "29", "43", "11", "80", "0", "0", "13", "2", "25", "31", "17", "56", "21", "26", "20", "61", "14", "69", "7", "61", "97", "19", "20", "6", "7", "0", "11", "22", "1", "127", "23", "0", "29", "7", "78", "31", "5", "7", "138", "10", "88", "27", "12", "30", "9", "23", "29", "61", "7", "170", "111", "52", "48", "145", "3", "100", "0", "21"]

PLT1 = [int(ele) for ele in PLT1]
PLT2 = [int(ele) for ele in PLT2]

PLT1 = [(ele/1000) for ele in PLT1]
PLT2 = [(ele/1000) for ele in PLT2]

fig = plt.figure(1, figsize=(8,6), facecolor="w")
ax = plt.subplot(111)

simple_data, simple_cdf = cdfplot(PLT1)
plt.plot(simple_data, simple_cdf, 'r', label="Original", linewidth=3)
simple_data, simple_cdf = cdfplot(PLT2)
plt.plot(simple_data, simple_cdf, 'b', label="Simplified", linewidth=3)

plt.legend(loc='upper left')
plt.xlabel("Page Size (kB)")
plt.ylabel("CDF")

plt.xlim([0,max(max(PLT1),max(PLT2))])
plt.ylim([0,1])

plt.grid()
plt.tight_layout()


fig.savefig('page_size.pdf', dpi=300)
plt.close(fig)

