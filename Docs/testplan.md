## Test plan
### General information
- Product name: SSN Validation Algorithm.
- Author: Juan Avila, ID1100378.
- Project description: Algorithm that checks whether an input fulfills the conditions to be a valid SSN (9 digits, divided in specific sections using hyphens).

### Tests
#### Unit tests
##### Preconditions
The tests will be run using an Ubuntu 22 virtual machine. The test will be performed automatically, running the test script from located inside the "tests" of the project, using the following script in the command line: 

	python3 -m unittest tests.test 
	
You shall be pointing to the root folder of the project before doing so.

##### Test List

|     #     |     Objective                                                                                        |     Input       |     Expected Result                                                                            |   |
|-----------|------------------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------|---|
|     1     |     Check result after entering string with special   characters                                     |     111-@3-2!3$ |     Prompt user that the   entered input is invalid. The user will be asked to write it again. |   |
|     2     |     Check result after   entering string with 9 digits but no hyphens                                |     123456789   |     Prompt user that the   input is invalid.                                                   |   |
|     3     |     Check result after   entering string with 9 digitis, hyphens, but 000 on the first section       |     000-11-2345 |     Prompt user that the   input is invalid.                                                   |   |
| 4         |     Check result after   entering string with 9 digitis, hyphens, but 666 on the first section       |     666-11-2345 |     Prompt user that the   input is invalid.                                                   |   |
| 5         |     Check result after   entering string with 9 digitis, hyphens, but 900 on the first section       |     900-11-2345 |     Prompt user that the   input is invalid.                                                   |   |
| 6         |     Check result after   entering string with 9 digitis, hyphens, but 916 on the first section       |     916-11-2345 |     Prompt user that the   input is invalid.                                                   |   |
|        7  |     Check result after   entering string with 9 digitis, hyphens, but 00 on the second section       |     445-00-2345 |     Prompt user that the   input is invalid.                                                   |   |
| 8         |     Check result after   entering string with 9 digitis, hyphens, but 0000 on the third section      |     445-24-0000 |     Prompt user that the   input is invalid.                                                   |   |
| 9         | Check result after entering an empty string                                                          |                 |     Prompt user that the   entered input is invalid. The user will be asked to write it again. |   |
|     10    |     Check result after   entering string with 9 digitis, hyphens, but 2 numbers in the first section | 13-331-2345     |     Prompt user that the   input is invalid.                                                   |   |
|        11 |     Check result after   entering string with 9 digitis, hyphens, but 3 numbers in the third section | 1333-331-234    |     Prompt user that the   input is invalid.                                                   |   |
|        12 |     Check result after   entering a valid string                                                     | 326-31-2376     |     Prompt user that the   input is valid.                                                     |   |

#### End to end 

##### Preconditions
Use the VM to conduct the test. The test will be done manually by the tester.
###### Objective
 Assure that the whole application and its features are working correctly.
###### Steps

| # | Description                                                                 | Expected Result                                         |
|---|-----------------------------------------------------------------------------|---------------------------------------------------------|
| 1 | Run ssn.py from console (you have   to be in the project's root directory). | Command line window should open   and show the program. |
| 2 | Give "string" as the   input. System should ask to repeat the process.      | Prompt user the user to re-enter   the SSN number.      |
| 3 | Give "132-86-8765" as   the input                                           | Prompt user that the input is   valid                   |
