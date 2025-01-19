# importing all the necessary libraries
import os
import time
import subprocess
import shutil

# Folder that will store instantly captured images
captureFolder = "C:\\Users\\user\\Pictures\\camera"
# Given URL to upload
folderUpload = ("https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_"
                "202501/upload.php")
# Folder to upload images to in order to reduce duplications
storeFolder = "C:\\Users\\user\\Pictures\\storefolder"

# Ensure the upload folder exists
os.makedirs(storeFolder, exist_ok=True)

def toUploadImage(picPath):
    # Using the curlCommand to upload
    try:
        # Prepare the curl command
        command = [
            "curl",
            "-X", "POST",
            "-F", f'imageFile=@{picPath}',
            folderUpload
        ]
        # curl command execution
        result = subprocess.run(command, capture_output=True, text=True)
        # monitor if the results have been added
        if result.returncode == 0 and "successfully uploaded" in result.stdout.lower():
            return True
        else:
            print(f"OOps! Failed to upload {picPath}: {result.stderr or result.stdout}")
            return False
    except Exception as e:
        print(f"Uploading failed with {picPath}: {e}")
        return False

def toMonitorCaptures():
    """Monitor the captured images and redirect them to the upload folder."""
    uploadedPic = set()

    while True:
        for fName in os.listdir(captureFolder):
            fPath = os.path.join(captureFolder, fName)

            if os.path.isfile(fPath) and fName not in uploadedPic:
                # Upload the image
                if toUploadImage(fPath):
                    print(f'Ta-da! Image uploaded: {fName}')
                    uploadedPic.add(fName)
                    # Move the file to the storage folder to reduce redundancy
                    shutil.move(fPath, os.path.join(storeFolder, fName))
                else:
                    print(f'OOPs! Pic failed to upload: {fName}')

        # Wait for 30 seconds
        time.sleep(30)

if __name__ == '__main__':
    try:
        print("Checking for new images...")
        toMonitorCaptures()
    except KeyboardInterrupt:
        print("\nChecking ending...")