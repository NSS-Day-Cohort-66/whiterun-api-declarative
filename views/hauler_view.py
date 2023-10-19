import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class HaulerView():

    def add(self, handler, hauler_data):
        sql = """
        INSERT INTO 'Hauler' VALUES (null, ?, ?)
        """
        number_of_rows_created = db_create(
            sql,
            (hauler_data['name'], hauler_data['dock_id']))
        if number_of_rows_created > 0:
            return handler.response("", status.HTTP_201_SUCCESS_CREATED.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def get(self, handler, pk):
        parsed_url = handler.parse_url(handler.path)
        if pk != 0:
            if '_expand' in parsed_url['query_params'] and 'docks' in parsed_url['query_params']['_expand']:
                sql = """SELECT 
                h.id,
                h.name,
                h.dock_id,
                d.id AS dockId,
                d.location,
                d.capacity
                FROM Hauler h
                JOIN Dock d
				ON h.dock_id = dockId
				WHERE h.id = ?
                """
                query_results = db_get_single(sql,pk)

                dock = {
                        "id": query_results['dockId'],
                        "location": query_results['location'],
                        "capacity": query_results['capacity']
                    }
                hauler = {
                        "id": query_results['id'],
                        "name": query_results['name'],
                        "dock_id": query_results['dock_id'],
                        "dock": dock
                    }

                serialized_hauler = json.dumps(dict(hauler))
            else:
                sql = "SELECT h.id, h.name, h.dock_id FROM Hauler h WHERE h.id = ?"
                query_results = db_get_single(sql, pk)
                serialized_hauler = json.dumps(dict(query_results))

            return handler.response(serialized_hauler, status.HTTP_200_SUCCESS.value)
        else:

            sql = "SELECT h.id, h.name, h.dock_id FROM Hauler h"
            query_results = db_get_all(sql)
            haulers = [dict(row) for row in query_results]
            serialized_haulers = json.dumps(haulers)

            return handler.response(serialized_haulers, status.HTTP_200_SUCCESS.value)

    def delete(self, handler, pk):
        number_of_rows_deleted = db_delete("DELETE FROM Hauler WHERE id = ?", pk)

        if number_of_rows_deleted > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def update(self, handler, hauler_data, pk):
        sql = """
        UPDATE Hauler
        SET
            name = ?,
            dock_id = ?
        WHERE id = ?
        """
        number_of_rows_updated = db_update(
            sql,
            (hauler_data['name'], hauler_data['dock_id'], pk)
        )

        if number_of_rows_updated > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
