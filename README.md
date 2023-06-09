# Description:

This project is using Selenium WebDriver with Python, using Pytest to automate the login page at Hudl.com. 

It will have multiple scripts, of both positive and negative testing to show my thought processes while navigating around the page. It will not be exhaustive, so nothing in terms of signing up, resetting passwords, or changing usernames and emails will be represented.

Since this project is specific to the login page and its functionality, I will set the baseURL as hudl.com/login.

Just for the sake of this project, I am assuming there are no bugs on the production login page for hudl.com. This means that the results I am given per the browser actions executed are the expected results. 

Since I was asked to use Selenium for this project, which requires downloading drivers to control the browsers, this project will only control the Google Chrome browser as proof. 

## The Ask:
- Setup an automation environment on your local machine using Selenium

- Automate any cases that you would think are good to test the functionality of validating logging into hudl.com.

- Push your tests to a GitHub repository (a public repo is fine) and share the link (please do not include any passwords in a public repo).

- We are expecting you to automate scenarios that you deem critical to validate the functionality of the hudl.com login page. 

- This project is an opportunity to showcase your organization structure, approach to automation, and ability to effectively write new automated test cases.
 
- We will be looking for well-established best practices and patterns. Lastly, we will run your automation suite against the site, so please write it in a way that allows us to do so.
 
- This isn't a timed test, however, we estimate this exercise to take you around 2 hours to complete. To allow us to continue to move through this process quickly, we ask that you return this project to us in 4 days. If you need more time for whatever reason, we ask that you please let us know, so we can properly set expectations with our project reviewers.

### Tips:
- If you're unfamiliar with Selenium the best place to start is with the below readings:
    - https://www.seleniumhq.org/projects/webdriver/
    - https://gist.github.com/huangzhichong/3284966 

## My Thoughts:

- I chose Python with Pytest for the project to submit due to its simple syntax and it not giving me as much trouble as JavaScript with mocha. There are a lot less lines needed to get the same job done using Python, so it seems cleaner as well.

- Selenium admits that waits are not their cup of tea, so instead of writing out a method to handle a global way of waiting, I simply imported `time` and call implicit waits accordingly. Since hudl.com is quick to navigate, I made a standard in my tests to wait 5 seconds for page loads and 2 seconds for element changes.

- If I was building a legit project to handle scalability, I would architech the repo with a page object model (POM) structure in mind. This approach would help reduce maintenance and allow for faster script writing in the future, if we were to build this out as a full project. A POM allows contributors to focus on writing new coverages without duplicating code whenever possible. Instead, contributors would be able to import and call selectors and methods into scripts, while also only having to update changes to these items in one place instead of multiple areas of the repo.

- I would also look into using a reporter so when a suite is ran, there would be a concise report of the results. In this case, the console does well enough in showing which tests passed and which ones failed accordingly.

- I didn't put much time into debugging or handling browser behavior if a test would fail, so if a test fails in this project, that browser session will remain open. control+C will kill the processes.

- I had thought of writing a script for remembering the user at log in, but since that requires figuring out a way of copying session cookies and injecting them into a new session, I decided against it for this example project.

- I only added comments to the first test as the rest of the file is pretty standard. I just wanted to show some insights on my workflow ideas.

## Scenarios:

### Positive:
- Valid user is able to log into hudl.com
- Clicking the Hudl logo link will navigate to hudl.com
- Clicking the left arrow link will navigate to hudl.com
- Clicking the Need help link from the login page will navigate to /login/help#
- Clicking the Need help link from the invalid log in message will navigate to /login/help
- Clicking the Log In with an Organization button will navigate to /login/organization
- Clicking the Sign up link will navigate to hudl.com/register/signup

### Negative:
- Invalid email will display message

## Run Project:

### Prerequisites:
- The environment will need Chrome browser version 102 installed
- Clone the project ([Instructions]([Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)))
- Python 3.11.3 will need to be installed and added to the machine's path ([Instructions](https://www.makeuseof.com/python-windows-path/))
- In a terminal, cd to the root of the project
    - Run the command: `pip install -r requirements.txt` (this will install all the dependencies required to run the project)

### Execute Specs:
- In a terminal, cd to the root of the project
- Run the command: `pytest login_page.py`
- If a test fails, please wait until the execution is finished and then press `control+C` to kill any remaining processes
- If you want to run a specific test instead of the whole file: `pytest login_page.py -k '<test name>'`
    - For example: `pytest login_page.py -k 'test_successful_login_goes_to_the_home_page'`