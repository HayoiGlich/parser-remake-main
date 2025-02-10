from redminelib import Redmine

api_key = ""
redmine = Redmine('https://tasks.etecs.ru/', key=api_key)

# number_of_task = 29352
user = 'Аточкин Александр'
task = redmine.issue.filter(limit = 2,assigned_to_id = 'me')
for i in task:
    print(list(i))


    print('-------------------')
    # if i.id == number_of_task:
    #     break

