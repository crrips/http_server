# HTTP server

## Description
HTTP server with one endpoint for processing requests. This endpoint will accept an identifier and check its existing in the database. If a record with the passed identifier is not in the database, the server must send a notification in Telegram to the administrator of the bot with this identifier.

## Usage
1. Open config.py in the config directory
2. Replace values with your bot token and your id (you can use @BotFather and @userinfobot to find out it)
3. Run the docker-compose
```bash
docker-compose up
```
4. Send GET-request to server (for example, you can use Postman)
```
http://127.0.0.1:5000/?id=42
```
Instead of '42' you can write identifier which you want to check. Currently, database contains '0' and '42', it means if you will write this identifiers, the notification in Telegram will not be sent
