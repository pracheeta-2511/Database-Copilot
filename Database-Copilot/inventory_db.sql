CREATE DATABASE inventory_db;
USE inventory_db;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10, 2),
    stock_quantity INT,
    last_restocked DATE
);

INSERT INTO products (name, category, price, stock_quantity, last_restocked) VALUES
('MacBook Pro 14', 'Electronics', 1999.00, 25, '2025-12-01'),
('Sony WH-1000XM5', 'Electronics', 349.99, 50, '2026-01-15'),
('Standing Desk', 'Furniture', 450.00, 10, '2025-11-20'),
('Coffee Grinder', 'Appliances', 85.00, 100, '2026-02-10');

CREATE TABLE IF NOT EXISTS query_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query_text TEXT,
    sql_executed TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

USE inventory_db;

INSERT INTO products (name, category, price, stock_quantity, last_restocked) VALUES
('iPhone 15 Pro', 'Electronics', 999.00, 40, '2026-01-10'),
('Samsung S24 Ultra', 'Electronics', 1199.00, 30, '2026-02-01'),
('Dell UltraSharp 27', 'Electronics', 580.00, 15, '2025-12-15'),
('AirPods Pro 2', 'Electronics', 249.00, 75, '2026-02-15'),
('Kindle Paperwhite', 'Electronics', 139.00, 60, '2026-01-20'),
('Ergonomic Keyboard', 'Electronics', 120.00, 25, '2025-11-30'),
('Herman Miller Aeron', 'Furniture', 1450.00, 8, '2025-10-05'),
('Bookshelf (Oak)', 'Furniture', 220.00, 20, '2026-01-05'),
('Standing Lamp', 'Furniture', 85.00, 45, '2026-02-12'),
('Air Fryer XXL', 'Appliances', 199.00, 35, '2026-02-18'),
('NutriBullet Pro', 'Appliances', 99.00, 50, '2026-01-25'),
('Dyson V15 Vacuum', 'Appliances', 749.00, 12, '2025-12-20'),
('Electric Kettle', 'Appliances', 45.00, 120, '2026-02-05'),
('Espresso Machine', 'Appliances', 899.00, 10, '2025-11-15'),
('Smart Thermostat', 'Home Automation', 249.00, 22, '2026-01-12'),
('Ring Video Doorbell', 'Home Automation', 180.00, 30, '2026-01-30');