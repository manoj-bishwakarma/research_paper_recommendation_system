# Machine Learning-Based Research Paper Recommendation System

## Overview

The Machine Learning-Based Research Paper Recommendation System is a Python-based command-line application that helps researchers and students discover relevant research papers based on their interests and previous interactions. The system provides role-based access for administrators and regular users.

Administrators can manage research papers and user accounts, while users can search papers, maintain reading history, save favorite papers, and receive personalized recommendations.

The system uses a content-based recommendation approach and stores all application data using CSV files.

## Features

### Administrator

* Add, edit, delete, and view research papers 
* Search research papers
* View and manage user accounts
* Train and update recommendation models

### Regular User

* Register and login
* View all research papers
* Search papers by ID, title, author, category, and keywords
* Receive personalized recommendations
* Save favorite papers
* View reading history
* Update research interests

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* CSV File Handling
* Machine Learning
* Content-Based Recommendation System
* Git and GitHub

## Project Structure

```
research_paper_recommendation_system/
│
├── data/
│   ├── users.csv
│   ├── papers.csv
│   ├── history.csv
│   └── favorites.csv
│
├── main.py
├── authentication.py
├── paper_manager.py
├── history_manager.py
├── favorite_manager.py
├── recommendation_engine.py
├── train_model.py
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── admin.py
├── user.py
├── research_paper.py
├── file_manager.py
└── README.md
```

## Run the Project

```bash
python main.py
```

* ## Future Enhancements
* Implement advanced recommendation algorithms
* Develop a graphical user interface (GUI)
* Integrate relational databases such as MySQL or PostgreSQL
* Deploy as a web application using FastAPI or Django
* Add password hashing with per-user salt (bcrypt/PBKDF2) for stronger security
* Add unit tests for authentication, paper management, and recommendation logic
* Support exporting recommended/favorite papers as PDF or CSV
* Add pagination for viewing large paper collections
* Allow filtering recommendations by multiple categories or keywords at once

## Author

**Manoj Bishwakarma**


