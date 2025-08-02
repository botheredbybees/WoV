from flask import Flask, request, jsonify
import os
import threading

app = Flask(__name__)

# This should reference a database or queue in your actual system.
PENDING_UPLOADS = []

@app.route('/webhook/file-upload', methods=['POST'])
def handle_upload():
    data = request.get_json()
    # Supabase will POST something like {"type":"OBJECT_CREATED","record":{"name":"photos/IMG_1234.JPG","bucket":"photo-uploads", ...}}
    try:
        record = data.get('record', {})
        file_path = record.get('name')
        bucket = record.get('bucket')
        # For prototype: just print and append to in-memory
        print(f"Received upload event: {file_path} in {bucket}")
        PENDING_UPLOADS.append((bucket, file_path))
        # Later: insert into pending_exif_jobs table/queue here!
        return jsonify({"status": "queued"}), 200
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"error": str(e)}), 400

def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # Run Flask in a thread, keep main process free for polling if needed.
    threading.Thread(target=run_flask).start()
