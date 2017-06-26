import numpy as np
import matplotlib.pyplot as plt

def evol_time(time,RA,DEC,PMRA,PMDEC):
	'''
	This function calculates the position of the star using proper motion 
	''' 
	
	RA_pred = (RA/1000.0 + PMRA*time)*1000.0
	DEC_pred = (DEC/1000.0 + PMDEC*time)*1000.0
	
	return RA_pred,DEC_pred
	
def get_error(sigra,sigdec,pmraerr,pmdecerr):
	
	delta_a = np.sqrt(sigra**2+15**2*pmraerr**2)
	delta_b = np.sqrt(sigdec**2+15**2*pmdecerr**2)
	delta_a_mean = np.mean(delta_a)
	delta_b_mean = np.mean(delta_b)
	print delta_a_mean
	print delta_b_mean
	return delta_a_mean,delta_b_mean	

def compare(RA_pred,DEC_pred,ID_Tgas,RA_Tgas,DEC_Tgas,delta_a,delta_b,match1,match2,match3):
	num_pred = len(RA_pred) #number of elements with predicted position
	num_tgas = len(RA_Tgas) #number of elements from tgas to compare
	
	
	tag = range(0,num_pred)

	c = list(zip(RA_pred, DEC_pred, tag))
	sorted(c)
	RA_pred, DEC_pred, tag = zip(*c)
	
	index = []
	index_val = []
	for i in range(0,70000,10000):
		index_val.append(RA_pred[i])
		index.append(i)
				
	for i in range(0,num_tgas):
		ra = RA_Tgas[i]
		dec = DEC_Tgas[i]
		for k in range(0,6):
			if(ra >= index_val[k] and ra <= index_val[k+1]):
				ini = index[k]
				fin = index[k+1]
		if(ra >= index_val[6]):
			ini = index[6]
			fin = num_pred
					
		for j in range(ini,fin):
			if(abs(ra-RA_pred[j]) < delta_a and abs(dec-DEC_pred[j]) < delta_b):
				if(match1[tag[j]] == 0):
					match1[tag[j]] = ID_Tgas[i]
				elif(match2[tag[j]] == 0):	
					match2[tag[j]] = ID_Tgas[i]
				elif(match3[tag[j]] == 0):
					match3[tag[j]] = ID_Tgas[i]
				else:
					print 'More than 3 matches'
	return match1,match2,match3
