green = '\033[92m'
reset = '\033[0m'
red = '\033[91m'
def how_many_medals(data, name):
    """
        returns a dictionary of dictionaries giving the number and type of medals
        for each year during which the participant won medals. The keys of the main dictio-
        nary are the Olympic games years. In each year’s dictionary, the keys are ’G’, ’S’, ’B’
        corresponding to the type of medals won (gold, silver, bronze). The innermost values
        correspond to the number of medals of a given type won for a given year.

        args:
            • a pandas.DataFrame which contains the dataset,
            • a participant name.

        return:
            a dictionary of dictionaries
    """
    dict = {}
    years = data.query("Name == '"+name+"'")['Year'].unique()
    for y in years:
        dict[y] = {"G":0, "S":0, "B":0}
    filter_name = data.query("Name == '"+name+"' and not Medal.isnull()")
    group_by_year = filter_name.groupby(['Year'])
    for year, group_value in group_by_year:
        medals = group_value['Medal']
        events = group_value['Event']
        for medal, event in zip(medals, events):
            gsv_dic = dict[year]
            gsv_dic[medal[0]] += 1
            dict[year] = gsv_dic
            print(f"{green}{year}{reset} : {event} -> {red}{medal}{reset}")
   
    sorted_dict = {}
    for key in sorted(dict.keys()):
        sorted_dict[key] = dict[key]
    
    return sorted_dict