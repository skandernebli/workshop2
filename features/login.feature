Feature: logging different users
  
  Scenario: users can login
	Given the user navigates to the url
	When he enters the "username" and "pwd"
	And clicks on the submit button below
	Then he must see a welcome message
  
  
  Scenario Outline: users can login
	Given the user navigates to the url
	When he enters the "<username>" and "<pwd>"
	And clicks on the submit button below
	Then he must see a welcome message
	Examples:
	  | username | pwd |
	  | skan    | pwd |
	  |      |  |
	  | 77888    | pw  |

	  