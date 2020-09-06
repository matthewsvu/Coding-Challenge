# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

# Libraries used:
  ## -Numpy
  ## -Pandas
  ## -matplotlib
  ## -sklearn
# Sources
  ## Used for learning how to extract data and use the KMeans algorithm respectively
   - https://www.youtube.com/watch?v=Qh7VxLsaU9M&ab_channel=LucasParisi
   
   - https://blog.cambridgespark.com/how-to-determine-the-optimal-number-of-clusters-for-k-means-clustering-14f27070048f
# How I did it
  - I obtained my solution by implementing a KMeans Clustering algorithm using the Elbow Method and Silhouette analysis to confirm the amount of clusters as **2** in total
  - I started by  intializing the centroids at random and using them to assign points to the nearest cluster
  - By finding the mean of all the points within the cluster I update the position of the cluster
  - This is repeated until the clusters have 
  - The elbow method I graphed to find out the where graph looks like an arm / elbow joint, which I identified as 2
  - The silhouette method is utilized in my program to confirm the results
