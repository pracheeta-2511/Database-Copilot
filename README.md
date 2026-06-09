# Database-Copilot

An AI-powered database assistant that converts natural language questions into SQL queries and retrieves results from a MySQL database. The project uses Flask, FastMCP, and Groq LLMs to provide an intuitive way to interact with structured data without writing SQL manually.

## Features

* Natural Language to SQL conversion using LLMs
* MySQL database integration
* MCP (Model Context Protocol) support using FastMCP
* Query history tracking
* AI-generated result summaries
* Secure database access through environment variables
* Simple and user-friendly web interface

## Tech Stack

* Python
* Flask
* MySQL
* FastMCP
* Groq API
* HTML/CSS/JavaScript

## Project Structure

```text
Database-Copilot
│
├── screenshots/
├── templates/
│   └── index.html
│
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── db_mcp_server.py
├── inventory_db.sql
└── Dummy Data for Data Management Testing.pdf
```

## How It Works

1. The user enters a natural language question.
2. The LLM converts the question into an SQL query.
3. The Flask backend executes the SQL query on the MySQL database.
4. Results are returned to the user.
5. The LLM generates a concise summary of the retrieved data.

## Sample Queries

* Show all products in the Electronics category.
* List products with stock quantity less than 20.
* Find products priced under $500.
* Show the most expensive product.
* Display all available inventory items.

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Database-Copilot.git
cd Database-Copilot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=inventory_db
```

### Import Database

```bash
mysql -u root -p < inventory_db.sql
```

### Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

### Run MCP Server

```bash
python db_mcp_server.py
```

## Security Improvements

* Environment variables are used for sensitive credentials.
* Only SELECT queries are allowed through the MCP server.
* API keys are excluded from version control using `.gitignore`.

## Future Enhancements

* Support for MongoDB
* Advanced SQL validation
* Interactive dashboards and charts
* Docker deployment
* Authentication and user management
* Query caching and optimization

## Learning Outcomes

This project demonstrates:

* Python backend development
* Database management using MySQL
* Prompt engineering for SQL generation
* MCP (Model Context Protocol) integration
* REST API development with Flask
* Secure handling of environment variables
* Application of AI in data engineering workflows

## Screenshots

### Query Results
![Home Page](screenshots/Screenshot%20(1).png)

### Home Page
![Query Results](screenshots/Screenshot%20(2).png)

### Query History
![Query History](screenshots/Screenshot%20(3).png)

### System Settings
![Architecture](screenshots/Screenshot%20(4).png)
