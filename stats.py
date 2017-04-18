from __future__ import division

def report(res):
	pr0 = precision(res, 0)
	rc0 = recall(res, 0)
	fs0 = Fscore(pr0, rc0)

	pr1 = precision(res, 1)
	rc1 = recall(res, 1)
	fs1 = Fscore(pr1, rc1)

	pMicro = Pmicro(res)
	rMicro = Pmicro(res)
	fMicro = Fscore(pMicro, rMicro)

	pMacro = (pr0+pr1)/2
	rMacro = (rc0+rc1)/2
	fMacro = Fscore(pMacro, rMacro)

	print 'Pred/Real Neg \tPos \n Neg \t  {:d} \t{:d} \n Pos \t  {:d} \t{:d} \n'.format(res[0][0], res[0][1], res[1][0], res[1][1])
	print 'Macro-averaged \n\tPrecision: %.3f \n\tRecall: %.3f \n\tFscore: %.3f ' %(pMacro, rMacro, fMacro)
	print 'Micro-averaged \n\tPrecision: %.3f \n\tRecall: %.3f \n\tFscore: %.3f ' %(pMicro, rMicro, fMicro)
	print 'Class Negative \n\tPrecision: %.3f \n\tRecall: %.3f \n\tFscore: %.3f ' %(pr0, rc0, fs0)
	print 'Class Positive \n\tPrecision: %.3f \n\tRecall: %.3f \n\tFscore: %.3f \n' %(pr1, rc1, fs1)

def precision(res, c): return (res[c][c])/(res[c][c]+res[1-c][c])

def recall(res, c): return (res[c][c])/(res[c][c]+res[c][1-c])

def Fscore(p, r): return (2*p*r)/(p+r)

def Pmicro(res): return (res[0][0]+res[1][1])/(res[0][0]+res[1][1]+res[1][0]+res[0][1])
