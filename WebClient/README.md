# Project SCARS

Project SCARS is a School Canteen Automated Reporting System for the Department
of Education (DepEd) Schools Division Office (SDO) of the City of Baliwag in
the Philippines.

![Web Client Tests](https://github.com/Chris1320/inTransit/actions/workflows/web-client-tests.yml/badge.svg)

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
