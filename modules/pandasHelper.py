#
# pandasHelper.py
#
# Helper functions for analysis
#

import pandas as pd

# TODO: add optional arguments to be passed to "value counts()"
def printColumnCounts(df,column,rows=0):
	if column not in df.columns:
		print ">> ERROR: column {0} does not exist\n".format(column)
		return None

	datacount=len(df.index)
	s = df[column].value_counts(dropna=False) # Series
	df=s.to_frame(name='count')
	df['pct']=df['count']/datacount
                                            #df.to_string(formatters={'pct':'${:,.2f}'.format})
	df['count'] = df['count'].map("{:,}".format)
	df.pct=df['pct'].map('{:,.2%}'.format)
	print "> Value distribution for: {0}\n{1}\n".format(column,df.head(rows))

# TODO: make this work for a list of columns
def showStatsMissing(df, column):
	if not isinstance (df, pd.DataFrame):
		print ">> ERROR: dataframe needs to be passed in, passed:", type(df)
		return None
	if (len(df.index) == 0):
		print "Empty dataframe supplied"
		return None

	if column not in df.columns:
		print ">> ERROR: column {0} does not exist\n".format(column)
		return None

	noValCnt = df[column].isnull().sum()
	print "Column: \"{0}\" missing values: {1:,} ({2:.1%})\n".format(column, noValCnt , float(noValCnt)/len(df.index))

####
# remap a data frame column, based on the mapping supplied in the mapfile
###
def remapColumn(df, column, mapfile, notfound="Other"):
    #lines = list(csv.reader(open(mapfile)))
    #[val, remap] = pieces = [x.strip() for x in val.split(',')]
    #data_dict = {h: v for h, v in zip(header, zip(*values))}
    
    file = open (mapfile,'r')
    dict={}
    for line in file:
        fields = line.split(',')
        print "Mapping: {0} -> {1}".format(fields[0], fields[1])
        dict[fields[0]] = fields[1]
    df[column] = df[column].map(lambda x:dict.get(x,notfound))    
