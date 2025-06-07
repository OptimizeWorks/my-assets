# Static Assets

This repository contains static assets exported from Webflow for the Latino Family Connections website.

## Knack Database Integration

The front‑end is expected to interact with a Knack database for dynamic content. Communication with the database will happen via the [Knack REST API](https://docs.knack.com/docs). The following endpoints will be used:

- **List records:** `GET $KNACK_BASE_URL/objects/{object_key}/records`
- **Get a record:** `GET $KNACK_BASE_URL/objects/{object_key}/records/{record_id}`
- **Create a record:** `POST $KNACK_BASE_URL/objects/{object_key}/records`
- **Update a record:** `PUT $KNACK_BASE_URL/objects/{object_key}/records/{record_id}`
- **Delete a record:** `DELETE $KNACK_BASE_URL/objects/{object_key}/records/{record_id}`

Authentication headers require the application's ID and an API key.
The following environment variables should be provided:

```text
KNACK_APPLICATION_ID=<your app id>
KNACK_API_KEY=<an API key with access to the app>
KNACK_BASE_URL=https://api.knack.com/v1
```

## Configuration Files

Create a `.env` file in the project root to supply credentials and other settings. An example is shown below:

```env
KNACK_APPLICATION_ID=abc123
KNACK_API_KEY=secret-key
KNACK_BASE_URL=https://api.knack.com/v1
```

The build or runtime scripts should load this file so API calls can be authenticated. Do not commit the `.env` file to version control.
