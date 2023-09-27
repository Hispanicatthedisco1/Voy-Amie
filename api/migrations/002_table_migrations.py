steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(20) NOT NULL UNIQUE,
            password VARCHAR(20) NOT NULL,
            email VARCHAR(100) NOT NULL,
            bio TEXT,
            profile_pic TEXT
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """
    ]
]
