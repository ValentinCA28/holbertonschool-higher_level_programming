#!/usr/bin/env python3
"""Flask application with JSON, CSV, and SQLite data sources."""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        product_list = read_json()
    elif source == 'csv':
        product_list = read_csv()
    elif source == 'sql':
        product_list = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        product_list = [p for p in product_list if p['id'] == product_id]
        if not product_list:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=product_list)


def read_json():
    """Read product data from JSON file."""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Read product data from CSV file."""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql():
    """Read product data from SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1],
             "category": row[2], "price": row[3]} for row in rows]


if __name__ == '__main__':
    app.run(debug=True, port=5000)
