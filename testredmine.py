from redminelib import Redmine

api_key = "70f5b1684a6f7e90a3725d721dc51fb754c2dbf6"
redmine = Redmine('https://tasks.etecs.ru/', key=api_key)

# number_of_task = 29352
user = 'Аточкин Александр'
task = redmine.issue.filter(limit = 2,assigned_to_id = 'me')
for i in task:
    print(list(i))


    print('-------------------')
    # if i.id == number_of_task:
    #     break

