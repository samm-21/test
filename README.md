# Quiz Analyzer
Quiz Analyzer is a python based project which analyses the performance of a student from the quiz and provides information like the strengths and weaknesses of the student using historical data and visualises the performance in bar graph for a better understanding.

# Key Features:
- Fetches quiz and historical data from APIs.
- Categorizes topics into performance levels: **Weak**, **Average**, **Good**, and **Strong**.
- Provides a summary of strengths and weaknesses.
- Visualizes performance using bar charts for easy understanding.

# Setup:
- python 3.7+
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
![Screenshot 2025-01-20 195322](https://github.com/user-attachments/assets/1e08a5dd-1710-4032-946f-aaee4cb31930)

![image](https://github.com/user-attachments/assets/b113f5e2-1fc1-4fc0-9fa9-226f279736d4)


Video:
https://github.com/user-attachments/assets/768d5619-fe53-415e-b762-45c2d077cf90



