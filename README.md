# lottery-service


[![CircleCI](https://circleci.com/gh/NayaraCaetano/lottery-service.svg?style=svg)](https://circleci.com/gh/NayaraCaetano/lottery-service)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/276e8d3f75eb4ca18931cbcf62f54cb6)](https://www.codacy.com/app/NahCaetano/lottery-service?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=NayaraCaetano/lottery-service&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/276e8d3f75eb4ca18931cbcf62f54cb6)](https://www.codacy.com/app/NahCaetano/lottery-service?utm_source=github.com&utm_medium=referral&utm_content=NayaraCaetano/lottery-service&utm_campaign=Badge_Coverage)


Micro service that receives a list of items and choose one between them storing a log


## Quick start


`docker-compose up --build`

The API will be available in `localhost:8000`


## Executing tests

`docker exec -it lottery-service_lottery_1 pytest`

## Documentation

The API documentation is available at endpoints:

`\swagger`

`\redoc`
