# BX React Workshop: Building a Scan Management Application

## Overview
This project implements a React-based frontend application that interfaces with a Brainomix backend API. The application provides functionality for displaying and managing scan records through a user-friendly interface.

## Project Objectives
- Create a responsive data table displaying scan records
- Implement CRUD operations (Create, Read, Update, Delete) via API integration
- Develop a professional and user-friendly interface

## Prerequisites

### Technical Skills
- Fundamental programming concepts:
  - Variables, control structures, and functions
  - Data structures (arrays, objects)
  - Basic algorithm understanding
- Code organization and syntax knowledge
- Familiarity with development best practices

### Development Environment

#### Required Software
1. **IDE**: WebStorm or VSCode
   - [Download WebStorm](https://www.jetbrains.com/webstorm/download/?section=windows)
   - [Create JetBrains Account](https://account.jetbrains.com/signup)
     - you can use some temporary email like [temp-mail](https://temp-mail.org/) or your own, if you are serious about learning ReactJS
   > Note: WebStorm support and configuration guidance is provided in this workshop

2. **Node.js**
   - Minimum version: 22.0
   - Verify installation: `node -v`
   - Recommended installation method: `nvm` (Node Version Manager)
     - If you need to change the node version, do this:
     - `nvm install --lts`
     - `nvm use --lts`

## Development Setup

### WebStorm Configuration
1. Open Settings (`Ctrl+Alt+S`)
2. Configure the following:

#### Node Interpreter
- Locate and select the appropriate Node.js instance
- Ensure version compatibility (20.0+)
- (see pictures at the end of this README) 

#### Code Formatting
1. **Prettier Configuration**
   - Enable automatic configuration
   - Set to run on save
   - (see pictures at the end of this README)

2. **ESLint Setup**
   - Enable automatic ESLint configuration
   - Configure for real-time linting
   - - (see pictures at the end of this README)

### Project Structure
- Backend API (pre-configured)
- React project template
  - Basic setup and file structure
  - Initial rendering implementation

## Development Tools

### AI Assistant Integration
WebStorm provides built-in AI assistance for development tasks:
- Access via the right panel
- Select preferred AI model
- Enable codebase context for relevant suggestions
- (see pictures at the end of this README)

# How to install your environment:
Javascript is fairly easy. Just locate the react folder and install.
- `cd bx-react-1-fe`
- `npm install`

Python might be a bit more problematic - you need python 3.x and python 3.x-venv packages installed in your WSL. The latest version is 3.12, but if you have an older one, that will also work (tested in both 12 and 10).
- `sudo apt-get update`
- `sudo apt install python3`
- `sudo apt install python3-venv`

Now that it's installed, we still need to install project's dependencies.
- `cd bx-react-1-be`
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

# How to start your environment:
If everything is installed correctly, then you need 2 separate terminal windows - one for the javascript and the other one for our server.
### Server:

- `cd bx-react-1-be`
- `source venv/bin/activate` (if you haven't activated your virtualenv)
- `python ./manage.py runserver` (and leave this running)

### Frontend:
- `cd bx-react-1-fe`
- `npm start` (and leave this running in the second terminal)

## Licensing Note
For WebStorm IDE:
- Commercial license recommended for professional development
- Free non-commercial license available for learning purposes


# WebStorm configuration and AI:
![Alt text](https://i.imgur.com/pnIS0GR.png)

![Alt text](https://i.imgur.com/tlU44kw.png)

![Alt text](https://i.imgur.com/lN8oqQu.png)

![Alt text](https://i.imgur.com/mbDXKQz.png)