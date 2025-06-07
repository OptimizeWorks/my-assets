# My Assets

This repository contains static assets for the project website.

## Knack Database Integration

The project communicates with a Knack database using Knack's REST API. Requests are sent to the API base URL, typically `https://api.knack.com/v1`.

Common endpoints include:

- `GET /v1/objects/{object_key}/records` – retrieve records
- `POST /v1/objects/{object_key}/records` – create a new record
- `PUT /v1/objects/{object_key}/records/{record_id}` – update a record

Replace `{object_key}` and `{record_id}` with the values from your Knack app. Each request must include your application ID and an API key in the HTTP headers.

Environment variables used by the application:

- `KNACK_APP_ID` – your Knack application ID
- `KNACK_API_KEY` – a REST API key generated in Knack
- `KNACK_BASE_URL` – optional override of the default base URL

These variables are loaded from a configuration file during development.

## Configuration Files

Create a `.env` file in the project root with your Knack credentials:

```bash
KNACK_APP_ID=your-app-id
KNACK_API_KEY=your-api-key
KNACK_BASE_URL=https://api.knack.com/v1
```

Additional configuration files may be added if the project integrates with other services.

