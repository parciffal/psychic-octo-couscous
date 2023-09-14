from app import db_manager


create_table_query = """
        CREATE TABLE IF NOT EXISTS Category (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tittle VARCHAR(100) NOT NULL
        )
        """

db_manager.query(create_table_query)
