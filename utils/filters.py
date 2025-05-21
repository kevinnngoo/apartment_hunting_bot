def is_listing_valid(rent, beds, max_rent=1500, min_beds=2):
    """
    Check if the listing meets the specified criteria.

    Args:
        rent (str): The rent amount as a string.
        beds (str): The number of bedrooms as a string.
        max_rent (int): The maximum rent allowed.
        min_beds (int): The minimum number of bedrooms required.

    Returns:
        bool: True if the listing is valid, False otherwise.
    """
    try:
        # Extract numeric value from rent string
        # Assuming rent is in format "$1,200 - $1,500"
        rent_value = int(rent.replace("$", "").replace(",", "").split(" - ")[0])
       
        #Handling "Studio" or "1-2 Beds" cases
        if "Studio" in beds:
            beds_value = 0
        else:
            beds_value = int(beds.split(" ")[0])
    except ValueError:
        return False

    return rent_value <= max_rent and beds_value >= min_beds