In this task I have explored GraphQL and how to use it.

I have defined Task model in models.py file of assessment_app.
Then, I have created schema.py file which have query and mutation for retrive and create new tasks respectively.
    - The Query type contains a resolver function for the tasks field. This resolver returns all the tasks from the database.
    - The mutation takes in the model fields as arguments within the inner-Argument class and added new tasks to the databases.

After running our application, navigate to localhost:8000/graphql for querying using GraphQL.
I have used below query and mutation for example.

query{
  tasks{
    id
    title
    description
  }
}

mutation {
  createTask(title: "Task 1", description: "Assessment using graphql") {
    ok
    task {
        id
        title
        description
    }
  }
} 
