# 1. Deep Learning & Mathematics notes

## 1.1. Table des matières
- [Statistics and basic ML](#statistics-and-basic-ml)
  - [Intuitive explanation of maximum likelihood estimation](#intuitive-explanation-of-maximum-likelihood-estimation)
  - [Calculation of the Likelihood Formula](#calculation-of-the-likelihood-formula)
  - [Benefits in Gaussian Distribution](#benefits-in-gaussian-dsitribution)
  - [Order of Likelihoods](#order-of-likelihoods)
  - [Computational Complexity](#computational-complexity)
  - [Why use negative log likelihood](#why-use-negative-log-likelihood)
- [Relationship to Entropy and Cross-Entropy](#relationship-to-entropy-and-cross-entropy)
  - [Negative Log Likelihood](#negative-log-likelihood-nll)
  - [Practical Example](#practical-example)
- [Bayesian Inference and Deep learning](#bayesian-inference-and-deep-learning)
  - [Basics of Bayesian Inference](#basics-of-bayesian-inference)
  - [Applications in Machine Learning](#application-in-machine-learning)
  - [Advantages of Bayesian Inference](#advantages-of-bayesian-inference)
  - [Challenges](#challenges)


# 2. Statistics and basic ML:
## 2.0 Turning Products into Sums

The following is a very simple trick, yet used very widely, particularly in Machine Learning. See, **products** are never very good. Here we have a product of 4 numbers, which is not bad, but imagine if we had a million data points. How would the product of a million small probabilities (between 0 and 1) would look? It would be a ridiculously tiny number. In general we want to avoid products as much as we can. What’s better than a product? Well, a **sum**! And how do we turn products into sums? Exactly, using the **logarithm** function, since the following identity will be very helpful:
![](https://miro.medium.com/v2/resize:fit:251/0*v6hxTSLvcZUiBanI.)

## 2.1. Intuitive explanation of maximum likelihood estimation

Maximum likelihood estimation is a method that determines values for the parameters of a model. The parameter values are found such that they maximise the likelihood that the process described by the model produced the data that were actually observed.

## 2.2. Calculation of the likelihood formula

It is extremely useful, for example, when you want to calculate the *joint likelihood* for a set of independent and identically distributed points. Assuming that you have your points:

$X = x_1, x_2, \ldots, x_N$

The total likelihood is the product of the likelihood for each point, i.e.:

$p(X \mid \Theta) = \prod_{i=1}^N p(x_i \mid \Theta)$

where $\Theta$ are the model parameters: vector of means $\mu$ and covariance matrix $\Sigma$. If you use the log-likelihood you will end up with sum instead of product:

$\ln p(X \mid \Theta) = \sum_{i=1}^N \ln p(x_i \mid \Theta)$

### 2.2.1. Transition to Cross-Entropy

Utilizing the properties of logarithms, specifically the rule that \(\ln(a \cdot b) = \ln a + \ln b\), the product of probabilities turns into a sum of logarithms, which is the foundation of cross-entropy in information theory.

In machine learning, particularly in classification tasks, we often deal with the scenario where we need to measure how well our predicted probability distribution \( q \) aligns with the actual distribution \( p \). This is where cross-entropy comes in.

Given the model's predicted probabilities for each class and the true distribution, cross-entropy is defined as:

$H(p, q) = -\sum p(x) \ln q(x)$

#### 2.2.1.1. Derivation from Log-Likelihood to Cross-Entropy

Starting from the log-likelihood for categorical distributions:

 $\ln p(X \mid \Theta) = \sum_{i=1}^N \ln p(x_i \mid \Theta)$

If \( p \) represents the true labels (in a one-hot encoded form where the actual class label corresponding to each observation is 1 and all others are 0), and \( q \) represents the predicted probabilities by the model, then for each instance \( i \), only the true class \( c \) contributes to the sum, since for all non-true classes \( j \neq c \), \( p(x_i = j \mid \Theta) = 0 \).

Therefore, the log-likelihood simplifies to:

 $\ln p(X \mid \Theta) = \sum_{i=1}^N \ln q_{c_i}$ 

Where \( $q_{c_i}$ \) is the predicted probability of the true class \( $c_i$ \) for each sample \( i \).

Transforming this into the formula for cross-entropy, we negate this sum to minimize the negative log-likelihood:

 $H(p, q) = -\sum_{i=1}^N \ln q_{c_i}$ 

This result shows that maximizing the likelihood is equivalent to minimizing the cross-entropy between the predicted and actual distributions, a key objective in training classification models.

## 2.3. Benefits in Gaussian Distribution

Also in the case of Gaussian, it allows you to avoid computation of the exponential:

$p(x \mid \Theta) = \frac{1}{((2\pi)^{\frac{d}{2}} \sqrt{\det \Sigma})} e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)}$ 

Which becomes:

$\ln p(x \mid \Theta) = -\frac{d}{2} \ln(2\pi) - \frac{1}{2} \ln(\det \Sigma) - \frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu)$

## 2.4. Order of Likelihoods

ln is a monotonically increasing function, thus log-likelihoods have the same relations of order as the likelihoods:

$p(x \mid \Theta_1) > p(x \mid \Theta_2) \Leftrightarrow \ln p(x \mid \Theta_1) > \ln p(x \mid \Theta_2)$

## 2.5. Computational Complexity

From a standpoint of computational complexity, you can imagine that first of all summing is less expensive than multiplication (although nowadays these are almost equal). But what is even more important, likelihoods would become very small and you will run out of your floating point precision very quickly, yielding an underflow. That's why it is way more convenient to use the logarithm of the likelihood by hand, using a pocket calculator - almost impossible.

Additionally in the classification framework you can simplify calculations even further. The relations of order will remain valid if you drop the division by 2 and the ln(2π) term. You can do that because these are class independent. Also, as one might notice if variance of both classes is the same (\(\Sigma_1 = \Sigma_2\)), then you can also remove the ln(\det \Sigma) term.


## 2.6. Why use negative log likelihood:

The likelihood expression for the total probability is actually quite a pain to differentiate, so it is almost always simplified by taking the natural logarithm of the expression. This is absolutely fine because the natural logarithm is a monotonically increasing function. This means that if the value on the x-axis increases, the value on the y-axis also increases (see figure below). This is important because it ensures that the maximum value of the log of the probability occurs at the same point as the original probability function. Therefore, we can work with the simpler log-likelihood instead of the original likelihood.

(when we are looking for the maximum point, as long as the x doesn’t change and doesn’t change the direction it’s not a problem when multiplying a function by a number, or apply a log).

- > when differentiating, we will retrieve the same x for the maximum)

**Source:**
*Probability concepts explained: Maximum likelihood estimation* by Jonny Brooks-Bartlett | Towards Data Science



# 3. Relationship to Entropy and Cross-Entropy

- **Entropy** and **Cross-Entropy**:
  - **Entropy** in information theory measures the average amount of information (or uncertainty) inherent in a variable's possible outcomes. It's originally a concept from thermodynamics, but Claude Shannon adapted it for use in telecommunications to measure the unpredictability of a message.
  - **Cross-Entropy** measures the average number of bits needed to identify an event from a set of possibilities if a wrong probability distribution is used instead of the true distribution. It's a measure of the difference between two probability distributions: the true distribution \( p \) and the estimated distribution \( q \).

### 3.1. Negative Log-Likelihood (NLL)

When discussing NLL in the context of machine learning models like those used in classification tasks, you often deal with minimizing the cross-entropy between the predicted probability distribution and the actual distribution of the labels. Here's how this relates to bits and information theory:

1. **Bit as a Unit of Information**:
   - In information theory, a "bit" is the fundamental unit of information. It essentially measures the information gained by observing the occurrence of an event that can happen with probability \( p \). The information content (or surprise) of an event that occurs with probability \( p \) is quantified as \( \log_2(\frac{1}{p}) \) bits.

2. **NLL and Cross-Entropy**:
   - For classification tasks, each target label can be considered as an event. The NLL for a predicted probability distribution over these labels is calculated using the logarithm of the predicted probabilities. If you use the base-2 logarithm, this calculation directly gives you the cross-entropy in bits.
   - The formula for cross-entropy in bits is:  $H(p, q) = -\sum p(x) \log_2 q(x)$, where \( p(x) \) is the true probability of outcome \( x \), and \( q(x) \) is the predicted probability of \( x \).

3. **Interpretation of NLL in Bits**:
   - When NLL is expressed in bits, each term  $-\log_2 q(x_i)$  (where \( x_i \) is the true label) measures the number of bits required to encode the event \( x_i \) using the predicted probability  $q$ . Lower values of  $q(x_i)$  (when the prediction is uncertain or wrong) lead to higher values of  $-\log_2 q(x_i)$ , indicating that more bits are required to encode the event due to the prediction error.
   - Minimizing NLL thus means minimizing the average number of bits needed to correctly encode the labels given the predictions. A perfect model, which predicts the true distribution exactly, would have a cross-entropy equal to the entropy of the true distribution (the theoretical lower bound in bits).

### 3.2. Practical Example

If a model predicts that a certain event has a probability of 0.5, the information content of that event occurring is  $\log_2(2) = 1  bit$. If the true probability of the event is actually 1 (it always happens), the cross-entropy would be higher because the model's prediction introduces uncertainty (inefficiency in coding).

In summary, expressing NLL in bits provides a direct interpretation in terms of the efficiency of the prediction. Minimizing NLL in bits can be seen as optimizing the model to reduce the average 'coding cost' in bits, making it as efficient as possible in terms of the information-theoretic encoding of predictions.


# 4. Bayesian Inference and Deep Learning

Bayesian inference is a method of statistical inference in which Bayes' theorem is used to update the probability for a hypothesis as more evidence or information becomes available. It is fundamentally a method of learning from evidence as it accumulates. Bayesian inference contrasts with frequentist approaches, which do not, in contrast, allow for the possibility of hypothesis probabilities being updated with new evidence.

### 4.1. Basics of Bayesian Inference

Bayesian inference revolves around updating our belief about the unknown parameters of a model based on observing data. This is expressed mathematically as:

$[ P(\Theta \mid X) = \frac{P(X \mid \Theta) P(\Theta)}{P(X)}]$

where:
-  $P(\Theta \mid X)$  is the posterior probability of the model parameters  $\Theta$ given the data  $X$ .
-  $P(X \mid \Theta)$  is the likelihood of the data given the model parameters.
-  $P(\Theta)$ is the prior probability of the model parameters.
- $P(X)$ is the marginal likelihood or evidence, which acts as a normalizing constant.

### 4.2. Application in Machine Learning

In machine learning, Bayesian methods are used to continuously update the probability of a model as more data becomes available, making it particularly useful in dynamically changing environments. This approach allows models to improve as they learn from new data, reflecting changes that might occur in real-world scenarios.

One common application of Bayesian inference is in the Bayesian networks, which are graphical models that represent the probabilistic relationships among a set of variables. Another application is Bayesian optimization, which is used for optimizing complex functions where the objective evaluations are expensive.

### 4.3. Advantages of Bayesian Inference

1. **Incorporation of Prior Knowledge:** Bayesian inference naturally allows the incorporation of prior knowledge through the prior distribution, which can provide robustness especially when the data is limited or noisy.
  
2. **Probabilistic Interpretation:** It provides a probabilistic approach to inference, which not only estimates the parameters but also quantifies uncertainty in the estimates, allowing for more informed decision-making.

3. **Flexibility:** Bayesian methods can adapt to new data incrementally, without needing to retrain from scratch, which is advantageous in continuous learning systems.

### 4.4. Challenges

While Bayesian inference has many advantages, it also faces computational challenges, especially in dealing with high-dimensional data or complex models. Advanced computational techniques like Markov Chain Monte Carlo methods are often used to approximate the posterior distributions.

# 5. Weight

### 5.1. Xavier Initialization
Xavier initialization is designed specifically for keeping the forward and backward propagation scales roughly the same in deep networks. 

#### 5.1.1. Theory and Formula
The key idea behind Xavier initialization is to maintain the variance of activations and backpropagated gradients throughout the network. For a layer with `n_in` inputs and `n_out` outputs, the Xavier initialization sets a layer’s weights W to be sampled from a distribution with zero mean and a variance of \( $\frac{2}{{n_{\text{in}} + n_{\text{out}}}}$ \) (for the uniform distribution, it ranges between $-\sqrt{\frac{6}{{n_{\text{in}} + n_{\text{out}}}}} and \sqrt{\frac{6}{{n_{\text{in}} + n_{\text{out}}}}}$.

#### 5.1.2. When to Use
Xavier initialization works best with layers followed by a sigmoidal activation function like logistic sigmoid or hyperbolic tangent.

### 5.2. He Initialization
He initialization is a strategy designed to address some of the problems that can occur with weights in deep neural networks, especially those with ReLU activation functions.

#### 5.2.1. Theory and Formula
He initialization specifically considers the needs of ReLU activations to maintain the mean and variance of the outputs over each layer. It initializes the weights of the \(i^{th}\) layer from a random normal distribution with a mean of 0 and a variance of \( \frac{2}{{n_{\text{in}}}} \), where \(n_{\text{in}}\) is the number of incoming network connections from the previous layer.

#### 5.2.2. When to Use
He initialization is especially effective for networks that use ReLU activation functions because it helps in avoiding problems related to the "dying ReLU" where neurons stop participating in the forward or backward propagation due to zero gradients.

### 5.3. Impact

By carefully initializing the weights, these methods help in speeding up the convergence of the training process by ensuring that all layers in the model initially have gradients that are neither too large nor too small. This improves the ability of the model to learn from the training data efficiently and effectively.

The choice between Xavier and He initialization generally depends on the activation function used in the network. Xavier is preferred for sigmoid and tanh functions, while He is better suited for ReLUs. This customization according to the activation function helps in optimizing the training process and leads to better performance of the neural network models.