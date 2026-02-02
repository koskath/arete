import os
import aiomysql
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)


async def save_to_database(session_id, question, response, course=None):
    """
    Save chat history to MySQL database (async version).
    
    Args:
        session_id (str): The session identifier
        question (str): The user's question
        response (str): The assistant's response
        course (str, optional): The course identifier. Defaults to None.
    
    Returns:
        int: The ID of the inserted record, or None if insertion failed
    """
    connection = None
    
    try:
        # Get database credentials from environment variables
        connection = await aiomysql.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            db=os.getenv("MYSQL_DB"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )
        
        async with connection.cursor() as cursor:
            # Insert query
            insert_query = """
                INSERT INTO chat_history (session_id, course, question, response)
                VALUES (%s, %s, %s, %s)
            """
            
            # Execute insert
            await cursor.execute(insert_query, (session_id, course, question, response))
            await connection.commit()
            
            # Get the inserted record ID
            record_id = cursor.lastrowid
            print(f"Record saved successfully with ID: {record_id}")
            return record_id
            
    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
        
    finally:
        # Close connection
        if connection:
            await connection.ensure_closed()
            print("MySQL connection is closed")


async def update_feedback(record_id, feedback):
    """
    Update feedback for a chat history record.
    
    Args:
        record_id (int): The ID of the record to update
        feedback (str): The feedback value - "Chosen" for like, "Rejected" for dislike, or None
    
    Returns:
        bool: True if update was successful, False otherwise
    """
    connection = None
    
    try:
        # Get database credentials from environment variables
        connection = await aiomysql.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            db=os.getenv("MYSQL_DB"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )
        
        async with connection.cursor() as cursor:
            # Update query
            update_query = """
                UPDATE chat_history
                SET feedback = %s
                WHERE id = %s
            """
            
            # Execute update
            await cursor.execute(update_query, (feedback, record_id))
            await connection.commit()
            
            print(f"Feedback updated successfully for record ID: {record_id}")
            return True
            
    except Exception as e:
        print(f"Error while updating feedback: {e}")
        return False
        
    finally:
        # Close connection
        if connection:
            await connection.ensure_closed()
            print("MySQL connection is closed")
