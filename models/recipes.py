from app import db_manager

create_table_query = """
    CREATE TABLE IF NOT EXISTS recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    instruction TEXT NOT NULL,
    date_made DATE,
    under_half_hour TINYINT(1) DEFAULT 0,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

"""

db_manager.query(create_table_query)
