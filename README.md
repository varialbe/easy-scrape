# EasyScrape - Roblox Inventory Decal Downloader

## Overview
EasyScrape is a tool designed for Roblox developers to easily scrape and download inventory decals. It streamlines the process of acquiring decals by automating the scraping and downloading, significantly reducing manual effort.

## Installation

### Installing selenium
```
pip install selenium
```

### Installing requests
```
pip install requests
```


### Prerequisites
- A modern web browser (Chrome, Firefox, Edge)
- Basic understanding of JavaScript and web development

### Steps
1. **Clone the Repository:** Start by cloning the repository to your local machine using Git.
   ```
   git clone https://github.com/varialbe/easy-scrape
   ```
2. **Navigate to the Project Directory:** After cloning, navigate to the project directory.
   ```
   cd EasyScrape
   ```

## Usage Instructions for EasyScrape

### Running the Script
1. **Open Your Browser:** Launch your preferred web browser.

2. **Navigate to the Desired User's Inventory:** Visit the Roblox website and navigate to the inventory section of the user whose decals you want to download.

3. **Copy the URL:** Once you're in the specific inventory section displaying the decals, copy the URL from the browser's address bar.

4. **Prepare the Script:** Open the EasyScrape script in a text editor. At the bottom of the script, you'll find a placeholder to insert the URL. Replace it with the URL you just copied.

    ```python
    # Example of the placeholder in the script
    inventory_url = 'PASTE_THE_COPIED_URL_HERE'
    ```

5. **Run the Script:** Execute the script in your Python environment. You can do this typically by running a command like `python EasyScrape.py` in your command line or terminal, assuming `EasyScrape.py` is the name of the script.

6. **Wait for Downloads to Complete:** The script will create a new folder named `images` in the same directory where the script is located. It will then begin downloading all the decals from the specified user's inventory into this folder. Ensure that the script runs until all images are downloaded.

### Important Notes:
- The script will only download decals visible on the page of the provided URL. Make sure you are on the correct page showing the decals you want to download.
- Ensure that your Python environment has the necessary permissions to create directories and save files.
- The download time will vary depending on the number of decals and your internet speed.
- Running the script multiple times for the same URL will result in repeated downloads unless the script is modified to check for existing files.

If you encounter any issues or errors during the process, make sure to check the script for any typos in the URL and verify that your Python environment is correctly set up with all necessary dependencies installed.
### Downloading Decals
Once the script is executed, it will automatically start scraping and downloading the decals. Files will be saved to your default download directory.

## Troubleshooting

### Issues Encountered
If you encounter any issues, such as the script not initiating or errors in the console:
- Ensure that you are on the correct Roblox inventory page.
- Check if there's a cookie consent banner or any pop-up on the page. If present, accept or close the banner.

## Important Notes
- **Legal Compliance:** Ensure you have the right to download and use the content. Unauthorized downloading may violate copyrights or other legal rights.
- **Pop-Up Blocker:** Disable any pop-up blockers as they may interfere with the downloading process.
- **Same-Origin Policy:** The script abides by the browser's same-origin policy. Downloading from different domains might require CORS to be enabled on the server.

## Contribution
Contributions to EasyScrape are welcome. Please follow the standard GitHub fork-and-pull request workflow.

## Support
For support, please open an issue in the GitHub repository. We aim to address issues promptly.
