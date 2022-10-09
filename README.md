# PackTravel

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7178601.svg)](https://doi.org/10.5281/zenodo.7178601)
![pylint Score](https://mperlet.github.io/pybadge/badges/7.svg)
[![contributors](https://img.shields.io/github/contributors/amisha-w/PackTravel)](https://github.com/amisha-w/PackTravel/graphs/contributors)
[![Total Lines](https://tokei.rs/b1/github/XAMPPRocky/tokei)](https://github.com/amisha-w/PackTravel)
[![Issues](https://img.shields.io/github/issues/amisha-w/PackTravel)](https://github.com/amisha-w/PackTravel/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/amisha-w/PackTravel)](https://github.com/amisha-w/PackTravel/pulls)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/w/amisha-w/PackTravel)](https://github.com/amisha-w/PackTravel/graphs/commit-activity)
[![Repo Size](https://img.shields.io/github/repo-size/amisha-w/PackTravel)](https://github.com/amisha-w/PackTravel)


**Goal:**

_Travelling alone?_ **Try PackTravel**


**Project Description:**

Most of the international students do not have a car to travel off-campus and rely mostly on the Wolfline. But what if someone wants to travel outside Wolfline's limit? Well... why not collaborate on PackTravel to travel off-campus by a cab, rental car, etc.


![we-should-travel](https://user-images.githubusercontent.com/111834635/194171695-02f5bda6-af44-4e9e-a1a5-4d734c7af5de.jpg)

**So, let's PackTravel 😎**


## Watch PackTravel in action 
https://user-images.githubusercontent.com/111834635/194171771-962a585e-5dc7-4ea3-af35-732ebd34e76c.mp4

**Built Using:**
</br>
<code><a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-ar21.svg"></a></code>
<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_css/w3_css-ar21.svg"></a></code>
<code><a href="https://getbootstrap.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-ar21.svg"></a></code>
<code><a href="https://www.javascript.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/javascript/javascript-ar21.svg"></a></code>
<code><a href="https://www.djangoproject.com/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194172149-ff6a56be-3025-4d2c-8cdb-b9a7e3f87259.png"></a></code>
<code><a href="https://www.mongodb.com/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194173280-628ecfc0-21ae-4870-8e22-711e6da83820.png"></a></code>
<code><a href="https://www.python.org/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194173533-37cd4997-55f3-4bb1-87bd-1a16a3af53aa.png"></a></code>




## Getting started:

  - ### Prerequisite:
      - Download [Python3.x](https://www.python.org/downloads/).
      - Download [Django](https://docs.djangoproject.com/en/4.1/topics/install/).

   ## Run Locally

Create a virtual environment:

```bash
  python3.x -m venv test_env
```

Activate the virtual environment:
Linux/MacOS:
```bash
  source test_env/bin/activate
```
Windows:
```bash
  ./test_env/Scripts/activate
```

Clone the project

```bash
  git clone https://github.com/amisha-w/PackTravel.git
```

Go to the project directory

```bash
  cd PackTravel
```

Install dependencies

```bash 
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py migrate
  python manage.py runserver
```



     - Site will be hosted at:
       `http://127.0.0.1:5000/`
       
## Tools
- [Preetier Code Formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [JS-HTML-CSS Formatter](https://marketplace.visualstudio.com/items?itemName=lonefy.vscode-JS-CSS-HTML-formatter)
- [PyLint](https://pylint.org/)

## Preview

- **Sign Up Page**
  - User Interface to signup to the app
 ![Sign Up](https://user-images.githubusercontent.com/111834635/194778553-99da6656-8eaf-4e6a-9a8d-a1d3ff1a40cf.jpeg)

- **Login Page**
  - User Interface to login to the PackTravel app. After successful login, user will be redirected to the Dashboard page
![Login Page](https://user-images.githubusercontent.com/111834635/194778542-2b1c810c-3a14-44a1-b7e6-2db6aa83ee3b.jpeg)


- **Home Page** 
![Home Page](https://user-images.githubusercontent.com/111834635/194778535-43e49377-76ab-4ad3-9579-39f41c483a76.jpeg)

- **Add New Ride** 
![Create new ride](https://user-images.githubusercontent.com/111834635/194778576-4f2a4f79-c56e-48ef-ba3b-7c56d529addc.jpeg)

- **View and Search List of PackTravel**
![Search Page](https://user-images.githubusercontent.com/111834635/194778702-efec2c3b-41d4-40fb-8acc-8e00c4d39d90.jpeg)



## Chat Channel

<code><a href="https://app.slack.com/client/T03UZM4975G/C03UT3QFHP0" target="_blank"><img height="50" width="100" src="https://user-images.githubusercontent.com/111834635/194175304-834d5663-b6bb-4e38-981d-98bc1bf028b8.png"></a></code>


### Phase 1:

- [x] Create database ER diagram
- [x] Create Mongo Database
- [x] Create HomePage
- [x] Create Login Page
- [x] Create Signup Page
- [x] Setup Django
- [ ] Add Unit testing
- [x] Add Error Handling mechanisms

### Future Enhancements:

- [ ] Integrating Components to create a complete workflow
- [ ] Embedding calendar and highligting important dates
- [ ] Send remainder mails for deadlines
- [ ] Upload and Maintain resume versions
- [ ] Display the location of the application on the map
- [ ] Create APIs for relevant functionalities
- [ ] Share your profile with others
- [ ] Reading mails from your inbox and automatically adding/updating the status of the application
- [ ] Enabling Desktop Notifications

## Contributions to the Project

## Contributors 👨‍🏭

<table>
  <tr>
    <td align="center"><a href="https://github.com/amisha-w"><img src="" width="100px;" alt=""/><br /><sub><b>Amisha Waghela</b></sub></a></td>
    <td align="center"><a href="https://github.com/Aoishi28"><img src="" width="100px;" alt=""/><br /><sub><b>Aoishi Das</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/ameyachavan26"><img src="" width="100px;" alt=""/><br /><sub><b>Ameya Chavan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/kunalshah03"><img src="" width="100px;" alt=""/><br /><sub><b>Kunal Shah</b></sub></a><br /></td>
    <td align="center"><a href=""><img src="" width="100px;" alt=""/><br /><sub><b>Swarnamalya M</b></sub></a><br /></td>
  </tr>
</table>


## Contact 
In case of any issues, please mail your queries to packtravel@gmail.com 
