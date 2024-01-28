# exercicio

def city_country(city, country, population=''):
    """recebe o nome de cidade e pais"""
    if population:
        location = city + ' ' + country + ' ' + str(population)
    else:
        location = city + ' ' + country
    return location.lower()
