from bs4 import BeautifulSoup
html = """

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
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
    <li data-example="yes">This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>

"""

# making a variable called soup and equaling that to BeautifulSoup as shown above that we have imported that.
soup = BeautifulSoup(html, "html.parser")


#example syntax of how to scrape certain html attributes
# d = soup.select("[data-example]")
# d = soup.select("h3")
# d = soup.select("li")
# d = soup.find_all("div")

# finding a div
#d = soup.find(id="first")

# finding all classes with special
# d = soup.find_all(class_="special")

# This pretty much says give me everything with the data atrribute set to yes.
# d = soup.find_all(attrs={"data-example": "yes"})

# ############################################
# ############################################


#example syntax of how to scrape css selectors

# adding [0] will give you back the actual object
# d = soup.select("#first")[0]

# you can select a class, a div or an attribute

d = soup.select(".special")

print(d)
