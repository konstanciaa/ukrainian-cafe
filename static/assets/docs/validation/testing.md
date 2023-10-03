Each user story was manually tested in line with intended functionality on both desktop & mobile. 

### Account Registration Tests
| Instruction | Result  |
|--|--|
| Click Login  | Redirected to Sign in form. There are two fields: Username, Password |
| Click Sign up to register an account| Redirected to sign up form with four fields: Username, E-mail, Password, Password confirmation |
| Click Sign up button without filling out the form| The form isn't submitted|
|Fill out the form|All the fields are working properly. New account is registered. I'm logged in and redirected to home page.|
|Click Logout | Redirected to Sign out page with question to confirm Sign out |
| Click Sign out button | Successfully signed out and redirected to home page. |
| Click Login and enter your Username and Password | Successfully logged in and redirected to home page |

### User Navigation Tests

| Instruction | Result  |
|--|--|
|Click Today's Specials | I'm moved to Today's Specials section on the home page |
|Click Menu |  I'm moved to Menu section on the home page |
| Click any of the Menu sections | I can see pop up window with more details about this section |
| Click Close | The pop up window is closed |
| Click Contact us | I'm moved to Contact Us section on the home page |
| Click "Book a Table" button | I'm redirected to sign in page |
| Sign in and click "Book a Table" button | Redirected to Booking form page |
| Click My Bookings | Redirected to My Bookings page |
| Sign in as Superuser and click Bookings | Redirected to Bookings page. As a superuser I can see all the bookings made by all the users |
| Sign in as Superuser and click Todays's Specials | Redirected to Today's specials page with the table of specials |
| Click Add Specials | Redirected to Today's specials form with four fields: Title, Description, Image, Today |
| Click "Ukrainian Cafe" logo in the top left corner | Redirected to home page |

### Account Security Tests

| Instruction | Result  |
|--|--|
| Log out and try to open booking page by adding "/add_booking/" to website's url  | Redirected to Sign in page |
| Log out and try to access Today's Specials page by adding "/today_specials/" to website's url  | Redirected to Sign in page |
| Click "Booking" | Redirected to Sign in page|
| Add "/bookings/" to website's url | 404 page |

### Booking Tests

| Instruction |Result  |
|--|--|
| Login and click "Book a Table"| Redirected to booking form page |
| Try to submit an empty form | All the fields are required |
| Enter data in the past and try to submit the form | The form is not submitted. Future data is required |
| Enter all the required data and submit the form | The form is submitted, I'm redirected to View bookings page. |
| Click "Edit Booking" | Redirected to the booking form, prefilled with the specific booking information. |
| Change some data in your booking and submit the form | The form is submitted, the booking information is updated|
| Click "Delete Booking" | Redirected to the booking form with the specific booking information and the question "Are you sure you want to delete this booking?" |
| Click "Delete Booking" again. | The booking is deleted. |
| Login as an admin and click "Bookings" | Business owner can view, edit and delete all bookings |

### Specials Tests

| Instruction | Result  |
|--|--|
| Login as an admin and tap "Today's Specials" in menu | Redirected to Today's Specials page |
| Click "Add Specials" | Redirected to "Add Specials" page with form. There are four fields: Title, Descriptiion, Image, Today |
| Fill out the form, add an image, type "yes" in Today field | All the fields work properly. The form is submitted. I'm redirected to today's specials list |
| Go to home page and check Today's Specials | My dish is added to today's specials |
| Tap "Today's Specials" in menu. Find the dish you added and click "Edit" | Redirected to edit specials page with the form. |
| Type "no" instead of "yes" in Today field. Submit the form. | The form is submitted. I'm redirected to today's specials list |
| Go to home page and check Today's Specials | My dish is no longer shown in today's specials on home page |
| Tap "Today's Specials" in menu. Find the dish you added and click "Delete" | Redirected to delete specials page with the form and question "Are you sure...?" |
| Click "Delete" | Redirected to today's specials list. The item has been deleted |
