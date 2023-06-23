# Property Price Prediction

This project focuses on predicting property prices using a machine learning model. It includes exploratory data analysis (EDA), preprocessing of the data, training an ElasticNet model, and creating a Flask application for predicting property prices based on user input.

<p align="center">
  <img width="1000" height="300" src="https://upload.wikimedia.org/wikipedia/commons/3/36/Lower_Manhattan_from_Jersey_City_November_2014_panorama_1.jpg">
</p>

## Features

### Exploratory Data Analysis (EDA)
In this section, we performed an exploratory data analysis to gain insights into the property prices dataset. The EDA process involved several steps:

1. **Data exploration**: We examined the structure and content of the dataset, including the number of rows and columns, data types, and basic statistics.

2. **Missing data handling**: We investigated the presence of missing values in the dataset and applied appropriate techniques to handle them, such as imputation or removal, based on the nature and extent of missingness.

3. **Outlier detection**: We identified outliers in the data using statistical methods or visualization techniques, and decided on the appropriate treatment, which could involve removal or transformation.

4. **Feature engineering**: We derived new features from the existing ones, such as creating boolean indicators for Education or Shopping centers around the properties.

**The EDA process provided valuable insights into the dataset, enabling us to make informed decisions during the preprocessing and modeling stages.**

### Preprocessing
To prepare the data for modeling, we performed several preprocessing steps on the dataset. These steps included:

1. **Encoding categorical variables**: Categorical variables were encoded into numerical representations using techniques such as one-hot encoding. This transformation allowed the machine learning model to interpret these variables effectively.
  
2. **Feature scaling**: We applied feature scaling to ensure that all features were on a similar scale.

**By performing these preprocessing steps, we prepared the dataset in a format suitable for training the ElasticNet model.**

### Model Training
In this section, we describe the process of training the ElasticNet model on the preprocessed dataset. The ElasticNet model is a linear regression model that combines the L1 and L2 regularization techniques. Here are the key details:

1. **Model architecture**: The ElasticNet model is a linear regression model that incorporates both the L1 (Lasso) and L2 (Ridge) regularization terms. It combines the strengths of both regularization techniques to achieve a balance between feature selection and parameter shrinkage.

2. **Hyperparameters**: The ElasticNet model has two main hyperparameters: alpha and l1_ratio. Alpha controls the overall strength of regularization, where higher values result in stronger regularization. The l1_ratio determines the mix between L1 and L2 regularization, ranging from 0 to 1, with 0 corresponding to pure L2 regularization and 1 corresponding to pure L1 regularization.

3. **Training process**: We split the preprocessed dataset into training and testing sets, typically using a random or stratified sampling technique. We then fitted the ElasticNet model to the training data, optimizing the hyperparameters using techniques like cross-validation.

4. **Evaluation metrics**: To assess the performance of the ElasticNet model, we used appropriate evaluation metrics such as mean squared error (MSE) and root mean squared error (RMSE). These metrics help quantify the model's ability to predict property prices accurately.

**The training process allowed us to learn the optimal parameters for the ElasticNet model and evaluate its performance on unseen data.**

### Flask Application
The Flask application provides a user-friendly interface for interacting with the trained ElasticNet model and obtaining predicted property prices. Here's how it works:

1. **User interface**: The Flask application presents a web-based user interface where users can input property information, such as the number of rooms, and the area size, address, etc.

2. **Data preprocessing**: Once the user submits the property details, the Flask application preprocesses the input data by applying the same transformations used during the initial data preprocessing step.

3. **Prediction**: The preprocessed data is then passed to the trained ElasticNet model, which generates a predicted property price based on the provided information.

4. **Result display**: The Flask application displays the predicted property price to the user, providing valuable insights into the estimated value of the property.

## Installation and Usage

Provide instructions on how to install and use the project. Include steps to set up the development environment, install the required dependencies, and run the Flask application.

1. Clone the repository:

```
git clone https://github.com/shonshchori/PropertiesPricePrediction/
cd PropertiesPricePrediction
```

2. Set up the environment:

- Create a virtual environment (optional but recommended):

```
python -m venv env
source env/bin/activate  # for Unix/Linux
env\Scripts\activate  # for Windows
```

- Install the required dependencies:

`pip install -r requirements.txt`

3. Run the Flask application:

`python api.py`

4. Access the Flask application in your web browser:

`http://localhost:5000`
