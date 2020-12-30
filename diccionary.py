def run():
    my_diccionary = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(my_diccionary["llave1"])
    # print(my_diccionary["llave2"])
    # print(my_diccionary["llave3"])

    country_poblation = {
        "Argentina": 44_938_721,
        "Brasil": 210_147_125,
        "Colombia": 50_372_424,
    }
    # print(country_poblation["Argentina"])

    # .keys():
    # .values():
    # .items():

    for country, poblation in country_poblation.items():

        print(f"{country} tiene {poblation} habitantes.")


if __name__ == "__main__":
    run()
