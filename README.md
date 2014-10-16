teyb Dialog System Testing Framework
====================================

This project is a web-service for testing of dialog systems over the Internet. The idea is that dialog system creators can share simulators for the same task and `teyb` will act as a proxy for continuous objective testing of dialog systems.

## API

```
POST /tasks/:task_id/dialogs/
    - Params:
        - API key
        - System ID
        - System DA
    - Result:
        - Dialog ID
        - User DA
    - Status codes:
        - 200: Created
        - 500: Error on server
        - 504: Error with user simulator

PATCH /tasks/:task_id/dialogs/:dialog_id/
    - Params:
        - System DA
    - Result:
        - User DA
    - Status codes:
        - 200: OK
        - 504: Error with user simulator
```
