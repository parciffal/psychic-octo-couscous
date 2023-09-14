from app import db_manager


create_table_query = """
        CREATE TABLE IF NOT EXISTS Product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category_id INT NOT NULL,
            count INT DEFAULT 0,
            price FLOAT NOT NULL,
            material VARCHAR(500),
            FOREIGN KEY (category_id) REFERENCES category(id)
        )
        """

# db_manager.query(create_table_query)
