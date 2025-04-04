# Project SCARS

Project SCARS is a School Canteen Automated Reporting System for the Department
of Education (DepEd) Schools Division Office (SDO) of the City of Baliwag in
the Philippines.

![Central Server Tests](https://github.com/Chris1320/inTransit/actions/workflows/central-server-tests.yml/badge.svg)
![Local Server Tests](https://github.com/Chris1320/inTransit/actions/workflows/local-server-tests.yml/badge.svg)
![Web Client Tests](https://github.com/Chris1320/inTransit/actions/workflows/web-client-tests.yml/badge.svg)
![Linter Results](https://github.com/Chris1320/inTransit/actions/workflows/lint.yml/badge.svg)

## Development

### Stacks

| Component      | Stack                                                                                              |
| -------------- | -------------------------------------------------------------------------------------------------- |
| Central Server | [![Central Server Stack](https://skillicons.dev/icons?i=py,fastapi,mysql,docker)](#central-server) |
| Local Server   | [![Local Server Stack](https://skillicons.dev/icons?i=py,fastapi,sqlite,arduino)](#local-server)   |
| Web Client     | [![Web Client Stack](https://skillicons.dev/icons?i=ts,react,tailwind,nextjs)](#web-client)        |

#### Central Server

The central server is written in Python using the FastAPI framework and
utilizes MySQL as its database. It is responsible for handling the
backend logic and storing the submitted data of canteen managers.

##### Central Server Requirements

The central server is written in [Python](https://python.org) v3.13.1, and is
managed using [uv](https://github.com/astral-sh/uv) v0.5.24.
If you are using [Docker](https://docker.com/) or [Podman](https://podman.io/),
make sure to also install [docker-compose](https://docs.docker.com/compose/)/[podman-compose](https://github.com/containers/podman-compose).
Otherwise, install [MySQL](http://www.mysql.com/) 9.2.0-1.el9 if don't plan to
use the SQLite database.

##### Central Server Development Setup

1. Install the required software.
2. Clone the repository.

   ```bash
   git clone https://github.com/Chris1320/ProjectSCARS.git
   ```

3. Navigate to the `CentralServer` directory.

   ```bash
   cd ProjectSCARS/CentralServer
   ```

4. Install dependencies.

   ```bash
   uv sync
   ```

5. Copy and edit the configuration file.

   ```bash
   cp .config.example.json config.json
   uv run ./scripts/secret.py  # Generate a secure secret key
                               # and write it to `config.json`
   ```

   Edit the `config.json` file to set the database connection string or to use
   the local SQLite database.

6. If you are using the containerized version of MySQL, run the following
   command to start the database container. Otherwise, manually start the
   database server if `debug.use_test_db` is set to `false` in `config.json`.

   ```bash
   cd ./db
   docker-compose up -d
   cd ..
   ```

7. Run the FastAPI development server.

   ```bash
   uv run fastapi dev centralserver
   ```

#### Local Server

The local server is also written in Python using the FastAPI framework.
SQLite is used as its database which is sufficient for local database
transactions while providing a lightweight solution. The local server
is responsible for providing inventory management and sales functionality
to the web client. It also serves as a bridge between the web client
and the canteen membership module.

#### Web Client

The web client is written in TypeScript using the Next.js framework. It
is the user-facing application that allows canteen managers to submit
their monthly financial reports to the central server. The web client
also optionally communicates with the local server to provide inventory
and sales functionality.

##### Web Client Requirements

The web client is written in TypeScript v5,
and is run via [NodeJS](https://nodejs.org) v23.6.0.

##### Web Client Development Setup

1. Install the required software.
2. Clone the repository.

   ```bash
   git clone https://github.com/Chris1320/ProjectSCARS.git
   ```

3. Navigate to the `WebClient` directory.

   ```bash
   cd ProjectSCARS/WebClient
   ```

4. Install dependencies.

   ```bash
   npm install
   ```

5. Run the development server.

   ```bash
   npm run dev
   ```
