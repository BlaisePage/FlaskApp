
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
import os
#from bokeh.charts import Histogram
from bokeh.embed import components



names = ['Fernando Abad', 'Dustin Ackley', 'Ronald Acuna Jr.', 'Cristhian Adames', 'Willy Adames', 'Lane Adams', 'Matt Adams', 'Tim Adleman', 'Ehire Adrianza', 'Jesus Aguilar', 'Nick Ahmed', 'Andrew Albers', 'Matt Albers', 'Hanser Alberto', 'Ozzie Albies', 'Arismendy Alcantara', 'Sandy Alcantara', 'Scott Alexander', 'Jorge Alfaro', 'Anthony Alford', 'Kolby Allard', 'Greg Allen', 'Yency Almonte', 'Albert Almora', 'Yonder Alonso', 'Aaron Altherr', 'Dariel Alvarez', 'Henderson Alvarez III', 'Alexi Amarista', 'Robert Andino', 'John Andreoli', 'Matt Andriese', 'Elvis Andrus', 'Miguel Andujar', 'Nori Aoki', 'Aristides Aquino', 'Jayson Aquino', 'Chris Archer', 'Francisco Arcia', 'Orlando Arcia', 'Oswaldo Arcia', 'Nolan Arenado', 'Jake Arrieta', 'Bronson Arroyo', 'Christian Arroyo', 'Cody Asche', 'Alec Asher', 'Barrett Astin', 'Willians Astudillo', 'Carlos Asuaje', 'Abiatal Avelino', 'Alex Avila', 'Luis Avilan', 'Erick Aybar', 'Harrison Bader', 'Javier Baez', 'Homer Bailey', 'Anthony Banda', 'Jett Bandy', 'Johnny Barbato', 'Brandon Barnes', 'Jacob Barnes', 'Darwin Barney', 'Tucker Barnhart', 'Steven Baron', 'Kyle Barraclough', 'Franklin Barreto', 'Jaime Barria', 'Tyler Bashlor', 'Antonio Bastardo', 'Jake Bauers', 'Buddy Baumann', 'Rafael Bautista', 'Gordon Beckham', 'Tim Beckham', 'Tyler Beede', 'Jalen Beeks', 'Matt Belisle', 'Cody Bellinger', 'Brandon Belt', 'Andrew Benintendi', 'James Beresford', 'Christian Bergman', 'Jose Berrios', 'Quintin Berry', 'Jon Berti', 'Dellin Betances', 'Christian Bethancourt', 'Chad Bettis', 'Mookie Betts', 'Joe Biagini', 'Austin Bibens-Dirkx', 'Jesse Biddle', 'Shane Bieber', 'Greg Bird', 'Ty Blach', 'Paul Blackburn', 'Charlie Blackmon', 'Andres Blanco', 'Gregor Blanco', 'Alex Blandino', 'Joe Blanton', 'Jabari Blash', 'Michael Blazek', 'Jerry Blevins', 'Xander Bogaerts', 'Mike Bolsinger', 'Emilio Bonifacio', 'Jorge Bonifacio', 'Lisalverto Bonilla', 'Julio Borbon', 'John Bormann', 'Wilfredo Boscan', 'Christopher Bostick', 'David Bote', 'Justin Bour', 'Peter Bourjos', 'Michael Bourn', 'Matt Bowman', 'Blaine Boyer', 'Silvino Bracho', 'Archie Bradley', 'Jackie Bradley Jr.', 'Michael Brantley', 'Rob Brantly', 'Steven Brault', 'John Brebbia', 'Alex Bregman', 'Bryce Brentz', 'Austin Brice', 'Jeff Brigham', 'Reid Brignac', 'Lewis Brinson', 'Socrates Brito', 'Mike Broadway', 'Keon Broxton', 'Jay Bruce', 'Jaycob Brugman', 'Kris Bryant', 'Jake Buchanan', 'Clay Buchholz', 'Walker Buehler', 'Madison Bumgarner', 'Dylan Bundy', 'Corbin Burnes', 'Emmanuel Burriss', 'Matt Buschmann', 'Nick Buss', 'Drew Butera', 'Billy Butler', 'Dan Butler', 'Eddie Butler', 'Byron Buxton', 'Marlon Byrd', 'Asdrubal Cabrera', 'Melky Cabrera', 'Ramon Cabrera', 'Trevor Cahill', 'Lorenzo Cain', 'Matt Cain', 'Kole Calhoun', 'Willie Calhoun', 'Orlando Calixte', 'Johan Camargo', 'Arquimedes Caminero', 'Vicente Campos', 'Jeimer Candelario', 'Mark Canha', 'Robinson Cano', 'Chris Capuano', 'Victor Caratini', 'Stephen Cardullo', 'Shane Carle', 'Ezequiel Carrera', 'Curt Casali', 'Andrew Cashner', 'Rusney Castillo', 'Welington Castillo', 'Harold Castro', 'Jason Castro', 'Starlin Castro', 'Jake Cave', 'Gavin Cecchini', 'Brett Cecil', 'Darrell Ceciliani', 'Francisco Cervelli', 'Yoenis Cespedes', 'Luis Cessa', 'Jhoulys Chacin', 'Tyler Chatwood', 'Jesse Chavez', 'Wei-Yin Chen', 'Robinson Chirinos', 'Yonny Chirinos', 'Lonnie Chisenhall', 'Ji-Man Choi', 'Shin-Soo Choo', 'Adam Cimber', 'Tony Cingrani', 'Steve Cishek', 'Nick Ciuffo', 'Steve Clevenger', 'Mike Clevinger', 'Tyler Cloyd', 'Jason Coats', 'Alex Cobb', 'Chris Coghlan', 'Chris Colabello', 'Gerrit Cole', 'Dusty Coleman', 'Josh Collmenter', 'Bartolo Colon', 'Christian Colon', 'Michael Conforto', 'Hank Conger', 'Adam Conley', 'Willson Contreras', 'Garrett Cooper', 'Patrick Corbin', 'Daniel Corcino', 'Ryan Cordell', 'Franchy Cordero', 'Allen Cordoba', 'Carlos Correa', 'Jarred Cosart', 'Jharel Cotton', 'Dylan Covey', 'Kaleb Cowart', 'Collin Cowgill', 'Zack Cozart', 'Dylan Cozens', 'Tyler Cravy', 'Brandon Crawford', 'Carl Crawford', 'Coco Crisp', 'Tony Cruz', 'Johnny Cueto', 'Noel Cuevas', 'Cheslor Cuthbert', "Chase d'Arnaud", "Travis d'Arnaud", 'David Dahl', 'Yu Darvish', 'Khris Davis', 'Rajai Davis', 'Rookie Davis', 'Grant Dayton', 'Austin Dean', 'Jaff Decker', 'Jacob deGrom', 'Paul DeJong', 'Randall Delgado', 'Daniel Descalso', 'Anthony DeSclafani', 'Ian Desmond', 'Odrisamer Despaigne', 'Ross Detwiler', 'Chris Devenski', 'Rafael Devers', 'Aledmys Diaz', 'Jumbo Diaz', 'Yandy Diaz', 'Corey Dickerson', "O'Koyea Dickson", 'Derek Dietrich', 'Wilmer Difo', 'Brandon Dixon', 'Matt Dominguez', 'Seranthony Dominguez', 'Josh Donaldson', 'Brian Dozier', 'Hunter Dozier', 'Oliver Drake', 'Stephen Drew', 'Brandon Drury', 'Lucas Duda', 'Brian Duensing', 'Tyler Duffey', 'Danny Duffy', 'Steven Duggar', 'Zach Duke', 'Adam Duvall', 'Jarrod Dyson', 'Carl Edwards Jr.', 'Zach Eflin', 'Cody Ege', 'Brett Eibner', 'Jerad Eickhoff', 'Roenis Elias', 'Brian Ellington', 'Jacoby Ellsbury', 'Jake Elmore', 'Edwin Encarnacion', 'Adam Engel', 'Dietrich Enns', 'Nathan Eovaldi', 'Robbie Erlin', 'Phil Ervin', 'Jake Esch', 'Alcides Escobar', 'Eduardo Escobar', 'Edwin Escobar', 'Yunel Escobar', 'Paolo Espino', 'Danny Espinosa', 'Andre Ethier', 'Phillip Evans', 'Jeurys Familia', 'Kyle Farmer', 'Luke Farrell', 'Taylor Featherston', 'Erick Fedde', 'Tim Federowicz', 'Scott Feldman', 'Caleb Ferguson', 'Johnny Field', 'Prince Fielder', 'Mike Fiers', 'Cole Figueroa', 'Heath Fillmyer', 'Brandon Finnegan', 'Doug Fister', 'Ryan Flaherty', 'Yohan Flande', 'David Fletcher', 'Chris Flexen', 'Kendry Flores', 'Wilmer Flores', 'Pedro Florimon', 'Dylan Floro', 'Tyler Flowers', 'Gavin Floyd', 'Mike Foltynewicz', 'Wilmer Font', 'Nolan Fontana', 'Logan Forsythe', 'Dexter Fowler', 'Dustin Fowler', 'Maikel Franco', 'Jeff Francoeur', 'Nick Franklin', 'Adam Frazier', 'Clint Frazier', 'Todd Frazier', 'Kyle Freeland', 'Freddie Freeman', 'Mike Freeman', 'Sam Freeman', 'David Freitas', 'Carlos Frias', 'Max Fried', 'Christian Friedrich', 'Eric Fryer', 'Michael Fulmer', 'Drew Gagnon', 'Rocky Gale', 'Cam Gallagher', 'Yovani Gallardo', 'Giovanny Gallegos', 'Joey Gallo', 'Freddy Galvis', 'Ben Gamel', 'John Gant', 'Adolis Garcia', 'Adonis Garcia', 'Aramis Garcia', 'Avisail Garcia', 'Jarlin Garcia', 'Leury Garcia', 'Willy Garcia', 'Brett Gardner', 'Dustin Garneau', 'Amir Garrett', 'Mitch Garver', 'Matt Garza', 'Evan Gattis', 'Kevin Gausman', 'Sam Gaviglio', 'Cory Gearrin', 'Dillon Gee', 'Scooter Gennett', 'Craig Gentry', 'Mike Gerber', 'Domingo German', 'Gonzalez Germen', 'Johnny Giavotella', 'Conor Gillaspie', 'Cole Gillespie', 'Sean Gilmartin', 'Lucas Giolito', 'Mychal Givens', 'Tyler Glasnow', 'Zack Godley', 'Tyler Goeddel', 'Luiz Gohara', 'Ryan Goins', 'Paul Goldschmidt', 'Austin Gomber', 'Yan Gomes', 'Erik Gonzalez', 'Gio Gonzalez', 'Marwin Gonzalez', 'Merandy Gonzalez', 'Severino Gonzalez', 'Niko Goodrum', 'Dee Gordon', 'Terrance Gore', 'Anthony Gose', 'Tuffy Gosewisch', 'Daniel Gossett', 'Matt Grace', 'Yasmani Grandal', 'Curtis Granderson', 'Juan Graterol', 'Kendall Graveman', 'Brett Graves', 'Sonny Gray', 'Grant Green', 'Shane Greene', 'Didi Gregorius', 'Grayson Greiner', 'Zack Greinke', 'Randal Grichuk', 'Justin Grimm', 'Robbie Grossman', 'Robert Gsellman', 'Junior Guerra', 'Gabriel Guerrero', 'Luis Guillorme', 'Lourdes Gurriel Jr.', 'Yuli Gurriel', 'Franklin Gutierrez', 'Brandon Guyer', 'Ronald Guzman', 'Jedd Gyorko', 'Eric Haase', 'Josh Hader', 'Jesse Hahn', 'Cole Hamels', 'Jason Hammel', 'Garrett Hampson', 'Brad Hand', 'Ryan Hanigan', 'Mitch Haniger', 'Jacob Hannemann', 'Alen Hanson', 'Ian Happ', 'Bryce Harper', 'Lucas Harrell', 'Josh Harrison', 'Donnie Hart', 'Austin Hays', 'Jeremy Hazelbaker', 'Chase Headley', 'Ryon Healy', 'Andrew Heaney', 'Adeiny Hechavarria', 'Chris Heisey', 'Jeremy Hellickson', 'Heath Hembree', 'Guillermo Heredia', 'Michael Hermosillo', 'Elieser Hernandez', 'Gorkys Hernandez', 'Teoscar Hernandez', 'Dilson Herrera', 'Odubel Herrera', 'Rosell Herrera', 'Chris Herrmann', 'David Hess', 'Jason Heyward', 'Aaron Hicks', 'Kyle Higashioka', 'Yoshihisa Hirano', 'Bryan Holaday', 'Derek Holland', 'Matt Holliday', 'Clay Holmes', 'Brock Holt', 'Destin Hood', 'Rhys Hoskins', 'Eric Hosmer', 'Jared Hoying', 'James Hoyt', 'Dakota Hudson', 'Chad Huffman', 'Jared Hughes', 'Phil Hughes', 'Nick Hundley', 'Cedric Hunter', 'Tommy Hunter', 'Drew Hutchison', 'Jae-gyun Hwang', 'Chris Iannetta', 'Jose Iglesias', 'Raisel Iglesias', 'Ender Inciarte', 'Omar Infante', 'Hernan Iribarren', 'Hisashi Iwakuma', 'Edwin Jackson', 'Paul Janish', 'Travis Jankowski', 'Danny Jansen', 'Kenley Jansen', 'John Jaso', 'Jon Jay', 'Jeremy Jeffress', 'Tyrell Jenkins', 'Desmond Jennings', 'Ubaldo Jimenez', 'Pierce Johnson', 'Sherman Johnson', 'JaCoby Jones', 'Ryder Jones', 'Caleb Joseph', 'Corban Joseph', 'Tommy Joseph', 'Matthew Joyce', 'Aaron Judge', 'Taylor Jungmann', 'Jakob Junis', 'Ariel Jurado', 'Kevin Kaczmarski', 'Ryan Kalish', 'Nate Karns', 'Munenori Kawasaki', 'Scott Kazmir', 'Brad Keller', 'Carson Kelly', 'Don Kelly', 'Tony Kemp', 'Howie Kendrick', 'Kyle Kendrick', 'Ian Kennedy', 'Max Kepler', 'Clayton Kershaw', 'Dallas Keuchel', 'Spencer Kieboom', 'Dean Kiekhefer', 'Kevin Kiermaier', 'Isiah Kiner-Falefa', 'Scott Kingery', 'Nick Kingham', 'Ian Kinsler', 'Brandon Kintzler', 'Jason Kipnis', 'Andrew Kittredge', 'Patrick Kivlehan', 'Phil Klein', 'Corey Kluber', 'Andrew Knapp', 'Tom Koehler', 'George Kontos', 'Pete Kozma', 'Erik Kratz', 'Ian Krol', 'Chad Kuhl', 'Tyler Ladendorf', 'Juan Lagares', 'Junior Lake', 'Blake Lalli', 'Ryan LaMarre', 'Jake Lamb', 'Andrew Lambo', 'Dinelson Lamet', 'Mat Latos', 'Eric Lauer', 'Ramon Laureano', 'Ryan Lavarnway', 'Derek Law', 'Casey Lawrence', 'Brett Lawrie', 'Mike Leake', 'Wade LeBlanc', 'Braxton Lee', 'Dae-ho Lee', 'Zach Lee', 'DJ LeMahieu', 'Sandy Leon', 'Jon Lester', 'Adam Liberatore', 'Tzu-Wei Lin', 'Adam Lind', 'Josh Lindblom', 'Francisco Lindor', 'Francisco Liriano', 'Rymer Liriano', 'Ben Lively', 'Kyle Lloyd', 'Kyle Lobstein', 'Tim Locastro', 'Jeff Locke', 'Walker Lockett', 'James Loney', 'Evan Longoria', 'Reynaldo Lopez', 'Michael Lorenzen', 'David Lough', 'Jed Lowrie', 'Joey Lucchesi', 'Jonathan Lucroy', 'Dawel Lugo', 'Seth Lugo', 'Jordan Luplow', 'Jordan Lyles', 'Lance Lynn', 'Tyler Lyons', 'Dixon Machado', 'Manny Machado', 'Jean Machi', 'Ryan Madson', 'Kenta Maeda', 'Matt Magill', 'Tyler Mahle', 'Mikie Mahtook', 'Luke Maile', 'Kazuhisa Makita', 'Martin Maldonado', 'Sean Manaea', 'Trey Mancini', 'Seth Maness', 'Manuel Margot', 'Jhan Marinez', 'Jake Marisnick', 'Mike Marjama', 'Nick Markakis', 'German Marquez', 'Chris Marrero', 'Deven Marrero', 'Jefry Marte', 'Ketel Marte', 'Starling Marte', 'Leonys Martin', 'Nick Martini', 'Darin Mastroianni', 'Jeff Mathis', 'Steven Matz', 'Joe Mauer', 'Cameron Maybin', 'Mike Mayers', 'Nomar Mazara', 'Vin Mazzaro', 'Matt McBride', 'Brian McCann', 'Brandon McCarthy', 'Andrew McCutchen', 'Casey McGehee', 'Dustin McGowan', 'Kyle McGowin', 'Kyle McGrath', 'Deck McGuire', 'Reese McGuire', 'Collin McHugh', 'Michael McKenry', 'Jeff McNeil', 'Alex McRae', 'Austin Meadows', 'Kris Medlen', 'Adalberto Mejia', 'Alex Mejia', 'Keury Mella', 'Tim Melville', 'Yohander Mendez', 'Daniel Mengden', 'Jordy Mercer', 'Whit Merrifield', 'Devin Mesoraco', 'Alex Meyer', 'Ben Meyer', 'Will Middlebrooks', 'Miles Mikolas', 'Wade Miley', 'Shelby Miller', 'Alec Mills', 'Hoby Milner', 'Tommy Milone', 'Mike Minor', 'Ariel Miranda', 'Bryan Mitchell', 'Yadier Molina', 'Yoan Moncada', 'Carlos Moncrief', 'Adalberto Mondesi', 'Frankie Montas', 'Rafael Montero', 'Kendrys Morales', 'Mitch Moreland', 'Adam Morgan', 'Justin Morneau', 'Max Moroff', 'Reyes Moronta', 'Logan Morrison', 'Brandon Morrow', 'Jon Moscot', 'Taylor Motter', 'Mike Moustakas', 'Steven Moya', 'Cedric Mullins', 'Max Muncy', 'Yairo Munoz', 'Colton Murray', 'Harrison Musgrave', 'Joe Musgrove', 'Wil Myers', 'Tyler Naquin', 'Omar Narvaez', 'Chris Narveson', 'Daniel Nava', 'Dioner Navarro', 'Efren Navarro', 'Zach Neal', 'Kristopher Negron', 'Hector Neris', 'Sean Newcomb', 'Kevin Newman', 'Gift Ngoepe', 'Juan Nicasio', 'Brett Nicholas', 'Justin Nicolino', 'Tomas Nido', 'Kirk Nieuwenhuis', 'Brandon Nimmo', 'Jacob Nix', 'Aaron Nola', 'Ricky Nolasco', 'Nick Noonan', 'Bud Norris', 'Daniel Norris', 'Derek Norris', 'James Norwood', 'Jacob Nottingham', 'Ivan Nova', 'Renato Nunez', 'Vidal Nuno III', "Peter O'Brien", "Chris O'Grady", "Shawn O'Malley", "Tyler O'Neill", "Ryan O'Rourke", 'Brett Oberholtzer', 'Jake Odorizzi', 'Seunghwan Oh', 'Mike Ohlman', 'Shohei Ohtani', 'Steven Okert', 'Hector Olivera', 'Nate Orf', 'Paulo Orlando', 'Danny Ortiz', 'Jose Osuna', 'Corey Oswalt', 'Dillon Overton', 'Chris Owings', 'Marcell Ozuna', 'Emilio Pagan', 'Daniel Palka', 'Joe Panik', 'Jimmy Paredes', 'Jarrett Parker', 'Chris Parmelee', 'Ian Parmley', 'Gerardo Parra', 'Wes Parsons', 'Jordan Patterson', 'Spencer Patton', 'Ben Paulsen', 'James Paxton', 'Brad Peacock', 'Jake Peavy', 'Joc Pederson', 'Dustin Pedroia', 'Brayan Pena', 'Felix Pena', 'Hunter Pence', 'Cliff Pennington', 'David Peralta', 'Freddy Peralta', 'Jhonny Peralta', 'Joel Peralta', 'Wandy Peralta', 'Wily Peralta', 'Hernan Perez', 'Oliver Perez', 'Salvador Perez', 'Williams Perez', 'Yefri Perez', 'Cameron Perkins', 'Dillon Peters', 'Dustin Peterson', 'Jace Peterson', 'Shane Peterson', 'Gregorio Petit', 'Yusmeiro Petit', 'Jake Petricka', 'Tommy Pham', 'Josh Phegley', 'David Phelps', 'Brandon Phillips', 'Brett Phillips', 'Tyler Pill', 'Kevin Pillar', 'Manny Pina', 'Chad Pinder', 'Michael Pineda', 'Josmil Pinto', 'Ricardo Pinto', 'Jose Pirela', 'Stephen Piscotty', 'Nick Pivetta', 'Kevin Plawecki', 'Trevor Plouffe', 'Adam Plutko', 'Gregory Polanco', 'Jorge Polanco', 'Drew Pomeranz', 'Dalton Pompey', 'Rick Porcello', 'Buster Posey', 'Martin Prado', 'Alex Presley', 'Jurickson Profar', 'Austin Pruitt', 'Cesar Puello', 'Yasiel Puig', 'Albert Pujols', 'Kevin Quackenbush', 'Juniel Querecuto', 'Roman Quinn', 'Jose Quintana', 'Ryan Raburn', 'Alexei Ramirez', 'Hanley Ramirez', 'Neil Ramirez', 'Yefry Ramirez', 'Edubray Ramos', 'Wilson Ramos', 'Anthony Ranaudo', 'Colby Rasmus', 'Josh Ravin', 'Robbie Ray', 'Colin Rea', 'Raudy Read', 'Anthony Recker', 'Josh Reddick', 'Rob Refsnyder', 'Sean Reid-Foley', 'Nolan Reimold', 'Jack Reinheimer', 'Tony Renda', 'Anthony Rendon', 'Hunter Renfroe', 'Ben Revere', 'Franmil Reyes', 'Jacob Rhame', 'Clayton Richard', 'Trevor Richards', 'Joey Rickard', 'JT Riddle', 'Yacksel Rios', 'Yadiel Rivera', 'Tanner Roark', 'Clint Robinson', 'Drew Robinson', 'Shane Robinson', 'Hansel Robles', 'Carlos Rodon', 'Dereck Rodriguez', 'Jefry Rodriguez', 'Joely Rodriguez', 'Sal Romano', 'Enny Romero', 'Fernando Romero', 'Stefen Romero', 'Andrew Romine', 'Austin Romine', 'Sergio Romo', 'Hector Rondon', 'Adam Rosales', 'Alberto Rosario', 'Amed Rosario', 'Eddie Rosario', 'Randy Rosario', 'Trevor Rosenthal', 'Tyson Ross', 'Ryan Rua', 'Drew Rucinski', 'Darin Ruf', 'Justin Ruggiano', 'Rio Ruiz', 'Cameron Rupp', 'Chris Rusin', 'Addison Russell', 'Josh Rutledge', 'Hyun-Jin Ryu', 'CC Sabathia', 'Casey Sadler', 'Tyler Saladino', 'Fernando Salas', 'Chris Sale', 'Jarrod Saltalamacchia', 'Jeff Samardzija', 'Keyvius Sampson', 'Aaron Sanchez', 'Anibal Sanchez', 'Pablo Sandoval', 'Jerry Sands', 'Miguel Sano', 'Danny Santana', 'Dennis Santana', 'Ervin Santana', 'Anthony Santander', 'Luis Sardinas', 'Michael Saunders', 'Warwick Saupold', 'Rob Scahill', 'Logan Schafer', 'Scott Schebler', 'Max Scherzer', 'Ryan Schimpf', 'Jonathan Schoop', 'Kyle Schwarber', 'Troy Scribner', 'Xavier Scruggs', 'Corey Seager', 'Kyle Seager', 'Rob Segedin', 'Jean Segura', 'Steve Selsky', 'Marcus Semien', 'Antonio Senzatela', 'Pedro Severino', 'Paul Sewald', 'Kevin Shackelford', 'Richie Shaffer', 'Braden Shipley', 'Chasen Shreve', 'JB Shuck', 'Magneuris Sierra', 'Moises Sierra', 'Andrelton Simmons', 'Alfredo Simon', 'Lucas Sims', 'Tony Sipp', 'Chance Sisco', 'Tyler Skaggs', 'Eric Skoglund', 'Matt Skole', 'Austin Slater', 'Kevan Smith', 'Mallex Smith', 'Seth Smith', 'Justin Smoak', 'Josh Smoker', 'Jake Smolinski', 'Drew Smyly', 'Blake Snell', 'Chad Sobotka', 'Miguel Socolovich', 'Eric Sogard', 'Donovan Solano', 'Yangervis Solarte', 'Jorge Soler', 'Sammy Solis', 'Mike Soroka', 'Edmundo Sosa', 'Geovany Soto', 'Steven Souza Jr.', 'Denard Span', 'Cory Spangenberg', 'George Springer', 'Jacob Stallings', 'Craig Stammen', 'Giancarlo Stanton', 'Brock Stassi', 'Max Stassi', 'Jackson Stephens', 'Andrew Stevenson', 'Christin Stewart', 'DJ Stewart', 'Drew Storen', 'Trevor Story', 'Matt Strahm', 'Dan Straily', 'Stephen Strasburg', 'Myles Straw', 'Ross Stripling', 'Marcus Stroman', 'Pedro Strop', 'Drew Stubbs', 'Andrew Suarez', 'Eugenio Suarez', 'Ranger Suarez', 'Jesus Sucre', 'Wander Suero', 'Andrew Susac', 'Brent Suter', 'Ichiro Suzuki', 'Kurt Suzuki', 'Dansby Swanson', 'Darnell Sweeney', 'Blake Swihart', 'Noah Syndergaard', 'Matt Szczur', 'Travis Taijeron', 'Jameson Taillon', 'Raimel Tapia', 'Mike Tauchman', 'Beau Taylor', 'Junichi Tazawa', 'Julio Teheran', 'Mark Teixeira', 'Ruben Tejada', 'Tomas Telis', 'Rowdy Tellez', 'Ryan Tepera', 'Nick Tepesch', 'Eric Thames', 'Jesen Therrien', 'Josh Thole', 'Trayce Thompson', 'Chris Tillman', 'Charlie Tilson', 'Carlos Tocci', 'Andrew Toles', 'Shawn Tolleson', 'Yasmany Tomas', 'Josh Tomlin', 'Kelby Tomlinson', 'Michael Tonkin', 'Luis Torrens', 'Gleyber Torres', 'Ronald Torreyes', 'Touki Toussaint', 'Blake Trahan', 'Devon Travis', 'Sam Travis', 'Jose Trevino', 'Andrew Triggs', 'Nick Tropeano', 'Mike Trout', 'Mark Trumbo', 'Jen-Ho Tseng', 'Matt Tuiasosopo', 'Troy Tulowitzki', 'Nik Turley', 'Spencer Turnbull', 'Stuart Turner', 'Trea Turner', 'Duane Underwood Jr.', 'Justin Upton', 'Richard Urena', 'Julio Urias', 'Luis Urias', 'Gio Urshela', 'Chase Utley', 'Pat Valaika', 'Luis Valbuena', 'Danny Valencia', 'Jesmuel Valentin', 'Breyvic Valera', 'Cesar Vargas', 'Ildemaro Vargas', 'Jason Vargas', 'Kennys Vargas', 'Vince Velasquez', 'Andrew Velazquez', 'Will Venable', 'Yordano Ventura', 'Alex Verdugo', 'Drew VerHagen', 'Justin Verlander', 'Logan Verrett', 'Engelb Vielma', 'Carlos Villanueva', 'Christian Villanueva', 'Jonathan Villar', 'Meibrys Viloria', 'Zach Vincej', 'Ryan Vogelsong', 'Stephen Vogt', 'Luke Voit', 'Edinson Volquez', 'Austin Voth', 'Joey Votto', 'Michael Wacha', 'Tyler Wade', 'Adam Wainwright', 'Mitch Walding', 'Christian Walker', 'Neil Walker', 'Taijuan Walker', 'Chad Wallach', 'Zach Walters', 'Taylor Ward', 'Adam Warren', 'Tony Watson', 'Jered Weaver', 'Luke Weaver', 'Jemile Weeks', 'Rickie Weeks', 'Joey Wendle', 'Jayson Werth', 'Matt Wieters', 'Tom Wilhelmsen', 'Adam Wilk', 'Aaron Wilkerson', 'Stevie Wilkerson', 'Andy Wilkins', 'Jerome Williams', 'Mason Williams', 'Mac Williamson', 'Bryse Wilson', 'Jesse Winker', 'Dan Winkler', 'Patrick Wisdom', 'Matt Wisler', 'Nick Wittgren', 'Asher Wojciechowski', 'Tony Wolters', 'Kolten Wong', 'Alex Wood', 'Blake Wood', 'Travis Wood', 'Brandon Woodruff', 'Vance Worley', 'Danny Worth', 'Austin Wynns', 'Jimmy Yacabonis', 'Ryan Yarbrough', 'Kirby Yates', 'Christian Yelich', 'Gabriel Ynoa', 'Rafael Ynoa', 'Mark Zagunis', 'Rob Zastryzny', 'Bradley Zimmer', 'Jordan Zimmermann', 'Ben Zobrist', 'Mike Zunino']


# create the application object
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


slg_data = pd.read_csv("statcast_data/final_slg_data.csv")
init_name = "Jayson Werth"

def create_bar(name):
    SLG = 0
    EGS = 0
    LGS = 0
    for index, row in slg_data.iterrows():
        if(row['name']==name):
            SLG = row['SLG']
            EGS = row['EGS']
            LGS = row['LGS']

    #print(SLG)
    #print(EGS)
    #print(LGS)

    title_string = (name + " SLG, EGS, and LGS")
    labels = ['SLG', 'EGS', 'LGS']
    p = figure(title=title_string, y_range=labels, x_range=(0,1.5), plot_width=700, plot_height=600)
    p.yaxis.major_label_orientation = np.pi/4   # radians, "horizontal", "vertical", "normal"

    p.hbar(y=labels, height=0.5, left=0, right=[SLG,EGS,LGS], color="#CAB2D6")
    p.xaxis.axis_label = "SLG Values"

    return p


# use decorators to link the function to a url
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    error = None
    if request.method == 'POST':
        # checks that both the username and password are 'admin' -> change this to a RDS check
        if request.form['player_name'] == None or request.form['player_name'] not in names:
            error = 'Invalid Player. Please try again.'
        else:
            # Create the plot
            print(request.form['player_name'])
            current_player_name=request.form['player_name']
            plot = create_bar(current_player_name)
            #plot = create_figure(test_list)

            # Embed plot into HTML via Flask Render
            script, div = components(plot)
            return render_template('visualization.html', script=script, div=div, current_player_name=current_player_name, error=error)

    return render_template('calculate.html', error=error)



@app.route('/visualization', methods=['GET', 'POST'])
def visualization():

    error = None
    if request.method == 'POST':
        # checks that both the username and password are 'admin' -> change this to a RDS check
        if request.form['player_name'] == None or request.form['player_name'] not in names:
            error = 'Invalid Player. Please try again.'
        else:
            # Create the plot
            print(request.form['player_name'])
            current_player_name=request.form['player_name']
            plot = create_bar(current_player_name)
            #plot = create_figure(test_list)

            # Embed plot into HTML via Flask Render
            script, div = components(plot)
            return render_template('visualization.html', script=script, div=div, current_player_name=current_player_name, error=error)


    #plot = create_figure(test_list)
    plot = create_bar(init_name)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template('visualization.html', script=script, div=div, error=error)



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
#    cur = g.db_conn.cursor()
#    cur.execute("SELECT * FROM country;")
    return render_template('home.html')
    #return "Hello World"

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
