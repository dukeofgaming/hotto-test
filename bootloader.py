import mysql.connector
import os

def drop_all_tables(cursor, conn):
    print("RESET_DB is true; dropping all tables...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    for (table_name,) in tables:
        cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`;")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    conn.commit()
    print("All tables dropped.")

def execute_statements_from_file(cursor, conn, filename, description):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        for statement in content.split(';'):
            stmt = statement.strip()
            if stmt:
                cursor.execute(stmt)
        conn.commit()
        print(f"{description} loaded from {filename}.")
    except FileNotFoundError:
        print(f"{filename} not found, skipping {description.lower()} loading.")

def print_tables(cursor):
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Current tables in database:")
    for (table_name,) in tables:
        print(f"- {table_name}")
    return tables

def bootloader(db_config, schema_file='schema_ddl.sql', fixtures_file='fixtures.sql'):
    """
    Checks if the database schema is empty. If so, creates tables from schema_ddl.sql.
    Loads fixtures from fixtures.sql if present.
    Always prints the list of tables in the database.
    """
    import os
    reset_db = os.getenv('RESET_DB', 'false').strip().lower() in ('1', 'true', 'yes', 'on')
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        if reset_db:
            drop_all_tables(cursor, conn)
        tables = print_tables(cursor)
        if not tables:
            execute_statements_from_file(cursor, conn, schema_file, 'Database schema')
            execute_statements_from_file(cursor, conn, fixtures_file, 'Fixtures')
            tables = print_tables(cursor)
        else:
            print("Database already initialized.")
            print_tables(cursor)
    except Exception as e:
        print(f"Bootloader error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
