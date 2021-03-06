<p align="center">
  <a href="" rel="noopener">
 <img width=541px height=151px src="https://raw.githubusercontent.com/iMiebaka/Companyz-Flask/935ec8ece27efe2b422a1d89782a7a051825684c/cover_image.svg" alt="Project logo"></a>
</p>

<h3 align="center">Companyz</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://https://github.com/iMiebaka/Companyz-Flask/pulls)

</div>


<p align="center"> My Journey to MongoDB Part 1.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

I finally had to swallow my pride and give the Big Data storage Genie 🧞 a try, and I'll say it was worth every keystroke. <br/>
I built this project to receive names of Companies and years of existence (Using Python and MongoDB)
## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for options to deploy the project on a live system.

### Prerequisites

- Python3  or greater
- MongoDB

### Installing

After cloning the repository, run the following command

```
cd mongodb_flask
pip3 install -r requirements.txt
python3 run.py
```

## 🎈 Usage <a name="usage"></a>
This is a simple crud app.
### URL Endpoint
- /api/v1/
- /api/v1/add
```
{
  "name": "xyz",
  "age": 25
}
```
- /api/v1/delete?item=<id>
- /api/v1/update?item=<id>



## 🚀 Deployment <a name = "deployment"></a>
- [Heroku](https://heroku.com) 
- [Light Sail](https://lightsail.aws.amazon.com/ls/webapp/home/instances/) 
- [PythonAnywhere](https://www.pythonanywhere.com/)


## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Flask](https://expressjs.com/) - Server Framework
- [Python](https://python.org/en/) - Server Environment


## ✍️ Authors <a name = "authors"></a>

- [@imiebaka](https://github.com/imiebaka) - Idea & Initial work (No need to thank me :sunglasses:)


## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- [Tutorial Point](https://www.tutorialspoint.com/python_data_access/python_mongodb_delete_document.htm)
- [Educba](https://www.educba.com/mongodb-pagination/)
- [pymongo](https://pypi.org/project/pymongo/) - Documentation for mongo DB wrapper