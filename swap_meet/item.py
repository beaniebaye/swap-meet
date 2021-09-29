class Item:
  def __init__(self, condition = 0.0, category = ""):
    
    # if not category:
    #     category = ""
    # elif not condition:
    #     condition = 0.0

    self.category = category
    self.condition = condition

  def __str__(self):
    return "Hello World!"

  def condition_description(self):
      if self.condition == 5:
          return "Fantastic"
      elif 4 < self.condition < 5:
          return "Great"
      elif 3 < self.condition <= 4:
          return "Good"
      elif 2 < self.condition <= 3:
          return "Meh"
      elif 1 < self.condition <= 2:
          return "Poor"
      elif 0 < self.condition <= 1:
          return "Bad"
      else:
          return "Not even if you paid me."



