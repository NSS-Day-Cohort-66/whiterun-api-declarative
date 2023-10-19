import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class DocksView():

    def add(self, handler, dock_data):

        sql = """
        INSERT INTO 'Dock' VALUES (null, ?, ?)
        """
        number_of_rows_created = db_create(
            sql,
            (dock_data['location'], dock_data['capacity']))
        response_sql = "SELECT id, location, capacity FROM DOCK"
        query_results = db_get_all(response_sql)
        row_docks = [dict(row) for row in query_results]
        response_docks = json.dumps(row_docks)
        if number_of_rows_created > 0:
            return handler.response(response_docks, status.HTTP_201_SUCCESS_CREATED.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
    def get(self, handler, pk):
        if pk != 0:
            sql = """
            SELECT
                d.id,
                d.location,
                d.capacity
            FROM Dock d
            WHERE d.id = ?
            """
            query_results = db_get_single(sql, pk)
            serialized_hauler = json.dumps(dict(query_results))

            return handler.response(serialized_hauler, status.HTTP_200_SUCCESS.value)
        else:

            query_results = db_get_all("SELECT d.id, d.location, d.capacity FROM Dock d")
            haulers = [dict(row) for row in query_results]
            serialized_haulers = json.dumps(haulers)

            return handler.response(serialized_haulers, status.HTTP_200_SUCCESS.value)

    def delete(self, handler, pk):
        number_of_rows_deleted = db_delete("DELETE FROM Dock WHERE id = ?", pk)

        if number_of_rows_deleted > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def update(self, handler, dock_data, pk):
        sql = """
        UPDATE Dock
        SET
            location = ?,
            capacity = ?
        WHERE id = ?
        """
        number_of_rows_updated = db_update(
            sql,
            (dock_data['location'], dock_data['capacity'], pk)
        )

        if number_of_rows_updated > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
