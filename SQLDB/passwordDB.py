import random,string,sqlite3,hashlib


async def savePassword(userId, password):
    try:
        salt = generate_salt(10)
        hashedPassword = generate_hash(password, salt)
        print("hashedPassword ",hashedPassword ,"salt ",salt )
        status = updatePasswordDB(userId, salt, hashedPassword)
        return status
    except Exception as ex:
        print("[password][savePassword]",ex)

async def create():
    try:

        def create_table(table_name, columns):
            # Establish a connection to the SQLite database
            conn = sqlite3.connect('Account.db')
            cursor = conn.cursor()

            # Construct the CREATE TABLE query
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"

            # Execute the query
            cursor.execute(query)

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

        # Example usage
        table_name = 'Passwords'
        columns = [
            'ID TEXT PRIMARY KEY',
            'SALT TEXT NOT NULL',
            'HASHED TEXT'
        ]

        create_table(table_name, columns)
    except Exception as ex:
        print("[password][create]",ex)

async def updatePasswordDB(userId, salt, hashedPassword):
    try:
        create()
        # Example usage
        table_name = 'Passwords'
        # fields = ['field1', 'field2', 'field3']
        fields = [userId,salt, hashedPassword]
        # conditions = {'category': 'books', 'price': 10}
        conditions = {}

        query = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in range(len(fields))])})"


        # if conditions :
        #     # Construct the query string
        #     query = f"SELECT {', '.join(fields)} FROM {table_name} WHERE "
        #     query += ' AND '.join(f"{key} = ?" for key in conditions)
        # else :
        #     query = f"SELECT {', '.join(fields)} FROM {table_name}"


        # Create the parameter tuple
        # params = tuple(conditions.values())

        results = execute_dynamic_query(query, fields)

        # Process the results
        for row in results:
            print(row)



    except Exception as ex :
        print("[password][updatePasswordDB]",ex)

    


async def generate_salt(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


async def generate_hash(string1, string2):
    concatenated_string = string1 + string2
    hash_object = hashlib.sha256()

    hash_object.update(concatenated_string.encode('utf-8'))
    hash_value = hash_object.hexdigest()

    return hash_value



async def validatePassword(userId, password):
    pass
    arr = getPassword(userId)

    



async def getPassword(userId):
    #get hashed password and salt
    pass


