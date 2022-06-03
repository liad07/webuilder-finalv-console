from downloads import download
import os
import requests

response = requests.get("https://liad07.github.io/checkey/license.txt")
data = response.text
data = data.split("\n")
inp = input("enter license\n")
count = 0
if inp==" " or inp=="":
    inp="nicetrybro"
for i in range(0, len(data)):
    data[i] = data[i].replace("\r", "")
    if inp == data[i]:
        count += 1
        break
if count == 1:
    print("good key")
    name = input("enter name\n")
    logo = input("enter link to logo\n")
    img1 = input("enter link to img 1\n")
    img2 = input("enter link to img 2\n")
    img3 = input("enter link to img 3\n")
    bgcolor = input("enter background color\n")
    topnavcolor = input("enter topnav color\n")
    currenttopnavcolor = input("enter current topnav color\n")
    hovertopnavcolor = input("enter hover top nav color\n")
    print("enter text about your site split this to 2 rows \n")
    about1 = input()
    about2 = input()
    os.mkdir(name)
    os.mkdir(name + "/images")
    download("https://raw.githubusercontent.com/liad07/cool-cars/main/main.js", out_path=f"{name}/main.js")
    download(logo, out_path=f"{name}/images/logo.png")
    download(img1, out_path=f"{name}/images/img1.png")
    download(img2, out_path=f"{name}/images/img2.png")
    download(img3, out_path=f"{name}/images/img3.png")
    # Home page
    f = open(f"{name}/Home.html", "a")
    f.write(f'<!DOCTYPE html> \n'
            f'<html>\n<head>\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">\n'
            f'    <meta charset="UTF-8">\n    <title>{name}</title>\n<link rel="stylesheet" href="Styles.css">\n<link rel="icon" href="images/logo.png">\n</head>\n'
            f'<body>\n<div class="background">\n<div class="center">\n<div class="topnav">\n<a class="active" href="Home.html">Home</a> \n<a href="Registration.html">Registration</a> \n<a href="CreateContentItem.html">CreateContentItem</a>\n <a href="SharedContent.html">SharedContent</a>\n <a href="gallery.html">gallery</a>\n <a href="About.html">About</a>\n </div>\n'
            f'<img class="topnav-right" id="img" src="images/logo.png" width="200px" height="200px" onclick="rotateImg()">\n</div>\n'
            f'<div class="center">\n<h1>{about1}</h1>\n<h2>{about2}</h2>\n'
            f'<table class="login">\n <tr> \n<td> \n<h3 class="center">login form</h3>\n </td> \n</tr>\n <tr>\n <td>\n<input type="text" placeholder="user">\n</td> \n</tr>\n <tr> \n<td>\n<input type="password" placeholder="password">\n</td> \n</tr> \n<tr> \n<td>\n<input type="submit" value="login">\n</td>\n </tr> \n<tr> \n<td>\n<a href="Registration.html">link 2 Registration</a>\n</td> \n</tr> \n</table>\n'
            f'<div class="center">\n<img src="images/img1.png" height="250" width="300">\n<img src="images/img2.png" height="250" width="300">\n<img src="images/img3.png" height="250" width="300">\n<script src="main.js"></script>\n'
            f'</div>\n</div>\n</div>\n</body>\n</html>')
    f.close()
    # Registration page
    y = open(f"{name}/Registration.html", "a")
    y.write(f'<!DOCTYPE html> \n'
            f'<html>\n<head>\n<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">\n'
            f'<meta charset="UTF-8">\n<title>{name}|Registration</title>\n<link rel="stylesheet" href="Styles.css">\n<link rel="icon" href="images/logo.png">\n</head>\n'
            f'<body>\n<div class="center">\n<div class="topnav">\n<a href="Home.html">Home</a> \n<a class="active" href="Registration.html">Registration</a> \n<a href="CreateContentItem.html">CreateContentItem</a>\n <a href="SharedContent.html">SharedContent</a>\n <a href="gallery.html">gallery</a>\n <a href="About.html">About</a>\n </div>\n'
            f'<h1>Registration Page</h1>\n<form>\n<input type="text" name="fname" size="8">\n<b>first name</b>\n<br>\n</br>\n<input type="text" name="user" size="8"><b>username</b><br></br>\n'
            f'<input type="email" id="email" placeholder="example@gmail.com"><b>email</b><br></br>\n<input type="password" id="password"><b>password</b><br></br>\n<input type="datetime-local" id="date"><b>born date</b><br></br>\n'
            f'<b>gender</b><br>\n <input type="radio" name="gender" value="male">male<br> \n<input type="radio" name="gender" value="female">female<br>\n'
            f'<br></br>\n <b>area</b>\n <br></br> \n<select name="area">\n <option value="north"> north \n<option value="west"> west \n<option value="center"> center \n<option value="outofIL">out of ISRAEL \n</select>\n<br> </br>'
            f'<div class="center">\n<input type="submit" onclick="is_valid()">\n<input type="reset">\n</div>\n</form>\n</div>\n<script src="main.js"></script>\n</body>\n</html>')
    y.close()
    # css page
    d = open(f"{name}/Styles.css", "a")
    d.write(
        '.topnav { overflow: hidden; background-color: ' + topnavcolor + '; } .topnav a { float: left; color: #000000; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; } .topnav a:hover { background-color: '+hovertopnavcolor+'; color: #000000; } .topnav a.active { background-color:'+currenttopnavcolor+'; color: white; } .topnav-right { float: right; weight: 10% !important; height: 5% !important; } .center { text-align: center; } .login{ height: 30%; text-align: right ; background-color: ' + topnavcolor + '; float: right; } body { background-color: ' + bgcolor + ';} * {box-sizing: border-box} body {font-family: Verdana, sans-serif; margin:0} .mySlides {display: none} img {vertical-align: middle;} /* Slideshow container */ .slideshow-container { max-width: 1000px; position: relative; margin: auto; } /* Next & previous buttons */ .prev, .next { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -22px; color: #111111; font-weight: bold; font-size: 18px; transition: 0.6s ease; border-radius: 0 3px 3px 0; user-select: none; } /* Position the "next button" to the right */ .next { right: 0; border-radius: 3px 0 0 3px; } /* On hover, add a black background color with a little bit see-through */ .prev:hover, .next:hover { background-color: rgb(26, 227, 173); } /* Caption text */ .text { color: #ffffff; font-size: 15px; padding: 8px 12px; position: absolute; bottom: 8px; width: 100%; text-align: center; } /* Number text (1/3 etc) */ .numbertext { color: #f2f2f2; font-size: 12px; padding: 8px 12px; position: absolute; top: 0; } /* The dots/bullets/indicators */ .dot { cursor: pointer; height: 15px; width: 15px; margin: 0 2px; background-color: #bbb; border-radius: 50%; display: inline-block; transition: background-color 0.6s ease; } .active, .dot:hover { background-color: #717171; } /* Fading animation */ .fade { -webkit-animation-name: fade; -webkit-animation-duration: 1.5s; animation-name: fade; animation-duration: 1.5s; } @-webkit-keyframes fade { from {opacity: .4} to {opacity: 1} } @keyframes fade { from {opacity: .4} to {opacity: 1} } /* On smaller screens, decrease text size */ @media only screen and (max-width: 300px) { .prev, .next,.text {font-size: 11px} } .galimg{ width: 1000px; height: 700px; } .login{ margin-top: 110px; margin-right:-200px ; }')
    d.close()
    # CreateContentItem page
    x = open(f"{name}/CreateContentItem.html", "a")
    x.write(
        f'<html>\n<head>\n<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">\n'
        f'<meta charset="UTF-8">\n<title>{name}|CreateContentItem</title>\n<link rel="stylesheet" href="Styles.css">\n<link rel="icon" href="images/logo.png">\n</head>\n'
        f'<body>\n<div class="center">\n<div class="topnav">\n<a href="Home.html">Home</a> \n<a href="Registration.html">Registration</a> \n<a class="active" href="CreateContentItem.html">CreateContentItem</a>\n <a href="SharedContent.html">SharedContent</a>\n <a href="gallery.html">gallery</a>\n <a href="About.html">About</a>\n </div>\n'
        f'<div class="center">\n<form>\n<h1><u>Content creation page</u></h1><br><br>\n<b>type of </b><br><input type="text"><br><br><br>\n<input type="radio" name="yad"><b> 1 </b><br>\n<input type="radio" name="yad"><b>2</b><br>\n<input type="radio" name="yad"><b> 3 </b><br>\n'
        f'<br><b>date</b>\n<br><input type="datetime-local">\n<br><br>\n<b>price</b>\n<br>\n<input type="number">\n<br>\n<b>photo of</b>\n<br>\n<input type="file" accept=".png,.jpg,.jpeg">\n'
        f'<br><br><br>\n<input type="submit"><input type="reset">\n </form>\n</div>\n</div>\n<script src="main.js"></script>\n</body>\n</html>')
    x.close()
    # sharedContent page
    t = open(f"{name}/SharedContent.html", "a")
    t.write('<!DOCTYPE html> \n'
            f'<html>\n<head>\n<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">\n'
            f'<meta charset="UTF-8">\n<title>{name}|SharedContent</title>\n<link rel="stylesheet" href="Styles.css">\n<link rel="icon" href="images/logo.png">\n</head>\n'
            f'<body>\n<div class="center">\n<div class="topnav">\n<a href="Home.html">Home</a> \n<a href="Registration.html">Registration</a> \n<a href="CreateContentItem.html">CreateContentItem</a>\n <a class="active" href="SharedContent.html">SharedContent</a>\n <a href="gallery.html">gallery</a>\n <a href="About.html">About</a>\n </div>\n'
            f'<h1 class="center">SharedContent page</h1>\n<table border=2 text align="center">\n<tr text align="center">\n<th>photo of</th>\n<th>name of</th>\n<th>date</th>\n<th>price</th>\n</tr>\n'
            f'<tr text align="center">\n<td><img src="images/img1.png" height="200" width="300"></td>\n<th><h1>first name</h1></th>\n<th><h1>first date</h1></th>\n<th><h1>first price</h1></th>\n</tr>\n'
            f'<tr text align="center">\n<td><img src="images/img2.png" height="200" width="300"></td>\n<th><h1>second name</h1></th>\n<th><h1>second date</h1></th>\n<th><h1>second price</h1></th>\n</tr>\n'
            f'<tr text align="center">\n<td><img src="images/img3.png" height="200" width="300"></td>\n<th><h1>third name</h1></th>\n<th><h1>third date</h1></th>\n<th><h1>third price</h1></th>\n</tr>\n'
            f'</table>\n<script src="main.js"></script>\n</body>\n</html>')
    t.close()
    # gallery page
    yb = open(f"{name}/gallery.html", "a")
    yb.write(f'<!DOCTYPE html> \n'
             f'<html>\n<head>\n'
             f'<meta charset="UTF-8">\n<title>{name}|gallery</title>\n<link rel="stylesheet" href="Styles.css">\n<link rel="icon" href="images/logo.png">\n</head>\n'
             f'<body  onload="currentSlide(1)" >\n<div class="center">\n<div class="topnav">\n<a href="Home.html">Home</a> \n<a href="Registration.html">Registration</a> \n<a href="CreateContentItem.html">CreateContentItem</a>\n <a href="SharedContent.html">SharedContent</a>\n <a class="active" href="gallery.html">gallery</a>\n <a href="About.html">About</a>\n </div>\n'
             f'<h1 class="center">our images</h1>\n<div class="slideshow-container">\n'
             f'<div class="mySlides fade">\n<div class="numbertext">1 / 3</div>\n<img class="galimg" src="images/img1.png" style="width:100%">\n</div>\n'
             f'<div class="mySlides fade">\n<div class="numbertext">2 / 3</div>\n<img class="galimg" src="images/img2.png" style="width:100%">\n</div>\n'
             f'<div class="mySlides fade">\n<div class="numbertext">3 / 3</div>\n<img class="galimg" src="images/img3.png" style="width:100%">\n</div>\n'
             f'<a class="prev" onclick="plusSlides(-1)">&#10094;</a>\n<a class="next" onclick="plusSlides(1)">&#10095;</a>\n</div>\n<br>\n'
             f'<div style="text-align:center">\n<span class="dot" onclick="currentSlide(1)"></span>\n<span class="dot" onclick="currentSlide(2)"></span>\n<span class="dot" onclick="currentSlide(3)"></span>\n</div>\n'
             f'<script src="main.js"></script>\n</body>\n</html>'
             f'')
    yb.close()
    # about page
    b = open(f"{name}/gallery.html", "a")
    b.write(f'<!DOCTYPE html> \n'
            f'<html>\n<head>\n'
            f'<meta charset="UTF-8">\n<title>{name}|gallery</title>\n<link rel="stylesheet" href="Styles.css">\n<link rel="icon" href="images/logo.png">\n</head>\n'
            f'<body>\n<div class="center">\n<div class="topnav">\n<a href="Home.html">Home</a> \n<a href="Registration.html">Registration</a> \n<a href="CreateContentItem.html">CreateContentItem</a>\n <a href="SharedContent.html">SharedContent</a>\n <a href="gallery.html">gallery</a>\n <a class="active" href="About.html">About</a>\n </div>\n'
            f'<div class="center">\n<h1>{about1}</h1>\n<h2>{about2}</h2>\n</div>\n<script src="main.js"></script>\n</body>\n</html>'

            )
    b.close()
else:
    print("Incorrect key")
    print(inp)