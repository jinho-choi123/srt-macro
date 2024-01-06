from pick import pick


def get_input():
    accept = False

    while not accept:
        departures = ['수서', '대전']
        arrivals = ['수서', '대전']

        departure, _ = pick(departures, 'pick station to departure')
        arrival, _ = pick(arrivals, 'pick station to arrive')

        reserve_date = input('Write the date you want to leave. \nex) 20240101\n')

        reserve_time = input(
            'Write the time(24hour format) you want to leave. You should only write even number. \nex) 00, 02, 04, ..., 20, 22\n')

        max_find = input('How many trains you want to search? (MAX 11) ex. 1, 2, ..., 10, 11\n')

        accepts = ["Yes", "No"]
        _, idx = pick(accepts, f'\nYou are trying to reserve train\n@{departure}=>{arrival}\n@{reserve_date} {reserve_time}\n@maxfind={max_find}\n')
        if idx == 0:
            accept = True

    return departure, arrival, reserve_date, reserve_time, max_find
