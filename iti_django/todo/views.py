from django.shortcuts import render, redirect

my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Transformers',
        'priority': 1,
        'description': "This is an action movie",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'The Ring',
        'priority': 4,
        'description': "This is a horror movie",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Jumanji',
        'priority': 2,
        'description': "This is an adventure movie",
    },
]

def _get_target_task(target_id):
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    index_of_task = my_task_list.index(final_list[0])
    return index_of_task

def update_task(request, **kwargs):
    task_id = kwargs.get('task_id')
    index_to_update = _get_target_task(task_id)
    my_task_list[index_to_update]['name'] = 'Updated {}'.format(my_task_list[index_to_update].get('name'))
    return redirect('todo:todo-list')


def delete_task(request, **kwargs):
    task_id = kwargs.get('task_id')
    index_to_delete = _get_target_task(task_id)
    if my_task_list:
        my_task_list.pop(index_to_delete)
    return redirect('todo:todo-list')

def todo_list(request):
    my_context = {'task_list': my_task_list}
    return render(request, 'others/list.html', context=my_context)


def show_details(request, **kwargs):

     task_id = kwargs.get('task_id')
     task_index = _get_target_task(task_id)
     my_task_dictionary = my_task_list[task_index]

     my_context = {
         'task_id': my_task_dictionary.get('id'),
         'task_name': my_task_dictionary.get('name'),
         'task_priority': my_task_dictionary.get('priority'),
         'task_description': my_task_dictionary.get('description')
     }

     return render(request, 'others/list_details.html', context=my_context)