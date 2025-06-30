# BX React 1: Building our scans table
## Prerequisites:
- basic programming skills 
  - variables, conditions, functions, basic operators, arrays/lists/objects/dictionaries/...
- understand code
- syntax knowledge
    - code organisation, naming conventions, ...
- IDE - VSCode or Webstorm
  - I am able to help you with Webstorm

## About the app:
We are going to build an app that gets the data from the backend API on Brainomix servers and display the data in some reasonable way. The app should also allow visitors to edit, add or remove the data.

### What we are starting with:
- A functional backend - already developed, we are not going to touch that
- A React project stub
  - base code setup, file structure and displaying raw texts

### What we will our React app look like after we are done:
- it displays all the scan records with all columns necessary
- it allows us to edit the database from the frontend (using APIs)
- it will look "not ugly."

### Recommendations:
- download [WebStorm IDE by JetBrains](https://www.jetbrains.com/webstorm/download/?section=windows)
- create a user account on [JetBrains user section](https://account.jetbrains.com/signup)
  - if you are serious about learning and using React, I suggest paying the commercial license, otherwise use free non-commercial
- set up NodeJS
  - if you are a developer, you might already have this under your ubuntu WSL
  - test it using `node -v` - if it shows the version, then great
  - if missing, install it using `nvm` (restart terminal afterwards)
  - once Node is successfully installed, make sure you're using version at least 20.0
    - if not, use `nvm` for installing another version (literally 5-second job)
- open settings (`Ctrl+Alt+S`)
  - I have already included `.idea` folder into the codebase and then marked it in `.gitignore`. That means that some of the following settings are automatically preselected for you.
  - locate `Node interpreter` and use the correct instance
  - ![Alt text](https://i.imgur.com/pnIS0GR.png)
  - locate `prettier` and enable it - automatic config, run on save
  - ![Alt text](https://i.imgur.com/tlU44kw.png)
  - similar thing with `eslint`
  - ![Alt text](https://i.imgur.com/lN8oqQu.png)
- use AI, if you continue using React and WebStorm
  - there is no shame of making your life better by utilising the in-build AI for dull tasks
  - it is always free, just hit that button on the right-panel - choose the AI model and hit `codebase`, so it can actually read the necessary files for the answer
  - ![Alt text](https://i.imgur.com/mbDXKQz.png)