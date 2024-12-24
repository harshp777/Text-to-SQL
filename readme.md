# QuerySmart

QuerySmart is a Streamlit-based web application that allows users to interact with databases using natural language. It leverages the power of Large Language Models (LLMs) like GPT-4, converting natural language queries into optimized SQL commands. The app is designed for non-technical users to easily query data without writing SQL, making database interaction more accessible and boosting productivity.


![image](https://github.com/user-attachments/assets/82f4dbf6-2653-4e71-9760-d63432186847)


## Project Overview

In today's data-driven world, accessing and querying databases can be a significant challenge, especially for users without SQL expertise. QuerySmart aims to bridge this gap by enabling natural language to SQL translation, simplifying the process of interacting with relational databases.

By leveraging GPT-4 and integrating with cloud platforms such as Microsoft Azure, AWS, and Databricks, QuerySmart empowers users to perform complex database queries, generate ERD diagrams, and save favorite queries, all through a simple, intuitive interface.

## Key Features

### 1. **Create ERD Diagrams**
   - Generate ERD (Entity-Relationship Diagrams) using LLMs to visualize the structure of your database. This helps users understand relationships between tables without diving into technical details.

### 2. **Quick Analysis**
   - Automatically generate 5 questions based on the selected data from Databricks. These questions aim to provide quick insights and data exploration without any manual input.

### 3. **Your Favourites**
   - Save your favorite questions and their associated SQL queries. This feature allows users to store frequently used queries for easy access.

### 4. **Deep Dive Analysis**
   - Perform more detailed analysis by generating queries based on user input, displaying data, and providing the option to build further queries on top of the results.

## Tech Stack

- **Language**: Python 3.10
- **Libraries**: 
  - `Langchain` 
  - `Langchain-openai`
  - `Streamlit`
  - `Databricks`
- **Model**: GPT-4o mini via OpenAI API
- **Cloud Platforms**: 
  - Microsoft Azure
  - AWS (EC2 for deployment)
 
  ## User Interface
**Select Data**

![image](https://github.com/user-attachments/assets/3d2f9384-3146-42f2-a739-fe54d2d6584e)

**UI**

![image](https://github.com/user-attachments/assets/21ae1188-7c4b-4a41-a7b5-7838fe552909)

![image](https://github.com/user-attachments/assets/2fadd7fa-4f4e-4c13-87d9-559d20025a59)


**ERD Diagram**
![image](https://github.com/user-attachments/assets/f7dc0077-7c56-44a3-a620-143397515f32)

**Select Question(AI Generated)**
![image](https://github.com/user-attachments/assets/ad87b52b-d590-42bf-a825-ece0394628de)

**Analyze the Query**

![image](https://github.com/user-attachments/assets/0b550e23-6cf7-496f-a02b-3290ccbc697a)

![image](https://github.com/user-attachments/assets/0fe720e8-1845-42f6-abc9-6aaa9e40f06e)


**Store as Favourite**

![image](https://github.com/user-attachments/assets/d078b257-daf6-432b-8356-da62dadafec0)

![image](https://github.com/user-attachments/assets/4d2295fd-62e2-43a0-b18e-3cf75da0aae0)


**Customize Questions**

![image](https://github.com/user-attachments/assets/51af4bdb-be94-4001-aaf1-e880a1052a5c)

![image](https://github.com/user-attachments/assets/78687c74-861e-4670-9816-61495008c67b)


**Build On top of Generated Query**

![image](https://github.com/user-attachments/assets/7ce38076-5f80-49f9-93c4-77d2861a9a0e)

![image](https://github.com/user-attachments/assets/a695ef76-c7f6-4d10-b93a-80082c445370)







