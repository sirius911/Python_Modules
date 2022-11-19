green = '\033[92m'
reset = '\033[0m'
red = '\033[91m'

def how_many_medals_by_country(data, country):
    """
        The function returns a dictionary of dictionaries giving the number and type of
        medal for each competition where the country delegation earned medals.
        args:
            • a pandas.DataFrame which contains the dataset
            • a country name. (string)
        return:
            Dictionary: The keys of the main
                dictionary are the Olympic games' years. In each year's dictionary, the key are 'G', 'S',
                'B' corresponding to the type of medals won.
    """
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball',\
         'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']

    
    # every years who the country have almost one medal
    years = data.query("Team == '"+country+"' and not Medal.isnull()")['Year'].unique()
    dict = {}
    for y in years:
        dict[y] = {"G":0, "S":0, "B":0}
    print(f"Found {green}{len(years)}{reset} Years")
    print(f"Counting the Medal of team sports")
    country_and_teams_sports = data.query("Team == '"+country+"' and not Medal.isnull() and Sport in "+str(team_sports))
    country_group = country_and_teams_sports.groupby(['Year', 'Event', 'Medal'])

    for group_key, group_value in country_group:
        year = group_key[0]
        event = group_key[1]
        medal = group_key[2][0]
        print(f"{year} -> {event} Medal = {medal}")
        gsv_dic = dict[year]
        gsv_dic[medal] += 1
        dict[year] = gsv_dic
        # print(group_value)
    print(f"-------------------")

    country_without_teams_sports = data.query("Team == '"+country+"' and not Medal.isnull() and Sport not in "+str(team_sports))
    country_group2 = country_without_teams_sports.groupby(['Year'])
    for year, group_value in country_group2:
        print(f"{green}{year}{reset}")
        medals = group_value['Medal']
        events = group_value['Event']
        for medal, event in zip(medals, events):
            gsv_dic = dict[year]
            gsv_dic[medal[0]] += 1
            dict[year] = gsv_dic
            print(f"{event} -> {red}{medal[0]}{reset}{medal[1:]}")      
    return dict