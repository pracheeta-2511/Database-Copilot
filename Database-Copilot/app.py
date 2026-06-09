import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY") 

def get_db_connection():
    return mysql.connector.connect(
        host="DB_HOST",
        user="DB_USER",
        password="DB_PASSWORD",
        database="DB_NAME"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query')
    try:
        sql_prompt = f"Table: products (id, name, category, price, stock_quantity). Question: {user_query}. Return ONLY SQL code, no backticks."
        
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": sql_prompt}]
        )
        
        generated_sql = completion.choices[0].message.content.strip().replace("```sql", "").replace("```", "")
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(generated_sql)
        rows = cursor.fetchall()
        
        cursor.execute("INSERT INTO query_history (query_text, sql_executed) VALUES (%s, %s)", (user_query, generated_sql))
        conn.commit()
        
        summary_prompt = f"User asked: {user_query}. Result: {rows}. Summarize in one professional sentence."
        summary_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": summary_prompt}]
        )
        
        answer = summary_completion.choices[0].message.content
        conn.close()
        
        return jsonify({"answer": answer, "sql": generated_sql, "raw_data": rows})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/history', methods=['GET'])
def get_history():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT query_text, sql_executed, DATE_FORMAT(created_at, '%H:%i') as time FROM query_history ORDER BY id DESC LIMIT 5")
    history = cursor.fetchall()
    conn.close()
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)
