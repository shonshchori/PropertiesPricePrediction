# Property Price Prediction

This project focuses on predicting property prices using a machine learning model. It includes exploratory data analysis (EDA), preprocessing of the data, training an ElasticNet model, and creating a Flask application for predicting property prices based on user input.

## Features

- **Exploratory Data Analysis (EDA)**: Provide an overview of the EDA process. Describe the steps taken to analyze the collected data, identify patterns, and gain insights into the property prices dataset.

- **Preprocessing**: Explain the preprocessing steps performed on the data. This may include handling missing values, encoding categorical variables, scaling features, or any other data transformation steps.

- **Model Training**: Describe the process of training the ElasticNet model. Provide details about the model architecture, hyperparameters, and the evaluation metrics used to assess the model's performance.

- **Flask Application**: Explain how the Flask application works. Describe how users can interact with the application, input new property data, and obtain predicted property prices. Include any relevant instructions on how to run the Flask app locally.

## Explain

## Exploratory Data Analysis (EDA)
In this section, we performed an exploratory data analysis to gain insights into the property prices dataset. The EDA process involved several steps:

1. Data exploration: We examined the structure and content of the dataset, including the number of rows and columns, data types, and basic statistics.

2. Data visualization: We created various visualizations such as histograms, scatter plots, and correlation matrices to understand the distribution of variables, identify patterns, and explore relationships between features.

3. Missing data handling: We investigated the presence of missing values in the dataset and applied appropriate techniques to handle them, such as imputation or removal, based on the nature and extent of missingness.

4. Outlier detection: We identified outliers in the data using statistical methods or visualization techniques, and decided on the appropriate treatment, which could involve removal or transformation.

5. Handling outliers: Outliers, identified during the EDA process, were treated using appropriate techniques such as capping, winsorization, or transformation (e.g., logarithmic transformation) to reduce their impact on the model.

6. Feature engineering: We derived new features from the existing ones, such as creating dummy variables for categorical features or generating interaction terms to capture potential non-linear relationships.

The EDA process provided valuable insights into the dataset, enabling us to make informed decisions during the preprocessing and modeling stages.

## Preprocessing
To prepare the data for modeling, we performed several preprocessing steps on the dataset. These steps included:

1. Handling missing values: We addressed missing values by either imputing them with appropriate values (e.g., mean, median, or mode) or removing the corresponding rows or columns, depending on the missing data pattern and the importance of the variable.

2. Encoding categorical variables: Categorical variables were encoded into numerical representations using techniques such as one-hot encoding or label encoding. This transformation allowed the machine learning models to interpret these variables effectively.

3. Feature scaling: We applied feature scaling to ensure that all features were on a similar scale. Common scaling techniques include standardization (subtracting the mean and dividing by the standard deviation) or normalization (scaling values to a specified range).

By performing these preprocessing steps, we prepared the dataset in a format suitable for training the ElasticNet model.

## Model Training
In this section, we describe the process of training the ElasticNet model on the preprocessed dataset. The ElasticNet model is a linear regression model that combines the L1 and L2 regularization techniques. Here are the key details:

1. Model architecture: The ElasticNet model is a linear regression model that incorporates both the L1 (Lasso) and L2 (Ridge) regularization terms. It combines the strengths of both regularization techniques to achieve a balance between feature selection and parameter shrinkage.

2. Hyperparameters: The ElasticNet model has two main hyperparameters: alpha and l1_ratio. Alpha controls the overall strength of regularization, where higher values result in stronger regularization. The l1_ratio determines the mix between L1 and L2 regularization, ranging from 0 to 1, with 0 corresponding to pure L2 regularization and 1 corresponding to pure L1 regularization.

3. Training process: We split the preprocessed dataset into training and testing sets, typically using a random or stratified sampling technique. We then fitted the ElasticNet model to the training data, optimizing the hyperparameters using techniques like cross-validation or grid search.

4. Evaluation metrics: To assess the performance of the ElasticNet model, we used appropriate evaluation metrics such as mean squared error (MSE), root mean squared error (RMSE), or R-squared. These metrics help quantify the model's ability to predict property prices accurately.

The training process allowed us to learn the optimal parameters for the ElasticNet model and evaluate its performance on unseen data.

## Flask Application
The Flask application provides a user-friendly interface for interacting with the trained ElasticNet model and obtaining predicted property prices. Here's how it works:

1. User interface: The Flask application presents a web-based user interface where users can input property information, such as the number of bedrooms, bathrooms, and the area size.

2. Data preprocessing: Once the user submits the property details, the Flask application preprocesses the input data by applying the same transformations used during the initial data preprocessing step.

3. Prediction: The preprocessed data is then passed to the trained ElasticNet model, which generates a predicted property price based on the provided information.

4. Result display: The Flask application displays the predicted property price to the user, providing valuable insights into the estimated value of the property.

To run the Flask application locally, follow these instructions:

Install dependencies: Make sure you have the required dependencies installed, including Flask, Flask-WTF, WTForms, NumPy, and any other necessary libraries. You can use pip or conda to install these dependencies.

Download model files: Ensure that the pickled model files (properties_model.pkl and fitted_preprocessor.pkl) are present in the same directory as the Flask application script (api.py).

Run the application: In the command line, navigate to the directory containing api.py and run the Flask application using the following command: python api.py.

Access the application: Open a web browser and enter the URL http://localhost:5000 to access the Flask application. From there, you can interact with the application, input property data, and obtain predicted property prices.

Make sure to customize these instructions based on your specific Flask application setup and requirements.

## Dependencies

List the software dependencies required to run the project. Include the versions of Python and any additional packages/libraries used in the project. It's recommended to include a `requirements.txt` file that contains all the necessary dependencies and their versions. You can generate this file by running `pip freeze > requirements.txt`.

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


## Contributing

Explain how others can contribute to your project. Include guidelines for bug reports, feature requests, and pull requests.

## License

Specify the license under which the project is distributed. For example, you can use an open-source license such as the MIT License or Apache License 2.0.

## Credits

Acknowledge any external resources, libraries, or frameworks used in the project. Provide links to their documentation or GitHub repositories, if applicable.

## Contact

Include your contact information (email, social media handles, etc.) so that users and potential contributors can reach out to you with questions or feedback.
