import graphene
from graphene_django import DjangoObjectType
from .models import Task

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ("id", "title", "description")

class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()

class CreateTask(graphene.Mutation):
    task = graphene.Field(TaskType)

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String()
    ok = graphene.Boolean() 
    task = graphene.Field(TaskType)
    
    def mutate(self, info, id, title, description=None):
        task = Task(id = id, title=title, description=description)
        task.save()
        return CreateTask(task=task)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
