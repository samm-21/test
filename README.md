# Quiz Analyzer
Quiz Analizer is a python based project which analyses the performance of a student from the quiz and provides information like the strengths and weaknesses of the student using historical data and visualises the performance in bar graph for a better understanding.

# Key Features:
- Fetches quiz and historical data from APIs.
- Categorizes topics into performance levels: **Weak**, **Average**, **Good**, and **Strong**.
- Provides a summary of strengths and weaknesses.
- Visualizes performance using bar charts for easy understanding.

# Setup:
- python 3.8+
- Libraries: pandas,numpy,requests,matplotlib

# Approach Description:
Data Cleaning:
- Replaces percentage signs in the accuracy column and converts it to numeric.
- Handles missing or invalid data.
  
Grouping:
- Groups the data by quiz.topic to calculate average scores and accuracy.
  
Performance Categorization:
- Categorises all the topics according to the accuracy of the tests into different categories.
  
Visualization:
- Creates a bar chart to visualize topic performance.
  
Insights:
- Strengths and weaknesses are summarized in the persona object for recommendations.

Screenshots of the output:
![image](https://github.com/user-attachments/assets/402dc696-591d-4617-958c-cbcd67bbf6db)
![image](https://github.com/user-attachments/assets/b113f5e2-1fc1-4fc0-9fa9-226f279736d4)


