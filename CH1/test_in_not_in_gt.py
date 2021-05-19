import random

def test_number_in():
    assert 83 in [49, 3, 83, 39, 45, 12, 83, 6, 51, 52, 51, 13, 4, 78, 57, 47, 51, 18, 29, 2]

def test_random_number_in():
    random_list = []
    for number in range(0, 20):
        random_number = random.randint(1, 100)
        random_list.append(random_number)
    assert random_list[3] in random_list


def test_string_not_in():
    assert 'mercedes' not in '''
    Eveniet nobis aut voluptates ratione quos quod nostrum quia eum ab. 
    Eum repellendus eum numquam minima quibusdam explicabo veniam animi iusto velit velit. 
    Deleniti porro quia mollitia et temporibus consequatur praesentium adipisci dolorem voluptatem id et. 
    Iure facere fuga ut et et esse quae. 
    Quis magni esse molestiae cupiditate necessitatibus eligendi omnis at vel doloribus quo corrupti. 
    Voluptas adipisci sed debitis amet et qui. 
    Et fugiat qui accusamus odit voluptatem modi laudantium iure id enim corrupti odio numquam sequi voluptatem.
    '''

def test_greater_than():
    assert 'b' > 'a'