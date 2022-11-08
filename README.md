# PiPicoMacroPad
<h1>Macropad With Raspberry Pi Pico</h1>
Just a simple yet "efficient" code for a macro pad built with a raspberry py pico

This is simple code made by me to minimize the size of the .py file loaded onto the board.
There is a better way to implement this code, I am sure, and here you are free to modify or update it

<h1>SETUP AND INSTALLATION:</h1>
The first time you'll connect your pi pico to you pc, it will show as an external drive.
You will only have to drag the <b>.uf2</b> file also posted in my repo.
(you can also look for the latest version here: https://circuitpython.org/board/raspberry_pi_pico/)
  
After the file is on the pico, it will reboot on its own and you will see some files and folders on it

You now just have to copy the file <b>pad.py</b> on it.
IMPORTANT: 
<ul>
  <li>In the code set the GP numbers in correspondence of the button connection on your pico</li>
  <li>You are free to change names and delcare new ones (functions too) as i did (just follow my comments in the code)</li>
  <li><b>In order to autostart the script, the file must be renamed main.py</b></li>
  <li><b>Copy the content of the lib folder provided by the prepo into your pico lib folder (those are adafruit libs, with it you can emulate both mouse and keyboard)</b></li>
  <li><h2>HAVE FUN!</h2></li>
</ul> 

For any question or collaboration feel free to contact me!

<h2>Simple explaination of my code (top-down)</h2>
<ul>
  <li>Library inclusion</li>
  <li>button pin declaration: specify name and GPnumber (can see on photo posted in repo or on official raspPi Pico page)</li>
  <li>Adding your buttons to a list (this will come handy later), <b>don't forget</b> to add/rename here your new buttons</li>
  <li>Keyboard object to emulate key press (don't need to change anything here)</li>
  <li>Writing functions: you can call those as you want, here you code your combination, you can write as many keys as you want (list will be at the bottom of the file). Remember to put both press and release or you will bestuck wit your combination active</li>
  <li>List of function names we just created, same story as the name list, just pay attention to not add "( )" at the end of each name </li>
  <li>Magic for loop (don't need to touch it): here is where the code savings happens, indeed we use the list to initialize all the button, instead of writing the same code for all buttons</li>
  <li>Waiting and listening for button to be pressed  (don't need to touch it)</li>
  <li>Disclaimer: feel free to play with timings if you feel them too fast/slow, just change value in time.sleep(value)</li>
</ul>
