import json

from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
  DeleteRowsEvent,
  UpdateRowsEvent,
  WriteRowsEvent,
)

def main():
  stream = BinLogStreamReader(
    connection_settings= {
      "host": "mysql",
      "port": 3306,
      "user": "root",
      "passwd": "debezium"
    },
    server_id=100,
    blocking=True,
    resume_stream=True,
    only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent])

  for binlogevent in stream:
    for row in binlogevent.rows:
      event = {"schema": binlogevent.schema,
      "table": binlogevent.table,
      "type": type(binlogevent).__name__,
      "row": row
      }

      print(json.dumps(event))


if __name__ == "__main__":
   main()