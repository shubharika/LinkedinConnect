# Automation

A bot to automate redundant manual tasks

Following steps need to be performed to replicate the environment I am using on Miniconda:

Run the following on CLI (with miniconda installed) in the repo folder: conda env create -f environment.yml
Activate the created environment using: conda activate /Path/To/Your/env


## Initialize Driver Function

The `initialize_driver()` function in this Python script is responsible for setting up and initializing the WebDriver required for web scraping with Selenium. Below is an explanation of the steps involved in setting up the WebDriver and how to use this function effectively.

## Steps to Set Up the WebDriver:

1. **Install ChromeDriver:**
   ChromeDriver is a separate executable that WebDriver uses to control Chrome. You can download ChromeDriver from the [Chrome for Testing website](https://googlechromelabs.github.io/chrome-for-testing/#beta). Make sure to download the version of ChromeDriver that matches the version of Chrome you have on your system. After downloading, place the ChromeDriver executable in a directory accessible to your Python script.

2. **.env file creation :**
  Create an environment file named .env similar to .env-example.

3. **Environment Variables**
  - `CHROME_LOCATION`: Path to your Chrome executable.
  - `DRIVER_LOCATION`: Path to your ChromeDriver executable.
  - `USERNAME`: Your LinkedIn username or email address.
  - `PASSWORD`: Your LinkedIn password.
  - `MESSAGE`: Custom message you want to send in the add note.
  - `MAX_RETRIES`: Number of times to retry in case of an error before skipping to the next URL.
  - `RETRY_DELAY`: Delay in seconds between retries.

  **Text files:**
  - `COMPANY_FILE`: Location of the NEWLY created text file containing the names of companies to search for on <Social Media>.
  - `PROFILE_LINK`: Location of the NEWLY created text file to store the scraped <Social Media> profile links.

## File Descriptions

- `get_profiles.py`: Main Python script for scraping <Social Media> profiles.
- `connect.py`: Main Python script for sending the connection request with a custom message.

- **Run the Script:**
  After setting up Chrome Beta and ChromeDriver, and logging in to your Chrome profile, you can run the Python script using the following command:

```bash
python <filename>.py
```

Replace `<filename>` with the Python script you want to run. (i.e. connect or get_profiles)


### Customizing `get_profiles.py`

You can adjust the start(Line:120) and end(Line:121) index parameters in `get_profiles.py` to specify the range of profiles you want to scrape from each company's search results on <Social Media>.

<Social Media> displays 10 search results per page. Modify the start and end index within the range `[0:10]` to select the desired number of profiles from each company.
