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
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE trips (
            trip_id SERIAL PRIMARY KEY NOT NULL,
            planner VARCHAR(20) REFERENCES users(username) NOT NULL,
            trip_name VARCHAR(50) NOT NULL,
            city VARCHAR(50) NOT NULL,
            country VARCHAR(50) NOT NULL,
            start_date VARCHAR(50) NOT NULL,
            end_date VARCHAR(50) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE trips;
        """,
    ],
]
