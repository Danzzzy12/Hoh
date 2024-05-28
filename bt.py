#DEC BY DMC

import webbrowser
import os



print('\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠶⠛⠋⠉⠉⠀⠀⠈⠉⠙⠓⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠤⠄⠠⠤⠤⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⣤⠞⠋⠁⠀⢀⣀⣤⠶⠖⠒⠒⠶⠦⣤⣀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠛⠉⠁⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠉⠙⠲⣤⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⣴⠋⠀⠀⣀⣴⠞⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢦⣄⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠀⣀⣤⠶⠒⠋⠉⠉⠉⠉⠉⠙⠓⠲⢤⣀⠀⠈⠙⢦⡀⠀⠀⠀⠀\n⠀⢀⡾⠁⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢳⣄⠀⠀⠉⠛⠲⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⢀⡴⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠈⢳⡀⠀⠀⠀\n⠀⣾⠁⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⡶⢤⣀⠀⠀⠈⠉⠙⠓⠒⠦⠤⠤⠄⠤⠤⠤⠞⠋⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣾⣄⣸⣆⠀⠈⢷⠀⠀⠀\n⣸⠇⠀⢰⣧⠤⠤⣴⣶⣿⣾⣿⣿⣿⣿⣿⣿⣷⣷⣶⣦⣤⣀⣀⠀⠀⠈⣷⠀⠈⠙⠳⠶⢤⣄⣀⣀⣀⡀⡀⠀⠀⠀⠀⢀⣀⣤⡾⠁⠀⠀⠀⠀⠀⣀⣀⣤⣦⣶⣾⣿⣿⡋⠉⢁⣀⠿⠟⠛⢹⡆⠀⠘⡇⠀⠀\n⣿⠀⠀⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⠿⣿⣿⣿⣿⡏⠉⠉⠛⢶⣄⣽⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠛⠛⠉⠉⣿⠁⠀⠀⣤⣠⣶⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⣿⠀⠀⡧⠀⠀\n⢂⠀⠠⣿⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠓⠶⠾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣯⣀⣴⣿⣿⣿⣿⣿⣿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣟⠀⠀\n⣹⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣭⣼⡿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣯⠀⠀\n⠸⡇⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣧⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠇⠀⢰⡇⠀⠀\n⠀⠹⣄⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀⠀⠙⣧⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⢀⡟⠀⠀⠀\n⠀⠀⠘⢦⡀⠀⠙⠳⣤⣀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣀⣼⣦⣄⠀⠀⠀⠀⣠⣽⠇⠀⠀⠀⠎⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠋⠀⠀⣠⠟⠁⠀⠀⠀\n⠀⠀⠀⠀⠳⢄⣀⠀⠀⠉⠛⠛⠒⠖⠛⢿⡟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠷⠶⠾⠋⠘⠀⠝⠛⠳⣾⢿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⠷⠦⣤⣤⣀⣤⣠⣤⣤⠤⠶⠚⠋⠁⠀⣀⣤⠞⠁⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⣤⣀⣀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⢀⣀⣀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡄⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠘⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⢷⣆⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⡀⠀⠘⢧⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠙⣧⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠈⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⢿⣆⠀⠀⠙⢦⡀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠈⢷⣄⠀⠀⠂⠀⠀⠂⠀⠀⢀⠀⠀⠀⠀⠀⠀⠐⣿⠇⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠇⠈⢹⣷⡄⠀⠀⠱⣆⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠻⣦⠀⠀⠈⠀⠀⢀⠀⠀⠀⠀⠀⡀⠀⣄⢸⣿⠀⠀⠀⠀⠀⢻⣆⠄⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠛⢶⢀⣿⠋⢻⣦⡀⠀⠈⠳⣄⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⠙⣷⡄⠀⠀⠁⠀⠀⠠⠐⠀⠀⢠⣾⠋⢸⡏⠀⠀⠀⠀⠀⠉⠻⣦⠓⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⢂⣾⡟⢀⡇⣿⡿⣦⠀⠀⠘⢧\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠈⢷⣄⠀⠈⠠⠀⠀⠀⠀⢠⣿⠃⠀⣰⡇⠀⡄⠀⠀⠀⠀⠀⠹⣷⡈⢠⣄⠀⠘⠁⠀⠀⢀⣴⡿⣋⣀⡟⣿⡿⢀⣨⠻⡦⠀⢸\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠌⢻⣆⠀⠀⠄⠐⠀⢠⣿⠃⠀⠀⣼⡇⠀⡶⠀⠀⠀⠀⠀⠀⠿⣿⣆⠋⣧⡀⠀⠶⠞⠋⠁⠀⠁⢰⣾⠿⣡⡏⠀⢸⡇⠀⢸\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⢻⡆⠀⠠⠀⠀⣾⡇⠀⠀⠀⣯⣇⠀⠃⠀⠀⠀⠀⠀⠐⠃⠘⣿⣦⠀⠲⡀⠀⠀⠀⠀⠐⠞⠛⠁⠊⠁⠀⠀⢸⡇⠀⠸\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⢸⣿⡄⠀⠀⢐⣿⠁⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠩⣿⣿⡛⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⣷⡁⠀⠈⢸⣿⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠘⢿⣷⣄⠙⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⢸⣿⢃⠀⠐⠸⣿⠀⠀⠀⠀⠀⢿⡇⠀⣀⠀⠀⠀⠀⠀⠀⠐⣇⡐⡈⣿⣿⣆⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠤⠀⠂⠀⣿⡄⠀⠀⠀⠀⢸⣧⠀⢹⣷⢠⡀⢀⠀⠠⢈⢻⣷⣈⠆⣿⣿⣧⡀⠀⠻⢦⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠆⠁⠠⠀⣹⡇⠀⠀⠀⠀⢸⣿⡄⠘⣿⡠⣍⢦⡉⠆⣅⠪⢽⣿⣼⣘⠿⣿⣷⡄⠀⠈⢷⣀⠀⠀⠀⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⠁⠀⠡⠀⢸⡇⠀⠀⠀⠀⠀⣹⡇⠀⣿⣗⣮⢳⣜⣧⠆⡓⢼⣿⣷⣯⣟⣿⣿⣿⣮⠀⡀⠙⣧⠀⠀⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠈⡐⠀⡘⣿⠀⠀⠀⠀⠀⠙⣿⠀⢸⣿⣧⣟⣮⢿⣎⡵⢪⡝⣿⣿⣿⣿⣽⣿⣿⣷⣁⠀⠈⠳⣄⠀⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠐⠠⠁⢀⢻⣇⠀⠀⠀⠀⠀⢹⣧⠐⢿⣿⣻⣾⣿⣿⣿⣷⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣦⢀⠁⠀⠄⢸⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠈⢄⠁⢂⠈⣿⡀⠀⠀⠀⠀⠀⢿⡆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡲⠀⢀⢺⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⢨⡄⡈⠄⢂⢹⣇⠀⠀⠀⠀⠀⠈⣿⣌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⠀⣼⡇⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠾⠷⠿⠾⠶⠾⠿⠷⠤⠦⠤⠄⠀⠸⠷⠾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⡿⠇⠀⢀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⢀⠞\n')
print('Saif Raed @rcurr')
print('انتضر تحمل مكاتب')
import getpass
attemps = 0
if attemps < 32:
    username = input('\x1b[1;33mاكتب الباسورد: ')
    if username == '2007':
        print('\x1b[2;32m الباسورد صح ✔️✔')
    
    print('\x1b[1;31m الباسورد خطأ')
    attemps += 1
    
    
from os import system, name
from json import loads, dumps
from time import sleep, time
from hashlib import md5
from io import BytesIO

try:
    from requests import Session
    from requests.utils import quote
finally:
    pass
system('pip install requests')
from requests import Session
from requests.utils import quote

try:
    from PIL import Image
finally:
    pass
system('pip install Pillow')
from PIL import Image

class edit:
    
    def __init__(self = None, sessionid = None, username = None):
        self.username = username
        self.cookies = {
            'sessionid': str(sessionid) }
        self.r = Session()

    
    def inforamtions(self):
        
        try:
            r = self.r.get(f'''https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}''', {
                'x-ig-app-id': '936619743392459' }, {
                'username': self.username },('headers', 'data')).json()['data']['user']
        finally:
            return None
            system('cls' if name == 'nt' else 'clear')
            report(self.cookies['sessionid'], input('- Enter Username Targrt : '),('sessionid', 'username')).reportW()
        return None


    
    def csrfToken(self):
        return self.r.get('https://i.instagram.com/api/v1/accounts/login/', {
            'User-Agent': 'Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)',
            'Content-Type': 'application/x-www-form-urlencoded' },('headers',)).cookies['csrftoken']

    
    def getMe(self):
        re = self.r.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', {
            'User-Agent': 'Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935; hero2lte; samsungexynos8890; en_US; 208061712)',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-ig-app-id': '936619743392459' }, self.cookies, 6,('headers', 'cookies', 'timeout')).text
        if 'message' in re:
            exit('- error sessionid')
        re = loads(re)
        return (re['user']['email'], re['user']['phone_number'], re['user']['username'], re['user']['full_name'])

    
    def editAccount(self, name = (None,)):
        response = self.inforamtions()
        response1 = self.getMe()
        if name == False:
            name = response1[3]
        else:
            name = response[1]
        csrf = self.csrfToken()
        image = Image.open(BytesIO(self.r.get(response[2]).content))
        image.save(self.username + '.jpg')
        ok = self.r.post('https://www.instagram.com/api/v1/web/accounts/edit/', {
            'X-Csrftoken': csrf,
            'X-Ig-App-Id': '936619743392459' }, {
            'biography': response[0],
            'chaining_enabled': 'on',
            'email': response1[0],
            'external_url': response[4],
            'first_name': name,
            'phone_number': response1[1],
            'username': response1[2] }, self.cookies,('headers', 'data', 'cookies')).text
        if '14 days.' in ok:
            print('- The Name has not been UpDated')
            edit(self.cookies['sessionid'], self.username,('sessionid', 'username')).editAccount(False,('name',))
        if '{"status":"ok"}' not in ok:
            print(ok)
        response = self.r.post('https://www.instagram.com/api/v1/web/accounts/web_change_profile_picture/', {
            'X-Csrftoken': csrf,
            'X-Ig-App-Id': '936619743392459' }, {
            'profile_pic': open(self.username + '.jpg', 'rb') }, self.cookies, {
            'Content-Disposition': 'form-data',
            'name': 'profile_pic',
            'filename': 'profilepic.jpg',
            'Content-Type': 'image/jpeg' },('headers', 'files', 'cookies', 'data')).text
        if '"has_profile_pic":true' not in response:
            print('- The Avatar has not been UpDated')
        print('- The Account has been UpDated ✓')



class report:
    
    def __init__(self = None, username = None, sessionid = None):
        self.username = username
        self.url = 'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/'
        self.cookies = {
            'sessionid': sessionid }
        self.headers = {
            'X-Ig-App-Id': '936619743392459' }
        self.s = Session()

    
    def getCsrf(self):
        return self.s.get('https://i.instagram.com/api/v1/accounts/login/', {
            'User-Agent': 'Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)' }, **('headers',)).cookies['csrftoken']

    
    def getID(self, username):
        return self.s.get(f'''https://www.instagram.com/api/v1/users/web_profile_info/?username={username}''', {
            'x-ig-app-id': '936619743392459' }, {
            'username': username },('headers', 'data')).json()['data']['user']['id']

    
    def getContext(self):
        self.headers['X-Csrftoken'] = self.getCsrf()
        id = self.getID(self.username)
        return (self.s.post(self.url, self.headers, {
            'container_module': 'profilePage',
            'entry_point': 1,
            'location': 2,
            'object_id': id,
            'object_type': 5,
            'frx_prompt_request_type': 1 }, self.cookies,('headers', 'data', 'cookies')).json()['response']['context'], self.headers['X-Csrftoken'])

    
    def reportW(self):
        (context, csrf) = self.getContext()
        self.headers['X-Csrftoken'] = csrf
        count = 0
        system('cls' if name == 'nt' else 'clear')
        response = self.s.post(self.url, {
            'container_module': 'profilePage',
            'entry_point': 1,
            'location': 2,
            'context': context,
            'object_id': 3,
            'object_type': 5,
            'selected_tag_types': '["ig_user_impersonation_me"]',
            'action_type': 2,
            'frx_prompt_request_type': 2 }, self.headers, self.cookies, ('data', 'headers', 'cookies')).json()['status']
        if response != 'ok':
            print('- False Report | Report Count : ' + str(count))
         
        count += 1
        print('- True Report | Report Count : ' + str(count))



class Login:
    
    def __init__(self, username, password, sessionid = (None, None, None)):
        self.password = password
        self.username = username
        self.sessionid = sessionid
        self.url = 'https://i.instagram.com/api/v1/accounts/login/'
        self.headers = {
            'User-Agent': 'Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)',
            'Content-Type': 'application/x-www-form-urlencoded' }
        self.r = Session()

    
    def csrfToken(self):
        return self.r.get(self.url, self.headers,('headers',)).cookies['csrftoken']

    
    def sessionID(self):
        response = self.r.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', {
            'User-Agent': 'Instagram 100.0.0.17.129 Android (28/9; 320dpi; 720x1422; HUAWEI; MRD-LX1F; HWMRD-M1; mt6761; ar_EG; 16147866)',
            'Cookie': f'''csrftoken={md5(str(time()).encode()).hexdigest()}; sessionid={self.sessionid};''' },('headers',))
        if response.json()['status'] != 'ok':
            system('cls' if name == 'nt' else 'clear')
            Login(input('- Bad SessionID\n- Enter SessionID : '), None, None, **('sessionid', 'username', 'password')).sessionID()
        return True

    
def account(self):
        csrf = self.csrfToken()
        fi = self.r.post(self.url, self.headers, f'''signed_body=fd5f359e5560870ec4cdc326850186a0ebc0033465fdd7477d727e6bae6d575e.{quote(dumps({
            '_csrftoken': csrf,
            'adid': 'bbe5bcdb-b1e3-4815-9e3b-9265c0740970',
            'country_codes': [
                {
                    'country_code': '964',
                    'source': [
                        'default'] }],
            'device_id': 'android-',
            'google_tokens': '[]',
            'guid': '064020d6-330c-471d-a7b2-fc1774dc7122',
            'login_attempt_count': 0,
            'password': self.password,
            'phone_id': '824595cb-7bf9-4b40-8075-685df82e23cc',
            'username': self.username }))}&ig_sig_key_version=4''',('headers', 'data'))
        if 'sessionid' in fi.cookies.get_dict().keys():
            return fi.cookies['sessionid']
        None(fi.json()['message'])
        sleep(3)
        system('cls' if name == 'nt' else 'clear')
        Login(input('- Enter Username : '), input('- Enter Password : '),('username', 'password')).account()



def runCode():
    print('1 - Login From SessionID\n2 - Login From Account')
    choice = input('- ? ')
    system('cls' if name == 'nt' else 'clear')
    if choice == '2':
        client = Login(input('- Enter Username : '), input('- Enter Password : '), None,('username', 'password', 'sessionid')).account()
    elif choice == '1':
        client = input('- Enter SessionID : ')
        client = Login('sessionid', 'username', 'password').sessionID()
    elif name == 'nt':
        pass
    
    os.system('clear')
    runCode()
    print('\n- Done Login : ' + str(client))
    sleep(2)
    if 1 == 1:
        system('cls' if name == 'nt' else 'clear')
        username = input('- Enter Username Targrt : ')
        edit(username, client,('username', 'sessionid')).editAccount()
        report(client, username,('sessionid', 'username')).reportW()

if __name__ == '__main__':
    runCode()



