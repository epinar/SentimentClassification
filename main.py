import train 
import test 
import stats

def main():
	train.doTrain(0) # Train with laplace smooting
	test.doTest()
	print ' === Results for classification without Laplace smooting === \n'
	#res = [[179, 121], [209, 91]]
	stats.report(test.res)
	#stats.report(res)

	train.calcLikeli(1) # Update likelihoods with laplace smooting
	test.doTest()
	print ' === Results for classification with Laplace smooting, alpha = 1 === \n'
	#res = [[269, 31], [76, 224]]
	#stats.report(res)
	stats.report(test.res)
	
main()