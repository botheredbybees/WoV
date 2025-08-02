Trigger pattern:

When a new image is uploaded to Supabase Storage (direct from UI or SvelteKit client), Supabase’s Storage Webhooks call an endpoint you expose (e.g., /batcher/notify).

This endpoint (could be a minimal Flask or FastAPI app within your exif-batcher container) writes the file path or ID into a pending_exif_jobs table in PostgreSQL.

The exif-batcher worker (polling or event-driven) picks up jobs from this table, downloads the images (using the Supabase Storage API), extracts EXIF (timestamp, GPS), and updates the relevant observation record. It also matches to underway sensor data if available.

Resource friendliness:

The batcher container only processes when new photos arrive (event or scheduled poll).

All heavy EXIF logic and context-matching in Python, but with the same containerization as the rest of your stack.

How Supabase Storage can call this
In Supabase project settings > Storage > Webhooks, set:

Event: File Created (OBJECT_CREATED)

URL: http://wov-exif-batcher:5000/webhook/file-upload (internal Docker network)
(If local: http://localhost:5000/webhook/file-upload, for test)

Configure your batcher to expose port 5000.