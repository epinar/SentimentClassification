
=== Movie Review Sentiment Classification with Multinomial Naive Bayes Approach ===

You can run this program via "python main.py". 

Initially, there is a training phase with the movie review data which is labeled by either "positive" or "negative" tags. During the training, conditional probabilities of each word in each class is calculated. One can choose to use Laplace smoothing by giving the alpha coefficient. If alpha is 0, then the calculation is done without smoothing.

In the testing phase, the posterior probability differences in log-space are calculated. The reviews in test dataset are classified accordingly.

The performance values of each classes and micro/macro-averaged precision, recall and F-scores of the system are calculated in the stats.py. These are reported as training results.

This dataset is used: https://www.cs.cornell.edu/people/pabo/movie-review-data/