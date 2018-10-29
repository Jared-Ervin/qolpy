from sqlalchemy import create_engine
import pandas as pd


def ez_connect(
    db_type="mssql", win_auth=True, username="", password="", port="", database=""
):

    """
    Function generates the appropriate connection string of the
    database you would like to connect to.

    Keyword Arguments:
        db_type {str} -- The type of database you are connecting
        to. (default: {"mssql"}):
            * mssql
            * postgresql
            * mysql
        win_auth {bool} -- Do you authenticate to the sql server
        through the logged in windows user. If you need to sepcify
        a username and password, change to false (default: {True})
        username {str} -- Username for authenticating to sql server
        (default: {""})
        password {str} -- Password for authenticating to sql server
        (default: {""})
        port {str} -- The name of the server you are attempting to query
        (default: {""})
        database {str} --  The name of the database you are attempting
        to query (default: {""})

    Raises:
        Exception -- Invalid or unsupported database type

    Returns:
        sqlalchemy.engine.base.Engine -- An Engine object used to connect to
        the specified database
    """

    if win_auth:
        dbdict = {
            "mssql": f"mssql+pyodbc://mssql+pyodbc://@sqlserver",
            "postgresql": f"postgresql://@{[port]}/{database}",
            "mysql": f"mysql://@{port}/{database}",
        }
    else:
        dbdict = {
            "mssql": f"mssql+pyodbc://{username}:{password}@{port}/{database}",
            "postgresql": f"postgresql://{username}:{password}@{[port]}/{database}",
            "mysql": f"mysql://{username}:{password}@{port}/{database}",
        }

    if db_type in dbdict:
        con_string = dbdict[db_type]
        engine = create_engine(con_string)
        return engine
    else:
        raise Exception("Invalid or unsupported database type")


def ez_execute(query, engine):

    """
    Function takes a query string and an engine object
    and returns a dataframe on the condition that the
    sql query returned any rows.

    Arguments:
        query {str} -- a Sql query string
        engine {sqlalchemy.engine.base.Engine} -- a database engine object
        to run the query

    Returns:
        DataFrame -- A dataframe containing the results of executing the
        sql query with the specified engine
    """

    data = pd.read_sql_query(query, engine)
    assert not data.empty, "Query returned no results"

    return data


print(
    ez_execute(
        "select top 10 * from hmwallacedata.dbo.netsuitetransactions", ez_connect()
    )
)

