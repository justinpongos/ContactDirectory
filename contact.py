class Contact:
  def __init__(self, fn, ln, ph, addr, city, zip):
    """ Initializes a contact object with the given first name, last name, phone number, address, city, and zip code.

    Args:
        self(object), fn(String), ln(String), ph(String), addr(String), city(String), zip(String): Objects of class Contact
    """
    self.first_name = fn
    self.last_name = ln
    self.phone = ph
    self.address = addr
    self.city = city
    self.zip = zip

  def __lt__(self, other):
    """ Passes in and compares two Contact objects. Sorts the contacts after comparing by last name, then first name if last name is equal.
    
    Args:
        self(Contact), other(Contact): Two Contacts that will be used to compare one anothers first and last name. 
    """
    if self.last_name == other.last_name:
      return self.first_name < other.first_name
    else:
      return self.last_name < other.last_name
  
  def __str__(self):
    """ Formats how the string of contact information will be displayed.

    Args:
        self(Contact): Takes in a contact object.

    Returns:
        String: Returns a string of the contact information.
    """
    return f"{self.first_name} {self.last_name}\n{self.phone}\n{self.address}\n{self.city} {self.zip}"

  def __repr__(self):
    """  Formats how the string of contact information will be stored in the txt file.

    Args:
        self(Contact): Takes in a contact object.

    Returns:
        String: Returns a string of the contact information formated to be like the txt file.
    """
    return f"{self.first_name},{self.last_name},{self.phone},{self.address},{self.city},{self.zip}"