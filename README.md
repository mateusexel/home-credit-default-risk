[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/mateusexel/home-credit-default-risk/blob/master/LICENSE)


# Home-Credit-Default-Risk
Predicting how capable each applicant is of repaying a loan (Kaggle Challenge).

<img src="https://github.com/mateusexel/home-credit-default-risk/blob/master/home-credit-image.jpeg" alt="loan" width="600" height="400"/>

## Getting Started

Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders.

Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

While Home Credit is currently using various statistical and machine learning methods to make these predictions, they're challenging Kagglers to help them unlock the full potential of their data. Doing so will ensure that clients capable of repayment are not rejected and that loans are given with a principal, maturity, and repayment calendar that will empower their clients to be successful.

```
https://www.kaggle.com/c/home-credit-default-risk
```
The objective of this competition is to use historical loan application data to predict whether or not an applicant will be able to repay a loan. This is a standard supervised classification task:

Supervised: The labels are included in the training data and the goal is to train a model to learn to predict the labels from the features.

Classification: The label is a binary variable, 0 (will repay loan on time), 1 (will have difficulty repaying loan)

### Aprouch

Commonly, problems are presented with both static and dynamic features. Typical machine learning models have poor solutions to that. 
On the other hand Neural Networks have a  common denominator when dealing with both types of data. 
In this project I tried to combine temporal and static data to improve the classification performance.

### Installing

1. Clone repository and install requirements (use Anaconda)

```
git clone https://github.com/mateusexel/home-credit-default-risk
```


```
conda create --name <env> --file requirements.txt
```

### Running 

2. Navigate inside the "home-credit-default-risk" folder and Run  

```
jupyter notebook
```

## Running the notebook

Navigate inside the "time_series" folder and launch the notebook & to run cells do:

```
Shift + Enter
```


## Built With

* [Jupyter Notebook](http://jupyter.org/) - Project Jupyter exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.
* [Numpy](http://numpy.org/) - NumPy brings the computational power of languages like C and Fortran to Python, a language much easier to learn and use. With this power comes simplicity: a solution in NumPy is often clear and elegant.
* [Keras](https://keras.io//) - Keras is an open-source software library that provides a Python interface for artificial neural networks.
* [Sklearn](http://scikit-learn.org/stable/) - Machine Learning in Python.
* [Pandas](https://pandas.pydata.org/) - pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
* etc
 
## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/mateusexel/home-credit-default-risk/blob/master/LICENSE) file for details

## Acknowledgments

* Awesome answers at stackoverflow.
* Kaggle

