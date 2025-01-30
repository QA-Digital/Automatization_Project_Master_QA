import random
from datetime import datetime, timedelta

# List of destinations from the extracted data
destinations = [
    63484, 63483, 63487, 63488, 63865, 63862, 63863, 63866, 63864, 64419,
    64420, 64423, 64425, 63249, 63250, 63251, 63289, 63326, 63529, 64246,
    64242, 64245, 64240, 64248, 64243, 64244, 64241, 64247, 63215, 63287,
    63296, 63410, 63426, 64204, 64205, 74847, 64203, 63720, 63719, 63726,
    63725, 63727, 63889, 63891, 63888, 63890, 63542, 63582, 63581, 63580,
    63976, 63975, 63982, 63208, 63348, 63220, 63281, 63311, 63314, 63316,
    63319, 63324, 63333, 63341, 63362, 63390, 63402, 63408, 63409, 63442,
    63471, 64087, 64094, 64089, 64090, 64091, 64086, 64092, 63213, 211764,
    63241, 63242, 213028, 63243, 63245, 74459, 74460, 63284, 74464, 63350,
    63354, 74465, 63765, 64126, 64127, 63252, 63447, 211801, 211814, 63260,
    63448, 64076, 64447, 64075, 63489, 63212, 63539, 63229, 63255, 64428,
    64427, 63265, 63271, 63298, 63330, 63329, 63339, 63356, 63436, 63376,
    63391, 63406, 219502, 63425, 63429, 63444, 63537, 63453, 63454, 63456,
    63457, 63459, 63881, 63880, 218467, 64188, 64186, 64189, 64191, 64190,
    64185, 64187, 63885, 63886, 63892, 63887, 63540, 64161, 64167, 64171,
    64166, 64169, 64172, 64174, 64159, 64168, 64162, 64170, 64164, 64176,
    64160, 64173, 64175, 64163, 64165, 63707, 63708, 63710, 63738, 63988,
    64102, 64099, 63992, 63994, 63995, 75728, 77251, 75729, 63993, 75730,
    77252, 75731, 77253, 63222, 63395, 63419, 63466, 63823, 63750, 63751,
    63752, 63753, 63754, 218634, 63755, 64443, 63756, 63757, 218503, 63758,
    63759, 63760, 63216, 63218, 63226, 63227, 63231, 64429, 63244, 74462,
    63263, 63267, 63272, 63299, 63312, 63334, 63313, 74461, 77806, 74463,
    63328, 64430, 63360, 63363, 63455, 64144, 64140, 64128, 64141, 64133, 64143
]

# List of available airports (example values)
airports = [
    2033, 3418, 3789, 483, 1837, 3437, 1862, 1825, 3850, 298, 874, 892, 983, 1091, 1293, 1956, 2397, 2563, 3352, 489
]


def generate_srl_urls(destinations, airports, num_urls):
    """
    Generate a specified number of SRL URLs with randomly selected parameters, including room occupancies.

    :param destinations: List of available destination codes.
    :param airports: List of available airport codes.
    :param num_urls: Number of URLs to generate.
    :return: List of generated URLs.
    """
    base_url = "/vysledky-vyhledavani/"
    static_airports = ["4312", "4305", "2682", "4308", "4392", "430"]  # Fixed static airport choices
    urls = []

    for _ in range(num_urls):
        # Select 13 random destinations
        selected_destinations = random.sample(destinations, 13)

        # Select 3-5 random airports from the provided list
        selected_airports = random.sample(airports, random.randint(3, 5))

        # Select 2 random static airports and add them to the selected airports
        selected_static_airports = random.sample(static_airports, 2)
        selected_airports.extend(selected_static_airports)

        # Get the current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Select a random departure date between 1 to 8 months from now
        start_date = datetime.now() + timedelta(days=random.randint(30, 240))
        start_date_str = start_date.strftime('%Y-%m-%d')

        # Select a return date at least 3 weeks and at most 2 months after the start date
        end_date = start_date + timedelta(days=random.randint(21, 60))
        end_date_str = end_date.strftime('%Y-%m-%d')

        # Decide number of rooms (1 or 2)
        num_rooms = random.randint(1, 2)

        # Generate occupancy details
        room_params = []
        for i in range(1, num_rooms + 1):
            adults = random.randint(1, 4)  # Max 4 adults per room
            total_kids = random.randint(0, 6 - adults)  # Remaining capacity for kids

            infants = random.randint(0, min(total_kids, 2))  # Max 2 infants (IC)
            kids = total_kids - infants  # Remaining are normal kids

            # Generate age groups for kids (3-14 years old)
            kids_ages = [random.randint(3, 14) for _ in range(kids)]

            # Construct room parameters
            room_param = f"ac{i}={adults}"
            if infants > 0:
                room_param += f"&ic{i}={infants}"
            if kids > 0:
                room_param += f"&ka{i}=" + "|".join(map(str, kids_ages))
                room_param += f"&kc{i}={kids}"

            room_params.append(room_param)

        # Construct the URL
        url = (f"{base_url}?d=" + "|".join(map(str, selected_destinations)) +
               f"&dd={start_date_str}&nn=7|8|9|10|11|12|13|14&rd={end_date_str}" +
               f"&to=" + "|".join(map(str, selected_airports)) + "&tt=1" +
               "&" + "&".join(room_params))  # Append room details

        urls.append(url)

    return urls



urls = generate_srl_urls(destinations,airports, 5)
for url in urls:
    print(url)
