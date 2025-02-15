# BrainyBeam Django Internship Tasks

This repository contains the tasks I completed during my internship at **BrainyBeam**, where I worked with the **Django framework** and other Python concepts. The tasks cover various aspects of web development, data handling, and object-oriented programming.

## Project Overview

This repository includes solutions to a series of tasks involving Django development, Python programming, and APIs. Below is a breakdown of each task and what I accomplished.

---

## Tasks Overview

### **Task 1: Quiz App with Dynamic Number of Options**
In this task, I developed a **Quiz App** using Django that supports a dynamic number of options for each question. The app has the following features:

- **Dynamic Question Options:** Each question can have a varying number of options (from 2 to 6 or more).
- **Answer Evaluation:** The app checks how many answers the user selects are correct and returns the count of right and wrong answers.
- **Django Forms & Models:** Used forms for input and models to store questions, options, and correct answers in the SQLite database.
  
This task allowed me to explore Django's flexibility in handling dynamic forms and database interactions.

### **Task 2: Time Complexity Analyzer**
In this task, I created a **Time Complexity Analyzer** that applies to any function and returns the time complexity based on the execution time. The key features include:

- **Execution Time Measurement:** Using Python's `time` module to measure the execution time of a given function.
- **Time Complexity Output:** Outputs the time taken by the function for different input sizes, helping to estimate its time complexity.

This task enhanced my understanding of performance analysis and how to evaluate algorithms.

### **Task 3: POST API with Serialized Data and Count**
For this task, I developed a **POST API** using Django REST Framework. The API allows users to create new posts and returns the serialized data along with the count of records saved. Features include:

- **POST Endpoint:** Users can send `title` and `content` to create a post.
- **Serialized Response:** The API returns the serialized data of the created post along with a count of how many posts are in the database.

This task helped me understand how to work with Django REST Framework for API development and data serialization.

### **Task 4: API for Country, State, City with Data Export**
In this task, I created a function to fetch all cities in India using an external **Country State City API**. I also saved the data in a `.csv` file. Features:

- **API Integration:** The function calls the **Country State City API** to retrieve a list of cities in India.
- **Data Export:** The retrieved city data is saved in a `.csv` file for further use or analysis.

This task provided experience with third-party API integration and data export in Python.

### **Task 5: Advantages of Polymorphism and Encapsulation**
For this task, I built a **Python program** that demonstrates the advantages of **Polymorphism** and **Encapsulation** within the same program. Key features include:

- **Polymorphism:** Displaying how different objects can be used interchangeably, making the code flexible and reusable.
- **Encapsulation:** Showing how data can be hidden and protected within classes, promoting modular code.

This task reinforced my understanding of core object-oriented programming concepts.

---

## Requirements

To run the project locally, ensure you have the following installed:

- Python 3.x
- Django 3.x or higher
- SQLite database (default)
- Django REST Framework for API tasks

---

## Task Breakdown

### **Task 1: Quiz App with Dynamic Number of Options**
- **Model:** Question, Option, Answer
- **Features:** Dynamic options, user answer evaluation, right/wrong count
- **Database:** SQLite

### **Task 2: Time Complexity Analyzer**
- **Execution Time:** Measured using Python's `time` module.
- **Output:** Displays the time complexity estimation based on execution time.

### **Task 3: POST API with Serialized Data and Count**
- **API Endpoint:** POST request for creating a post
- **Serialized Response:** Returns post data with a count of total posts in the database

### **Task 4: API for Country, State, City with Data Export**
- **API Integration:** Fetches cities of India using the Country State City API.
- **Data Export:** Saves city data in a `.csv` file.

### **Task 5: Advantages of Polymorphism and Encapsulation**
- **Polymorphism:** Demonstrates flexible and reusable code.
- **Encapsulation:** Hides data to ensure modularity and security.

---

## Report

A report detailing how to use the app, its functionalities, expected outputs, and more is included in the project. This report provides in-depth explanations for each task and how to run them. You can view and download it [here](./Rejection%20Letter.pdf).

---

## Rejection Notice

While working on these tasks, I had the opportunity to participate in the internship program at **BrainyBeam**. Unfortunately, I was informed that my application was **rejected**. 

The **rejection letter** is attached in this repository for reference. It outlines the reasons for the rejection and provides constructive feedback, which I plan to use to improve my skills.

---

## Contributing

Feel free to fork the repository and contribute to the project. You can submit pull requests for improvements, new features, or bug fixes.

---

## License

This project is open-source and available under the MIT License.

---

Feel free to explore the code and modify it for your own use cases!
