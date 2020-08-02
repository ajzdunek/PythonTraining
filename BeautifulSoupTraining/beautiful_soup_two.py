from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# method one

# el = soup.select(".special")[0]
# print(el.get_text())

# also print(el) will work for retriveing a singular element - comes in handy 
# for bits and pieces of data.

# ############################################################################
# ############################################################################

# method two

# for el in soup.select(".special"):
#   print(el.get_text())

# Output - how ever many items with the class special

# ############################################################################
# ############################################################################

# method three

for el in soup.select(".special"):
  print(el.name)

# Output - two li's and meta

# ############################################################################
# ############################################################################

# method four

for el in soup.select(".special"):
  print(el.attrs)

# Output - meta li li {'charset': 'UTF-8', 'class': ['special']} {'class': ['special']} {'class': ['special']}