from astropy.io import fits

def import_fits_data(name):
	'''
	This function opens the fit file. It can be use to analize what is inside the file.
	'''
	hdulist = fits.open(name)
	
	#to get information of the file
	#hdulist.info() #gives number and info of hdu objects in file
	#print(hdulist[1].columns.info)
	#hdulist[1].header['comment'] #gives comment on the hdu selected
	#print(hdulist[1].columns) #if hdulist is data, gives label of columns
	#print(hdulist[1].data[0]) #to access lines
	#print(hdulist[1].data.field(11)) #to access columns 
	#print(hdulist[1].data.shape) #shape of data in hdulist selected
	#print(hdulist[1].data['ref_epoch']) #to access columns but with the name 

	return hdulist
	
def get_columns(hdulist):	
	
	RA = hdulist[1].data['RA']
	DEC = hdulist[1].data['DEC']
	PMRA = hdulist[1].data['PMRA']
	PMDEC = hdulist[1].data['PMDEC']
	
	return RA,DEC,PMRA,PMDEC
