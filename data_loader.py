#!/usr/bin/env python3
"""
Script to download Olist Brazilian E-Commerce Public Dataset
"""

import os
import urllib.request
import zipfile
import pandas as pd

def download_olist_data():
    """Download the Olist dataset if not already present"""
    
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Check if we already have the CSV files
    csv_files = [
        'olist_orders_dataset.csv',
        'olist_order_items_dataset.csv',
        'olist_order_payments_dataset.csv',
        'olist_order_reviews_dataset.csv',
        'olist_products_dataset.csv',
        'olist_customers_dataset.csv',
        'olist_sellers_dataset.csv',
        'olist_geolocation_dataset.csv',
        'product_category_name_translation.csv'
    ]
    
    all_files_exist = all(os.path.exists(os.path.join(data_dir, f)) for f in csv_files)
    
    if not all_files_exist:
        print("Downloading Olist dataset...")
        # Kaggle dataset URL (requires Kaggle API)
        # Alternative: Use a direct URL if available, or manual download
        print("Please download the Olist Brazilian E-Commerce dataset from:")
        print("https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce")
        print("Extract the CSV files to the 'data' directory")
        return False
    
    return True

def load_data():
    """Load all Olist datasets into pandas DataFrames"""
    
    if not download_olist_data():
        # For demo purposes, let's create some sample data that matches the schema
        print("Creating sample data for demonstration...")
        return create_sample_data()
    
    data_dir = "data"
    
    # Load all datasets
    datasets = {}
    
    try:
        datasets['orders'] = pd.read_csv(os.path.join(data_dir, 'olist_orders_dataset.csv'))
        datasets['order_items'] = pd.read_csv(os.path.join(data_dir, 'olist_order_items_dataset.csv'))
        datasets['order_payments'] = pd.read_csv(os.path.join(data_dir, 'olist_order_payments_dataset.csv'))
        datasets['order_reviews'] = pd.read_csv(os.path.join(data_dir, 'olist_order_reviews_dataset.csv'))
        datasets['products'] = pd.read_csv(os.path.join(data_dir, 'olist_products_dataset.csv'))
        datasets['customers'] = pd.read_csv(os.path.join(data_dir, 'olist_customers_dataset.csv'))
        datasets['sellers'] = pd.read_csv(os.path.join(data_dir, 'olist_sellers_dataset.csv'))
        datasets['geolocation'] = pd.read_csv(os.path.join(data_dir, 'olist_geolocation_dataset.csv'))
        datasets['category_translation'] = pd.read_csv(os.path.join(data_dir, 'product_category_name_translation.csv'))
        
        print("Data loaded successfully!")
        return datasets
        
    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        print("Creating sample data for demonstration...")
        return create_sample_data()

def create_sample_data():
    """Create sample datasets for demonstration"""
    import numpy as np
    from datetime import datetime, timedelta
    
    np.random.seed(42)
    
    # Sample data creation (minimal structure for demo)
    n_orders = 1000
    n_customers = 800
    n_products = 200
    
    # Generate sample orders
    orders = pd.DataFrame({
        'order_id': [f'order_{i}' for i in range(n_orders)],
        'customer_id': [f'customer_{np.random.randint(0, n_customers)}' for _ in range(n_orders)],
        'order_status': np.random.choice(['delivered', 'shipped', 'canceled', 'processing'], n_orders, p=[0.85, 0.10, 0.03, 0.02]),
        'order_purchase_timestamp': [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(n_orders)],
        'order_approved_at': [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(n_orders)],
        'order_delivered_carrier_date': [datetime.now() - timedelta(days=np.random.randint(0, 30)) for _ in range(n_orders)],
        'order_delivered_customer_date': [datetime.now() - timedelta(days=np.random.randint(0, 20)) for _ in range(n_orders)],
        'order_estimated_delivery_date': [datetime.now() + timedelta(days=np.random.randint(5, 30)) for _ in range(n_orders)]
    })
    
    # Generate sample order items
    n_items = n_orders * 2  # Average 2 items per order
    order_items = pd.DataFrame({
        'order_id': [f'order_{np.random.randint(0, n_orders)}' for _ in range(n_items)],
        'order_item_id': range(1, n_items + 1),
        'product_id': [f'product_{np.random.randint(0, n_products)}' for _ in range(n_items)],
        'seller_id': [f'seller_{np.random.randint(0, 100)}' for _ in range(n_items)],
        'shipping_limit_date': [datetime.now() + timedelta(days=np.random.randint(1, 10)) for _ in range(n_items)],
        'price': np.random.uniform(10, 500, n_items),
        'freight_value': np.random.uniform(5, 50, n_items)
    })
    
    # Generate sample payments
    order_payments = pd.DataFrame({
        'order_id': [f'order_{i}' for i in range(n_orders)],
        'payment_sequential': np.ones(n_orders),
        'payment_type': np.random.choice(['credit_card', 'boleto', 'debit_card', 'voucher'], n_orders, p=[0.7, 0.2, 0.08, 0.02]),
        'payment_installments': np.random.choice([1, 2, 3, 4, 5, 6], n_orders, p=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05]),
        'payment_value': np.random.uniform(20, 600, n_orders)
    })
    
    # Generate sample reviews
    order_reviews = pd.DataFrame({
        'review_id': [f'review_{i}' for i in range(n_orders)],
        'order_id': [f'order_{i}' for i in range(n_orders)],
        'review_score': np.random.choice([1, 2, 3, 4, 5], n_orders, p=[0.05, 0.05, 0.15, 0.25, 0.5]),
        'review_comment_title': [''] * n_orders,
        'review_comment_message': [''] * n_orders,
        'review_creation_date': [datetime.now() - timedelta(days=np.random.randint(0, 30)) for _ in range(n_orders)],
        'review_answer_timestamp': [datetime.now() - timedelta(days=np.random.randint(0, 25)) for _ in range(n_orders)]
    })
    
    # Generate sample products
    categories = ['bed_bath_table', 'health_beauty', 'sports_leisure', 'computer_accessories', 
                  'furniture_decor', 'housewares', 'watches_gifts', 'telephony', 'auto', 
                  'fashion_bags_accessories']
    
    products = pd.DataFrame({
        'product_id': [f'product_{i}' for i in range(n_products)],
        'product_category_name': np.random.choice(categories, n_products),
        'product_name_lenght': np.random.randint(10, 100, n_products),
        'product_description_lenght': np.random.randint(100, 1000, n_products),
        'product_photos_qty': np.random.randint(1, 10, n_products),
        'product_weight_g': np.random.randint(100, 5000, n_products),
        'product_length_cm': np.random.randint(5, 100, n_products),
        'product_height_cm': np.random.randint(5, 50, n_products),
        'product_width_cm': np.random.randint(5, 50, n_products)
    })
    
    # Generate other datasets (minimal)
    customers = pd.DataFrame({
        'customer_id': [f'customer_{i}' for i in range(n_customers)],
        'customer_unique_id': [f'unique_customer_{i}' for i in range(n_customers)],
        'customer_zip_code_prefix': np.random.randint(10000, 99999, n_customers),
        'customer_city': ['São Paulo'] * n_customers,
        'customer_state': ['SP'] * n_customers
    })
    
    sellers = pd.DataFrame({
        'seller_id': [f'seller_{i}' for i in range(100)],
        'seller_zip_code_prefix': np.random.randint(10000, 99999, 100),
        'seller_city': ['São Paulo'] * 100,
        'seller_state': ['SP'] * 100
    })
    
    geolocation = pd.DataFrame({
        'geolocation_zip_code_prefix': np.random.randint(10000, 99999, 1000),
        'geolocation_lat': np.random.uniform(-30, -10, 1000),
        'geolocation_lng': np.random.uniform(-60, -40, 1000),
        'geolocation_city': ['São Paulo'] * 1000,
        'geolocation_state': ['SP'] * 1000
    })
    
    category_translation = pd.DataFrame({
        'product_category_name': categories,
        'product_category_name_english': [
            'bed_bath_table', 'health_beauty', 'sports_leisure', 'computer_accessories',
            'furniture_decor', 'housewares', 'watches_gifts', 'telephony', 'auto',
            'fashion_bags_accessories'
        ]
    })
    
    return {
        'orders': orders,
        'order_items': order_items,
        'order_payments': order_payments,
        'order_reviews': order_reviews,
        'products': products,
        'customers': customers,
        'sellers': sellers,
        'geolocation': geolocation,
        'category_translation': category_translation
    }

if __name__ == "__main__":
    datasets = load_data()
    print("Available datasets:", list(datasets.keys()))
    for name, df in datasets.items():
        print(f"{name}: {df.shape}")