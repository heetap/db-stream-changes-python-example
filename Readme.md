**How To Run**

1. run `docker-compose build`
2. run `docker-compose up -d`
3. run `docker-compose exec app bash`

**How To Run Debezium**

1. create connector `curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "inventory-connector", "config": { "connector.class": "io.debezium.connector.mysql.MySqlConnector", "tasks.max": "1", "database.hostname": "mysql", "database.port": "3306", "database.user": "debezium", "database.password": "dbz", "database.server.id": "184054", "database.server.name": "dbserver1", "database.whitelist": "inventory", "database.history.kafka.bootstrap.servers": "kafka:9092", "database.history.kafka.topic": "dbhistory.inventory" } }'`
2. run `python debezium.py`

**How To Run bin log streamer**
1. run `python mysql-streamer.py`