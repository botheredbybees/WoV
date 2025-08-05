📸 EXIF/Context Batcher Design
This document details the design and workflow of the exif-batcher service, which automates the extraction of EXIF metadata from uploaded images and integrates it with observational and sensor data.

How it Works: Trigger Pattern
The exif-batcher operates on an event-driven model, triggered by new image uploads to Supabase Storage. This ensures near real-time processing of observation photos.

User Uploads Photo: A user uploads a photo via the SvelteKit web application to a designated bucket in Supabase Storage (e.g., photo-uploads).

Supabase Storage Webhook: Supabase Storage is configured to trigger a webhook (OBJECT_CREATED event) when a new file is created.

Webhook Routing (via Kong): The webhook POSTs an event JSON payload to a specific endpoint exposed by your exif-batcher service. This routing is handled by the Kong API Gateway, which directs the internal Docker network traffic.

exif-batcher Receives Event: The exif-batcher (a Python application, likely Flask or FastAPI) receives the webhook event.

Process and Annotate: The batcher then:

Downloads the newly uploaded image from Supabase Storage using the provided file path or ID.

Extracts EXIF metadata (e.g., datetime_original, GPS coordinates, camera model).

Looks up the nearest matching underway sensor data (e.g., sea surface temperature, wind speed) by timestamp.

Updates and annotates the associated observation record in the PostgreSQL database (wov.wov_observations and wov.wov_images tables) with the extracted EXIF and sensor context.

Records the processing status or flags the image for review if EXIF extraction or context matching fails.

Resource Friendliness
This event-driven architecture ensures efficient resource utilization:

The exif-batcher container only processes data when new photos arrive, avoiding constant polling or unnecessary resource consumption.

All heavy EXIF logic and context-matching are handled in Python within a dedicated container, maintaining separation of concerns and preventing performance bottlenecks in other services.

The entire workflow operates within the local Docker network, ensuring true offline capabilities and high performance at sea.

Configuration: How Supabase Storage Calls the Batcher
To enable this webhook integration, you will configure Supabase Storage within your local Supabase Studio dashboard:

Access Supabase Studio: Navigate to http://localhost:54323/project/default/storage/buckets.

Select your bucket: Choose the bucket designated for photo uploads (e.g., photo-uploads).

Configure Webhook: Go to the "Webhooks" settings for that bucket.

Event: Select File Created (OBJECT_CREATED).

URL: Set this to the internal Docker network address of your exif-batcher service. Assuming your exif-batcher container is named wov_exif-batcher and exposes port 5000 internally for its webhook endpoint (e.g., /webhook/file-upload), the URL would be:
http://wov_exif-batcher:5000/webhook/file-upload
(For local testing outside the Docker network, if needed, you might temporarily use http://localhost:5005/webhook/file-upload if your docker-compose.yaml maps 5005 to 5000 for the exif-batcher service).

Secret: (Optional but recommended) Provide a shared secret to verify webhook authenticity. This secret should also be configured in your exif-batcher application.

Batcher Port Exposure: Ensure your exif-batcher Docker service is configured to expose the necessary port (e.g., 5000) for the webhook listener. This is usually defined in your docker-compose.yaml (or docker-compose.override.yaml if you're using that pattern).