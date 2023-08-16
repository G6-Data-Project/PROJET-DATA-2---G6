# IA1 Project - Exploiting Football API for Talent Identification

## Team
- Abraham RAMAROSANDY (STD 21017)
- Fabien MALALA-ZO Raharison (STD 21101)
- Vohizy ANDRIATSIMIADY Ramiandrisoa (STD 21005)
- Mirado RAHARINAIVOSOA Radintsoa (STD 21081)

## Context
As part of the IA1 project, our team focuses on harnessing the football API to refine the search for future talents in the world of football. Our goal is to simplify the player recruitment process by identifying emerging talents. The targeted API is as follows: [Link to Football API](https://apifootball.com/documentation/?gclid=CjwKCAjw8symBhAqEiwAaTA__FHopu1tvtKPyd9Kq2CkYNy4z1voKLIXDjwRvuOmvwmhqVebHnzE-RoC6ngQAvD_BwE)

## Technologies
We have agreed to use the following tools and languages:
- Scripting Language: Python
- Data Visualization: Tableau
- Storage: Amazon Web Services' S3 Service

## Tasks
Task distribution was organized within our GitHub organization, using the Project tool. Here's our team composition:
- Abraham: Full-Stack 
- Fabien: Product Owner
- Vohizy: Operations (OPS)
- Mirado: Backend

## Process

### Data Extraction from the API
We've created code to extract necessary information from the football API and convert it into .csv format. We obtained information by querying leagues, teams, and players, and then stored this data in a .csv file.

### Data Transformation
We've applied filters to identify general characteristics sought in professional players. Subsequently, we've extracted top players for each specific position and calculated a score based on their statistics. This allowed us to establish a ranking of the best players per position.

### Orchestration via Apache Airflow
We've designed a DAG (Directed Acyclic Graph) to automate data extraction and transformation every 3 months. The DAG configures the execution of necessary tasks, from importing dependencies to connecting with Amazon S3.

## Link to GitHub Project
For a detailed view of our project and task distribution, please refer to the following link: [GitHub Project - Group 6](https://github.com/orgs/G6-Data-Project/projects/1/views/1)

*This document was created and validated by the IA1 Project Team - Group 6.*
