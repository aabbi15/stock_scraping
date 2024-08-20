import psycopg2
from psycopg2 import sql

# Database connection parameters
dbname = 'stockdb'
user = 'postgres'
password = 'postgres'  # Replace with your actual password
host = 'localhost'
port = '5432'

# Sample data
data = [
    {
        "name": "Adani Ports and Special Economic Zone Ltd.",
        "Open": "863.90",
        "Previous Close": "858.15",
        "Volume": "8037324",
        "Value (Lacs)": "68678.93",
        "i\n VWAP": "860.52",
        "Beta": "1.80",
        "High": "869.00",
        "Low": "853.35",
        "UC Limit": "943.95",
        "LC Limit": "772.35",
        "52 Week High": "987.85",
        "52 Week Low": "395.10",
        "Face Value": "2",
        "Mkt Cap (Rs. Cr.)": "184583",
        "Dividend Yield": "0.59",
        "20D Avg Volume": "8226210",
        "20D Avg Delivery(%)": "37.55",
        "Book Value Per Share": "148.37",
        "TTM EPS ": "29.01\n(+35.56% YoY)",
        "TTM PE ": "29.46\n(Average PE)",
        "P/B ": "5.76\n(High P/B)",
        "Sector PE": "76.52",
    },
    {
        "name": "Asian Paints Ltd.",
        "Open": "3198.60",
        "Previous Close": "3182.30",
        "Volume": "377068",
        "Value (Lacs)": "11989.63",
        "i\n VWAP": "3182.58",
        "Beta": "0.39",
        "High": "3198.60",
        "Low": "3171.00",
        "UC Limit": "3500.50",
        "LC Limit": "2864.10",
        "52 Week High": "3582.90",
        "52 Week Low": "2685.85",
        "Face Value": "1",
        "Mkt Cap (Rs. Cr.)": "304996",
        "Dividend Yield": "0.81",
        "20D Avg Volume": "797418",
        "20D Avg Delivery(%)": "53.07",
        "Book Value Per Share": "148.03",
        "TTM EPS ": "48.37\n(+33.36% YoY)",
        "TTM PE ": "65.74\n(Low PE)",
        "P/B ": "21.48\n(Average P/B)",
        "Sector PE": "71.24",
    },
    # Add more data here...
]

# Function to insert data into the table
def insert_data(data):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()

        # SQL query to insert data
        insert_query = sql.SQL("""
            INSERT INTO stock_data (
                company_name, date, open, previous_close, volume, value_lacs, vwap, beta, market_cap_rs_cr, high, low,
                uc_limit, lc_limit, week_52_high, week_52_low, face_value, all_time_high, all_time_low, avg_volume_20d,
                avg_delivery_20d_percentage, book_value_per_share, dividend_yield, ttm_eps, ttm_eps_growth_percentage,
                ttm_pe, pe_type, pb, pb_type, sector_pe
            ) VALUES (
                %s, NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """)

        # Iterate over the data and insert each record
        for record in data:
            cur.execute(insert_query, (
                record["name"],
                float(record["Open"].replace(",", "")),
                float(record["Previous Close"].replace(",", "")),
                int(record["Volume"].replace(",", "")),
                float(record["Value (Lacs)"].replace(",", "")),
                float(record["i\n VWAP"].replace(",", "")),
                float(record["Beta"].replace(",", "")),
                float(record["Mkt Cap (Rs. Cr.)"].replace(",", "")),
                float(record["High"].replace(",", "")),
                float(record["Low"].replace(",", "")),
                float(record["UC Limit"].replace(",", "")),
                float(record["LC Limit"].replace(",", "")),
                float(record["52 Week High"].replace(",", "")),
                float(record["52 Week Low"].replace(",", "")),
                float(record["Face Value"].replace(",", "")),
                0,  # Placeholder for all_time_high
                0,  # Placeholder for all_time_low
                int(record["20D Avg Volume"].replace(",", "")),
                float(record["20D Avg Delivery(%)"].replace(",", "")),
                float(record["Book Value Per Share"].replace(",", "")),
                float(record["Dividend Yield"].replace(",", "")),
                float(record["TTM EPS "].split("\n")[0].replace(",", "")),
                float(record["TTM EPS "].split("\n")[1].strip("()% YoY").replace("+", "").replace(",", "")),
                float(record["TTM PE "].split("\n")[0].replace(",", "")),
                record["TTM PE "].split("\n")[1].strip("()"),
                float(record["P/B "].split("\n")[0].replace(",", "")),
                record["P/B "].split("\n")[1].strip("()"),
                float(record["Sector PE"].replace(",", ""))
            ))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        print("Data inserted successfully")

    except Exception as e:
        print(f"Error: {e}")

# Call the function to insert data
# insert_data(data)
