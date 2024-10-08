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
- **Model**: GPT-4 via OpenAI API
- **Cloud Platforms**: 
  - Microsoft Azure
  - AWS (EC2 for deployment)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/QuerySmart.git
cd QuerySmart
