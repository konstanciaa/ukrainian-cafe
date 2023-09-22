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
|Non logged in user cannot access bookings page | Pass|
|Non superuser cannot view all users bookings |Pass|
|Non superuser cannot access Today's Specials page |Pass|
|Non superuser cannot access admin panel|Pass|

### Booking Tests

| Test |Result  |
|--|--|
|User can make a booking when all fields complete | Pass |
|User tries to submit booking with empty form |Fail|
|User tries to submit form without email address| Fail|
|User tries to submit form without phone number | Fail|
|User can view their bookings on My Bookings page |Pass|
|User can edit their booking | Pass|
|User can delete their booking | Pass|
|Business owner can view all bookings | Pass |
|Business owner can edit all bookings | Pass |
|Business owner can delete all bookings | Pass |

### Specials Tests

| Test |Result  |
|--|--|
|Business owner can add items to specials|Pass|
|Business owner can add a new item with title, description and image in "Add Specials" form |Pass|
|Business owner can edit items in specials|Pass|
|Business owner can delete items in specials|Pass|
