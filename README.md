
The SMS spam classification project focuses on developing a model that can accurately classify text messages as spam or not spam. The project utilizes a dataset called "spam.csv" which contains two columns: "target" and "text". The "target" column represents the label for each text message and can have two values: "spam" indicating the message is spam, and "ham" indicating the message is legitimate. The "text" column contains the actual content of the text messages.

To begin the project, the dataset is loaded into a dataframe called "df" using the pd.read_csv function. The dataset is encoded using 'latin-1' encoding to ensure proper handling of text content.

Before building the classification model, an exploratory data analysis (EDA) is performed on the dataset. EDA involves analyzing and visualizing different aspects of the data to gain insights and identify patterns. In the SMS spam classification project, the EDA encompasses various visualizations, such as analyzing the total number of words in spam and non-spam messages, the total number of characters, and sentence lengths. These visualizations help in understanding the characteristics and distinguishing features of spam and non-spam messages.

Once the EDA is completed, multiple machine learning algorithms are employed to build the SMS spam classification model. The following algorithms from the sklearn and xgboost libraries are used:
- Logistic Regression
- Support Vector Machines (SVM)
- Naive Bayes Classifier (MultinomialNB)
- Decision Tree Classifier
- K-Nearest Neighbors Classifier
- Random Forest Classifier
- AdaBoost Classifier
- Bagging Classifier
- Extra Trees Classifier
- Gradient Boosting Classifier
- XGBoost Classifier

Each algorithm is trained on a training set and evaluated on a test set to determine its effectiveness in classifying SMS messages as spam or not spam. The performance metrics such as accuracy, precision are calculated for each algorithm to assess their classification performance.

By comparing the performance of different algorithms, the project aims to identify the most effective classifier for SMS spam classification. The selected model can then be used to automatically classify incoming text messages, aiding in the identification and filtration of spam messages to enhance user experience and communication security.

