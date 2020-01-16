from sklearn. metrics import r2_score
from numpy import percentile
from math import isnan
from statistics import mean

def criterionA(truth, pred):
	if pred <= truth*1.1 +5 and pred >= truth*0.9 -5:
		return True
	else:
		return False

#Outputs indicators from the true values and predicted values
def benchmark(ytrue, ypred, criteria = None):
	'''benchmark outputs different values depending on the true values and
	the predicted ones. It also outputs an array containing the different ratios
	of (true,pred) values that make the different criteria true'''
	
	som =0
	relatsom =0.0
	errs = []
	relaterrs = []
	somcrits = [[] for _ in criteria]
	
	for truth, pred in zip(ytrue, ypred):
	
		err = abs(truth-pred)
		if (truth==0 and pred==0):
			relaterr=0
		else:
			relaterr=err/((float(truth)+float(pred))/float(2))
			
		#ADDING ERROR TO VARIABLES
		som = som + err
		errs.append(err)
		
		relatsom = relatsom+relaterr
		relaterrs.append(relaterr)
		
		if criteria:
			for cr,somcrit in zip(criteria,somcrits):
				if cr(truth, pred):
					somcrit.append(1)
				else:
					somcrit.append(0)
	
	#RETURN VALUES:	
	r2= r2_score(ytrue, ypred)

	moyerr = som/len(ytrue)
	
	relatmoyerr = relatsom/len(ytrue)

	deciles = percentile(errs, range(0,101,10))
	
	relatdeciles = percentile(relaterrs, range(0,101,10))
	
	if criteria:
		ratiocrits = [mean(s) for s in somcrits]
	else:
		ratiocrits= None
	return(r2, moyerr,relatmoyerr, deciles,relatdeciles, ratiocrits)
	
def benchmark_print(bmresult):
	print('R2 SCORE: ' + str(bmresult[0]))
	print('AVRG ERROR (RAW): ' +str(bmresult[1]))
	print('AVRG ERROR (RELAT): ' +str(bmresult[2]))
	print('DECILES OF ERROR (RAW): ')
	print(bmresult[3])
	print('DECILES OF ERROR (RELAT): ')
	print(bmresult[4])
	if bmresult[5]:
		print('RATIO OF VALUES THAT VALIDATE THE CRITERIA: ')
		print(bmresult[5])
