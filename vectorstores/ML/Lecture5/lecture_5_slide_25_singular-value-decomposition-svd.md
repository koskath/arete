# Slide 25 of Lecture 5 contains information about the Singular Value Decomposition (SVD).

fromsklearn.decomposition importTruncatedSVD
importnumpy asnp
np.random.seed(0)
X= np.random.rand(100, 100)
#four components
svd =TruncatedSVD(n_components=4, n_iter=10, random_state=5)
U = svd.fit_transform(X)
Sigma =np.diag(svd.singular_values_)
V = svd.components_
#incase wewant to dothe multiplication
# U x Sigma
U_x_Sigma =np.dot(U, Sigma)
#(U x Sigma) xV
U_Sigma_V =np.dot(U_x_Sigma ,V)
https://predictivehacks.com/?all-tips=svd-with-scikit-learn
