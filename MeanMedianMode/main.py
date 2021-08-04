"""Mean, Median, and Mode without using libraries"""



def mean(num_list):
    """Accepts a integer list and returns the mean. """
    return sum(num_list)/len(num_list)



def median(num_list):
    """Accepts a list and rearranges in order to find the median"""

    num_list.sort()
    if len(num_list) % 2 == 0:
        median =  len(num_list) / 2
        return median,median+1,f"mean of the median is { (median+median+1)/2}"
    else:
        return num_list[round(len(num_list)/2) -1]


def mode(num_list):
    """Gets the mode of the given list."""
    num_list.sort()
    count_dic = {}
    for i in num_list:
        if i in count_dic:
            continue
        count_dic[i]= num_list.count(i)

    mode_list = []
    max_mode = max(count_dic.values())

    for num,freq in count_dic.items():
        if freq == max_mode:
            mode_list.append(num)
    return mode_list



def interface():
    user_choice = ''
    while user_choice not in ['mean','median','mode','q']:
        user_choice = input('What do you want? Mean, Median or Mode?  : ').strip().lower()
    if user_choice == 'q':
        return
    list_param = input("Input the numbers seperated by comma  : ")
    list_param = [int(i) for i in list_param.split(',')]
    answer = ''
    if user_choice == 'mean':
        answer = mean(list_param)
    elif user_choice == 'median':
        answer = median(list_param)
    elif user_choice == 'mode':
        answer = mode(list_param)
    print(answer)

    if input('Do you want to start again? "n" to Quit  ').lower() == 'n':
        return

    interface()


interface()