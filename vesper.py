import os
import time
import logging
from datetime import datetime

# Setup Logging for the Night Shift
logging.basicConfig(
    filename='vesper_upload.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_night_batch(source_dir, completed_dir):
    """Handles the night-to-morning batch upload sequence."""
    logging.info("Vesper AI activated. Night batch sequence initiated.")
    
    # Ensure folders exist
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(completed_dir, exist_ok=True)
    
    batch_files = os.listdir(source_dir)
    
    if not batch_files:
        print("Status: No files in the night batch queue. Standing by.")
        logging.info("Queue empty. Waiting for batch files.")
        return

    print(f"Vesper System: Found {len(batch_files)} files. Starting batch upload...")
    
    for filename in batch_files:
        source_path = os.path.join(source_dir, filename)
        upload_path = os.path.join(completed_dir, filename)
        
        try:
            print(f"Uploading: {filename}...")
            logging.info(f"Processing {filename}...")
            
            # Simulating API upload and moving file to completed folder
            time.sleep(2) 
            os.rename(source_path, upload_path)
            
            print(f"Success: {filename}")
            logging.info(f"Successfully uploaded: {filename}")
            
        except Exception as e:
            print(f"Error on {filename}: {str(e)}")
            logging.error(f"Upload failed for {filename}: {str(e)}")
            
    print("Vesper System: Night batch completed successfully. Ready for morning review.")
    logging.info("Batch cycle finished.")

if __name__ == "__main__":
    print("--- Vesper AI Batch Processor ---")
    
    QUEUE_FOLDER = "night_batch_queue"
    DONE_FOLDER = "uploaded_morning"
    
    # Creating a test file automatically so the script has something to process when they test it
    os.makedirs(QUEUE_FOLDER, exist_ok=True)
    with open(os.path.join(QUEUE_FOLDER, "batch_test_01.mp4"), "w") as f:
        f.write("mock data")
        
    process_night_batch(QUEUE_FOLDER, DONE_FOLDER)
