import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class ShippingShipsView():

    def get(self, handler, pk):
        if pk != 0:
            sql = "SELECT s.id, s.name, s.hauler_id FROM Ship s WHERE s.id = ?"
            query_results = db_get_single(sql, pk)
            serialized_hauler = json.dumps(dict(query_results))

            return handler.response(serialized_hauler, status.HTTP_200_SUCCESS.value)
        else:

            sql = "SELECT s.id, s.name, s.hauler_id FROM Ship s"
            query_results = db_get_all(sql)
            haulers = [dict(row) for row in query_results]
            serialized_haulers = json.dumps(haulers)

            return handler.response(serialized_haulers, status.HTTP_200_SUCCESS.value)

    def delete(self, handler, pk):
        number_of_rows_deleted = db_delete("DELETE FROM Ship WHERE id = ?", pk)

        if number_of_rows_deleted > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def update(self, handler, ship_data, pk):
        sql = """
        UPDATE Ship
        SET
            name = ?,
            hauler_id = ?
        WHERE id = ?
        """
        number_of_rows_updated = db_update(
            sql,
            (ship_data['name'], ship_data['hauler_id'], pk)
        )

        if number_of_rows_updated > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
