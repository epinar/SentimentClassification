import train 
import test 
import stats

# Main function to execute training, testing and reporting phases.
def main():
	train.doTrain(0) # Train without laplace smooting(alpha=0).
	test.doTest()
	print ' === Results for classification without Laplace smooting === \n'
	stats.report(test.res)

	train.calcLikeli(1) # Update likelihoods with laplace smooting(alpha=1).
	test.doTest()
	print ' === Results for classification with Laplace smooting, alpha = 1 === \n'
	stats.report(test.res)
	
main()