# Ukrainian Cafe

[View the live project here.](https://ukrainian-cafe-f4f96fd63fc0.herokuapp.com/)

The Ukrainian Cafe website is made for a cafe. This website shows today's specials, menu, contact information, and opening hours. Potential customers can register and book a table online using a form on the "Booking" page of the website. 
Users are able to view pages like the home page, menu and the contact page, also to create an account, sign in, make a booking and view bookings, which unregistered users don't have access to. Through the booking and the view booking navbar link users can access their bookings, edit and delete them. Site user administrators have access to all bookings and all create, edit and delete functionalities.

The website is designed to be responsible on a range of devices.

![Am I responsive screenshot]()


## Table of contents
 1. [ UX ](#ux)
 2. [Agile Development](#agile)
 3. [ Features ](#features)  
 4. [ Future Features ](#future)  
 5. [ Technology used ](#tech) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#bugs)  
 8. [ Deployment](#deployment)
 9. [ Credits](#credits)
 10. [ Content](#content)  
 11. [ Acknowledgements](#acknowledgements)

## User Experience (UX)

## Agile Development

## Features

## Future features

## Technology used

## Testing

## Deployment



---

Happy coding!

**Media**
Photo: [name of the photographer], [name of the organization/company that donated the image or the photo] / ukraine.ua/imagebank
Traditional Ukrainian borscht - photo: Yevhen Kudriavtsev

Fried dumplings with onion and bacon top view - photo: nioloxs - Depositphotos (три вареника)

Spotykach. Liqueur made of berries or fruits - photo:  - klopotenko.com (ликер на темном фоне)

Borscht with prunes and porcini mushrooms - photo:  - klopotenko.com (борщ в правом углу на сером фоне)

Ukrainian varenyky with potatoes and onion - photo: Yevhen Kudriavtsev (варениеи картошкойб цибулей и салом)

Lard with spices and herbs on a old wooden table - photo: igorr1 - Depositphotos (salo vertical)

Borscht is a beetroot soup that has over 70 recipes. Usually served with garlic fritters called pampushky. It is included on the list of the Ukrainian intangible heritage - photo: Oksana Sybydlo Food Photographer / їzhakultura - Ukrainian Institute (борщ в треугольной тарелке)

Delicious Chicken Kyiv and mashed potato served on plate on wooden table - photo: AntonMatyukha - Depositphotos (chicken Kyiv)

Spotykach. Liqueur made of berries or fruits - photo:  - klopotenko.com

Traditional kvass beer mug with rye bread on wooden table - photo: etorres69 - Depositphotos

Field of the green wheat near Kitsman, Chernivtsi region - photo: Max Kozmenko


**Bugs**
1. When upload image in form "Add Specials", image won't show up. 

Solution: I had to retrieve request.FILES in the view:
```
form = SpecialsForm(request.POST, request.FILES)
```
and add the following enctype to the form in html file:
```
<form method="POST" name="form" enctype="multipart/form-data"></form>
```
2. Menu links don't work on the Booking page.

3. Booking form not rendering in html. I found solution on [stackoverflow.com](https://stackoverflow.com/questions/75495403/django-returns-templatedoesnotexist-when-using-crispy-forms) It says: "inside settings.py in the main app add INSTALLED_APPS = [ ... 'crispy_forms', 'crispy_bootstrap4', ... ] and CRISPY_TEMPLATE_PACK = 'bootstrap4'." It helped me to solve the problem. The booking is now displayed on add_booking.html.
